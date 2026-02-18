# Grow from seeds problem

**Topic ID**: 10414
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/grow-from-seeds-problem/10414

---

## Post #1 by @rlazol (2020-02-24 15:00 UTC)

<p>Dear All,</p>
<p>we tried to segmentate the bones in an elephants’ limb using grow from seeds. My collague marked each bone extensively for a different segmentation using “paint” and then initiated the Grow from seeds. The result is attached. If we turn off all segments it still looks like this (there are no models).<br>
Can anybody help with this?</p>
<p>thank you<br>
Laci</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb8367e8b6a057c88f18e24c6d063369f37b9ab3.jpeg" data-download-href="/uploads/short-url/xBrJXT978u94HWEux1jqbQJxD0f.jpeg?dl=1" title="87790354_534289530543272_5392728582868959232_n" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb8367e8b6a057c88f18e24c6d063369f37b9ab3_2_666x500.jpeg" alt="87790354_534289530543272_5392728582868959232_n" data-base62-sha1="xBrJXT978u94HWEux1jqbQJxD0f" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb8367e8b6a057c88f18e24c6d063369f37b9ab3_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb8367e8b6a057c88f18e24c6d063369f37b9ab3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb8367e8b6a057c88f18e24c6d063369f37b9ab3.jpeg 2x" data-dominant-color="4E5761"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">87790354_534289530543272_5392728582868959232_n</span><span class="informations">912×684 86.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b299b81fd831842be87edebe70f11029e8c2000.jpeg" data-download-href="/uploads/short-url/aIUX8yxm8T3LiqLazlYyogLA5Wg.jpeg?dl=1" title="87492869_151826335847788_7622018202372931584_n" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b299b81fd831842be87edebe70f11029e8c2000_2_653x500.jpeg" alt="87492869_151826335847788_7622018202372931584_n" data-base62-sha1="aIUX8yxm8T3LiqLazlYyogLA5Wg" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b299b81fd831842be87edebe70f11029e8c2000_2_653x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b299b81fd831842be87edebe70f11029e8c2000_2_979x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b299b81fd831842be87edebe70f11029e8c2000.jpeg 2x" data-dominant-color="686A5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">87492869_151826335847788_7622018202372931584_n</span><span class="informations">1080×826 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-02-25 05:17 UTC)

<p>Try hardening all transforms on all nodes before starting registration and make sure to choose the correct master volume in Segment Editor. Also, test with latest Slicer Preview Release, too.</p>

---

## Post #3 by @rlazol (2020-02-26 08:54 UTC)

<p>Tnak you for you answer. I am really sorry but I do not really understand what you you mean by “hardening all transforms on all nodes” - can you please explain?<br>
thank you</p>

---

## Post #4 by @Amine (2020-02-26 12:20 UTC)

<p>Go in the “transform” module, select a transform from the list (if there is none then no need to worry about this), and select the nodes (volumes or segmentations, or anything) on the list at the right (transforms pending hardening). Select each one and hit the harden button under the lists</p>

---

## Post #6 by @rlazol (2020-02-26 17:37 UTC)

<p>Thank you, we will try it I well come back with the result <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
