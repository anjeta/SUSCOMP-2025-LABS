# Measuring Software Energy Consumption

The goal for this lab excercise is to learn how to take energy measurements associated with running specific software and to explore the effect of offloading computation from the CPU to the GPU. We’ll be indirectly using the Intel RAPL for Linux and Power Metrics for MacOS to report energy consumtion from the CPU. Unfortunately, this will not work on Windows machines so please use the lab machine or pair up with someone who has a Linux/MacOS on their personal laptop machine.

Further note that you will be able to run GPU test only on the lab machine or if your machine has an Intel graphics. Keep in mind that Intel graphics has a considerably lower power draw than a dedicated GPU found in most gaming machines and high end AI or graphics machines. Recall, that processors increasingly have other co-processors, such as Intel's NPU, for accelerating operations for machine learning - which also might perform specialist parallel instructions with good compute/energy performance.  *You should keep this in mind when generalising from your findings!*

## Taking good measurements

We will take a snapshot of the energy use of the CPU/GPU from the time we start measuring to the time the task is complete.

1. This could catch any computation going on, not just your code, so we should aim for **isolation**, i.e. trying not to get data that's confounded by other software and hardware running at the same time.
2. Ideally, recognise that the measurement framework may add additional **overhead** (hopefully in this case it should be relatively constant for all tests).
3. Understanding how much is **missed** by what we are able to measure (for example, the scripts we will use measure the CPU/GPU, but not the memory, I/O subsystems or anything else that makes up the total system energy).
4. **Repeatable** and **representative** test selection.  We should run tests more than once and take an average (arithmetic mean) and standard deviation.  We should report each run and the average. Run **each test 5 times**, providing **all** of the readings in your report markdown file.
5. You should do a 'warmup' run before taking your measurements, not least because this task **downloads a large data file at startup**.  Be careful **not to include** the download and data loading time in your benchmark results.  **Take care also to remove or not include the data file in your git repo!**

We're going to use a test which forecasts data points from a [linear regression](https://www.geeksforgeeks.org/ml-linear-regression/) using python for [this task](https://uxlfoundation.github.io/scikit-learn-intelex/latest/samples/linear_regression.html) which utilises the [`scitkit-learn`](https://scikit-learn.org/stable/) package and GPU extension by Intel).

## Understanding Intel RAPL channels

For Linux machines, the profiler script will give you a block of output like this:

```
Performance Metrics:
Execution time: 6402.042 ms (6402042057 ns)
CPU time (user): 16.690 seconds
CPU time (system): 0.680 seconds

CPU Power Usage (RAPL):
  intel-rapl:0: 133020839 µJ (133.021 J)
  intel-rapl:0:0: 123113210 µJ (123.113 J)
  intel-rapl:0:1: 7812 µJ (0.008 J)
```

If you're curious, read about `user` and `system` time in this answer to [this stackoverflow question](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1).

Note that the `intel-rapl:` corresponds to different MSRs (module specific registers) on your Intel processor.  These are normally:

Channel | Value | Meaning
----|----|----
`intel-rapl:0:`| 133020839 µJ (133.021 J)| Overall 'package' energy (all parts of the CPU package, including CPU and GPU)
`intel-rapl:0:0:` | 123113210 µJ (123.113 J) | Channel 0 is the 'CPU cores' part of the package
`intel-rapl:0:1:` | 7812 µJ (0.008 J) | "Normally" the GPU

Note that 0.008 Joules is tiny, so probably more significant in interpreting your results is the difference between the package and CPU channels and estimating 'what is saved' by the GPU by taking workload from the processor between test variants. The energy saved should really be *not just the difference in load*, but *also the reduced execution time*.  **You'll need to take this into account and explain your working out in your markdown report.**

## Task

Time available: 1 hour:

Make sure you have an up to date copy of your coursework repo available.  In the '`week5`' folder create a new markdown document called `username-week5-labnotes.md`.

