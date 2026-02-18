# How to move the Slicer View origin to the model's center?

**Topic ID**: 19928
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/how-to-move-the-slicer-view-origin-to-the-models-center/19928

---

## Post #1 by @slicer365 (2021-09-30 10:32 UTC)

<p>As we know ，In the Blender software, there is a function to move the geometric center to the origin and move the origin to the geometric center.</p>
<p>Is there a way to implement this function in Slicer?</p>
<p>If I use the Creat models module to creat a sphere ,is the centre of the sphere the origin ?</p>
<p>Thanks for any answer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/905e9ef2e15049d3855c5b10d92a2e8f22c21315.png" data-download-href="/uploads/short-url/kB9tLp70vcdKHCiHQlfdbf6UQOF.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905e9ef2e15049d3855c5b10d92a2e8f22c21315_2_517x265.png" alt="捕获" data-base62-sha1="kB9tLp70vcdKHCiHQlfdbf6UQOF" width="517" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905e9ef2e15049d3855c5b10d92a2e8f22c21315_2_517x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905e9ef2e15049d3855c5b10d92a2e8f22c21315_2_775x397.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905e9ef2e15049d3855c5b10d92a2e8f22c21315_2_1034x530.png 2x" data-dominant-color="DCDCF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1407×722 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pll_llq (2021-09-30 13:34 UTC)

<p>You might be looking for the “Center 3D View” button</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view</a></p>

---

## Post #3 by @slicer365 (2021-09-30 15:26 UTC)

<p>Thank you for your answer.</p>
<p>Actually I am trying to find out the whole 3D view’s origin ,not the visible 3D view’s centre.</p>

---

## Post #4 by @pll_llq (2021-09-30 15:28 UTC)

<p>Can you explain your use case a bit more?</p>

---

## Post #5 by @lassoan (2021-09-30 16:01 UTC)

<p>The 3D view’s origin is always at (0,0,0) in the renderer coordinate system (also known as RAS or World coordinate system).</p>

---

## Post #6 by @slicer365 (2021-09-30 22:56 UTC)

<p>When I use Transform module to rotate a model ,</p>
<p>I want it rotate along a fixed point ,</p>
<p>I know the point is the 3D View’s origin.</p>
<p>For example , a puncture tube for brain hemorrhage,</p>
<p>after I fixed one end ,I can use Transform module to rotate the other end anyway  so that find a better path .</p>

---

## Post #7 by @lassoan (2021-10-01 00:12 UTC)

<p>See how to rotate a model around an arbitrary point here:</p>
<aside class="quote" data-post="2" data-topic="16846">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/rotate-model-around-specific-point/16846/2">Rotate model around specific point</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Maybe this is what you looking for ? 
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point</a> 
And video made by Prof Lasso 
<a href="https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd" class="onebox" target="_blank" rel="noopener">https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd</a>
  </blockquote>
</aside>


---
