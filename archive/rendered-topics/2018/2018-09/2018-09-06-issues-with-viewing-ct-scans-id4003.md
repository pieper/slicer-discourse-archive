# Issues with viewing CT scans

**Topic ID**: 4003
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/issues-with-viewing-ct-scans/4003

---

## Post #1 by @ReNeu (2018-09-06 15:06 UTC)

<p>Operating system: Microsoft<br>
Slicer version:4.8.0<br>
Expected behavior: Opening CT scans in Slicer<br>
Actual behavior: I have two problems with viewing axial CT scan.</p>
<ol>
<li>
<p>For some of my data When I open one image in the sequence file I can only see a thin strip of that axial slice (as if it’s one row of voxels out of the slice matrix of rows x columns).</p>
</li>
<li>
<p>In one file I have raw data where slice numbers (in the raw data) are not according to their anatomical order. When I rename slice number to follow their anatomical order I get problem number 1.</p>
</li>
</ol>
<p>Thanks for the help</p>
<p>Ettie</p>

---

## Post #2 by @pieper (2018-09-06 15:27 UTC)

<p>Hi -</p>
<p>If this is dicom data, see this FAQ:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>
<p>If they are other kinds of files, try unchecking the SingleFile option described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/LoadingData" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/LoadingData</a></p>
<p>If that doesn’t help, let us know the filenames and types you are using.</p>

---

## Post #4 by @ReNeu (2018-09-13 01:36 UTC)

<p>Hi Steve,</p>
<p>Thank you for your reply,</p>
<p>The CT scans are DICOM files and I have followed the instructions “Something is displayed, but it is not what I expected” from: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>
<p>but couldn’t solve the problem by adjusting the slice viewer’s field of view</p>
<p>Here is my problem in more detail:</p>
<p>The original file has DICOM file numbers (99113093 - 99113123) that are not in the same order as the anatomical slice number (1-31). For example:</p>
<p>DICOM 9113093	Anatomical slice number 25</p>
<p>DICOM 9113094	Anatomical slice number 19</p>
<p>DICOM 9113095	Anatomical slice number 6</p>
<p>DICOM 9113096	Anatomical slice number 22</p>
<p>DICOM 9113097	Anatomical slice number 10</p>
<p>etc.</p>
<p>Furthermore, the sequence contains a scouting type image (one for the DICOM files), which ideally will be removed before mapping the lesion.</p>
<p>When I view the original DICOM in slicer it shows the CT scan slices correctly but of course in incorrect order. This makes lesion mapping very difficult.</p>
<p>When I change the DICOM file number according to anatomical slice order (for example DICOM 9113095, Anatomical slice number 6, becomes DICOM 9113101), I see a narrow slice of the image (narrow on the Y axis) rather than the full image (the whole Y axis). I suspect that renaming interrupts something, but not sure what.</p>
<p>How can I view the DICOM files in their anatomical order (like any other subject) and see the whole image rather than just a strip?</p>
<p>Cheers,</p>
<p>Ettie</p>

---

## Post #5 by @lassoan (2018-09-13 04:39 UTC)

<aside class="quote no-group" data-username="ReNeu" data-post="4" data-topic="4003">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/e8c25b/48.png" class="avatar"> ReNeu:</div>
<blockquote>
<p>When I view the original DICOM in slicer it shows the CT scan slices correctly but of course in incorrect order</p>
</blockquote>
</aside>
<p>Slicer ignores file and folder names when loading DICOM files. Slices are ordered based on position information embedded in each file (in “image position patient” tag). If slices in Slicer appear in wrong order then most likely the DICOM files are written incorrectly.</p>
<p>Make sure you import data into Slicer’s DICOM browser and load it from the DICOM browser. Do <em>not</em> use “Add data dialog” for loading DICOM files, especially if you have DICOM files dispersed in multiple folders or the files have random names.</p>
<p>if you still have problems then the best is if you can share an anonymized data set (upload to a file sharing service and paste the link here).</p>

---

## Post #6 by @GingerHill (2021-06-16 18:06 UTC)

<p>I have the same problem. It started when I updated to most recent stable version of slicer.</p>

---
