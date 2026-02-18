# Integration of Fast Growcut extension for 3D slicer

**Topic ID**: 32786
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/integration-of-fast-growcut-extension-for-3d-slicer/32786

---

## Post #1 by @Shreyas_reddy (2023-11-13 17:50 UTC)

<p>Hi everybody,</p>
<p>Subject: Inquiry on Integrating Fast GrowCut Software with Latest 3D Slicer Version</p>
<p>Dear 3D Slicer Developer Community,</p>
<p>I am currently working on a project that involves utilizing Fast GrowCut software for segmentation purposes. However, I have encountered challenges in integrating Fast GrowCut with the latest version of 3D Slicer (version 5.4.0). Despite my efforts to find an extension or plugin for Fast GrowCut in the Extensions Manager, I have been unsuccessful. I would greatly appreciate any guidance or information on how to effectively use Fast GrowCut within the latest 3D Slicer environment. If there are specific steps, scripts, or alternative methods that could facilitate this integration, your expertise would be invaluable. Thank you for your time and assistance.</p>
<p>Best regards,</p>
<p>Dr Shreyas Reddy K<br>
email - <a href="mailto:Drshreyasreddy111295@gmail.com">Drshreyasreddy111295@gmail.com</a></p>

---

## Post #2 by @pieper (2023-11-13 18:17 UTC)

<p>How is the version you are working on different than what’s already in Slicer?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITKGrowCut">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/InsightSoftwareConsortium/ITKGrowCut" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/5496308324e91d14b60d71f91e20bc074561bc801bad279eb886589d66854a00/InsightSoftwareConsortium/ITKGrowCut" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/InsightSoftwareConsortium/ITKGrowCut" target="_blank" rel="noopener">GitHub - InsightSoftwareConsortium/ITKGrowCut: ITKGrowCut is a remote module...</a></h3>

  <p>ITKGrowCut is a remote module for ITK. It segments a 3D image from user-provided foreground and background seeds. - GitHub - InsightSoftwareConsortium/ITKGrowCut: ITKGrowCut is a remote module for ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5807">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5807" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/5807" target="_blank" rel="noopener">Enable GrowCut remote module in ITK</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>dzenanz:updateITK</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-19" data-time="19:51:19" data-timezone="UTC">07:51PM - 19 Aug 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/dzenanz" target="_blank" rel="noopener">
            <img alt="dzenanz" src="https://avatars.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
            dzenanz
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/5807/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">GrowCut remote module in ITK has recently been updated to mirror Slicer's improv<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5807" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ements. This PR contains pre-requisites to removing this code from Slicer and refactoring it to use the version coming from ITK.

I have not begun the Slicer refactoring, and I would prefer if somebody else did that. I could support them by making changes inside `ITKGrowCut`.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2023-11-14 23:20 UTC)

<p>FastGrowCut is available by the name “Grow from seeds” in Segment Editor module.</p>

---
