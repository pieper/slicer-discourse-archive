---
topic_id: 6666
title: "Grow Cut On 2D Image"
date: 2019-05-01
url: https://discourse.slicer.org/t/6666
---

# Grow-cut on 2D image

**Topic ID**: 6666
**Date**: 2019-05-01
**URL**: https://discourse.slicer.org/t/grow-cut-on-2d-image/6666

---

## Post #1 by @gcsharp (2019-05-01 17:50 UTC)

<p>It seems grow-cut doesn’t work on 2D images.  The output are empty segments.  Below is what I get in the error log.</p>
<p>Maybe I can workaround by duplication into a stack.  Is there a built-in function for this?</p>
<pre><code>self.extentGrowthRatio = 0.5
masterImageExtent = (0, 638, 0, 638, 0, 0)
labelsEffectiveExtent = (0, 638, 0, 638, 0, 0)
labelsExpandedExtent = [0, 638, 0, 638, 0, 0]
Generic Warning: In /PHShome/gcs6/build/slicer-4/Slicer/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx, line 483
vtkImageGrowCutSegment: image size is too small

The update extent specified in the information for output port 0 on algorithm vtkTrivialProducer(0x55aa46c909b0) is -1 -1 -1 -1 -1 -1, which is outside the whole extent 0 -1 0 -1 0 -1.
This data object does not contain the requested extent.
The update extent specified in the information for output port 0 on algorithm vtkTrivialProducer(0x55aa4be99dc0) is -1 -1 -1 -1 -1 -1, which is outside the whole extent 0 -1 0 -1 0 -1.
This data object does not contain the requested extent.</code></pre>

---

## Post #2 by @lassoan (2019-05-01 18:08 UTC)

<p>Yes, “Grow from seeds” effect only works on 3D images. It would not be too much work to update the filter to support single-slice volumes, but if you only need to segment a single slice then it is usually faster to directly paint or draw the final contour (instead of specify seeds and grow them).</p>
<p>What is your use case? If you use “Grow from seeds” to make a completely automatic segmentation from automatically placed seeds then I can see how it would be useful to be able use the effect on a single slice. In that case, using Crop volume to resample to have multiple slices could be a viable workaround (but maybe you could spend the time instead on updating vtkImageGrowCutSegment to accept single-slice volumes).</p>

---

## Post #3 by @gcsharp (2019-05-01 18:37 UTC)

<p>I’m helping a guy in material science segment an image of a carbon fiber sample.  I used thresholding to get most of the segmentation, and was trying to use grow-cut to finish the job.</p>
<p>But anyway, I just wanted to report this.  It works fine if I make a stack.</p>

---
