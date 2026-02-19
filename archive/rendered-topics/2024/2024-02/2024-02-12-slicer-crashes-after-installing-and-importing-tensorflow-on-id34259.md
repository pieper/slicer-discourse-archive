---
topic_id: 34259
title: "Slicer Crashes After Installing And Importing Tensorflow On"
date: 2024-02-12
url: https://discourse.slicer.org/t/34259
---

# Slicer crashes after installing and importing tensorflow on linux

**Topic ID**: 34259
**Date**: 2024-02-12
**URL**: https://discourse.slicer.org/t/slicer-crashes-after-installing-and-importing-tensorflow-on-linux/34259

---

## Post #1 by @CyprienB (2024-02-12 16:22 UTC)

<p>Operating system: Fedora Linux 39<br>
Slicer version: Slicer-5.6.1<br>
Expected behavior: Import tensorflow from a python extension<br>
Actual behavior: Slicer crashes after installing tensorflow</p>
<p>Hello,<br>
After installing Slicer-5.6.1 on linux, I have created a new extension <strong>TestExtension</strong> using the Extension Wizard module in which I have added a new module <strong>TestModule</strong>. Then, I have installed the latest version of tensorflow (2.15.0.post1) using the synthax pip_install(‘tensorflow’) in the python console. When I restart Slicer, everything works fine. Then I added on the python file TestExtension/TestModuleTestModule.py the line “import tensorflow as tf”. After doing that I cannot restart Slicer as it crashes everytime with the following code:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/374a82b8bb22b4d926374a3a9c7f03192b35a402.png" data-download-href="/uploads/short-url/7T7TKoqeOTAFPdgdjA3pec8pGWm.png?dl=1" title="Report_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/374a82b8bb22b4d926374a3a9c7f03192b35a402_2_690x89.png" alt="Report_error" data-base62-sha1="7T7TKoqeOTAFPdgdjA3pec8pGWm" width="690" height="89" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/374a82b8bb22b4d926374a3a9c7f03192b35a402_2_690x89.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/374a82b8bb22b4d926374a3a9c7f03192b35a402_2_1035x133.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/374a82b8bb22b4d926374a3a9c7f03192b35a402_2_1380x178.png 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Report_error</span><span class="informations">1894×245 63.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-02-12 17:13 UTC)

<p>The medical image computing research community seems to have moved away from TensorFlow/Keras and standardized on using pytorch. Pytorch has become critically important for Slicer community as well, many users on many types of computers, GPUs, operating systems test it and we quickly fix any problems that arise.</p>
<p>In contrast, there might be a few extensions that use tensorflow for historical reasons, but they are not widely used and I’m not sure how well supported. Probably they all run tensorflow in an external Python environment. Of course this is really inconvenient for end users, as users don’t want to install Python and set up virtual python environments.</p>
<p>Overall, if you work in the medical image computing field then you might consider switching to using pytorch, as you will be part of a larger community and it will probably make your life easier.</p>

---

## Post #3 by @jamesobutler (2024-02-12 18:29 UTC)

<p>The below Google search interest metrics seems to support the idea that PyTorch has become more preferred than Tensorflow since 2021.<br>
<a href="https://trends.google.com/trends/explore?date=2016-01-12%202024-02-12&amp;q=pytorch,tensorflow&amp;hl=en" rel="noopener nofollow ugc">https://trends.google.com/trends/explore?date=2016-01-12%202024-02-12&amp;q=pytorch,tensorflow&amp;hl=en</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af26adfdef22660dc2665e4e0a3d4e4821c248e.png" data-download-href="/uploads/short-url/8pt4mnBDG2DnLgqaIzj8Z1uTikC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af26adfdef22660dc2665e4e0a3d4e4821c248e_2_690x406.png" alt="image" data-base62-sha1="8pt4mnBDG2DnLgqaIzj8Z1uTikC" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af26adfdef22660dc2665e4e0a3d4e4821c248e_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af26adfdef22660dc2665e4e0a3d4e4821c248e_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af26adfdef22660dc2665e4e0a3d4e4821c248e.png 2x" data-dominant-color="F7F8FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1171×690 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
