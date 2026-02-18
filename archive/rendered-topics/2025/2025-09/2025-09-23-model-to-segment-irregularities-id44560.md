# Model to segment irregularities

**Topic ID**: 44560
**Date**: 2025-09-23
**URL**: https://discourse.slicer.org/t/model-to-segment-irregularities/44560

---

## Post #1 by @bserrano (2025-09-23 10:56 UTC)

<p>Hi everyone,</p>
<p>We’re trying to use the <strong>Segment Editor (Subtract)</strong> with <strong>shapeNodes (cylinders)</strong>.<br>
Our current workflow is:</p>
<ol>
<li>Convert the shapeNode (model) into a segment.</li>
<li>Apply the segment editor operations.</li>
</ol>
<p>The issue appears after converting the model into a segment: the geometry no longer matches the volume (see yellow cylinder below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fc10de8b25aa3b7018f0281b298c93323b9a87e.jpeg" data-download-href="/uploads/short-url/4wUpX1VkGXglqjWKM92ysjIwvng.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fc10de8b25aa3b7018f0281b298c93323b9a87e_2_690x299.jpeg" alt="imagen" data-base62-sha1="4wUpX1VkGXglqjWKM92ysjIwvng" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fc10de8b25aa3b7018f0281b298c93323b9a87e_2_690x299.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fc10de8b25aa3b7018f0281b298c93323b9a87e_2_1035x448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fc10de8b25aa3b7018f0281b298c93323b9a87e_2_1380x598.jpeg 2x" data-dominant-color="878479"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1647×714 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If we try forcing the volume with the <em>“source geometry”</em> option in the Segment Editor, the result is a very irregular cylinder segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a645e3b7fdfb3dd1ccc1461020c29628cf246f18.png" data-download-href="/uploads/short-url/nIUZRdatehbiuAABkvHYxoz7aUE.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a645e3b7fdfb3dd1ccc1461020c29628cf246f18_2_690x285.png" alt="imagen" data-base62-sha1="nIUZRdatehbiuAABkvHYxoz7aUE" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a645e3b7fdfb3dd1ccc1461020c29628cf246f18_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a645e3b7fdfb3dd1ccc1461020c29628cf246f18.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a645e3b7fdfb3dd1ccc1461020c29628cf246f18.png 2x" data-dominant-color="89867B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">792×328 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Why does this happen?</li>
<li>Is there a way to fix it so we get a smoother cylinder segment?</li>
</ul>
<p>Related topic: <a href="https://discourse.slicer.org/t/crop-segment-using-shapenode/43822/3" class="inline-onebox">Crop segment using shapeNode - #3 by bserrano</a></p>

---

## Post #2 by @chir.set (2025-09-23 13:05 UTC)

<p>You are converting a polydata (closed surface) to a representation based on an image data (binary label map, segment, vtkOrientedImageData); it is not directly related to Shape nodes.</p>
<p>The result is highly dependent on the resolution of the segmentation, which is initially set according to the spacing or resolution of the input scalar volume. It can be resampled later; in general, I found that the staircase effect gets worse when a segmentation is oversampled.</p>
<p>It might be better to first resample your input volume before creating a segmentation based on it.</p>
<p>In the image below, a segment has been created from the cylinder. In green, the image data has a spacing of <code>0.3125 x 0.3125 x 0.6250</code>, i.e, the cylinder diameter is just above the minimum spacing. In red, the same volume has been resampled to <code>0.1 x 0.1 x 0.1</code> (don’t do that routinely). The result speaks for itself.</p>
<p>In all cases, the segment will shrink after removing and recreating the representation (Show 3D button).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41aa173a174d885c811bec0d82d4919d2e77b16.png" data-download-href="/uploads/short-url/yPryDMYjPUE88hGahs78uh3K5sq.png?dl=1" title="Resolution_ImageData_Conversion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f41aa173a174d885c811bec0d82d4919d2e77b16_2_662x500.png" alt="Resolution_ImageData_Conversion" data-base62-sha1="yPryDMYjPUE88hGahs78uh3K5sq" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f41aa173a174d885c811bec0d82d4919d2e77b16_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41aa173a174d885c811bec0d82d4919d2e77b16.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41aa173a174d885c811bec0d82d4919d2e77b16.png 2x" data-dominant-color="4C3A37"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Resolution_ImageData_Conversion</span><span class="informations">808×610 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @bserrano (2025-09-25 12:29 UTC)

<p>Thank you for the explanation.</p>
<p>In my case, I’m not resampling the volume at any point – the spacing remains the same. However, as you mention, the shrink that happens after converting and recreating the representation seems too aggressive, as can be seen in the image I attached.</p>
<p>I’m working with a spacing of <strong>0.25 x 0.25 x 0.25</strong>, so I would expect the geometry to be preserved more closely. Is this amount of shrink considered normal behavior?</p>

---

## Post #4 by @pieper (2025-09-25 12:56 UTC)

<p><a class="mention" href="/u/bserrano">@bserrano</a> - thanks for posting - it’s possible there’s a systemic shift when converting back and forth between representations.  Or it’s possible that the image you posted is related to the resolution and other particularities, such as orientation, since your vessels are small compared to the spacing as <a class="mention" href="/u/chir.set">@chir.set</a> points out..</p>
<p>This would be good to investigate systematically, probably with some kind of test scripts that try various configurations and make it easy to visualize and quantify what’s going on.</p>

---

## Post #5 by @chir.set (2025-09-25 13:01 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="3" data-topic="44560">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Is this amount of shrink considered normal behavior?</p>
</blockquote>
</aside>
<p>In your images, I would say <code>yes</code>.</p>
<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="44560">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>If we try forcing the volume with the <em>“source geometry”</em> option in the Segment Editor</p>
</blockquote>
</aside>
<p>The representation gets worse, that’s what I mentioned above. You may repeat on a new segmentation with a source volume that is first resampled at <code>0.1 x 0.1 x 0.1</code>. If you crop the volume to the region of study before resampling the volume, you may avoid memory warnings.  <code>0.25 x 0.25 x 0.25</code> is already a tight spacing though.</p>

---
