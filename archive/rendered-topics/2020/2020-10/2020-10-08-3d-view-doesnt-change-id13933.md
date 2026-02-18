# 3D view doesn't change

**Topic ID**: 13933
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/3d-view-doesnt-change/13933

---

## Post #1 by @arifeuzundurukan (2020-10-08 13:19 UTC)

<p>Hello everyone,<br>
I do not understand why I see the 3D picture even I hide the all of the parts. Also, I couldn’t see seperately in 3D when I try to click the eye icon neither for soft tissue or for rib cage .<br>
Could you please help me</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3f7b736a71c4497c6a5af84d05c1a893576978.png" data-download-href="/uploads/short-url/vQWu81X9ni2eoIE5uf24FBUW5cI.png?dl=1" title="Capture d'écran 2020-10-08 09.10.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3f7b736a71c4497c6a5af84d05c1a893576978_2_690x388.png" alt="Capture d'écran 2020-10-08 09.10.27" data-base62-sha1="vQWu81X9ni2eoIE5uf24FBUW5cI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3f7b736a71c4497c6a5af84d05c1a893576978_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3f7b736a71c4497c6a5af84d05c1a893576978_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3f7b736a71c4497c6a5af84d05c1a893576978_2_1380x776.png 2x" data-dominant-color="97897F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d'écran 2020-10-08 09.10.27</span><span class="informations">1920×1080 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-10-08 13:51 UTC)

<p>You probably have other nodes displayed (e.g., you exported segmentation to models). You can check what nodes you have in the scene (and hide what you don’t need) in Data module.</p>

---

## Post #3 by @arifeuzundurukan (2020-10-08 14:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>odes displayed (e.g., you exported segmentation to models</p>
</blockquote>
</aside>
<p>Excuse me, I am new in 3D slicer and I have just only used the sample data in software. Could you please help me about how I can check it.<br>
Before exporting and saving my 3D geometries, I was able to use  the hide and show eye buttom.</p>

---

## Post #4 by @lassoan (2020-10-08 16:38 UTC)

<p>The <em>model node</em> you exported is shown regardless you show or hide your <em>segmentation node</em>. Go to Data module and hide your model nodes (by clicking on the eye icon) so that they don’t occlude your segmentation.</p>

---
