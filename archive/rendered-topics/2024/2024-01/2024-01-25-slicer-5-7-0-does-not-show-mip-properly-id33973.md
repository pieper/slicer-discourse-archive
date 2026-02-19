---
topic_id: 33973
title: "Slicer 5 7 0 Does Not Show Mip Properly"
date: 2024-01-25
url: https://discourse.slicer.org/t/33973
---

# Slicer 5.7.0 does not show MIP properly

**Topic ID**: 33973
**Date**: 2024-01-25
**URL**: https://discourse.slicer.org/t/slicer-5-7-0-does-not-show-mip-properly/33973

---

## Post #1 by @ruili (2024-01-25 16:24 UTC)

<p>Hello,</p>
<p>I would like to report a possible bug with slicer 5.7.0 revision 32698 built 2024-01-25 for Mac system. In module “Volume Rendering”, when I tried to show the maximum/minimum intensity projection of a volume, it does not show properly in the 3D view.</p>
<p>Best,</p>
<p>Rui</p>

---

## Post #2 by @lassoan (2024-01-25 17:30 UTC)

<p>Shadows are not compatible with maximum/minimum intensity projection rendering modes. You can to disable “Shadows visibility” in the view controller. I’ve added an issue to make sure that the users are aware of this limitation:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7560">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7560" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7560" target="_blank" rel="noopener">MIP volume rendering MIP does not appear if shadows visibility is enabled</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-25" data-time="17:29:11" data-timezone="UTC">05:29PM - 25 Jan 24 UTC</span>
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

Volume rendering MIP (minimum/maximum intensity projection) is inc<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ompatible with shadows option. The volume does not appear if "Shadows visibility" option is enabled in the 3D view.

## Environment
- Slicer version: Slicer-5.7.0 2024-01-25
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
