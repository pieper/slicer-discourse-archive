---
topic_id: 23959
title: "Horizontally Gantry Tilt"
date: 2022-06-20
url: https://discourse.slicer.org/t/23959
---

# Horizontally Gantry Tilt

**Topic ID**: 23959
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/horizontally-gantry-tilt/23959

---

## Post #1 by @Mahdiye_Imanpanah (2022-06-20 11:39 UTC)

<p>Hi everyone<br>
I’m a medical image processing specialist, and now I’m working on Dicom.<br>
I have a question about Tilt in Dicom, which is defined using the (0018, 1120) Dicoms tag.<br>
Based on my research, we have 3 types of tilts, Normal, Vertical, and Horizontal.<br>
1- Is there anybody to tell me what are the differences between these types?<br>
2- Why do the applications support the Vertical and Normal but they don’t support the horizontal?<br>
I will be so thankful if you answer my questions.</p>

---

## Post #2 by @lassoan (2022-06-20 13:28 UTC)

<aside class="quote no-group" data-username="Mahdiye_Imanpanah" data-post="1" data-topic="23959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mahdiye_imanpanah/48/15747_2.png" class="avatar"> Mahdiye_Imanpanah:</div>
<blockquote>
<p>Based on my research, we have 3 types of tilts, Normal, Vertical, and Horizontal.</p>
</blockquote>
</aside>
<p>These 3 types of tilts don’t sound familiar. Maybe it refers to “no tilt”, or rotation around horizontal axis and rotation around vertical axis. Rotation around horizontal axis it means towards the patient’s head or feet, this is what <a href="https://dicom.innolitics.com/ciods/pet-image/pet-series/00181120">(0018,1120)</a> DICOM standard can describes, and I have ever encountered in CT images. Rotation around vertical axis might be feasible, too, but would be harder to implement (there is not much space available to do that) and I don’t think it is commonly done (if at all).</p>
<p>Maybe gantry rotations that you have come across describe C-arm rotations (RAO/LAO, CRA/CAU), which are very different from Gantry tilt of a CT described by <a href="https://dicom.innolitics.com/ciods/pet-image/pet-series/00181120">(0018,1120)</a>.</p>

---

## Post #3 by @Mahdiye_Imanpanah (2022-06-20 14:15 UTC)

<p>Thanks for answering dear Andras<br>
I have seen these types in some applications,  you might be right and (0018, 1120) is not the same thing that I’m working on.<br>
My main problem is that I can’t get the MPR for some datasets, cause of this error: Does not support [horizontally gantry tilted images] as a source dataset for MPR.<br>
I can’t figure out why there is no problem with vertical and normal images, but for horizontal?<br>
In my point of view, the acquired images should be the same in the 3 directions, so what is the problem?<br>
Is my question clear?</p>

---

## Post #4 by @pieper (2022-06-20 18:17 UTC)

<aside class="quote no-group" data-username="Mahdiye_Imanpanah" data-post="3" data-topic="23959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mahdiye_imanpanah/48/15747_2.png" class="avatar"> Mahdiye_Imanpanah:</div>
<blockquote>
<p>this error: Does not support [horizontally gantry tilted images] as a source dataset for MPR.</p>
</blockquote>
</aside>
<p>That doesn’t sound like a Slicer error.  Where does it come from?</p>
<p>Slicer uses a more general method to account for gantry tilt (and other geometric issues like irregular slice spacing) so it doesn’t rely on the  tag you referenced.</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0" target="_blank" rel="noopener">ENH: model DICOM acquisition geometry (addresses #4409)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-10-20" data-time="12:57:03" data-timezone="UTC">12:57PM - 20 Oct 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="changed 2 files with 278 additions and 6 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0" target="_blank" rel="noopener">
          <span class="added">+278</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Add a step to the DICOMScalarVolumePlugin to check that the loaded
volume node's<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> slice geometry matches what is expected from
the position and orientation information of the individual
slices in the DICOM headers.

