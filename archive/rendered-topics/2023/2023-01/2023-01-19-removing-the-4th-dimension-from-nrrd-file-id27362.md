# Removing the 4th dimension from NRRD file

**Topic ID**: 27362
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/removing-the-4th-dimension-from-nrrd-file/27362

---

## Post #1 by @Senn81 (2023-01-19 18:02 UTC)

<p>Hi Slicer support</p>
<p>In some of my segmentations my NRRD files have an extra dimension (4th dimension). This has caused issues with compatibility with certain software loading the file up. Would anyone know how to remove this extra dimension so that the file only has 3 dimensions?</p>
<p>Any help would be greatly appreciated.</p>
<p>Thank you</p>
<p>Senn</p>

---

## Post #2 by @pieper (2023-01-19 18:51 UTC)

<p>You might be able to use <code>unu reshape</code> as <a href="https://teem.sourceforge.net/unrrdu/">described here</a>.</p>

---

## Post #3 by @muratmaga (2023-01-19 18:58 UTC)

<aside class="quote no-group" data-username="Senn81" data-post="1" data-topic="27362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/senn81/48/18085_2.png" class="avatar"> Senn81:</div>
<blockquote>
<p>This has caused issues with compatibility with certain software loading the file up</p>
</blockquote>
</aside>
<p>You mean you are trying load the segmentation you did in Slicer (*.seg.nrrd file) into a some other software? If that’s the case, you will probably be better off exporting the segmentation as a labelmap and try.</p>

---
