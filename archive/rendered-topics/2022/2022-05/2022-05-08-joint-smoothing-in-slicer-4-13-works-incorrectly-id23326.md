# Joint Smoothing in Slicer 4.13 works incorrectly 

**Topic ID**: 23326
**Date**: 2022-05-08
**URL**: https://discourse.slicer.org/t/joint-smoothing-in-slicer-4-13-works-incorrectly/23326

---

## Post #1 by @Volha (2022-05-08 02:04 UTC)

<p>Hello!<br>
I do the following: run Slicer4.13=&gt; Segment Editor=&gt; Smoothing =&gt; Joint smoothing (1.0) =&gt; apply. I get the result: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d72e176582ae516ed9e0f1e781ab4a7d5efc0841.jpeg" data-download-href="/uploads/short-url/uHzpcAjtmnC1CjeT4NdXxspoqs1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72e176582ae516ed9e0f1e781ab4a7d5efc0841_2_690x221.jpeg" alt="image" data-base62-sha1="uHzpcAjtmnC1CjeT4NdXxspoqs1" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72e176582ae516ed9e0f1e781ab4a7d5efc0841_2_690x221.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72e176582ae516ed9e0f1e781ab4a7d5efc0841_2_1035x331.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72e176582ae516ed9e0f1e781ab4a7d5efc0841_2_1380x442.jpeg 2x" data-dominant-color="79AB8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2010×644 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
But in Slice v4.11 result is different: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e62345438103ccb7516d225d04840a4077424e6f.jpeg" data-download-href="/uploads/short-url/wPTnS3YNRlrke2zBkLfXjFwRBi7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e62345438103ccb7516d225d04840a4077424e6f_2_690x209.jpeg" alt="image" data-base62-sha1="wPTnS3YNRlrke2zBkLfXjFwRBi7" width="690" height="209" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e62345438103ccb7516d225d04840a4077424e6f_2_690x209.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e62345438103ccb7516d225d04840a4077424e6f_2_1035x313.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e62345438103ccb7516d225d04840a4077424e6f_2_1380x418.jpeg 2x" data-dominant-color="7CA69B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2139×649 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please explain what has changed in Slicer v4.13 compared to Slicer v4.11 for Joint Smoothing?<br>
How can it be fixed for Slicer v4.13?</p>

---

## Post #2 by @lassoan (2022-05-08 22:47 UTC)

<p>I can confirm that there is a change in behavior of the joint smoothing. It is due to change in the underlying smoothing filter in VTK. I’ve posted a question on the VTK forum about it:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/mesh-internal-surface-smoothing-behavior-changed-in-vtkwindowedsincpolydatafilter/8446">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/mesh-internal-surface-smoothing-behavior-changed-in-vtkwindowedsincpolydatafilter/8446" target="_blank" rel="noopener" title="10:44PM - 08 May 2022">VTK – 8 May 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:619/500;"><img src="https://discourse.vtk.org/uploads/default/optimized/2X/a/a6609463fa083082648046345fffa4dbc0f3e28e_2_1024x827.png" class="thumbnail" width="619" height="500"></div>

<h3><a href="https://discourse.vtk.org/t/mesh-internal-surface-smoothing-behavior-changed-in-vtkwindowedsincpolydatafilter/8446" target="_blank" rel="noopener">Mesh internal surface smoothing behavior changed in...</a></h3>

  <p>It seems that the rewrite of vtkWindowedSincPolyDataFilter (that amazingly improved its performance) also changed how internal surfaces are smoothed. Smoothing of internal surfaces are important because when we segment a medical image we usually...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In the meantime, you can use other smoothing methods with the <code>Apply to all segments</code> option enabled, optionally followed by <code>Joint smoothing</code> to reduce gaps between segments.</p>

---
