# Spherical shape detection on a 3D surface

**Topic ID**: 41532
**Date**: 2025-02-06
**URL**: https://discourse.slicer.org/t/spherical-shape-detection-on-a-3d-surface/41532

---

## Post #1 by @MReza (2025-02-06 17:41 UTC)

<p>Hello everyone,</p>
<p>We are working on a project where we glue spherical markers onto a tissue, and 3D scan both the tissue and the markers to capture the initial position. Then, we apply a force to deform the tissue and perform a second scan. The goal is to measure the deformation using these markers.</p>
<p>Is there a way in 3D Slicer (or elsewhere) where we can click on the markers, and the software detects the spherical shape and returns the centroid? When I use simple markup in 3D Slicer, it doesn’t necessarily return the centroid of our markers.</p>
<p>Thanks for any help</p>

---

## Post #2 by @pieper (2025-02-06 17:49 UTC)

<p>I’ve done a project like this in the past by making a “virtual” scan of the sphere and registering it to each of the real spheres.  As long as your scanned spheres are a different density from the surrounding tissue this can be very robust and accurate.</p>

---

## Post #3 by @MReza (2025-02-06 18:22 UTC)

<p>Thanks for your reply! May I ask how you registered your virtual markers to the real scans?</p>

---

## Post #4 by @pieper (2025-02-06 18:28 UTC)

<aside class="quote no-group" data-username="MReza" data-post="3" data-topic="41532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/8baadc/48.png" class="avatar"> MReza:</div>
<blockquote>
<p>May I ask how you registered your virtual markers to the real scans?</p>
</blockquote>
</aside>
<p>In that particular case I looked at the (mostly uniform) intensity of the spheres in the real scan and then programmatically made a shere of the same intensity and size with a little background intensity border around it.  I also blurred it a bit.  Then I just did a simple optimizer that, given a reasonable starting point, just kept tweaking the center of the sphere to minimize the summed intensity differences.  I started from a user click near the target, but it would also be possible to do an exhaustive search for things that look like spheres.  In my case the optimizer converged very quickly.</p>
<p>Of course there are many possible complications, like poor resolution, artifacts, or the tissue looking similar to the spheres in some way.</p>

---
