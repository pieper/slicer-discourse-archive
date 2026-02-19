---
topic_id: 41833
title: "Compile And Run Slicer In Vs2022 And The Prompt Access Denie"
date: 2025-02-22
url: https://discourse.slicer.org/t/41833
---

# Compile and run slicer in vs2022, and the prompt “Access Denied” appears

**Topic ID**: 41833
**Date**: 2025-02-22
**URL**: https://discourse.slicer.org/t/compile-and-run-slicer-in-vs2022-and-the-prompt-access-denied-appears/41833

---

## Post #1 by @zhuofalin (2025-02-22 21:07 UTC)

<p>I compiled slicer on two windows (one is win10 and the other is win11). At that time, I could compile and run slicer normally using vs2022. However, after a few days, when I compiled and ran slicer again, it prompted access denied. What’s going on? Note: The operating environment has not changed.</p>

---

## Post #2 by @cpinter (2025-02-25 12:14 UTC)

<p>Do you have any other thing to show? The exact error message, a full log? Thanks!</p>

---

## Post #3 by @zhuofalin (2025-02-25 14:22 UTC)

<p>Sorry for the late reply. This mainly prompts the following error screenshot, but I haven’t found the log yet. Whether it is compiled by cmake or ninja, this error is reported when compiled in vs2022.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fc0b28d0feba9c3f5b2526017c1ce40cd09a1f.jpeg" data-download-href="/uploads/short-url/e7ENak7w1UVX760JIsbUyq9euCj.jpeg?dl=1" title="屏幕截图 2025-02-25 211134" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62fc0b28d0feba9c3f5b2526017c1ce40cd09a1f_2_690x462.jpeg" alt="屏幕截图 2025-02-25 211134" data-base62-sha1="e7ENak7w1UVX760JIsbUyq9euCj" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62fc0b28d0feba9c3f5b2526017c1ce40cd09a1f_2_690x462.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62fc0b28d0feba9c3f5b2526017c1ce40cd09a1f_2_1035x693.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fc0b28d0feba9c3f5b2526017c1ce40cd09a1f.jpeg 2x" data-dominant-color="393839"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2025-02-25 211134</span><span class="informations">1162×779 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d96b892cb01085c027cef98ea237b7669f260ec1.jpeg" data-download-href="/uploads/short-url/v1o0lmDWqJJmG6lgO2TjSJO0eNH.jpeg?dl=1" title="屏幕截图 2025-02-25 222151" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d96b892cb01085c027cef98ea237b7669f260ec1_2_690x462.jpeg" alt="屏幕截图 2025-02-25 222151" data-base62-sha1="v1o0lmDWqJJmG6lgO2TjSJO0eNH" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d96b892cb01085c027cef98ea237b7669f260ec1_2_690x462.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d96b892cb01085c027cef98ea237b7669f260ec1_2_1035x693.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d96b892cb01085c027cef98ea237b7669f260ec1_2_1380x924.jpeg 2x" data-dominant-color="353536"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2025-02-25 222151</span><span class="informations">1518×1017 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have tried running vs2022 as an administrator and then running slicer in debug, or changing the folder properties to no longer read-only, but the problem cannot be solved.</p>

---

## Post #4 by @cpinter (2025-02-25 14:41 UTC)

<p>It seems that you forgot to specify the startup project, and probably the executable as well</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cef3f06e4316cd9b172f417f6079c1807af863f.png" data-download-href="/uploads/short-url/moj4dq1dta4NFZGSHId2S2T8Cdh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cef3f06e4316cd9b172f417f6079c1807af863f.png" alt="image" data-base62-sha1="moj4dq1dta4NFZGSHId2S2T8Cdh" width="523" height="452"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">523×452 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9101a2b4f51fe6238a42c708ce272271b75aa64a.png" data-download-href="/uploads/short-url/kGMJICMuRmT9quwMBZ0wdjydDS2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9101a2b4f51fe6238a42c708ce272271b75aa64a.png" alt="image" data-base62-sha1="kGMJICMuRmT9quwMBZ0wdjydDS2" width="690" height="222" data-dominant-color="EAECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">778×251 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is explained here btw<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html</a></p>

---
