---
topic_id: 6903
title: "Computing Transformation Matrix On Labelmaps"
date: 2019-05-23
url: https://discourse.slicer.org/t/6903
---

# Computing transformation matrix on labelmaps

**Topic ID**: 6903
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/computing-transformation-matrix-on-labelmaps/6903

---

## Post #1 by @m.hilani (2019-05-23 18:49 UTC)

<p>Hi all,</p>
<p>I’ve been working on segmentation of a full body MRI, and after segmenting most of the tissues I realized the need to co-register all the different sequences that I’m using for segmentation.<br>
Using 3D slicer, I was able to have one reference MRI sequence and a transformation matrix that allows each other scan I used in my segmentation to be co registered with it.</p>
<p>My question is about the labelmaps that I have already created prior to co-registering the sequences together.<br>
Is it possible to apply the transform matrix on the labelmaps to have them all co registered with the reference MRI sequence?<br>
If possible could you explain to me how this is done and how to create a model (.stl) from the transformed labelmap file (.nii).</p>
<p>Thank you!<br>
Michel</p>

---

## Post #2 by @lassoan (2019-05-23 18:58 UTC)

<p>You can apply the same transformation to a segmentation or model (STL file) as you applied to the volume. You can apply a transform in Transforms module (Apply transform section) or in Data module (double-click on the transform column and select transform).</p>

---

## Post #3 by @m.hilani (2019-05-28 12:19 UTC)

<p>Thank you so much Andras!<br>
I didn’t realize that I can upload the .stl file and apply the transformation directly on it.</p>

---
