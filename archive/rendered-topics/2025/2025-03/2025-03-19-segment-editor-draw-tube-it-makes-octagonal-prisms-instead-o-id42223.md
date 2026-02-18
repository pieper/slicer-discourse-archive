# Segment Editor: Draw Tube - it makes octagonal prisms instead of smooth cylinders

**Topic ID**: 42223
**Date**: 2025-03-19
**URL**: https://discourse.slicer.org/t/segment-editor-draw-tube-it-makes-octagonal-prisms-instead-of-smooth-cylinders/42223

---

## Post #1 by @bobcieri (2025-03-19 17:18 UTC)

<p>I am using the draw tube feature in the segment editor. It is great, except that it is drawing octagonal prisms instead of cylinders/tubes. This is much more apparent when the radius is increased to above 10. Can the number of sides of the polygon be increased to make smoother tubes?</p>
<p>I am running the current Slicer version 5.8.1 on Windows</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d67575381e996353ddea264a26f1ca171969a6c1.jpeg" data-download-href="/uploads/short-url/uBbPww0lClayoeY2ww1vFtqlLAR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67575381e996353ddea264a26f1ca171969a6c1_2_657x500.jpeg" alt="image" data-base62-sha1="uBbPww0lClayoeY2ww1vFtqlLAR" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67575381e996353ddea264a26f1ca171969a6c1_2_657x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67575381e996353ddea264a26f1ca171969a6c1_2_985x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67575381e996353ddea264a26f1ca171969a6c1_2_1314x1000.jpeg 2x" data-dominant-color="868BA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1636×1244 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2025-03-19 20:08 UTC)

<p>Here is the source:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L525-L528">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L525-L528" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerSegmentEditorExtraEffects</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L525-L528" target="_blank" rel="noopener nofollow ugc">SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py#L525-L528" rel="noopener nofollow ugc"><code>784997471</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="525" style="counter-reset: li-counter 524 ;">
          <li>markupsToModel.UpdateOutputCurveModel( inputMarkup, outputModel,</li>
          <li>  interpolationType, False, self.radius, 8, NumberOfLineSegmentsBetweenControlPoints, True, 3,</li>
          <li>  slicer.vtkMRMLMarkupsToModelNode.RawIndices, self.curveGenerator,</li>
          <li>  polynomialFitType )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You should be able to change the resolution to any you want (only limited by segmentation geometry). Currently the resolution is hard-coded to 8 sides for the tube</p>

---

## Post #3 by @bobcieri (2025-03-19 20:19 UTC)

<p>Thanks! I will give this a try.</p>

---
