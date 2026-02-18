# Segmentation in Jupyter notebook

**Topic ID**: 13583
**Date**: 2020-09-21
**URL**: https://discourse.slicer.org/t/segmentation-in-jupyter-notebook/13583

---

## Post #1 by @Hugo (2020-09-21 09:41 UTC)

<p>Hello everyone,</p>
<p>I’m trying to make a simply version of 3d slicer using the Jupyter notebook.<br>
I would like to enable the « sphere » brush option and be able to choose the % of the brush in my def paint but didn’t find a way to do it properly.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad37288b660decda0fdb13ed885e6cc047ca8aaf.png" alt="image002" data-base62-sha1="oIkMhbN5XwWqvY5JJ21xlQqcMTt" width="587" height="282"></p>
<p>For now the brush is working find but only in 2d.</p>
<p>Thank you</p>

---

## Post #2 by @Hugo (2020-09-21 09:52 UTC)

<p>I’ve managed to resolve my issue by adding this line:</p>
<pre><code>    segmentEditorWidget.effectByName("Paint").setCommonParameter("BrushSphere", 1)</code></pre>

---

## Post #3 by @Hugo (2020-09-21 14:25 UTC)

<p>Hello everyone,</p>
<p>I’m currently coding in a 3d slicer Jupyter notebook in order to make a simplify version of 3d slicer with only the tools I need.<br>
I would like to enable the « sphere » brush option and be able to choose the % of the brush in my def paint but didn’t find a way to do it properly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50bbe52391f4b4e6fd1997fba73f439e33cd00e4.png" data-download-href="/uploads/short-url/bwcLbbJWlfrd2SNP7Tscd5m9XOA.png?dl=1" title="GraphiqueCollé-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50bbe52391f4b4e6fd1997fba73f439e33cd00e4_2_690x331.png" alt="GraphiqueCollé-1" data-base62-sha1="bwcLbbJWlfrd2SNP7Tscd5m9XOA" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50bbe52391f4b4e6fd1997fba73f439e33cd00e4_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50bbe52391f4b4e6fd1997fba73f439e33cd00e4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50bbe52391f4b4e6fd1997fba73f439e33cd00e4.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GraphiqueCollé-1</span><span class="informations">782×376 45.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For now the brush is working find but only in 2d.</p>
<p>Thank you!</p>
<p>Hugo</p>

---

## Post #4 by @lassoan (2020-09-21 14:27 UTC)

<p>This topic should help:</p>
<aside class="quote" data-post="2" data-topic="13460">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/shortcut-for-sphere-brush/13460/2">Shortcut for Sphere brush</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Instead of creating a new widget, refer to the Segment Editor module’s widget: 
segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
paintEffect = segmentEditorWidget.effectByName("Paint")
paintEffect.setCommonParameter("BrushSphere", 1)  # enable
paintEffect.setCommonParameter("BrushSphere", 0)  # disable
  </blockquote>
</aside>


---

## Post #5 by @Hugo (2020-09-22 08:26 UTC)

<p>It worked for me thanks a lot!<br>
I’m now trying to do the same thing with the diameter of the brush</p>

---

## Post #6 by @lassoan (2020-09-22 12:18 UTC)

<p>This topic should help:</p>
<aside class="quote" data-post="10" data-topic="4247">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/controlling-brush-diameter-increment-when-using-shift-scroll/4247/10">Controlling brush diameter increment when using Shift+Scroll</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Good. I guess not re-creating the segment editor widget fixed the selection reset issue. 
Brush parameters are shared between paint and erase effects, so it is a common parameter, which need to be set by using setCommonParameter method: 
effect.setCommonParameter("BrushDiameterIsRelative", "0")
effect.setCommonParameter("BrushAbsoluteDiameter", newDiam)
  </blockquote>
</aside>


---
