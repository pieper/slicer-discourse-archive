---
topic_id: 15371
title: "Calculating The Deformation"
date: 2021-01-06
url: https://discourse.slicer.org/t/15371
---

# Calculating the deformation

**Topic ID**: 15371
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/calculating-the-deformation/15371

---

## Post #1 by @BORIPHAT (2021-01-06 08:26 UTC)

<p>Hello,<br>
I have the two CT image data sets of breast phantom (the same body size but different breast size). I would like to know how much it deformed?  Firstly, I use the segmentation comparison module to get HD and DICE metrics. Now, I would like to analyze the deformation from DVF and show the result with the profile. Could you please recommend which module of 3Dslicer can solve this problem? Thank you in advance for your help.</p>

---

## Post #2 by @lassoan (2021-01-06 15:51 UTC)

<p>You can use Segment Registration extension to get a dense displacement field. You are guaranteed to get correspondence on the surface but internally you just get a smoothly changing field. If you can identify landmark points inside the phantom then you can use Landmark registration or Fiducial Registration Wizard module (in SlicerIGT extension) to get accurate internal displacements, too. If the images have sufficient internal texture (this may not be the case for phantoms) then you can use automatic image registration using “General registration (Elastix)” module (in SlicerElastix extension).</p>
<p>See more information on image registration in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">user manual</a>.</p>

---

## Post #3 by @BORIPHAT (2021-01-07 07:35 UTC)

<p>Thank you very much for your help. Can it show the histogram of displacement vector field?</p>

---

## Post #4 by @lassoan (2021-01-07 16:33 UTC)

<p>You can get the displacement field as a numpy array and can easily compute any statistics you need using standard numpy functions.</p>

---

## Post #5 by @BORIPHAT (2021-01-08 05:14 UTC)

<p>Thank you very much for your recommendation. It’s very useful.</p>

---
