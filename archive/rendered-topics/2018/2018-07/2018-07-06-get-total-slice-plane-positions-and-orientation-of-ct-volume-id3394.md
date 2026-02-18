# Get total slice plane positions and orientation of CT volume in RAS?

**Topic ID**: 3394
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/get-total-slice-plane-positions-and-orientation-of-ct-volume-in-ras/3394

---

## Post #1 by @shahrokh (2018-07-06 02:37 UTC)

<p>Hi Slicer developers.</p>
<p>Excuse me to send this question. I have CT slices as 3D volume.<br>
How can I get the total axial slice plane positions and orientations in RAS coordinates using python interactor?<br>
Thanks for your guidance.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-07-06 04:12 UTC)

<p>Coordinates of which positions you would like to get? You would like the user to select a point with the mouse? Or, you have the IJK voxel coordinates of a point and you would like to get RAS world coordinates?</p>

---

## Post #3 by @shahrokh (2018-07-06 16:51 UTC)

<p>Thanks a lot your reply.<br>
I want to get only coordinates of axial plane in total CT slice. I do not necessary to coronal and sagital coordinates. I can get the coordinates of point selected with the mouse. As mentioned I want to get only one coordinates related to axial plane with command line of python interactor.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #4 by @shahrokh (2018-07-07 02:48 UTC)

<p>Excuse me to repeat my question. When I change axial planes in green window with mouse, I can see the value of axial location in this window. I want to get these location values for all axial CT slices in each coordinate systems in python interactor. How can I do it?</p>
<p>I have noticed that the difference between these values is not the same with the slice thickness (third dimension of voxel). Is it related to the gap between slices in the image acquisition? Does Slicer  do the interpolation between slices?</p>
<p>Please guide me.<br>
Shahrok.</p>

---

## Post #5 by @lassoan (2018-07-07 04:57 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="3" data-topic="3394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>I want to get only one coordinates related to axial plane with command line of python interactor</p>
</blockquote>
</aside>
<p>Slice position in RAS is stored in the last (4th column) of the SliceToRAS matrix stored in the slice node.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="4" data-topic="3394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Is it related to the gap between slices in the image acquisition? Does Slicer do the interpolation between slices?</p>
</blockquote>
</aside>
<p>Slice position increment equals acquisition slice spacing when you switch to previous/next slice using arrow keys or page up/down keys on the keyboard. However, when you move the slice positioning slider using your mouse then you can set the slice position at higher precision. Slicer interpolates between slices by default, but you can disable this (see for example <a href="https://discourse.slicer.org/t/slice-interpolation/2808/2">this topic</a> for more info). You can still set the slice position to be between original acquisition slices, but the voxels values will not be interpolated for display.</p>

---
