---
topic_id: 21235
title: "Otsu Segmentation On Head And Neck Pet Image"
date: 2021-12-27
url: https://discourse.slicer.org/t/21235
---

# Otsu segmentation on Head and Neck PET image

**Topic ID**: 21235
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/otsu-segmentation-on-head-and-neck-pet-image/21235

---

## Post #1 by @MPhilip (2021-12-27 12:22 UTC)

<p>Operating system: Windows 11 home<br>
Slicer version:Slicer 4.13.0-2021-12-22<br>
Is it advisable to use otsu method to segment tumour (marked in blue) on PET images? If it is possible, please guide me to the relevant resources (a tutorial preferably) on how to apply the otsu method to this image. I tried otsu method, but not sure whether I did it right.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/145b87c85f58d435fadba13eb71b9c064cb11e6b.png" alt="image" data-base62-sha1="2U5ErMALR5Rf66uUlspH6S08J2X" width="591" height="387"></p>
<p>If there are any other methods that would work on this image please suggest that too pointing to relevant documents.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-12-27 12:52 UTC)

<p>Otsu threshold is not typically used for this. 40-43% of maximum SUV value is used instead. There have been a few discussions about this, for example:</p>
<aside class="quote quote-modified" data-post="6" data-topic="16629">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-from-curved-plane-by-markup-points/16629/6">Segmentation from curved plane by markup points</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    For the first question is this something like what you are building <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> ? 
Regarding your second question, that’s a mode I also want to implement for a PET project I’m involved with.  Probably it can just be a simple segment editor effect that would be used as follows: use the Paint (or any tool) to draw anything that is possibly lesion and then the effect would calculate the max value of the background in that segment and then only keep the places where the background are 41% of that…
  </blockquote>
</aside>


---
