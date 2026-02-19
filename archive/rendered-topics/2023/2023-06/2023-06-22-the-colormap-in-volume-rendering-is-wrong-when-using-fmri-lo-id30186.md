---
topic_id: 30186
title: "The Colormap In Volume Rendering Is Wrong When Using Fmri Lo"
date: 2023-06-22
url: https://discourse.slicer.org/t/30186
---

# The colormap in "Volume Rendering" is wrong when using "fMRI" lookup table in "Volume"

**Topic ID**: 30186
**Date**: 2023-06-22
**URL**: https://discourse.slicer.org/t/the-colormap-in-volume-rendering-is-wrong-when-using-fmri-lookup-table-in-volume/30186

---

## Post #1 by @ffr (2023-06-22 18:42 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.3.0<br>
Expected behavior: fMRI colormap in “Volume Rendering”<br>
Actual behavior: Looks like it is using the “Warm2” colormap.</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2023-06-24 19:27 UTC)

<p>Thanks for reporting, you’ve discovered a problem: colormap is inaccurately copied from color tables that have few entries and sudden changes between them. I’ve pushed a fix that will be integrated into the Slicer Preview Release soon. You can monitor the status of the fix here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7042">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7042" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7042" target="_blank" rel="noopener">BUG: Fix color synchronization inaccuarcy in volume rendering module</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-volume-rendering-color-sync</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-24" data-time="19:25:18" data-timezone="UTC">07:25PM - 24 Jun 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 88 additions and 61 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7042/files" target="_blank" rel="noopener">
            <span class="added">+88</span>
            <span class="removed">-61</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a color node with few color table entries (such as fMRI) was used for showi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7042" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ng a volume, the "Synchronize with Volumes module" button in volume rendering module very inaccurately copied the color entries to the color transfer function. The problem was that only every 64th color table entry was copied. Fixed the issue by copying up to 24 color entries (evenly sampled in the lookup table) of the table into the transfer function. This number is large enough to accurately represent a color table, but not too high so that users can still edit the color transfer manually.

Also fixed synchronization of continuous color mapping. All control points of continuous color maps are copied, so these are copied in full fidelity.

Fixes the problem reported at https://discourse.slicer.org/t/the-colormap-in-volume-rendering-is-wrong-when-using-fmri-lookup-table-in-volume/30186</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
