---
topic_id: 17990
title: "How To Interact With Module Using Python Interactor Is There"
date: 2021-06-07
url: https://discourse.slicer.org/t/17990
---

# How to interact with module using python interactor? / is there a scripting info box?

**Topic ID**: 17990
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/how-to-interact-with-module-using-python-interactor-is-there-a-scripting-info-box/17990

---

## Post #1 by @mgpoirot (2021-06-07 09:50 UTC)

<p>I’ve been able to load a file by drag and dropping it into slicer.<br>
The GUI pops up and an extension (SlicerFreeSurfer) recognizes its format and the file can be loaded.</p>
<p>How would I replace the same actions using the command line interactor?<br>
I’ve already found <code>slicer.util.loadModel</code> not to work since it’s using the extension?</p>
<p>I don’t think there is anything like the <code>scripting info</code> box that Blender employs? It’s really usefull for finding commands for otherwise manual tasks.<br>
                    <a href="https://i.imgur.com/kcRhGES.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.imgur.com/kcRhGES.png" width="476" height="500">
          </a>

<br>
<em>in this image the lower half of the screen shows the scripting info box: a line by line summary of script executed during manual tasks. The terminal to the right of the 3D view of the sphere shows python interaction executing some of this code.</em></p>

---

## Post #2 by @lassoan (2021-09-07 19:07 UTC)

<p>There is macro recording capability in Slicer: if you enable QtTesting then you can record and replay user interface events. We haven’t invested much time into making this more user friendly or easier to find because it is only intended for test automation. It would be extremely fragile for production use.</p>
<p>Instead, we recommend to determine the Python functions that are at the most suitable level for what you want to achieve. See an example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">here</a>. You can also always ask here if you don’t manage to find an appropriate function. This is certainly more work than just recording a macro, but it results in scripts that are much more configurable and maintainable in the long term.</p>

---
