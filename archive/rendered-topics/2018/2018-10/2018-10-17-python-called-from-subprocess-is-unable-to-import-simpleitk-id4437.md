---
topic_id: 4437
title: "Python Called From Subprocess Is Unable To Import Simpleitk"
date: 2018-10-17
url: https://discourse.slicer.org/t/4437
---

# Python -called from subprocess- is unable to import SimpleITK

**Topic ID**: 4437
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/python-called-from-subprocess-is-unable-to-import-simpleitk/4437

---

## Post #1 by @abertelsen (2018-10-17 15:01 UTC)

<p>Hello everybody,</p>
<p>I want to call a python module from Slicer, but I need to call it through the <em>subprocess</em> module and not directly from Slicer’s Python environment. This is because my module uses scipy, which is not available in Slicer’s Pyhton (my module also depends on SimpleITK, which also brings a problem as you may see below).</p>
<p>I have tried to call my module using <code>subprocess.check_call</code> but it fails as scipy is not avaiable. In fact, a single call to <code>import scipy</code> fails:</p>
<pre><code>&gt;&gt;&gt; import subprocess
&gt;&gt;&gt; python_path = 'C:/Users/abertelsen/AppData/Local/Continuum/Anaconda2/python.exe'
&gt;&gt;&gt; subprocess.check_call([python_path, '-c', 'import scipy'])
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Slicer 4.8.1\lib\Python\Lib\subprocess.py", line 219, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
CalledProcessError: Command '['C:/Users/abertelsen/AppData/Local/Continuum/Anaconda2/python.exe', '-c', 'import scipy']' returned non-zero exit status 1
</code></pre>
<p>I though that the problem may be related to the environment variables, so I added the <code>-E</code> option to python -which forces Python to ignore all environment variables that begin with ‘PYTHON*’- and it seemed to work:</p>
<pre><code>&gt;&gt;&gt; subprocess.check_call([python_path, '-E', '-c', 'import scipy'])
0
</code></pre>
<p>And now comes the ‘funny’ part: adding the <code>-E</code> option prevents the import of SimpleITK</p>
<pre><code>&gt;&gt;&gt; subprocess.check_call([python_path, '-E', '-c', 'import SimpleITK'])
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Slicer 4.8.1\lib\Python\Lib\subprocess.py", line 186, in check_call
    raise CalledProcessError(retcode, cmd)
CalledProcessError: Command '['C:/Users/abertelsen/AppData/Local/Continuum/Anaconda2/python.exe', '-E', '-c', 'import SimpleITK']' returned non-zero exit status -1073740777
</code></pre>
<p>…but removing the <code>-E</code> option solves the problem</p>
<pre><code>&gt;&gt;&gt; subprocess.check_call([python_path, '-c', 'import SimpleITK'])
0
</code></pre>
<p>Therefore, if I add the <code>-E</code> option I am unable to import SimpleITK and, if I remove it, I become unable to import scipy. In both cases, I am unable to run my script from Slicer <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>My Python environment is Anaconda2 (with Python 2.7.13, which is the same Python version that Slicer 4.8.1 uses). I do not get the same problem calling the commands above from the Anaconda Prompt: in fact, all cases above work when called from there.</p>
<p>Some info on my environment:</p>
<ul>
<li>Slicer 4.8.1 (with Python 2.7.13)</li>
<li>Anaconda2 4.4.0 64-bits (with Python 2.7.13)</li>
<li>Windows 10 (64 bits)</li>
</ul>
<p>Any help would be greatly appreciated!</p>
<p>Best wishes,<br>
Álvaro B.</p>
<p><strong>PS</strong> I have noticed that Slicer’s Python has been compiled with MSC v.1800, whereas Anaconda’s Python has been compiled with MSC v.1500. Do you believe that the problem may be related to the compiler? I doubt it, but I wanted to add this point.</p>

---

## Post #2 by @lassoan (2018-10-17 15:04 UTC)

<p>You can use <code>slicer.util.startupEnvironment()</code> to get an unmodified system environment. See details in this post: <a href="https://discourse.slicer.org/t/subprocess-call-in-python-interpreter-results-in-memory-corruption/919/17">Subprocess call in Python interpreter results in memory corruption</a></p>

---

## Post #3 by @abertelsen (2018-10-17 15:24 UTC)

<p>Using <code>slicer.util.startupEnvironment</code> still produces an error</p>
<p><code>subprocess.check_output([python_path, '-c', 'import SimpleITK'], env=slicer.util.startupEnvironment())</code></p>
<p><code>Traceback (most recent call last): File "&lt;console&gt;", line 1, in &lt;module&gt; File "C:\Program Files\Slicer 4.8.1\lib\Python\Lib\subprocess.py", line 212, in check_output process = Popen(stdout=PIPE, *popenargs, **kwargs) File "C:\Program Files\Slicer 4.8.1\lib\Python\Lib\subprocess.py", line 390, in __init__ errread, errwrite) File "C:\Program Files\Slicer 4.8.1\lib\Python\Lib\subprocess.py", line 640, in _execute_child startupinfo) TypeError: environment can only contain strings</code></p>
<p>I get the same error calling Python with or without the <code>-E</code> option.</p>

---

## Post #4 by @ihnorton (2018-10-17 15:51 UTC)

<p>If you installed SimpleITK with pip rather than conda, then it might rely on something being in PATH.</p>
<p>A hacky quick-fix for the <code>TypeError</code> might be passing a modified environment, <code>env = {str(k): str(v) for k,v in slicer.util.startupEnvironment().items()}</code>.</p>

---

## Post #5 by @lassoan (2018-10-17 17:41 UTC)

<p>I just see now that you use Slicer-4.8.1. This issue has been fixed in recent Slicer-4.9.x versions.</p>

---

## Post #6 by @abertelsen (2018-10-18 07:28 UTC)

<p>Calling <code>subprocess.check_call</code> using the modified <code>env</code> did the trick. Thank you Andras and Isaiah for your replies!</p>
<p>Best wishes,<br>
Álvaro B.</p>

---

## Post #7 by @lassoan (2018-10-18 11:46 UTC)

<p>Forced conversion to string was implemented in nightly (Slicer-4.9.x) version several months ago. So, any recent nightly builds should work as is.</p>

---
