# EM Segmenter: input type mismatch

**Topic ID**: 376
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/em-segmenter-input-type-mismatch/376

---

## Post #1 by @nshusharina (2017-05-24 16:57 UTC)

<p>Operating system: Windows<br>
Slicer version: 3.6.3<br>
Expected behavior:<br>
Actual behavior: Input Image Error</p>
<p>Hello.<br>
I am getting “Scalar type mismatch for input images” error in EM Segmenter. How do I match the types?<br>
Thank you,<br>
Nadya</p>

---

## Post #2 by @pieper (2017-05-24 17:11 UTC)

<p>Sounds like you may need to cast the volumes to the same datatype.</p>

---

## Post #3 by @Byounghoon_Kim (2018-02-06 18:33 UTC)

<p>Hi Steve,</p>
<p>Could you give us little more detail about casting datatype?</p>
<p>Thanks.</p>

---

## Post #4 by @pieper (2018-02-06 20:58 UTC)

<p>Hi -</p>
<p>You can look in the Volumes module to see what datatypes the images are.  Then you can use the Cast Scalar Volume module so that your input matches the atlas (I think the EMSegment requires type short but you may need to do some experiments).</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/CastScalarVolume" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/CastScalarVolume</a></p>
<p>-Steve</p>

---
