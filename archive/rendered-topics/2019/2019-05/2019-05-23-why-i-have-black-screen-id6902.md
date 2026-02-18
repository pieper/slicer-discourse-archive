# Why I have black screen?

**Topic ID**: 6902
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/why-i-have-black-screen/6902

---

## Post #1 by @Sylwia_Gasowska (2019-05-23 18:31 UTC)

<p>Hi,<br>
After open Slicer3D I can see nothing, only black screen, during pressing at different places in Slicer window, I can see parts of menu. Like in the pictures. What can I do to fix that? Please help  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6ea4574a55ac993f5499c4bdd26ff0996e049d7.jpeg" data-download-href="/uploads/short-url/q68P3SMPvsUqmffSL68zwCkwSRF.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6ea4574a55ac993f5499c4bdd26ff0996e049d7_2_690x415.jpeg" alt="1" data-base62-sha1="q68P3SMPvsUqmffSL68zwCkwSRF" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6ea4574a55ac993f5499c4bdd26ff0996e049d7_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6ea4574a55ac993f5499c4bdd26ff0996e049d7_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6ea4574a55ac993f5499c4bdd26ff0996e049d7.jpeg 2x" data-dominant-color="0F0C07"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1075×648 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab9bf3a2b868171d38a802bd7c4d41d82f57165.jpeg" data-download-href="/uploads/short-url/vcW34MeyDsHm7knadRvFoF9Jpad.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dab9bf3a2b868171d38a802bd7c4d41d82f57165_2_690x414.jpeg" alt="2" data-base62-sha1="vcW34MeyDsHm7knadRvFoF9Jpad" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dab9bf3a2b868171d38a802bd7c4d41d82f57165_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dab9bf3a2b868171d38a802bd7c4d41d82f57165_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab9bf3a2b868171d38a802bd7c4d41d82f57165.jpeg 2x" data-dominant-color="999793"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1074×645 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-05-23 18:55 UTC)

<p>This happens when your CPU/graphics chipset is too old (see for example <a href="https://discourse.slicer.org/t/images-cannot-be-seen-after-loading-data/6154/4">this</a> topic).</p>
<p>What CPU model and graphics card, and operating system do you use?</p>

---

## Post #3 by @Sylwia_Gasowska (2019-05-23 21:53 UTC)

<p>Oh <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> oky, thank you</p>
<p>My<br>
CPU : Intel Core i3 - 5010u   2.10GHz<br>
Graphics Card: Intel HD Graphics 5500<br>
Operating system : Windows 8.1</p>

---

## Post #4 by @lassoan (2019-05-24 01:09 UTC)

<p>Thanks for the additional information. If you update graphics card drivers to the latest version and/or upgrade the operating system to Windows10 then there may be a chance that Slicer will work on that computer.</p>

---

## Post #5 by @Sorin_Acela (2021-11-24 19:04 UTC)

<p>Wrong answers!<br>
I solved the black home screen by launching the app with “Run as Administrator”. It worked smoothly.<br>
You can also go to program’s PROPERTIES/ Shortcut/ Advanced…/ Run as Administrator. This way you don’t have to click “Run as Administrator” each time.</p>

---

## Post #6 by @lassoan (2021-11-24 19:45 UTC)

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
