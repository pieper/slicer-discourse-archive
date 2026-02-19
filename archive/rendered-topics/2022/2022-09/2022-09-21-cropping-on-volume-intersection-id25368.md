---
topic_id: 25368
title: "Cropping On Volume Intersection"
date: 2022-09-21
url: https://discourse.slicer.org/t/25368
---

# Cropping on volume intersection

**Topic ID**: 25368
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/cropping-on-volume-intersection/25368

---

## Post #1 by @Vincebisca (2022-09-21 08:02 UTC)

<p>Hello everyone,</p>
<p>I am currently working on CT/MRI registration using Elastix in a script. Since I want to automate as much of the workflow as possible, I want to automate the cropping of CT and MRI volumes and launch Elastix from there.</p>
<p>For now, my workflow is as follows :</p>
<ul>
<li>Pre-alignement of MRI (moving) on CT (fixed) with 3 points fiducial registration</li>
<li>Cloning the CT and cropping using an ROI fitted to the MRI volume</li>
<li>Registration of Cloned cropped CT (fixed) and MRI (moving) using elastix (preset Generic (all))</li>
<li>Delete the cloned CT</li>
</ul>
<p>This workflow seems to work fairly well, however, I get problems when the MRI is not fully included in the CT, since after cropping, the MRI have more information than the CT (since I only crop the CT based on the MRI bounding box). To correct that, I made a few tests by manually cropping both CT and MRI at their intersection, so that both resulting cropped volumes have the same bounding box. This seems to produce better results.</p>
<p>My question is : is there a way to fit the ROI directly on the intersection of volumes?</p>
<p>Thank you in advance !</p>
<p>Vincent</p>

---
