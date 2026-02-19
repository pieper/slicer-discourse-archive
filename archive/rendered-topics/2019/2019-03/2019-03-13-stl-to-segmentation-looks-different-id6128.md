---
topic_id: 6128
title: "Stl To Segmentation Looks Different"
date: 2019-03-13
url: https://discourse.slicer.org/t/6128
---

# STL to Segmentation Looks different

**Topic ID**: 6128
**Date**: 2019-03-13
**URL**: https://discourse.slicer.org/t/stl-to-segmentation-looks-different/6128

---

## Post #1 by @brhoom (2019-03-13 10:30 UTC)

<p>Hi,<br>
I am trying to fix and segment an STL model to multiple parts.</p>
<p>Here is what I did</p>
<ol>
<li>An STL is loaded as segmentation.</li>
<li>Segmentation is exported to labelmap. I believe, this is the step where things go wrong.</li>
<li>The labelmap is saved and the saved file is loaded as volume.</li>
<li>I used the loaded volume as master volume and did thresholding. I expected to get a result similar to the original model but I get something different.</li>
</ol>
<p>The green color represents the original model, the blue color represents the thresholding result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246510886f40486a356a337dc9051f98cb2a5e44.png" data-download-href="/uploads/short-url/5bXIz58XnqOu8sp2Lfhx3wrKbLS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246510886f40486a356a337dc9051f98cb2a5e44_2_573x500.png" alt="image" data-base62-sha1="5bXIz58XnqOu8sp2Lfhx3wrKbLS" width="573" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246510886f40486a356a337dc9051f98cb2a5e44_2_573x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246510886f40486a356a337dc9051f98cb2a5e44.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246510886f40486a356a337dc9051f98cb2a5e44.png 2x" data-dominant-color="8A8A9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">679×592 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the image and the original model in the 3D view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6ff8eff35a66ddf06ac248f5c86a97212b351c00.png" data-download-href="/uploads/short-url/fYylnWWXa7RGHnD0Dz7QMf2hQek.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6ff8eff35a66ddf06ac248f5c86a97212b351c00_2_587x500.png" alt="image" data-base62-sha1="fYylnWWXa7RGHnD0Dz7QMf2hQek" width="587" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6ff8eff35a66ddf06ac248f5c86a97212b351c00_2_587x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6ff8eff35a66ddf06ac248f5c86a97212b351c00.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6ff8eff35a66ddf06ac248f5c86a97212b351c00.png 2x" data-dominant-color="8B968D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">629×535 53.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2019-03-13 12:45 UTC)

<p>It seems that your model is not a closed surface (I can see a large hole in the second screenshot, and there may be others). Can you try to do a “Fill holes” in the Surface Toolbox module?</p>

---

## Post #3 by @brhoom (2019-03-13 12:50 UTC)

<p>Yes, it is not a closed surface. That is why I am trying to fix it. Unfortunately, filling holes does not work even with the maximum number.</p>

---

## Post #4 by @cpinter (2019-03-13 13:12 UTC)

<p>A simple idea that I have is to rotate the model with a transform, then harden, then try to convert to labelmap. The converter probably works in a set direction, so there could be an orientation where it doesn’t leak out.</p>

---

## Post #5 by @lassoan (2019-03-13 13:16 UTC)

<p>How did you create this STL file?</p>
<p>Are triangles actually missing or just oriented incorrectly? (do you still see holes if you load it as a model and in Models / Display / 3D Display / Visible sides you choose “All”?)</p>
<p>You may also try to fix the model using Surface Toolbox module. If that does not help you can try mesh correction options in MeshLab, MeshMixer, Blender, etc. before importing into Slicer.</p>

---

## Post #6 by @brhoom (2019-03-13 13:19 UTC)

<p>The original STL file has large holes I was hopping to fix them via segmentation option. I will try fix it outside Slicer.</p>

---
