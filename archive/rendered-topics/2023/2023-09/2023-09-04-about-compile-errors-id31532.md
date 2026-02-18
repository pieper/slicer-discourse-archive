# About compile errors

**Topic ID**: 31532
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/about-compile-errors/31532

---

## Post #1 by @iwangwangwang (2023-09-04 01:29 UTC)

<p>Hello!<br>
When I compiled the 3DSLICER source code, the following error occurred. How Do I fix it?</p>
<ol>
<li>
<p>Failed to clone repository:<br>
‘<a href="https://github.com/KitwareMedical/ITKMorphologicalContourInterpolation.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/ITKMorphologicalContourInterpolation: An implementation of morphological contour interpolation</a>’</p>
</li>
<li>
<p>By not providing “FindITK.cmake” in CMAKE_MODULE_PATH this project has<br>
asked CMake to find a package configuration file provided by “ITK”, but<br>
CMake did not find one.<br>
Could not find a package configuration file provided by “ITK” with any of<br>
the following names:<br>
ITKConfig.cmake<br>
itk-config.cmake</p>
</li>
<li>
<p>By not providing “FindCTK.cmake” in CMAKE_MODULE_PATH this project has<br>
asked CMake to find a package configuration file provided by “CTK”, but<br>
CMake did not find one.<br>
Could not find a package configuration file provided by “CTK” with any of<br>
the following names:<br>
CTKConfig.cmake<br>
ctk-config.cmake</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e95d8a0bf90af09844c3696add3b9cd36719eca0.png" data-download-href="/uploads/short-url/xirELwbuvhRqne3i6TvHu839eTK.png?dl=1" title="图片1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e95d8a0bf90af09844c3696add3b9cd36719eca0_2_690x175.png" alt="图片1" data-base62-sha1="xirELwbuvhRqne3i6TvHu839eTK" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e95d8a0bf90af09844c3696add3b9cd36719eca0_2_690x175.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e95d8a0bf90af09844c3696add3b9cd36719eca0_2_1035x262.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e95d8a0bf90af09844c3696add3b9cd36719eca0.png 2x" data-dominant-color="F4F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片1</span><span class="informations">1311×333 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @yulaomao (2023-09-04 03:35 UTC)

<aside class="quote no-group" data-username="iwangwangwang" data-post="1" data-topic="31532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/f1d935/48.png" class="avatar"> iwangwangwang:</div>
<blockquote>
<p>Failed to clone repository:<br>
‘<a href="https://github.com/KitwareMedical/ITKMorphologicalContourInterpolation.git" rel="noopener nofollow ugc">GitHub - KitwareMedical/ITKMorphologicalContourInterpolation: An implementation of morphological contour interpolation</a>’</p>
</blockquote>
</aside>
<p>Are you compiling in China? This is a network issue. If you are in China, you will need to configure a VPN.</p>

---

## Post #3 by @yulaomao (2023-09-04 03:36 UTC)

<p>The other issues are likely caused by the previous problem as well.</p>

---

## Post #4 by @iwangwangwang (2023-09-04 03:56 UTC)

<p>Yes, I have configured a VPN， but I found that some sub projects must require VPN, while others cannot use VPN, I cannot compile successfully at once, I am seeking a solution。</p>

---

## Post #5 by @yulaomao (2023-09-04 03:59 UTC)

<p>Simply enabling a VPN cannot solve the problem. You need to configure it separately for Git. When installing certain libraries in Python, you may need to turn off the VPN.</p>

---

## Post #7 by @iwangwangwang (2023-09-04 04:04 UTC)

<p>What you said is correct, so do I need to compile each sub project separately? or are there any other simple and feasible configuration methods?</p>

---

## Post #8 by @yulaomao (2023-09-04 05:44 UTC)

<p>You can search on Baidu for how to configure VPN for Git. Once you have done that, most of the download issues should be resolved. If you encounter failures with Python’s pip, it will typically display relevant error messages. When you see an error, try closing the VPN and retrying the process again.</p>

---

## Post #9 by @iwangwangwang (2023-09-04 06:32 UTC)

<p>I will try, thank you</p>

---
