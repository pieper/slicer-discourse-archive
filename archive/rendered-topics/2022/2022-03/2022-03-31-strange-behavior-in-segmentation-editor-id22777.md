# Strange behavior in segmentation editor

**Topic ID**: 22777
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/strange-behavior-in-segmentation-editor/22777

---

## Post #1 by @alan6690 (2022-03-31 13:07 UTC)

<p>Sometimes when I use mask volume under the segmentation editor, the output volume option behaves weird that neither existing volume nor creating new volume can be chosen. Instead, only a option called “scene” can be selected, as shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47c8c91da26b2e388730a966b2df66b73ac5843e.png" data-download-href="/uploads/short-url/af253BKkzUEgBPaQyKuYE4Rre4m.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47c8c91da26b2e388730a966b2df66b73ac5843e_2_690x388.png" alt="1" data-base62-sha1="af253BKkzUEgBPaQyKuYE4Rre4m" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47c8c91da26b2e388730a966b2df66b73ac5843e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47c8c91da26b2e388730a966b2df66b73ac5843e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47c8c91da26b2e388730a966b2df66b73ac5843e_2_1380x776.png 2x" data-dominant-color="CACACA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1962×1106 369 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Normally, it should behave like the following image that you can choose the output volume from your existing volume loaded. Only closing the 3D slicer app and reopen can solve the problem. But it means that I would lose my edited segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/245edf685d00a128ee8f36b3a6d91e6803118e4f.jpeg" data-download-href="/uploads/short-url/5bKs4hYGamO0cZ2AYP2fok1qCqH.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245edf685d00a128ee8f36b3a6d91e6803118e4f_2_690x388.jpeg" alt="3" data-base62-sha1="5bKs4hYGamO0cZ2AYP2fok1qCqH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245edf685d00a128ee8f36b3a6d91e6803118e4f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245edf685d00a128ee8f36b3a6d91e6803118e4f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245edf685d00a128ee8f36b3a6d91e6803118e4f_2_1380x776.jpeg 2x" data-dominant-color="828282"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1920×1082 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I do not know if this is a bug or my mis-use. Thank you</p>

---

## Post #2 by @cpinter (2022-03-31 15:51 UTC)

<p>The latest stable version is more than a year old. Can you please test it with the latest preview version? We only do fixes in the latest version and 5.0 stable will be released very soon. Thanks!</p>

---
