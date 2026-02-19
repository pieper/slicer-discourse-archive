---
topic_id: 4589
title: "How To Change The Different Flip Angle Volume Into Multivolu"
date: 2018-10-30
url: https://discourse.slicer.org/t/4589
---

# How to change the different flip angle volume into multivolume?

**Topic ID**: 4589
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/how-to-change-the-different-flip-angle-volume-into-multivolume/4589

---

## Post #1 by @Jin (2018-10-30 14:02 UTC)

<p>Operating system:windows 10<br>
Slicer version: 4.7.0<br>
Expected behavior: output multivolume<br>
Actual behavior: don’t know how to fill the settings, where can I get those informations? Thanks a lot!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/381adeb70aacad6966917cf6d314b6f4e8419cf3.png" alt="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181030220318" data-base62-sha1="80kj29L4o45kR3LljG8Jwvdf4EX" width="243" height="145"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3e69555af80c7a50f92529042310effa0d4e45.jpeg" data-download-href="/uploads/short-url/frzhwRkS254wdt21LrAxuShLUr3.jpeg?dl=1" title="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181030220651" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3e69555af80c7a50f92529042310effa0d4e45_2_690x373.jpeg" alt="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181030220651" data-base62-sha1="frzhwRkS254wdt21LrAxuShLUr3" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3e69555af80c7a50f92529042310effa0d4e45_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3e69555af80c7a50f92529042310effa0d4e45_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3e69555af80c7a50f92529042310effa0d4e45_2_1380x746.jpeg 2x" data-dominant-color="828289"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181030220651</span><span class="informations">1920×1039 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @fedorov (2018-10-30 16:50 UTC)

<p>What is the format of your input data?</p>

---

## Post #3 by @Jin (2018-10-31 07:14 UTC)

<p>thanks a lot! I have solved the problem with somebody help, but when I use PKmodeling to calculate the Ktrans, I got the output without mask image, but when I choose the ROI mask image, there are errors. Somethings happened when I got the mask image.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddd0e3128b928111e989203e838e13e3e32f9317.png" data-download-href="/uploads/short-url/vEh3FYnxEWSXOpkw3u3r36BR6fR.png?dl=1" title="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181031142447" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd0e3128b928111e989203e838e13e3e32f9317_2_690x373.png" alt="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181031142447" data-base62-sha1="vEh3FYnxEWSXOpkw3u3r36BR6fR" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd0e3128b928111e989203e838e13e3e32f9317_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd0e3128b928111e989203e838e13e3e32f9317_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddd0e3128b928111e989203e838e13e3e32f9317_2_1380x746.png 2x" data-dominant-color="918D92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181031142447</span><span class="informations">1920×1039 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/002907684a93e288f514db61798d190fe833b169.png" data-download-href="/uploads/short-url/1pU3juYPTUshSv6iG3OcMqtz4J.png?dl=1" title="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181031151705" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002907684a93e288f514db61798d190fe833b169_2_690x373.png" alt="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181031151705" data-base62-sha1="1pU3juYPTUshSv6iG3OcMqtz4J" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002907684a93e288f514db61798d190fe833b169_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002907684a93e288f514db61798d190fe833b169_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002907684a93e288f514db61798d190fe833b169_2_1380x746.png 2x" data-dominant-color="86868D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181031151705</span><span class="informations">1920×1039 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @fedorov (2018-11-01 14:38 UTC)

<p>Glad to hear you solved the problem. It would be nice if you could post the solution so that if someone has a similar issue your post could help them.</p>
<p>About your new question, please include the full error log and ideally the de-identified dataset to allow reproduce the problem.</p>

---

## Post #5 by @Jin (2018-11-07 11:59 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/584a7ca89044ff9bb650f16c4286febf68131ba2.png" data-download-href="/uploads/short-url/cB3BvpXf4MM5Su2WHey8cerhHay.png?dl=1" title="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181107194717" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/584a7ca89044ff9bb650f16c4286febf68131ba2_2_690x369.png" alt="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181107194717" data-base62-sha1="cB3BvpXf4MM5Su2WHey8cerhHay" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/584a7ca89044ff9bb650f16c4286febf68131ba2_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/584a7ca89044ff9bb650f16c4286febf68131ba2_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/584a7ca89044ff9bb650f16c4286febf68131ba2_2_1380x738.png 2x" data-dominant-color="EDEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181107194717</span><span class="informations">1916×1027 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> !<br>
I use the Dicom module to solved the problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d723e032b86f45ab7e38f70fa0b00732810c4eb2.png" data-download-href="/uploads/short-url/uHdwdudlyvlL22Cb2qF1jGWtBTk.png?dl=1" title="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181107194725" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d723e032b86f45ab7e38f70fa0b00732810c4eb2_2_690x373.png" alt="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181107194725" data-base62-sha1="uHdwdudlyvlL22Cb2qF1jGWtBTk" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d723e032b86f45ab7e38f70fa0b00732810c4eb2_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d723e032b86f45ab7e38f70fa0b00732810c4eb2_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d723e032b86f45ab7e38f70fa0b00732810c4eb2_2_1380x746.png 2x" data-dominant-color="78787F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181107194725</span><span class="informations">1920×1039 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Actually I don’t know how to add the ROI image that allow me to analysis the region of interest like circle/cube/free area, and how I can get the time intensity curves？<br>
Thanks a lot!!</p>

---

## Post #6 by @fedorov (2018-11-07 15:54 UTC)

<aside class="quote no-group" data-username="Jin" data-post="5" data-topic="4589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4af34b/48.png" class="avatar"> Jin:</div>
<blockquote>
<p>I use the Dicom module to solved the problem.</p>
</blockquote>
</aside>
<p>Makes sense. You should use DICOM Browser to load multivolumes from DICOM. The purpose of MultiVolumeImporter is to load multivolumes that are saved as a sequence of volumes in non-DICOM format.</p>
<aside class="quote no-group" data-username="Jin" data-post="5" data-topic="4589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4af34b/48.png" class="avatar"> Jin:</div>
<blockquote>
<p>Actually I don’t know how to add the ROI image that allow me to analysis the region of interest like circle/cube/free area, and how I can get the time intensity curves？</p>
</blockquote>
</aside>
<p>You first need to extract a single frame from the multivolume, and then use Editor module to segment the regions of interest. You can then plot curves averaged over those regions.</p>
<p>If you want to see curves for the individual pixels, you can do that using MultiVolumeExplorer module.</p>
<p>If this is too confusing, I will make a demo video later.</p>

---

## Post #7 by @Jin (2018-11-25 16:26 UTC)

<p>Thanks a lot, I will try it as you say.</p>

---
