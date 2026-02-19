---
topic_id: 31793
title: "Segmentation Editor Painting Raises Vtk Error No Input Data"
date: 2023-09-19
url: https://discourse.slicer.org/t/31793
---

# Segmentation Editor: Painting raises VTK error: no input data

**Topic ID**: 31793
**Date**: 2023-09-19
**URL**: https://discourse.slicer.org/t/segmentation-editor-painting-raises-vtk-error-no-input-data/31793

---

## Post #1 by @gortm (2023-09-19 16:14 UTC)

<p>Dear community,</p>
<p>First I’d like to mention that I’m new to slicer and probably I’m making a very obvious mistake.</p>
<p>While trying to segment ct data captured on a Skyscan 1176, I ran into the issue that I could not use the painting function. I followed the tutorial <em>Whole heart segmentation from cardiac CT in 10 minutes</em> but when painting into the viewport I receive this error message in the python console: <em>[VTK] No input data</em>. The model looks fine in the viewport.</p>
<p>I imported the data using the slicermorph extension, which is why I also tagged it. Maybe I did something wrong there.</p>
<p>Any suggestions as to why I cannot use the painting function in the segmentation editor?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @muratmaga (2023-09-19 16:49 UTC)

<p>How are you importing the 1176 data into Slicer?</p>
<p>If the data are read as vector (RGB) then SegmentEditor won’t work.</p>
<p>In SlicerMorph there is a <code>SkyscanReconImport</code> module that simplifies the procedure, though it is not ideal to use if your data is too large or you want to downsample as you import etc. If that’s the case, use the <code>ImageStacks</code> module in SlicerMorph. Both of them will bring the data ready to be used in SegmentEditor.</p>

---

## Post #3 by @pieper (2023-09-19 19:39 UTC)

<p>You are probably seeing this issue:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7212">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7212" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7212" target="_blank" rel="noopener">BUG: Fix "No input data" message in Segment Editor paint effect</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-segment-editor-paint-no-input-data-message</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-02" data-time="11:32:35" data-timezone="UTC">11:32AM - 02 Sep 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 11 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7212/files" target="_blank" rel="noopener">
            <span class="added">+11</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">If there is no input or if the input has no points, the vtkTransformPolyDataFilt<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7212" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er will display an error message on every update: "No input data", polluting the log and slowing down the application. To prevent logging the error, an error callback command is set that discards the message.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It should be harmless, but it’s being fixed to clear up the log.  If painting actually isn’t working it’s some other issue.</p>

---

## Post #4 by @gortm (2023-09-19 20:00 UTC)

<p>Thank you very much for your reply <a class="mention" href="/u/muratmaga">@muratmaga</a>!</p>
<p>Indeed I used Imagestack to import the files (tiff). SkyscanReconImport didn’t work because I was missing one image which I will get tomorrow. Otherwise I will have to adjust the log file which I would prefer not to.<br>
I will check if I accidentally imported it as RGB (I don’t know where the setting is).</p>

---

## Post #5 by @gortm (2023-09-19 20:13 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> for pointing out this bug.<br>
Looks like it’s exactly that. But what can I do about it? Should it still draw something? It doesn’t draw anything in my case.</p>

---

## Post #6 by @muratmaga (2023-09-19 20:24 UTC)

<aside class="quote no-group" data-username="gortm" data-post="4" data-topic="31793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/848f3c/48.png" class="avatar"> gortm:</div>
<blockquote>
<p>I will check if I accidentally imported it as RGB (I don’t know where the setting is).</p>
</blockquote>
</aside>
<p>You can check whether your data is scalar (grayscale) or vector (RGB) under volumes module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f095cf52101d049610a8c6a037906003eebc212.png" data-download-href="/uploads/short-url/291dN3pVq88jFiPAmACLkDAh8HM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f095cf52101d049610a8c6a037906003eebc212_2_482x500.png" alt="image" data-base62-sha1="291dN3pVq88jFiPAmACLkDAh8HM" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f095cf52101d049610a8c6a037906003eebc212_2_482x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f095cf52101d049610a8c6a037906003eebc212_2_723x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f095cf52101d049610a8c6a037906003eebc212_2_964x1000.png 2x" data-dominant-color="F3F3F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">966×1002 49.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Imagestacks will normally convert the image to grayscale (scalar). Make sure that option is checked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61d3704b287fa341e0bb214e152f58148a595a23.png" data-download-href="/uploads/short-url/dXpjPu3eXQlDmnPakWKTtX9moTN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61d3704b287fa341e0bb214e152f58148a595a23_2_367x500.png" alt="image" data-base62-sha1="dXpjPu3eXQlDmnPakWKTtX9moTN" width="367" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61d3704b287fa341e0bb214e152f58148a595a23_2_367x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61d3704b287fa341e0bb214e152f58148a595a23_2_550x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61d3704b287fa341e0bb214e152f58148a595a23_2_734x1000.png 2x" data-dominant-color="F5F6F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">989×1346 54.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2023-09-19 20:35 UTC)

<aside class="quote no-group" data-username="gortm" data-post="5" data-topic="31793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/848f3c/48.png" class="avatar"> gortm:</div>
<blockquote>
<p>But what can I do about it? Should it still draw something? It doesn’t draw anything in my case.</p>
</blockquote>
</aside>
<p>Yes, it should still draw so if it’s still an issue after doing the steps that <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested, it would be great if you could share a few files (enough that someone could replicate the issue).</p>

---

## Post #8 by @gortm (2023-09-22 05:19 UTC)

<p>Sorry, for taking so long to reply. I was running experiments and new CT scans the last couple days.</p>
<p>I resolved the issue. While not being 100% sure, what resolved the problem was downloading the files to have them locally. Probably an obvious solution but I prefer to leave such large datasets (20 Gb) on the NAS. Anyway, now I know and it worked now for another dataset too. The STLs I exported from it are impressively good.</p>
<p>What strangely doesn’t work is the SkyscanReconImport I always have to use ImageStack but that’s off-topic.</p>
<p>Thank you very much <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/pieper">@pieper</a> for your help!</p>

---

## Post #9 by @muratmaga (2023-09-22 10:55 UTC)

<aside class="quote no-group" data-username="gortm" data-post="8" data-topic="31793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/848f3c/48.png" class="avatar"> gortm:</div>
<blockquote>
<p>What strangely doesn’t work is the SkyscanReconImport I always have to use ImageStack but that’s off-topic.</p>
</blockquote>
</aside>
<p>If you can provide the error log for <code>SkyscanReconImport</code> and better yet provide a non-working dataset, we can take a look.</p>

---
