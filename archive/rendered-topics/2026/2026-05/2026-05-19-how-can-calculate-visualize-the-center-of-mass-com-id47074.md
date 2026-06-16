---
topic_id: 47074
title: "How can Calculate & Visualize the Center of Mass (COM)?"
date: 2026-05-19
url: https://discourse.slicer.org/t/47074
last_bumped: 2026-06-15T22:30:38.323Z
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

## Post #3 by @zahra_Tabasi (2026-06-15 11:58 UTC)

<p>I ask everyone for help. I followed these steps: obtained the Displacement field or Vector using the Segment Registration module between two CT scans in different respiratory phases of a patient, then created a vector mask with the Segment Editor module, and finally used the Vector to Scalar module, naming its output scalar volume.</p>
<p>How can I obtain the Center of Mass (Centroid) of a contoured segment? Can I use the Segment Statistics module under Labels, select Centroid, and get the center of mass as three numerical values in RAS vectors? If I want to use Segment Statistics, what should the inputs be (scalar volume or vector)?</p>

---

## Post #4 by @MasatoshiOBA (2026-06-15 22:30 UTC)

<p>I may be overcomplicating this, but I think there are two different steps here.</p>
<p>If your goal is to obtain the center of mass / centroid of a heart segment, Segment Statistics is the right tool. The input should be the segmentation node containing the heart segment. The displacement vector field or the scalar volume created from it is not needed just to calculate the centroid.</p>
<p>However, if your goal is to compare the heart COM between free breathing and DIBH CT, then the important question is the reference coordinate system.</p>
<p>A possible simple workflow would be:</p>
<ol>
<li>Segment the heart on the free-breathing CT.</li>
<li>Segment the heart on the DIBH CT.</li>
<li>Make sure that the two segmentations are represented in the same coordinate system.</li>
<li>Calculate the centroid of each heart segment using Segment Statistics.</li>
<li>Calculate the vector between the two centroids.</li>
</ol>
<p>For example:</p>
<p>displacement vector = COM_DIBH - COM_free_breathing</p>
<p>But this vector is only meaningful if both COM coordinates are in the same coordinate system.</p>
<p>The difficult part is how to define that coordinate system. In the thorax, there is no perfectly fixed structure during respiration. The ribs, sternum, diaphragm, lungs, and even the relationship between the heart and chest wall change with breathing. Even a spine-based rigid registration would define only a “spine-based” displacement, not an absolute heart motion.</p>
<p>I would also avoid using the heart itself for registration if the purpose is to measure heart motion, because that may remove the motion you want to measure.</p>
<p>So before calculating the COM displacement, it may be useful to define exactly what you want to measure:</p>
<ul>
<li>heart COM displacement relative to the scanner / treatment setup coordinates,</li>
<li>heart COM displacement relative to a spine-based registration,</li>
<li>or change in heart position relative to the breast, chest wall, target volume, or radiation field.</li>
</ul>
<p>These are related, but they are not exactly the same question.</p>
<p>Also, if you want to compare this value across patients, the raw displacement in mm may depend on body size and inspiration level. Lung volume change between free breathing and DIBH, chest dimensions, or other respiratory parameters may be useful covariates or normalization factors.</p>
<p>So in short:</p>
<ul>
<li>Segment Statistics can give you the heart centroid.</li>
<li>To compare two centroids, they must be in the same coordinate system.</li>
<li>The interpretation of the displacement vector depends on how that coordinate system is defined.</li>
</ul>

---
