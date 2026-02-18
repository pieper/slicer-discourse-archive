# 3D cardiac CT to 4D in 3D Slicer?

**Topic ID**: 19038
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/3d-cardiac-ct-to-4d-in-3d-slicer/19038

---

## Post #1 by @xiaolin (2021-08-03 11:08 UTC)

<p>Hello, I want to use the 3D cardiac CT to get the 4D data. Does anybody know there is a special module in 3D slicer that can perform? Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-08-03 11:51 UTC)

<p>Do you mean that you would like to warp a cardiac CT to simulate cardiac and respiratory motion?</p>
<p>You can achieve this by getting a transform sequence from a similar 4D CT using SequenceRegistration extension, then apply that transform to your 3D CT image. You can use 4D cardiac CTs in Sample Data module. You need to choose the fixed frame for the sequence registration that is in the same cardiac phase as your single 3D image. Before you apply the transform sequence, you need to align your single 3D image to the fixed frame (for example, using SlicerElastix extension).</p>

---

## Post #3 by @xiaolin (2021-08-03 12:21 UTC)

<p>Yes, I got the 3D data from the animal cardiac CT, want to simulate the displacement of the heart during the whole cardiac cycle. Thanks for your help, I will try it.</p>

---

## Post #4 by @xiaolin (2021-08-04 08:38 UTC)

<p>Hi Andras, I tried your method, it’s working quite well. Can I ask you a further question? Is it possible to make a beating heart model (or animation) using the 4D CT created from the 3D CT data? <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=10" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #5 by @lassoan (2021-08-04 18:47 UTC)

<p>Yes, you can create a beating heart model by segmenting the heart image and then apply the same transform sequence to the segmentation or exported models.</p>

---

## Post #6 by @xiaolin (2021-08-05 08:02 UTC)

<p>Thank you so much. Have a good day.</p>

---
