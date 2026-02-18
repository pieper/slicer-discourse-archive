# Install extensions

**Topic ID**: 26528
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/install-extensions/26528

---

## Post #1 by @Mohamed1 (2022-12-01 04:02 UTC)

<p>Hey dears 3D slicer supporters<br>
First of all thank you all for your tremendous support.<br>
today I want to ask about the tissueSegmentation extension, I have already installed it, and once I go to choose it from the modules windows, it said the extension was not uploaded. however, in the extension manager it appears as an installed extension.<br>
please any help with that<br>
Thank you very much!</p>

---

## Post #2 by @lassoan (2022-12-01 04:45 UTC)

<p>The initialization of the tissue segmentation module was broken. I’ve submitted a pull request to get it fixed:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/MarinaSandonis/SlicerTissueSegmentation/pull/1">
  <header class="source">

      <a href="https://github.com/MarinaSandonis/SlicerTissueSegmentation/pull/1" target="_blank" rel="noopener">github.com/MarinaSandonis/SlicerTissueSegmentation</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/MarinaSandonis/SlicerTissueSegmentation/pull/1" target="_blank" rel="noopener">Update Tis_Seg.py</a>
      </h4>

    <div class="branches">
      <code>MarinaSandonis:main</code> ← <code>lassoan:patch-1</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-01" data-time="04:43:11" data-timezone="UTC">04:43AM - 01 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 30 additions and 43 deletions">
          <a href="https://github.com/MarinaSandonis/SlicerTissueSegmentation/pull/1/files" target="_blank" rel="noopener">
            <span class="added">+30</span>
            <span class="removed">-43</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes the problem reported here: https://discourse.slicer.org/t/install-extensio<span class="show-more-container"><a href="https://github.com/MarinaSandonis/SlicerTissueSegmentation/pull/1" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ns/26528

pip_install must not be called from the main namespace of a script because that may take long time and it is always executed (even if the user does not even open the module)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