If needed, a grid transform is created to reposition each slice
to the appropriate position in patient space.

Use an empirically defined epsilon threshold to decide if
an acquisition transform is needed.  The selected value of
1e-3 millimeters (one micrometer) is still very small by
medical imaging standards but is large enough that rounding
errors and other small variations do not result in extra
correction transforms when they won't add real value.
The error is defined as the max absolute difference
in any coordinate of the corner of any slice so it
is designed to handle gantry tilt, missing slices,
and irregularly spaced slices.

The DICOMReaders self test has been extended to test this in the
case where slices are missing from the middle of the volume.  The
grid transform results in an interpolated band of pixels using
information from adjacent slices to 'fill in' for the missing
data.  The test confirms that the last slice of the reconstructed
volume is in the expected location in patient space.  This correction
means that calculations like ruler or segment statistics can be
robust even with missing slices.

Currently the only available testing data is for the case of missing
slices.  However this code should allow proper loading and display of
several not-uncommon imaging scenarios:

1) Missing slices due to network failure or accidental file deletion.

2) Gantry tilted image acquisitons (see #4409) which is
used, for example, to minimize radiation exposure to the retinas
especially in pediatric imaging.

3) Variable table speed during CT acquisition, which is sometimes
used in abdominal or musculoskeletal imaging to provide high resolution
in selected body parts and lower resolution between (e.g. high res
at the ankle, knee and hip, but low res in the shin and thigh).

Consderations:

By creating a transform we preserve the original data and leave it
to the user to resample if desired.  The option of resampling
during load was rejected since it is unclear what sampling grid
would be best in all cases.

Although the transform should correct the geometry, a warning dialog is
still generated during loading since the issue could be correctable
(such as missing slices) or may be triggered by other data issues
not forseen by this code.

Most DICOM data has identical row and column spacing
but when they do not it's critical to have the right
spacing geomtry.  This code uses the correct definitions
from the standard.  Where PixelSpacing is row/column
but ImageOrientationPatient if column/row

We check and avoid ValueError warning when dicom files do not have
geometry information.

svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26500
git-svn-id: http://svn.slicer.org/Slicer4/trunk@26500 3bd1e089-480b-0410-8dfb-8563597acbee</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Mahdiye_Imanpanah (2022-06-20 19:15 UTC)

<p>Thanks for answering dear Steve<br>
The link you’ve sent is really helpful.</p>

---

## Post #6 by @lassoan (2022-06-20 23:20 UTC)

<p>It seems that the message comes from <a href="https://documentation.clearcanvas.ca/Documentation/UsersGuide/Personal/13_1/index.html?mpr.htm">ClearCanvas</a>. The small illustration that they provide is very nice and clear:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bef3cbb4113099c70fcebc01088690e8cb127ca.png" alt="image" data-base62-sha1="mfszqaWqbwhRy0oK7ZlliOxHIro" width="384" height="163"></p>
<p>However, I don’t think this “horizontal tilt” technique is used in clinical imaging. It may be hard to implement because the gantry would collide with the table, it would need an extra rotation joint for the gantry, etc.</p>
<p>What ClearCanvas documentation calls “vertical tilt” is used for clinical imaging (I’ve seen mostly in brain imaging) and this is what (0018,1120) refers to as well:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0e95dbe332c02e553b86b55b8e0bfceace04913.png" alt="image" data-base62-sha1="w5EWa8VdHwIFrohUVs0ntx8ekJJ" width="384" height="163"></p>
<p>If you indeed use ClearCanvas then I would recommend to replace it with some more up-to-date software. If you host the DICOM server yourself then you can use DCM4CHE or Orthanc; if you are on the cloud then Google, Microsoft, etc. have their own hosted DICOM server implementations that you can rely on (and may save you some maintenance efforts). If you want to just have something simple then you may use <a href="https://github.com/dcmjs-org/dicomweb-server">DCM.js DICOMweb server</a> or <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#dicomweb-endpoints">Slicer’s built-in DICOMweb server</a>.</p>

---
