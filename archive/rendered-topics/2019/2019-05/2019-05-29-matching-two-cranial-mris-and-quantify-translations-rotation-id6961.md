---
topic_id: 6961
title: "Matching Two Cranial Mris And Quantify Translations Rotation"
date: 2019-05-29
url: https://discourse.slicer.org/t/6961
---

# Matching two cranial MRIs and quantify translations & rotations between them?

**Topic ID**: 6961
**Date**: 2019-05-29
**URL**: https://discourse.slicer.org/t/matching-two-cranial-mris-and-quantify-translations-rotations-between-them/6961

---

## Post #1 by @Michiel (2019-05-29 19:33 UTC)

<p>Hi there!</p>
<p>I’m currently trying to match two MRIs of the same patient and quantify both the translations and rotations between the images. They should be (near) perfect matches.</p>
<p>I am new to 3D Slicer and I’ve been messing around with it for a bit now while going through the documentations and tutorials.  I’ve successfully managed to fuse images together now, but I haven’t found a way to test the images yet.</p>
<p>How would overlay a matched image to qualitatively check it (for example, a magenta/green comparison) and is it possible to view the match output (translation and rotation values)? I have been looking around for it for some time but I’m afraid I haven’t succeeded yet.</p>

---

## Post #2 by @pieper (2019-05-29 20:41 UTC)

<p>One thing you can try is the LandmarkRegistration module, where you pick one as fixed and the other as moving.  Even if you don’t do any further registration you can use the flicker, fade, and reveal cursor tools to visually investigate the existing registration.  You can also use the Volumes module to set custom colors to the your volumes.</p>

---

## Post #3 by @lassoan (2019-05-29 20:58 UTC)

<p>You may also try “Compare volumes” module.</p>

---

## Post #4 by @Michiel (2019-05-30 13:16 UTC)

<p>Thanks a lot for the advice! Now I know how I can qualitatively assess the images. I’m also able to match them, but I haven’t found a way to quantify the match results. Is there a way to output the match results? I’m looking for a translation and a rotation value.</p>

---

## Post #5 by @lassoan (2019-05-30 13:20 UTC)

<p>You can segment the same anatomical structures and compute how well they match using Segment Comparison module (provided by SlicerRT extension). You can also add markups fiducials on the same anatomical landmarks in the two volumes and compute statistics between them (Fiducial registration wizard module in SlicerIGT extension can compute basic RMSE metric but you can easily compute anything else by a couple of lines of Python code).</p>

---
