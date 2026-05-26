---
topic_id: 47074
title: "How can Calculate & Visualize the Center of Mass (COM)?"
date: 2026-05-19
url: https://discourse.slicer.org/t/47074
last_bumped: 2026-05-21T15:00:04.290Z
---

# How can Calculate & Visualize the Center of Mass (COM)?

**Topic ID**: 47074
**Date**: 2026-05-19
**URL**: https://discourse.slicer.org/t/how-can-calculate-visualize-the-center-of-mass-com/47074

---

## Post #1 by @zahra_Tabasi (2026-05-19 08:23 UTC)

<p>Hello everyone,</p>
<p>I am currently conducting a research study involving patients with unilateral left-sided breast cancer undergoing radiotherapy. The purpose of my study is to compare Normal Breathing (free breathing) and Deep Inspiration Breath Hold (DIBH) conditions using CT images and image analysis in 3D Slicer version 5.10.0.</p>
<p>In this project, I need to evaluate anatomical displacement and motion-related parameters of the heart and lungs between the two breathing conditions. I would greatly appreciate detailed step-by-step guidance for the following questions.</p>
<p>Question 1:<br>
How can I calculate the Center of Mass (COM) or Centroid of the heart in 3D Slicer version 5.10.0?</p>
<p>I already have segmented heart structures for both breathing conditions. I would like to know the exact workflow step-by-step, including:</p>
<p>Which modules or extensions should be used</p>
<p>How to obtain the centroid coordinates numerically</p>
<p>How to export or save these coordinates</p>
<p>Whether this can be done directly from a segmentation or label map</p>
<p>Any recommended method for accurate COM calculation in Slicer</p>
<p>Question 2:<br>
After obtaining the Center of Mass coordinates for different patients, how can I visualize or display the heart COM inside 3D Slicer?</p>
<p>Specifically, I would like to know:</p>
<p>How to display the COM as a point/marker in 2D and 3D views</p>
<p>Whether fiducial points or markups should be used</p>
<p>How to compare COM locations between Normal Breathing and DIBH</p>
<p>Whether there is a recommended workflow for multiple patients</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d78230ff10036f7622ad87fb0cd5160ccd82e5d0.jpeg" data-download-href="/uploads/short-url/uKtAzDP8O5v6Xxs8R9x4dY5L6JW.jpeg?dl=1" title="Capture 12.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d78230ff10036f7622ad87fb0cd5160ccd82e5d0_2_690x330.jpeg" alt="Capture 12.PNG" data-base62-sha1="uKtAzDP8O5v6Xxs8R9x4dY5L6JW" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d78230ff10036f7622ad87fb0cd5160ccd82e5d0_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d78230ff10036f7622ad87fb0cd5160ccd82e5d0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d78230ff10036f7622ad87fb0cd5160ccd82e5d0.jpeg 2x" data-dominant-color="7B7C7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture 12.PNG</span><span class="informations">1018×488 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Figure 1.<br>
Visualization of the heart Center of Mass (COM) in 3D Slicer for a patient with unilateral left-sided breast cancer undergoing radiotherapy planning. This figure is related to Questions 1 and 2 regarding the calculation and visualization of the heart centroid in Normal Breathing and DIBH conditions.</p>
<p>I am a student and still a beginner in working with 3D Slicer software. Therefore, I would highly appreciate very detailed, step-by-step guidance for the following questions. If possible, please explain the workflow in a beginner-friendly manner, including the names of modules, extensions, buttons, and menus that should be used in 3D Slicer version 5.10.0.</p>
<p>Additionally, I noticed that some older tutorials mention extensions such as Plastimatch or QARegistration, but these extensions do not appear in the Extension Manager of Slicer 5.10.0. Therefore, I would appreciate recommendations for alternative workflows that are currently supported in this version.</p>
<p>Thank you very much for your help and guidance.</p>

---

## Post #2 by @MasatoshiOBA (2026-05-21 15:00 UTC)

<p>Yes, you can obtain the centroid coordinates using the <strong>Segment Statistics</strong> module.</p>
<p>If you already have a segmentation of the heart, you can open <strong>Segment Statistics</strong>, select the segmentation node and the heart segment, and run the calculation. The module can report the centroid / center of mass coordinates of the segment in Slicer’s coordinate system.</p>
<p>However, if your goal is to <strong>compare</strong> the center of mass between free breathing and DIBH CT, one additional step is important.</p>
<p>The centroid coordinates are only directly comparable if the two CT volumes are in the <strong>same physical coordinate system</strong>. If the two CT scans were acquired separately, differences in patient positioning, table position, or image origin may affect the coordinates. In that case, the difference between the two centroids may not represent only the motion of the heart.</p>
<p>So, a possible workflow would be:</p>
<ol>
<li>
<p>Calculate the centroid of the heart segment in the free-breathing CT.</p>
</li>
<li>
<p>Calculate the centroid of the heart segment in the DIBH CT.</p>
</li>
<li>
<p>Register the two CT volumes, or otherwise make sure they are in the same coordinate system.</p>
</li>
<li>
<p>Then compare the two centroid positions, for example by calculating the displacement vector or distance between them.</p>
</li>
</ol>
<p>In short: <strong>Segment Statistics can give you the centroid coordinates, but for comparison between two CT scans, you need to make sure both centroids are expressed in the same coordinate system.</strong></p>
<p>Otherwise, you may be measuring differences in scan position rather than true anatomical displacement.</p>

---
