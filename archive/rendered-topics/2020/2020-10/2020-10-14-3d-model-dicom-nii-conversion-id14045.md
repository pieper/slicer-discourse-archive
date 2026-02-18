# 3D model -> DICOM/nii conversion

**Topic ID**: 14045
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/3d-model-dicom-nii-conversion/14045

---

## Post #1 by @a10227 (2020-10-14 22:51 UTC)

<p>Good day,<br>
I have raw patient images as well as their segmentations as 3D models. I need to convert segmentations to 3D images so that these converted images are aligned with the patient’s images.<br>
Could you please tell me, is it possible to convert 3D mesh(.ply) to the DICOM or any other format for 3D images? And is it possible to align it with the other DICOM image?</p>

---

## Post #2 by @JanWitowski (2020-10-14 23:14 UTC)

<p>If I understand correctly, you don’t have a segmentation file, but rather mesh that was a result of the segmentation? If you can convert the .ply to .stl, then you could simply drag and drop the model to Slicer and open it as e.g. Segmentation node, <a href="https://discourse.slicer.org/t/3d-model-to-segmentation/5135/2">as described here</a>.</p>
<p>There are many ways to do registration in Slicer, too. You can even perform registration directly on the model and loaded volume through fiducial registration (<a href="https://discourse.slicer.org/t/non-rigid-registration-between-dicom-volume-and-stl-alias-volume/3225">relevant thread</a>).</p>
<p>You have also received some useful comments <a href="https://discourse.itk.org/t/3d-model-dicom-nii-conversion/3536" rel="noopener nofollow ugc">on the ITK forum</a>.<br>
.</p>

---

## Post #3 by @lassoan (2020-10-14 23:17 UTC)

<p>You can do this in Slicer, but it is not commonly needed. What is your end goal? Are you sure you need to convert the surface mesh to DICOM format? What software will visualize/analyze it? What DICOM representation that software recognizes (DICOM Segmentation object RT structure set, fake CT, overlays,…)?</p>

---

## Post #4 by @a10227 (2020-10-15 10:18 UTC)

<p>Thank you for your reply. I need to convert a mesh to DICOM or any other 3D images format. I need these images to work with them in python, so no presets for visualizations should be applied.</p>
<p>The thing is, I have segmentations made by a physician in one program. The problem is, this physician makes segmentations on the 3d model which is rendered according to a specific visualization preset. As a result, in his viewer he sees a clean model generated from segmentations but in a real situation, without any visualization presets, images of these segmentations have some noise, he just doesn’t see it because he segments 3d model when a visualization preset is applied.</p>
<p>What I want is to get clean images of segmentations without any garbage. We’ve managed to export a ply model from this tool that is not as ideal as the model the physician sees but is very close to it.</p>
<p>Now our goal is to convert this ply back to dicom because for my purposes I need the image, not a mesh.</p>

---

## Post #5 by @a10227 (2020-10-15 10:20 UTC)

<p>Actually I have also 3D images of my segmentations, but they have some noise (you can find an explanation of this in my reply to <a href="https://discourse.slicer.org/u/lassoan">Andras Lasso</a>, so I can’t use them. Thank you for your replay, I will take a look at this solutions.</p>

---

## Post #6 by @JanWitowski (2020-10-15 19:25 UTC)

<p>Could you explain what do you mean by “visualization preset”? Usually we talk about presets when we are using volume rendering (directly from volume), not surface rendering (from segmentation), <a href="https://discourse.slicer.org/t/volume-representation-without-noise-and-garbage/14046/3">as we discussed in the other thread</a>. Have you tried converting your .ply file to .stl and opening it in Slicer? Can you provide screenshots of the “noise” or files so we can try to replicate the issue?</p>

---

## Post #7 by @a10227 (2020-10-21 09:17 UTC)

<p>Sorry I hand’t access to my laptop and couldn’t reply you earlier. By visualization preset I mean the “scalar opacity mapping” option on the volumes rendering tab. When I upload 3D images of my segmentations there, run volume rendering for them, and then change the opacity mapping, the visualization changes and some noise disappears, but it doesn’t impact the real 3D images and in the real situation the noise is still there. When the physician does segmentations in another viewer, he applies some visualization presets (some presets for opacity mapping) and that’s why he doesn’t see the real noise which exists. The example of the noise attached <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a04fc86b463a594919b7aa8fb180b1370cc07e3a.png" alt="image_2020-10-21_121511" data-base62-sha1="mSbkpTQTO5FEraBrudNQVKKdTTk" width="388" height="341">.</p>

---
