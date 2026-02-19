---
topic_id: 7411
title: "Draw Specific Lines And Measure Ange Between Them"
date: 2019-07-04
url: https://discourse.slicer.org/t/7411
---

# Draw specific lines and measure ange between them

**Topic ID**: 7411
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/draw-specific-lines-and-measure-ange-between-them/7411

---

## Post #1 by @Bence_Horvath (2019-07-04 12:44 UTC)

<p>Hi,</p>
<p>I would like to know, is it possible, that I draw line or circle with specific lenght/radius (instead of I move the mosue and change the lenght), like type xx mm and I get a xx mm lenght line or circle.<br>
And how can I measure angle between this lines?</p>
<p>Thanks!<br>
Bence</p>

---

## Post #2 by @lassoan (2019-07-04 12:52 UTC)

<p>You can create sphere or line using VTK source objects (vtkSphereSource, vtkLineSource, etc.) and set their output in a model node as input. See for example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" rel="nofollow noopener">here</a> and in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">PerkLab Slicer programming tutorial</a>.</p>
<p>You can compute angles using trigonometry functions (e.g., <a href="https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan2.html" rel="nofollow noopener">arctan2</a> between line direction vectors). See a complete example <a href="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @Bence_Horvath (2019-07-04 13:30 UTC)

<p>Thank you very much!</p>

---
