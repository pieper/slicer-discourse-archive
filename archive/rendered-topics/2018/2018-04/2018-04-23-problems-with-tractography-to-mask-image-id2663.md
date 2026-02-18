# Problems with Tractography to mask image 

**Topic ID**: 2663
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/problems-with-tractography-to-mask-image/2663

---

## Post #1 by @punadkat (2018-04-23 13:05 UTC)

<p>Hello,</p>
<p>I am trying to convert fiber bundles to label maps. However, when I use the ‘Tractography to mask image’ module, my slicer app crashes. I have tried this on multiple slicer versions with no luck (4.8.1, nightly build). For the label map I’m using the one generated from the baseline image.</p>
<p>Alternatively, I also tried loading the fiber bundles as models and use the ‘model to label map’ module. However, on doing this, the entire label gets filled with the assigned label value(see image below)</p>
<p>Is there something I need to do differently?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc18f2974abf0846c137d77eec294c70bddf7525.png" alt="image" data-base62-sha1="zY9LTOzkfmNR1EpW6fpxZdcMg6h" width="576" height="349"></p>
<p>Thanks</p>

---

## Post #2 by @ihnorton (2018-05-02 19:55 UTC)

<ul>
<li>the Tractography to Mask Image issue will be fixed in tomorrow’s SlicerPreview build:</li>
</ul>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/pull/106">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/106" target="_blank" rel="noopener">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/106" target="_blank" rel="noopener">BUG: fix crash in FB2LabelMap due to mismatched NumPy/VTK dtype size</a>
      </h4>

    <div class="branches">
      <code>SlicerDMRI:master</code> ← <code>ihnorton:fix_fb2labelmap_windows_crash</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-05-02" data-time="19:49:06" data-timezone="UTC">07:49PM - 02 May 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/ihnorton" target="_blank" rel="noopener">
            <img alt="ihnorton" src="https://avatars.githubusercontent.com/u/327706?v=4" class="onebox-avatar-inline" width="20" height="20">
            ihnorton
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 2 additions and 1 deletions">
          <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/106/files" target="_blank" rel="noopener">
            <span class="added">+2</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">NumPy defaults to 'long' on Windows, which is int32. Use a helper inside VTK whi<span class="show-more-container"><a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/106" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ch has the correct dtype for vtkIdTypeArray.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<ul>
<li>I think the issue with ModelToLabelMap is that it is designed for closed surfaces, so it runs a fill operation which isn’t well-defined for streamlines.</li>
</ul>

---

## Post #3 by @lassoan (2018-05-02 22:18 UTC)

<p>You should be able to convert model to labelmap robustly by using segmentations infrastructure:</p>
<ul>
<li>go to Segment editor module, select a master volume that will define geometry of the labelmap</li>
<li>go to Segmentations module</li>
<li>import from model</li>
<li>export to labelmap</li>
</ul>

---

## Post #4 by @ljod (2018-05-02 22:37 UTC)

<p>To clarify tractography-specific usage, it’s good to use the dedicated module. It upsamples the polylines (fibers) to more accurately find the voxels intersected by the points along the fibers. Though I’m interested to know if the Segment Editor does something similar with polylines as well?</p>

---

## Post #5 by @lassoan (2018-05-02 22:43 UTC)

<p>Segmentations can only deal with surface meshes (not lines), so it requires the input to have tubes instead of just centerlines. Currently, you can define labelmap resolution by selecting a reference volume and optionally specifying an oversampling factor.</p>

---
