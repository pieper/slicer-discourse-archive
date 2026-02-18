# The shape will be changed when I turn an array to volume

**Topic ID**: 29920
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/the-shape-will-be-changed-when-i-turn-an-array-to-volume/29920

---

## Post #1 by @slicer365 (2023-06-08 15:31 UTC)

<p>I use the script  slicer.util.arrayFromVolume(volumeNode) get an array.</p>
<p>Then I use the script slicer.util.addVolumeFromArray(array), the volume’s shape is changed as is shown in the picture.</p>
<p>Why? How can I get the original volume from the array.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f644cc33bd3bc1b2997cbe27642797069a87150.jpeg" data-download-href="/uploads/short-url/bkkBV2bt6gmVvqROHmogrCDC400.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f644cc33bd3bc1b2997cbe27642797069a87150_2_517x363.jpeg" alt="image" data-base62-sha1="bkkBV2bt6gmVvqROHmogrCDC400" width="517" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f644cc33bd3bc1b2997cbe27642797069a87150_2_517x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f644cc33bd3bc1b2997cbe27642797069a87150_2_775x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f644cc33bd3bc1b2997cbe27642797069a87150_2_1034x726.jpeg 2x" data-dominant-color="7D7E81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1204×847 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-06-08 15:47 UTC)

<p>You can specify the ijkToRAS transform from the source volume, something like this:</p>
<pre><code class="lang-auto">ijkToRAS = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRAS)
segArray = numpy.stack(segmentationArrays)
segNode = slicer.util.addVolumeFromArray(segArray, ijkToRAS=ijkToRAS, name="Segmentation")
</code></pre>

---
