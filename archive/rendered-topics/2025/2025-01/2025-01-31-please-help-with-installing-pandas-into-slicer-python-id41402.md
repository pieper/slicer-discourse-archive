---
topic_id: 41402
title: "Please Help With Installing Pandas Into Slicer Python"
date: 2025-01-31
url: https://discourse.slicer.org/t/41402
---

# Please help with installing Pandas into Slicer Python

**Topic ID**: 41402
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/please-help-with-installing-pandas-into-slicer-python/41402

---

## Post #1 by @Misterkim (2025-01-31 11:28 UTC)

<p>I ran the following from the PythonSlicer console:</p>
<pre><code class="lang-auto">from slicer.util import pip_install
pip_install("pandas&gt;2")
</code></pre>
<p>and received the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
 File "&lt;console&gt;", line 1, in &lt;module&gt;
 File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3571, in pip_install
   _executePythonModule('pip', args)
 File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3533, in _executePythonModule
   logProcessOutput(proc)
 File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3502, in logProcessOutput
   raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'pandas&gt;2']' returned non-zero exit status 1.
</code></pre>
<p>Does anyone more experienced than I am know what might be going on? Thanks!</p>

---

## Post #2 by @Thibault_Pelletier (2025-01-31 16:34 UTC)

<p>Hi <a class="mention" href="/u/misterkim">@Misterkim</a>,</p>
<p>pandas usually installs fine for 3D Slicer.<br>
What you can test is opening the command prompt and run the pip install command manually to get more information on what went wrong.</p>
<p>In your case something like :</p>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/bin/PythonSlicer -m pip install pandas&gt;2
</code></pre>

---

## Post #3 by @jumbojing (2025-02-04 21:04 UTC)

<hr>
<p>CalledProcessError                        Traceback (most recent call last)<br>
Cell In[36], line 1<br>
----&gt; 1 ut.pip_install(‘nibabel’)</p>
<p>File /Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3887, in pip_install(requirements)<br>
3884 else:<br>
3885     raise ValueError(“pip_install requirement input must be string or list”)<br>
 → 3887 _executePythonModule(“pip”, args)</p>
<p>File /Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3848, in _executePythonModule(module, args)<br>
3846 commandLine = [pythonSlicerExecutablePath, “-m”, module, *args]<br>
3847 proc = launchConsoleProcess(commandLine, useStartupEnvironment=False)<br>
 → 3848 logProcessOutput(proc)</p>
<p>File /Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3814, in logProcessOutput(proc)<br>
3812 retcode = proc.returncode<br>
3813 if retcode != 0:<br>
 → 3814     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘nibabel’]’ returned non-zero exit status 1.</p>
<p>I also encountered the same problem…<br>
我也遇到了同样的问题</p>

---
