---
topic_id: 20274
title: "Ambiguous Control Point In Right Click Context Menu"
date: 2021-10-20
url: https://discourse.slicer.org/t/20274
---

# Ambiguous control point in right-click context menu

**Topic ID**: 20274
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/ambiguous-control-point-in-right-click-context-menu/20274

---

## Post #1 by @jamesobutler (2021-10-20 19:26 UTC)

<p>When hovering the mouse over a Markups Line, Angle, Curve or Closed Curve node where you are highlighting and not hovering over a control point, then right-clicking to bring up the context menu has confusing options to manipulate a control point.</p>
<p>There are options to rename, toggle, jump, and delete control point however it is ambiguous about which control point it will be acting upon since none is highlighted. This does not happen for a Markups Plane or ROI node which just provides the ability to delete the markup node.</p>
<p>It also seems odd that there would be an ability to rename a control point when the individual control point label is not even being shown. Only the label for the markup name is being shown.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/371f7dcdfe63005665b2f7dba0e8474bb406e254.png" data-download-href="/uploads/short-url/7RDJjJzBdyGLCLwNJyoi13MinUo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/371f7dcdfe63005665b2f7dba0e8474bb406e254.png" alt="image" data-base62-sha1="7RDJjJzBdyGLCLwNJyoi13MinUo" width="690" height="368" data-dominant-color="4E4945"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">695×371 12.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdb03cb11f2dbf8d920ef66a53c505463ba570fc.png" data-download-href="/uploads/short-url/tlBsZBB0b2yxakC0UEO5lAcv6EI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdb03cb11f2dbf8d920ef66a53c505463ba570fc.png" alt="image" data-base62-sha1="tlBsZBB0b2yxakC0UEO5lAcv6EI" width="690" height="241" data-dominant-color="302D2D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">807×283 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2021-10-21 16:32 UTC)

<p>The control point menu actions when hovering over the object and not at a control point, appears to manipulate the closest control point even though it isn’t highlighted. If I hover over the line between the first and second control point, but I’m 25% along the line so closer to the first control point then renaming will rename the first control point which is “OC-1”.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> It would be clearer for control point modification to only be when the control point is highlighted and not just along the line. Can it be change to be like the plane and ROI node and when hovering over the object such as along the line it instead only show context options for the markup node rather than the control point?</p>

---

## Post #3 by @lassoan (2021-10-21 16:41 UTC)

<p>I agree, it could make sense to only show control point actions (except jump to closest control point) if the active component is a control point. It would be great if you could submit a pull request with the change.</p>

---

## Post #4 by @muratmaga (2021-10-21 16:43 UTC)

<p>One action that would make sense is to delete the whole curve (or change its colors/edit properties). Currently it is possible but it is indicated delete markup. Better to rename it to “delete curve”</p>

---

## Post #5 by @jamesobutler (2021-10-21 16:46 UTC)

<p>So rename:</p>
<ul>
<li>Delete markup</li>
<li>Edit markup terminology…</li>
<li>Edit properties…</li>
</ul>
<p>to something with markup type name like the following?</p>
<ul>
<li>Delete curve</li>
<li>Edit curve terminology…</li>
<li>Edit curve properties…</li>
</ul>

---

## Post #6 by @jamesobutler (2021-10-23 21:12 UTC)

<p>PR posted for this work:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5961">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5961" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5961" target="_blank" rel="noopener nofollow ugc">Markups context menu specific text based on type and improved options based on active selection</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:markups-context-menu-updates</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-23" data-time="21:12:28" data-timezone="UTC">09:12PM - 23 Oct 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="2 commits changed 1 files with 12 additions and 8 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5961/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+12</span>
          <span class="removed">-8</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Originally discussed over at https://discourse.slicer.org/t/ambiguous-control-po<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5961" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">int-in-right-click-context-menu/20274

| | Before | This PR |
|-|---------|---------|
|Right-click point|![image](https://user-images.githubusercontent.com/15837524/138571657-98c0ed20-90ad-4aa8-a478-11dfe2444c64.png)|![image](https://user-images.githubusercontent.com/15837524/138571663-04f5ab62-6b76-4080-a4b8-ee80051ba1a4.png)|
|Right-click node|![image](https://user-images.githubusercontent.com/15837524/138571682-47a484de-454b-44a1-b8db-8a2abaf2eb3c.png)|![image](https://user-images.githubusercontent.com/15837524/138571688-ed341910-1cdc-4dbc-8196-12a796ab2d63.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
