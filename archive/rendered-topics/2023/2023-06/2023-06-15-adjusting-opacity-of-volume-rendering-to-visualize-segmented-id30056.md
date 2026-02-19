---
topic_id: 30056
title: "Adjusting Opacity Of Volume Rendering To Visualize Segmented"
date: 2023-06-15
url: https://discourse.slicer.org/t/30056
---

# Adjusting Opacity of Volume Rendering to Visualize Segmented Lesions

**Topic ID**: 30056
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/adjusting-opacity-of-volume-rendering-to-visualize-segmented-lesions/30056

---

## Post #1 by @yanpfei (2023-06-15 18:27 UTC)

<p>I performed volume rendering on a volume from a CT scan.<br>
I segmented the lesions within the said volume. Now, I have displayed both parts of the content in a 3D window.<br>
However, the content of the volume rendering overlays the segmented content, preventing me from seeing the relative position of the segmented lesion with the head (as seen in Figure 1).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fb65c95cd7e6e047bd6e8e6d914caaeb9b248fb.png" data-download-href="/uploads/short-url/mMSCNNqsORJDzTvVhP0mg6wjODp.png?dl=1" title="Fig1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fb65c95cd7e6e047bd6e8e6d914caaeb9b248fb_2_546x500.png" alt="Fig1" data-base62-sha1="mMSCNNqsORJDzTvVhP0mg6wjODp" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fb65c95cd7e6e047bd6e8e6d914caaeb9b248fb_2_546x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fb65c95cd7e6e047bd6e8e6d914caaeb9b248fb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fb65c95cd7e6e047bd6e8e6d914caaeb9b248fb.png 2x" data-dominant-color="A39DB6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig1</span><span class="informations">629×575 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am wondering if there is a way to adjust the opacity of the entire volume rendering so that I can visualize the segmented content.<br>
I have been able to achieve this effect with other software, such as MRIcroGL (as shown in Figure 2).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/359e6722a51ba6c57e011dad71385963d013ba11.png" data-download-href="/uploads/short-url/7EkGjCgQQDENMmUcHCtP7Y6sbf3.png?dl=1" title="Fig2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/359e6722a51ba6c57e011dad71385963d013ba11_2_392x500.png" alt="Fig2" data-base62-sha1="7EkGjCgQQDENMmUcHCtP7Y6sbf3" width="392" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/359e6722a51ba6c57e011dad71385963d013ba11_2_392x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/359e6722a51ba6c57e011dad71385963d013ba11_2_588x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/359e6722a51ba6c57e011dad71385963d013ba11.png 2x" data-dominant-color="624D37"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig2</span><span class="informations">641×817 339 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2023-06-15 20:05 UTC)

<aside class="quote no-group" data-username="yanpfei" data-post="1" data-topic="30056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yanpfei/48/6954_2.png" class="avatar"> yanpfei:</div>
<blockquote>
<p>adjust the opacity of the entire volume rendering</p>
</blockquote>
</aside>
<p>Yes, you can via the Scalar Opacity maps. Please read the Volume Rendering section of the user documentation.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html</a></p>

---

## Post #3 by @lassoan (2023-06-16 13:55 UTC)

<p>Another approach is not to waste computational resources and limit your rendering options by using volume rendering for displaying the skin surface. Instead, you can <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">segment the skin surface using simple thresholding Warp solidify effect</a>. You can then adjust the opacity of the skin surface segment to make the lesion in the brain visible.</p>

---
