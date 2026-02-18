# Mask scalar volume vs masking within the registration

**Topic ID**: 7835
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/mask-scalar-volume-vs-masking-within-the-registration/7835

---

## Post #1 by @labixin (2019-08-01 09:20 UTC)

<p>Hi everyone,</p>
<p>I am now using Slicer 4.11.0 and want to register pre-surgical CT to post-surgical CT (breast). The two images were acquired using different CT table (curved vs flat), and there are some metal markers on the breast skin in post-surgical CT (shown below).</p>
<p>I know from FAQ manual (<a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ#Masking" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.10/FAQ - Slicer Wiki</a>) that masking is a powerful tool and I want to use it in my registration. But I am not sure about the difference between “mask scalar volume” and “masking within the registration”.</p>
<p>If I just mask the breast region in registration, can the unexpected misleading effect of markers and CT table be well handled? (I am not quite certain about “This does not mean that the rest is not registered, but rather that it moves along passively, i.e. areas outside the mask do not actively contribute to the cost function that determines the quality of the match.”) Or do I need to mask these relatively high intensity regions and set them to background value (-1024)?</p>
<p>Which one would be more reasonable? Hope for some advice, thanks a lot!</p>
<p>Crayon</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f61a35d95a0577e57473cc5e9bb49b0bf4cc56c9.jpeg" data-download-href="/uploads/short-url/z77C0UO4e89PnEc89fQQzZVufMJ.jpeg?dl=1" title="masking" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f61a35d95a0577e57473cc5e9bb49b0bf4cc56c9_2_334x500.jpeg" alt="masking" data-base62-sha1="z77C0UO4e89PnEc89fQQzZVufMJ" width="334" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f61a35d95a0577e57473cc5e9bb49b0bf4cc56c9_2_334x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f61a35d95a0577e57473cc5e9bb49b0bf4cc56c9_2_501x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f61a35d95a0577e57473cc5e9bb49b0bf4cc56c9_2_668x1000.jpeg 2x" data-dominant-color="242220"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">masking</span><span class="informations">886×1326 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-08-05 21:10 UTC)

<p>This post should clarify:</p>
<aside class="quote quote-modified" data-post="9" data-topic="7808">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/mask-volume-segment-editor/7808/9">Mask volume- segment editor</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    To keep things simple, make the segment cover the region you are interested in. Then, you can us Mask volume effect to blank out the parts outside your region of interest. 

Yes, this is correct. All effects (Scissors, Surface cut, Paint, etc.) only modify segments. They will not modify any volume nodes. 

If you blank out a region of a volume, Elastix will still take those voxels into account. This is probably not what you want. 
To make Elastix ignore certain regions then you can specify mask…
  </blockquote>
</aside>


---

## Post #3 by @labixin (2019-08-06 02:46 UTC)

<p>I will try the methods mentioned in this post. Thank you very much!</p>
<p>Crayon</p>

---
