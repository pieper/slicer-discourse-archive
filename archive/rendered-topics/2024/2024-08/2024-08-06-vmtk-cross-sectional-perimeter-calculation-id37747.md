# VMTK - cross-sectional perimeter calculation

**Topic ID**: 37747
**Date**: 2024-08-06
**URL**: https://discourse.slicer.org/t/vmtk-cross-sectional-perimeter-calculation/37747

---

## Post #1 by @JoGervCon (2024-08-06 21:59 UTC)

<p>Hi, I am using the VMTK extension to calculate the cross sectional area of arteries. Is there a function that can calculate the perimeter of the cross sectional area along the centerline?</p>

---

## Post #2 by @chir.set (2024-08-07 07:00 UTC)

<aside class="quote no-group" data-username="JoGervCon" data-post="1" data-topic="37747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jogervcon/48/66811_2.png" class="avatar"> JoGervCon:</div>
<blockquote>
<p>calculate the perimeter</p>
</blockquote>
</aside>
<p>It is (π x CEDiameter).</p>

---

## Post #3 by @JoGervCon (2024-08-07 11:58 UTC)

<p>Hi! Sorry, I should’ve been more specific. Is there a way to find the perimeter of irregularly shaped cross-sectional areas (along centerline), especially if it is not a circle? Additionally, would there be a way to automate this process to find the perimeter along the centerline of a cross-sectional area, similar to an outputted table? I tired using the markup tool “closed curve” to get as close as I can to the perimeter. But I was wondering if there was a faster/automated way. Thank you!</p>

---

## Post #4 by @chir.set (2024-08-08 17:26 UTC)

<aside class="quote no-group" data-username="JoGervCon" data-post="3" data-topic="37747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jogervcon/48/66811_2.png" class="avatar"> JoGervCon:</div>
<blockquote>
<p>especially if it is not a circle?</p>
</blockquote>
</aside>
<p>You can use vtkvmtkPolyDataBoundaryExtractor to create a polydata where point ids are contiguous. The input is a polydata with co-planar points. You can next easily loop through the points of the output to tally up the distance between successive points, the result is the perimeter.</p>
<p>It works with complex input also, like below. The yellow outline is not produced by that class, it’s just a visualisation model from the output.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43ee913f585ba5815add5c3d911f547683e0e3c8.png" alt="PolyData_Boundary_Ordered" data-base62-sha1="9GX7mvBI7oaNYNSe6bVLZyIT3G8" width="382" height="364"></p>
<p>What clinical inferences can you draw from this quantity?</p>

---
