# How to select one among several annotated images to do the segmentation process in 3D Slicer?

**Topic ID**: 17608
**Date**: 2021-05-13
**URL**: https://discourse.slicer.org/t/how-to-select-one-among-several-annotated-images-to-do-the-segmentation-process-in-3d-slicer/17608

---

## Post #1 by @Mostafa2020 (2021-05-13 19:23 UTC)

<p>Operating system: macOS<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi all,</p>
<p>I am using an annotation file to do the segmentation process in 3D Slicer. But in the annotation file, there are several annotated images of a patient. How should I select one among several annotated images to do the segmentation process in 3D Slicer?</p>
<p>Thanks in advance for your help,</p>

---

## Post #2 by @lassoan (2021-05-13 19:28 UTC)

<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this documentation page</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#tutorials">tutorials</a> for an introduction to segmentation.</p>
<p>To answer your question more specifically, you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">choose any volume master volume</a>. Usually you would choose the volume where the structure you want to segment is the best visible. You can switch master volume any time, so you can use different volumes for segmenting different structures.</p>

---

## Post #3 by @Mostafa2020 (2021-05-18 14:21 UTC)

<p>Thanks, Andras. I think about testing a criterion for selecting an image representing the sample images, like taking the average of all images to make it as one image. What about this idea? Do you think it is possible to do it by 3D Slicer?</p>

---

## Post #4 by @lassoan (2021-05-18 18:00 UTC)

<p>It is very easy to combine images into one new image using numpy, see example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">script repository</a>. If geometry (origin, spacing, axis directions, extents) of the volumes are not the same then you need to resample all of them using the same reference volume.</p>
<p>Using some weighted average of the volumes makes sense as it is very simple and intensity differences that you have in any of the volumes may show up in the combined volume. There is a chance that sum of changes in multiple volumes result in zero difference in some relevant part of the volume, so you may experiment with different weighting factors or non-linear scaling.</p>

---

## Post #5 by @Mostafa2020 (2021-06-15 18:00 UTC)

<p>Thanks, Andras. It was very helpful.</p>

---
