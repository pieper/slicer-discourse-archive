# CT to CBCT registration and structure sets

**Topic ID**: 40059
**Date**: 2024-11-06
**URL**: https://discourse.slicer.org/t/ct-to-cbct-registration-and-structure-sets/40059

---

## Post #1 by @tenzin_kunkyab (2024-11-06 22:19 UTC)

<p>Hi Developers,</p>
<p>I want to get structure sets/contour of the CBCT from planning CT (structure set for planning CT is available). First I want to register the planning CT to CBCT and then use the parameter to deform the structure set of the planning CT to CBCT - ending up with the contour for CBCT. I have tried Elastix commands but I hoped if I am able to tweak it better in slicer, that would really help. Is there any functionality/workflow for this on slicer?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2024-11-06 22:28 UTC)

<p>It would help if you posted some screenshots illustrating what you are trying to do and what’s not working.</p>

---

## Post #3 by @tenzin_kunkyab (2024-11-07 15:45 UTC)

<p>Thanks for the response. I am unable to provide screenshots since it involves patient CT. Basically the idea is we want to contour bladder, prostate, femur and rectum on daily CBCTs. The RO’s contour on the CBCT is not available. We do have planning CT and the contours for that (bladder etc.). Initially I tried running it through a Elastix command with a parameter file from the manual. I then transformed the CT structure sets with the same transformation parameter to obtain the contour on the CBCT - the result needs improvement. I am wondering if I can do a similar idea (more manually) on slicer and hopefully get better result especially in structure such as Bladder and Prostate contour on the CBCT?</p>

---

## Post #4 by @pieper (2024-11-08 12:01 UTC)

<aside class="quote no-group" data-username="tenzin_kunkyab" data-post="3" data-topic="40059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tenzin_kunkyab/48/3916_2.png" class="avatar"> tenzin_kunkyab:</div>
<blockquote>
<p>the result needs improvement</p>
</blockquote>
</aside>
<p>Can you be more specific?  There are many options, such as the SegmentRegistration module, or manually dragging the transform to visually align but it’s not clear to me what you are asking for.  Again, images are very helpful and usually an image of internal anatomy is not considered PHI.</p>

---

## Post #5 by @Keegan_Paetzel (2024-11-08 19:12 UTC)

<p>hay i need to get a meeting for to get me starti</p>

---

## Post #6 by @lassoan (2024-11-09 13:32 UTC)

<p>Field of view of CBCT is much smaller than the CT. Therefore, you need to give Elastix a good initialization by adjusting the CT’s position and orientation to be within about 5mm and 5 degrees of the CBCT’s (you can use the new transform interactors or the Fiducial Registration Wizard module in SlicerIGT extension). You probably also need to crop the CT to the CBCT’s region (you can use Crop volume module) to avoid the CT from drifting off.</p>
<p>Once you have this cropped CT in the correct position, with the transform hardened on it, then you can register it to the CBCT using Elastix. It will reduce the misalignment to about 1mm/1deg if there was only rigid motion. If there is also deformation (e.g., difference in bladder filling) then you may need to tune Elastix parameters to track some the soft tissue deformation.</p>
<p>You can then apply the initialization transform and the additional Elastix-computed transform on the segmentation to get the structures in the CBCT.</p>

---