1. Create and activate a Python environment running the following commands:

	```bash
	conda create -n "suscomp-25" python=3.12.10
	conda activate "suscomp-25"
	```

	or

	```bash
	pyenv install 3.12.10
	pyenv virtualenv 3.12.10 "suscomp-25"
	pyenv activate "suscomp-25"
	```

2. Install the dependencies from [requirements.txt]():

	```bash
	pip install -r requirements.txt
	```bash
	
3. Download the [profiler.py](https://github.com/anjeta/SUSCOMP-2025-LABS/blob/main/week5-measuring-software/profiler.py) script.  This is a python script and **needs to be executable** - you may need to change it's file permissions (to do so, run `chmod u+x profiler.py` in the terminal shell)

4. Download the two test files [test-cpu.py](https://github.com/anjeta/SUSCOMP-2025-LABS/blob/main/week5-measuring-software/test-cpu.py) and [test-gpu.py](https://github.com/anjeta/SUSCOMP-2025-LABS/blob/main/week5-measuring-software/test-gpu.py).  This is the same code, the only difference being that with `test-cpu.py` all the calculation is done on the CPU cores.

5. Run the test case to 'warm up' the system (*load packages and data files for the first time*).

	```bash
	python test-cpu.py
	```
	
6. Run each test case at least 5 times, noting down the test case, energy and time taken for each.  e.g. using:

	```bash
	sudo ./profiler.py "python test-cpu.py"
	```
	**Important note: the profiler.py swallows the output from the task, so it's recommend to run the task to verify it's running correctly, before running under the energy profiler.  Especially, if the task completion time and energy used is suspiciously small!**

7. Document your experiment *in markdown format*, using markdown tables.  Add an *introductory paragraph* on what you plan to measure and your 'method statement' of how you've conducted your tests.  *Take care to explain how you are calculating the energy saved.*

8. For each test case, add a subsection with the goal of the test, *the command line* you've used and a table with the results.

9. The table should have the results of each test run, how much time it took and how many Joules of energy and total Watt/hours. Additionally, calculate the total power consumtion of running each of the scripts in each test run. You can convert Joules to Watts [using a converter](https://www.rapidtables.com/calc/electric/Joule_to_Watt_Calculator.html), or by hand:

   Recall, the power P in watts (W) is equal to the energy E in joules (J), divided by the time period t in seconds (s) - *take care with your units!!*
   
   $$
   P = \frac{E}{t}
   $$

10. Finish the table with the average time taken and standard deviation.  You could use a spreadsheet like excel, or a stats package like R (see [getting started reference](https://education.rstudio.com/learn/beginner/))

11. Add a subsection called `## Reflections` which summarises what you've found, and any personal observations on the number of Watt's associated with the computations.  How much energy was saved by offloading from CPU to GPU and speeding up the task?  If you ran this task for an entire day, week, month or year how many kWh would be used for CPU and GPU variants?

Don't forget to `git add` your new file, `commit` and `push` to the server at least at the end of the task.  **Take care not to add the 'data' folder to your git repository - it contains an enormous data file that you don't need to keep!**  You can remove it with `git rm -r data`.

## Learning outcomes
* You should have an appreciation of how energy varies with CPU vs. GPU computation.
* Reinforcing your expirimental method, i.e. how to take measurements, calculate a difference in energy saved and report them in a systematic way.
* A 'ready reckoning' of the bounds for energy saving due to reducing load on the CPU by shifting workloads to the GPU.
* An appreciation of how efficient GPU cores are for offloading parallel mathematical tasks (e.g. vector matrix operations).

## Starting points

Here are some useful digital resources to help.

- [About Python virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)

<!-- ## Going further

* [https://pawseysc.github.io/sc20-gpu-offloading/](https://pawseysc.github.io/sc20-gpu-offloading/) -->

## Acknowledgement

This lab exercise is made based on the materials from the Sustainable Computing course held by Adrian Friday, a Professor of Computing and Sustainability at Lancaster University.
