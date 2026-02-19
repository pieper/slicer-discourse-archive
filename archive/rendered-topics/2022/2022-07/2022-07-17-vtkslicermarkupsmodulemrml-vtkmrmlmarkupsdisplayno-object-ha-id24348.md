---
topic_id: 24348
title: "Vtkslicermarkupsmodulemrml Vtkmrmlmarkupsdisplayno Object Ha"
date: 2022-07-17
url: https://discourse.slicer.org/t/24348
---

# 'vtkSlicerMarkupsModuleMRML.vtkMRMLMarkupsDisplayNo' object has no attribute 'SetSliceDisplayModeToProjection'

**Topic ID**: 24348
**Date**: 2022-07-17
**URL**: https://discourse.slicer.org/t/vtkslicermarkupsmodulemrml-vtkmrmlmarkupsdisplayno-object-has-no-attribute-setslicedisplaymodetoprojection/24348

---

## Post #1 by @jumbojing (2022-07-17 05:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bdcd81fd395af3e01c0c2b528ba8ad6808e1858.png" data-download-href="/uploads/short-url/jXhwy2E4vcSeGr96eluI9ht2Xzi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bdcd81fd395af3e01c0c2b528ba8ad6808e1858_2_690x69.png" alt="image" data-base62-sha1="jXhwy2E4vcSeGr96eluI9ht2Xzi" width="690" height="69" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bdcd81fd395af3e01c0c2b528ba8ad6808e1858_2_690x69.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bdcd81fd395af3e01c0c2b528ba8ad6808e1858.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bdcd81fd395af3e01c0c2b528ba8ad6808e1858.png 2x" data-dominant-color="DDF2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×99 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
what’s wrong?</p>

---

## Post #2 by @lassoan (2022-07-17 07:25 UTC)

<p>As the error message states, there is no such method. It is only available in model display nodes. See what projection options are available for markups in the <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html">markups display node documentation</a>.</p>

---

## Post #3 by @jumbojing (2022-07-17 07:58 UTC)

<p><code>dn.SliceProjectionOn()</code></p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="24348" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>如错误消息所述，没有此类方法。它仅在模型显示节点中可用。在标记<a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html" rel="noopener nofollow ugc">显示节点文档中</a>查看哪些可用于标记的投影选项。</p>
</blockquote>
</aside>
<p>Thanks</p>

---
