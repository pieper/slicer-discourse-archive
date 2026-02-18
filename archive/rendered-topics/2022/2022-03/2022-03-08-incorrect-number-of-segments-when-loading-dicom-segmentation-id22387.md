# Incorrect number of segments when loading DICOM segmentation file

**Topic ID**: 22387
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/incorrect-number-of-segments-when-loading-dicom-segmentation-file/22387

---

## Post #1 by @DeepaKrishnaswamy (2022-03-08 22:11 UTC)

<p>Hi,</p>
<p>I created and saved a DICOM segmentation file:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e731b22c3dc4add64d041c84cf4bb2ddf9a00d25.jpeg" alt="create_segments" data-base62-sha1="wZeLFp9LzRJnpGUxoGrltcTXnZH" width="610" height="208"></p>
<p>I checked the logs, and it seems to have exported successfully. However, when I load this file, it seems that the number of regions is doubled:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02e8efbb5bf3f730713ced13b64a3b4b2166f245.jpeg" alt="load_seg_dicom_error" data-base62-sha1="pK1aZBEzG8ePlKtfMMWDVJu3fn" width="617" height="260"></p>
<p>Checking the logs, I see the following errors:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fa538f992a5860a554a8f44c619f4ed4e902abf.jpeg" data-download-href="/uploads/short-url/9524eGwNi3wDU3gXyv5mCIoeKRx.jpeg?dl=1" title="load_log_error_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fa538f992a5860a554a8f44c619f4ed4e902abf_2_690x86.jpeg" alt="load_log_error_1" data-base62-sha1="9524eGwNi3wDU3gXyv5mCIoeKRx" width="690" height="86" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fa538f992a5860a554a8f44c619f4ed4e902abf_2_690x86.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fa538f992a5860a554a8f44c619f4ed4e902abf.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fa538f992a5860a554a8f44c619f4ed4e902abf.jpeg 2x" data-dominant-color="E9E9E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">load_log_error_1</span><span class="informations">743×93 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc11c40d3918534d884fe51a908e83b2e9cc0400.jpeg" data-download-href="/uploads/short-url/zXUnUtVonfha8vwb77UKN51RcfC.jpeg?dl=1" title="load_log_error_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc11c40d3918534d884fe51a908e83b2e9cc0400_2_690x34.jpeg" alt="load_log_error_2" data-base62-sha1="zXUnUtVonfha8vwb77UKN51RcfC" width="690" height="34" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc11c40d3918534d884fe51a908e83b2e9cc0400_2_690x34.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc11c40d3918534d884fe51a908e83b2e9cc0400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc11c40d3918534d884fe51a908e83b2e9cc0400.jpeg 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">load_log_error_2</span><span class="informations">744×37 5.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m unsure of how to debug this, thanks!</p>
<p>Deepa</p>

---

## Post #2 by @lassoan (2022-03-09 06:31 UTC)

<p>I could not reproduce this issue with the latest Slicer Preview Release? Could you please check if that version works well for you, too?</p>

---

## Post #3 by @DeepaKrishnaswamy (2022-03-09 18:13 UTC)

<p>Previously I was using Slicer 4.13.0-2022-01-26, but the same issue occurs when switching to the latest Slicer preview release. It seems to happen when multiple segments are present. With a single segment, the DICOM SEG file seems to load successfully – but when I check the logs, the same warnings/errors are present (as above) concerning the AnatomicContext.</p>

---

## Post #4 by @fedorov (2022-03-09 21:13 UTC)

<p>I was able to reproduce the issue. Here’s the sample dataset (I am not sure if the slice location mismatch pointed to by the second red arros is an issue or not, since I did not create the sample - that might be a “red herring”): <a href="https://www.dropbox.com/s/d3pyl6moin4giq8/prostate_repeatability_mpReview_Andrey.zip?dl=0" class="inline-onebox">Dropbox - prostate_repeatability_mpReview_Andrey.zip - Simplify your life</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f327f871b50d0b0e2fcded14d5b92bcc7c31fd.jpeg" data-download-href="/uploads/short-url/jGmn84qAuqoZBkfLrCOswmCrKep.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89f327f871b50d0b0e2fcded14d5b92bcc7c31fd_2_647x500.jpeg" alt="image" data-base62-sha1="jGmn84qAuqoZBkfLrCOswmCrKep" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89f327f871b50d0b0e2fcded14d5b92bcc7c31fd_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f327f871b50d0b0e2fcded14d5b92bcc7c31fd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f327f871b50d0b0e2fcded14d5b92bcc7c31fd.jpeg 2x" data-dominant-color="A09FA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">955×738 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-03-10 01:07 UTC)

<p>I’ve submitted a pull request with the fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/QIICR/QuantitativeReporting/pull/264">
  <header class="source">

      <a href="https://github.com/QIICR/QuantitativeReporting/pull/264" target="_blank" rel="noopener">github.com/QIICR/QuantitativeReporting</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/QuantitativeReporting/pull/264" target="_blank" rel="noopener">BUG: Fix duplicate segments appearing when importing single-slice segmentations</a>
    </h4>

    <div class="branches">
      <code>QIICR:master</code> ← <code>lassoan:fix-duplicate-segment-loading</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-03-10" data-time="01:05:30" data-timezone="UTC">01:05AM - 10 Mar 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 6 additions and 1 deletions">
        <a href="https://github.com/QIICR/QuantitativeReporting/pull/264/files" target="_blank" rel="noopener">
          <span class="added">+6</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Single-slice segmentations were loaded as an image stack (from files 1.nrrd, 2.n<span class="show-more-container"><a href="https://github.com/QIICR/QuantitativeReporting/pull/264" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rrd, ...), therefore each volume contained every label.
Fixed by enforcing loading each nrrd file as a single file.

Fixes the problem described at https://discourse.slicer.org/t/incorrect-number-of-segments-when-loading-dicom-segmentation-file/22387</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The problem was that the ITK interpreted the single-slice images as an image volume by default. Fixed by forcing loading each segment labelmap with single-file option.</p>

---
