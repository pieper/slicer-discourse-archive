---
topic_id: 13203
title: "Finding Creating Modules From Python Scripts And Or Framewor"
date: 2020-08-27
url: https://discourse.slicer.org/t/13203
---

# Finding & creating modules from python scripts and/or frameworks

**Topic ID**: 13203
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/finding-creating-modules-from-python-scripts-and-or-frameworks/13203

---

## Post #1 by @epearlstone (2020-08-27 20:39 UTC)

<p>I am looking to find python code to create modules. For example I know there is a post describing how to use an AI-assisted brain tumor segmentation but I would like to know where to find other open-source scripts/code that create models (modules other than seed grow or thresholding). So, where is the best place to look or best way to search for python modules. As another example, is there maybe a scripted module to best create a model of a kidney? Any suggestions would be much appreciated.<br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @stevenagl12 (2022-01-25 21:56 UTC)

<p>Is there a specific section of the available python code for 3D Slicer to find how to create module buttons, sliding bars, open regions for typing names and such?</p>

---

## Post #3 by @lassoan (2022-01-25 22:04 UTC)

<p>We recommend to use Qt designer for this. You can create a new scripted module using the Extension Wizard module then click “Edit UI” in the header of your module to edit its GUI using Qt Designer.</p>
<p>There are <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">tutorials</a> (I would recommend the PerkLab bootcamp Slicer module development tutorial). However, Qt and VTK are large toolkits so you cannot learn them from Slicer tutorials but you need to study their excellent tutorials and documentation.</p>

---

## Post #4 by @stevenagl12 (2022-01-25 22:04 UTC)

<p>Thank you very much!</p>

---
