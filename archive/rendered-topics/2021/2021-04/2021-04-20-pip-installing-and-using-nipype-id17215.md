---
topic_id: 17215
title: "Pip Installing And Using Nipype"
date: 2021-04-20
url: https://discourse.slicer.org/t/17215
---

# Pip installing and using nipype

**Topic ID**: 17215
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/pip-installing-and-using-nipype/17215

---

## Post #1 by @mangotee (2021-04-20 15:57 UTC)

<p>Hi,<br>
I’m trying to install and use nipype inside Slicer. I can install via</p>
<p><code>pip_install('nipype')</code></p>
<p>However, when I try to <code>import nipype</code>, I get the following error message(s):</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\mangotee\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\nipype\__init__.py", line 26, in &lt;module&gt;
    faulthandler.enable()
AttributeError: 'PythonQtStdOutRedirect' object has no attribute 'fileno' 
</code></pre>
<p>Is there anything I can do to fix this? Any help is appreciated… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @pieper (2021-04-20 20:06 UTC)

<p>Unfortunately not every pip package is going to be compatible with Slicer.  In this case it seems nipype is making assumptions about the program’s standard output so it may not work.  You might be able to install/build nipype from source and turn off whatever feature is trying to do this access.</p>

---
