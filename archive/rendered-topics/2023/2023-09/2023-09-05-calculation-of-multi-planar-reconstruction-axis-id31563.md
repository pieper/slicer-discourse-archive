# Calculation of Multi-Planar Reconstruction axis

**Topic ID**: 31563
**Date**: 2023-09-05
**URL**: https://discourse.slicer.org/t/calculation-of-multi-planar-reconstruction-axis/31563

---

## Post #1 by @Pinyu_Huang (2023-09-05 11:25 UTC)

<p>For example. If I rotate the axial-axis in sagittal plane, as a result, the axial plane will interpolate as the computer will capture the angle and point, and the axial-axis in coronal plane will rotate in some rules.<br>
Is the axis for axial plane means the cross-line with coronal plane or sagittal plane?<br>
How can I know how to calculate the axial-axis in coronal plane? What kind of the rules the calculation abided?</p>

---

## Post #2 by @lassoan (2023-09-05 16:46 UTC)

<p>Computing the rotation axis position is the main challenge, as slice planes may not intersect each other in the same position (there may be several intersection points or there may be none). We choose to use the center of gravity of all the intersection points as center of rotation.</p>
<p>The rotation axis direction is the slice normal.</p>
<p>We then simply rotate all the slices around this rotation axis using homogeneous linear transformation.</p>
<p>You can find the source code of the intersection point computation <a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionRepresentation2D.cxx#L584">here</a> and all the other computations are in the same file or maybe some in the slice intersection widget class, too.</p>

---

## Post #3 by @Pinyu_Huang (2023-09-06 01:30 UTC)

<p>Thanks for your reply. I am trying to reproduce the function.<br>
In the source code, <code>line1</code> controled by mouse influences <code>line2</code>. After calculating the cross point, <code>line2</code> is updated.<br>
But the logic in my code is that I captured the horzView and vertView and calculate the projection on those plane then plot the line on the current view. It seems not correct?</p>

---

## Post #4 by @lassoan (2023-09-06 10:59 UTC)

<aside class="quote no-group" data-username="Pinyu_Huang" data-post="3" data-topic="31563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pinyu_huang/48/67421_2.png" class="avatar"> Pinyu_Huang:</div>
<blockquote>
<p>I captured the horzView and vertView and calculate the projection on those plane then plot the line on the current view. It seems not correct?</p>
</blockquote>
</aside>
<p>Since there can be any number of intersecting slice views (not just two - horzView and vertView) and they can have any orientation (not horizontal and vertical) and they may not be orthogonal to the current slice (so projection does not necessarily produce a line), the method you describe does not seem to be usable in general. It might work in the special case when you only have 3 slices, all orthogonal to each other, but you haven’t described the entire method (just “plot the line on the current view” is probably not all that you need), so it is hard to tell.</p>

---

## Post #5 by @Pinyu_Huang (2023-09-12 08:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="31563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since there can be any number of intersecting slice views (not just two - horzView and vertView) and they can have any orientation (not horizontal and vertical) and they may not be orthogonal to the current slice (so projection does not necessarily produce a line), the method you describe does not seem to be usable in general. It might work in the special case when you only have 3 slices, all orthogonal to each other, but you haven’t described the entire method (just “plot the line on the current view” is probably not all that you need), so it is hard to tell.</p>
</blockquote>
</aside>
<p>Hi, there. I found that might be the angle calculated wrong. If I rotate like a radian like 3.0 from the axial-plane. How can I calculate the corresponding radian in coronal-plane and sagittal-plane? Is there some source code for these computations? Great thanks!</p>

---

## Post #6 by @Pinyu_Huang (2023-09-12 09:07 UTC)

<p>It seems that the <a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionRepresentation2D.cxx#L584" rel="noopener nofollow ugc">source code</a> of the intersection point just the output of rotation, then the changes of the rotation is calculated based on this point?<br>
Is it necessary when slices update each new origin point in different plane need to be calculated again? It seems that the rotation in different planes is updated with the rotation axis.</p>

---

## Post #7 by @lassoan (2023-09-12 10:39 UTC)

<p>The center of rotation is computed when the rotation is started and it is not changed by the rotation operation.</p>

---

## Post #10 by @Pinyu_Huang (2023-09-13 02:49 UTC)

<p>Sorry for the misunderstanding. The vectors is not the center of the rotation, but the coordinate projection from world to local. so after calculating the rotation radian, the coordinate projection is re-computed. But I am confused about the other plane coordinate projection calculation. For in my MPR project, the crossline of current plane is changed but other planes stay silent.<br>
Is it possible for me to get the world situation of the mouse moving point, and then re-compute the rotation matrix in different plane? The X-Y-Z axis orient is the problem to solve.</p>

---

## Post #13 by @Pinyu_Huang (2023-09-18 06:31 UTC)

<p>hey there. after recalculate three planes(in my project is axial, sagittal and coronal), with reset the orients of these planes, I found that the rotation of cross lines like the propellers of helicopter. It seems that it is not necessary that updating all the orients(X,Y) each time.<br>
I found that Slicer has the similar function <code>Set/GetOrients</code> like mine, too. But the input is “Qt::Orientation orientation” class or “int ID”, could you please tell me that how to calculate the rotation matrix for each plane in Slicer? Great thanks thanks a lot!</p>

---

## Post #14 by @Pinyu_Huang (2023-09-18 06:38 UTC)

<p>It seems that the logic of rotation matrix application is in <a href="https://github.com/Slicer/Slicer/blob/23bf4eb14c3367b77563b428b75577a1616b5559/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L867" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #15 by @lassoan (2023-10-24 13:09 UTC)

<p>Sorry, I don’t understand your questions. Maybe you can provide a code snippet that you expect to work but it doesn’t, or draw sketches and/or record screenshot videos to explain.</p>

---
