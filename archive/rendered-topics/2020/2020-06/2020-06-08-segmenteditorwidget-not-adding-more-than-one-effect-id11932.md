# SegmentEditorWidget not adding more than one effect

**Topic ID**: 11932
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/segmenteditorwidget-not-adding-more-than-one-effect/11932

---

## Post #1 by @Queen_Rei (2020-06-08 19:52 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55ee47ee78af9d2e2da207d039a1a85fd69ae7d7.png" alt="image" data-base62-sha1="cgb6b0I8oP1ZjoU1J7rDeAH4LJB" width="598" height="398"></p>
<p>I tried to add a threshold, open, and close smoothing effect in my module, but it’s only doing the thresholding. Is there something I am doing wrong? Do you need any more info?</p>
<p>Thank you and hope you and your family/friends are safe &lt;3</p>

---

## Post #2 by @lassoan (2020-06-08 21:07 UTC)

<p>You need to call <code>onApply</code> when you want to apply an effect (it is not enough to do it once at the end).</p>
<p>Also, name of the smoothing methods are not correct. See the correct values here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/6256f99080957f39f41b1830f52bd8dcd5263a3d/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorSmoothingEffect.py#L353-L357" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6256f99080957f39f41b1830f52bd8dcd5263a3d/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorSmoothingEffect.py#L353-L357" target="_blank">Slicer/Slicer/blob/6256f99080957f39f41b1830f52bd8dcd5263a3d/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorSmoothingEffect.py#L353-L357</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="353" style="counter-reset: li-counter 352 ;">
<li>MEDIAN = 'MEDIAN'</li>
<li>GAUSSIAN = 'GAUSSIAN'</li>
<li>MORPHOLOGICAL_OPENING = 'MORPHOLOGICAL_OPENING'</li>
<li>MORPHOLOGICAL_CLOSING = 'MORPHOLOGICAL_CLOSING'</li>
<li>JOINT_TAUBIN = 'JOINT_TAUBIN'</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Finally, if you want to both remove extrusions and fill holes then use median method instead of opening+closing.</p>

---
