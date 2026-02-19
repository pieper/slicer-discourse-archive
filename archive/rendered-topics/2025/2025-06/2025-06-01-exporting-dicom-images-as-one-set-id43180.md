---
topic_id: 43180
title: "Exporting Dicom Images As One Set"
date: 2025-06-01
url: https://discourse.slicer.org/t/43180
---

# Exporting dicom images as one set

**Topic ID**: 43180
**Date**: 2025-06-01
**URL**: https://discourse.slicer.org/t/exporting-dicom-images-as-one-set/43180

---

## Post #1 by @folkertvanheusden (2025-06-01 11:41 UTC)

<p>Hi,</p>
<p>I would like to use Slicer as a tool to convert a dicom-set into a new decompressed set.<br>
I can succesfully load the set (study?) and export as dicom, but this gives 76 individual sets with each 1 dicom-image. How can I export uncompressed while keeping the relation between images?</p>

---

## Post #2 by @lassoan (2025-06-01 11:44 UTC)

<p>It may be just as valid to have one file per slice as to have all slices of a series in a single file. What kind if image are you working with?</p>

---

## Post #3 by @folkertvanheusden (2025-06-01 16:39 UTC)

<p>Hi,</p>
<p>The image-set is of an 3D ultrasound scan of my child.<br>
I want to see if I can print it in 3D.</p>

---

## Post #4 by @lassoan (2025-06-02 00:40 UTC)

<p>If you want to print something from an image then you need to segment some structures from it and then export the segmentation as an STL file. Exporting the image to DICOM is not needed for this (and may actually make your workflow more complicated).</p>
<p>To segment an image for 3D printing, you can use the Segment Editor module in Slicer. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> can help you getting started.</p>

---
