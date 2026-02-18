# There seems to be a problem with the display of the progress bar

**Topic ID**: 25796
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/there-seems-to-be-a-problem-with-the-display-of-the-progress-bar/25796

---

## Post #1 by @wojiazaiyugang (2022-10-20 05:25 UTC)

<p>slicer version:  Slicer-5.1.0-2022-10-18-linux-amd64<br>
When loading data, the progress bar just shows, but there is no content. slicer.util.MessageDialog has the same problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/561f29e39a9b28242deeb48404699f29f0e4ccbe.png" data-download-href="/uploads/short-url/chRPtoalRaFdH3mLcwuowmNMC5w.png?dl=1" title="2022-10-20_11-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/561f29e39a9b28242deeb48404699f29f0e4ccbe_2_690x408.png" alt="2022-10-20_11-11" data-base62-sha1="chRPtoalRaFdH3mLcwuowmNMC5w" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/561f29e39a9b28242deeb48404699f29f0e4ccbe_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/561f29e39a9b28242deeb48404699f29f0e4ccbe_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/561f29e39a9b28242deeb48404699f29f0e4ccbe.png 2x" data-dominant-color="767575"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-10-20_11-11</span><span class="informations">1269×751 23.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @wojiazaiyugang (2022-10-20 07:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82b314733b27afe2de2ad5e847cf4b72aab476c9.png" data-download-href="/uploads/short-url/iEdKnsAWnP4riv3T8OBIZ2fj79D.png?dl=1" title="2022-10-20_11-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b314733b27afe2de2ad5e847cf4b72aab476c9_2_690x468.png" alt="2022-10-20_11-38" data-base62-sha1="iEdKnsAWnP4riv3T8OBIZ2fj79D" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b314733b27afe2de2ad5e847cf4b72aab476c9_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b314733b27afe2de2ad5e847cf4b72aab476c9_2_1035x702.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82b314733b27afe2de2ad5e847cf4b72aab476c9.png 2x" data-dominant-color="9B9090"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-10-20_11-38</span><span class="informations">1085×737 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2022-10-20 13:15 UTC)

<p>This doesn’t happen on other systems, so please add details about what OS, window system, etc you are seeing this on.</p>

---

## Post #4 by @lassoan (2022-10-20 14:43 UTC)

<p>It looks like an issue with the graphics driver or compositor. Try to upgrade your driver (or switch to a different one) and restart your computer. You can also try to disable wayland (if you use it).</p>

---

## Post #5 by @pranjal.sahu (2022-12-23 21:42 UTC)

<p>Getting a similar issue when using MessageDialog in the Ubuntu system. The text message is not getting displayed.</p>

---

## Post #6 by @lassoan (2022-12-24 02:08 UTC)

<p>Are you using Wayland?</p>

---

## Post #7 by @pranjal.sahu (2022-12-24 21:44 UTC)

<p>No, on printing the $XDG_SESSION_TYPE variable I get x11.</p>

---
