---
topic_id: 29701
title: "Threshold Function Not Working"
date: 2023-05-29
url: https://discourse.slicer.org/t/29701
---

# Threshold function not working

**Topic ID**: 29701
**Date**: 2023-05-29
**URL**: https://discourse.slicer.org/t/threshold-function-not-working/29701

---

## Post #1 by @umair04 (2023-05-29 00:59 UTC)

<p>I am trying to threshold different DICOM files to create segmentations, but some of the DICOM files are not working properly.</p>
<p>File working properly:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fc46a5b7e7e8472387b955ff07fcde4b1136bcb.png" data-download-href="/uploads/short-url/bnExnoCkb3KEZYVx20C8d3yDffB.png?dl=1" title="Screenshot 2023-05-28 at 4.37.50 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc46a5b7e7e8472387b955ff07fcde4b1136bcb_2_690x431.png" alt="Screenshot 2023-05-28 at 4.37.50 PM" data-base62-sha1="bnExnoCkb3KEZYVx20C8d3yDffB" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc46a5b7e7e8472387b955ff07fcde4b1136bcb_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc46a5b7e7e8472387b955ff07fcde4b1136bcb_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc46a5b7e7e8472387b955ff07fcde4b1136bcb_2_1380x862.png 2x" data-dominant-color="66666D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-28 at 4.37.50 PM</span><span class="informations">3024×1890 421 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>File not working properly:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71254de9adb0ec3ea6c73755d83e88d6eab7ddfd.png" data-download-href="/uploads/short-url/g8VSsoG5HBZ3JOcDFaxQch9ALkp.png?dl=1" title="Screenshot 2023-05-28 at 4.39.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71254de9adb0ec3ea6c73755d83e88d6eab7ddfd_2_690x431.png" alt="Screenshot 2023-05-28 at 4.39.15 PM" data-base62-sha1="g8VSsoG5HBZ3JOcDFaxQch9ALkp" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71254de9adb0ec3ea6c73755d83e88d6eab7ddfd_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71254de9adb0ec3ea6c73755d83e88d6eab7ddfd_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71254de9adb0ec3ea6c73755d83e88d6eab7ddfd_2_1380x862.png 2x" data-dominant-color="65656C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-28 at 4.39.15 PM</span><span class="informations">3024×1890 435 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have numerous files that fall into either of the categories above: the image is fully highlighted during the thresholding process and creating a segmentation successfully, or it is only highlighting the edges and not creating a segmentation. How can I fix the second category to create segmentations?</p>

---

## Post #2 by @muratmaga (2023-05-29 01:04 UTC)

<p>Might be related to the extremely high (128K) max intensity value in your second datasets. Most DICOM datasets are 16 bit and goes up to 65K. You may want to rescale your intensity ranges for this dataset (using simple filters) and try anew.</p>

---

## Post #3 by @umair04 (2023-05-29 01:27 UTC)

<p>That worked, thanks!</p>

---

## Post #4 by @lassoan (2023-05-29 02:09 UTC)

<p>FYI, this issue is fixed in recent Slicer Preview Releases:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/ef3d86b3b9053f4fa53e8e4a6ab9ab42db14f88b">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/ef3d86b3b9053f4fa53e8e4a6ab9ab42db14f88b" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/ef3d86b3b9053f4fa53e8e4a6ab9ab42db14f88b" target="_blank" rel="noopener">BUG: Ensure that the min/max values can be reached in ctkDoubleSlider and ctkDoubleRangeSlider</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-03-11" data-time="02:28:38" data-timezone="UTC">02:28AM - 11 Mar 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 5 files with 113 additions and 33 deletions">
        <a href="https://github.com/commontk/CTK/commit/ef3d86b3b9053f4fa53e8e4a6ab9ab42db14f88b" target="_blank" rel="noopener">
          <span class="added">+113</span>
          <span class="removed">-33</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The minimum and maximum values were not always reachable in ctkDoubleSlider and <span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/ef3d86b3b9053f4fa53e8e4a6ab9ab42db14f88b" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ctkDoubleRangeSlider widgets when moved the slider to the minimum or maximum position.

For example:

```
lo = -1024
hi = 2000
step = (hi - lo) / 1000.

thresholdSlider = ctk.ctkRangeWidget()
thresholdSlider.spinBoxAlignment = qt.Qt.AlignTop
thresholdSlider.setRange(lo, hi)
thresholdSlider.singleStep = step
thresholdSlider.show()
# Impossible to reach 2000.0

slider = ctk.ctkDoubleSlider()
slider.minimum = lo
slider.maximum = hi
slider.singleStep = step
slider.show()
slider.connect("valueChanged(double)", lambda v: print(v))
# Impossible to reach 2000.0
```

The problem was that the integer slider range was determined by rounding, which could result in the integer slider range not covering the entire value range.
Fixed the problem by extending the integer slider range when it did not fully cover the value range.

Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
