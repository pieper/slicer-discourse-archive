---
topic_id: 46522
title: "Smoothing aorta segmentations across time"
date: 2026-03-20
url: https://discourse.slicer.org/t/46522
last_bumped: 2026-03-26T18:25:13.747Z
---

# Smoothing aorta segmentations across time

**Topic ID**: 46522
**Date**: 2026-03-20
**URL**: https://discourse.slicer.org/t/smoothing-aorta-segmentations-across-time/46522

---

## Post #1 by @tassiasalles (2026-03-20 18:45 UTC)

<p>Good afternoon,</p>
<p>I’m working with aorta segmentation across different cardiac frames and I was wondering if there is any way to smooth the segmentations across time (different cardiac frames) to avoid segmentations inconsistencies between time points.</p>
<p>I would appreciate any suggestions or recommendations to address this issue.</p>
<p>Thank you in advance =D</p>
<p>Tassia</p>

---

## Post #2 by @mikebind (2026-03-20 19:42 UTC)

<p>You could try using sequence registration to take one segmentation and deform it across time instead of having a separate segmentation for each frame.  This will likely result in a more consistent appearance over time because the registration will only introduce smooth deformations.</p>

---

## Post #3 by @tassiasalles (2026-03-23 15:43 UTC)

<p>Hi Mike,</p>
<p>Thank you for your suggestions. In that case I would only have the segmentation for one frame and the following ones would be deformed based on the images, correct? Do I need a specific extension to work with thoracic MRI data?</p>
<p>Thank you!!</p>

---

## Post #4 by @mikebind (2026-03-26 18:25 UTC)

<p>You would need to install the “Sequence Registration” module from the Extension Manager.  When you run the registration, ensure you are generating as output the sequence of transforms and not just the registered images.  See some usage documentation at <a href="https://github.com/moselhy/SlicerSequenceRegistration?tab=readme-ov-file" class="inline-onebox" rel="noopener nofollow ugc">GitHub - moselhy/SlicerSequenceRegistration · GitHub</a></p>
<p>The generated transforms apply deformations to each corresponding frame to make it look maximally like the selected fixed frame (you can choose which frame in the advanced section).  If you have a segmentation of the aorta in that frame, you can apply the inverses of the transforms to deform that segmentation into a corresponding segmentation for each of the other frames.  This is straightforward conceptually, but unfortunately, I’m not sure there’s a simple automated way to do it.  It can be achieved with a python script or by manually going through each frame, inverting each transform, making a copy of the segmentation, applying the inverted transform to the segmentation copy, hardening the transform (this applies the deformation to the segmentation in a permanent way, as opposed to just a visualization option, a necessary step before you would do something like measure anything quantitatively, like volume or shape).</p>
<p>Take a look at the sequence registration extension, learn a little about nonlinear transforms in Slicer (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="inline-onebox" rel="noopener nofollow ugc">Transforms — 3D Slicer documentation</a>), and see if you can sort out the above workflow.  If you get stuck, post back here and I (or others) can try to help.  Public AI chatbots also know a fair amount about Slicer; for a faster response you can ask one of them for some help first.</p>

---
