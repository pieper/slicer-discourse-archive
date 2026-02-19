---
topic_id: 25956
title: "Generate 3D Visualization By Stacking 2D Rgb H E Images"
date: 2022-10-28
url: https://discourse.slicer.org/t/25956
---

# Generate 3D visualization by Stacking 2D RGB H&E Images

**Topic ID**: 25956
**Date**: 2022-10-28
**URL**: https://discourse.slicer.org/t/generate-3d-visualization-by-stacking-2d-rgb-h-e-images/25956

---

## Post #1 by @chokevin8 (2022-10-28 17:10 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 3D Slicer 5.0.3<br>
Expected behavior: N/A<br>
Actual behavior: N/A<br>
Hi, I have 34 H&amp;E (histology) 2-D RGB Images that are in .png file format and I want to stack them to visualize them in 3-D using 3D Slicer. I’ve tried the tutorials for ImageStack, but it automatically turns the stack into grayscale, which is something I don’t want. I’m familiar with Python, but not familiar with the python extension of 3dslicer- is there an example/documentation that I can follow so I can do this? I’ve read previous forum posts about this as well but I do not know where to start. If there’s a way to do it in the app itself (rather than coding in python), that would be even better. Thank you so much!</p>

---

## Post #2 by @pieper (2022-10-28 17:34 UTC)

<p>Did you try unchecking the Grayscale option?  It should do what you want, but be aware that not all features of Slicer support color images.  Also with just 34 slices you won’t get much 3D detail, but it may be all you need.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3490f0413c5078e82f0c8bd38ac048d155f09ec9.png" alt="image" data-base62-sha1="7v1mbdF0OqCdYa8qWlR3b8HigK5" width="233" height="63"></p>

---

## Post #3 by @chokevin8 (2022-10-28 17:37 UTC)

<p>Thanks for the reply, may I ask where this option is?</p>

---

## Post #4 by @muratmaga (2022-10-28 17:44 UTC)

<p>Towards the bottom of the ImageStack’s UI<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/142972be8b6c9c9ca5b52e541a21f4c81fa022e3.png" data-download-href="/uploads/short-url/2SmlOmlEkEZodLy2nSQCNApHcQz.png?dl=1" title="Screen Shot 2022-10-28 at 10.43.17 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/142972be8b6c9c9ca5b52e541a21f4c81fa022e3_2_470x500.png" alt="Screen Shot 2022-10-28 at 10.43.17 AM" data-base62-sha1="2SmlOmlEkEZodLy2nSQCNApHcQz" width="470" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/142972be8b6c9c9ca5b52e541a21f4c81fa022e3_2_470x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/142972be8b6c9c9ca5b52e541a21f4c81fa022e3_2_705x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/142972be8b6c9c9ca5b52e541a21f4c81fa022e3.png 2x" data-dominant-color="E8E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-28 at 10.43.17 AM</span><span class="informations">896×952 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @chokevin8 (2022-10-28 18:42 UTC)

<p>Thank you- I was able to generate a volume, but it obviously wasn’t what I expected. Each RGB 2-D images look like this, and below that is the generated 3-D representation. What would be the best method to reveal the “sides” of the stack so that the entire volume representation can be seen? Currently it is all black and you cannot see any contours of the side, etc. I’m guessing maybe that’s related to the transparency channel (RGBA)? Also, I’m wondering why the top surface image look blurry as well. Could that be related to the 10x downsampling I did to the image? Thank you so much, these questions may sound basic/stupid, but I’m a beginner and I would appreciate all the help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f69d97e3d968d43e0c6e7df779ecd9e0ddd15dc.jpeg" data-download-href="/uploads/short-url/fTBMpNpmzH5UFIWKEZbCFc4SZHK.jpeg?dl=1" title="z0025_25C1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f69d97e3d968d43e0c6e7df779ecd9e0ddd15dc_2_422x500.jpeg" alt="z0025_25C1" data-base62-sha1="fTBMpNpmzH5UFIWKEZbCFc4SZHK" width="422" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f69d97e3d968d43e0c6e7df779ecd9e0ddd15dc_2_422x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f69d97e3d968d43e0c6e7df779ecd9e0ddd15dc_2_633x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f69d97e3d968d43e0c6e7df779ecd9e0ddd15dc_2_844x1000.jpeg 2x" data-dominant-color="EAD2DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">z0025_25C1</span><span class="informations">1920×2270 465 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e26847973cba3b2f21b6b53019a403996c3291d.jpeg" data-download-href="/uploads/short-url/hZYGrzH8gujwT30K7YTlIhaMeGV.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e26847973cba3b2f21b6b53019a403996c3291d_2_690x342.jpeg" alt="Capture.PNG" data-base62-sha1="hZYGrzH8gujwT30K7YTlIhaMeGV" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e26847973cba3b2f21b6b53019a403996c3291d_2_690x342.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e26847973cba3b2f21b6b53019a403996c3291d_2_1035x513.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e26847973cba3b2f21b6b53019a403996c3291d_2_1380x684.jpeg 2x" data-dominant-color="A8A8B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">1433×712 89.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @chokevin8 (2022-10-28 20:41 UTC)

<p>I was actually able to resolve this by myself, marking two previous replies as a solution, thanks!</p>

---

## Post #7 by @curtislisle (2022-10-29 16:50 UTC)

<p>Unfortunately, some of the difficulty you are encountering is because this type of data (a few very large histology slices) is a type of volume which is not the application proglem 3D Slicer is designed to address. There have been several efforts to bring histology data into Slicer over the years because Slicer is so good at managing imagery analysis, but it is still a challenge.</p>
<p>It may be a somewhat different application, but I found this Nature paper to have some discussion about image stack preparation, in case it is helpful: <a href="https://www.nature.com/articles/s41598-020-69163-z" rel="noopener nofollow ugc">https://www.nature.com/articles/s41598-020-69163-z</a></p>
<p>For histology volumes like yours, there are generally large gaps in the depth direction between slices, so this data would benefit from pre-processing before it can be rendered correctly using a traditional volume rendering application, like what is built into Slicer. In your case, the downsampling to 10X does increase blur. The rendering algorithm will also tend to increase blur because it is compiling the visual effect along the rays between the voxels and the viewpoint. Since histology volumes have large white regions at their boundaries, they require a lot of tweaking to the volume rendering transfer functions to eliminate the black borders unless the imagery is pre-processed before rendering to eliminate the non-tissue areas. Since you have this data in Slicer already, try adjusting the alpha channel of the volume rendering so that voxels of the highest-intensity are completely transparent. This will make a bit of your tissue become transparent along with the borders, but it should be closer to what you are looking for. Good luck!</p>

---

## Post #8 by @lassoan (2022-10-30 12:39 UTC)

<aside class="quote no-group" data-username="curtislisle" data-post="7" data-topic="25956">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/48db29/48.png" class="avatar"> curtislisle:</div>
<blockquote>
<p>using a traditional volume rendering application, like what is built into Slicer. In your case, the downsampling to 10X does increase blur</p>
</blockquote>
</aside>
<p>What downsampling do you mean? Slicer directly displays the image at the actual resolution. There is no resolution limit in the CPU volume renderer. The GPU volume renderer may have hardware limitations for maximum texture but the image can then be cropped to the region of interest or tiling can be enabled by a few lines of Python script.</p>

---
