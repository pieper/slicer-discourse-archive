# I want to branch extract(remove)

**Topic ID**: 37001
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/i-want-to-branch-extract-remove/37001

---

## Post #1 by @Seokjun_Hwang (2024-06-25 08:26 UTC)

<p>I am using Python and would like to remove the short branches from the aorta in the image below. My goal is to obtain a clean, tubular representation of the aorta. The purpose is to eliminate noise in order to calculate the cross-sectional area of the aorta in the Python code. Below is the current implementation, which includes the centerline and curved lines.</p>
<p>As far as I know, the branch clipper module is not yet available for implementation in Python. What extensions or libraries would you recommend for this task? Any guidance on the methods to achieve this would be greatly appreciated.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d22e7c3c9ca0315fdcf5b506e7b266cf939cae.png" alt="image" data-base62-sha1="3xzLOHTo7qHXV1QjTEt3gyy59T0" width="352" height="420"></p>

---

## Post #2 by @chir.set (2024-06-25 08:54 UTC)

<aside class="quote no-group" data-username="Seokjun_Hwang" data-post="1" data-topic="37001">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seokjun_hwang/48/76745_2.png" class="avatar"> Seokjun_Hwang:</div>
<blockquote>
<p>the branch clipper module is not yet available for implementation in Python</p>
</blockquote>
</aside>
<p>You may instantiate the logic of any loadable module very simply in Python. In this case:</p>
<blockquote>
<p>l = slicer.modules.branchclipper.logic()</p>
</blockquote>
<aside class="quote no-group" data-username="Seokjun_Hwang" data-post="1" data-topic="37001">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seokjun_hwang/48/76745_2.png" class="avatar"> Seokjun_Hwang:</div>
<blockquote>
<p>What extensions or libraries would you recommend for this task?</p>
</blockquote>
</aside>
<p>Check the ‘Guided artery segmentation’ module of SlicerVMTK. It can output a result like below:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca204214f6b5b36b2bbce0dcceadcaae56869d73.png" alt="aorta_arch_clean" data-base62-sha1="sQ5yPpheklFkQHFE0sfeBTW6E4b" width="384" height="468"></p>

---

## Post #3 by @ilovedogsColonD (2024-07-08 03:10 UTC)

<p>Hey did you ever figure out how to do this?</p>

---
