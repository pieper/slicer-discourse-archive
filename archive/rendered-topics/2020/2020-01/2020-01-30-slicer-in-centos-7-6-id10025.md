---
topic_id: 10025
title: "Slicer In Centos 7 6"
date: 2020-01-30
url: https://discourse.slicer.org/t/10025
---

# Slicer in CentOS 7.6

**Topic ID**: 10025
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/slicer-in-centos-7-6/10025

---

## Post #1 by @muntahi398 (2020-01-30 13:44 UTC)

<p>Operating system: CentOS 7.6<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior: Data is not shown</p>
<p>Dear people,<br>
In a server computer running CentOS 7.6, I installed Slicer1.11.0 and downloaded sample model of CTchest.<br>
I can see its loaded. But in the 3 axis viewer I cant see the images.  All extention installtion seems to work fine. Is this  any graphics issue?  how  to resolve?</p>
<p>Attached an screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c314b6f32af5a608bc7f27767abe57a06702566.png" data-download-href="/uploads/short-url/41oYUKLsggjXkHWyfFMWjCDx2oC.png?dl=1" title="Slicer_centos" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c314b6f32af5a608bc7f27767abe57a06702566_2_690x333.png" alt="Slicer_centos" data-base62-sha1="41oYUKLsggjXkHWyfFMWjCDx2oC" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c314b6f32af5a608bc7f27767abe57a06702566_2_690x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c314b6f32af5a608bc7f27767abe57a06702566_2_1035x499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c314b6f32af5a608bc7f27767abe57a06702566_2_1380x666.png 2x" data-dominant-color="5D5E5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_centos</span><span class="informations">1792×865 79.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sam_Horvath (2020-01-30 14:38 UTC)

<p>Hi!</p>
<p>This is likely a graphics issue. Could you send the error log (View-&gt;ErrorLog  on the toolbar)?</p>
<p>Sam</p>

---

## Post #3 by @lassoan (2020-01-30 14:56 UTC)

<p>Do you have multiple monitors connected? What are their resolutions?</p>
<p>You may try to adjust screen scaling by adjusting environment variables - see <a href="https://discourse.slicer.org/t/strange-window-layout/7301/9" class="inline-onebox">Strange Window Layout</a>.</p>

---

## Post #4 by @muntahi398 (2020-01-30 15:31 UTC)

<p>It shows couldnt find compatible OpenGL .<br>
I checked in the system, it has OpenGL version string: 2.1 Mesa 18.0.5. Slicer needs 3.2 at least.</p>
<p>It is a remote server PC mostly used for simulation with its many cores. and mostly system is not in my control.<br>
So there is no hope running Slicer in this case?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31825f277541692688a7655270d826cd23fdf344.png" data-download-href="/uploads/short-url/73YIoLWXe9X7N5UZUnB0rFwtyx6.png?dl=1" title="install_problem1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31825f277541692688a7655270d826cd23fdf344_2_690x369.png" alt="install_problem1" data-base62-sha1="73YIoLWXe9X7N5UZUnB0rFwtyx6" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31825f277541692688a7655270d826cd23fdf344_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31825f277541692688a7655270d826cd23fdf344_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31825f277541692688a7655270d826cd23fdf344_2_1380x738.png 2x" data-dominant-color="E7ECF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">install_problem1</span><span class="informations">1862×998 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
