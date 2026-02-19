---
topic_id: 6151
title: "Converting An Stl File To Dicom"
date: 2019-03-14
url: https://discourse.slicer.org/t/6151
---

# Converting an STL file to dicom

**Topic ID**: 6151
**Date**: 2019-03-14
**URL**: https://discourse.slicer.org/t/converting-an-stl-file-to-dicom/6151

---

## Post #1 by @danielfcraft (2019-03-14 20:43 UTC)

<p>I have an externally produced STL file (from a 3D scanner) that I would like to be converted or added to a CT study so it can be used in radiation therapy planning. I’m not sure which of the following ways would work/be best.</p>
<ol>
<li>
<p>Import the STL as a segmentation, add it to an existing CT study, export the entire thing as dicom.</p>
</li>
<li>
<p>Load the STL and somehow directly export it to a new CT dicom series.</p>
</li>
</ol>
<p>Could someone walk me through how to do one of these approaches?</p>
<p>Thanks.</p>
<p>I can import</p>

---

## Post #2 by @lassoan (2019-03-14 20:50 UTC)

<p>You need to load the existing CT study anyway to register the surface scan with the CT, so go with (1).</p>
<p>See instructions for DICOM export here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>

---

## Post #3 by @danielfcraft (2019-03-15 18:53 UTC)

<p>How do I register the segmentation to the CT?</p>

---

## Post #4 by @lassoan (2019-03-15 21:55 UTC)

<p>There are many options but probably a landmark registration is a good start (SlicerIGT extension, Fiducial Registration Wizard module). You may follow it up with an ICP-based surface registration (SlicerIGT extension, Surface registration module). If surfaces may be deformed then you can use Segment Registration extension to align them with a warping transform.</p>

---
