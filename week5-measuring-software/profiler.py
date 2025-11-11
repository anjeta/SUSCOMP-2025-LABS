#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 12:32:22 2025

@author: anetakartali
"""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import platform
import psutil
import re
import shutil
import subprocess
import sys
import time
import tempfile


class CrossPlatformPowerProfiler:
    def __init__(self):
        self.system = platform.system().lower()
        self.is_intel = "intel" in platform.processor().lower() or "intel" in platform.uname().machine.lower()

    def profile(self, command, duration=None):
        if self.system == "linux":
            return self._profile_linux(command)
        elif self.system == "windows":
            raise NotImplementedError(f"Unsupported OS: {self.system}")
            # return self._profile_windows(command, duration)
        elif self.system == "darwin":  # macOS
            return self._profile_macos(command, duration)
        else:
            raise NotImplementedError(f"Unsupported OS: {self.system}")

    # ------------------- LINUX -------------------
    def _profile_linux(self, command):
        rapl_path = Path("/sys/class/powercap/intel-rapl")
        supports_rapl = rapl_path.exists()
        
        # Initial readings
        start_time = time.perf_counter_ns()
        start_cpu_times = psutil.cpu_times()
        start_energy = self._read_rapl(rapl_path) if supports_rapl else {}
        
        # Get initial CPU frequency
        # start_freq = psutil.cpu_freq(percpu=True) if hasattr(psutil, 'cpu_freq') else None
        
        # Execute command
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Final readings
        end_time = time.perf_counter_ns()
        end_cpu_times = psutil.cpu_times()
        end_energy = self._read_rapl(rapl_path) if supports_rapl else {}
        # end_freq = psutil.cpu_freq(percpu=True) if hasattr(psutil, 'cpu_freq') else None
        
        # Calculate metrics
        execution_time_ns = end_time - start_time
        execution_time_ms = execution_time_ns / 1_000_000
        
        # RAPL energy calculations
        energy_usage = {}
        for k in start_energy:
            diff = end_energy[k] - start_energy[k]
            energy_usage[k] = diff / 1_000_000  # microjoules to joules
        
        # CPU utilization
        cpu_user = end_cpu_times.user - start_cpu_times.user
        cpu_system = end_cpu_times.system - start_cpu_times.system

        return {
            "os": "linux",
            "command": command,
            'timestamp': datetime.now().isoformat(),
            "execution_time_s": (end_time - start_time) / 1e9,
            "execution_time_ms": execution_time_ms,
            "execution_time_ns": execution_time_ns,
            "energy_usage_joules": energy_usage,
            "cpu_time_user": cpu_user,
            "cpu_time_system": cpu_system,
            "stdout": process.stdout,
            "stderr": process.stderr,
            "return_code": process.returncode,
            "rapl_supported": supports_rapl
        }

    def _read_rapl(self, base):
        data = {}
        for p in base.rglob("energy_uj"):
            try:
                data[str(p.parent.name)] = int(Path(p).read_text().strip())
            except:
                pass
        return data

    # ------------------- macOS -------------------
    def _profile_macos(self, command, duration=None):
        # Prepare power_samples list
        cpu_power_samples = []
        gpu_power_samples = []
        
        # Initial readings
        start_time = time.perf_counter_ns()
        start_cpu_times = psutil.cpu_times()
        
        # Get initial CPU frequency
        # start_freq = psutil.cpu_freq(percpu=True) if hasattr(psutil, 'cpu_freq') else None
    
        # Execute command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
        # Detect powermetrics command
        power_proc = None
        power_cmd = self._detect_powermetrics()
        if power_cmd:
            try:
                power_proc = subprocess.Popen(power_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            except Exception as e:
                print(f"Failed to start powermetrics: {e}", file=sys.stderr)
                power_proc = None
    
        # Read powermetrics output in real time
        if power_proc:
            while True:
                if power_proc.stdout is None:
                    break
                line = power_proc.stdout.readline()
                if not line:
                    # No new line; check if process finished
                    if process.poll() is not None:
                        break
                    continue
                # Parse CPU Power in Milliwatts
                m = re.search(r"CPU Power:\s+([\d\.]+)\s*mW", line)
                if m:
                    cpu_power_samples.append(float(m.group(1)) / 1000)
                m = re.search(r"GPU Power:\s+([\d\.]+)\s*mW", line)
                if m:
                    gpu_power_samples.append(float(m.group(1)) / 1000)
                # Exit if target process finished
                if process.poll() is not None:
                    break
    
        # Wait for target process to finish
        stdout, stderr = process.communicate()
    
        # Terminate powermetrics safely
        if power_proc:
            power_proc.terminate()
            power_proc.wait()
            
        # Final readings
        end_time = time.perf_counter_ns()
        end_cpu_times = psutil.cpu_times()
        # end_freq = psutil.cpu_freq(percpu=True) if hasattr(psutil, 'cpu_freq') else None
        
        # Calculate metrics
        execution_time_ns = end_time - start_time
        execution_time_ms = execution_time_ns / 1_000_000
        execution_time_s = execution_time_ns / 1_000_000_000
    
        # Compute average power and total energy in Joules
        cpu_avg_power = sum(cpu_power_samples) / len(cpu_power_samples) if cpu_power_samples else 0
        cpu_total_energy = cpu_avg_power * execution_time_s  # Joules = Watts * seconds
        
        gpu_avg_power = sum(gpu_power_samples) / len(gpu_power_samples) if gpu_power_samples else 0
        gpu_total_energy = gpu_avg_power * execution_time_s  # Joules = Watts * seconds
    
        # CPU utilization
        cpu_user = end_cpu_times.user - start_cpu_times.user
        cpu_system = end_cpu_times.system - start_cpu_times.system
    
        return {
            "os": "macos",
            "command": command,
            "timestamp": datetime.now().isoformat(),
            "execution_time_s": execution_time_s,
            "execution_time_ms": execution_time_ms,
            "execution_time_ns": execution_time_ns,
            "cpu_energy_usage_joules": cpu_total_energy,
            "gpu_energy_usage_joules": gpu_total_energy,
            "cpu_time_user": cpu_user,
            "cpu_time_system": cpu_system,
            "stdout": stdout,
            "stderr": stderr,
            "return_code": process.returncode,
            "rapl_supported": False
        }
    
    def _detect_powermetrics(self):
        """Check whether powermetrics is available and determine the right samplers."""
        if platform.system() != "Darwin":
            return None
    
        path = shutil.which("powermetrics")
        if not path:
            return None
    
        arch = platform.machine().lower()
        if "arm" in arch or "apple" in platform.platform().lower():
            # Apple Silicon
            samplers = "cpu_power,gpu_power,thermal"
        else:
            # Intel Macs
            samplers = "smc"
    
        return ["sudo", "powermetrics", "--samplers", samplers, "-n", "2", "-i", "1000"]


def format_results(results):
    """Format profiling results for display"""
    output = []
    output.append(f"\nProfile results for: {results['command']}")
    output.append(f"Timestamp: {results['timestamp']}")
    output.append("\nPerformance Metrics:")
    output.append(f"Execution time: {results['execution_time_ms']:.3f} ms ({results['execution_time_ns']} ns)")
    output.append(f"CPU time (user): {results['cpu_time_user']:.3f} seconds")
    output.append(f"CPU time (system): {results['cpu_time_system']:.3f} seconds")
    
    if results['rapl_supported']:
        output.append("\nCPU Energy Usage (RAPL):")
        for domain, energy in results['energy_usage_joules'].items():
            output.append(f"  {domain}: {energy} J\n")
    else:
        output.append(f"\nCPU Energy Usage: {results['cpu_energy_usage_joules']} J")
        output.append(f"GPU Energy Usage: {results['gpu_energy_usage_joules']} J\n")
    
    if results['return_code'] != 0:
        output.append(f"Warning: Command returned non-zero exit code: {results['return_code']}\n")
    
    # Print the program Output
    # if results['stdout']:
    #     output.append(f"\nStandard output:\n{results['stdout']}")
    # if results['stderr']:
    #     output.append(f"\nStandard error:\n{results['stderr']}")
        
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Profile execution time and power usage of a command',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
          %(prog)s "python3 script.py"
          %(prog)s "ls -la"
          %(prog)s "sleep 5"
        """
    )
    
    parser.add_argument(
        'command',
        help='Command to profile (use quotes for commands with arguments)',
        type=str,
        nargs=argparse.REMAINDER
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output file for results (default: stdout)',
        type=argparse.FileType('w'),
        default=sys.stdout
    )
    
    parser.add_argument(
        '--json',
        help='Output results in JSON format',
        action='store_true'
    )

    args = parser.parse_args()

    if not args.command:
        parser.error("No command provided to profile")
        
    # Reconstruct the command string
    command = ' '.join(args.command)
    
    try:
        profiler = CrossPlatformPowerProfiler()
        results = profiler.profile(command)
        
        if args.json:
            # Convert results to JSON-serializable format
            json_results = {k: v for k, v in results.items() if isinstance(v, (dict, list, str, int, float, bool, type(None)))}
            print(json.dumps(json_results, indent=2), file=args.output)
        else:
            formatted_results = format_results(results)
            print(formatted_results, file=args.output)
        
        if args.output is not sys.stdout:
            args.output.close()
            print(f"Results written to {args.output.name}")
            
    except KeyboardInterrupt:
        print("\nProfiling interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error during profiling: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()