# Measurement of the vessel wall thickness

**Topic ID**: 14337
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/measurement-of-the-vessel-wall-thickness/14337

---

## Post #1 by @Andreas (2020-10-30 16:39 UTC)

<p>I still have problems measuring my vessel wall thickness. Can you make marker points smaller so that a more precise measurement is possible? Due to the large marking points, there is also a great risk of measurement deviation.</p>
<p>Another problem with the measurement is the placement of the measuring points. I have little control over where the measuring points are placed and whether they also run in a horizontal line, since the measuring line between the marking points cannot be recognized by the vessel model.<br>
Readjustment is made considerably more difficult.</p>

---

## Post #2 by @lassoan (2020-10-30 19:02 UTC)

<p>For precise point marking, I would recommend Glyph Type → “Cross2D” or “CrossDot2D” or “StarBurst2D” and adjustment of Line thickness, maybe also Opacity.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa13a3e221150c503cde11568910706bf83ef9c1.png" data-download-href="/uploads/short-url/ogzfqyGp3mwADcZmZxsl7JpqfWp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa13a3e221150c503cde11568910706bf83ef9c1.png" alt="image" data-base62-sha1="ogzfqyGp3mwADcZmZxsl7JpqfWp" width="536" height="500" data-dominant-color="403F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">655×611 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="14337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>I have little control over where the measuring points are placed and whether they also run in a horizontal line, since the measuring line between the marking points cannot be recognized by the vessel model</p>
</blockquote>
</aside>
<p>Measuring at a few positions will be inevitably quite inaccurate and subjective. It may be more accurate to segment the structure in 3D or draw curves on two sides and compute min/max/mean distance between the contours with a 2-3-line Python script.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6393f4522ecf367c51ff13671a0c9ad672d044f0.jpeg" data-download-href="/uploads/short-url/ecUg8RlOTVIzHhLcGwVhtYjRJa8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6393f4522ecf367c51ff13671a0c9ad672d044f0_2_690x368.jpeg" alt="image" data-base62-sha1="ecUg8RlOTVIzHhLcGwVhtYjRJa8" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6393f4522ecf367c51ff13671a0c9ad672d044f0_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6393f4522ecf367c51ff13671a0c9ad672d044f0_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6393f4522ecf367c51ff13671a0c9ad672d044f0.jpeg 2x" data-dominant-color="2A2A2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1055×563 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Vessel wall thickness is typically not visible on clinical images (except maybe IVUS or OCT). What imaging modality do you work with? Can you post a screenshot of a typical image and what you want to measure? Why do you want to measure vessel wall thickness? What accuracy is needed? What is the resolution of your images?</p>

---

## Post #3 by @Andreas (2020-10-30 19:08 UTC)

<p>Thank you for the quick response and illustration.</p>

---

## Post #4 by @Andreas (2020-11-04 07:22 UTC)

<p><strong>1) What imaging modality do you use?</strong></p>
<p>my imaging modality is brain vessel angiography.</p>
<p><strong>2) Can you post a screenshot of a typical image and its measurements?</strong></p>
<p>Attached you can see the screenshot with the attempt to measure.<br>
Another problem is that I cannot create an exact cutting path, but only cut freely with the scissors, which leads to serious measurement errors.</p>
<p><strong>3) Why do you want to measure the wall thickness of the container?</strong></p>
<p>The vessel should ultimately be printed three-dimensionally as a silicone model. With a calculated expansion behavior, which I only have from a certain wall thickness, so it is important not to get too large nominal deviations of the “shell”. (continuous and uniform wall thickness in the entire course of the vessel)</p>
<p><strong>4) What accuracy is required?</strong></p>
<p>I would like to see how exact the set wall thickness (e.g. 0.5 mm) actually is in different sections and places.</p>
<p>I try, as you recommended, to choose the “Spacing Scale” 4-6 x smaller with the help of “Crop Volume” in order to get the most exact wall thickness possible.</p>
<p><strong>5) What is the resolution of your pictures?</strong></p>
<p>Unfortunately, I do not know the resolution of my clinical DICOM data sets. You may be able to tell me where I can find it.</p>
<p>Many thanks for your help</p>
<p>Sincerely yours</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86d4dc769759947c9e984b017de9cbba4d83ce27.jpeg" data-download-href="/uploads/short-url/jeM26N3O9dhFTXUfLV4OEJuVk5F.jpeg?dl=1" title="Unnamed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86d4dc769759947c9e984b017de9cbba4d83ce27_2_606x499.jpeg" alt="Unnamed" data-base62-sha1="jeM26N3O9dhFTXUfLV4OEJuVk5F" width="606" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86d4dc769759947c9e984b017de9cbba4d83ce27_2_606x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86d4dc769759947c9e984b017de9cbba4d83ce27_2_909x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86d4dc769759947c9e984b017de9cbba4d83ce27.jpeg 2x" data-dominant-color="575667"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unnamed</span><span class="informations">1130×932 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-11-10 21:28 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="4" data-topic="14337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Another problem is that I cannot create an exact cutting path, but only cut freely with the scissors, which leads to serious measurement errors.</p>
</blockquote>
</aside>
<p>You don’t need to cut the model. You can measure directly in slice views. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">rotate the slice views</a> using Ctrl+Alt+Left-click-and-drag (after enabling “Slicer intersections” in <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=crosshair%20selection#view-cross-reference">crosshair toolbar</a>), or reorient your slice view to show the exact cross-section of the vessel automatically using Cross-section analysis module (in SlicerVMTK extension).</p>
<aside class="quote no-group" data-username="Andreas" data-post="4" data-topic="14337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Unfortunately, I do not know the resolution of my clinical DICOM data sets. You may be able to tell me where I can find it.</p>
</blockquote>
</aside>
<p>See Volumes module / Volume information section / Spacing. To measure a distance accurately, you would need approximately a magnitude smaller voxel size (it would still mean that you have 10-20% error in the measurement, just because of limited spatial resolution). So, for accurate wall thickness measurement of 0.5mm, you would need voxel size of 0.05mm or smaller, which I think is beyond of what is feasible in current clinical practice. To improve accuracy, you may measure at thousands of positions instead of a handpicked few, by segmenting the inner and outer surface of the vessel and compute average surface-to-surface distance.</p>

---
