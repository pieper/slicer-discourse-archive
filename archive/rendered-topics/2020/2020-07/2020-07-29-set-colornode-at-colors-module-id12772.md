---
topic_id: 12772
title: "Set Colornode At Colors Module"
date: 2020-07-29
url: https://discourse.slicer.org/t/12772
---

# Set ColorNode at Colors Module

**Topic ID**: 12772
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/set-colornode-at-colors-module/12772

---

## Post #1 by @siaeleni (2020-07-29 18:05 UTC)

<p>Hi,</p>
<p>I want to set a color Node programmatically that I have created to the Colors Module in order to display it.<br>
I have created a node like this, but I am not sure how to set it to the Colors module.</p>
<blockquote>
<p>colorNode = slicer.vtkMRMLColorNode()<br>
table = slicer.modules.colors.logic().CopyNode(colorNode, “rainbow”)<br>
slicer.mrmlScene.AddNode(table)</p>
</blockquote>
<p>Thanks</p>

---
