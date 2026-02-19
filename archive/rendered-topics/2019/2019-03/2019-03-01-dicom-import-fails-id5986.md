---
topic_id: 5986
title: "Dicom Import Fails"
date: 2019-03-01
url: https://discourse.slicer.org/t/5986
---

# DICOM import fails

**Topic ID**: 5986
**Date**: 2019-03-01
**URL**: https://discourse.slicer.org/t/dicom-import-fails/5986

---

## Post #1 by @margherita (2019-03-01 09:52 UTC)

<p>Hallo<br>
we are using Slicer 4.8.1 and we hve the database with 15 patients that are segmented and analyzed.<br>
The problem that we are facing is that we are not able importing new patients  images.<br>
Despite we are following the same procedure, the result of DICOM import  is the message 0 new patient, 0 new studies,0 new series, 0 new instances<br>
Can you help us?</p>

---

## Post #2 by @pieper (2019-03-01 12:38 UTC)

<aside class="quote no-group quote-modified" data-username="margherita" data-post="3" data-topic="3501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/margherita/48/3182_2.png" class="avatar"><a href="https://discourse.slicer.org/t/import-nrrd-segmentation/3501/3">import nrrd segmentation</a></div>
<blockquote>
<p>0 new patient, 0 new studies,0 new series, 0 new instances</p>
</blockquote>
</aside>
<p>That message can either mean that the new data are not recognized as valid dicom or that the data already exists in the current database.  You could check this by creating a new database directory and importing the data there.</p>
<p>Use the “more” button on the top bar to expose the directory browser to pick where to store the database.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985.png" data-download-href="/uploads/short-url/uft67YjAV1FRNpu90CTO7iRY8a9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985_2_690x432.png" alt="image" data-base62-sha1="uft67YjAV1FRNpu90CTO7iRY8a9" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985.png 2x" data-dominant-color="E2E3EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1335×836 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @margherita (2019-03-01 13:31 UTC)

<p>we did it and it didn’t work<br>
we made also empy database and tried to upload again and it doesn’t work<br>
It created a file ctkDICOM.slq e ctkDICOMtagcache.sql  but the images are not visible</p>

---

## Post #4 by @pieper (2019-03-01 19:03 UTC)

<p>In that case it must be something about your dicom files.  Have a look at the suggestions in the FAQ and see if any of those help and let us know what you find.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser</a></p>

---
