# Would Slicer Volume Rendering improve by using other interpolation functions?

**Topic ID**: 28328
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/would-slicer-volume-rendering-improve-by-using-other-interpolation-functions/28328

---

## Post #1 by @mau_igna_06 (2023-03-12 13:44 UTC)

<p>Here is a short video that showcases different interpolation functions:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="YJB1QnEmlTs" data-video-title="An In-Depth look at Lerp, Smoothstep, and Shaping Functions" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=YJB1QnEmlTs" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/YJB1QnEmlTs/maxresdefault.jpg" title="An In-Depth look at Lerp, Smoothstep, and Shaping Functions" width="" height="">
  </a>
</div>

<p>Could this be used for transfer functions of opacity or colormapping?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-03-13 14:29 UTC)

<p>Using higher-order interpolation for the transfer function control points would allow us to specify smooth transfer functions with less points. However, this would require comsiderable effort to implement and I’m not sure if the difference would be very noticeable. Have you analyzed the difference in appearance between using piecewise linear and smooth functions (e.g., a linear ramp and a smooth sigmoid function)?</p>

---

## Post #3 by @mau_igna_06 (2023-03-13 21:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="28328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you analyzed the difference in appearance between using piecewise linear and smooth functions (e.g., a linear ramp and a smooth sigmoid function)?</p>
</blockquote>
</aside>
<p>Maybe I’ll test next weekend and share my results about it</p>

---
