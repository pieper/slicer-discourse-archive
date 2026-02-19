---
topic_id: 8409
title: "Subprocess Using Conda Python"
date: 2019-09-12
url: https://discourse.slicer.org/t/8409
---

# Subprocess using conda python

**Topic ID**: 8409
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/subprocess-using-conda-python/8409

---

## Post #1 by @ghnguyen (2019-09-12 18:29 UTC)

<p>Hi,<br>
I’m trying to use subprocess to get the output of another script running in conda environment since I want other python packages there.</p>
<blockquote>
<p>subprocess.check_call([“C:/Users/gnguyen/Anaconda/envs/pytest/python.exe”, “-c”, “from skimage import io”],env=slicer.util.startupEnvironment())</p>
</blockquote>
<p>This returns CalledProcessError: non-zero exit status 1. If I drop the -c and use a script, same thing happens. However, simple statements like “-c”, “print (‘hola’)” work fine and gives exit status 0. I followed the documentation as well as this thread <a href="https://discourse.slicer.org/t/interacting-with-external-python/4897">https://discourse.slicer.org/t/interacting-with-external-python/4897</a> but could not resolve the problem. My conda environment has all the packages I need. I was searching on the web and found <a href="https://www.scivision.dev/python-calling-python-subprocess/" rel="noopener nofollow ugc">this</a> but not sure if that helps here. Is there anything I’m missing or how should I work around this problem? Thanks.<br>
I’m using Windows 10 (64 bit) and I have tested on both Slicer 4.10.2 and 4.11.0 (version on 09/12).</p>

---

## Post #2 by @lassoan (2019-09-12 21:09 UTC)

<p>It works well for me. Run it <code>subprocess.check_output</code> to see the error message, probably it is some trivial error (using wrong environment, scipy not installed, etc.).</p>
<p>Note that if you use recent Slicer Preview version then you can install skimage by <code>pip_install('scipy scikit-image')</code> and use it in Slicer. You can even run a Python script as a module in Slicer (with GUI generated from an XML file) - see example here: <a href="https://github.com/lassoan/SlicerPythonCLIExample" rel="nofollow noopener">https://github.com/lassoan/SlicerPythonCLIExample</a>.</p>

---

## Post #3 by @ghnguyen (2019-09-13 15:10 UTC)

<p>Thanks for the suggestion, I installed sciki-image and can keep working on my project for now. Pip installing scikit image in older versions is broken but you’re correct, the recent versions works fine.<br>
I was looking for a way to use this <a href="https://pypi.org/project/pyimagej/" rel="nofollow noopener">https://pypi.org/project/pyimagej/</a> in Slicer as well but could not do it because of pyjnius installation kept producing error when pip_install. Hence I resorted to the subprocess route which still is not working now as I described.</p>

---

## Post #4 by @lassoan (2019-09-13 15:11 UTC)

<p>What is the output if you use <code>subprocess.check_output</code>?</p>

---

## Post #5 by @ghnguyen (2019-09-13 15:33 UTC)

<blockquote>
<p>subprocess.check_output([“C:/Users/gnguyen/Anaconda/envs/imagej/python.exe”, “C:/Users/gnguyen/Desktop/3dSlicerExtension/Macro_Test/pyimagej.py”], env=slicer.util.startupEnvironment())</p>
</blockquote>
<p>results in this:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\gnguyen\AppData\Local\NA-MIC\Slicer 4.11.0-2019-09-11\lib\Python\Lib\subprocess.py”, line 336, in check_output<br>
**kwargs).stdout<br>
File “C:\Users\gnguyen\AppData\Local\NA-MIC\Slicer 4.11.0-2019-09-11\lib\Python\Lib\subprocess.py”, line 418, in run<br>
output=stdout, stderr=stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/gnguyen/Anaconda/envs/imagej/python.exe’, ‘C:/Users/gnguyen/Desktop/3dSlicerExtension/Macro_Test/pyimagej.py’]’ returned non-zero exit status 120.</p>
</blockquote>
<p>Catching the error with except clause would give the same thing, error.output is a blank string and error.returncode is 120.</p>

---

## Post #6 by @lassoan (2019-09-13 16:42 UTC)

<p>If you use virtual environment then you must activate it before you can use it (if you installed non-native Python packages, such as pyimagej). Simply running <code>python.exe</code> executable is expected to fail with DLL loading errors.</p>
<p>You need to use <code>conda run</code> or some other techniques to instruct conda to run your script in a specific virtual environment. All these have nothing to do with Slicer but general anaconda behavior, so you should be able to find help and examples on the web.</p>
<p>By the way, this whole pyimagej idea of wrapping Java with a Python interface is quite messy. Probably you would be better off with using equivalent Python packages.</p>

---

## Post #7 by @ghnguyen (2019-09-13 16:56 UTC)

<p>I agree, our collaborators used that so I was just trying to be consistent but now I think scikit image is more than enough to recreate the results. Thanks Andras!</p>

---
