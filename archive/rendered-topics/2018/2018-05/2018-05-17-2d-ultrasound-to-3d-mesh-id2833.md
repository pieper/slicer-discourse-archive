# 2D ultrasound to 3D mesh 

**Topic ID**: 2833
**Date**: 2018-05-17
**URL**: https://discourse.slicer.org/t/2d-ultrasound-to-3d-mesh/2833

---

## Post #1 by @ror_input (2018-05-17 03:15 UTC)

<p>Hi,</p>
<p>I have a set of tiff images of 2D ultrasound (likely will get DICOM in the future) that I am hoping to convert to a 3D mesh and export as an STL file. The goal here is to do some image segmentation on breast tumors for a research project.</p>
<p>I have genuinely had a look around the forums but i can’t see any solid examples that lead me to believe this is possible with slicer. I’m worried about the imaging modality i.e ultrasound having an irregular Z stack and what I can do to deal with this issue.</p>
<p>Any support/examples would really be appreciated!</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2018-05-17 04:42 UTC)

<p>We actually already do exactly this in Slicer, regularly, in patients, using SlicerIGT extension. You can find more details about it here: <a href="http://www.slicerigt.org/wp/breast-cancer-surgery/">http://www.slicerigt.org/wp/breast-cancer-surgery/</a></p>
<p>You can use free-hand ultrasound, you don’t need to worry about irregular spacing or slice orientation, you just need to attach a position tracker on the ultrasound probe. System setup, calibration, etc. are all described in detail in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>, but feel free to ask here if you have any specific question.</p>

---

## Post #3 by @ror_input (2018-05-17 04:55 UTC)

<p>ok this is great feedback for the prospective data we will gather,</p>
<p>For now (sorry for not articulating this originally) i’m wondering is there any solution for retrospective data where no position tracker was used? I understand reliability etc will be an issue however the retrospective data will allow us to do some proof of concept work.</p>
<p>Much appreciated for the response, slicer has an amazing community</p>

---

## Post #4 by @lassoan (2018-05-17 16:46 UTC)

<p>If you moved the transducer along a straight line with even speed then you might be able to reconstruct some volumetric data, but it will be probably quite inaccurate (due to unknown out-of-plane displacement).</p>
<p>Load your image stack as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F">here</a>. After loading adjust image spacing: first two components define scale pixel size of the ultrasound images (same value, probably around 0.2mm), the third component defines the distance between image slices in mm (probably around 1.0mm, if you moved the probe faster then it is a higher value).</p>
<p>You can use Segment editor to segment the tumor. We use a variant of Surface cut effect (provided by SegmentEditorExtraEffects extension).</p>

---
