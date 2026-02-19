---
topic_id: 36547
title: "Jupyterkernel Error Information"
date: 2024-06-02
url: https://discourse.slicer.org/t/36547
---

# JupyterKernel Error Information

**Topic ID**: 36547
**Date**: 2024-06-02
**URL**: https://discourse.slicer.org/t/jupyterkernel-error-information/36547

---

## Post #1 by @lotus (2024-06-02 02:01 UTC)

<p>Dear expert, I tried to run a script in JupyterNotebook to execute slicer’s registration function, but error messages appeared during the installation process, what should I do with these error messages, thank you</p>
<p>Python 3.9.10 (main, Apr  5 2024, 01:02:26) [MSC v.1938 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>JupyterConnectionFile:[C:\Users\Lotus\AppData\Roaming\jupyter\runtime\kernel-7d3729d1-7d62-46df-b068-1f5b98165e19.json]<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
RuntimeError: std::runtime_error: ModuleNotFoundError: No module named ‘IPython’</p>
<p>At:<br>
D:\ProgramData\slicerorg\Slicer\slicer.org\Extensions-32448\SlicerJupyter\Lib\site-packages\xeus_python_shell\shell.py(10): <br>
(228): _call_with_frames_removed<br>
(850): exec_module<br>
(695): _load_unlocked<br>
(986): _find_and_load_unlocked<br>
(1007): _find_and_load<br>
(1): </p>

---

## Post #2 by @lotus (2024-06-02 02:15 UTC)

<aside class="quote no-group" data-username="lotus" data-post="1" data-topic="36547">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/0ea827/48.png" class="avatar"> lotus:</div>
<blockquote>
<p>IPython</p>
</blockquote>
</aside>
<p>I checked the environment, Requirement already satisfied.</p>
<p>(base) PS C:\WINDOWS\system32&gt; pip install IPython<br>
Requirement already satisfied: IPython in d:\users\lotus\anaconda3\lib\site-packages (8.10.0)<br>
Requirement already satisfied: pygments&gt;=2.4.0 in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (2.11.2)<br>
Requirement already satisfied: prompt-toolkit&lt;3.1.0,&gt;=3.0.30 in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (3.0.36)<br>
Requirement already satisfied: decorator in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (5.1.1)<br>
Requirement already satisfied: colorama in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (0.4.6)<br>
Requirement already satisfied: pickleshare in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (0.7.5)<br>
Requirement already satisfied: stack-data in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (0.2.0)<br>
Requirement already satisfied: traitlets&gt;=5 in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (5.7.1)<br>
Requirement already satisfied: jedi&gt;=0.16 in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (0.18.1)<br>
Requirement already satisfied: backcall in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (0.2.0)<br>
Requirement already satisfied: matplotlib-inline in d:\users\lotus\anaconda3\lib\site-packages (from IPython) (0.1.6)<br>
Requirement already satisfied: parso&lt;0.9.0,&gt;=0.8.0 in d:\users\lotus\anaconda3\lib\site-packages (from jedi&gt;=0.16-&gt;IPython) (0.8.3)<br>
Requirement already satisfied: wcwidth in d:\users\lotus\anaconda3\lib\site-packages (from prompt-toolkit&lt;3.1.0,&gt;=3.0.30-&gt;IPython) (0.2.5)<br>
Requirement already satisfied: asttokens in d:\users\lotus\anaconda3\lib\site-packages (from stack-data-&gt;IPython) (2.0.5)<br>
Requirement already satisfied: pure-eval in d:\users\lotus\anaconda3\lib\site-packages (from stack-data-&gt;IPython) (0.2.2)<br>
Requirement already satisfied: executing in d:\users\lotus\anaconda3\lib\site-packages (from stack-data-&gt;IPython) (0.8.3)<br>
Requirement already satisfied: six in d:\users\lotus\anaconda3\lib\site-packages (from asttokens-&gt;stack-data-&gt;IPython) (1.16.0)</p>

---
