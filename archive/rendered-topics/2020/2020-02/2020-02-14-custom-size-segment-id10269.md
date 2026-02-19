---
topic_id: 10269
title: "Custom Size Segment"
date: 2020-02-14
url: https://discourse.slicer.org/t/10269
---

# Custom Size Segment

**Topic ID**: 10269
**Date**: 2020-02-14
**URL**: https://discourse.slicer.org/t/custom-size-segment/10269

---

## Post #1 by @manjula (2020-02-14 23:26 UTC)

<ol>
<li>
<p>Can some one please help me with in creating a custom Box shape area  of segmentation  like the Sphere in the  “Manipulating objects in the slice viewer” ?</p>
</li>
<li>
<p>Or is there a way to define the ROI and then create a segment out of the region within the ROI box ?<br>
I need to create a segment with define length and width and height.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24fc73c417ef1b04c3f1949ef08444ade76b02a7.png" data-download-href="/uploads/short-url/5hc431EMZ7mljwZiVl6khR7BypF.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fc73c417ef1b04c3f1949ef08444ade76b02a7_2_651x500.png" alt="Screenshot" data-base62-sha1="5hc431EMZ7mljwZiVl6khR7BypF" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fc73c417ef1b04c3f1949ef08444ade76b02a7_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fc73c417ef1b04c3f1949ef08444ade76b02a7_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24fc73c417ef1b04c3f1949ef08444ade76b02a7.png 2x" data-dominant-color="332F36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1160×890 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Is it possible to cut out multiple segments at once ?</li>
</ol>

---

## Post #2 by @lassoan (2020-02-16 04:58 UTC)

<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="10269">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Can some one please help me with in creating a custom Box shape area of segmentation like the Sphere in the “Manipulating objects in the slice viewer” ?</p>
</blockquote>
</aside>
<p>The same example works for box shape, too. You can use <code>vtkCubeSource</code> instead of <code>vtkSphereSource</code>.</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="10269">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Or is there a way to define the ROI and then create a segment out of the region within the ROI box ?<br>
I need to create a segment with define length and width and height.</p>
</blockquote>
</aside>
<p>You can create a box using <code>vtkCubeSource</code> and create a model from that. This is done in SlicerIGT extension’s “Create models” module.</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="10269">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Is it possible to cut out multiple segments at once ?</p>
</blockquote>
</aside>
<p>Yes. For this, set masking settings to “overwrite all other segments” and then create a new segment and <em>fill</em> that. If you fill a segment that will erase that region from all other segments.</p>

---
