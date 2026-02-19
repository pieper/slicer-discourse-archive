---
topic_id: 20139
title: "Image Orientation Issue"
date: 2021-10-13
url: https://discourse.slicer.org/t/20139
---

# Image orientation issue

**Topic ID**: 20139
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/image-orientation-issue/20139

---

## Post #1 by @Vinny (2021-10-13 19:14 UTC)

<p>Hello,</p>
<p>I recently started using Slicer 4.13-2021-10-10 and noticed that some images are loading in a near ac-pc alignment even though they were not acquired in that way, and no ac-pc transformation has been applied.  I’ve used earlier versions of Slicer, e.g., Slicer 4.11-20200930 with no issue on image orientation.</p>
<p>Here is an example:</p>
<p>Screenshot is from Slicer 4.11-20200930 that displays the original orientation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3388ff3d0a83dc79f84e222c6f97733d0d461c17.jpeg" data-download-href="/uploads/short-url/7lTRG0bXo6VUjdyFhKgPbrL1cxx.jpeg?dl=1" title="Screenshot3dSlicer4.11-raw" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3388ff3d0a83dc79f84e222c6f97733d0d461c17_2_690x393.jpeg" alt="Screenshot3dSlicer4.11-raw" data-base62-sha1="7lTRG0bXo6VUjdyFhKgPbrL1cxx" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3388ff3d0a83dc79f84e222c6f97733d0d461c17_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3388ff3d0a83dc79f84e222c6f97733d0d461c17_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3388ff3d0a83dc79f84e222c6f97733d0d461c17_2_1380x786.jpeg 2x" data-dominant-color="787778"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot3dSlicer4.11-raw</span><span class="informations">1850×1055 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Screenshot from Slicer 4.11-20200930 after ac-pc transformation that displays correct orientation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d22392059f97ab860959f3c8ea30d92a58f670c.jpeg" data-download-href="/uploads/short-url/dhTJ6yxradF1EVQmnsx6xsmNyZC.jpeg?dl=1" title="Screenshot3dSlicer4.11-acpc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d22392059f97ab860959f3c8ea30d92a58f670c_2_690x393.jpeg" alt="Screenshot3dSlicer4.11-acpc" data-base62-sha1="dhTJ6yxradF1EVQmnsx6xsmNyZC" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d22392059f97ab860959f3c8ea30d92a58f670c_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d22392059f97ab860959f3c8ea30d92a58f670c_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d22392059f97ab860959f3c8ea30d92a58f670c_2_1380x786.jpeg 2x" data-dominant-color="787776"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot3dSlicer4.11-acpc</span><span class="informations">1850×1055 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Screenshot from Slicer 4.13-2021-10-10 (with no ac-pc transformation applied; only original image loaded):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db99bb88df89576ec511457c3f3fac004072a0d3.jpeg" data-download-href="/uploads/short-url/vkFW3Xkt7zXpqxRxtKFVrCbsP2X.jpeg?dl=1" title="Screenshot3dSlicer4.13_raw" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db99bb88df89576ec511457c3f3fac004072a0d3_2_690x393.jpeg" alt="Screenshot3dSlicer4.13_raw" data-base62-sha1="vkFW3Xkt7zXpqxRxtKFVrCbsP2X" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db99bb88df89576ec511457c3f3fac004072a0d3_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db99bb88df89576ec511457c3f3fac004072a0d3_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db99bb88df89576ec511457c3f3fac004072a0d3_2_1380x786.jpeg 2x" data-dominant-color="787777"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot3dSlicer4.13_raw</span><span class="informations">1850×1055 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The ac-pc fiducials do not line up for the last scan, which makes sense since no ac-pc transformation has been applied.  When I apply the ac-pc transformation,  the ac-pc fiducials do align but the image display is oriented obliquely since all three dimensions are moving in the Data Probe window when moving the cursor:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf822379a61fbb21cf7b86cc1a8b82dba97f7a58.jpeg" data-download-href="/uploads/short-url/rka158OctphqdluSNKOl1C3zOyY.jpeg?dl=1" title="Screenshot-3dSlicer4.13-2021-1010-acpc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf822379a61fbb21cf7b86cc1a8b82dba97f7a58_2_690x393.jpeg" alt="Screenshot-3dSlicer4.13-2021-1010-acpc" data-base62-sha1="rka158OctphqdluSNKOl1C3zOyY" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf822379a61fbb21cf7b86cc1a8b82dba97f7a58_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf822379a61fbb21cf7b86cc1a8b82dba97f7a58_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf822379a61fbb21cf7b86cc1a8b82dba97f7a58_2_1380x786.jpeg 2x" data-dominant-color="787877"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-3dSlicer4.13-2021-1010-acpc</span><span class="informations">1850×1055 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any idea on how to get the image to correctly along the ac-pc axis after transformation like the earlier Slicer version?</p>
<p>Thanks for your help,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2021-10-13 20:42 UTC)

<p>This post should answer your questions:</p>
<aside class="quote quote-modified" data-post="2" data-topic="20092">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/question-about-display-in-slicer/20092/2">Slice view orientation of oblique/rotated volumes - aligned to volume or anatomical axes?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In earlier Slicer versions, slice views were initialized to be aligned with anatomical axes (as defined when the patient was scanned). In recent Slicer Preview Releases we switched to aligning slice views with voxel arrays because this seems to be what most users expect. 
You can switch between the two orientations using <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controls</a>: 

choose an anatomical plane using the “Slice orientation” selector to align with anatomical axes
click “Rotate to volume plane” button to snap the slice pl…
  </blockquote>
</aside>

<p>Let us know if anything is not clear.</p>

---

## Post #3 by @Vinny (2021-10-13 21:31 UTC)

<p>Thanks Andras, this worked.  I noticed in the new Slicer version, the ‘Slicer orientation’ drop-down menu defaults to ‘Reformat’.  I changed the ‘Slice orientation’ selector to ‘Axial’  as you suggested and this displays the image along the anatomical axes.  However, clicking ‘Rotate to volume plane’ reverts the orientation back to ‘Reformat’.  But, the first step of changing the ‘Slicer orientation’ seems to have solved my problem.</p>
<p>Vinny</p>

---

## Post #4 by @lassoan (2021-10-14 05:22 UTC)

<p>OK, so everything works as expected then. You are free to choose which default alignment you prefer (anatomical axes or voxel axes) by right-clicking the eye icon of the volume node in Data module and checking/unchecking the “Reset view orientation on show” checkbox.</p>

---
