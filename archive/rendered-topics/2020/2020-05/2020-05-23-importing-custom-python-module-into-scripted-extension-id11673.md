---
topic_id: 11673
title: "Importing Custom Python Module Into Scripted Extension"
date: 2020-05-23
url: https://discourse.slicer.org/t/11673
---

# Importing custom python module into scripted extension

**Topic ID**: 11673
**Date**: 2020-05-23
**URL**: https://discourse.slicer.org/t/importing-custom-python-module-into-scripted-extension/11673

---

## Post #1 by @talmazov (2020-05-23 03:27 UTC)

<p>Hey all,<br>
I have a custom python file asyncsocket.py that contains some code independent of 3d slicer. I am trying to import that module to use in a scripted widged by doing<br>
import asyncsocket<br>
howeveri get this<br>
RuntimeError: qSlicerScriptedLoadableModule::setPythonSourc<br>
apperently it is not a scripted loadable module. this is a generic python code that utilizes only core python function<br>
asyncsocket.py is in the same directory as the slicer scripted widget</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-05-23 04:18 UTC)

<p>This topic should help:</p>
<aside class="quote" data-post="2" data-topic="6339">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/python-scripted-module-code-organization/6339/2">Python scripted module code organization</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Python modules must be in subfolder(s). See for example how it is done in <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DataProbe" rel="nofollow noopener">DataProbe module</a>.
  </blockquote>
</aside>


---

## Post #3 by @adamrankin (2023-05-17 13:40 UTC)

<p>FYI this is the first google hit on the subject</p>

---

## Post #4 by @talmazov (2023-07-10 01:37 UTC)

<p>this was fixed by placing the custom python file in a subdirectory (eg. comm) of the scriptable module and using</p>
<p>example: from comm import asyncsock</p>
<p>in comm folder there is</p>
<p><code>__init__.py</code></p>
<p>which contains</p>
<p>from .asyncsock import *</p>

---
