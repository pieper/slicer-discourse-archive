# Is it possible to change ROI to a labelmap?

**Topic ID**: 33193
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/is-it-possible-to-change-roi-to-a-labelmap/33193

---

## Post #1 by @Xiaojie_Guo (2023-12-04 07:44 UTC)

<p>Hi,<br>
I drew a rectangle ROI box in slicer, and want to change it to a label map. Then I can get a mask. What should I do?</p>

---

## Post #2 by @chir.set (2023-12-04 10:00 UTC)

<aside class="quote no-group" data-username="Xiaojie_Guo" data-post="1" data-topic="33193">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaojie_guo/48/67098_2.png" class="avatar"> Xiaojie_Guo:</div>
<blockquote>
<p>change it to a label map</p>
</blockquote>
</aside>
<p>Check the ‘<a href="https://gitlab.com/chir-set/Tools7/-/tree/master/MarkupsToSurface/" rel="noopener nofollow ugc">Markups to surface</a>’ module. It can create a segment from an ROI, that you can convert to a label map in the ‘Data’ module.</p>

---

## Post #3 by @Xiaojie_Guo (2023-12-05 01:16 UTC)

<p>Great! Thanks very much.</p>

---
