---
topic_id: 29288
title: "How Can I Use Python Script In Chest Imaging Platform"
date: 2023-05-04
url: https://discourse.slicer.org/t/29288
---

# How can I use Python script in Chest Imaging Platform？

**Topic ID**: 29288
**Date**: 2023-05-04
**URL**: https://discourse.slicer.org/t/how-can-i-use-python-script-in-chest-imaging-platform/29288

---

## Post #1 by @wangjianmerci (2023-05-04 12:33 UTC)

<p>Hello everyone, I have about 200 CTvolumes to do. My procedure is as follow:</p>
<hr>
<p>Load CTfiles → Open lung CT segmenter and use lungmask LTRCLobes → Open lung CT analyzer and lobe analysis → Export csv.</p>
<hr>
<p>And I write a script like this:</p>
<pre><code class="lang-auto">import os
import slicer

# Nifti path
nifti_file_path = r'F:\CT\\benyuezhi\ST00001\SE00002\IM00001PulmonaryFunctions007a002_1.nii'

# load Nifti
nifti_node = slicer.util.loadVolume(nifti_file_path)
slicer.app.applicationLogic().GetSelectionNode().SetReferenceActiveVolumeID(nifti_node.GetID())
slicer.app.applicationLogic().PropagateVolumeSelection(0)

# open lungCTSegmenter
slicer.util.selectModule('LungCTSegmenter')
</code></pre>
<p>But I don’t know how to use the function of lungCTsementer with Python script.</p>

---

## Post #2 by @rbumm (2023-05-04 13:11 UTC)

<p>Hi,</p>
<p>Processing 200 NIFTI volumes in Lung CT Segmenter and Analyzer is possible with the batch processing tool built within the GUIs. Depending on the size of the files as well as your hardware, the combined processing time including lobes and regions using the TotalSegmentator option will be around 26 hours.</p>
<p>Update to the latest versions.</p>
<p>Here is the wiki for  <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Batch-processing-with-Lung-CT-Segmenter">batch processing with Lung CT Segmenter</a><br>
Do this first and write to a separate (segmentation) output directory.</p>
<p>Here is the wiki for <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Batch-Processing-with-Lung-CT-Analyzer">batch processing with Lung CT Analyzer</a><br>
Use the (segmentation output directory as batch processing input directory and define a (final results) output directory.</p>
<p>Writing a Python script is also possible but requires more effort.</p>

---
