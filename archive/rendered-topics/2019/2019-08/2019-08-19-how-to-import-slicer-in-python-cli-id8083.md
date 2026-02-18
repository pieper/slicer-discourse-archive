# How to import Slicer in python-cli

**Topic ID**: 8083
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/how-to-import-slicer-in-python-cli/8083

---

## Post #1 by @joechenrh (2019-08-19 04:07 UTC)

<p>Hi,<br>
I’m trying to use python-cli to save node and upload to remote server. But I got error when using saveNode. How can I use these functions in python-cli?<br>
Thanks.</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/chen/Desktop/SlicerRadiomicsCLI/SlicerRadiomicsCLI.py”, line 48, in<br>
main()<br>
File “C:/Users/chen/Desktop/SlicerRadiomicsCLI/SlicerRadiomicsCLI.py”, line 42, in main<br>
slicer.util.saveNode(getNode(‘1’), ‘1.nii.gz’)<br>
AttributeError: ‘module’ object has no attribute ‘util’</p>

---

## Post #2 by @joechenrh (2019-08-20 06:02 UTC)

<p>Sorry, currently I meet another problem. Can I exchange data with process created by CLI?<br>
For example, in CLI, I have</p>
<pre><code class="lang-python">Queue.put(data)
</code></pre>
<p>and in main process</p>
<pre><code class="lang-python">if not Queue.empty():
    data = Queue.get()
</code></pre>

---

## Post #3 by @Sam_Horvath (2019-08-20 15:06 UTC)

<p>Generally, CLIs are not intended to have direct access to the Slicer scene / infrastructure.  They are meant for non-interactive data processing with non-slicer libraries.  If you want to work within the Slicer environment, you should keep the code within a python scripted module.</p>

---
