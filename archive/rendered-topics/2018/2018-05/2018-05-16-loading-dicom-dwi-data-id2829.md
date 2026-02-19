---
topic_id: 2829
title: "Loading Dicom Dwi Data"
date: 2018-05-16
url: https://discourse.slicer.org/t/2829
---

# Loading DICOM DWI Data

**Topic ID**: 2829
**Date**: 2018-05-16
**URL**: https://discourse.slicer.org/t/loading-dicom-dwi-data/2829

---

## Post #1 by @cphillips (2018-05-16 18:42 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1<br>
Expected behavior: DICOM DWI Data loads normally<br>
Actual behavior: DICOM DWI Data appears garbled</p>
<p>I am using the DICOM Browser to import and load MRI data. The imported DICOM folder holds data of a variety of scan types (T2 weighted, T1 weighted, diffusion weighted, etc.). When attempting to load the diffusion weighted (DWI) scan from this folder, I get the following pop-up:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffe6913d61bd6c039a5db2bc7a3a1bf8e2939f17.png" alt="DWI_Load_Error" data-base62-sha1="AvNK4VJVfMLthTchvlhO9kX3beL" width="516" height="117"></p>
<p>First of all, how do I examine the data in advanced mode? I have looked through the Application Settings and haven’t been able to find anything on how to do this.</p>
<p>After I click OK, the Python Interactor gives the following error message:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/977a0d7ec82357b93ab3061c2cdba0c8f59906ad.png" data-download-href="/uploads/short-url/lC1ASjCHRx6j9nzSlCjNYBVv9tb.png?dl=1" title="DWI_Load_Error_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/977a0d7ec82357b93ab3061c2cdba0c8f59906ad.png" alt="DWI_Load_Error_2" data-base62-sha1="lC1ASjCHRx6j9nzSlCjNYBVv9tb" width="690" height="65" data-dominant-color="FCF1EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DWI_Load_Error_2</span><span class="informations">1267×121 6.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The image that does appear is very garbled and does not match what I see when I pull the data up in a DICOM viewer. I also tried to open the corresponding .nrrd file, which was unsuccessful (it stalled on each try, both before and after restarting Slicer).</p>
<p>Any ideas on how I might load this DWI scan effectively? Thank you!</p>

---

## Post #2 by @pieper (2018-05-16 19:08 UTC)

<aside class="quote no-group" data-username="cphillips" data-post="1" data-topic="2829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/848f3c/48.png" class="avatar"> cphillips:</div>
<blockquote>
<p>how do I examine the data in advanced mode?</p>
</blockquote>
</aside>
<p>Bottom right of the study browser:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fade01162ad17357d88689c99feffc9e70e6d368.png" alt="image" data-base62-sha1="zNh0Az5h3u7PX45dZkHDaLsXKM8" width="391" height="81"></p>
<aside class="quote no-group" data-username="cphillips" data-post="1" data-topic="2829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/848f3c/48.png" class="avatar"> cphillips:</div>
<blockquote>
<p>Any ideas on how I might load this DWI scan effectively? Thank you!</p>
</blockquote>
</aside>
<p>Did you install the <a href="http://dmri.slicer.org/">SlicerDMRI</a> extension with the latest nightly build?  It provides a DWI-specific plugin for the dicom module.</p>

---

## Post #3 by @cphillips (2018-05-16 20:55 UTC)

<p>I did indeed install that extension. What is the plugin for the dicom module called/how do I access it?</p>

---

## Post #4 by @pieper (2018-05-16 21:14 UTC)

<p>If you have SlicerDMRI installed, then the plugin should be listed on the left side in Advanced mode and selected by default.  If it detects your DWI data as something it can load then after you run Examine the DWI loader will be chosen.  But if your DWI data isn’t recognized, which is not uncommon, then you need to dig deeper to debug, probably by using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWIConverter">DWIConvert</a> directly.</p>
<p>As a heads up, DWI data is sophisticated and not well standardized - it’s entirely possible that the data cannot be loaded correctly because nobody has handled your particular data format.  If you aren’t able to debug it yourself, then usually the only real way forward is to acquire a phantom or human volunteer study that you are allowed to share publicly and make it available with all the details about how it was acquired.  If you can share the data there a chance people can help you.</p>

---
