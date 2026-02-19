---
topic_id: 25291
title: "Modify Slicer Default Home Module And Slicer Default Favorit"
date: 2022-09-16
url: https://discourse.slicer.org/t/25291
---

# Modify Slicer_DEFAULT_HOME_MODULE and Slicer_DEFAULT_FAVORITE_MODULES

**Topic ID**: 25291
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/modify-slicer-default-home-module-and-slicer-default-favorite-modules/25291

---

## Post #1 by @miniminic (2022-09-16 05:02 UTC)

<p>I wanted to change the default module and the default favorite module. I changed the two macros and deleted the slicer.ini file<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/606a08df316b05c4c871e44b8f2625f93cf77f44.jpeg" data-download-href="/uploads/short-url/dKV0X3W7zOFDkLkzv36YwhDyzac.jpeg?dl=1" title="屏幕截图 2022-09-13 114936" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606a08df316b05c4c871e44b8f2625f93cf77f44_2_690x177.jpeg" alt="屏幕截图 2022-09-13 114936" data-base62-sha1="dKV0X3W7zOFDkLkzv36YwhDyzac" width="690" height="177" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606a08df316b05c4c871e44b8f2625f93cf77f44_2_690x177.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606a08df316b05c4c871e44b8f2625f93cf77f44_2_1035x265.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/606a08df316b05c4c871e44b8f2625f93cf77f44.jpeg 2x" data-dominant-color="242524"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-09-13 114936</span><span class="informations">1088×280 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Somewhere else is the vtkslicerconfigure.h file rewritten<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78852346cc8b2a531bf9b8a449b4bcd64b4720c7.jpeg" data-download-href="/uploads/short-url/hcaxENNfgEeC3A3A85KOXUpEgTB.jpeg?dl=1" title="屏幕截图 2022-09-16 125815" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78852346cc8b2a531bf9b8a449b4bcd64b4720c7_2_690x75.jpeg" alt="屏幕截图 2022-09-16 125815" data-base62-sha1="hcaxENNfgEeC3A3A85KOXUpEgTB" width="690" height="75" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78852346cc8b2a531bf9b8a449b4bcd64b4720c7_2_690x75.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78852346cc8b2a531bf9b8a449b4bcd64b4720c7_2_1035x112.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78852346cc8b2a531bf9b8a449b4bcd64b4720c7.jpeg 2x" data-dominant-color="282728"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-09-16 125815</span><span class="informations">1122×122 30 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-09-16 05:26 UTC)

<p>You need to change these variables in CMake and then configure and build Slicer. The .h header file content is generated automatically from the CMake variables, so any changes that you make in them may be overwritten at the next build.</p>

---

## Post #3 by @miniminic (2022-09-16 05:30 UTC)

<p>Is this the file<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b57b995afb7954356c5d8c5c35f3e11a8c04bd.jpeg" data-download-href="/uploads/short-url/dNwF3PGRT5xCLT8x0rT0R17ydFr.jpeg?dl=1" title="屏幕截图 2022-09-16 132854" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b57b995afb7954356c5d8c5c35f3e11a8c04bd_2_690x446.jpeg" alt="屏幕截图 2022-09-16 132854" data-base62-sha1="dNwF3PGRT5xCLT8x0rT0R17ydFr" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b57b995afb7954356c5d8c5c35f3e11a8c04bd_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b57b995afb7954356c5d8c5c35f3e11a8c04bd_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b57b995afb7954356c5d8c5c35f3e11a8c04bd.jpeg 2x" data-dominant-color="F2F3F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-09-16 132854</span><span class="informations">1245×805 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I rebuilt slicer, but it didn’t seem to work</p>

---

## Post #4 by @lassoan (2022-09-16 05:40 UTC)

<p>You can set CMake variables when you configure the project in CMake (either using the GUI or by using <code>-Dname:type=value</code> command-line arguments).</p>

---

## Post #5 by @miniminic (2022-09-16 05:43 UTC)

<p>Okay, I know what to do thank you</p>

---
