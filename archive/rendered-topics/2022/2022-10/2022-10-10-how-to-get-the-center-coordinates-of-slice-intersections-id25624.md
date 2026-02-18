# How to get the center coordinates of Slice intersections

**Topic ID**: 25624
**Date**: 2022-10-10
**URL**: https://discourse.slicer.org/t/how-to-get-the-center-coordinates-of-slice-intersections/25624

---

## Post #1 by @miniminic (2022-10-10 07:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/003519931b3c86ae57839fbdb6ef6acede3d3ec7.jpeg" data-download-href="/uploads/short-url/1PLuylSJl0m6udMOyfs5XvedSv.jpeg?dl=1" title="屏幕截图 2022-10-10 155740" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/003519931b3c86ae57839fbdb6ef6acede3d3ec7_2_289x499.jpeg" alt="屏幕截图 2022-10-10 155740" data-base62-sha1="1PLuylSJl0m6udMOyfs5XvedSv" width="289" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/003519931b3c86ae57839fbdb6ef6acede3d3ec7_2_289x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/003519931b3c86ae57839fbdb6ef6acede3d3ec7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/003519931b3c86ae57839fbdb6ef6acede3d3ec7.jpeg 2x" data-dominant-color="4F454C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-10-10 155740</span><span class="informations">397×686 24.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2022-10-10 11:29 UTC)

<p>Take a look at the Slicer script repository linked below to see if this is what you are looking for</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view</a></p>

---

## Post #3 by @miniminic (2022-10-11 04:04 UTC)

<p>I figured out how to get the center position of crosshair, but I didn’t figure out how to get the center position of Slice intersections. The feature I want to implement now is that when Slice intersections move,crosshair moves with them and their center points are always in the same place. When Slice intersections move as a whole, I can easily move them to the mouse position. The problem now is that I can’t get the central position of Slice intersections when the individual intersectingSliceNode moves. Thanks</p>

---

## Post #4 by @lassoan (2022-10-19 06:12 UTC)

<p>In general slices do not intersect each other in a single point (there may be 0, 1, or several intersection points), so in general I would not recommend to depend on it.</p>
<p>However, it is quite common to have 3 non-parallel slice planes and for this case there is a single intersection point. You can find the computation for example in the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py#L213">ValveView module in SlicerHeart extension</a>.</p>

---

## Post #5 by @miniminic (2022-10-19 06:14 UTC)

<p>Thanks. I’ll give it a try</p>

---
