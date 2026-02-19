---
topic_id: 41115
title: "The Markups To Model Is Displayed As A Radius Not A Sphere"
date: 2025-01-16
url: https://discourse.slicer.org/t/41115
---

# The"Markups to Model" is displayed as a radius, not a sphere

**Topic ID**: 41115
**Date**: 2025-01-16
**URL**: https://discourse.slicer.org/t/the-markups-to-model-is-displayed-as-a-radius-not-a-sphere/41115

---

## Post #1 by @coenwang01 (2025-01-16 12:14 UTC)

<p>I drew a sphere using the “Shape” function in ExtraMarkups , and then used “Markups to Model” in IGT. However, in the subject hierarchy, the model is only displayed as a radius, not a sphere. Is this a bug?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e3ccf442c0862a3fac80933c2775515fffefb9.jpeg" data-download-href="/uploads/short-url/gXKoVuhj3GKBAqI7TRaxWArjmnT.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e3ccf442c0862a3fac80933c2775515fffefb9_2_690x356.jpeg" alt="1" data-base62-sha1="gXKoVuhj3GKBAqI7TRaxWArjmnT" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e3ccf442c0862a3fac80933c2775515fffefb9_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e3ccf442c0862a3fac80933c2775515fffefb9_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e3ccf442c0862a3fac80933c2775515fffefb9_2_1380x712.jpeg 2x" data-dominant-color="959197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1910×986 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96a3c4f3f5a8a6ba1153d192237cec36d1284223.jpeg" data-download-href="/uploads/short-url/luCuFV1HVlrqi1KcvAdximMSGVt.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a3c4f3f5a8a6ba1153d192237cec36d1284223_2_690x345.jpeg" alt="2" data-base62-sha1="luCuFV1HVlrqi1KcvAdximMSGVt" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a3c4f3f5a8a6ba1153d192237cec36d1284223_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a3c4f3f5a8a6ba1153d192237cec36d1284223_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a3c4f3f5a8a6ba1153d192237cec36d1284223_2_1380x690.jpeg 2x" data-dominant-color="97989F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×962 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-01-16 12:39 UTC)

<aside class="quote no-group" data-username="coenwang01" data-post="1" data-topic="41115">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coenwang01/48/78959_2.png" class="avatar"> coenwang01:</div>
<blockquote>
<p>Is this a bug?</p>
</blockquote>
</aside>
<p>The markups nodes in ‘ExtraMarkups’ are not part of Slicer. SlicerIGT has not been developed taking account of these nodes, and ExtraMarkups has not been developed taking account of SlicerIGT. It’s already surprising that you could do something in SlicerIGT with the Shape node.</p>
<p>If you want to get a sphere with the Shape node, you may consider <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/MarkupsToSurface" rel="noopener nofollow ugc">this</a> module.</p>

---

## Post #3 by @coenwang01 (2025-01-16 12:55 UTC)

<p>It works, thanks very much, it’s helps me a lot!</p>

---
