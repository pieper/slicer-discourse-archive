---
topic_id: 32306
title: "Dicom To Nrrd Conversion In Command Line For Pyradiomics"
date: 2023-10-18
url: https://discourse.slicer.org/t/32306
---

# DICOM to NRRD conversion in command line (for PyRadiomics)

**Topic ID**: 32306
**Date**: 2023-10-18
**URL**: https://discourse.slicer.org/t/dicom-to-nrrd-conversion-in-command-line-for-pyradiomics/32306

---

## Post #1 by @marcin.jakalski (2023-10-18 16:00 UTC)

<p>Hello! I would like to recreate some of the functionality of 3D Slicer in command line for batch analysis of several hundred of patients’ images. I have a set of DICOM images along with their segmentations. For these I want to calculate radiomics features. It is fairly easy to do using GUI for a single case, but not for the entire set of patients.<br>
I noticed, that when running Radiomics feature extraction within Slicer, two NRRD files are being created in the temporary directory, as well as an CSV file and a JSON file with run parameters. I assume these two NRRD files correspond to the image and the mask (segment). I would like to be able to create the same kind of files directly on the command line.<br>
I’ve already tried using different tools/scripts for converting original images and segments to either NII or NRRD (as required by pyradiomics command line tool) but these always seem to be invalid, namely - there is some problem, such as mismatched input’s size:<br>
<code>pyradiomics Image.nii Segmentation.nii</code><br>
<code>sitk::ERROR: Input "labelImage" for "LabelStatisticsImageFilter" has size of [ 512, 512, 134 ] which does not match the primary input's size of [ 512, 512, 536 ]!</code></p>

---

## Post #2 by @pieper (2023-10-18 17:50 UTC)

<p>Probably the same answer as this post: <a href="https://discourse.slicer.org/t/radiologist-saved-segmentations-without-references-annotations-come-out-cropped-when-loading-as-numpy-arrays/32277/2" class="inline-onebox">radiologist saved segmentations without references -&gt; annotations come out cropped when loading as numpy arrays - #2 by pieper</a></p>

---
