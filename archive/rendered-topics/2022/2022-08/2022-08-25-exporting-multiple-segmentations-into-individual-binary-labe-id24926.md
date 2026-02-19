---
topic_id: 24926
title: "Exporting Multiple Segmentations Into Individual Binary Labe"
date: 2022-08-25
url: https://discourse.slicer.org/t/24926
---

# Exporting multiple segmentations into individual binary labelmaps?

**Topic ID**: 24926
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/exporting-multiple-segmentations-into-individual-binary-labelmaps/24926

---

## Post #1 by @dokay1 (2022-08-25 19:52 UTC)

<p>I have a project where we segmented 500 tumors from 50 patients and into a single segmentation with 1 segment per tumor.</p>
<p>I want to generate a probability map by adding all 500 lesions into a binary file, then divide it by the number of subjects.</p>
<p>Is there a way to bulk export every segment to a binary labelmap with a value of 1 (or 0)?<br>
Or alternatively is there a way to bulk add segments into a single layer without overlaps but summed intensity values?</p>
<p>Do I have to use python interactor for this?</p>
<p>THanks in advance!</p>

---

## Post #2 by @cpinter (2022-08-27 11:54 UTC)

<p>You could look into the Batch Processing module in the SlicerRT extension.</p>

---

## Post #3 by @dokay1 (2022-09-11 15:19 UTC)

<p>Thanks Csaba! It doesn’t seem to work on Mac. The solution was to export each segmentation layer individually (which was tedious but doable with only 6 layers.</p>
<ol>
<li>I turned on show Segment layer on the Segment viewer</li>
<li>Exported each layer’s segments to a separate binary label map</li>
<li>SimpleITK filters was used to binarize them (0 vs. 1)</li>
<li>Added binary maps to each other</li>
<li>Converted the summed map to a FLOAT (Cast Scalar module)</li>
<li>Divided by the number of patients (created a labelmap whose entire value was the equivalent of the number of patients using BinaryImage Threshold filter in Simple ITK filters)</li>
<li>Voila the result is a population lesion probability map.</li>
</ol>

---
