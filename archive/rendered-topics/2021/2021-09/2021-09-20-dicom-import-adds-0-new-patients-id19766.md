---
topic_id: 19766
title: "Dicom Import Adds 0 New Patients"
date: 2021-09-20
url: https://discourse.slicer.org/t/19766
---

# DICOM Import Adds 0 New Patients

**Topic ID**: 19766
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/dicom-import-adds-0-new-patients/19766

---

## Post #1 by @ckbow (2021-09-20 17:28 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>When I try to import DICOM files, I get a message that says “Added 0 New Patients, 0 Studies” etc. This only occurs with certain files, even though I am able to upload other DICOM data from the same folder. I have seen threads reporting a similar issue, but I am not familiar enough with Slicer (or computer terminology in general) to follow along with the solutions.</p>

---

## Post #2 by @lassoan (2021-09-20 17:34 UTC)

<p>Are you sure the patients/studies/series have not been already imported into the database? Remove all data sets from the DICOM database and see if anything shows up after that.</p>
<p>If that does not help then please go through each and every item to check in the DICOM module documentation’s <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser">data import troubleshooting section</a>.</p>

---

## Post #3 by @ckbow (2021-09-20 17:40 UTC)

<p>Yes, I have a spreadsheet with all of the patients’ file names and the corresponding Patient ID that is generated upon import. All the files that I have been able to import are accounted for. I am able to import all except for 2, and I have ensured that the files themselves are not redundant copies of one another.</p>

---

## Post #4 by @lassoan (2021-09-20 17:52 UTC)

<p>The files themselves (filename, folder, etc.) do not matter in DICOM, but they are identified by the universally unique identifiers stored inside the files. For example, if you have the same series instance UID in multiple files then only one of them will be imported. You can ensure that this is not the case by clearing the database and just loading a single file or folder.</p>

---

## Post #5 by @ckbow (2021-09-20 18:00 UTC)

<p>I believe one of the suggestions from the link you sent has solved the issue. On an unrelated note, is there any possible fix for distorted data caused by unevenly-spaced images (the acquisition geometry regularization does not fix it)?</p>

---

## Post #6 by @pieper (2021-09-20 18:03 UTC)

<aside class="quote no-group" data-username="ckbow" data-post="5" data-topic="19766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/49beb7/48.png" class="avatar"> ckbow:</div>
<blockquote>
<p>On an unrelated note, is there any possible fix for distorted data caused by unevenly-spaced images (the acquisition geometry regularization does not fix it)?</p>
</blockquote>
</aside>
<p>What kind of distortion do you see?  Geometry regularization should handle variable slice spacing unless there are overlapping acquisitions or something.</p>

---

## Post #7 by @ckbow (2021-09-20 18:21 UTC)

<p>The image seems to cut from one structure directly to a distant one. For example, the image seems to jump from the condyles of the tibia to partway down the shaft. Viewed from the side, the image appears “smeared”.</p>

---

## Post #8 by @pieper (2021-09-20 18:26 UTC)

<p>You could post a screenshot to confirm, but that sounds like exactly what I would expect.  For many ortho CT scans they move the table slowly through certain parts for high resolution and then faster in the parts where they don’t want detail.  In Slicer we preserve the geometric relationships so that measurements are  correct but the interpolated data can look smeared because it is sparse.</p>

---

## Post #9 by @lassoan (2021-09-20 22:28 UTC)

<aside class="quote no-group" data-username="ckbow" data-post="5" data-topic="19766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/49beb7/48.png" class="avatar"> ckbow:</div>
<blockquote>
<p>I believe one of the suggestions from the link you sent has solved the issue.</p>
</blockquote>
</aside>
<p>Which one was that?</p>
<aside class="quote no-group" data-username="ckbow" data-post="7" data-topic="19766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/49beb7/48.png" class="avatar"> ckbow:</div>
<blockquote>
<p>The image seems to cut from one structure directly to a distant one.</p>
</blockquote>
</aside>
<p>When using classic (one-slice-per-file) data sets, DICOM cannot distinguish between slices that are missing because they were not acquired (to reduce dose and acquisition time) and slices that got lost (due to file corruption, forgetting to copy some files, etc).</p>
<p>So, if you don’t expect such large gaps then go back to the imaging device or PACS and export the files again and make sure that you got them all. You may also double-check that the number of images (slices) shown on the PACS workstation is the same what you see in the DICOM browser in Slicer.</p>

---

## Post #10 by @ckbow (2021-09-21 13:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="19766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which one was that?</p>
</blockquote>
</aside>
<p>The file was able to work when I used the “Load Data” button instead of trying to import it to the DICOM database.</p>

---

## Post #11 by @pieper (2021-09-21 13:57 UTC)

<aside class="quote no-group" data-username="ckbow" data-post="10" data-topic="19766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/49beb7/48.png" class="avatar"> ckbow:</div>
<blockquote>
<p>I used the “Load Data” button instead of trying to import it to the DICOM database.</p>
</blockquote>
</aside>
<p>That’s generally a bad sign since the database approach handles a lot of important cases that Load Data does not.</p>

---
