# Segmentation of artificially created surfaces

**Topic ID**: 27662
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/segmentation-of-artificially-created-surfaces/27662

---

## Post #1 by @JonathanLV (2023-02-06 14:09 UTC)

<p>Hello,<br>
I’ve generated a segment of an endocast from a fossil. The thing is that there are holes in the skull I’ve used, so the module tried to interpolate the surface, creating artificial part in this segment. I’d like to find a way to highlight these parts with an additional segment probably. Any suggestions?<br>
In the following image you may find said part represented as a bulge with flat surfaces or the bottom part of it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d56ac06b699685da3c696dc3a46f9093507465.jpeg" data-download-href="/uploads/short-url/zvhEHw3sQTUNJGOGqT7Ws9sQ75j.jpeg?dl=1" title="001_frontal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d56ac06b699685da3c696dc3a46f9093507465_2_690x388.jpeg" alt="001_frontal" data-base62-sha1="zvhEHw3sQTUNJGOGqT7Ws9sQ75j" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d56ac06b699685da3c696dc3a46f9093507465_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d56ac06b699685da3c696dc3a46f9093507465_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d56ac06b699685da3c696dc3a46f9093507465_2_1380x776.jpeg 2x" data-dominant-color="EEEEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001_frontal</span><span class="informations">1920×1080 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2023-02-06 14:14 UTC)

<p>You can distinguish regions that hole filling adds by computing distance between the mesh with hole fllling and the mesh without the filling. You can use ModelToModelDistance extension to compute the distance and color the surface with it.</p>
<p>What is your overall goal? Colored 3D printing, surface area measurement, …?</p>
<p>Did you use “Wrap Solidify” effect (provided by SurfaceWrapSolidify extension) to automatically create a solid endocast from the skull?</p>

---

## Post #3 by @JonathanLV (2023-02-06 14:24 UTC)

<p>Thank you so much Andras.<br>
Will try your suggestion, although I got to say that I’ve already found some sort of a solution. This solution was to manually go with the paint brush in sphere mode with a threshold set for covering empty voxels and draw only within the endocast segment. Not the best solution and took me forever, but somehow worked.<br>
The goal is indeed to get this in the end to 3D printing, but initially I just wanted to show what parts are artifacts, so they could be ignored. I’ve used the Wrap Solidify indeed! What a great tool!</p>

---
