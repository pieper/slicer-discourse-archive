---
topic_id: 12229
title: "How To Stitch Two Dicom X Ray Files To Form A Full Length In"
date: 2020-06-26
url: https://discourse.slicer.org/t/12229
---

# How to stitch two DICOM X-ray files to form a full length integrated DICOM file

**Topic ID**: 12229
**Date**: 2020-06-26
**URL**: https://discourse.slicer.org/t/how-to-stitch-two-dicom-x-ray-files-to-form-a-full-length-integrated-dicom-file/12229

---

## Post #1 by @Beygi (2020-06-26 13:03 UTC)

<p>Operating system: Windows 7<br>
Slicer version:4.5.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Dear Community,<br>
Hope this message finds you all well. Beforehand, I am sorry as the question may look superficial to some of you. As I am a beginner in using Slicer and I noticed that this software has the potential to stitch the DICOM files together to generate a longer integrated DICOM file ( in case where the X-ray can not cover the whole interested length of scanning), I was wondering may you kindly help me on how to go through to successfully stitch my 2 or3 DICOM file to transform them into one full-length DICOM file please?</p>
<p>Many thanks for your time.</p>
<p>Best,<br>
Bob</p>

---

## Post #2 by @pieper (2020-06-26 19:23 UTC)

<p>Hi - You probably won’t get a very precise alignment, but you can paste them together with the following basic steps:</p>
<ul>
<li>load all three X-ray images.  They will be one-slice thick volumes, so they’ll only show in the axial (red) view.</li>
<li>create two linear transforms and put one in each</li>
<li>use the transform controls to position the images where you want them</li>
<li>harden the transforms on the images</li>
<li>use the CropVolume module and stretch the ROI to include all three images and apply</li>
<li>use the Add Scalar Volumes module to add each of the transformed volumes into the new big image</li>
<li>export the result as dicom or other format.</li>
</ul>
<p>p.s. this should all work in version 4.5, but it’s very old and you should get the latest nightly version since it has many fixes and new features.</p>

---

## Post #3 by @Beygi (2020-06-29 09:19 UTC)

<p>Dear Mr. Pieper,</p>
<p>Thank you very much for your time to explain the procedure to me, please. As I am a layman in this field, may you kindly give me more information such as how to harden the transforms, working on CropVolume etc? Is there any guideline to further clarification on beginners’ level, please?</p>
<p>Once again may thanks.</p>
<p>Best,<br>
Babak</p>

---

## Post #4 by @pieper (2020-06-29 18:28 UTC)

<p>Hi Babak -</p>
<p>It’s true the software is kind of complex and there are several things to learn - it’s hard to describe in detail but I hope the keywords in the outline I sent earlier should let you search google and this forum.</p>
<p>A good way to start getting familiar is to try the tutorials, and then work your way to the Registration topic, which addresses things related to your project.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training</a></p>

---

## Post #5 by @BeakyThings (2020-10-10 20:02 UTC)

<p>My apologies for asking a question in an old thread.</p>
<p>Will this process work for aligning two DICOM <strong>stacks</strong> (~800 images each) to generate a new, stitched <strong>stack</strong> of DICOMs? I’m not certain if mine is a similar or different problem to the original poster because it seemed like the input/output of the original post was only 1-2 files.</p>
<p>Problem I’m having: I’m working with an old GE CT-scanner that outputs a stitched DICOM stack with a slight misalignment in it. I’ve tried fixing the alignment in the attached (and equally old) computer but it takes a long time and doesn’t always work right. I can get the original stacks used to create the stitch and I’m hoping 3d-Slicer can help me to align the images before I start segmenting.</p>
<p>Thank you.</p>

---

## Post #6 by @lassoan (2020-10-10 20:20 UTC)

<p>Yes, the method works just as well with 3D volumes as with 2D images: align them, resample them to be in the same coordinate system, then add them.</p>

---
