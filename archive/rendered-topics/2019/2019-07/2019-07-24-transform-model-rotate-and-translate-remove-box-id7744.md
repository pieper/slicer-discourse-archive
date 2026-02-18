# Transform Model-rotate and translate remove box

**Topic ID**: 7744
**Date**: 2019-07-24
**URL**: https://discourse.slicer.org/t/transform-model-rotate-and-translate-remove-box/7744

---

## Post #1 by @Christina (2019-07-24 20:10 UTC)

<p>Hello Slicer expert,</p>
<p>In Slicer, how do you get rid of the white box around the model when you are rotating and translating a model in the Transform module?</p>
<p>Thank you,<br>
Christina</p>

---

## Post #2 by @lassoan (2019-07-24 20:15 UTC)

<p>You can hide the transformation editing box in Transforms module by unchecking “Visible in 3D view” checkbox in Display / Interaction section.</p>

---

## Post #3 by @Christina (2019-07-26 12:18 UTC)

<p>Thank you. However, how do you continue editing of the transform while interacting with the 3D scene; move the model around without showing the white box?</p>

---

## Post #4 by @lassoan (2019-07-26 12:23 UTC)

<p>You can edit the transform using sliders in Transforms module GUI.</p>
<p>You can also write custom Python script that observe markups fiducial points and updates transform based on point positions.</p>

---
