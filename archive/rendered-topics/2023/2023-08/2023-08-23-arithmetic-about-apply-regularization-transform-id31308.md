# Arithmetic about apply regularization transform

**Topic ID**: 31308
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/arithmetic-about-apply-regularization-transform/31308

---

## Post #1 by @slicer365 (2023-08-23 07:07 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cabe9190b58ef9526bf16ac7412ca5c83d99cbc3.png" alt="image" data-base62-sha1="sVyJU6YU0EkwYvYIpValbFILT23" width="658" height="66"><br>
I am developing an independent software for my clients.</p>
<p>I need this function to correct the data.</p>
<p>The tilt value can be found in Tag,</p>
<p>but how to make changes to the data,</p>
<p>I searched the source code,</p>
<p>but I can’t find the implementation entry for this.</p>
<p>Can anyone help me? Thank you !</p>

---

## Post #2 by @jcfr (2023-08-23 12:36 UTC)

<blockquote>
<p>I searched the source code,</p>
</blockquote>
<p>If you search for the words <code>Regularization</code> and <code>regularization</code>,  you should be able to identify the relevant files.</p>
<p>Let us know if you sill have issues.</p>

---

## Post #3 by @slicer365 (2023-08-23 13:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edf81c4eb0b50d57797d851f5e13895bf6be121f.png" data-download-href="/uploads/short-url/xXaJz9X058ut9Z9KhRPfgGABlH9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edf81c4eb0b50d57797d851f5e13895bf6be121f.png" alt="image" data-base62-sha1="xXaJz9X058ut9Z9KhRPfgGABlH9" width="690" height="265" data-dominant-color="272829"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1225×471 19.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here is the result ,it seems that there is no  what I want.</p>

---

## Post #4 by @pieper (2023-08-23 13:54 UTC)

<p>The description and the corresponding source code are here:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">
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

## Post #5 by @slicer365 (2023-08-23 14:23 UTC)

<p>Thank you very much ! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @jcfr (2023-08-23 15:22 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="31308">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>If you search for the words <code>Regularization</code> and <code>regularization</code>, you should be able to identify the relevant files.</p>
</blockquote>
</aside>
<p>To complete my previous answer, doing a case-insensitive search returns the following:</p>
<pre><code class="lang-auto">$ rg -i regularization

[...]

Docs/user_guide/modules/dicom.md
186:        - Acquisition geometry regularization option supports the creation of a nonlinear transform that corrects for things like missing slices or gantry tilt in the acquisition.  See more information [here](https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0)
243:Scanners may create image volumes with varying image slice spacing. Slicer can represent such images in the scene by apply a non-linear transform. To enable this feature, go to menu: Edit / Application settings / DICOM and set *Acquisition geometry regularization* to *apply regularization transform*. Slice view, segmentation, and many other features work directly on non-linearly transformed volumes. For some other features, such as volume rendering, you need to harden the transform on the volume: go to Data module, in the row of the volume node, right-click on the transform column, and choose *Harden transform*.

Modules/Scripted/DICOMLib/DICOMUtils.py
665:    # Get acquisition geometry regularization setting value
667:    acquisitionGeometryRegularizationEnabled = (settings.value("DICOM/ScalarVolume/AcquisitionGeometryRegularization", "default") != "none")
688:                if acquisitionGeometryRegularizationEnabled:
691:                    warningText += ("  If loaded image appears distorted, enable 'Acquisition geometry regularization'"

Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py
88:                                          " If no regularization is applied then image may appear distorted if it was acquired with irregular geometry.")
90:        importFormatsComboBox.addItem(_("default (apply regularization transform)"), "default")
92:        importFormatsComboBox.addItem(_("apply regularization transform"), "transform")
96:        formLayout.addRow(_("Acquisition geometry regularization:"), importFormatsComboBox)
98:            "DICOM/ScalarVolume/AcquisitionGeometryRegularization", importFormatsComboBox,
137:    def acquisitionGeometryRegularizationEnabled(self):
139:        return (settings.value("DICOM/ScalarVolume/AcquisitionGeometryRegularization", "default") != "none")
542:                                                                addAcquisitionTransformIfNeeded=self.acquisitionGeometryRegularizationEnabled())
850:                    logging.warning(warningText + "  Regularization transform is not added, as the option is disabled.")

[...]
</code></pre>

---
