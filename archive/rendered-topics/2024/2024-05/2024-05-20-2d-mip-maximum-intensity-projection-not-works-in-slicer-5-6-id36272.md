# 2D MIP (maximum intensity projection) not works in Slicer 5.6.1

**Topic ID**: 36272
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/2d-mip-maximum-intensity-projection-not-works-in-slicer-5-6-1/36272

---

## Post #1 by @park (2024-05-20 06:55 UTC)

<p>Hi all,</p>
<p>I would like to make maximum intensity projection (MIP) in 2D view<br>
Thus, I tried the code below from the ‘script repository’</p>
<pre><code class="lang-auto">sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sliceLayerLogic = sliceLogic.GetBackgroundLayer()
reslice = sliceLayerLogic.GetReslice()
reslice.SetSlabModeToMax()
reslice.SetSlabNumberOfSlices(600) # use a large number of slices (600) to cover the entire volume
reslice.SetSlabSliceSpacingFraction(0.5) # spacing between slices are 0.5 pixel (supersampling is useful to reduce interpolation artifacts)
sliceNode.Modified()
</code></pre>
<p>This codes work in Slicer 5.0.3  but not works in 5.6.1, 5.6.2<br>
Could I get a solution about this ?</p>

---

## Post #2 by @pieper (2024-05-20 14:49 UTC)

<p>Slab reconstruction has moved to the core, so operating on the <code>vtkImageResllice</code> directly is no longer the right way.</p>
<p>You should be able to migrate using the info here.  It would be great if you could make a PR to the script repository updating to the new approach.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/530b8fcdca4987533a03cfc9361585007883808b">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/530b8fcdca4987533a03cfc9361585007883808b" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/530b8fcdca4987533a03cfc9361585007883808b" target="_blank" rel="noopener">ENH: Update Slicer Controller adding Thick Slab Reconstruction (#7021)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-07-14" data-time="03:00:03" data-timezone="UTC">03:00AM - 14 Jul 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/stephencrowell" target="_blank" rel="noopener">
          <img alt="stephencrowell" src="https://avatars.githubusercontent.com/u/85647068?v=4" class="onebox-avatar-inline" width="20" height="20">
          stephencrowell
        </a>
      </div>

      <div class="lines" title="changed 12 files with 457 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/530b8fcdca4987533a03cfc9361585007883808b" target="_blank" rel="noopener">
          <span class="added">+457</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit updates the Slice Controller widget adding controls for
enabling th<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/530b8fcdca4987533a03cfc9361585007883808b" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">e Thick Slab Reconstruction (TSR), selecting the reconstruction
type (max, min, mean, sum) as well as adjusting the slab thickness.

It also updates the DataProbe/SlicerViewAnnotations to allow displaying
the slab type and thickness.

It updates the Slice node adding the following properties:
* SlabReconstructionEnabled
* SlabReconstructionType
* SlabReconstructionThickness
* SlabReconstructionOversamplingFactor

Finally, it also updates vtkMRMLSliceNodeTest adding the following tests:
* SlabReconstructionEnabledTest
* SlabReconstructionTypeTest
* SlabReconstructionThicknessTest

Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @park (2024-05-28 08:02 UTC)

<p>I got a solution about this</p>
<pre><code class="lang-auto">
sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeSlice7")
sliceNode.SetSlabReconstructionEnabled(True)
sliceNode.SetSlabReconstructionOversamplingFactor(VolumeSpacing)
sliceNode.SetSlabReconstructionThickness(thickness)
sliceNode.SetSlabReconstructionType(2) # Mean projection
sliceNode.Modified()
</code></pre>

---

## Post #4 by @pieper (2024-05-28 18:47 UTC)

<p>Nice!  It would be cool if you could update the script repository with your solution.</p>

---
