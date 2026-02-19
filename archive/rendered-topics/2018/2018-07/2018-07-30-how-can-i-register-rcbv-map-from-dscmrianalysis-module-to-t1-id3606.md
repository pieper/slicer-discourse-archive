---
topic_id: 3606
title: "How Can I Register Rcbv Map From Dscmrianalysis Module To T1"
date: 2018-07-30
url: https://discourse.slicer.org/t/3606
---

# How can I register rCBV map from DSCMRIAnalysis module to T1-weighted contrast enhanced images?

**Topic ID**: 3606
**Date**: 2018-07-30
**URL**: https://discourse.slicer.org/t/how-can-i-register-rcbv-map-from-dscmrianalysis-module-to-t1-weighted-contrast-enhanced-images/3606

---

## Post #1 by @Kyu_Sung_Choi (2018-07-30 04:57 UTC)

<p>Dear Dr.Fedorov,</p>
<p>Thanks to your awesome works, I managed to make colored rCBV maps from DSC dicom files using DSCMRIAnalysis module.<br>
However, I was trying to register the rCBV maps as well as 4D DSC images to T1-weighted contrast enhanced images with FLIRT, FNIRT, and ANTS, which was not working at all.<br>
<em>So I’ve noticed that there is a module named “BRAINS” for general registration in Slicer, however I can’t tell which submodule should I use (e.g. BRAINSfit, Resample Image, etc.)</em>.<br>
<strong>1. Could you recommend proper pipeline to register rCBV maps as well as 4D DSC images to T1-weighted contrast enhanced images?</strong></p>
<p>Moreover, actually, I already register DWI/ADC images to T1-weighted contrast enhanced images using FLIRT only.<br>
<strong>2. Do I have to use “ResampleDTIvolume” module instead of FSL FLIRT to re-registration for better quality of registration?</strong></p>
<p>Thank you for your help!</p>
<p>Sincerely,<br>
Kyu Sung</p>

---

## Post #2 by @fedorov (2018-07-30 13:36 UTC)

<aside class="quote no-group" data-username="Kyu_Sung_Choi" data-post="1" data-topic="3606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b77776/48.png" class="avatar"> Kyu_Sung_Choi:</div>
<blockquote>
<ol>
<li>Could you recommend proper pipeline to register rCBV maps as well as 4D DSC images to T1-weighted contrast enhanced images?</li>
</ol>
</blockquote>
</aside>
<p>No, I don’t have a specific pipeline I could recommend, but as a general suggestion, you should probably try to register a representative frame from the DSC sequence to the T1w image. You should find a frame in the temporal sequence that has contrast that allows you to see similar structures as in T2w, and use that for registration. You can use MultiVolumeExplorer module to examine the temporal sequence and extract selected frame into a scalar volume that you should use for registration.</p>
<p>For registration, there are many options. Take a look at this FAQ: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/Registration" class="inline-onebox">Documentation/Nightly/FAQ/Registration - Slicer Wiki</a>. You can start with “General registration”, which wraps the <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/BRAINSFit">BRAINSFit tool</a>, or you can use the SlicerElastix extension, which has a lot of presets that might work for you (see <a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165" class="inline-onebox">Elastix registration toolbox is now available in Slicer</a>).</p>
<aside class="quote no-group" data-username="Kyu_Sung_Choi" data-post="1" data-topic="3606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b77776/48.png" class="avatar"> Kyu_Sung_Choi:</div>
<blockquote>
<ol start="2">
<li>Do I have to use “ResampleDTIvolume” module instead of FSL FLIRT to re-registration for better quality of registration?</li>
</ol>
</blockquote>
</aside>
<p>That module performs resampling of the image, not registration (i.e., you can sample the values from one image into a voxel lattice of a different geometry).</p>
<p>I do not have any knowledge about how Slicer registration tools compare with FSL FLIRT. If I were you, I would try all tools that are available before deciding on the optimal workflow, unless the first tool you try gives you a satisfactory result.</p>

---
