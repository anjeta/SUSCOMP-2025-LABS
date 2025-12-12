# Measuring Cloud Emissions

The goal for this lab excercise is to learn how to measure energy usage and understand hidden emissions when running software in a cloud environment such as Google Colab. On a virtual machine (VM), like the one our Colab notebook will be running on, you do not have access to low-level hardware counters such as Intel RAPL. Instead, we will rely on software-level measurements and approximate energy uage for CPU, GPU, and networking. Because cloud hardware is virtualised, these measurements we will take are estimates, and not exact ground-truth values. 

## How to make measurements on Colab

#### GPU measurements

Google Colab provides real-time GPU power readings using:

```
nvidia-smi --query-gpu=power.draw
```

This returns instantaneous power in watts. We will sample this repeatedly and integrate over time to obtain the energy consumption in kWh.

#### CPU measurements

On the other hand, Colab does not expose CPU power, so we will estimate CPU energy using CPU utilisation and `psutil.cpu_percent()`. We will also estimate CPU power consumption based on the allocated CPU model.

## Taking good measurements

1. Isolation - Avoid performing tasks that download data inside the measurement window. Uploads, downloads, and print-heavy output will skew energy readings.

2. Overhead - The logger runs in a Python thread. This adds a small but constant overhead, so repeat your tests and take the average.

3. What we miss -  Colab does not expose DRAM power, NVMe/SSD power, and CPU package components are not visible via utilisation. Take this into account when writing your report.

4. Repeating tests - Run each test 3 times, record all runs, report mean and standard deviation.

## Task

Time available: 1.5 hours.

Make sure you have an up to date copy of your coursework repo available.  In the '`week9`' folder create a new markdown document called `username-week9-labnotes.md`.

Upload Lab_09.ipynb from this repository to Google Colab. Run the script following the instructions and document your results in `username-week9-labnotes.md`.
