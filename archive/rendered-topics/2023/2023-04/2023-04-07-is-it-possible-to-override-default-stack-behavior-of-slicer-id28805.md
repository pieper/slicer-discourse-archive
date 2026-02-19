---
topic_id: 28805
title: "Is It Possible To Override Default Stack Behavior Of Slicer"
date: 2023-04-07
url: https://discourse.slicer.org/t/28805
---

# Is it possible to override default stack behavior of slicer viewport?

**Topic ID**: 28805
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/is-it-possible-to-override-default-stack-behavior-of-slicer-viewport/28805

---

## Post #1 by @turtleizzy (2023-04-07 22:16 UTC)

<p>I want to implement an image plugin that generates and displays image on the fly with a parameter derived from the position of a slider. Is it possible to make use of the slider control above the viewport and override the default behavior that sets the slicing position along a certain vector?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ddb750f60f7c74cbcebcbce3d88a939e507ba7.png" data-download-href="/uploads/short-url/n5VTD22ziQfGBLPxq3HkNrEW58j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ddb750f60f7c74cbcebcbce3d88a939e507ba7_2_690x45.png" alt="image" data-base62-sha1="n5VTD22ziQfGBLPxq3HkNrEW58j" width="690" height="45" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ddb750f60f7c74cbcebcbce3d88a939e507ba7_2_690x45.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ddb750f60f7c74cbcebcbce3d88a939e507ba7_2_1035x67.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ddb750f60f7c74cbcebcbce3d88a939e507ba7.png 2x" data-dominant-color="91A88C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1058×70 8.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For example, if I am to implement a straightened CPR image plugin that takes the abscissa on the centerline as the parameter, and generates an sliced image on the fly, I want to override the slider control to make its minimal value 0mm and maximal value the arclen of the centerline, and the behavior of moving that slider would be a callback to a function that generates a new image and replaces current viewport by the position of the slider.</p>
<p>Another example, if I am to implement a non-volumetric dicom image stack plugin that takes the index of the image in the stack as the parameter, I want to make the slider control take minimal value of 0 and maximal value of len(stack), and the behavior of moving that slider would be replacing current viewport with some .</p>
<p>P.S: Non-volumentric dicom image stacks are common here in clinical practice relating to intervertebral discs. The technician scans along the axis of each intervertebral disc for, like 3 slices, and stacks the images from all intervertebral discs into one series. So this series as whole would not be compatible with volumetric image, but splitting them into groups of 3 images would be also too overwhelming for viewing purpose.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56793ccfcc4a965a69ff811472cc2bdcc90ccd6.jpeg" data-download-href="/uploads/short-url/pSMkO1bXLPoWh3zNCwtei5ly3f8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56793ccfcc4a965a69ff811472cc2bdcc90ccd6.jpeg" alt="image" data-base62-sha1="pSMkO1bXLPoWh3zNCwtei5ly3f8" width="690" height="458" data-dominant-color="241414"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×565 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-04-07 22:28 UTC)

<aside class="quote no-group" data-username="turtleizzy" data-post="1" data-topic="28805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/turtleizzy/48/65548_2.png" class="avatar"> turtleizzy:</div>
<blockquote>
<p>Non-volumentric dicom image stacks are common here in clinical practice</p>
</blockquote>
</aside>
<p>Actually, Slicer reconstructs a volume from these arbitrarily spaced and oriented slices on-the-fly! So, you can browse the sparse volume using parallel slices. (If the slices intersect then Volume reconstruction module of IGSIO extension can be used to create a meaningful 3D volume, but this is probably not worth the trouble.)</p>
<p>However, if you don’t want to do this then you can load the image slices as a sequence. It may not be the default interpretation of the series, so you may need to use the “Advanced” option in the DICOM module to load them as a sequence. You can add a custom DICOM reader plugin that recognizes your very special kind of acquisition type and make it loaded as a sequence by default.</p>
<p>You can browser the slices using the slider on the sequence toolbar. You can also put a sequence browser widget on your module’s GUI. If you want the sequence browser appear in the slice view controller then you need to hack a little (hide the slice offset slider and add a <code>slicer.qMRMLSequenceBrowserSeekWidget</code> or a Qt slider there).</p>
<p>Once the frames are loaded as a sequence, you can use VolumeResliceDriver module to make a slice view move along with the slice position/orientation.</p>
<p>All these could be nicely implemented in a Python scripted module. If you accept the challenge of implementing this then you could create a new “CurvedPlanarReformat” extension, move the “Curved Planar Reformat” module into that extension, and add these improved browsing features to that module. You could also add the custom DICOM importer plugin to that extension (that recognizes your kind of MR series and load them as a sequence by default).</p>

---

## Post #3 by @turtleizzy (2023-04-10 00:58 UTC)

<p>Cool! I’ve heard of sequence. I will try that out!</p>

---
