---
topic_id: 15674
title: "Build Slicer Failed On Win10"
date: 2021-01-26
url: https://discourse.slicer.org/t/15674
---

# Build Slicer failed on win10

**Topic ID**: 15674
**Date**: 2021-01-26
**URL**: https://discourse.slicer.org/t/build-slicer-failed-on-win10/15674

---

## Post #1 by @kejuhn (2021-01-26 08:24 UTC)

<p>Hi,</p>
<p>I followed the Build Instructions to build Slicer on Windows 10.<br>
CMake: 3.19.3<br>
Git: 2.30.0.2<br>
Qt: 5.15.2 64-bit (MSVC 2019)<br>
Visual Studio 2019 C++ x64<br>
After build Slicer in Visual Studio, 5 errors occurred.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4ee7fe371415d0245d7c6b73aa627e3677eb13d.jpeg" data-download-href="/uploads/short-url/s68zabXIRyYBxT4Y9wP6TKowLJr.jpeg?dl=1" title="圖片1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ee7fe371415d0245d7c6b73aa627e3677eb13d_2_690x163.jpeg" alt="圖片1" data-base62-sha1="s68zabXIRyYBxT4Y9wP6TKowLJr" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ee7fe371415d0245d7c6b73aa627e3677eb13d_2_690x163.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ee7fe371415d0245d7c6b73aa627e3677eb13d_2_1035x244.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ee7fe371415d0245d7c6b73aa627e3677eb13d_2_1380x326.jpeg 2x" data-dominant-color="363B3F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">圖片1</span><span class="informations">1418×335 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How to solve these errors? Thanks!</p>

---

## Post #2 by @cpinter (2021-01-26 08:51 UTC)

<p>Not sure it is related to your error, but you need to use a short superbuild path on Windows. For example <code>d:\s\S4D</code></p>

---

## Post #3 by @kejuhn (2021-01-27 08:00 UTC)

<p>Hi,<br>
I try again.<br>
The source folder is set to as C:\S4, and the build folder is set to as C:\S4R.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6225cbab195d268fb6c70a9d4ee479d31f79327d.png" data-download-href="/uploads/short-url/e0fLF6WZQJZV3Jk8MBQkD6Cjeix.png?dl=1" title="2021-01-27 10 31 28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6225cbab195d268fb6c70a9d4ee479d31f79327d_2_690x373.png" alt="2021-01-27 10 31 28" data-base62-sha1="e0fLF6WZQJZV3Jk8MBQkD6Cjeix" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6225cbab195d268fb6c70a9d4ee479d31f79327d_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6225cbab195d268fb6c70a9d4ee479d31f79327d_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6225cbab195d268fb6c70a9d4ee479d31f79327d_2_1380x746.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-01-27 10 31 28</span><span class="informations">1920×1040 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After build Slicer in Visual Studio, 5 errors also occurred.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34106c2f3c19224611302945460562fda0bcb5fa.png" data-download-href="/uploads/short-url/7qA0QI3WS6QRS7NxktsuZByWbAC.png?dl=1" title="2021-01-27 15 52 30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34106c2f3c19224611302945460562fda0bcb5fa.png" alt="2021-01-27 15 52 30" data-base62-sha1="7qA0QI3WS6QRS7NxktsuZByWbAC" width="690" height="175" data-dominant-color="353537"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-01-27 15 52 30</span><span class="informations">1545×392 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t know where the settings are wrong.<br>
Please help me to solve these errors. Thanks!</p>

---

## Post #4 by @lassoan (2021-01-27 17:39 UTC)

<p>The error list window in Visual Studio shows the errors in a somewhat random order. The errors that you show in the screenshot (all of them due to missing <code>archive.h</code>) are consequence of some previous errors that we don’t see.</p>
<p>Can you upload the full build log (not the content of “Error list” but content of “Output” window) somewhere and post the download link here?</p>

---

## Post #5 by @kejuhn (2021-01-29 00:30 UTC)

<p>Hi,</p>
<p>Here is the <a href="https://drive.google.com/file/d/15pQXad09ZRG20k_LQCAXfU6_uXXPqLoG/view?usp=sharing" rel="noopener nofollow ugc">full build log</a>.</p>
<p>Thanks for your replay!</p>

---

## Post #6 by @lassoan (2021-01-29 05:32 UTC)

<p>Probably the issue is that your system code page is set to 950 (Traditional Chinese) and c:\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c contains characters that cannot be interpreted in this code page.</p>
<p>The simplest is to remove the offending characters (remove entire line 74, it is just a comment):</p>
<pre><code> * "Rar!→•☺·\x00"
</code></pre>
<p>If you will keep running into similar errors then you may consider switching to Latin1 code page for the build.</p>

---

## Post #7 by @kejuhn (2021-02-01 00:27 UTC)

<p>It’s solved by your method.<br>
Thanks for your help!</p>

---

## Post #8 by @moonchi (2021-04-26 12:51 UTC)

<p>Hello, I am a graduate student in a master class, and I am currently working on building a 3D slicer, and some building errors are happening to me. It is convenient for you to ask if the five errors are all solved by deleting the comments, or  Is it useful for other solutions? If you are willing and available, is it convenient to email you for more details.  Thank you! It doesn’t matter if you don’t want to, thank you for reading.</p>
<details>
<summary>
Machine-translated from Chinese</summary>
<p>你好，我是一個碩班的研究生，目前也正在進行建置3D slicer的作業，有些建置錯誤我也正在發生，方便跟請問您五項錯誤都是把註釋刪掉就解決了嗎，還是有用了其他解決方式呢?如果您願意也有空，方便跟您要email請教詳細細節嗎。謝謝!不願意也沒有關係，謝謝您閱讀。</p>
</details>

---
