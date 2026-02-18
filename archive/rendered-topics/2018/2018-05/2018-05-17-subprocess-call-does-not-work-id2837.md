# Subprocess.call does not work!

**Topic ID**: 2837
**Date**: 2018-05-17
**URL**: https://discourse.slicer.org/t/subprocess-call-does-not-work/2837

---

## Post #1 by @wpgao (2018-05-17 10:00 UTC)

<p>Hi all,</p>
<p>I try to use subprocess.call to run an external application in the python interactor of 3D Slicer but failed! Error message is “terminate called after throwing an instance of ‘H5::DataSpaceIException’”<br>
However, when I run the python in the terminal and input the same command, the application works!<br>
Is there any difference between the two pythons?<br>
Thanks very much!</p>
<p>Operating system: Centos 7<br>
Slicer version: 4.8<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @ihnorton (2018-05-17 14:33 UTC)

<aside class="quote no-group" data-username="wpgao" data-post="1" data-topic="2837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>Is there any difference between the two pythons?</p>
</blockquote>
</aside>
<p>Yes, Slicer’s python is <a href="https://discourse.slicer.org/t/access-slicer-modules-and-libraries-in-pycharm/2765/2">embedded</a>.</p>
<p><code>subprocess.call</code> should generally work, however, it will block Slicer (GUI will freeze) until the call completes (you can use <code>Popen</code> or Slicer’s CLI infrastructure instead for asynchronous calls). I just tried <code>subprocess.call(['sleep', '10'])</code> on linux with a recent nightly, and it worked fine.</p>
<p>Please show a minimal example if you can – maybe someone will notice a problem.</p>

---

## Post #3 by @lassoan (2018-05-17 16:52 UTC)

<p>The crash is probably because your application tries to use Slicer’s ITK, VTK, HDF5, etc. libraries. If you want to use the default system environment, you can retrieve it using <code>slicer.util.startupEnvironment()</code>.</p>
<pre><code>from subprocess import check_output
check_output(
  ["/usr/bin/python3", "-c", "print('hola')"], 
  env=slicer.util.startupEnvironment())
'hola\n'
</code></pre>
<p>See details in this post: <a href="https://discourse.slicer.org/t/subprocess-call-in-python-interpreter-results-in-memory-corruption/919/17">Subprocess call in Python interpreter results in memory corruption</a></p>

---

## Post #4 by @wpgao (2018-05-18 10:51 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Thanks for your reply. I just try to call a function of ANTs for image registration!<br>
<a class="mention" href="/u/lassoan">@lassoan</a> Thanks! It works according to your suggestion. In addition, shell should be set True. Otherwise, it does not work. I don’t know why and there is no any information output to the terminal!</p>

---

## Post #5 by @ihnorton (2018-09-06 04:31 UTC)

<p>A post was split to a new topic: <a href="/t/calling-c-from-python/3998">Calling C++ from Python</a></p>

---

## Post #6 by @Saima (2019-07-08 08:53 UTC)

<p>Hi andras,<br>
I am extactly doing the same but getting error.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Slicer 4.10.2\lib\Python\Lib\subprocess.py", line 212, in check_output
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
  File "C:\Program Files\Slicer 4.10.2\lib\Python\Lib\subprocess.py", line 390, in __init__
    errread, errwrite)
  File "C:\Program Files\Slicer 4.10.2\lib\Python\Lib\subprocess.py", line 640, in _execute_child
    startupinfo)
WindowsError: [Error 2] The system cannot find the file specified
</code></pre>
<p>Would you please suggest what am I doing wrong??</p>

---

## Post #7 by @jcfr (2019-07-08 13:46 UTC)

<p>The message indicates that the path to the executable is incorrect. So that we can better understand the problem, could you share the code leading to this exception ?</p>

---

## Post #8 by @Saima (2019-07-09 06:56 UTC)

