---
topic_id: 21796
title: "Algorithm Used In Watershed Effect In Segment Editor"
date: 2022-02-03
url: https://discourse.slicer.org/t/21796
---

# Algorithm used in Watershed effect in Segment Editor

**Topic ID**: 21796
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/algorithm-used-in-watershed-effect-in-segment-editor/21796

---

## Post #1 by @MPhilip (2022-02-03 12:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> could you please guide me to relevant documentation of the watershed effect implemented on the 3D slicer detailing the algorithm implemented?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-02-04 04:25 UTC)

<p>This effect uses MorphologicalWatershedFromMarkersImageFilter class in ITK. See the full implementation here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5331eafdc77946e957fe771c5324d34dc7c3bc2e/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L114-L119">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5331eafdc77946e957fe771c5324d34dc7c3bc2e/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L114-L119" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5331eafdc77946e957fe771c5324d34dc7c3bc2e/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L114-L119" target="_blank" rel="noopener">lassoan/SlicerSegmentEditorExtraEffects/blob/5331eafdc77946e957fe771c5324d34dc7c3bc2e/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L114-L119</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="114" style="counter-reset: li-counter 113 ;">
            <li>featureImage = sitk.GradientMagnitudeRecursiveGaussian(backgroundImage, float(self.scriptedEffect.doubleParameter("ObjectScaleMm")))
</li>
            <li>del backgroundImage
</li>
            <li>f = sitk.MorphologicalWatershedFromMarkersImageFilter()
</li>
            <li>f.SetMarkWatershedLine(False)
</li>
            <li>f.SetFullyConnected(False)
</li>
            <li>labelImage = f.Execute(featureImage, labelImage)
</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @MPhilip (2022-02-04 09:20 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
Thank you very much for the reply.<br>
I would like to know what the algorithm is called. Is it marker controlled watershed transformation algorithm?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2022-02-04 12:54 UTC)

<p>You can find an details about the algorithm in this paper: <a href="https://doi.org/10.54294/lf8u75">https://doi.org/10.54294/lf8u75</a></p>

---
