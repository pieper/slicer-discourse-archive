---
topic_id: 45658
title: "Include Functionality Of Control Point Status In Custom Scri"
date: 2026-01-02
url: https://discourse.slicer.org/t/45658
---

# Include functionality of control point status in custom scripted module

**Topic ID**: 45658
**Date**: 2026-01-02
**URL**: https://discourse.slicer.org/t/include-functionality-of-control-point-status-in-custom-scripted-module/45658

---

## Post #1 by @W.J.Heerink (2026-01-02 09:42 UTC)

<p>Hi, I really like the use of the control point status as it is implemented in the Markups module. I mainly use the functionality of the buttons in the column of the table to change the status of individual control points.</p>
<p>Currently, I am building a scripted module where I would like to implement the same functionality, because the constant switching between the custom scripted module and the Markups module would be annoying.</p>
<p>To my knowledge, qSlicerSimpleMarkupsWidget does not provide this functionality. Is there an easy way to get the same kind of table integrated in my module?</p>
<p>Thanks!</p>

---

## Post #2 by @W.J.Heerink (2026-01-08 20:46 UTC)

<p>I found this issue in the attic that seems to be related: <a href="https://github.com/Slicer/Slicer/issues/6452" class="inline-onebox" rel="noopener nofollow ugc">Add reusable widget for markups control point list · Issue #6452 · Slicer/Slicer · GitHub</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Do you think there will be progress on this feature anytime soon? Thanks!</p>

---

## Post #3 by @lassoan (2026-01-08 20:52 UTC)

<p>It would be easy to add a “position status” column to the simple markups widget, which you could click to cycle through the position states (as in the main Markups GUI). Would that be sufficient for your use case?</p>

---

## Post #4 by @W.J.Heerink (2026-01-08 21:42 UTC)

<p>Yes it would. As I mainly need to toggle control points between missing and defined as well as put them in place mode to define undefined points.</p>

---

## Post #5 by @lassoan (2026-01-10 18:06 UTC)

<p>I’ve added this new feature, it is currently under review.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8955">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8955" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8955" target="_blank" rel="noopener">ENH: Add position status column to qSlicerSimpleMarkupsWidget</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:simple-markups-position-status</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-01-10" data-time="18:06:03" data-timezone="UTC">06:06PM - 10 Jan 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 193 additions and 25 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8955/files" target="_blank" rel="noopener">
            <span class="added">+193</span>
            <span class="removed">-25</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The new column is hidden by default. Its visibility is controlled by the positio<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8955" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nStatusColumnVisible property.

Requested in https://discourse.slicer.org/t/include-functionality-of-control-point-status-in-custom-scripted-module/45658

related to #6452

Example:

```
w=slicer.qSlicerSimpleMarkupsWidget()
w.setMRMLScene(slicer.mrmlScene)
w.setPositionStatusColumnVisible(True)
w.show()
```

&lt;img width="742" height="219" alt="image" src="https://github.com/user-attachments/assets/fe97a3c4-f2e6-4335-b275-22901aa2dd70" /&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @W.J.Heerink (2026-01-12 11:18 UTC)

<p>Thank you so much for quickly resolving this request. I guess it will be available in the new nightly release? Is there any way to get it working within a stable release, too?</p>

---

## Post #7 by @lassoan (2026-01-12 16:34 UTC)

<p>It was merged two days ago, so it should be already available in the latest Slicer Preview Release.</p>
<p>We usually don’t backport new features into patch releases, so it will be available in the new Slicer Stable Release (5.12) in about 3 month.</p>

---
