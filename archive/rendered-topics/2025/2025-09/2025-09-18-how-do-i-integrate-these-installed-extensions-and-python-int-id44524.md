---
topic_id: 44524
title: "How Do I Integrate These Installed Extensions And Python Int"
date: 2025-09-18
url: https://discourse.slicer.org/t/44524
---

# How do I integrate these installed extensions and python into the EXE installation package?

**Topic ID**: 44524
**Date**: 2025-09-18
**URL**: https://discourse.slicer.org/t/how-do-i-integrate-these-installed-extensions-and-python-into-the-exe-installation-package/44524

---

## Post #1 by @bulala (2025-09-18 17:49 UTC)

<p>Operating system:Windows 11<br>
Slicer version:5.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d6bfbbab4cf00d085848018ae471c28bdabaf5.png" data-download-href="/uploads/short-url/tWjT6IblvCFtAA8g069qdK5VRxr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d6bfbbab4cf00d085848018ae471c28bdabaf5.png" alt="image" data-base62-sha1="tWjT6IblvCFtAA8g069qdK5VRxr" width="423" height="499" data-dominant-color="E6E9EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">803×947 32.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you 3D Slicer for providing such a handy medical imaging software. Due to network issues, I installed some extension packages offline. However, many of the Python packages required by these extensions are not installed. What should I do to install the corresponding versions of these Python packages?</p>

---

## Post #2 by @lassoan (2025-09-20 22:24 UTC)

<p>It would be hard to install all dependencies manually. I would recommend to perform segmentation once with each model you want to use to ensure all required Python libraries and models are installed. All Python package are stored in the application’s folder and so later you will not need network connection. You can even copy the application folder to different computers and it will just work, you just have to move the model files over to the new computer.</p>

---

## Post #3 by @bulala (2025-09-22 06:09 UTC)

<p>Thank you for your reply. I have packaged all the files under the installation path,C:\Users\320280359\AppData\Roaming\slicer.org. Do I need any other files?</p>
<p>1.All files under the installation path</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fea5149a5651747b5b82c752cd25a16a0eb1c73.png" data-download-href="/uploads/short-url/4ykP7FHuCHmVslFELd8vC5Mil5p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fea5149a5651747b5b82c752cd25a16a0eb1c73.png" alt="image" data-base62-sha1="4ykP7FHuCHmVslFELd8vC5Mil5p" width="650" height="373"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">650×373 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>2.C:\Users\320280359\AppData\Roaming\slicer.org</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a97ef9f6697620b2cd20a065c1e54c89915605.png" data-download-href="/uploads/short-url/xcdUPC2HSYihOU1qV8N2vlv9ioB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a97ef9f6697620b2cd20a065c1e54c89915605.png" alt="image" data-base62-sha1="xcdUPC2HSYihOU1qV8N2vlv9ioB" width="407" height="113"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">407×113 1.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Xiaojie_Guo (2025-09-22 09:44 UTC)

<p>Zipped everything in Slicer 5.8.1. And it worked for me.</p>

---

## Post #5 by @bulala (2025-09-29 09:07 UTC)

<p>请问还有啥文件，我感觉好乱，尤其C盘，它解决了py包问题，但是还是有一些冲突</p>

---

## Post #6 by @Xiaojie_Guo (2025-09-30 01:32 UTC)

<p>就是安装路径下的所有文件都打包就可以了。</p>

---
