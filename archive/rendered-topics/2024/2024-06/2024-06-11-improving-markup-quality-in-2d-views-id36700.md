---
topic_id: 36700
title: "Improving Markup Quality In 2D Views"
date: 2024-06-11
url: https://discourse.slicer.org/t/36700
---

# Improving Markup Quality in 2D Views

**Topic ID**: 36700
**Date**: 2024-06-11
**URL**: https://discourse.slicer.org/t/improving-markup-quality-in-2d-views/36700

---

## Post #1 by @park (2024-06-11 14:42 UTC)

<p>Hi all</p>
<p>Is there a way to improve the markup quality as seen on the right side of the image? (It doesn’t necessarily have to look like 3D.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/237ef8668d2b3229e931e681d35b66d47b5a22ea.gif" data-download-href="/uploads/short-url/540K8modmzNp940H1Kqb9DUpb8S.gif?dl=1" title="스크린샷 2024-06-11 오후 11.28.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/237ef8668d2b3229e931e681d35b66d47b5a22ea_2_690x268.gif" alt="스크린샷 2024-06-11 오후 11.28.46" data-base62-sha1="540K8modmzNp940H1Kqb9DUpb8S" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/237ef8668d2b3229e931e681d35b66d47b5a22ea_2_690x268.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/237ef8668d2b3229e931e681d35b66d47b5a22ea_2_1035x402.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/237ef8668d2b3229e931e681d35b66d47b5a22ea_2_1380x536.gif 2x" data-dominant-color="484747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2024-06-11 오후 11.28.46</span><span class="informations">1593×621 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Morever, I’d like to enhance the quality of lines and curves, particularly addressing artifacts like stair-stepping in both markup curves and diagonal lines in the 2D view.</p>

---

## Post #2 by @lassoan (2024-06-11 16:36 UTC)

<p>You can enable interpolation, for example MSAA or FXAA.</p>
<p>MSAA interpolation can be enabled in application settings / Views / Multi-sampling (MSAA) → 4x (or higher for smoother results with higher computation cost).</p>
<p>FXAA can be enabled with a short Python code snippet. See example in the image below: left with FXAA, right without interpolation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/508f7a50adcafc60be2b32ab9e6c02db3ec7f16b.jpeg" data-download-href="/uploads/short-url/buFB2mYVPglaJjBg3vijVuBfcTh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508f7a50adcafc60be2b32ab9e6c02db3ec7f16b_2_690x197.jpeg" alt="image" data-base62-sha1="buFB2mYVPglaJjBg3vijVuBfcTh" width="690" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508f7a50adcafc60be2b32ab9e6c02db3ec7f16b_2_690x197.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508f7a50adcafc60be2b32ab9e6c02db3ec7f16b_2_1035x295.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508f7a50adcafc60be2b32ab9e6c02db3ec7f16b_2_1380x394.jpeg 2x" data-dominant-color="6E6666"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1798×515 63.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See in this topic how to enable FXAA and some more information on interpolation:</p>
<aside class="quote quote-modified" data-post="4" data-topic="21140">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/antialiasing-in-in-slice-mpr-views/21140/4">Antialiasing in in slice (MPR) views</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Multi-sampling is the true antialiasing method, but that would mess with the Z buffer, and therefore with hardware-accelerated picking that is used for markup nodes label display and control point manipulation, compositing volume rendering and surface rendering, etc. Also as <a class="mention" href="/u/pieper">@pieper</a> mentioned there seem to be some some issues with it in recent VTK and Qt versions (for example, I don’t think the MSAA setting has any effect right now on Windows). 
Alternatively, you can do screen-space antialiasin…
  </blockquote>
</aside>


---
