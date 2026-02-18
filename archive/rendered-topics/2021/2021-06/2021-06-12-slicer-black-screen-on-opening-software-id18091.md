# Slicer Black screen on opening software

**Topic ID**: 18091
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/slicer-black-screen-on-opening-software/18091

---

## Post #1 by @Lucky_Girish (2021-06-12 12:03 UTC)

<p>Operating system: Windows 10 Home<br>
Slicer version: 4.13.0<br>
Expected behavior: Starting with Slicer 3d<br>
Actual behavior: A blank black screen is appearing<br>
Pls help , i am unable to see any icons/ or options to upload data<br>
Just a blank black screen is appearing , i tries reinstalling , also the previous version same output.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921ebe55412a0dddda5037675e52d62e70246f74.png" data-download-href="/uploads/short-url/kQDzR0qrStMJGMZc4BzzQodJbGQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/921ebe55412a0dddda5037675e52d62e70246f74_2_690x368.png" alt="image" data-base62-sha1="kQDzR0qrStMJGMZc4BzzQodJbGQ" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/921ebe55412a0dddda5037675e52d62e70246f74_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/921ebe55412a0dddda5037675e52d62e70246f74_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921ebe55412a0dddda5037675e52d62e70246f74.png 2x" data-dominant-color="060606"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×730 5.73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-06-12 12:08 UTC)

<p>This typically happens if the computer does not have sufficient graphics capabilities to run Slicer. What CPU and graphics does this computer has?</p>

---

## Post #3 by @Lucky_Girish (2021-06-12 13:53 UTC)

<p>Hi Lassoan,<br>
Thanks for the response<br>
CPU : Intel I5<br>
Graphics - Intel (R) , Shared memory 2GB</p>
<p>It worked well for the first time immediately after download. Later on when i open after closing is appearing like this.</p>

---

## Post #4 by @lassoan (2021-06-12 14:12 UTC)

<p>What is the exact CPU model? Intel Core i5-…? (you can find it in System Information)</p>

---

## Post #5 by @Lucky_Girish (2021-06-12 17:07 UTC)

<p>CPU Details<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78b2a766d0c2603fd9f00d62644723560c6d0028.png" alt="image" data-base62-sha1="hdK3LjDdby4LwMn3TP3X1CgdbPa" width="502" height="149"><br>
Graphic Card Details<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36c25b926e9e8b65dff1f44ccb0b7997a9c05c63.png" alt="image" data-base62-sha1="7OqbXmACcPlNcjJFR4qXYmIZRgn" width="345" height="176"></p>

---

## Post #6 by @lassoan (2021-06-12 17:13 UTC)

<p>This is a 4th generation Intel CPU that was released in 2014. We need to balance between compatibility between old hardware and achieving good performance on modern hardware. As a result, we target 3D Slicer to run on computers that are not older than 5 years. See some more details <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">here</a>.</p>
<p>You either need to upgrade to a newer computer or rent a more recent computer from a cloud provider.</p>

---

## Post #7 by @Lucky_Girish (2021-06-12 17:25 UTC)

<p>Ok  thank you ,by any chance will it work if i download older version of slicer ?</p>

---

## Post #8 by @lassoan (2021-06-12 17:40 UTC)

<p>You can find old Slicer versions if you click the “access older releases” on the <a href="https://download.slicer.org/">Slicer download page</a>.</p>
<p>However, new versions of Slicer are so much better that I cannot recommend using older versions.</p>
<ul>
<li>If you consider your time valuable: the time that you save by using a more recent Slicer version is worth more than the cost of buying a computer (you can buy a used desktop computer that can run Slicer for about $500)</li>
<li>If you consider your time valuable but don’t want to buy a new computer right now (because you want to use Slicer for just a few hours or don’t want to spend money on computer hardware): you can rent a computer by the minute from a cloud provider.</li>
<li>If you don’t consider your time not valuable: you can use free cloud services, which are slower and not as convenient, but should still be usable (for example Binder, as explained in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">Getting started page</a>). You can click <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">here</a> to run a 1-year-old version of Slicer, for free, on the cloud. (you can configure newer versions, too)</li>
</ul>

---

## Post #9 by @Lucky_Girish (2021-06-12 17:45 UTC)

<p>Thanks a lot for the support lassoan. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> since I am using it for a study purpose project, I will try to rent from the cloud as recommended</p>

---

## Post #10 by @Sorin_Acela (2021-11-24 19:01 UTC)

<p>Wrong answers! I solved the black home screen by launching the app with “Run as Administrator”. It worked smoothly. You can also go to program’s PROPERTIES/ Shortcut/ Advanced…/ Run as Administrator. This way you don’t have to click “Run as Administrator” each time.</p>

---

## Post #11 by @lassoan (2021-11-24 19:45 UTC)

<p>Thanks for taking the time for letting other users know what worked for you. It is important to note that the answers above are not wrong, but of course there may be many different reasons behind the same symptom and not all solution work for everyone.</p>
<p>To better understand the impact of running Slicer as an administrator (on old Windows versions?), I’ve posted some questions to clarify - see here:</p>
<aside class="quote" data-post="5" data-topic="16531">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-opens-with-black-screen-on-windows-with-slicer-4-11-20210226/16531/5">Slicer opens with black screen on Windows with Slicer-4.11.20210226</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can go back and download earlier Slicer versions as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">here</a>.
  </blockquote>
</aside>


---

## Post #12 by @Sorin_Acela (2022-06-21 17:38 UTC)

<p>If you have Windows 10, another solution is to run Slicer in compatibility mode Windows 8.</p>

---

## Post #13 by @CASON_HINES (2026-02-12 18:56 UTC)

<p>wrong answer all you its 10</p>

---
