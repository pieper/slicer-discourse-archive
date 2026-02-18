# Transform: scale

**Topic ID**: 8731
**Date**: 2019-10-10
**URL**: https://discourse.slicer.org/t/transform-scale/8731

---

## Post #1 by @Melodicpinpon (2019-10-10 12:39 UTC)

<p>Hellohello,</p>
<p>Is there a way to scale an imported image within 3D slicer?<br>
I try to capture a 3D volume render of a patient’s head based on the point of view of a picture taken from somebody else. The purpose is to make the point of view match in order to use both sources for several illustrations.</p>
<p>By the way, is it possible to make the 3D render transparent?</p>

---

## Post #2 by @lassoan (2019-10-10 23:42 UTC)

<p>Can you show an example visualization that you would like to achieve?</p>
<p>If you want to overlay a 3D rendering over a 2D photo then you can do the followings:</p>
<ul>
<li>load a 3D volume, set up volume rendering with a transparent preset, such as CT X-ray</li>
<li>load a photo and show the slice view in 3D view</li>
<li>rotate the 3D view to see the photo from a good angle</li>
<li>apply a transform to the 3D volume to align it with the background photo</li>
</ul>
<p>By default, Slicer uses a perspective camera so you don’t need to scale the 3D volume, just move it closer to the camera to make it appear bigger compared to the photo. If you want, you can change the scale of the volume in Volumes module / Volume information section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/638b299016549301bc803475adc558f723cabcb3.jpeg" data-download-href="/uploads/short-url/ecBqg6xXXUEUWf1mLnmwkSKahaP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/638b299016549301bc803475adc558f723cabcb3_2_690x438.jpeg" alt="image" data-base62-sha1="ecBqg6xXXUEUWf1mLnmwkSKahaP" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/638b299016549301bc803475adc558f723cabcb3_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/638b299016549301bc803475adc558f723cabcb3_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/638b299016549301bc803475adc558f723cabcb3.jpeg 2x" data-dominant-color="BFB9B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1128×717 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @pieper (2019-10-11 00:35 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"></p>
<p>(<img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"><img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"> to meet the 20 character limit <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">)</p>

---

## Post #4 by @Melodicpinpon (2019-10-11 08:15 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ae27be650a187640be4da088588bc0abb1fdc5b.jpeg" data-download-href="/uploads/short-url/3PPExHeIqarz7rcZ1wWVOWXWquf.jpeg?dl=1" title="Marina" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ae27be650a187640be4da088588bc0abb1fdc5b_2_477x500.jpeg" alt="Marina" data-base62-sha1="3PPExHeIqarz7rcZ1wWVOWXWquf" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ae27be650a187640be4da088588bc0abb1fdc5b_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ae27be650a187640be4da088588bc0abb1fdc5b_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ae27be650a187640be4da088588bc0abb1fdc5b_2_954x1000.jpeg 2x" data-dominant-color="E2CBBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Marina</span><span class="informations">1280×1340 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!<br>
I love this program</p>

---

## Post #5 by @lassoan (2019-10-11 11:35 UTC)

<p>Nice. To remove the woodgrain artifact from the volume rendered CT, you can enable “Surface smoothing” or set Quality to “Maximum” in volume rendering module’s advanced section (Techniques tab).</p>
<p>You can make the volume more transparent by moving control points on “Scalar Opacity Mapping” function lower (if you find it hard to precisely manipulate the points by your mouse then you can select a point and type the opacity “O” value in the top-right corner of the function editor).</p>

---

## Post #6 by @timeanddoctor (2019-10-20 13:35 UTC)

<p>Can I set up the picture with a transparent view?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed858f32896f0a009740e377c191fd280979d070.jpeg" alt="" data-base62-sha1="xTdje5jQSoQ4NIyHiC1dQLz9yKY" role="presentation" width="477" height="500"></p>

---

## Post #7 by @lassoan (2019-10-21 04:02 UTC)

<p>I would recommend to simply put the semi-transparent 3D rendering in front of the slice view, but for example you can make the red slice view transparent by copy-pasting this to the Python console (before showing the slice view in 3D):</p>
<p><code>getNode("Red Volume Slice").GetDisplayNode().SetOpacity(0.5)</code></p>
<p>See some discussion about this feature here: <a href="https://discourse.slicer.org/t/3d-view-can-the-image-slices-be-made-semi-transparent/8713" class="inline-onebox">Can the image slices be made semi-transparent in 3D view?</a></p>

---
