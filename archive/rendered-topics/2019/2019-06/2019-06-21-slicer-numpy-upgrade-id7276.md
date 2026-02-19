---
topic_id: 7276
title: "Slicer Numpy Upgrade"
date: 2019-06-21
url: https://discourse.slicer.org/t/7276
---

# Slicer numpy upgrade

**Topic ID**: 7276
**Date**: 2019-06-21
**URL**: https://discourse.slicer.org/t/slicer-numpy-upgrade/7276

---

## Post #1 by @jamesobutler (2019-06-21 12:26 UTC)

<p>I was playing around with the ability to pip install packages into Slicer nightly and attempted a upgrade of Numpy from 1.16.2 to 1.16.4 which resulted in some errors (seen below). This got me thinking about if numpy built and installed as part of the Slicer build process could be simplified to a pip install from a wheel instead of building from source. It is currently built from a Slicer fork (<a href="https://github.com/Slicer/numpy/tree/slicer-v1.16.2-2019-02-26-0eeb158ea" rel="nofollow noopener">Slicer/numpy v1.16.2-2019-02-26-0eeb158ea</a>) with a few custom commits to help with building.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.pip_install("numpy -U")
Collecting numpy
  Using cached https://files.pythonhosted.org/packages/20/ed/e036d31a9b2c750f270cbb1cfc1c0f94ac78ae504eea7eec3267be4e294a/numpy-1.16.4-cp36-cp36m-win_amd64.whl
dicomweb-client 0.11.0 requires pillow&gt;=5.0, which is not installed.
Installing collected packages: numpy
  Found existing installation: numpy 1.16.2
    Uninstalling numpy-1.16.2:
      Successfully uninstalled numpy-1.16.2
  The script f2py.exe is installed in 'C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 4.11.0-2019-06-20\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Could not install packages due to an EnvironmentError: [WinError 5] Access is denied: 'c:\\users\\jamesbutler\\appdata\\local\\na-mic\\slicer 4.11.0-2019-06-20\\lib\\python\\lib\\site-packages\\~umpy-1.16.2-py3.6-win-amd64.egg\\numpy\\core\\_multiarray_tests.cp36-win_amd64.pyd'
Consider using the `--user` option or check the permissions.

Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 4.11.0-2019-06-20\bin\Python\slicer\util.py", line 1714, in pip_install
    logProcessOutput(proc)
  File "C:\Users\JamesButler\AppData\Local\NA-MIC\Slicer 4.11.0-2019-06-20\bin\Python\slicer\util.py", line 1678, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/JamesButler/AppData/Local/NA-MIC/Slicer 4.11.0-2019-06-20/bin/../bin/PythonSlicer.exe', '-m', 'pip', 'install', 'numpy', '-U']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @lassoan (2019-06-21 13:11 UTC)

<p>When you start Slicer, various modules already import numpy, so you cannot upgrade it (you’ll get access denied errors). You need to run <code>slicer.util.pip_install</code> from PythonSlicer:</p>
<pre><code class="lang-auto">from slicer import util
util.pip_install("numpy -U")
</code></pre>
<p>or even simpler, run pip directly from the command line:</p>
<pre><code>PythonSlicer.exe -m pip install numpy -U</code></pre>

---

## Post #3 by @jamesobutler (2019-06-21 14:13 UTC)

<p>Ok got it. I didn’t think of other modules having already imported it.</p>

---
