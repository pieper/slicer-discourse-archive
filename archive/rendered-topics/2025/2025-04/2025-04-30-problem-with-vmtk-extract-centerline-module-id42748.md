# Problem with VMTK extract centerline module

**Topic ID**: 42748
**Date**: 2025-04-30
**URL**: https://discourse.slicer.org/t/problem-with-vmtk-extract-centerline-module/42748

---

## Post #1 by @francesca_flore (2025-04-30 12:53 UTC)

<p>It seems that the generated centerline does not start and end from the endpoints I give it, but it is as if it is cut before. Any idea?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1368d0d2a9c38c959d0680c081e244e80a011f.png" data-download-href="/uploads/short-url/jZaqGpDC3M78ku61QupotYMT08D.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1368d0d2a9c38c959d0680c081e244e80a011f_2_533x500.png" alt="image" data-base62-sha1="jZaqGpDC3M78ku61QupotYMT08D" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1368d0d2a9c38c959d0680c081e244e80a011f_2_533x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1368d0d2a9c38c959d0680c081e244e80a011f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1368d0d2a9c38c959d0680c081e244e80a011f.png 2x" data-dominant-color="8483A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">617×578 51.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Deep_Learning (2025-04-30 14:13 UTC)

<p>That is expected behavior.</p>

---

## Post #3 by @francesca_flore (2025-04-30 14:20 UTC)

<p>but I need the centerline from the two assigned points. I am missing a part because it is not totally attached to the assigned points.</p>

---

## Post #4 by @mikebind (2025-05-01 17:09 UTC)

<p>The problem is that the endpoints you provided are not on the “centerline” of the object you provided.  The centerline returned by VMTK runs along the voronoi medial surface of the object.  The endpoints you chose are not on this surface.  I assume the physical object you are interested in extends beyond the two flat faces that you put the endpoints on, but those are the boundaries of your image.  You could try adding two cylindrical extensions to those faces (one for each face) with your endpoints at the center of the cylinder face against the object, and then run centerline extraction on the augmented object.  The extensions should ensure that your endpoints then lie on the voronoi medial surface, and you can see if the extracted centerline will work for you as desired.</p>

---

## Post #5 by @francesca_flore (2025-05-05 07:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7988d703ca13a3115e795a0b802d87f9684ef290.png" data-download-href="/uploads/short-url/hl8X1IS4ZYuUjjALIEoTalkY0s8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7988d703ca13a3115e795a0b802d87f9684ef290_2_588x499.png" alt="image" data-base62-sha1="hl8X1IS4ZYuUjjALIEoTalkY0s8" width="588" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7988d703ca13a3115e795a0b802d87f9684ef290_2_588x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7988d703ca13a3115e795a0b802d87f9684ef290.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7988d703ca13a3115e795a0b802d87f9684ef290.png 2x" data-dominant-color="9E9BB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">685×582 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think the problem is better understood here. I have a valve model and I would like the centerline along its entire section, but the centerline generated is shorter than it should be.</p>

---

## Post #6 by @chir.set (2025-05-05 08:39 UTC)

<p>Since you model is very harmonious, you may try this:</p>
<ul>
<li>use <code>Edit centerline</code> module to generate a tube</li>
<li>fit the tube to the ends of your model</li>
<li>use the spline of the tube as centerline</li>
<li>or create a new centerline in the module.</li>
</ul>

---

## Post #7 by @francesca_flore (2025-05-06 07:46 UTC)

<p>Finally for the valve model I solved it by generating the centerline.vtk  myself. But how is it possible that for the vessel segments the centerline seems to be wrong? As in the attached photo, the centerline seems to go to one side and is not centered and does not reach the endpoints.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f554ef995641b0a7b69fde288726232f2ec2714f.jpeg" data-download-href="/uploads/short-url/z0iXbHN8AFBodOSN5QEqSIzeddR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f554ef995641b0a7b69fde288726232f2ec2714f.jpeg" alt="image" data-base62-sha1="z0iXbHN8AFBodOSN5QEqSIzeddR" width="547" height="500" data-dominant-color="8398CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">574×524 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
