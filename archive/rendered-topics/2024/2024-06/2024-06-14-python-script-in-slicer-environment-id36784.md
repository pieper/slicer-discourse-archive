# python script in slicer environment 

**Topic ID**: 36784
**Date**: 2024-06-14
**URL**: https://discourse.slicer.org/t/python-script-in-slicer-environment/36784

---

## Post #1 by @Adham (2024-06-14 14:37 UTC)

<p>I’m running a python script using PythonSlicer myscript.py. Here is my script:</p>
<pre><code class="lang-auto">import slicer

directory = "/path/to/files"

loadedVolumeNode = slicer.util.loadVolume(directory, {"singleFile": False})
</code></pre>
<p>I got this error message:</p>
<pre><code class="lang-auto">No module named 'logic'
Traceback (most recent call last):
  File "/path/to/myscript.py", line 9, in &lt;module&gt;
    loadedVolumeNode = slicer.util.loadVolume(directory, {"singleFile": False})
AttributeError: module 'slicer' has no attribute 'util'
</code></pre>
<p>Based on slicer documentation, slicer has a module named util. Why it can’t find it?</p>
<p>My slicer version is: Slicer 5.6.2.</p>
<p>Could you please help with this issue? thanks in advance.</p>

---

## Post #2 by @lassoan (2024-06-14 14:41 UTC)

<p>PythonSlicer application does not start the Slicer application and so no Slicer modules are instantiated. You may be able to instantiate module logic classes manually and use them, but it is simpler to run your script in the Slicer application’s Python environment</p>
<pre><code>Slicer --no-main-window --python-script "path/to/myfile.py"
</code></pre>

---

## Post #3 by @Adham (2024-06-14 19:25 UTC)

<p>Thank you for your reply. I’m trying to run an app which uses slicer’s modules in the back end for visualization without using slicer’s user interface. Is it possible to install Slicer modules as a python package so I can import them in my environment?</p>

---

## Post #4 by @lassoan (2024-06-15 03:37 UTC)

<p>We are working on making Slicer core available as pip-installable packages, but it is a long-term project (we need to get funding for it and then work on it for a few years).</p>
<p>But there are several almost as good solutions that you can use until then. The easiest method is to prevent any GUI from appearing is to used dockerized versions of Slicer. But you can also launch Slicer once and hide its window. While Slicer is running, you can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">Slicer’s web API</a> to run any commands (e.g., from a web app or from the command line) or you can conveniently use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">slicerio Python package</a> to launch Slicer from Python and run commands in Slicer from any Python environment.</p>

---

## Post #5 by @Adham (2024-06-18 03:04 UTC)

<p>Thank you so much for your guidance. I used :</p>
<pre><code class="lang-auto">Slicer.exe --python-script "C:/Users/myscript.py"
</code></pre>
<p>I run it through subprocess module from my main app and it worked !!</p>
<p>Thanks again, your replies helped me a lot.</p>
<p>Best regards.</p>

---
