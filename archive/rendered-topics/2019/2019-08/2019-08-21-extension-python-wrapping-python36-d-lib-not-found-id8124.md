---
topic_id: 8124
title: "Extension Python Wrapping Python36 D Lib Not Found"
date: 2019-08-21
url: https://discourse.slicer.org/t/8124
---

# Extension python wrapping (python36_d.lib not found)

**Topic ID**: 8124
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/extension-python-wrapping-python36-d-lib-not-found/8124

---

## Post #1 by @adamrankin (2019-08-21 16:32 UTC)

<p>Hello all,</p>
<p>Is it possible to use the release python built by debug Slicer to be used in extensions for wrapping?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Cheers,<br>
Adam</p>

---

## Post #2 by @adamrankin (2019-08-21 18:05 UTC)

<p>To myself:</p>
<p>Yes, it is an error in the library to automatically use the python_d library. In this case, Swig looks for python36_d.lib unless configured using the SWIG_PYTHON_INTERPRETER_NO_DEBUG preprocessor define.</p>
<p><a href="http://www.swig.org/Doc3.0/Python.html" class="onebox" target="_blank" rel="nofollow noopener">http://www.swig.org/Doc3.0/Python.html</a></p>

---

## Post #3 by @jcfr (2019-08-21 20:25 UTC)

<p>As you may have noticed, independently of the configuration you choose to build Slicer (Release, RelWithDebInfo, … , Debug), CPython is always built in Release/</p>
<p>This should not prevent you from wrapping your code.</p>
<p>Could you provide more details about the error you got and how to reproduce it ?</p>

---
