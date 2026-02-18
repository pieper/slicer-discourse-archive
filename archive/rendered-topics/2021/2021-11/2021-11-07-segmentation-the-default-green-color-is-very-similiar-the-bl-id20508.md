# Segmentation: the default green color is very similiar the bluegreen color

**Topic ID**: 20508
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/segmentation-the-default-green-color-is-very-similiar-the-bluegreen-color/20508

---

## Post #1 by @tsinesh (2021-11-07 09:15 UTC)

<p>in the Segmentation Editor, the blue-green color automatically suggested by Local Threshold (picture 1) is very similar default green color for a new segmentation (picture 2). When I press Ctrl+left mouse to add a suggested segment to the final segmentation, the difference between the two colors is hard to see for me (picture 3). To recognize if all parts of the my segmentation are added is difficult, because of the similarity of the both colors. A color other than green as default for new segments that does not resemble bluegreen would be more user friendly. Since I want to segment several hundred records, manually changing the default color green results in significant extra work.<br>
How can I change the default color to green in 3d Slicer version 4.13?</p>
<p><strong>picture 1:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76faf9c7ab6628849956fb5129a098fcddcd0ff5.jpeg" data-download-href="/uploads/short-url/gYy3npjOgwtWCNj6HP2YqKZeTVH.jpeg?dl=1" title="bluegreen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76faf9c7ab6628849956fb5129a098fcddcd0ff5_2_690x388.jpeg" alt="bluegreen" data-base62-sha1="gYy3npjOgwtWCNj6HP2YqKZeTVH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76faf9c7ab6628849956fb5129a098fcddcd0ff5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76faf9c7ab6628849956fb5129a098fcddcd0ff5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76faf9c7ab6628849956fb5129a098fcddcd0ff5_2_1380x776.jpeg 2x" data-dominant-color="808080"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bluegreen</span><span class="informations">1920×1080 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>picture 2:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b24b8556c14be7730f841474ed2d41a0e7a5640.jpeg" data-download-href="/uploads/short-url/fhPLdVZ4lQuSE9HKTD0tIPfiPF6.jpeg?dl=1" title="green" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b24b8556c14be7730f841474ed2d41a0e7a5640_2_690x388.jpeg" alt="green" data-base62-sha1="fhPLdVZ4lQuSE9HKTD0tIPfiPF6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b24b8556c14be7730f841474ed2d41a0e7a5640_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b24b8556c14be7730f841474ed2d41a0e7a5640_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b24b8556c14be7730f841474ed2d41a0e7a5640_2_1380x776.jpeg 2x" data-dominant-color="808080"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">green</span><span class="informations">1920×1080 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>picture 3:</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61c03196a4ceeebcd6fa6bb16893851db2bf7311.png" alt="together" data-base62-sha1="dWK5riChg6pxYQUCzTmVzFP4C9r" width="462" height="268"></p>

---

## Post #2 by @DIV (2021-11-07 23:35 UTC)

<p>Hello, tsinesh.  Though not an immediate solution, the discussions at <a href="https://discourse.slicer.org/t/simple-color-vs-terminology-color-usage/20271" class="inline-onebox">Simple Color vs Terminology Color usage</a> and <a href="https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236" class="inline-onebox">Segment Editor: reduce the number of mouse clicks to set basic colour for segment</a> might also be relevant to your usage.<br>
—DIV</p>

---

## Post #3 by @lassoan (2021-11-08 02:39 UTC)

<p>The preview (“bluegreen”) color is generated automatically from the segment’s color by making it similar enough so that you know which segment you are dealing with, but different enough so that you can distinguish it from the segment color.</p>
<p>You can go and edit the <a><code>&lt;yourslicerfolder&gt;/NA-MIC/Extensions-&lt;NNNNN&gt;/SegmentEditorExtraEffects/lib/Slicer-&lt;X&gt;.&lt;Y&gt;/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py</code></a> file to make the colors more distinguishable by modifying this line:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/88673aa16b5c818f8319c7860eef73c361be985b/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L80">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/88673aa16b5c818f8319c7860eef73c361be985b/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L80" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/88673aa16b5c818f8319c7860eef73c361be985b/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L80" target="_blank" rel="noopener">lassoan/SlicerSegmentEditorExtraEffects/blob/88673aa16b5c818f8319c7860eef73c361be985b/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L80</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="70" style="counter-reset: li-counter 69 ;">
          <li>  return</li>
          <li>
          </li>
<li># Make sure we keep the currently selected segment hidden (the user may have changed selection)</li>
          <li>if segmentID != self.previewedSegmentID:</li>
          <li>  self.setCurrentSegmentTransparent()</li>
          <li>
          </li>
<li># Change color hue slightly to make it easier to distinguish filled regions from preview</li>
          <li>r,g,b = segmentationNode.GetSegmentation().GetSegment(segmentID).GetColor()</li>
          <li>import colorsys</li>
          <li>colorHsv = colorsys.rgb_to_hsv(r, g, b)</li>
          <li class="selected">(r, g, b) = colorsys.hsv_to_rgb((colorHsv[0]+0.2) % 1.0, colorHsv[1], colorHsv[2])</li>
          <li>
          </li>
<li># Set values to pipelines</li>
          <li>for sliceWidget in self.previewPipelines:</li>
          <li>  pipeline = self.previewPipelines[sliceWidget]</li>
          <li>  pipeline.lookupTable.SetTableValue(1,  r, g, b,  opacity)</li>
          <li>  layerLogic = self.getMasterVolumeLayerLogic(sliceWidget)</li>
          <li>  pipeline.thresholdFilter.SetInputConnection(layerLogic.GetReslice().GetOutputPort())</li>
          <li>  pipeline.thresholdFilter.ThresholdBetween(min, max)</li>
          <li>  pipeline.actor.VisibilityOn()</li>
          <li>  sliceWidget.sliceView().scheduleRender()</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The simplest is to change the 0.2 value to something bigger, but you can also experiment with adjusting the saturation (<code>colorHsv[1]</code>) and brightness (<code>colorHsv[2]</code>) components as well.<br>
If you think you have a formula that works better then modify the file on GitHub (by clicking the link above then clicking the pencil - <code>Edit this file</code> icon in the top-right corner). GitHub will offer to create a fork and a pull request - just accept those and we’ll receive your proposed change, review, and update the extension accordingly.</p>

---
