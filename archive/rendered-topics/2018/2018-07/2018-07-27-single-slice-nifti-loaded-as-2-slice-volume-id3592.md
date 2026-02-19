---
topic_id: 3592
title: "Single Slice Nifti Loaded As 2 Slice Volume"
date: 2018-07-27
url: https://discourse.slicer.org/t/3592
---

# Single slice nifti loaded as 2 slice volume

**Topic ID**: 3592
**Date**: 2018-07-27
**URL**: https://discourse.slicer.org/t/single-slice-nifti-loaded-as-2-slice-volume/3592

---

## Post #1 by @Felix_Navarro_Guirad (2018-07-27 14:46 UTC)

<p>Dear all, I’m having a issue while loading a single slice nifti file.</p>
<p>When I load this file (<a href="https://drive.google.com/file/d/1B3_lQWOoUnr333--sk5gJuJRA77JOc_n/view?usp=sharing" rel="nofollow noopener">1.nii</a>) into slicer, the volume module informs me about that it is a 2 slice volume but it should be 1 slice only.</p>
<p>I created the file using matlab, when I load it into imageJ or matlab, both show 1 slice volume.</p>
<p>Using the same library from Matlab I created a nifti file containing a mask (<a href="https://drive.google.com/file/d/1cW43VhbTutUmyPqSE9EYhtlyW0ofqfSt/view?usp=sharing" rel="nofollow noopener">mascaraAlineacion.nii</a>), which is correctly loaded as 1 slice labelmap.</p>
<p>I’m quite sure that both files only differ in the content of the image and glmin/glmax values contained into the header.</p>
<p>Is this a bug?  or should I take care of any special requirement for the nii header?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @fedorov (2018-07-27 14:48 UTC)

<p>I don’t have an answer to your specific question, but why don’t you look at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension</a> instead of writing NIfTI file?</p>

---

## Post #3 by @lassoan (2018-07-27 15:02 UTC)

<p>As a quick test, you can use nrrdwrite.m function of MatlabBridge to write a nrrd image file - <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver</a></p>
<p>The mascaraAlineacion.nii file that you’ve sent the link to, can be loaded without any warnings in the nightly build. It seems to be a binary image, so you may want to load it as a labelmap volume (in “Add data” dialog, click “Show options”, then click “Labelmap”).</p>

---

## Post #4 by @ihnorton (2018-07-27 19:45 UTC)

<aside class="quote no-group" data-username="Felix_Navarro_Guirad" data-post="1" data-topic="3592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/4491bb/48.png" class="avatar"> Felix_Navarro_Guirad:</div>
<blockquote>
<p>When I load this file (<a href="https://drive.google.com/file/d/1B3_lQWOoUnr333--sk5gJuJRA77JOc_n/view?usp=sharing">1.nii </a>) into slicer, the volume module informs me about that it is a 2 slice volume but it should be 1 slice only.</p>
</blockquote>
</aside>
<p>I loaded this file in to three different Slicer versions I had running (2018/07-25 &amp; 06-13, and 4.8.1). All of them show dimensions as 512x512x1 mm in the Volumes module.</p>

---

## Post #5 by @Felix_Navarro_Guirad (2018-07-30 09:07 UTC)

<p>Dear all, thank you very muh for your replies.</p>
<p>I have tested this on versions 4.5.0-1 and 4.9.0 (18/07/2018). On both versions the problem appears when I do NOT select the “single file” option when I load the volumes.</p>
<p>I intend to use Slicer from Matlab using a system call to send a CLI command. I intend to perform several rigid registrations. May I check if Brainsfit is using the correct volumes?</p>
<p>Thank you in advance.</p>

---

## Post #6 by @lassoan (2018-07-30 10:18 UTC)

<p>If you have multiple slices with similar enough names in the same folder then Slicer can load them as a 3D volume. If you prefer to load just a single slice then check single file option, put files in separate folders, or use different file names.</p>
<p>I’m not sure if BRAINS other registration modules support single-slice volume registration, you may need to resample the single-slice volume to have at least 3 slices (for example, using Crop and resample module, as described in other topics in this forum). If you have any problems with registration, please post it in a new topic and give high-level overview, what you would like to do, and any specific problem that you have.</p>

---