<p>I am simply checking it with print statement.</p>
<pre><code class="lang-python">command_line = [r"F:\anaconda3\python3.exe","-c","print('helo')"]
from subprocess import check_output
command_result = check_output(command_line, env = slicer.util.startupEnvironment())
</code></pre>

---

## Post #9 by @Saima (2019-07-10 07:24 UTC)

<p>Hi,<br>
Why am I unable to run the code below</p>
<pre><code class="lang-python">command_line=["F:\anaconda3\python.exe","-c", "print('hola')"]
from subprocess import run
command_result = run(command_line, env =
slicer.util.startupEnvironment())
print(command_result)
</code></pre>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "F:\Slicer 4.11.0-2019-07-06\bin\Python\slicer\ScriptedLoadableModule.py", line 196, in onReload
    slicer.util.reloadScriptedModule(self.moduleName)
  File "F:\Slicer 4.11.0-2019-07-06\bin\Python\slicer\util.py", line 769, in reloadScriptedModule
    moduleName, fp, filePath, ('.py', 'r', imp.PY_SOURCE))
  File "F:\Slicer 4.11.0-2019-07-06\lib\Python\Lib\imp.py", line 235, in load_module
    return load_source(name, filename, file)
  File "F:\Slicer 4.11.0-2019-07-06\lib\Python\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "F:/Slicer 4.11.0-2019-07-06/subprocess/subprocess/subprocess.py", line 134, in &lt;module&gt;
    slicer.util.startupEnvironment())
  File "F:\Slicer 4.11.0-2019-07-06\lib\Python\Lib\subprocess.py", line 403, in run
    with Popen(*popenargs, **kwargs) as process:
  File "F:\Slicer 4.11.0-2019-07-06\lib\Python\Lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "F:\Slicer 4.11.0-2019-07-06\lib\Python\Lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] The system cannot find the file specified
</code></pre>

---

## Post #10 by @jcfr (2019-07-10 07:45 UTC)

<p>You should do this instead:</p>
<pre><code class="lang-auto">command_line=["F:/anaconda3/python.exe", "-c", "print('hola')"]
from subprocess import run
command_result = run(command_line, env=slicer.util.startupEnvironment())
print(command_result)
</code></pre>

---

## Post #11 by @Saima (2019-07-11 13:16 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="10" data-topic="2837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>command_line=[“F:/anaconda3/python.exe”, “-c”, “print(‘hola’)”] from subprocess import run command_result = run(command_line, env=slicer.util.startupEnvironment()) print(command_result)</p>
</blockquote>
</aside>
<p>the error remain the same</p>
<p>I am unable to understand.</p>
<p>It could not find the file.</p>

---

## Post #12 by @jamesobutler (2019-07-11 13:41 UTC)

<p><a class="mention" href="/u/saima">@Saima</a> I get the error you are getting when the python path that you are targeting doesn’t actually exist.</p>
<p>Can you confirm that  <code>"F:\anaconda3\python.exe"</code> actually exists?</p>

---

## Post #13 by @Saima (2019-07-11 13:45 UTC)

<p>yes I did installation again and the path was changed. I didnt check updated the path. now its running.</p>
<p>Thanks all</p>

---

## Post #14 by @lassoan (2019-07-11 14:25 UTC)

<p>FYI, since backslash (<code>\</code>) is an escape character in Python, you cannot simply use it in a string literal in Python.</p>
<p>The easiest is to indicate that you specify a raw string by prepending an <code>r</code> character before the string. This is correct:</p>
<pre><code>somePath = r"F:\someFolder\python.exe"
</code></pre>
<p>If you need to use a regular string then backslash can be entered by typing double-backslash. This is correct:</p>
<pre><code>somePath = "F:\\someFolder\\python.exe"
</code></pre>
<p>You may also use Unix-type separators. This is correct:</p>
<pre><code>somePath = "F:/someFolder/python.exe"</code></pre>

---
