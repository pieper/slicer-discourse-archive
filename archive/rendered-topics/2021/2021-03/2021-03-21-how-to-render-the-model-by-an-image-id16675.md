# How to render the model by an image

**Topic ID**: 16675
**Date**: 2021-03-21
**URL**: https://discourse.slicer.org/t/how-to-render-the-model-by-an-image/16675

---

## Post #1 by @slicer365 (2021-03-21 15:16 UTC)

<p>Dear Professors<br>
I Always fail when using image rendering model! as is shown in this picture.How to solve the problem，After clicking apply, the model becomes white.win 20210226<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c01d53d5eb3b4097614827585363d2c8502464.jpeg" data-download-href="/uploads/short-url/qmnsoYtDnd4PLpCgUhNPz5AruVm.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8c01d53d5eb3b4097614827585363d2c8502464_2_690x349.jpeg" alt="捕获" data-base62-sha1="qmnsoYtDnd4PLpCgUhNPz5AruVm" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8c01d53d5eb3b4097614827585363d2c8502464_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8c01d53d5eb3b4097614827585363d2c8502464_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c01d53d5eb3b4097614827585363d2c8502464.jpeg 2x" data-dominant-color="938A90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1365×692 86.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2021-03-22 05:03 UTC)

<p>You need to choose the texture image (in your case: “Heart_B”) as “Texture”.</p>

---

## Post #4 by @slicer365 (2021-03-22 05:08 UTC)

<p>Thank you very much for the reply from Professor Andras Lasso. Yes, I chose Heart_B as the texture. I named it 1.jpg, but as you can see, the model changed from the original color to white.</p>

---

## Post #5 by @lassoan (2021-03-22 05:20 UTC)

<p>If the model is all white after applying the texture then most likely no texture coordinates are found. VTK (the visualization toolkit that Slicer uses) can most reliably load textures from .obj files.</p>

---

## Post #7 by @pieper (2021-03-22 14:05 UTC)

<p>If you are using SlicerDMRI to generate and save the tracts then you probably need to change from RAS to LPS (just negate the first two coordinates).  Tractography .vtk files are always in RAS (as are any tensors stored with them) while models now default to LPS.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/ecbb45593c276f5e0f501b8284521d84cb314215" target="_blank" rel="noopener">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/ecbb45593c276f5e0f501b8284521d84cb314215" target="_blank" rel="noopener">Merge pull request #137 from SlicerDMRI/136-flipped-fibers</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-08-25" data-time="16:04:09" data-timezone="UTC">04:04PM - 25 Aug 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
        
      </div>

      <div class="lines" title="changed 3 files with 12 additions and 0 deletions">
        <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/ecbb45593c276f5e0f501b8284521d84cb314215" target="_blank" rel="noopener">
          <span class="added">+12</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">BUG: explicitly flag all vtk fiber bundles RAS</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @slicer365 (2021-03-22 15:13 UTC)

<p>Thank you Professor Steve Pieper,you are right！I solved the problem with your help！</p>

---

## Post #9 by @pieper (2021-03-22 15:57 UTC)

<p>Excellent, best of luck!</p>

---
