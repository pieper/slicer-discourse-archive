---
topic_id: 14381
title: "How To Fix Error Occured During Itk Connversion Error"
date: 2020-11-02
url: https://discourse.slicer.org/t/14381
---

# How to fix "Error occured during ITK connversion" Error

**Topic ID**: 14381
**Date**: 2020-11-02
**URL**: https://discourse.slicer.org/t/how-to-fix-error-occured-during-itk-connversion-error/14381

---

## Post #1 by @gipson04 (2020-11-02 12:52 UTC)

<p>Hi</p>
<p>I tend to compare contours from 2 Rt structure files from pinnacle using Segment comparison tool. When i loaded the the files and computed similarity matrix i got a error stating ‘Error occurred during ITK connversion’. How to fix it. Am i doing something stupid? Any help?</p>

---

## Post #2 by @cpinter (2020-11-02 13:33 UTC)

<p>Can you please show us the log? There must be another error that tells us why conversion failed.</p>

---

## Post #3 by @marianaslicer (2020-12-01 15:53 UTC)

<p>Hi everyone.</p>
<p>I am getting the same error. The log message is the following:</p>
<blockquote>
<p>GetBinaryLabelmapRepresentation: No binary labelmap representation in segment</p>
<p>GetInputSegmentsAsPlmVolumes: Failed to get binary labelmap from reference segment: CTV1 30 4D</p>
<p>ComputeHausdorffDistances: Error occurred during ITK conversion</p>
</blockquote>
<p>I would appreciate some help. Thank you!</p>

---

## Post #4 by @Olivio_Donati (2020-12-30 08:05 UTC)

<p>Hi Did you find a solution yet? I get the exact same error.</p>

---

## Post #5 by @Costea_Madalina (2021-01-06 09:33 UTC)

<p>Following…I get the same error as well …</p>

---

## Post #6 by @stevn_dk (2021-01-06 12:47 UTC)

<p>I get the same error as well …</p>

---

## Post #7 by @lassoan (2021-01-06 15:34 UTC)

<p>Segment comparison requires labelmap representation. You can create this labelmap representation in Segmentations module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1987f2177fa7a2953516fd83f030bcb0c999a38.png" data-download-href="/uploads/short-url/n3xATZk7puIzlCFC7kWuljh6rNK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1987f2177fa7a2953516fd83f030bcb0c999a38_2_534x500.png" alt="image" data-base62-sha1="n3xATZk7puIzlCFC7kWuljh6rNK" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1987f2177fa7a2953516fd83f030bcb0c999a38_2_534x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1987f2177fa7a2953516fd83f030bcb0c999a38_2_801x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1987f2177fa7a2953516fd83f030bcb0c999a38_2_1068x1000.png 2x" data-dominant-color="3B3B3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1170×1095 57.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve submitted an issue to SlicerRT that the behavior should be more intuitive:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/SlicerRT/issues/170">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/issues/170" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/170" target="_blank" rel="noopener">"Error occurred during ITK conversion" in Segment comparison module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-01-06" data-time="15:32:39" data-timezone="UTC">03:32PM - 06 Jan 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-04-12" data-time="13:57:09" data-timezone="UTC">01:57PM - 12 Apr 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Segment comparison module seems to rely on labelmap representation. Normally the<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> segmentation is read from RTSTRUCT and so does not contain labelmap representation.

When somebody wants to compare segments, Segment comparison module simply displays a message "Error occurred during ITK conversion".

The module should probably compute labelmap representation automatically (but at least print a more meaningful error message).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
