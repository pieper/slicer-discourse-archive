# How to display two volumes over each other

**Topic ID**: 6858
**Date**: 2019-05-20
**URL**: https://discourse.slicer.org/t/how-to-display-two-volumes-over-each-other/6858

---

## Post #1 by @safa (2019-05-20 17:59 UTC)

<p>hello, is it possible to see two volumes one over other. like i want to put segmented output result on original images. how to do it using slicer?</p>
<p>Operating system:windows<br>
Slicer version:4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @muratmaga (2019-05-21 02:31 UTC)

<p>You don’t need to do anything special.<br>
If you render the original volume via volume rendering module, and turn on the 3D for your segmentation, it is done. You just need to adjust your transfer functions and opacity for segments for best possible result.</p>

---

## Post #3 by @safa (2019-05-22 12:12 UTC)

<p>ok thank you</p>
<p>Le mar. 21 mai 2019 à 03:42, Murat Maga via 3D Slicer Forum <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> a écrit :</p>

---
