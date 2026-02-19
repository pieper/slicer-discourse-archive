---
topic_id: 4347
title: "Fiducial Registration For Multiple Sequences"
date: 2018-10-10
url: https://discourse.slicer.org/t/4347
---

# Fiducial registration for multiple sequences

**Topic ID**: 4347
**Date**: 2018-10-10
**URL**: https://discourse.slicer.org/t/fiducial-registration-for-multiple-sequences/4347

---

## Post #1 by @Melanie (2018-10-10 14:43 UTC)

<p>Hi All</p>
<p>Could you suggest where I could read about the fiducial registration wizard please. It goes to IGT and then link goes to Assembla site. I am trying to register fiducial points that I have put on one moving sequence to another multivolume sequence, tried creating a new sequence, one after the other. Then I applied the markers to the reference frame and registered making the reference the fixed frame. (fixed to moving) Markers did not get transferred to corresponding points. Is it because these are two different sequences? Is this doable? Thanks</p>

---

## Post #2 by @lassoan (2018-10-10 16:20 UTC)

<p>You can learn about how to use Fiducial Registration Wizard module in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>
<p>To apply a sequence of transforms to another sequence, you need to put all of them in the same Sequence Browser node and make sure they have the same index name, unit, and values (index is used for determining which transform corresponds to which markup fiducial list).</p>

---

## Post #3 by @Melanie (2018-10-10 16:39 UTC)

<p>Thank you very much.Prof. Lasso.</p>

---
