---
topic_id: 7055
title: "Threshholding A Binary Image"
date: 2019-06-06
url: https://discourse.slicer.org/t/7055
---

# Threshholding a binary image

**Topic ID**: 7055
**Date**: 2019-06-06
**URL**: https://discourse.slicer.org/t/threshholding-a-binary-image/7055

---

## Post #1 by @Kasra_Arnavaz (2019-06-06 12:44 UTC)

<p>Slicer version: 4.10.0</p>
<p>I would like to segment a stack of tiff files in Segment Editor. This should have been quite simple because there are only 0 and 255 pixel values, but to my surprise some part of the image are not segmented correctly. Any idea why this occurs and how to fix it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52ec27198aa5067590ef44f714df833e98fe2ffe.png" data-download-href="/uploads/short-url/bPz6F8gOPMsrGN1vRQrbYReha2y.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52ec27198aa5067590ef44f714df833e98fe2ffe.png" alt="Untitled" data-base62-sha1="bPz6F8gOPMsrGN1vRQrbYReha2y" width="616" height="499" data-dominant-color="383D38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1093×887 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-06-06 13:24 UTC)

<p>There could be many reasons for this. Instead of trying to guess which one is it, could you please upload somewhere an example scene (in .mrb format - click the package icon in the save data window) and send us the link?</p>
<p>If the image is already segmented then I would recommend to load it as a labelmap volume (choose “Show options” and click “LabelMap” in “Add data” window) then convert it to segmentation (in Data module, right-click on it and choose "Convert labelmap to segmentation node).</p>

---

## Post #3 by @Kasra_Arnavaz (2019-06-07 12:18 UTC)

<p>Thank you very much Andras! That solved my problem. The visibility options in Data module is a bit tricky but I can find my segmentation under Segment Editor as well.</p>
<p>As for why this is happening, I have created the .mrb file in case you have the time to take a look at.<br>
<a href="https://we.tl/t-JCxiKzYHy3" rel="nofollow noopener">https://we.tl/t-JCxiKzYHy3</a></p>

---
