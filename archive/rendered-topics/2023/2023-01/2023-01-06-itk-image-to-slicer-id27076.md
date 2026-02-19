---
topic_id: 27076
title: "Itk Image To Slicer"
date: 2023-01-06
url: https://discourse.slicer.org/t/27076
---

# ITK image to Slicer

**Topic ID**: 27076
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/itk-image-to-slicer/27076

---

## Post #1 by @muratmaga (2023-01-06 06:19 UTC)

<p>I am testing the <a href="https://github.com/KitwareMedical/ITKIOScanco" rel="noopener nofollow ugc">itk-ioscanco module</a> with Slicer and successfully imported a file through Slicer Python console. Is there any documentation on how to convert this ITK image in a way that shows up in Slicer UI?</p>

---

## Post #2 by @lassoan (2023-01-06 17:49 UTC)

<p><a href="https://github.com/Slicer/Slicer/commit/8d8ba687b8626fb77f5237a87180dd659f7f856d">Scanco file reading was added</a> was added to Slicer almost two years ago. Is there any .isq file that you cannot load just by drag-and-dropping to Slicer that you can load using the itk-ioscanco module?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/thewtex">@thewtex</a> In general, what is a good way to transfer images, transforms, etc. between ITKPython modules and Slicer?</p>

---

## Post #3 by @muratmaga (2023-01-06 18:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="27076">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer/commit/8d8ba687b8626fb77f5237a87180dd659f7f856d">Scanco file reading was added </a> was added to Slicer almost two years ago.</p>
</blockquote>
</aside>
<p>I wasn’t aware of it. Works like a charm!</p>

---
