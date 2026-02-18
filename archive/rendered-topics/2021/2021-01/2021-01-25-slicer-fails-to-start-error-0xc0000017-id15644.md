# Slicer fails to start - error 0xc0000017

**Topic ID**: 15644
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/slicer-fails-to-start-error-0xc0000017/15644

---

## Post #1 by @slicer365 (2021-01-25 01:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8bafd808ca1cd01dfdc2111167a18c4a5b30791.jpeg" data-download-href="/uploads/short-url/sDK7mOfesFOr1fxRn2vlni3CwW5.jpeg?dl=1" title="微信图片_20210125092046" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8bafd808ca1cd01dfdc2111167a18c4a5b30791_2_666x500.jpeg" alt="微信图片_20210125092046" data-base62-sha1="sDK7mOfesFOr1fxRn2vlni3CwW5" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8bafd808ca1cd01dfdc2111167a18c4a5b30791_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8bafd808ca1cd01dfdc2111167a18c4a5b30791_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8bafd808ca1cd01dfdc2111167a18c4a5b30791_2_1332x1000.jpeg 2x" data-dominant-color="788476"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20210125092046</span><span class="informations">1440×1080 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The computer can run version 4.10 normally, but after 4.11 is installed, it prompts this error when running 4.11，0XC0000017   win10 -64</p>

---

## Post #2 by @lassoan (2021-01-25 01:36 UTC)

<p>Try to install Slicer in a folder that only has English (ASCII) characters in its name, for example, C:\test and let us know if it helped.</p>

---

## Post #3 by @slicer365 (2021-01-25 01:38 UTC)

<p>Yes, the software is installed in the English path, but the error still exists. I tried to run it in a compatible way, but it was also an error.The message is that the application cannot be started normally</p>

---

## Post #4 by @lassoan (2021-01-25 01:46 UTC)

<p>I’ve checked what this error code means:</p>
<pre><code>Not enough virtual memory or paging file quota is available to complete the specified operation
</code></pre>
<p>What operating system do you use?<br>
How old is this computer?<br>
How much physical RAM and what CPU and graphics do you have?</p>

---

## Post #5 by @slicer365 (2021-01-25 01:53 UTC)

<p>win 10  - 64<br>
It is a new computer ，RAM 8G，<br>
Intel® Xeon® CPU E5-2450 0 @ 2.10GHz(2101 MHz)，<br>
NVIDIA GeForce GTX 750 (4096MB)</p>

---

## Post #6 by @lassoan (2021-01-25 02:23 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="5" data-topic="15644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Intel® Xeon® CPU E5-2450</p>
</blockquote>
</aside>
<p>This CPU model was <a href="https://ark.intel.com/content/www/us/en/ark/products/64611/intel-xeon-processor-e5-2450-20m-cache-2-10-ghz-8-00-gt-s-intel-qpi.html">released in 2012</a>. This system is too old to run current version of Slicer.</p>
<p>We need to balance between supporting old hardware and having good performance by utilizing features of recent hardware generations. As a result, we aim for supporting hardware that is released in the past 5 years.</p>
<p>You can use older Slicer versions or try to rebuild current Slicer version on the old system. However, old hardware will keep holding you back, so I would recommend to replace your system with one that has at least 8th generation i5 CPU (you can get a desktop system like that for about $500, refurbished), but it is even a better investment to spend $1000-1500 on a computer that you can use comfortably for a few more years.</p>

---

## Post #7 by @slicer365 (2021-01-25 03:26 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="15644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>来代替您的系统</p>
</blockquote>
</aside>
<p>Thank you very much ,this is an assembling computer，I will refer to your suggestions.</p>

---
