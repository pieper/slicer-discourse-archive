---
topic_id: 20276
title: "Multiple Control Points In The Edit Position State"
date: 2021-10-20
url: https://discourse.slicer.org/t/20276
---

# Multiple control points in the "Edit" position state

**Topic ID**: 20276
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/multiple-control-points-in-the-edit-position-state/20276

---

## Post #1 by @jamesobutler (2021-10-20 21:54 UTC)

<p>Should the number of control points equal the summation of number of defined and number of undefined control points?</p>
<p>Here I had a control point in the “Edit” state which I copied and pasted into the same list to create multiple. Number of control points is 8, number of defined control points is 1 and number of undefined controls points is 0. A control point in “Edit” mode is considered neither defined or undefined? Or should it actually be considered undefined?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddb5209e48cb3c8f0524626e6f5a145db6b5d414.png" data-download-href="/uploads/short-url/vDjAfsqEbhoAiYPcXCTz3BMWbFG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb5209e48cb3c8f0524626e6f5a145db6b5d414_2_690x228.png" alt="image" data-base62-sha1="vDjAfsqEbhoAiYPcXCTz3BMWbFG" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb5209e48cb3c8f0524626e6f5a145db6b5d414_2_690x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb5209e48cb3c8f0524626e6f5a145db6b5d414_2_1035x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddb5209e48cb3c8f0524626e6f5a145db6b5d414.png 2x" data-dominant-color="B4B6BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1138×377 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-10-21 04:38 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="20276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Should the number of control points equal the summation of number of defined and number of undefined control points?</p>
</blockquote>
</aside>
<p>GetNumberOfDefinedControlPoints: returns PositionDefined or PositionDefined+PositionPreview</p>
<p>GetNumberOfUndefinedControlPoints: returns PositionUndefined or PositionUndefined+PositionPreview</p>
<p>None of them includes PositionMissing and including of PositionPreview is optional.</p>
<p>Therefore, sum of defined and undefined control points does not equal the number of control points.</p>

---

## Post #3 by @jamesobutler (2021-10-21 16:27 UTC)

<p>Is there currently not a method in the API to query the number of control points that are currently in the  “Edit” or “Skip placement” state?</p>
<p>It is confusing to me that a point can be in the “Edit” state, but have a position shown in the table. I guess this is part of what is being described at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5911">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5911" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5911" target="_blank" rel="noopener nofollow ugc">Markups: initiate editing in the control point list should not make a position displayed immediately</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-29" data-time="15:17:59" data-timezone="UTC">03:17PM - 29 Sep 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When clicking the control point table to edit a point then the point position is<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> filled immediately. This position gets deleted if I move over to a view and leave the view and the edit icon disappears from the table. It would be better if starting editing would just change the icon to edit (would not show the coordinates) and after going over a view and coming back, the edit icon would stay displayed in the table while placement mode is enabled. This would make it clear for the user which point will be the next to place (without need to hover over any view) and would ensure that the table state would not be changed just because the user temporarily moves the mouse over a view.

## Environment
- Slicer version: Slicer-4.11.0-2021-09-27
- Operating system: Windows

@smrolfe</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
