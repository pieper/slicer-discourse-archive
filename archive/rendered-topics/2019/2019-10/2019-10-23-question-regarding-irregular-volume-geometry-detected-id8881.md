# Question regarding Irregular volume geometry detected

**Topic ID**: 8881
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/question-regarding-irregular-volume-geometry-detected/8881

---

## Post #1 by @cecilcharles (2019-10-23 17:23 UTC)

<p>Operating system:MAC 10.13.6<br>
Slicer version:4.10.2<br>
Expected behavior:source images and calculated images have correct image dimensions in the DICOM header but the calculated images show wrong in plane dimensions<br>
Actual behavior: 6.25 x 6.25 x 15 mm source images load correctly.  calculated images with correct info in the DICOM header load as 1 x 1 x 15 mm.</p>
<p>From the Python interactor:</p>
<pre><code>Imported a DICOM directory, checking for extensions

Imported a DICOM directory, checking for extensions

Imported a DICOM directory, checking for extensions

reg inside examine

Loading with imageIOName: GDCM

Window/level found in DICOM tags (center=162.5, width=315.0) has been applied to volume 122: washout_03_r1

Irregular volume geometry detected (maximum error of 336 mm is above tolerance threshold of 0.001 mm). Regularization transform is not added, as the option is disabled.

reg inside examine

Loading with imageIOName: GDCM

Window/level found in DICOM tags (center=21.0, width=58.0) has been applied to volume 101: MEANWI

Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 7.62939e-06 mm, tolerance threshold is 0.001 mm).</code></pre>

---

## Post #2 by @lassoan (2019-10-23 17:49 UTC)

<aside class="quote no-group" data-username="cecilcharles" data-post="1" data-topic="8881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/df788c/48.png" class="avatar"> cecilcharles:</div>
<blockquote>
<p>122: washout_03_r1</p>
</blockquote>
</aside>
<p>There is something wrong or unusual about volume <code>122: washout_03_r1</code>. Maybe slices are missing or there are extra slices. You can inspect the header using the DICOM browser’s “Metadata” and find what causing the issue by looking at values of “ImagePositionPatient” and “ImageOrientationPatient” fields.</p>
<p>Your other volume, <code>101: MEANWI</code> does not have any issue in its geometry (image slices are evenly spaced).</p>

---

## Post #3 by @cecilcharles (2019-10-23 18:14 UTC)

<p>The two sets of images are spatially identical.  The washout image is derived from fitting a model to a series of 3D volume images (the Mean image is derived from the set of source images).  There are not missing slices or extra slices, it is a 3D MRI dataset.<br>
How does the ‘irregular volume geometry work’ on a DICOM dataset?  I can provide deid’d images if that would help.</p>

---

## Post #4 by @lassoan (2019-10-23 18:20 UTC)

<p>Yes, if you can share anonymized images then we can tell what’s wrong with them.</p>

---

## Post #5 by @cecilcharles (2019-10-23 18:32 UTC)

<p>Andras,</p>
<p>I will create them.  I have some suspicion that this is some subtle UID issue rather than a geometry issue.  I will create a set with the source images as well as the processed images.</p>
<p>Thanks</p>
<p>Cecil</p>

---

## Post #6 by @cecilcharles (2019-10-23 19:27 UTC)

<p>Andras,</p>
<p>I passed the problem file through DICOM Cleaner to send to you and tested it for loading in a couple of programs.  It now loads correctly in Slicer so I suspect something weird.  I will do a little more testing but will send the two examples tomorrow.</p>
<p>Cecil</p>

---
