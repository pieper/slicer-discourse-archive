---
topic_id: 30938
title: "Automatically Split Segmentation Islands Connected By A Narr"
date: 2023-08-02
url: https://discourse.slicer.org/t/30938
---

# Automatically split segmentation islands connected by a narrow path

**Topic ID**: 30938
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/automatically-split-segmentation-islands-connected-by-a-narrow-path/30938

---

## Post #1 by @nasibov_98 (2023-08-02 15:39 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9717eccaa68b7976476b350c6b2a3382b5ba8f96.png" alt="Screenshot 2023-08-02 at 16.35.26" data-base62-sha1="lyDm8tuHm7j6hY6hjl1CVFidcY6" width="300" height="284"></p>
<p>Hi there, I have a simple question.</p>
<p>I am using the segment islands tool to separate tumours that are not touching each other into unique segments. How do I separate tumours that are touching each other i.e. have narrow connections in the segmentation? I need a method that does not involve the scissors tool as this takes too long.</p>
<p>I have hundreds of MRI images with similar labelmaps. I cannot use the scissors tool manually on them one by one this would take days, and would also drive me insane.</p>
<p>Cheers,</p>
<p>Ulvi</p>

---

## Post #2 by @mau_igna_06 (2023-08-02 17:41 UTC)

<p>Maybe margin down and then margin up the tumor segment, although you may lose some accuracy of the segment surface</p>

---

## Post #3 by @rbumm (2023-08-02 18:32 UTC)

<p>For bones, I find Smoothing effect → Opening very helpful. If you threshold bones, try a conservative not overaggressive setting that leaves the connections minimal.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e76e7a01f16cea4353f01f4047acfead2e939bb.jpeg" data-download-href="/uploads/short-url/mBQbWANAugzjfdjIb2WIM0R4U6T.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e76e7a01f16cea4353f01f4047acfead2e939bb_2_690x252.jpeg" alt="image" data-base62-sha1="mBQbWANAugzjfdjIb2WIM0R4U6T" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e76e7a01f16cea4353f01f4047acfead2e939bb_2_690x252.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e76e7a01f16cea4353f01f4047acfead2e939bb_2_1035x378.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e76e7a01f16cea4353f01f4047acfead2e939bb_2_1380x504.jpeg 2x" data-dominant-color="787879"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×699 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @nasibov_98 (2023-08-03 11:33 UTC)

<p>Thank you for your responses guys.</p>
<p>Unfortunately, large variations in the size of the tumours in the imaged mice means that the calibration of the margin and smoothing tool are impossible to fit all cases.</p>
<p>Surely there is a 3D equivalent of the binary watershed algorithm used in FIJI (ImageJ)?</p>
<p>Cheers,</p>
<p>Ulvi</p>

---

## Post #5 by @lassoan (2023-08-03 13:20 UTC)

<p>Watershed method is available in Slicer, too, along with many others. We usually want to segment identified structures, each marked with some seeds, therefore both “Watershed” (in SegmentEditorExtraEffects extension) and “Grow from seeds” (in Slicer core) effects require some input segments. These input segments can be very easily generated automatically (e.g., using Thresholding or Margin effect, followed by Islands / Split islands to segments).</p>
<p>Alternatively, you can run classic markerless watershed using ITK: compute distance map from the segmentation, partition it using watershed filter, then apply that partitioning to the original segmentation. You can use the application GUI for this (see the steps below), but you can of course fully automate it, to perform all the steps with a short Python script.</p>
<p>Classic watershed partitioning of a segment:</p>
<ul>
<li>Export segment to labelmap (by right-clicking on the segmentation in Data module)</li>
<li>Compute distance map from segment (Simple Filters module, SignedMaurerDistanceMapImageFilter)</li>
<li>Compute watershed regions (Simple Filters module, MorphologicalWatershedImageFilter; Input Volume is the computed distance map; Level is a positive distance value, the optimal value depends on the thickness of the connecting path and size of the structure, you can start with 10 and increase if there are too many segments, decrease it if the structures are not separated; for output, choose <code>Create new LabelMapVolume</code>, scroll down to see this option).</li>
<li>Import the watershed results into the segmentation (drag-and-drop the labelmap output of the watershed filter into the segmentation; or use Import section in Segmentations module)</li>
<li>Use “Logical operators” effect to intersect the each imported segment from watershed with the original segmentation</li>
</ul>
<p>If you confirmed that this works well for your data using the GUI, you can fully automate this process using Python scripting. Simple Filters code shows up in the Python console (or you can use <a href="https://examples.itk.org/src/segmentation/watersheds/segmentwithwatershedimagefilter/documentation">ITKPython</a>). Other operations are described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>. If you have trouble figuring out how to automate a certain step and Bing chat/ChatGPT does not help either then you can ask us here.</p>
<p>If you find this useful then we may consider adding this watershed-based splitting method as a Segment Editor effect (you can submit a <a href="https://discourse.slicer.org/c/support/feature-requests/9">feature request</a> for it).</p>

---
