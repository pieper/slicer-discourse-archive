---
topic_id: 22059
title: "Gel Dosimetry Registration Step Fails"
date: 2022-02-18
url: https://discourse.slicer.org/t/22059
---

# Gel dosimetry registration step fails

**Topic ID**: 22059
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/gel-dosimetry-registration-step-fails/22059

---

## Post #1 by @Kawtar_Lakrad (2022-02-18 22:11 UTC)

<p>Thank you so much for your help, the slicelet window pops up again. but the problem now is that I can’t perform automatic registration, which used to take only few sec.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beba9960c2dded64b7f02ca9ab24050875fa6e09.png" data-download-href="/uploads/short-url/rdgvnLFhn5EhIW0UsVhiEX1BrW9.png?dl=1" title="registration2T" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beba9960c2dded64b7f02ca9ab24050875fa6e09.png" alt="registration2T" data-base62-sha1="rdgvnLFhn5EhIW0UsVhiEX1BrW9" width="690" height="156" data-dominant-color="2C2726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registration2T</span><span class="informations">1421×322 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Kawtar_Lakrad (2022-02-21 21:28 UTC)

<p>It looks like this is perturbing other functions of the gel dosimetry module, because I tried to do registration manually but then when I got to do gamma analysis the software crushed (3 times).</p>

---

## Post #3 by @cpinter (2022-02-22 12:11 UTC)

<p>It seems that the extension needs to be updated to be compatible with the latest Slicer version.</p>
<p>Can you please try with an older release? Such as the last stable release?</p>

---

## Post #4 by @Kawtar_Lakrad (2022-02-23 19:25 UTC)

<p>Unfortunately, in the previous release I was not able to find the SandBox extension.</p>

---

## Post #5 by @cpinter (2022-02-24 08:37 UTC)

<p>To do gel dosimetry you need the Gel Dosimetry Analysis extension not Sandbox.</p>

---

## Post #6 by @Kawtar_Lakrad (2022-02-28 16:14 UTC)

<p>Yes, you’re right but when you want to draw line profiles, you’ll need the Sandbox extension…<br>
It’s okey now the problem was solved in the last release.<br>
Thank you for your answer.</p>

---

## Post #7 by @cpinter (2022-02-28 17:10 UTC)

<aside class="quote no-group" data-username="Kawtar_Lakrad" data-post="6" data-topic="22059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kawtar_lakrad/48/13528_2.png" class="avatar"> Kawtar_Lakrad:</div>
<blockquote>
<p>when you want to draw line profiles, you’ll need the Sandbox extension</p>
</blockquote>
</aside>
<p>I’m 99% sure that you actually don’t.</p>

---
