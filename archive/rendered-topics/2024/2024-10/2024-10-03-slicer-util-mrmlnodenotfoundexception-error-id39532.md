---
topic_id: 39532
title: "Slicer Util Mrmlnodenotfoundexception Error"
date: 2024-10-03
url: https://discourse.slicer.org/t/39532
---

# slicer.util.MRMLNodeNotFoundException Error

**Topic ID**: 39532
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/slicer-util-mrmlnodenotfoundexception-error/39532

---

## Post #1 by @BenAsh (2024-10-03 21:28 UTC)

<p>Hi there. So I’ve been trying to run a one of the simple filters on my scans, that one being the “RichardsonLucyDeconvolutionImageFilter”. However, whenever I attempt to run this (or any other Simple Filter) I am hit with an error saying ‘slicer.util.MRMLNodeNotFoundException’. I found a previous post regarding this error (<a href="https://discourse.slicer.org/t/slicer-util-mrmlnodenotfoundexception-could-not-find-nodes-in-the-scene-by-name-or-id-error/14135" class="inline-onebox">slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id '' error</a>) and attempted to follow the instructions for a fix but, given my limited understanding of coding in general, I’m not sure if it didn’t work because I did it wrong or because the fix is now outdated. Does anyone know what is causing this error and how to fix it? Thanks!</p>

---

## Post #2 by @lassoan (2024-10-03 21:34 UTC)

<p>The error is because you used a node name in the <code>getNode</code> thay does not exist. You can see what nodes are available in <code>Data</code> module.</p>
<p>If all you want to do is trying ITK image processing filters, such as <code>RichardsonLucyDeconvolutionImageFilter</code>, thrn you don’t need any Pyrhon scripting, but you can use the graphical user interface in <code>Simple Filters</code> module.</p>

---
