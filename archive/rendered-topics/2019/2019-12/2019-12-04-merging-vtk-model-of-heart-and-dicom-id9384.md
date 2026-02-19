---
topic_id: 9384
title: "Merging Vtk Model Of Heart And Dicom"
date: 2019-12-04
url: https://discourse.slicer.org/t/9384
---

# Merging VTK model of Heart and DICOM

**Topic ID**: 9384
**Date**: 2019-12-04
**URL**: https://discourse.slicer.org/t/merging-vtk-model-of-heart-and-dicom/9384

---

## Post #1 by @Honza_Hecko (2019-12-04 15:07 UTC)

<p>Hello,</p>
<p>i need you help. I have a VTK model with scalars and DICOM series. Can you tel me if is possible to merge colour (scalars) to the DICOM series? Or maybe is sufficient to mark white voxels according to a specific color on the VTK map.</p>
<p>Can you anyone help me?<br>
Thank<br>
Honza H</p>

---

## Post #2 by @Honza_Hecko (2019-12-04 15:07 UTC)

<p>Plese is here anyone who can help me? I need merge some properties of VTK map to the DICOM and export DiCOM<br>
Thanks</p>

---

## Post #3 by @lassoan (2019-12-04 15:12 UTC)

<p>You can merge information and export to DICOM, so probably what you want is doable, but it is not clear what you are trying to achieve. Would you like to export to DICOM an image or a surface? What should it contain (can you attach a sketch or screenshot)? How do you plan to use the exported DICOM series? What software will import and use the created DICOM series?</p>

---

## Post #4 by @Honza_Hecko (2019-12-04 15:56 UTC)

<p>Thank you for your message. Maybe i am far away than you though. I have dicom series of heart in 3D slicer and equally VTK map from carto with colormap (bipolar map). I want merge colormap or scar of map to the dicom series.<br>
Is it possible? Screen or video i can show you tomorrow?<br>
Thanks</p>

---

## Post #5 by @lassoan (2019-12-04 16:04 UTC)

<p>You can alter (paint inside) a volume by using Segment Editor modules’s Mask volume effect (provided by SegmentEditorExtraEffects extension). You can create segments by manually painting or placing markup points (e.g., using Surface Cut effect) or automatically (as shown in examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>).</p>
<p>I am at RSNA all week, but if you can join the <a href="https://discourse.slicer.org/c/community/hangout">Slicer hangout</a> next Tuesday and you may also consider joining one of the <a href="https://projectweek.na-mic.org/">Slicer Project weeks</a>.</p>

---

## Post #6 by @Honza_Hecko (2019-12-04 16:33 UTC)

<p>Ehm, do you think, that when i send you a model, you can show me a short video on some randomly heart CT?</p>

---

## Post #7 by @lassoan (2019-12-04 17:12 UTC)

<p>You can find a video here that shows how to alter an existing volume using Mask volume and surface cut:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>In the video, we set regions to intensity of air, essentially hiding/erasing them, but you can set intensity to a high value to make regions very visible.</p>
<p>If you are interested in automating the procedure then you can start from <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b">this example</a>, which shows how to create sphere-shaped segments at specified anatomical positions.</p>

---

## Post #8 by @Honza_Hecko (2019-12-04 20:53 UTC)

<p>Hi,<br>
I think that this is not that what i need. But i am not so experience like you. So i will try study that.</p>

---

## Post #9 by @lassoan (2019-12-05 00:32 UTC)

<p>How do you envision to use the model in generating/modifying an image?</p>

---

## Post #10 by @Honza_Hecko (2019-12-05 04:50 UTC)

<p>the model is used to bridge colors to DICOM, or depending on the model to highlight white pixels on DICOM so that this location can be focused by CyberKnife</p>

---

## Post #11 by @lassoan (2019-12-05 07:33 UTC)

<p>Probably the easiest is to create a segmentation node and paint into it using Paint effect in segment editor (enable “Sphere brush”, “Edit in 3D views”, click “%” button to switch brush diameter setting to “mm” and set the desired size - e.g., 5mm). You can paint on 3D electrophysical map model and the points/strokes will be added to the segmentation (that is visible in 2D and can be shown in 3D by clicking “Show 3D”):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f9fa5156fa1f867ba544834a6f68bd005d9a46f.jpeg" data-download-href="/uploads/short-url/94Q7kfaY1aqmLERwP9JWg7epjc3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9fa5156fa1f867ba544834a6f68bd005d9a46f_2_537x500.jpeg" alt="image" data-base62-sha1="94Q7kfaY1aqmLERwP9JWg7epjc3" width="537" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9fa5156fa1f867ba544834a6f68bd005d9a46f_2_537x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9fa5156fa1f867ba544834a6f68bd005d9a46f_2_805x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9fa5156fa1f867ba544834a6f68bd005d9a46f_2_1074x1000.jpeg 2x" data-dominant-color="605657"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1303×1213 416 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When you are done, use Mask volume effect to paste the segments into the volume (e.g., as very bright regions):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b5ae814eb48de7ee2e7ceb7ac0e696d8be4f42.jpeg" data-download-href="/uploads/short-url/bNGp1YoZiUCHbaWNpjruyDHgyki.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52b5ae814eb48de7ee2e7ceb7ac0e696d8be4f42_2_539x500.jpeg" alt="image" data-base62-sha1="bNGp1YoZiUCHbaWNpjruyDHgyki" width="539" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52b5ae814eb48de7ee2e7ceb7ac0e696d8be4f42_2_539x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52b5ae814eb48de7ee2e7ceb7ac0e696d8be4f42_2_808x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52b5ae814eb48de7ee2e7ceb7ac0e696d8be4f42_2_1078x1000.jpeg 2x" data-dominant-color="615A56"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1308×1213 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If the CyberKnife treatment planning system can load DICOM RT Structure Set or DICOM Segmentation Object then you don’t have to paste the targets into the volume but you can export the segmentation to a separate DICOM object.</p>

---

## Post #12 by @Honza_Hecko (2019-12-05 07:47 UTC)

<p>Wow, i think that this is what i want <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> i try that and after that i report you. Ok?</p>

---
