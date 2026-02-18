# Clear mask popup in segmentation

**Topic ID**: 22013
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/clear-mask-popup-in-segmentation/22013

---

## Post #1 by @Shahnawaz_Vora (2022-02-17 08:11 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.13</p>
<p>Actual behavior:<br>
Currently on right clicking and in menu select clear selected segments it will show pop up and prompt to user for clear the selected mask(Yes/No) .</p>
<p>Expected behavior:<br>
I want to disable the pop up shows up on clicking the (clear selected segments) menu  and clear selected mask directly without showing any pop.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9312c0dfef2c336871330cc1913928e19f04095.png" data-download-href="/uploads/short-url/qqhGktIeuMsMJZFXN9C561B68D3.png?dl=1" title="Screenshot (12)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9312c0dfef2c336871330cc1913928e19f04095_2_690x388.png" alt="Screenshot (12)" data-base62-sha1="qqhGktIeuMsMJZFXN9C561B68D3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9312c0dfef2c336871330cc1913928e19f04095_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9312c0dfef2c336871330cc1913928e19f04095_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9312c0dfef2c336871330cc1913928e19f04095_2_1380x776.png 2x" data-dominant-color="929398"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (12)</span><span class="informations">1920×1080 490 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7b07c18af0fe6d01aa529a8cfc272e0909703c6.png" data-download-href="/uploads/short-url/x3CpzGKqSOyVlszJvGG3VqK6ilU.png?dl=1" title="Screenshot (13)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b07c18af0fe6d01aa529a8cfc272e0909703c6_2_690x388.png" alt="Screenshot (13)" data-base62-sha1="x3CpzGKqSOyVlszJvGG3VqK6ilU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b07c18af0fe6d01aa529a8cfc272e0909703c6_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b07c18af0fe6d01aa529a8cfc272e0909703c6_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b07c18af0fe6d01aa529a8cfc272e0909703c6_2_1380x776.png 2x" data-dominant-color="97979D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (13)</span><span class="informations">1920×1080 465 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-02-18 04:26 UTC)

<p>We would need to understand why do you need to clear segments so often that this popup gets in the way. Can you tell a bit more about your use case?</p>

---

## Post #3 by @Dwij_Mistry (2022-02-18 04:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22013">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We would need to understand why do you need to clear segments so often</p>
</blockquote>
</aside>
<p>No, user will not use if often but whenever it required they can.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22013">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>that this popup gets in the way</p>
</blockquote>
</aside>
<p>This is creating an extra click for user that we are trying to eliminate.</p>

---

## Post #4 by @lassoan (2022-02-18 05:00 UTC)

<p>It would be better to address the root cause (not require the user to clear the segments in the first place), but if you don’t have any specific use case in mind and you are sure that it will be a problem for users then you can set <code>DontShowAgainVisible</code> to true and set a valid <code>DontShowAgainSettingsKey</code> on the popup.</p>

---
