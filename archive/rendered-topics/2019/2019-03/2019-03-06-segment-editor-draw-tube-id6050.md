---
topic_id: 6050
title: "Segment Editor Draw Tube"
date: 2019-03-06
url: https://discourse.slicer.org/t/6050
---

# Segment Editor: Draw Tube

**Topic ID**: 6050
**Date**: 2019-03-06
**URL**: https://discourse.slicer.org/t/segment-editor-draw-tube/6050

---

## Post #1 by @triple_axel (2019-03-06 20:32 UTC)

<p>Hi,</p>
<p>I am having issues creating a segment using the “Draw Tube” widget on Slicer 4.10.1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a5943c96ee06c0e4810d0687f58b023f6f33e2c.png" data-download-href="/uploads/short-url/8kaWpTO6QdBOzCRb7GeEv1Z57jK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5943c96ee06c0e4810d0687f58b023f6f33e2c_2_690x356.png" alt="image" data-base62-sha1="8kaWpTO6QdBOzCRb7GeEv1Z57jK" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5943c96ee06c0e4810d0687f58b023f6f33e2c_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5943c96ee06c0e4810d0687f58b023f6f33e2c_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5943c96ee06c0e4810d0687f58b023f6f33e2c_2_1380x712.png 2x" data-dominant-color="B7B9DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2787×1439 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Once I mark the fudicials, why won’t the “Apply” button be enabled?<br>
What instances would render the “Apply” button enabled?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2019-03-06 20:45 UTC)

<p>You need to place at least 3 fiducials for the apply button to become enabled for effects like “Draw tube” and “Surface cut”.</p>

---

## Post #3 by @triple_axel (2019-03-06 20:58 UTC)

<p>Ahhh that did the trick. Thanks.</p>

---

## Post #4 by @doc-xie (2019-06-25 01:31 UTC)

<p>Hi,<br>
But in my software(4.11.0), the button of "place a markup point and delete last added markup point in Fiducial Placement is grey and can not be activated, what’s the reason about this?<br>
Thanks,<br>
Xie</p>

---

## Post #5 by @cpinter (2019-06-25 02:04 UTC)

<p>Have you added a segment? Do you have a master volume selected?</p>

---

## Post #6 by @doc-xie (2019-06-26 01:26 UTC)

<p>Hi Csaba Pinter,<br>
I have created a new segment and set the master volume, but the button of “place a markup point and delete last added markup point” in Fiducial Placement was still gray.<br>
Thanks,<br>
Xie<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d73bd0834dbf8b487b319066e4a890eeeaccf099.png" data-download-href="/uploads/short-url/uI2O6rQFrwdBaufNt5eQ0FVQNoR.png?dl=1" title="15%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d73bd0834dbf8b487b319066e4a890eeeaccf099_2_392x499.png" alt="15%20AM" data-base62-sha1="uI2O6rQFrwdBaufNt5eQ0FVQNoR" width="392" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d73bd0834dbf8b487b319066e4a890eeeaccf099_2_392x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d73bd0834dbf8b487b319066e4a890eeeaccf099_2_588x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d73bd0834dbf8b487b319066e4a890eeeaccf099_2_784x998.png 2x" data-dominant-color="EFF2F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15%20AM</span><span class="informations">1358×1732 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2019-06-26 02:19 UTC)

<p>I’ve just checked and it works well on Windows using both 4.10.2 and recent 4.11.x.</p>
<p>Please use latest stable version (currently 4.10.2) or later. Make sure to install “Markups to model” extension when offered (during installation of SegmentEditorExtraEffects extension). Is there any error in the application log?</p>

---

## Post #8 by @doc-xie (2019-07-30 01:08 UTC)

<p>Hi Lassoan,<br>
After I delete the software and download the latest stable version again, the “Draw Tube” work well.<br>
Thanks,<br>
Dr.Xie</p>

---

## Post #9 by @jens-k (2020-03-23 19:08 UTC)

<p>Hey guys,<br>
why this decision to require the user to mark 3 points? Doesn’t that mean I basically cannot draw a straight tube?</p>
<p>Have you thought about linking the undo/redo buttons under the fiducial gui to the fiducial placement, so that one can undo those?</p>
<p>Best,<br>
Jens</p>

---

## Post #10 by @lassoan (2020-03-23 19:28 UTC)

<p>There is no such limitation anymore. You can specify a straight line using 2 points.</p>
<p>If you use Slicer-4.10.2 then you need to update (or uninstall and reinstall) SegmentEditorExtraEffects extension. Or, you can install a recent Slicer Preview Release.</p>

---

## Post #11 by @jamesobutler (2020-03-23 22:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> 3 points is still required to be able to press “Apply” for the Draw Tube effect and Surface Cut.  I guess it could be changed for Draw Tube to support &gt;= 2 points, but doesn’t make sense for Surface Cut.</p>

---

## Post #12 by @lassoan (2020-03-24 01:05 UTC)

<p>Good point, “Apply” button was indeed disabled for 2 points. I’ve updated the extension now. Tomorrow’s version should allow you to draw a line using 2 points.</p>

---

## Post #14 by @Jiuling_SHEN (2023-11-24 08:44 UTC)

<p>Hi Lassoan,<br>
Can I input the coordinate values of fiducial position, such as X, Y, Z coordinates when Draw Tube ?<br>
Thanks,<br>
Dr.Shen</p>

---
