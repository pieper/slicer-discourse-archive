# Volume cropping CT images using lung masks

**Topic ID**: 28155
**Date**: 2023-03-03
**URL**: https://discourse.slicer.org/t/volume-cropping-ct-images-using-lung-masks/28155

---

## Post #1 by @Vahdane (2023-03-03 14:19 UTC)

<p>Hello,</p>
<p>I want to crop the lung CT image to lobe subregions by using lung masks. I have the masks, however, as far as I know, we can only crop the image to a rectangular shape in the <em>crop volume</em> module.</p>
<p>Thanks for your help in advance,<br>
Vahdaneh</p>

---

## Post #2 by @hherhold (2023-03-03 14:34 UTC)

<p>You can use the “Mask volume” tool in the Segment Editor to do exactly this.</p>
<p>You may need to install Segment Editor Extra Effects; I always have it installed and I don’t remember if the base Slicer has this tool or not.</p>

---

## Post #3 by @Vahdane (2023-03-03 14:58 UTC)

<p>Many thanks for your help! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---
