# Interacting with external python

**Topic ID**: 4897
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/interacting-with-external-python/4897

---

## Post #1 by @muratmaga (2018-11-27 22:23 UTC)

<p>I am trying to build on this example in:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment</a></p>
<p>This</p>
<pre><code>python_path = "C:/Users/amaga/AppData/Local/Continuum/anaconda3/python"
command_line = [python_path, "-c", "import pyRserve; conn = pyRserve.connect(); print(conn.eval('3 + 5'))"]
from subprocess import check_output
command_result = check_output(command_line, env=slicer.util.startupEnvironment())
print(command_result)
</code></pre>
<p>fails with error.</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File "&lt;console&gt;", line 1, in &lt;module&gt;<br>
File "C:\Program Files\Slicer 4.11.0-2018-11-02\lib\Python\Lib\subprocess.py", line 219, in check_output<br>
raise CalledProcessError(retcode, cmd, output=output)<br>
CalledProcessError: Command ‘[‘C:/Users/amaga/AppData/Local/Continuum/anaconda3/python’, ‘-c’, "import pyRserve; conn = pyRserve.connect(); print(conn.eval(‘3 + 5’))"]’ returned non-zero exit status 120</p>
</blockquote>
<p>But in the interactive python console <strong>import pyRserve; conn = pyRserve.connect(); print(conn.eval(‘3 + 5’))</strong><br>
returns the correct value. So I know Rserve is working.</p>
<p>What is the correct way of passing bunch of commands to the external python in this context?</p>

---

## Post #2 by @jcfr (2018-11-28 07:34 UTC)

<p>After first starting the R server from a separate R interpreter (details <a href="http://www.rforge.net/Rserve/faq.html#start" rel="nofollow noopener">here</a>), I wasn’t able to reproduce the issue.</p>

---

## Post #3 by @muratmaga (2018-11-28 08:09 UTC)

<p>himm,</p>
<p>On a different windows computer, I followed your updated pip install example and issued the command<br>
"“c:\Program Files\Slicer 4.10.0\bin\PythonSlicer.exe” -m pip install pyRserve<br>
as admin.<br>
As far as I can tell, pyRserve installed correctly (although there was a warning about path (truncated output below)</p>
<blockquote>
<p>Successfully built pyRserve<br>
Installing collected packages: attrs, pluggy, scandir, pathlib2, funcsigs, colorama, atomicwrites, more-itertools, py, pytest, pyRserve<br>
The scripts py.test.exe and pytest.exe are installed in ‘C:\Program Files\Slicer 4.10.0\lib\Python\Scripts’ which is not on PATH.<br>
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.<br>
Successfully installed atomicwrites-1.2.1 attrs-18.2.0 colorama-0.4.1 funcsigs-1.0.2 more-itertools-4.3.0 pathlib2-2.3.2 pluggy-0.8.0 py-1.7.0 pyRserve-0.9.1 pytest-4.0.1 scandir-1.9.0</p>
</blockquote>
<p>then I started the Rserve on my local R (3.5.0) and tested its connection with anaconda by issuing</p>
<blockquote>
<p>import pyRserve; conn = pyRserve.connect(); print(conn.eval(‘3 + 5’))</p>
</blockquote>
<p>and got the right result.</p>
<p>then I opened Slicer 4.10, and typed the script example above (path is slightly different on this machine).</p>
<blockquote>
<p>python_path = “C:/Users/murat/anaconda3/python”<br>
command_line = [python_path, “-c”, “import pyRserve; conn = pyRserve.connect(); print(conn.eval(‘3 + 5’))”]<br>
from subprocess import check_output<br>
command_result = check_output(command_line, env=slicer.util.startupEnvironment())<br>
print(command_result)</p>
</blockquote>
<p>and still got the exact error message as above.</p>
<p>Should I add the C:\Program Files\Slicer 4.10.0\lib\Python\Scripts’ to system path as suggested by install? I was wary of that messing up other things in Slicer. WHat else I might be missing?</p>

---

## Post #4 by @jcfr (2018-11-28 08:11 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="4897">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>WHat else I might be missing?</p>
</blockquote>
</aside>
<p>Based on the snippet you are trying to execute, pyRserve should be installed within anaconda not within Slicer.</p>

---

## Post #5 by @muratmaga (2018-11-28 08:13 UTC)

<p>Right, there was no point in installing into Slicer (getting late here).<br>
Nevertheless, it was installed in anaconda.</p>

---

## Post #6 by @muratmaga (2018-11-28 08:14 UTC)

<p>Whatever it was, it doesn’t matter anymore. Running it through Slicer’s pyRserve worked fine, which is more important anyways.<br>
Thanks for the help!</p>

---
