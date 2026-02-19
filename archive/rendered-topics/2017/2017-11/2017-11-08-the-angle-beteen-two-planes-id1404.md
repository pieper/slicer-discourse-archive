---
topic_id: 1404
title: "The Angle Beteen Two Planes"
date: 2017-11-08
url: https://discourse.slicer.org/t/1404
---

# The angle beteen two planes

**Topic ID**: 1404
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/the-angle-beteen-two-planes/1404

---

## Post #1 by @doc-xie (2017-11-08 13:01 UTC)

<p>Hello,<br>
In general,there is only one angle between two planes. In the Angle Planes module,after I calculated the angle between two planes,I got three numbers(Pitch,yaw,roll),what is the meaning about the angles respectively?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cb120ff58bbe880031319f697f32886e731c6c0.jpeg" data-download-href="/uploads/short-url/aWrMEfrG5TFeZ6MjYbqFMonzDKE.jpg?dl=1" title="000" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4cb120ff58bbe880031319f697f32886e731c6c0_2_690x234.jpg" alt="000" data-base62-sha1="aWrMEfrG5TFeZ6MjYbqFMonzDKE" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4cb120ff58bbe880031319f697f32886e731c6c0_2_690x234.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4cb120ff58bbe880031319f697f32886e731c6c0_2_1035x351.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cb120ff58bbe880031319f697f32886e731c6c0.jpeg 2x" data-dominant-color="BEBED8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">000</span><span class="informations">1340×455 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rfenioux (2023-10-27 09:11 UTC)

<p>The transform between two planes can either be described by :</p>
<ul>
<li>one rotation around the intersection line between the planes (= 1 angle + 1 axis vector)</li>
<li>three rotations around the 3 main directions of the reference frame (x,y,z or in RAS coordinate : RL, AP and SI). These are also known as “Euler angles”</li>
</ul>
<p>That second representation is used here.</p>

---
