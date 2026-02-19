---
topic_id: 4288
title: "Replace Ukf Modality Node With External Data"
date: 2018-10-04
url: https://discourse.slicer.org/t/4288
---

# Replace UKF modality node with external data

**Topic ID**: 4288
**Date**: 2018-10-04
**URL**: https://discourse.slicer.org/t/replace-ukf-modality-node-with-external-data/4288

---

## Post #1 by @mrjeffs (2018-10-04 21:43 UTC)

<p>is there a pythonic way to replace one or more of the scalar values in UKF fiberbundle,  eg FA1 or trace1 for example, with external data or better yet a volume node or a multivolume node for a movie preserving spacial registration between vtk and vol?</p>
<p>jeff</p>

---

## Post #2 by @zhangfanmark (2018-10-05 18:22 UTC)

<p>Hi Jeff,</p>
<p>You can do this by creating your own extension using Extension Wizard.<br>
We had a tutorial in the last month at MICCAI for teaching how to build a new extension. You can find the materials online at: <a href="https://projects.iq.harvard.edu/slicerdmri2018" rel="nofollow noopener">https://projects.iq.harvard.edu/slicerdmri2018</a><br>
The third hands-on tutorial talks about creating extensions. For your problem, the third part “Module: tractography processing” is the most related.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @mrjeffs (2018-10-08 21:36 UTC)

<p>thanks Fan, i was afraid you’d say build an extension. would love to but not possible in my time frame. jeff</p>

---

## Post #4 by @ljod (2018-10-08 22:18 UTC)

<p>Hi this is a python module that contains example code. No need to build anything. Using the extension wizard module, you just click some buttons and your new module appears. This takes maybe two minutes. Then in the new module there are buttons to open the code in a text editor and also to reload the code, so it’s easy to play with changing the functionality to do what you want.</p>

---

## Post #5 by @mrjeffs (2018-10-18 21:33 UTC)

<p>hi lauren, ok i’ll bite a little, cause i have a little more time:<br>
1st question is we have a UKF vtk file and an RAS+ volume in the same space. outside slicer it seems the x<br>
coordinate on the vtk is revesed or swapped. is that true?<br>
how would you recommend getting a one to one matching coordinate between the vtk in mm and RAS+<br>
volume?<br>
when we do it outside slicer the x values get wrong offsets.<br>
jeff</p>

---

## Post #6 by @ljod (2018-10-18 22:13 UTC)

<p>You need to use the ijktoRAS transform in Slicer to convert between image and world space (fiber tract) coordinates. There are multiple modules that do this so you can look at the code. There is one module that makes a mask image from fiber tracts, and another that selects fibers based on an image ROI. I’m on the phone now so I don’t have the exact module names but they should be easy to find on the diffusion menu. Please reply if this is not clear and we can take a more specific look tomorrow.</p>

---

## Post #7 by @mrjeffs (2018-10-18 22:29 UTC)

<p>no worries, i will investigate. thanks jeff</p>

---

## Post #8 by @lassoan (2018-10-19 04:44 UTC)

<p>Internally, Slicer stores data in RAS coordinate system (due to historical reasons). However, Slicer writes most data types in LPS coordinate system for maximum compatibility, as LPS is used by DICOM and by most medical image computing software nowadays.</p>
<p>Slicer still writes model nodes in RAS coordinate system instead of LPS, but you can detect this (if you find <code>SPACE=RAS</code> in file comment) and compensate for it by applying ijkToRas transform (<code>diag(-1.0, -1.0, 1.0, 1.0)</code> transformation matrix) to the point coordinates. Within a year, we will change Slicer so that model files are saved in LPS coordinate system by default (you’ll find <code>SPACE=LPS</code> in the header so you will know that no RAS-&gt;LPS transformation is necessary).</p>

---
