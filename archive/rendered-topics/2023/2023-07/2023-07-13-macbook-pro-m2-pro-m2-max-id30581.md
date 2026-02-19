---
topic_id: 30581
title: "Macbook Pro M2 Pro M2 Max"
date: 2023-07-13
url: https://discourse.slicer.org/t/30581
---

# MacBook Pro M2 Pro/ M2 Max

**Topic ID**: 30581
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/macbook-pro-m2-pro-m2-max/30581

---

## Post #1 by @D11 (2023-07-13 12:07 UTC)

<p>Does the new MacBook Pro M2 Pro and MacBook Pro M2 Max meet the requirements to run 3D slicer smoothly?</p>
<p>I wanted to confirm that 3D slicer will be running smoothly before I buy a new Mac.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-07-13 13:11 UTC)

<p>Yes, it should work fine.  There have been some reports of slow startup the first time you run the app, but we aren’t sure why that is.  Once it’s running it seems fine but report if you run into any issues.  We still only provide the Intel binaries, but the native builds work and eventually we’ll make binaries available and they should work even better.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0db1e354f222b555f150a4534edf52aee26b423.jpeg" data-download-href="/uploads/short-url/w5apvVI1pRXn4lWUMF5xPtwTj7Z.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0db1e354f222b555f150a4534edf52aee26b423_2_690x447.jpeg" alt="image" data-base62-sha1="w5apvVI1pRXn4lWUMF5xPtwTj7Z" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0db1e354f222b555f150a4534edf52aee26b423_2_690x447.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0db1e354f222b555f150a4534edf52aee26b423_2_1035x670.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0db1e354f222b555f150a4534edf52aee26b423_2_1380x894.jpeg 2x" data-dominant-color="909195"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1246 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2023-07-13 13:33 UTC)

<p>There is the 3D Max texture limitation that <a class="mention" href="/u/fishguy">@Fishguy</a> has encountered.</p>
<aside class="quote quote-modified" data-post="3" data-topic="29152">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/gpu-and-cpu-rendering-on-macbookpro-m2-promax/29152/3">GPU and CPU rendering on MacBookPro M2 ProMax</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for sharing the data.  I could use GPU rendering on a mac pro, but on a mac book air m2 I got this error: 
[VTK] Invalid texture dimensions [447, 318, 2308]

[FD] UNSUPPORTED (log once): POSSIBLE ISSUE: unit 1 GLD_TEXTURE_INDEX_3D is unloadable and bound to sampler type (Float) - using zero texture because texture unloadable

so it must be a hardware or driver limit, probably to 2048 max dimension 
I used CropVolume with a 1.5x multiplier on the spacing and then GPU rendering worked on th…
  </blockquote>
</aside>


---
