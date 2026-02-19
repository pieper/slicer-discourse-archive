---
topic_id: 5175
title: "Trasformation Matrix To Assess Displacement"
date: 2018-12-23
url: https://discourse.slicer.org/t/5175
---

# Trasformation matrix to assess displacement

**Topic ID**: 5175
**Date**: 2018-12-23
**URL**: https://discourse.slicer.org/t/trasformation-matrix-to-assess-displacement/5175

---

## Post #1 by @Jainey (2018-12-23 13:01 UTC)

<p>Hello all- I am a new slicer.<br>
doing a project to assess displacement of bone with time to create a joint kinematic model model.<br>
How can I measure the displacement of bones with time using transformation.</p>

---

## Post #2 by @lassoan (2018-12-23 13:15 UTC)

<p>Slicer stores linear transforms as 4x4 homogeneous transformation matrix.</p>
<p>You can retrieve translation of the coordinate system origin (4th column of the matrix) or rotation of each coordinate system axis (rotated coordinate system axes are stored as the first 3 columns of the matrix).</p>
<p>For these to make sense anatomically, make sure to choose the origin of the coordinate system with a meaningful position (e.g., approximate center of rotation of the joint) and axes with anatomical axes (e.g., principal axes of a bone). To achieve this, you can compute a transform from user-defined landmarks points (1. center of the joint, 2. a point on the first principal axis, 3. a point on the second principal axis) and apply that transform to all bones.</p>

---

## Post #3 by @Jainey (2018-12-24 07:42 UTC)

<p>Thanks. But how would I make sure the use defined landmark points are the same from one frame to the other.   <a class="mention" href="/u/lassoan">@lassoan</a>- Professor Andras Lasso- would it be easy if I share my data set to set up the scene. Thanks</p>

---

## Post #4 by @lassoan (2018-12-27 06:44 UTC)

<p>One option is to choose your landmarks as anatomical points that you can accurately identify on each image.</p>
<p>Another option is to specify landmarks in one image. Then you can use image intensity or surface based registration to transform all images to the reference image.</p>

---
