---
topic_id: 16292
title: "Alignment Of Two Images In Physical Space Prior To Landmark"
date: 2021-03-01
url: https://discourse.slicer.org/t/16292
---

# Alignment of two images in physical space prior to landmark registration

**Topic ID**: 16292
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/alignment-of-two-images-in-physical-space-prior-to-landmark-registration/16292

---

## Post #1 by @songbird (2021-03-01 17:36 UTC)

<p>Hello,</p>
<p>I am very new to Slicer and would like to register a phantom to a patient image (same image dimensions) using the Landmark Registration module. However, they are not in the same orientation: the patient image is in the axial plane, while the phantom image is at an arbitrary angle.</p>
<p>To align the images prior to registration, I have tried the following:</p>
<ul>
<li>Automatic Initialization (Geometry Align) in the General Registration (BRAINs) module</li>
<li>Apply that transform to phantom image using ResampleScalarVectorDWIVolume module</li>
</ul>
<p>My transformed phantom image is now in the axial plane as desired, but appears to cut off at certain slices.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41bd161bcd47078e26a2984bce0593b29be17214.png" alt="slicer_alignment" data-base62-sha1="9ny9nmUY2Qqmls5WoWsyAS4vd5y" width="651" height="486"></p>
<p>Is this the right procedure to align two images prior to registration? If so, how can I prevent the transformed image from being “cut off”?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-03-01 17:56 UTC)

<p>If the input images are far from each other then you can prealign them before automatic registration using  <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">semi-automatic registration methods</a>. You need to harden the transforms on the images before starting automatic registration.</p>
<p>For automatic registration only the physical location of the volumes matter. Orientation of the voxel array axes is irrelevant (volumes are always shifted and rotated during registration anyway).</p>
<p>Just to confirm, are you registering 3D volumes to each other? You can do 2D/2D, 2D/3D, and multi-slice 2D/3D registration, too, but those are very different problems from 3D/3D registration.</p>

---
