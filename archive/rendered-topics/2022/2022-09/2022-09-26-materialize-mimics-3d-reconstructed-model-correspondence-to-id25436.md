---
topic_id: 25436
title: "Materialize Mimics 3D Reconstructed Model Correspondence To"
date: 2022-09-26
url: https://discourse.slicer.org/t/25436
---

# Materialize Mimics 3d reconstructed model correspondence to CT

**Topic ID**: 25436
**Date**: 2022-09-26
**URL**: https://discourse.slicer.org/t/materialize-mimics-3d-reconstructed-model-correspondence-to-ct/25436

---

## Post #1 by @dj_96 (2022-09-26 13:46 UTC)

<p>I’m trying to make sense of the coordinate system correspondence between a Mimics 3d export(.stl) to the DICOM files that were used for the construction? Stl files don’t have any metadata about the patient coordinates so what coordinate system am I working with?</p>
<p>I believe mimics has it’s own world coordinates, does that line up with fixed coordinates from the CT scan? Essentially how would I know where a vertex on the stl file corresponds to on a Dicom slice?</p>
<p>Thank you,</p>

---

## Post #2 by @lassoan (2022-09-26 17:00 UTC)

<blockquote>
<p>I believe mimics has it’s own world coordinates, does that line up with fixed coordinates from the CT scan?</p>
</blockquote>
<p>I don’t see any reason why Mimics would use some special world coordinates in exported STL files. DICOM uses LPS, so I would expect that LPS is used in the exported STL file, too.</p>
<p>When you import an STL file into current Slicer version (Slicer-5.0.3) then it is assumed to be in LPS coordinate system by default. We switched this default from RAS a couple of years ago, so if you use a very old Slicer version then give it a try with the current Slicer version, too. Make sure to load the CT into Slicer using DICOM module.</p>
<p>If the Mimics-exported STL still does not line up with the CT then check Mimics user manuals or contact the company to get information on what coordinate system they use in the exported STL file. You can also try to export into different formats (STL is bad because it does not store surface normals and some implementations shift all points into a “positive space” so that all coordinate values are &gt;=0) or see if there are export options that you can adjust.</p>
<p>What kind of segmentation do you do in Mimics? Have you tried using Slicer for it?</p>

---

## Post #3 by @dj_96 (2022-09-26 17:10 UTC)

<p>A third party used mimics so I’m pretty sure we’re constrained to use mimics. I’ll probably have to ask them or discuss using a different 3d model format. I don’t know the details all I’m aware of that I’m getting some DICOM files with a few 3d reconstructions based on them. I need the coordinates on the stl to match up to the ones on the DICOM. So even if one of the stl files contains say a liver… it should be at the LPS coordinates ideally.</p>
<p>Do you know if LPS is standard for mimics exports(it’s multiple models)? Otherwise I’ll have to get in contact with the person using it.</p>

---

## Post #4 by @lassoan (2022-09-26 17:57 UTC)

<p>All image computing software that I know of, use the same anatomical coordinate system for meshes and images. Most likely Mimics allows this, too, so if the model position is not right then probably wrong export options are used.</p>

---
