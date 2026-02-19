---
topic_id: 19001
title: "Understanding Ct Image Spacing And Acquisition Geometry Regu"
date: 2021-07-31
url: https://discourse.slicer.org/t/19001
---

# Understanding CT Image spacing and Acquisition geometry regularization

**Topic ID**: 19001
**Date**: 2021-07-31
**URL**: https://discourse.slicer.org/t/understanding-ct-image-spacing-and-acquisition-geometry-regularization/19001

---

## Post #1 by @manjula (2021-07-31 17:13 UTC)

<p>Dear all,</p>
<p>"Images are not equally spaced (a difference of 0.6 vs 0.3 was detected)’</p>
<p>Why does this error occur? What causes the acquisition of acquired irregular geometry? is it something to do with CT machine, protocol, technique or just a problem with exporting the data?</p>
<p>with Acquisition geometry regularization correction transform applied,  I tried to harden the transformation and I expected the corrected version of the image to persist but it changed to the original? is this the expected behavior?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d32528e6a5b3977d17b05b89f74bd840eb53be7.png" data-download-href="/uploads/short-url/k958BoJMk4zeuAcIXQ4ukwpz8yj.png?dl=1" title="Screenshot_20210731_222649" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d32528e6a5b3977d17b05b89f74bd840eb53be7_2_690x183.png" alt="Screenshot_20210731_222649" data-base62-sha1="k958BoJMk4zeuAcIXQ4ukwpz8yj" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d32528e6a5b3977d17b05b89f74bd840eb53be7_2_690x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d32528e6a5b3977d17b05b89f74bd840eb53be7_2_1035x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d32528e6a5b3977d17b05b89f74bd840eb53be7_2_1380x366.png 2x" data-dominant-color="ABABCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20210731_222649</span><span class="informations">1589×423 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>what does this mean and is there a difference that is too much to be corrected or too little to be ignored ?  (a difference of 0.6 vs 0.3 was detected) ?</p>
<p>thank you</p>

---

## Post #2 by @pieper (2021-07-31 18:08 UTC)

<p>Hi <a class="mention" href="/u/manjula">@manjula</a> -</p>
<p>There’s a description of the purpose and implementation technique in the git commit message linked below (small aside: it still makes me smile that Andras said he wished he’d thought of this : )</p>
<p>In your case it looks like the third cited motivation:</p>
<pre><code class="lang-auto">3) Variable table speed during CT acquisition, which is sometimes
used in abdominal or musculoskeletal imaging to provide high resolution
in selected body parts and lower resolution between (e.g. high res
at the ankle, knee and hip, but low res in the shin and thigh).
</code></pre>
<p>They often to this to speed up the exam, minimize radiation exposure, avoid a bunch of extra useless slices, and extend the life of the x-ray tube.</p>
<p>The volume shouldn’t move at all when you harden the transform, but maybe the RAS box is fit to the data differently.  Please confirm this and we can investigate.  The acquisition geometry regularization correction transform is not applied automatically so that you have an option to use a resampling tool to pick the desired resolution.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
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

## Post #3 by @manjula (2021-07-31 18:44 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thank you for the reply and I will go through it.</p>
<p>This is what happens after loading this data and when I try to transform. Both in the stable and the preview release that I use (2021.06.24). I don’t know it is an error or not but I recorded a clip so you can see if it does what it intends to do or not.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="wshQXzH-5Ks" data-video-title="transform" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wshQXzH-5Ks" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wshQXzH-5Ks/maxresdefault.jpg" title="transform" width="" height="">
  </a>
</div>


---

## Post #4 by @pieper (2021-07-31 20:01 UTC)

<p>This is probably correct because the volume rendering doesn’t take non-linear transforms like the acquisition correction into account.  You can confirm this by making the slice views visible in the 3D view and they won’t match until you harden.  It needs to be fixed at the VTK level, and we’ve discussed it but it hasn’t been done yet as far as I know.  The volume rendering module should really generate a visible warning or error dialog when a volume with a nonlinear transform is selected.</p>
<p>In any case, it appears that things are working correctly elsewhere and things like rulers and other markups will work.  You might do a few measurements as a sanity check.</p>

---

## Post #6 by @lassoan (2021-08-02 00:51 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="19001">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The volume rendering module should really generate a visible warning or error dialog when a volume with a nonlinear transform is selected</p>
</blockquote>
</aside>
<p>The related issue is here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4701">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4701" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4701" target="_blank" rel="noopener">Non-linear transform is ignored by volume renderer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:05:21" data-timezone="UTC">01:05AM - 13 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-11-15" data-time="04:36:38" data-timezone="UTC">04:36AM - 15 Nov 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Medium
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=4701). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Davide_Punzo (2023-11-13 08:37 UTC)

<p>NOTE: Support for regularization transform hardening in DICOM Scalar plugin has been added. See <a href="https://discourse.slicer.org/t/enh-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">link</a>.</p>

---
