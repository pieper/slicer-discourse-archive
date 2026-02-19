---
topic_id: 13427
title: "Creating Models From Dicom Files In 3 Different Crossections"
date: 2020-09-10
url: https://discourse.slicer.org/t/13427
---

# Creating models from dicom files in 3 different crossections

**Topic ID**: 13427
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/creating-models-from-dicom-files-in-3-different-crossections/13427

---

## Post #1 by @BlueLan (2020-09-10 18:11 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2</p>
<p>Hi everyone,</p>
<p>I am trying to construct a knee model using data from <a href="https://stanfordmlgroup.github.io/competitions/mrnet/" rel="nofollow noopener">Stanford’s MRI knee images</a> (stored in nonpy arrays). For each knee, the data is stored in 3 different cross-sections - sagittal, coronal and axial. However, for each knee, each cross-section only contains ~30 slices and there is <em>no other information other than the image array</em> in the data package. I have the following questions:</p>
<ol>
<li>
<p>I’ve converted the image arrays in each crosssection in 3 dicom files - 1 sag, 1 cor, 1 ax. Is it possible to open these 3 dicom files in Slicer at once and let slicer interpolate their relative position to one another and construct a model?</p>
</li>
<li>
<p>When I tried to open the 3 dicom files at once in Slicer, Slicer could not identify them as 1 single patient (even though I let them have the same patient name). Is there a way to open them as 1 single patient?</p>
</li>
<li>
<p>I’ve been browsing through past discussions about similar topics. A person has recommended <a href="https://github.com/gift-surg/NiftyMIC" rel="nofollow noopener">NiftyMic</a>. However, the software seems to only accept .nii files (seems to be file format specifically for neuroimaging ???). I am not sure if it is okay to convert mri image arrays to .nii files. If you have experience with using NityMic, would you mind sharing some insights?</p>
</li>
</ol>
<p>Thanks a lot!</p>

---

## Post #2 by @lassoan (2020-09-10 18:19 UTC)

<aside class="quote no-group" data-username="BlueLan" data-post="1" data-topic="13427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bluelan/48/8059_2.png" class="avatar"> BlueLan:</div>
<blockquote>
<p>I’ve converted the image arrays in each crosssection in 3 dicom files - 1 sag, 1 cor, 1 ax. Is it possible to open these 3 dicom files in Slicer at once and let slicer interpolate their relative position to one another and construct a model?</p>
</blockquote>
</aside>
<p>Yes, they should be all loaded correctly and appear in the same physical position.</p>
<aside class="quote no-group" data-username="BlueLan" data-post="1" data-topic="13427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bluelan/48/8059_2.png" class="avatar"> BlueLan:</div>
<blockquote>
<p>When I tried to open the 3 dicom files at once in Slicer, Slicer could not identify them as 1 single patient (even though I let them have the same patient name). Is there a way to open them as 1 single patient?</p>
</blockquote>
</aside>
<p>Most likely UIDs were not correctly replaced during anonymization. This should not be an issue.</p>
<p>You can load all 3 DICOM files at once, you can switch between them any time and can show a blended display of any two at the same time in any of the slice viewers. You can also use any of them in creating one 3D segmentation. Having 3 sparse (highly anisotropic resolution) volumes is nearly not as good as one isotropic volume - see this topic for details: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing? - #2 by lassoan</a></p>
<aside class="quote no-group" data-username="BlueLan" data-post="1" data-topic="13427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bluelan/48/8059_2.png" class="avatar"> BlueLan:</div>
<blockquote>
<p>browsing through past discussions about similar topics. A person has recommended <a href="https://github.com/gift-surg/NiftyMIC">NiftyMic</a>. However, the software seems to only accept .nii files (seems to be file format specifically for neuroimaging ???).</p>
</blockquote>
</aside>
<p>You can save the volume in nifti format using Save data window (select Nifti in File Format column). We don’t have experience with NiftyMic but it seems that you will! Let us know if you find it useful. People quite often struggle with getting a decent 3D volumes from these kind of sparse acquisitions.</p>

---

## Post #3 by @BlueLan (2020-09-25 00:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, thank you so much for your response! I have some questions that I want to confirm with you.</p>
<ol>
<li>When I open the 3 dicom files in Slicer, their “front side” all appear in the axial position. Could this happen because I have nothing in the image orientation and patient orientation tags in the dicom files?</li>
</ol>
<p>2.since I only have 3 anisotropic dicom files, I could only create 3 spare volumes based on each dicom file individually, right? The only way that I could make an isotropic volume is by using the toolkit NiftyMic, and slicer does not have any build-in functions to make isotropic volumes by ansisotropic volumes?</p>

---

## Post #4 by @lassoan (2020-09-25 01:20 UTC)

<aside class="quote no-group" data-username="BlueLan" data-post="3" data-topic="13427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bluelan/48/8059_2.png" class="avatar"> BlueLan:</div>
<blockquote>
<p>When I open the 3 dicom files in Slicer, their “front side” all appear in the axial position. Could this happen because I have nothing in the image orientation and patient orientation tags in the dicom files?</p>
</blockquote>
</aside>
<p>They should be all oriented correctly. For example, in an axial slice view, you should see an image slice orthogonal to the patient IS axis, regardless of what was the slice orientation during acquisition.</p>
<aside class="quote no-group" data-username="BlueLan" data-post="3" data-topic="13427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bluelan/48/8059_2.png" class="avatar"> BlueLan:</div>
<blockquote>
<p>since I only have 3 anisotropic dicom files, I could only create 3 spare volumes based on each dicom file individually, right?</p>
</blockquote>
</aside>
<p>You can create an isotropic volume from any of them. Use the one that has high resolution along the most important axis.</p>
<aside class="quote no-group" data-username="BlueLan" data-post="3" data-topic="13427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bluelan/48/8059_2.png" class="avatar"> BlueLan:</div>
<blockquote>
<p>The only way that I could make an isotropic volume is by using the toolkit NiftyMic, and slicer does not have any build-in functions to make isotropic volumes by ansisotropic volumes?</p>
</blockquote>
</aside>
<p>You should be able to run NiftyMic in Slicer’s Python environment but there is no convenient graphical user interface available for setting it up, set inputs, and get outputs. If you set it up manually and confirm that it works well then maybe we’ll invest time into developing an easy-to-use GUI for it (or you can even do it yourself - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">programming tutorial</a>).</p>

---
