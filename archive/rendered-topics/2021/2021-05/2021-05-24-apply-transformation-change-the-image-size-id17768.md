---
topic_id: 17768
title: "Apply Transformation Change The Image Size"
date: 2021-05-24
url: https://discourse.slicer.org/t/17768
---

# Apply transformation change the image size

**Topic ID**: 17768
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/apply-transformation-change-the-image-size/17768

---

## Post #1 by @marianaslicer (2021-05-24 17:20 UTC)

<p>Hi everyone,</p>
<p>I’m using the 3D Slicer version 4.13 and when I apply a b-spline transformation to an image it changes the original size.</p>
<p>Original size = 512 x 512 x 140</p>
<p>After apply the transformation:</p>
<pre><code>    transformLogic = slicer.modules.transforms.logic()
    ctNode.SetAndObserveTransformNodeID(transform.GetID())
    transformLogic.hardenTransform(ctNode)
</code></pre>
<p>The final image size becomes = 513 x 513 x 140</p>
<p>I don’t want to change the original image size. Is it possible to maintain the original image size after transformation without cropping?</p>
<p>The transformation is saved in .txt file with the following parameters:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ebedad24b8d4c94c8761095042c00898bfa158.png" alt="image" data-base62-sha1="jG6T2zJPxINcsYUKVYqopuTPjQs" width="233" height="149"></p>
<p>I would appreciate some help. Thanks.</p>

---

## Post #2 by @lassoan (2021-05-25 03:50 UTC)

<p>Deformable transforms can translate volumes and make parts of the volume bulge out, therefore in general you don’t want the resampled volume to have the same geometry (origin, spacing, axis directions, extents) as the non-transformed volume. Slicer automatically expands the volume extents to ensure that the complete warped volume is preserved.</p>
<p>If you want to enforce a particular image geometry then you can use a resampling module (for example, “Resample scalar/vector/dwi volume”) to create a transformed volume resampled to a chosen reference volume. In your case, the “Reference volume” will be your input volume.</p>

---

## Post #3 by @marianaslicer (2021-05-25 10:37 UTC)

<p>Thank you for your answer</p>

---
