---
topic_id: 4951
title: "4D Non Rigid Registration Of Bones"
date: 2018-12-04
url: https://discourse.slicer.org/t/4951
---

# 4D non-rigid registration of bones

**Topic ID**: 4951
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/4d-non-rigid-registration-of-bones/4951

---

## Post #1 by @Melanie (2018-12-04 11:06 UTC)

<p>Hi All</p>
<p>Could I know whether slicer 4 D elastix module /volume registration has been validated to use with 4 D CT s please. where could I find any citations please.</p>
<p>I am using this to register my 4D data sets on bone movements to track there position.Thanks</p>

---

## Post #2 by @lassoan (2018-12-05 07:00 UTC)

<p>Slicer’s Sequence Registration module uses <a href="http://elastix.isi.uu.nl/" rel="nofollow noopener">Elastix library</a>, which has been extensively validated on many data sets, including 4D CTs. See a list of papers <a href="http://elastix.bigr.nl/wiki/index.php/Parameter_file_database" rel="nofollow noopener">here</a>. However, before using the software clinically, you always need to do your own validation, on your data sets. If you don’t find registration results good enough with default registration parameters then you may tune the parameters or choose a different parameter set.</p>

---

## Post #3 by @Melanie (2018-12-05 09:50 UTC)

<p>Thank you Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a><br>
My data set include wrists - multiple small bones and I am tracking motion relative to one another. So basically bones<br>
Thanks</p>
<p>Melanie</p>

---

## Post #4 by @lassoan (2018-12-05 14:01 UTC)

<p>Typically you need piecewise rigid transform to describe displacement of bones. The resulting displacement field may have discontinuities at the bone surface, so representing it accurately using b-spline transform (which is probably the most common transform used in non-rigid registration) may not be easy.</p>
<p>If bone motion is moderate (bones that are close to each other do not rotate more than 10-20 degrees relative to each other) then probably you can keep using b-spline transform to represent displacement. Otherwise you may need to register bones to each other in smaller groups (using cropping and masking to exclude effect of other bones) or use some rigidity constraints.</p>
<p>If shape of bones is unique enough then you may be able to do surface-based registration of the same bone between two time points using Surface Registration module. This requires segmentation of each bone, which may be easy if image quality is good.</p>
<p>You can also do manual registration based on landmark points if the bones have clearly identifiable points and you have sufficiently high resolution images. You can use Fiducial registration wizard module of SlicerIGT extension for this.</p>

---

## Post #5 by @Melanie (2018-12-06 00:19 UTC)

<p>Thank you very much Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
Manual segmentation is not an option as my data set contains 80 frames per sequence and 10 bones to be tracked per frame. I calculate the position of each bone in space.<br>
Each bone moves relative to one another and when the wrist moves as a whole.<br>
What I used to do was applying fiducial markers once non rigid transform is done and get the RAS coordinates and calculate  outside slicer for displacement. I don’t see my fiducial markers moving from the place I put them on- although it is hard to say as these bones do not have proper anatomical land marks.<br>
But it is a bit doubtful the numbers I get for rotation. In 2 d movements they look ok, like translation  and bending. But these bones move with 6 degrees of freedom.</p>
<p>Do you have any suggestions how I could improve-<br>
Thanks</p>

---

## Post #6 by @lassoan (2018-12-06 02:34 UTC)

<p>I’ve made a lot of suggestions above that should help. If you can share a data set then we may have better idea of what might work. Also, we would be happy to answer any specific question.</p>

---

## Post #7 by @Melanie (2018-12-13 11:12 UTC)

<p>Thank you very much Prof Lasso.I did try this and due to the data set being very large didn’t work out last time.<br>
Will try and l.et you know</p>

---
