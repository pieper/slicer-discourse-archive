---
topic_id: 4378
title: "Issue Loading Nii Files Onto 3D Slicer"
date: 2018-10-12
url: https://discourse.slicer.org/t/4378
---

# Issue loading .nii files onto 3D slicer 

**Topic ID**: 4378
**Date**: 2018-10-12
**URL**: https://discourse.slicer.org/t/issue-loading-nii-files-onto-3d-slicer/4378

---

## Post #1 by @rjortiz2 (2018-10-12 17:44 UTC)

<p>I am having issue loading/viewing my .nii files onto my computer.</p>
<p>*I was able to view and view my .nii files on itk snap, so it doesn’t seem to be a data problem</p>
<ul>
<li>I loaded some example .nii files that I downloaded online onto 3D slicer and they were able to be viewed as well.</li>
</ul>
<p>I am running on a OS X and using version 4.8.1 r26813.</p>
<p>Is there a way to troubleshoot this and view my files?</p>

---

## Post #2 by @lassoan (2018-10-12 17:45 UTC)

<p>What did you do exactly? What did you expect to happen? What happened instead?<br>
Could you also try with latest nightly version of Slicer?</p>

---

## Post #3 by @rjortiz2 (2018-10-12 18:20 UTC)

<p>I converted my data from sti to nifti. Data size for each nifiti file is 73.7 mb.  I tried drag-and-dropping the files, but I could not view the images at all. I believe I am running on the nightly version (downloaded original, then downloaded the nightly version last night). I also tried loading the nifti  file onto the file directory and I am still not able to view it.</p>
<p>I was expecting to view my nifti files when I dropped them (see video). My .nii files are able to be viewed on other softwares.  I was also able to view other fMRI .nii files that I found online. I can upload some of my files on dropbox, if that works as well</p>
<p><a href="https://www.dropbox.com/s/ygir8ance23iiwl/nii_example_vid.mov?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/ygir8ance23iiwl/nii_example_vid.mov?dl=0</a><br>
<a href="https://www.dropbox.com/s/ygir8ance23iiwl/nii_example_vid.mov?dl=0" rel="nofollow noopener"></a></p>
<p><a href="https://www.dropbox.com/s/ygir8ance23iiwl/nii_example_vid.mov?dl=0" rel="nofollow noopener">nii_example_vid.mov</a></p>
<p><a href="http://www.dropbox.com" class="onebox" target="_blank" rel="nofollow noopener">www.dropbox.com</a></p>
<p>Shared with Dropbox</p>
<p>Thank you,</p>
<p>Richard Joaquin Ortiz, B.S.</p>
<p>R.I.S.E. Pre-Doctoral Fellow, Biological Sciences</p>
<p>Department of Biological Sciences</p>
<p>Dr. Cushing Laboratory</p>
<p>The University of Texas at El Paso</p>
<p>500 West University Ave</p>
<p>El Paso, TX 79968</p>
<p>rjortiz2@miners.utep.edu</p>
<p>Phone: 915.731.3354</p>

---

## Post #4 by @ihnorton (2018-10-15 01:22 UTC)

<p>Please share a dataset, and how you converted the files to nii. (<em>make sure there is no patient information in the files or filenames</em>)</p>
<p>If you can’t share data, then please check the error log and share it:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report</a></p>

---

## Post #5 by @rjortiz2 (2018-10-17 23:38 UTC)

<p><a href="https://www.dropbox.com/sh/hzhmglne8bto3pv/AADvSOpScH4UwthPtkJPbF-wa?dl=0" rel="nofollow noopener">nii. file</a></p>

---

## Post #6 by @Mihail_Isakov (2018-10-18 01:26 UTC)

<p>Drag-and-drop worked for me (i have latest nightly build), but it is 4D image (probably fMRI of mice looking at a cheese or a cat). To load the image as 4D put it in a separate folder, go to<br>
MultiVolumeSupport-&gt;MultiVolumeImported<br>
select folder, create new multi volume, click “Import”<br>
Go to MultiVolumeSupport-&gt;MultiVolumeExplorer, move slider or “Play”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad1a1968678788a63a9d01e07eed40a60f2ffee0.png" data-download-href="/uploads/short-url/oHkwe06ipJGP1W2sVkvng12QTcY.png?dl=1" title="Screenshot%20at%202018-10-18%2003-25-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1a1968678788a63a9d01e07eed40a60f2ffee0_2_690x379.png" alt="Screenshot%20at%202018-10-18%2003-25-12" data-base62-sha1="oHkwe06ipJGP1W2sVkvng12QTcY" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1a1968678788a63a9d01e07eed40a60f2ffee0_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1a1968678788a63a9d01e07eed40a60f2ffee0_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1a1968678788a63a9d01e07eed40a60f2ffee0_2_1380x758.png 2x" data-dominant-color="A4A4A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20at%202018-10-18%2003-25-12</span><span class="informations">1724×948 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @ihnorton (2018-10-18 13:57 UTC)

<p>Yes, the first volume of both loads fine for me (even in 4.8), but as <a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> says you will need to use MultiVolume to browse as a 4D volume.</p>
<p>That said, if you run in to issues converting via the intermedia STI step, you might want to try: <a href="https://github.com/neurolabusc/Bru2Nii">https://github.com/neurolabusc/Bru2Nii</a></p>

---

## Post #8 by @rjortiz2 (2019-02-27 22:32 UTC)

<p>Awesome!</p>
<p>I was able to upload the files needed!</p>
<p>Thanks!</p>

---
