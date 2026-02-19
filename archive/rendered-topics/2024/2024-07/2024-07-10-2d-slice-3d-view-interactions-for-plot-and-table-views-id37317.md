---
topic_id: 37317
title: "2D Slice 3D View Interactions For Plot And Table Views"
date: 2024-07-10
url: https://discourse.slicer.org/t/37317
---

# 2D Slice/3D View interactions for Plot and Table views

**Topic ID**: 37317
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/2d-slice-3d-view-interactions-for-plot-and-table-views/37317

---

## Post #1 by @jamesobutler (2024-07-10 21:41 UTC)

<p>Maximizing of views with a button in the view controller as well as right-click context menu and double-click actions were originally added in Slicer with the following commit:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/fdb836254de763efdca87a99377e3e5195d83e7e">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/fdb836254de763efdca87a99377e3e5195d83e7e" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/fdb836254de763efdca87a99377e3e5195d83e7e" target="_blank" rel="noopener nofollow ugc">ENH: Allow temporarily maximize a view in the layout</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-09-01" data-time="01:00:44" data-timezone="UTC">01:00AM - 01 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 35 files with 678 additions and 287 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/fdb836254de763efdca87a99377e3e5195d83e7e" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+678</span>
          <span class="removed">-287</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Clicking "maximize" button in the header of the view controller makes the corres<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/fdb836254de763efdca87a99377e3e5195d83e7e" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ponding view maximized in the view layout. Clicking the button again restores the original view layout.

Shortcuts added to access this feature without leaving the view:
- double-click in an empty area in the view maximizes/restores a view
- "Maximize" / "Restore view layout" actions view context menu (right-clicking in an empty area)

Implementation: A new MaximizedViewNode node reference is added to vtkMRMLLayoutNode. If MaximizedViewNode is set to a valid view node then that view is displayed instead of the views defined by vtkMRMLLayoutNode::GetCurrentLayoutDescription(). The current layout ID or description in the layout node is not changed, the override happens at lower level, in qMRMLLayoutManager. The commit moves storage and observation of view nodes from various view controller widgets to the nodes into the parent qMRMLViewControllerBar to reduce code duplication.

fixes #1409

Co-authored-by: jahnavi0801 &lt;jahnavi0801@gmail.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I have recently been doing more work using Plot (and table) views and found myself double-clicking to maximize a Plot view, but nothing happened. I could only maximize the plot using the button in the plot view controller.</p>
<p>Similarly there is no right-click context menu for a Plot view to do things possibly such as changing interaction mode, reset field of view, Copy image to clipboard (svg type like existing Plot export functionality).</p>
<p>Is there any considerations that might’ve avoided the development of double-click to maximize for Plot views and Table views? Tables would probably only have issue in that double-click in the table would try to edit the cell, but double clicking outside of the table cell area could potentially be for maximize/minimize of the table.</p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> for thoughts on these interactions for Plot Views and Table Views as he was a core Slicer developer creating the functionality for the 2D Slice and 3D View interactions.</p>

---

## Post #2 by @lassoan (2024-07-11 02:15 UTC)

<p>I agree that it would be more consistent if double-click to maximized plot and table views as well (maybe table views only when the table is read-only), and some useful features could be added as context menu actions. There was no specific reason to avoid implementing these, we just moved on to work on other things.</p>

---
