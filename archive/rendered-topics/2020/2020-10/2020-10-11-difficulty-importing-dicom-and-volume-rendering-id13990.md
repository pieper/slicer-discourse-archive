---
topic_id: 13990
title: "Difficulty Importing Dicom And Volume Rendering"
date: 2020-10-11
url: https://discourse.slicer.org/t/13990
---

# difficulty importing DICOM and volume rendering

**Topic ID**: 13990
**Date**: 2020-10-11
**URL**: https://discourse.slicer.org/t/difficulty-importing-dicom-and-volume-rendering/13990

---

## Post #1 by @Sz368 (2020-10-11 18:51 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: when i drag and drop the DICOM provided in the troubleshoot page  (QIN-HEADNECK-01-0024-CT) or my own DICOM volume render might work<br>
Actual behavior:<br>
I only see lines in the green and yellow boxes, normal axial images in red. No volume render unfortunately</p>
<p>many thanks for any help</p>

---

## Post #2 by @manjula (2020-10-11 19:19 UTC)

<p>You need to enable volume rendering from the volume rendering module !</p>

---

## Post #3 by @lassoan (2020-10-11 19:19 UTC)

<p>It sounds like you load a single slice only. Use the DICOM module to load all DICOM images properly:</p>
<ul>
<li>Switch to DICOM module</li>
<li>Drag-and-drop the DICOM folder to the application screen and wait for import to complete</li>
<li>Double-click on a patient, study, or series to load it into the scene</li>
</ul>
<p>The easiest way to load images from TCIA is to use  “TCIA Browser” module (provided by TCIABrowser extension): it allows you to browse the entire TCIA collection, select patients/studies/series, and download them into the Slicer DICOM database and optionally load them directly into the scene:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd195373c7a2e5789291513daa8490cc5fa63d5.png" data-download-href="/uploads/short-url/2fWbRkC35ZRwXqYFC0qWe9mBGHH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd195373c7a2e5789291513daa8490cc5fa63d5_2_690x439.png" alt="image" data-base62-sha1="2fWbRkC35ZRwXqYFC0qWe9mBGHH" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd195373c7a2e5789291513daa8490cc5fa63d5_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd195373c7a2e5789291513daa8490cc5fa63d5_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd195373c7a2e5789291513daa8490cc5fa63d5_2_1380x878.png 2x" data-dominant-color="343434"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1436 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can active volume rendering by two clicks in Data module: right-click on the eye icon and choose “Show in 3D views as volume rendering”. You can tune volume rendering settings in “Volume rendering” module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c86eb3eab14b2ca58d9e684a8abe94a4e193e4b.jpeg" data-download-href="/uploads/short-url/44mqLcZVmkLvrzTpdvbsjWcoNoT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c86eb3eab14b2ca58d9e684a8abe94a4e193e4b_2_690x420.jpeg" alt="image" data-base62-sha1="44mqLcZVmkLvrzTpdvbsjWcoNoT" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c86eb3eab14b2ca58d9e684a8abe94a4e193e4b_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c86eb3eab14b2ca58d9e684a8abe94a4e193e4b_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c86eb3eab14b2ca58d9e684a8abe94a4e193e4b_2_1380x840.jpeg 2x" data-dominant-color="3E3E42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 663 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Sz368 (2020-10-12 13:24 UTC)

<p>thank you Andras for taking the time to help,<br>
I’ll try these suggestions of yours<br>
many thanks<br>
Susan</p>

---

## Post #5 by @Sz368 (2020-10-12 13:28 UTC)

<p>thanks Manjula for taking the time to help me,<br>
the volume render/ open eyes work on the sample data it’s just getting my own DICOMS to load which is my troubled step at the moment. I might try this TCIA browser too and see if this helps<br>
thanks again<br>
Susan</p>

---
