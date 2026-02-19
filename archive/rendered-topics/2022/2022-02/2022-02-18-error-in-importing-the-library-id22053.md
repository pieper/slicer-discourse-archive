---
topic_id: 22053
title: "Error In Importing The Library"
date: 2022-02-18
url: https://discourse.slicer.org/t/22053
---

# Error in importing the library

**Topic ID**: 22053
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/error-in-importing-the-library/22053

---

## Post #1 by @user5 (2022-02-18 17:32 UTC)

<p>Sorry that it is my first time to do the project based programming.</p>
<p>I have tried to import library into visual studio for programming .</p>
<p>I follow the tutorial in internet and I imported the VTK modules successfully, but some header file still can not be import, such as vtkMRMLApplicationLogic.h, vtkMRMLScene.h, vtkMRMLModelNode.h which is in the slicer master library.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24dd383754118a9cf0125d7b1b9bb5a1988ec5fc.png" data-download-href="/uploads/short-url/5g79hz4PKkP1Pfe2W1cgtfPpeck.png?dl=1" title="1234" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24dd383754118a9cf0125d7b1b9bb5a1988ec5fc_2_690x371.png" alt="1234" data-base62-sha1="5g79hz4PKkP1Pfe2W1cgtfPpeck" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24dd383754118a9cf0125d7b1b9bb5a1988ec5fc_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24dd383754118a9cf0125d7b1b9bb5a1988ec5fc_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24dd383754118a9cf0125d7b1b9bb5a1988ec5fc_2_1380x742.png 2x" data-dominant-color="EAECEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1234</span><span class="informations">2560×1379 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I try to use the library directories or import directly, but both method are failed.</p>
<p>Is it have any other way to import the header file?</p>

---

## Post #2 by @lassoan (2022-02-18 17:43 UTC)

<p>To get started, I would recommend to follow the existing modules as examples or use the <a href="https://github.com/Slicer/Slicer/tree/master/Utilities/Templates">templates</a>.</p>

---

## Post #3 by @user5 (2022-02-18 18:16 UTC)

<p>Sorry, I do not quite understand your meaning.</p>
<p>Is it mean that I just need to modify in existing extension file?</p>

---

## Post #4 by @lassoan (2022-02-18 18:19 UTC)

<p>Yes, first study existing extensions, understand how they work, make small modifications to them. Once you are confident you can start creating new modules.</p>

---

## Post #5 by @user5 (2022-02-18 18:27 UTC)

<p>I have already modified the extensions code, but it needs to export to be .pyd file.</p>
<p>Following the tutorial in internet, I need to build the project successfully first. But some header file which is mention in question cannot be included. It makes cannot able to build project sucessfully.</p>

---

## Post #6 by @lassoan (2022-02-18 18:35 UTC)

<p>You can start with just building an existing extension without any modification. If you have problems with that then let us know what the exact error message is and we should be able to help.</p>

---

## Post #7 by @user5 (2022-02-18 18:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebd695b91dcc8c6301603369e0ac56b73953f39a.png" data-download-href="/uploads/short-url/xEjWZwsKLTEqltHQtksvwhAu0oq.png?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebd695b91dcc8c6301603369e0ac56b73953f39a_2_690x348.png" alt="12" data-base62-sha1="xEjWZwsKLTEqltHQtksvwhAu0oq" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebd695b91dcc8c6301603369e0ac56b73953f39a_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebd695b91dcc8c6301603369e0ac56b73953f39a_2_1035x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebd695b91dcc8c6301603369e0ac56b73953f39a_2_1380x696.png 2x" data-dominant-color="EEEFF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">2557×1293 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
It still come out same error.</p>

---

## Post #8 by @lassoan (2022-02-18 23:58 UTC)

<p>Have you followed <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows">these instructions</a>?</p>

---

## Post #9 by @user5 (2022-02-19 04:57 UTC)

<p>No, I just open the .cxx file directly.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="22053">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows" rel="noopener nofollow ugc">these instructions</a></p>
</blockquote>
</aside>
<p>I will try to use it to build the project again.<br>
Thanks for your help.</p>

---
