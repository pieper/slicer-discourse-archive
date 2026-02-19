---
topic_id: 25725
title: "Linear Transform In Image Plane"
date: 2022-10-16
url: https://discourse.slicer.org/t/25725
---

# Linear transform in image plane

**Topic ID**: 25725
**Date**: 2022-10-16
**URL**: https://discourse.slicer.org/t/linear-transform-in-image-plane/25725

---

## Post #1 by @BraDan (2022-10-16 18:33 UTC)

<p>Hello everyone,</p>
<p>This question must be trivial to you - but I would very much appreciate any help on this.</p>
<p>Does anybody know how to translate a segmentation in the image plane using the translation sliders?</p>
<p>The only way for me to achieve this is to rotate the segmentation reference frame to the image plane and then use "translation in local (rotated) reference frame’. Problem is then, of course, that the segmentation is rotated…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d678f0efcc8befbf5017701b0a55a3c860a21af7.jpeg" alt="Screenshot" data-base62-sha1="uBjidO0JEI4HjZxeL3JpVMB6zav" width="662" height="473"></p>

---

## Post #2 by @pieper (2022-10-17 18:07 UTC)

<p>One option is to make two nested transforms.  The outer one rotates to the desired plane, and then the second inner nested one counter rotates by the same amount.  Then if you go back to the first and translate in local reference frame you’ll be moving in the rotated plane.</p>

---

## Post #3 by @BraDan (2022-10-17 18:48 UTC)

<p>Thanks! Will give this a try as soon as possible.</p>

---

## Post #4 by @BraDan (2022-10-18 17:41 UTC)

<p>Works perfectly, here is what I have done according to your input:</p>
<p>Markups → Create a plane in the rotated volume on any image slice.<br>
Then get its orientation in relation to the world coordinate system with:</p>
<pre><code class="lang-auto">planeToWorld = vtk.vtkMatrix4x4()
getNode('P').GetObjectToWorldMatrix(planeToWorld)
print(planeToWorld)
</code></pre>
<p>Copy the rotation transform (3 x 3 submatrix).</p>
<p>Create first LinearTransform ‘counterRotate’: Paste 3 x 3 submatrix in transform matrix. Press ‘Invert’ button. Apply transform to Segmentation.</p>
<p>Create second LinearTransform ‘rotateAndTranslateWithSliders’: Paste 3 x 3 submatrix in transform matrix. Select translation in local (rotated) coordinate system. Apply transform to transformed segmentation.</p>
<p>Now, as expected, the translation sliders translate the segmentation in the plane of the volume slices. Thank you very much again!</p>

---
