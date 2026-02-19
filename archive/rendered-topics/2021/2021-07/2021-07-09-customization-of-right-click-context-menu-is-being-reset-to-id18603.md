---
topic_id: 18603
title: "Customization Of Right Click Context Menu Is Being Reset To"
date: 2021-07-09
url: https://discourse.slicer.org/t/18603
---

# Customization of right-click context menu is being reset to default unexpectedly

**Topic ID**: 18603
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/customization-of-right-click-context-menu-is-being-reset-to-default-unexpectedly/18603

---

## Post #1 by @jamesobutler (2021-07-09 15:35 UTC)

<p>I’m trying to modify visible options of the right-click context menu, but my customization is not being maintained. I haven’t figured out what causes it by it ultimately returns to the default right-click context menu and reverting my customization.</p>
<p>I’m doing the right-click context menu customization using<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/subjecthierarchy.html?highlight=context%20menu#use-whitelist-to-customize-view-menu" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/subjecthierarchy.html?highlight=context%20menu#use-whitelist-to-customize-view-menu</a></p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f4558beccf23a939536fa23b2aada495b7e0d3.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f4558beccf23a939536fa23b2aada495b7e0d3.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f4558beccf23a939536fa23b2aada495b7e0d3.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @cpinter (2021-07-09 15:38 UTC)

<p>There was a recent change in the API, it’s probably just that the example script has not been updated. Let me look into it.</p>

---

## Post #3 by @jamesobutler (2021-07-09 15:41 UTC)

<p>Appears to happen when I customize and then I right-click in the open area to bring up the transform/adjust Window/Level/Place/Copy menu. Then when right-clicking over the markups it is different from the beginning.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d4eaa5c0f4828f397064336a38f703a224cebca.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d4eaa5c0f4828f397064336a38f703a224cebca.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d4eaa5c0f4828f397064336a38f703a224cebca.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #4 by @cpinter (2021-07-09 15:43 UTC)

<p>My suspicion was not right, the function names are correct…</p>

---

## Post #5 by @jamesobutler (2021-07-09 15:59 UTC)

<p>Was there a defined way to customize the right-click context menu of the Slice view versus the right-click context menu on a markups point? I would guess this is contributing to the problem as one is probably redefining the other?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b100e66fffb59f1416394b517f565291c41d03.png" alt="image" data-base62-sha1="od9V5w7Ko1EaQsmgftuighoVb11" width="196" height="105"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bda85ba53c3c5f790ff8736faa00c09657c7737.png" alt="image" data-base62-sha1="fo7gP860XJoaCxanjW02ltkL5Ij" width="224" height="176"></p>

---

## Post #6 by @cpinter (2021-07-09 16:15 UTC)

<p>You are probably right. The view context menu was recently overhauled by <a class="mention" href="/u/lassoan">@lassoan</a> so I’d refer to him with this, since he is more familiar with the latest code.</p>

---

## Post #7 by @lassoan (2021-07-09 17:22 UTC)

<p>I’ve checked the code and the menu is rebuilt after a menu is constructed without any visible items (because none of the DisplayedViewContextMenuActionNames were visible when you right-clicked on the view background). This problem has not come up before because the menu was only available for markups. I’ll push a fix later today.</p>

---

## Post #8 by @jamesobutler (2021-07-09 18:04 UTC)

<p>Thanks! I guess those 4 empty string “” entries returned by <code>availableViewContextMenuActionNames()</code> were those 4 new slice view context menu actions.</p>
<p>I guess if they weren’t empty string named actions, then I probably could have customized to something like <code>newActions = ["ToggleSelectPointAction", "ViewTransformAction"]</code> to have at least one action in both menus and then they would not get recreated from default and maintain the customization.</p>

---

## Post #9 by @lassoan (2021-07-09 20:01 UTC)

<p>Pushed a fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5732">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5732" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5732" target="_blank" rel="noopener">BUG: Fix customization of view context menu</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:fix-view-context-menu-whitelist</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-07-09" data-time="20:00:45" data-timezone="UTC">08:00PM - 09 Jul 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 6 files with 77 additions and 70 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5732/files" target="_blank" rel="noopener">
          <span class="added">+77</span>
          <span class="removed">-70</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">List of allowed view context menu actions was reset whenever the menu was rebuil<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5732" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">t.
Fixed by introducing a string list that stores the allowed action names.

https://discourse.slicer.org/t/customization-of-right-click-context-menu-is-being-reset-to-default-unexpectedly/18603/7</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
