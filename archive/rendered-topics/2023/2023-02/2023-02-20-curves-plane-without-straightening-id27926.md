# Curves plane without straightening

**Topic ID**: 27926
**Date**: 2023-02-20
**URL**: https://discourse.slicer.org/t/curves-plane-without-straightening/27926

---

## Post #1 by @mohammed_alshakhas (2023-02-20 12:43 UTC)

<p>Is it possible to create  a curved plane without being straightened ?</p>
<p>Thanks</p>

---

## Post #2 by @RafaelPalomar (2023-02-21 05:50 UTC)

<p>In <a href="https://github.com/ALive-research/Slicer-Liver" rel="noopener nofollow ugc">Slicer-Liver</a> we use Bezier surfaces, which can be defined by sets of control points.</p>
<p>Bezier surfaces can be initialized as planes if all control points lie on a plane:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69bb59f086f4c300c4064b0a7675deec52f38954.jpeg" data-download-href="/uploads/short-url/f5lx1Whg9zRVyMScOyP93mxOOeE.jpeg?dl=1" title="Slicer-Liver_screenshot_01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69bb59f086f4c300c4064b0a7675deec52f38954_2_281x256.jpeg" alt="Slicer-Liver_screenshot_01" data-base62-sha1="f5lx1Whg9zRVyMScOyP93mxOOeE" width="281" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69bb59f086f4c300c4064b0a7675deec52f38954_2_281x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69bb59f086f4c300c4064b0a7675deec52f38954_2_421x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69bb59f086f4c300c4064b0a7675deec52f38954_2_562x512.jpeg 2x" data-dominant-color="ECEEEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-Liver_screenshot_01</span><span class="informations">1194×1060 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and can take any arbitrary form (depending of the number of control points):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5888b115519ff05f08fd18ffefce59617368e9de.png" data-download-href="/uploads/short-url/cDcSrlVPDKZSO49QCV2XpuhkXHo.png?dl=1" title="Slicer-Liver_screenshot_04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5888b115519ff05f08fd18ffefce59617368e9de_2_316x256.png" alt="Slicer-Liver_screenshot_04" data-base62-sha1="cDcSrlVPDKZSO49QCV2XpuhkXHo" width="316" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5888b115519ff05f08fd18ffefce59617368e9de_2_316x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5888b115519ff05f08fd18ffefce59617368e9de_2_474x384.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5888b115519ff05f08fd18ffefce59617368e9de_2_632x512.png 2x" data-dominant-color="E0E5E6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-Liver_screenshot_04</span><span class="informations">1045×826 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There is more information in our repository <a href="https://github.com/ALive-research/Slicer-Liver" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</a> and our Project Week page <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/" class="inline-onebox" rel="noopener nofollow ugc">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a></p>
<p><a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a>, what is your application? Would this be of any help?</p>

---

## Post #3 by @mohammed_alshakhas (2023-02-22 09:04 UTC)

<p>Looks very interesting , I tried the module but couldn’t figure out where to start</p>
<p>I’m planning to use it for visualizing mandible .<br>
Mandible lesions or certain anatomy visualization is better seen in curved planes instead of looking at slice a time .</p>

---

## Post #4 by @RafaelPalomar (2023-02-22 13:06 UTC)

<p>There is documentation in here: <a href="https://github.com/ALive-research/Slicer-Liver" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</a></p>
<p>And also a video tutorial here: <a href="https://www.youtube.com/watch?v=oRu624mtQZE" class="inline-onebox" rel="noopener nofollow ugc">Slicer-liver tutorial - YouTube</a></p>
<p>For your specific application, do you mean that you would like to slice the image volume using these curved geometries? For Slicer-Liver we don’t map the volume information in the surface or change the slice information.</p>

---

## Post #5 by @johny723 (2024-01-03 21:23 UTC)

<p>Hi. I need to create a bezier surface. Is there any video tutorial showing how to actually do it? How do I make my own set of control points in an arbitrary organ and then create a bezier surface ? Thanks</p>

---

## Post #6 by @lassoan (2024-01-04 04:28 UTC)

<p>Have you tried following the video tutorial described in the post above?<br>
You can also try markup provided by SurfaceMarkups extension.</p>

---
