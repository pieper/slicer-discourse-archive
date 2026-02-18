# Markup control point coordinate values are not automatically updated when switching between World and Local

**Topic ID**: 39982
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/markup-control-point-coordinate-values-are-not-automatically-updated-when-switching-between-world-and-local/39982

---

## Post #1 by @MMMPPPMMM (2024-11-01 12:03 UTC)

<p>Hello</p>
<p>When I switch between “World” and “Local” in the “Coordinates:” drop down list of the Control Points section of the Markups module, the coordinates are not automatically updated.</p>
<p>As workaround one can use the “Previous Modules” and “Next Modules” buttons once. Then the coordinate values are updated.</p>
<p>However, I assume this is not the intended behavior.</p>
<p>Tested with 3D Slicer 5.6.2 r32448 / f10cd8c</p>
<p>Kind regards</p>

---

## Post #2 by @lassoan (2024-11-01 15:02 UTC)

<p>Thank you, good catch. I’ve submitted an issue and tentatively scheduled to be fixed before the next stable release (that is due end of next week), but maybe it will be fixed later:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8024">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8024" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8024" target="_blank" rel="noopener">Markup control point coordinates are not updating in the table</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-01" data-time="15:02:01" data-timezone="UTC">03:02PM - 01 Nov 24 UTC</span>
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
    <p class="github-body-container">## Summary

1. When I switch between “World” and “Local” in the “Coordinates:”<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> drop down list of the Control Points section of the Markups module, the coordinates are not automatically updated.

As workaround one can use the “Previous Modules” and “Next Modules” buttons once. Then the coordinate values are updated.

(reported here: https://discourse.slicer.org/t/markup-control-point-coordinate-values-are-not-automatically-updated-when-switching-between-world-and-local/39982)

2. When the markup is under a transform and the transform is changed, displayed control point coordinates in World mode should keep changing, but the displayed coordinate values are not updated.

## Environment
- Slicer version: 3D Slicer 5.6.2 r32448 / f10cd8c (happens with latest Slicer-5.7 version, too)
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
