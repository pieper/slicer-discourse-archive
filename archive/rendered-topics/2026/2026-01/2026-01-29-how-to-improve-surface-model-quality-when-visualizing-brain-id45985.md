# How to improve surface model quality when visualizing brain ROI masks in 3D Slicer

**Topic ID**: 45985
**Date**: 2026-01-29
**URL**: https://discourse.slicer.org/t/how-to-improve-surface-model-quality-when-visualizing-brain-roi-masks-in-3d-slicer/45985

---

## Post #1 by @younghoo (2026-01-29 14:46 UTC)

<p>Dear experts,</p>
<p>I am trying to visualize a set of white matter tract masks in 3D using 3D Slicer. My current workflow involves loading the masks as segmentations and then using the “Export visible segments to models” tool to convert them into surface models. However, the resulting models are not ideal. As shown in the attached figure (using one tract mask as an example), the edges appear overly sharp, the surfaces contain holes, and there are isolated fragments where the structure should be continuous and whole.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b39f83ce5de3db8fcde736a5045b62c23fbd1d9.png" data-download-href="/uploads/short-url/hA6Vyv4DODOuVcRQwBscWJWCGVj.png?dl=1" title="one_example_tract_mask" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b39f83ce5de3db8fcde736a5045b62c23fbd1d9_2_690x339.png" alt="one_example_tract_mask" data-base62-sha1="hA6Vyv4DODOuVcRQwBscWJWCGVj" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b39f83ce5de3db8fcde736a5045b62c23fbd1d9_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b39f83ce5de3db8fcde736a5045b62c23fbd1d9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b39f83ce5de3db8fcde736a5045b62c23fbd1d9.png 2x" data-dominant-color="96A4C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">one_example_tract_mask</span><span class="informations">898×442 50.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please advise on how to improve the visualization quality? For instance, are there recommended ways to preprocess the masks to generate better surface models, or is it possible to directly modify the surface models after generation?</p>
<p>Thank you for your time and expertise.</p>
<p>Best regards,<br>
Yang Hu</p>

---

## Post #2 by @pieper (2026-01-29 15:44 UTC)

<p>You can change the segmentation geometry to supersample the labelmap so that the surface generation has more voxels to represent the thin structures.</p>

---

## Post #3 by @younghoo (2026-01-30 06:08 UTC)

<p>Thank you for the suggestion. Following your advice, I supersampled the ROI mask from its original 1mm resolution to 0.5mm and 0.25mm.</p>
<p>As shown in the attached figures, the surface model generated from the 0.5mm mask shows noticeable improvement in smoothness and continuity. I also verified that the isolated components observed earlier were indeed present in the original mask itself, and not an artifact introduced by the surface generation process.</p>
<p>At this point, the 0.5mm result seems to be the best achievable through resampling. Could you please suggest if there are any further steps I could take to enhance the visualization quality?</p>
<p>0.5mm<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02b5e3bc0bc87e71f37918f2d36e41451973c3e1.jpeg" data-download-href="/uploads/short-url/nYEoHdTyXkbqRyuODTViXuIrOV.jpeg?dl=1" title="mask_0.5mm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02b5e3bc0bc87e71f37918f2d36e41451973c3e1_2_690x335.jpeg" alt="mask_0.5mm" data-base62-sha1="nYEoHdTyXkbqRyuODTViXuIrOV" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02b5e3bc0bc87e71f37918f2d36e41451973c3e1_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02b5e3bc0bc87e71f37918f2d36e41451973c3e1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02b5e3bc0bc87e71f37918f2d36e41451973c3e1.jpeg 2x" data-dominant-color="9298BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mask_0.5mm</span><span class="informations">988×480 41.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
0.25mm<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdc1e4d71e8837fcb0ccc3176348bc1cbf3eebcb.jpeg" data-download-href="/uploads/short-url/r4FEMbj20VpilU5MDYIc7T70Qnp.jpeg?dl=1" title="mask_0.25mm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdc1e4d71e8837fcb0ccc3176348bc1cbf3eebcb_2_690x335.jpeg" alt="mask_0.25mm" data-base62-sha1="r4FEMbj20VpilU5MDYIc7T70Qnp" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdc1e4d71e8837fcb0ccc3176348bc1cbf3eebcb_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdc1e4d71e8837fcb0ccc3176348bc1cbf3eebcb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdc1e4d71e8837fcb0ccc3176348bc1cbf3eebcb.jpeg 2x" data-dominant-color="9499C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mask_0.25mm</span><span class="informations">988×480 56.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2026-01-30 07:41 UTC)

<p>Yes, after you supersample you can smooth the labelmap and/or smooth the surface model more to remove the woodgrain effect.</p>

---

## Post #5 by @younghoo (2026-02-01 14:17 UTC)

<p>Thank you for your guidance on improving surface model quality. I have a related follow-up question regarding visualization. If it is more appropriate to open a new thread for this topic, please let me know.</p>
<p>I have calculated a specific brain measure (e.g., FA, MD) for each white matter tract mask and performed statistical group analysis. As a result, each tract now has an associated statistical value (e.g., T-value or p-value). I would like to visualize these statistical values directly on the corresponding 3D tract surface models using a continuous colormap, essentially creating a statistical overlay on the anatomy. My initial thought is to export the tract surface as a .vtk file and then embed the statistical data into the file, which could then be mapped to colors in 3D Slicer.</p>
<p>Is this the recommended approach for such visualization in 3D Slicer? If so, what tools or modules within (or outside) Slicer could I use to efficiently insert the statistical data into the surface mesh?</p>
<p>Thank you in advance for your suggestions.</p>

---

## Post #6 by @pieper (2026-02-01 14:24 UTC)

<p>Yes, you can add a scalar field to the cells or points of the tracts and then select it for display in the models module.  Depending on how you are calculating the statistical values, you may find it easiest to do this in python.</p>
<p>Something like how it’s done here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L148-L151">
  <header class="source">

      <a href="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L148-L151" target="_blank" rel="noopener">github.com/pieper/SlicerSOFA</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L148-L151" target="_blank" rel="noopener">Experiments/vertebra.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L148-L151" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="148" style="counter-reset: li-counter 147 ;">
          <li>stressVTKArray = vtk.vtkFloatArray()</li>
          <li>stressVTKArray.SetNumberOfValues(grid.GetNumberOfCells())</li>
          <li>stressVTKArray.SetName("VonMisesStress")</li>
          <li>modelNode.GetUnstructuredGrid().GetCellData().AddArray(stressVTKArray)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L276-L279">
  <header class="source">

      <a href="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L276-L279" target="_blank" rel="noopener">github.com/pieper/SlicerSOFA</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L276-L279" target="_blank" rel="noopener">Experiments/vertebra.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/pieper/SlicerSOFA/blob/main/Experiments/vertebra.py#L276-L279" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="276" style="counter-reset: li-counter 275 ;">
          <li># update stress from forceField</li>
          <li>stressArray = slicer.util.arrayFromModelCellData(modelNode, "VonMisesStress")</li>
          <li>stressArray[:] = forceField.vonMisesPerElement.array()</li>
          <li>slicer.util.arrayFromModelCellDataModified(modelNode, "VonMisesStress")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
