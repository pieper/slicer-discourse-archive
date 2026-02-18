# Relationship between pixels and mm from Matlab

**Topic ID**: 427
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/relationship-between-pixels-and-mm-from-matlab/427

---

## Post #1 by @Marina_CM (2017-06-02 16:14 UTC)

<p>Hi all again!</p>
<p>I’d like to know how can I get the relationship between pixels and mm from Matlab, as I know it has to be somewhere because with the Slicer Ruler tool, it’s possible to measure structures in mm.</p>
<p>Thank you very much in advance.</p>
<p>BR,</p>
<p>Marina C.</p>

---

## Post #2 by @lassoan (2017-06-02 16:35 UTC)

<p>It is defined in <code>img.ijkToLpsTransform</code> as a 4x4 homogeneous transformation matrix. From <code>nrrdread.m</code>:</p>
<pre><code> img.ijkToLpsTransform: pixel (IJK) to physical (LPS, assuming 'space' is 'left-posterior-superior')
  coordinate system transformation, the origin of the IJK coordinate system is (1,1,1) to match Matlab matrix indexing
</code></pre>
<p>Note that this matrix include origin, spacing, and axis directions of the volume.</p>
<p>You can convert a coordinate from IJK (voxel) to LPS (physical, in mm) coordinate system by multiplying the coordinate by ijkToLpsTransform from the left. Spacing is the norm of column vectors of ijkToLpsTransform.</p>
<p>See more information for example  here: <a href="https://www.slicer.org/wiki/Coordinate_systems">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @Marina_CM (2017-06-02 16:51 UTC)

<p>Thank you very much!<br>
I’ll use this info <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>BR,</p>
<p>Marina C.</p>

---

## Post #4 by @Marina_CM (2017-06-05 23:23 UTC)

<p>Hi all,</p>
<p>Using the valuable information provided, I tried to measure the distance in mm between two points with matlab, but I think I’m doing something wrong:</p>
<p>Assuming that <code>M = cli_imageread(inputParams.inputvolume);</code><br>
And <code>Point1</code> and <code>Point2</code> are the coordinates of two different points from M which are in the same slice, I’ve used the next code but I must have misunderstood something:</p>
<pre><code>Point1 = [x1, y1, z1, 1];
Point2 = [x2, y2, z2, 1];

spacing_x = norm(img.ijkToLpsTransform(:,1));
spacing_y = norm(img.ijkToLpsTransform(:,2));

Point1_LPS = img.ijkToLpsTransform*(Point1');
Point2_LPS = img.ijkToLpsTransform*(Point2');

dis_x = (Point1_LPS(1)-Point2_LPS(1))*spacing_x;
dis_y = (Point1_LPS(1)-Point2_LPS(1))*spacing_y;
distance_p = sqrt((dis_x^2) + (dis_y^2));
</code></pre>
<p>How should I use this inputs to find the right distance?</p>
<p>Thank you very much.</p>
<p>Best Regards,</p>
<p>Marina C.</p>

---

## Post #5 by @lassoan (2017-06-06 00:06 UTC)

<p>Don’t compute spacing. Use the matrix to convert point coordinates from IJK to LPS coordinate system. Unit of LPS coordinate system is mm, so distance that you compute in LPS is the distance you need. Something like this:</p>
<p><code>norm( img.ijkToLpsTransform*[p1_i, p1_j, p1_k, 1]' - img.ijkToLpsTransform*[p2_i, p2_j, p2_k, 1]' )</code></p>

---

## Post #6 by @Marina_CM (2017-06-06 16:28 UTC)

<p>Thank you very much! It worked <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>BR</p>
<p>Marina C.</p>

---
