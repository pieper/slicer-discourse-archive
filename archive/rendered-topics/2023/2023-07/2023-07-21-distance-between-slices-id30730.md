---
topic_id: 30730
title: "Distance Between Slices"
date: 2023-07-21
url: https://discourse.slicer.org/t/30730
---

# Distance between slices 

**Topic ID**: 30730
**Date**: 2023-07-21
**URL**: https://discourse.slicer.org/t/distance-between-slices/30730

---

## Post #1 by @Lindee_Wilson (2023-07-21 17:08 UTC)

<p>Hi,</p>
<p>I am currently segmenting something from a screenshot. Therefore, it is a 2D image. I am wanting to make it into a 2D surface mesh. I was told since 3D slicer will only export as 3D .stl files, to duplicate the segment and put distance between them. As a beginner, I really have no idea how to do that. Could you help?</p>

---

## Post #2 by @lassoan (2023-07-21 17:09 UTC)

<p>What would you like to segment on what kind of images?</p>

---

## Post #3 by @Lindee_Wilson (2023-07-21 19:24 UTC)

<p>I am trying to segment some tissue from a jpeg file.</p>

---

## Post #4 by @lassoan (2023-07-21 19:26 UTC)

<p>What is the imaging modality? What would you like to segment? Do you have some constraints (maximum time, required accuracy, available operator expertise, …)?</p>

---

## Post #5 by @Lindee_Wilson (2023-07-21 19:30 UTC)

<p>I am very much a beginner. Can you explain what you’re meaning by imaging modality?</p>

---

## Post #6 by @lassoan (2023-07-21 19:30 UTC)

<p>Imaging modality: CT, MRI, ultrasound, microscopy, etc.</p>

---

## Post #7 by @Lindee_Wilson (2023-07-21 19:33 UTC)

<p>CT. But I only have singular slice</p>

---

## Post #8 by @lassoan (2023-07-21 19:37 UTC)

<p>What would you like to segment? Do you have some constraints (maximum time, required accuracy, available operator expertise, …)?</p>
<p>Could you attach a screenshot of an image with an example segmentation?</p>

---

## Post #9 by @Lindee_Wilson (2023-07-21 19:43 UTC)

<p>I am segmenting collagen beams. I do not know anything about constraints. I segmented the beams and made a model. I was told to overlay a second segmentation of the same beams 30 micrometers above the first. I was wondering if there was any way to do that with only one image slice.</p>

---

## Post #10 by @lassoan (2023-07-21 19:45 UTC)

<p>If you don’t have any constraints - you have the necessary expertise to segment what you need with sufficient accuracy and you can spend as much time with it as needed - then you can use existing segmentation tools in Segment Editor to manually segment the image.</p>

---

## Post #11 by @Lindee_Wilson (2023-07-21 19:47 UTC)

<p>This still doesn’t answer my question, though. My segmentation is done the way I need it to be done.</p>

---

## Post #12 by @lassoan (2023-07-21 19:53 UTC)

<p>You can add the same slice to a volume by adding a filename similar to the original one (for example, image001.jpg, image002.jpg) and load it with <code>Single slice</code> option disabled.</p>
<p>For a thicker slice, you don’t need to duplicate slices, but you can set a larger spacing value for the third axis.</p>
<p>If this does not fully answer you question then please draw a sketch or explain it in more detail what you want to achieve. Why do you want to overlay a “second segmentation”? What is the overall goal of your project? How this specific task (“overlaying a second segmentation 30 micrometer above the first”) will help you to achieve that?</p>

---

## Post #13 by @Lindee_Wilson (2023-07-21 20:02 UTC)

<p>I will try the larger spacing value route. How do I do that?</p>

---

## Post #14 by @lassoan (2023-07-22 00:51 UTC)

<p>You can set the image spacing values in <code>Volumes</code> module, in the <code>Volume information</code> section.</p>

---
