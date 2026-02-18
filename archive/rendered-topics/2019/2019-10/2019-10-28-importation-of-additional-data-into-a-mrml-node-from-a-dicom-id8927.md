# Importation of additional data into a MRML node from a dicom

**Topic ID**: 8927
**Date**: 2019-10-28
**URL**: https://discourse.slicer.org/t/importation-of-additional-data-into-a-mrml-node-from-a-dicom/8927

---

## Post #1 by @Impetus (2019-10-28 15:28 UTC)

<p>Hello,</p>
<p>I am currently working on a scripted plugin for 3DSlicer that aims to load extra data from DICOM files and store it into a MRML node. I was wondering if the embedded DICOM reader is enough for that purpose or if I need to use an other DICOM reader (for example : pydicom).<br>
Is anybody already worked on this ?</p>

---

## Post #2 by @pieper (2019-10-28 17:24 UTC)

<p>Hi -</p>
<p>Pydicom is bundled with Slicer, so you can easily access any of the header data you need that way.</p>
<p>What data are you trying to load?  You can look at the DICOMPlugin classes for ideas on how to load and populate MRML nodes (see SlicerRT, and Quantitative Reporting extensions for a lot of examples).</p>

---

## Post #3 by @lassoan (2019-10-28 17:32 UTC)

<p>Links to two DICOM plugins implemented in Python using pydicom:</p>
<ul>
<li>Structured report and segmentation: <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py">https://github.com/QIICR/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py</a>
</li>
<li>Various ultrasound images: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py">https://github.com/SlicerHeart/SlicerHeart/blob/master/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py</a>
</li>
</ul>

---
