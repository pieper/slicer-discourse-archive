# I have some rendering problem , i think i can't solve this by myself

**Topic ID**: 26405
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/i-have-some-rendering-problem-i-think-i-cant-solve-this-by-myself/26405

---

## Post #1 by @jay1987 (2022-11-23 12:00 UTC)

<p>the volumerendering of CT data in slicer is awesome ,the preset of CT-AAA looks below in both CPU Raycast and GPU Raycast<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9c71e3c0d0cbcf6c9a0cfe06b79dd1f33ee78dc.jpeg" alt="image" data-base62-sha1="v4ydCmuNBOrPNXGSSsxQRbQKR9G" width="333" height="272"></p>
<p>but when I copy the preset parameters to MITK , the CPU Ray cast like Slicer Effect,it’s good.and slow,<br>
but the GPU Version looks like below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5284a523e36548aea9a0144fc811e6b99c413e5c.jpeg" alt="image" data-base62-sha1="bLZlhPlDBs44kasJVFXYDRtRdog" width="528" height="456"></p>
<p>Slicer and MITK both use vtkGPUVolumeRayCastMapper as Render , But i don’t know that’s wrong in MITK .</p>

---

## Post #2 by @cpinter (2022-11-23 12:11 UTC)

<aside class="quote no-group" data-username="jay1987" data-post="1" data-topic="26405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jay1987/48/16183_2.png" class="avatar"> jay1987:</div>
<blockquote>
<p>i don’t know that’s wrong in MITK</p>
</blockquote>
</aside>
<p>To me this sounds like an issue for MITK, not Slicer.</p>

---

## Post #3 by @jay1987 (2022-11-23 13:24 UTC)

<p>that’s right Pinter<br>
sorry for me to find help from slicer community.<br>
the mitk community is  not active<br>
i think maybe someone here can find the difference between the  vtkGPUVolumeRayCastMapper</p>

---

## Post #4 by @pieper (2022-11-23 18:05 UTC)

<p>The rendering pipeline is more than just the question of which mapper is used, since there are many settings that influence the result.  You could print the mapper and renderer / render window settings in both programs to see what’s set differently.</p>

---

## Post #5 by @jay1987 (2022-11-24 00:51 UTC)

<p>thank you pieper<br>
it’s a good idea.</p>

---

## Post #6 by @lassoan (2022-12-01 06:17 UTC)

<p>I’m just curious, why would you consider using MITK instead of Slicer?</p>

---

## Post #7 by @jay1987 (2022-12-02 03:12 UTC)

<p>i don’t think MITK can instead of Slicer.<br>
I always think Slicer is the development trend in the future<br>
my company has an old project using MITK , and the project has been in use in some hospital .my leader do not understand programming,and wants me to Optimize this program<br>
finaly i find the reason why MITK rendering so strange,MITK use vtkLightKit instead of UseJittering , i change the rendering parameter from Slicer to MITK,it works</p>

---
