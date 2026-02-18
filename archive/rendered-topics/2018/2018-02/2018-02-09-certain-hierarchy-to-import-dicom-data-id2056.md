# Certain hierarchy to import DICOM data?

**Topic ID**: 2056
**Date**: 2018-02-09
**URL**: https://discourse.slicer.org/t/certain-hierarchy-to-import-dicom-data/2056

---

## Post #1 by @Joe (2018-02-09 14:59 UTC)

<p>I am new to 3DSlicer so please bear with me if my qustion seems stupid to you.</p>
<p>I got some files from a doctor who uses a program called Medigration and I can not import them correctly into 3DSlicer. I get this error every time:</p>
<p>"Warning in DICOM plugin Scalar Volume when examining loadable 608: sag weich: One or more images is missing geometry information.</p>
<p>Warning in DICOM plugin Scalar Volume when examining loadable 607: cor weich: One or more images is missing geometry information.</p>
<p>Warning in DICOM plugin Scalar Volume when examining loadable 606: tra weich: One or more images is missing geometry information.</p>
<p>Warning in DICOM plugin Scalar Volume when examining loadable 605: VRT: Reference image in series does not contain geometry information.  Please use caution.  "</p>
<p>Do you know what there is to be done to make it work?<br>
Do I need to rearrange the files into a certain hierarchy so they can be imported?</p>
<p>You would make me really happy if you would answer me!</p>

---

## Post #2 by @cpinter (2018-02-09 15:15 UTC)

<p>What Slicer version do you use?<br>
What modality is your image? (CT, MRI, etc)</p>
<p>Thanks!</p>

---

## Post #3 by @Joe (2018-02-09 15:23 UTC)

<p>I use 4.8 but tried 4.5 as well.</p>
<p>The modality is MRI.</p>

---

## Post #4 by @cpinter (2018-02-09 15:46 UTC)

<p>Can you please try the <a href="http://download.slicer.org/">latest nightly</a>? There have been fixes lately around loading DICOM image with missing slices.</p>
<p>If the nightly cannot load your image either, can you please send us the whole log? You can find it in Help / Report a bug</p>

---

## Post #5 by @lassoan (2018-02-09 16:21 UTC)

<p>There are 3 DICOM readers available in Slicer-4.8.1. Could you please try if your data set can be loaded with one of them? In the menu select Edit / Application settings / DICOM / DICOMScalarVolumePlugin / DICOM reader approach, and try GDCM, DCMT, and Archetype.</p>
<p>If loading fails with all three readers then probably there is something wrong with your data. To assist you with diagnosing the issue, please send us what values you have in ImageType, ImagePositionPatient, and ImageOrientationPatient DICOM tags - see instructions here: <a href="https://discourse.slicer.org/t/problem-with-sagittal-and-coronal-view-from-ccta-dicom-files/716/13?u=lassoan">Problem with sagittal and coronal view from CCTA DICOM files</a></p>

---

## Post #6 by @Joe (2018-02-09 17:31 UTC)

<p>I tried 4.9 and the other DICOM reader. Unfortunately it doesn’t work neither.</p>
<p>I think there is an other problem. I made some pictures that could show my problem a bit better:</p>
<ol>
<li>
<p><a href="https://imgur.com/rb6AFJE" rel="nofollow noopener">https://imgur.com/rb6AFJE</a> - Here you can see the hierarchy of the files. In each of these folders are the files for every Slice</p>
</li>
<li>
<p><a href="https://imgur.com/CqhUDpb" rel="nofollow noopener">https://imgur.com/CqhUDpb</a> - Here you can see the files for one slice</p>
</li>
</ol>
<p>I tried to import them with “import data” and I got no Errors.</p>
<ol start="3">
<li>
<p><a href="https://imgur.com/nMvVepy" rel="nofollow noopener">https://imgur.com/nMvVepy</a> - Here you can see that every image is loadad seperatly</p>
</li>
<li>
<p><a href="https://imgur.com/cg1PqTL" rel="nofollow noopener">https://imgur.com/cg1PqTL</a><br>
<a href="https://imgur.com/CsvFYwZ" rel="nofollow noopener">https://imgur.com/CsvFYwZ</a><br>
<a href="https://imgur.com/rOWwKrB" rel="nofollow noopener">https://imgur.com/rOWwKrB</a><br>
<a href="https://imgur.com/yNov4Ip" rel="nofollow noopener">https://imgur.com/yNov4Ip</a></p>
<p>Here are some loadad images</p>
</li>
</ol>
<p>So I can not scroll through the slices as I have to load every image manually.</p>

---

## Post #7 by @lassoan (2018-02-09 19:47 UTC)

<aside class="quote no-group" data-username="Joe" data-post="6" data-topic="2056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9e5f3/48.png" class="avatar"> Joe:</div>
<blockquote>
<p>I tried to import them with “import data” and I got no Errors.</p>
</blockquote>
</aside>
<p>This means that the problem is with DICOM fields that define image geometry (voxel spacing, position, directions).</p>
<p>Use DICOM module for importing and loading data (import the top-level folder, Slicer will go through all the the fiels in all subfolders).Try if your data set can be loaded with one of the 3 readers. In the menu select Edit / Application settings / DICOM / DICOMScalarVolumePlugin / DICOM reader approach, and try GDCM, DCMT, and Archetype.</p>
<p>If loading fails with all three readers then probably there is something wrong with your data. To assist you with diagnosing the issue, please send us what values you have in ImageType, ImagePositionPatient, and ImageOrientationPatient DICOM tags - see instructions here: Problem with sagittal and coronal view from CCTA DICOM files</p>

---

## Post #8 by @MSilent (2018-02-22 22:22 UTC)

<p>Can you let me know where to find those values of mageType, ImagePositionPatient, and ImageOrientationPatient DICOM tags</p>

---
