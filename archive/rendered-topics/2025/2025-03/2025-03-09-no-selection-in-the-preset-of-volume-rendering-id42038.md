# No selection in the Preset of Volume Rendering

**Topic ID**: 42038
**Date**: 2025-03-09
**URL**: https://discourse.slicer.org/t/no-selection-in-the-preset-of-volume-rendering/42038

---

## Post #1 by @slicer365 (2025-03-09 03:48 UTC)

<p>Version: Windows Slicer 5.8.1</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e347c9aa675b5041519b23fd3ac721544b1d174.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd6de7031230bf353c52fa048e9bc4df11677d2.jpeg" data-video-base62-sha1="21F8uemRsUYFH46CsdS7M86JwuU.mp4">
  </div><p></p>

---

## Post #2 by @lassoan (2025-03-10 01:00 UTC)

<p>Good catch, thanks for reporting. I’ve pushed a fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8305">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8305" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8305" target="_blank" rel="noopener">BUG: Show the currently selected volume rendering preset name</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:fix-volume-rendering-preset-selection-display</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-03-10" data-time="00:59:57" data-timezone="UTC">12:59AM - 10 Mar 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 4 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8305/files" target="_blank" rel="noopener">
            <span class="added">+4</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When selecting a volume rendering preset, the preset name was not reflected in t<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8305" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">he preset selector. The problem was that the volume rendering preset selector looked up what preset should be the selected one by the name of the vtkMRMLVolumePropertyNode and recently copying of the volume property node was changed so that the name was no longer copied.

A quick fix was to copy the preset name to the vtkMRMLVolumePropertyNode.

In the long term, it would be more robust to store the preset node ID in the vtkMRMLVolumePropertyNode when a preset is applied to it.

Fixes the issue reported at https://discourse.slicer.org/t/no-selection-in-the-preset-of-volume-rendering/42038</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It should be integrated within a couple of days into the Slicer Preview Release.</p>

---
