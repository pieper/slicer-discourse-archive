---
topic_id: 27114
title: "Multiple Monitors Drawing Tablet"
date: 2023-01-08
url: https://discourse.slicer.org/t/27114
---

# multiple monitors, drawing tablet

**Topic ID**: 27114
**Date**: 2023-01-08
**URL**: https://discourse.slicer.org/t/multiple-monitors-drawing-tablet/27114

---

## Post #1 by @JaredAmudeo (2023-01-08 19:23 UTC)

<p>Hi! is there any way to work with a single layout (e.g. the green) in a drawing tablet (xp-pen artist 12 pro) and let the other like the red, yellow or the 3d view in the main monitor?.</p>

---

## Post #2 by @lassoan (2023-01-10 22:51 UTC)

<p>Multi-monitor support will be added in a few days. You can monitor the progress here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6776">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6776" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6776" target="_blank" rel="noopener">Multi monitor layout</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:multi-monitor-layout</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-10" data-time="22:43:12" data-timezone="UTC">10:43PM - 10 Jan 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 22 files with 571 additions and 104 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6776/files" target="_blank" rel="noopener">
            <span class="added">+571</span>
            <span class="removed">-104</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Layouts can now contain multiple viewports. The default viewport is displayed as<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6776" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> the center widget of the application main window, additional Additional viewports can be independent top-level windows or docking windows.

Views can be maximized/restored separately in each viewport.

Currently, a single new dual-viewport layout is added: Dual Monitor Four-Up View

![image](https://user-images.githubusercontent.com/307929/211677816-0a77cd67-f564-46b3-87d0-944f19da22c8.png)

The pull request is set as "draft" because it requires merging of https://github.com/commontk/CTK/pull/1061 first.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
