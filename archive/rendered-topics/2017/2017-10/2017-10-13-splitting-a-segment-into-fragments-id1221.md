---
topic_id: 1221
title: "Splitting A Segment Into Fragments"
date: 2017-10-13
url: https://discourse.slicer.org/t/1221
---

# Splitting a segment into fragments

**Topic ID**: 1221
**Date**: 2017-10-13
**URL**: https://discourse.slicer.org/t/splitting-a-segment-into-fragments/1221

---

## Post #1 by @moselhy (2017-10-13 21:10 UTC)

<p>Hello,</p>
<p>I would like to split a segment into three and get rid of the first and second fragment. The segment is of a leg so we can assume that the length is always the greater dimension, which is helpful when finding the axis to cut on.</p>
<p>However, I am having trouble seeing if there is any segmented area in a slice at a specific RAS coordinate, i.e. if the volume of the segment in that slice is 0…</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2017-10-13 21:25 UTC)

<p>What do you mean by fragments? Disconnected components - islands? If yes, then you can use the Islands effect to split, delete, etc. them as needed.</p>

---

## Post #3 by @moselhy (2017-10-13 21:46 UTC)

<p>I am trying to split the leg along its length into three equal fragments, and take the middle one and export it to another segment</p>

---

## Post #4 by @lassoan (2017-10-14 18:56 UTC)

<p>You can create a new Segment and split it up with Scissors (Fill inside). In Masking settings, choose to allow editing inside all segments.</p>

---

## Post #5 by @lassoan (2017-10-14 19:17 UTC)

<p>If you need to do this programmatically then you can create a solid cube segment and use Logical operators effect to remove parts of the other segments that are outside the cube.</p>

---

## Post #6 by @TudorSlicer (2017-10-15 19:34 UTC)

<p>Why not split using meshmixer?.  It is quite easy to do.  Also open source.<br>
Are you splitting the bone from a Ct?<br>
Boyd</p>

---

## Post #7 by @lassoan (2017-10-15 21:33 UTC)

<p>Scissors effect in Segment editor in Slicer is just as effective as Meshmixer, but a huge advantage of Slicer that while you are editing your mesh, you can cross-reference it with the original image.</p>
<p>Meshmixer cannot show you the original CT, so you essentially edit the mesh blindly: you cannot check how smoothing or other operations made your model deviate from ground truth imaging data. Another shortcoming of using Meshmixer for medical image computing is that it always have to be used along with other software that can import DICOM images and can segment the images, so you end up with a complex processing workflow, involving several software and manual export/import data between them.</p>

---

## Post #8 by @lassoan (2017-10-15 23:41 UTC)

<p>By the way, MeshMixer is not open-source. You have very limited options for customizing it or combining it with your own software (compared to open-source software) and Autodesk may decide to stop distributing it for free or change/remove features as they wish.</p>

---

## Post #9 by @moselhy (2018-01-18 22:16 UTC)

<p>Thanks, could you please point me to the documentation on how to create a solid cube segment?</p>

---

## Post #10 by @lassoan (2018-01-18 22:34 UTC)

<p>You can create a cube model using “Create models” module (in SlicerIGT extension) and then import it into a segmentation node using Segmentations module. You can also create cube shape using Scissors effect in two orthogonal views.</p>

---
