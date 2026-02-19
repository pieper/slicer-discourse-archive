---
topic_id: 24056
title: "Simplemarkupswidget Is Missing Features"
date: 2022-06-26
url: https://discourse.slicer.org/t/24056
---

# SimpleMarkupsWidget is missing features

**Topic ID**: 24056
**Date**: 2022-06-26
**URL**: https://discourse.slicer.org/t/simplemarkupswidget-is-missing-features/24056

---

## Post #1 by @koeglfryderyk (2022-06-26 23:12 UTC)

<p>I have a SimpleMarkupsWidget in my Python Scripted module, that looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a647d1d5ac13b88ea9ab7324f7bf4b177abb3e.jpeg" data-download-href="/uploads/short-url/v3pRF23qtB8ExiDRFRQ2w6o3cyG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9a647d1d5ac13b88ea9ab7324f7bf4b177abb3e_2_345x157.jpeg" alt="image" data-base62-sha1="v3pRF23qtB8ExiDRFRQ2w6o3cyG" width="345" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9a647d1d5ac13b88ea9ab7324f7bf4b177abb3e_2_345x157.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9a647d1d5ac13b88ea9ab7324f7bf4b177abb3e_2_517x235.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9a647d1d5ac13b88ea9ab7324f7bf4b177abb3e_2_690x314.jpeg 2x" data-dominant-color="F0EFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1006×460 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, this widget is missing certain features that are important to me, in contrast to the Control Points menu in the Markups module, as show below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ad67f0f68578589684af87a247f660797eb646.jpeg" data-download-href="/uploads/short-url/zCKptdFUAkldH21kLAd4zHCrBEq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ad67f0f68578589684af87a247f660797eb646_2_345x213.jpeg" alt="image" data-base62-sha1="zCKptdFUAkldH21kLAd4zHCrBEq" width="345" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ad67f0f68578589684af87a247f660797eb646_2_345x213.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ad67f0f68578589684af87a247f660797eb646_2_517x319.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ad67f0f68578589684af87a247f660797eb646_2_690x426.jpeg 2x" data-dominant-color="E8E8E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1028×636 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The features that I’m missing are the column with ‘eye’ for visibility and the Description column. Is there a way to add those features to the SimpleMarkupsWidget? Or is there another widget that has those features? (I looked for one in the QT designer but couldn’t find any)</p>

---

## Post #2 by @lassoan (2022-06-28 03:27 UTC)

<p>qSimpleMarkupsWidget is intended to be a simplified version of the control point list widget in the Markups module. I agree that since the widget was developed many years ago, many features were added to Markups module that would make sense to expose in a reusable widget. Would you be interested in developing this feature? I’ve added some information about this task here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6452">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6452" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6452" target="_blank" rel="noopener">Add reusable widget for markups control point list</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-28" data-time="03:26:55" data-timezone="UTC">03:26AM - 28 Jun 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

qSlicerSimp<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">leMarkupsWidget does not support any of the new features that are available in the Markups module's control point table widget.

## Describe the solution you'd like

We would need to create a new qSlicerMarkupsControlPointTableView+Model that could replace both these widgets.

## Additional context

I've started to work on this at some point but then ran out of time. The development branch is available here: https://github.com/lassoan/Slicer/tree/attic/markups-control-points-table-view</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @koeglfryderyk (2022-07-01 21:58 UTC)

<p>Thanks for the information - I’ll take a look at it, but I’m not sure I have enough time at the moment</p>

---

## Post #4 by @jmhuie (2023-01-20 20:17 UTC)

<p>Just chiming in to say that I would also like an updated qSimpleMarkupsWidget that can handle template point lists. I don’t have the knowledge on how to make that happen (or the time currently).</p>

---
