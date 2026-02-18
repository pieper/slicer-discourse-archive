# How can I "dicom to .ima"

**Topic ID**: 24620
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/how-can-i-dicom-to-ima/24620

---

## Post #1 by @hozermd (2022-08-03 14:46 UTC)

<p>Hi<br>
I work in interventional radiology. The 3D unit of our existing angiography device (Artis Zee) can fusion tomography images. However, cross-sectional images must be *.IMA. Since our tomography device is General Electric, I cannot export to *.IMA. How can I convert standard dicom file to IMA.<br>
Thanks</p>

---

## Post #2 by @pieper (2022-08-03 15:05 UTC)

<p>Sometimes .IMA is used as an extension for dicom files.  You could check by trying to import them into the slicer database.</p>

---

## Post #3 by @hozermd (2022-08-03 18:47 UTC)

<p>I can open images with .IMA extension on my computer for example with RadiAnt. But I cannot open standard DICOM images on angio device.</p>

---

## Post #4 by @pieper (2022-08-03 19:34 UTC)

<p>Are you saying that you think the .IMA files that do load on your angio device are dicom, but that other dicom files do not load, did you try changing the extension name of your standard dicom files to be .IMA?</p>
<p>If that’s not a workaround maybe someone else has ideas.  I’m not sure anyone here works with the angiography device you mentioned so you might be better off asking their technical support.</p>

---

## Post #5 by @hozermd (2022-08-04 20:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="24620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Are you saying that you think the .IMA files that do load on your angio device are dicom, but that other dicom files do not load,</p>
</blockquote>
</aside>
<p>Yes, that’s right.</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="24620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>did you try changing the extension name of your standard dicom files to be .IMA?</p>
</blockquote>
</aside>
<p>Yes, but didn’t work. But also, one of my friend exported the metadata of the sample *.IMA file to the standard dicom with MATLAB. Then it worked. So IMA is a dicom standard, I guess.</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="24620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If that’s not a workaround maybe someone else has ideas. I’m not sure anyone here works with the angiography device you mentioned so you might be better off asking their technical support.</p>
</blockquote>
</aside>
<p>Yes, I think so. I talk technical support. They couldn’t help as we didn’t have Siemens tomography. There are various types of technical services. The applicator knows how to use the device and the other guys how to fix and update the angio device. I couldn’t access the third kind of expert, expert of dicom and pacs management :). But maybe if someone is using Syngo workstation working with Siemens, maybe there is *.IMA export option. I’ve never used Syngo before. Or maybe there is someone who is sound familiar to IMA. Thank you for your attention.</p>

---
