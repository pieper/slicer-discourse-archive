---
topic_id: 24278
title: "Slicer 5 0 X Stable Downloads"
date: 2022-07-11
url: https://discourse.slicer.org/t/24278
---

# Slicer-5.0.x stable downloads

**Topic ID**: 24278
**Date**: 2022-07-11
**URL**: https://discourse.slicer.org/t/slicer-5-0-x-stable-downloads/24278

---

## Post #1 by @smrolfe (2022-07-11 18:24 UTC)

<p>When I click on the stable Mac download on <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> I’m getting the following error:</p>
<pre><code class="lang-auto">{
    "message": "Invalid item id (62cc52d2aa08d161a31c1af4).",
    "type": "rest"
}
</code></pre>

---

## Post #2 by @smrolfe (2022-07-11 18:29 UTC)

<p>Linux appears to be working but I’m getting a similar error for the Windows build.</p>

---

## Post #3 by @muratmaga (2022-07-11 18:38 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
Windows gives the same error too!</p>

---

## Post #4 by @jcfr (2022-07-11 18:45 UTC)

<p>Thanks for the feedback. We are aware of the issue.</p>
<p>I will revert the windows and macos updates and re-enable them once the packages are signed.</p>
<p>Release instructions will also be updated to avoid such problem from happening again</p>

---

## Post #5 by @jcfr (2022-07-11 19:10 UTC)

<p>Internal records have been fixed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55af247932e40d7bc2f04e75720e0a603b8aa0a3.png" data-download-href="/uploads/short-url/cdZPdb2wiGzLVr2xHrsNtTqhrCb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55af247932e40d7bc2f04e75720e0a603b8aa0a3_2_690x180.png" alt="image" data-base62-sha1="cdZPdb2wiGzLVr2xHrsNtTqhrCb" width="690" height="180" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55af247932e40d7bc2f04e75720e0a603b8aa0a3_2_690x180.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55af247932e40d7bc2f04e75720e0a603b8aa0a3_2_1035x270.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55af247932e40d7bc2f04e75720e0a603b8aa0a3_2_1380x360.png 2x" data-dominant-color="EEF4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2014×528 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jcfr (2022-07-11 21:39 UTC)

<p>To follow-up, the macOS package for <code>5.0.3</code> has been signed &amp; notarized and is now available for download.</p>

---

## Post #7 by @lassoan (2022-07-13 10:59 UTC)

<p>Thank you for working on these! When Slicer-5.0.3 package is expected to be available for Windows?</p>

---

## Post #8 by @jcfr (2022-07-13 15:42 UTC)

<blockquote>
<p>When Slicer-5.0.3 package is expected to be available for Windows?</p>
</blockquote>
<p>The unsigned windows installer is available for download <a href="https://slicer-packages.kitware.com/#item/62c7fb6aaa08d161a319b428">here</a></p>
<p>Given unforeseen circumstances, the windows package will likely be signed on Monday July 18th.</p>

---

## Post #9 by @lassoan (2022-07-13 23:02 UTC)

<p>Thanks for the link, this is very useful to know.</p>

---

## Post #10 by @jcfr (2022-07-18 21:42 UTC)

<p>The Windows package for Slicer 5.0.3 has been signed and is now available for download.</p>

---

## Post #11 by @madhawa (2023-08-29 03:12 UTC)

<p>I tried to download Slicer 5.0.3 for Windows using the links below, but it didn’t work. However, it seems to be working for Linux.<br>
Link1 - <a href="http://download.slicer.org/?offset=-270" class="inline-onebox" rel="noopener nofollow ugc">Download 3D Slicer | 3D Slicer</a><br>
Link2 - <a href="http://download.slicer.org/download?os=win&amp;stability=any&amp;offset=-270" rel="noopener nofollow ugc">http://download.slicer.org/download?os=win&amp;stability=any&amp;offset=-270</a></p>
<p>Got following message<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc13f10184e72ca4714d219717a1186aa92eb76f.png" alt="image" data-base62-sha1="zXZ2Ua7gEVysbPjb2vogzczfH7p" width="458" height="79"></p>
<p>I also tried to download the unsigned version from the link (<a href="https://slicer-packages.kitware.com/#item/62c7fb6aaa08d161a319b428" class="inline-onebox" rel="noopener nofollow ugc">SPKC</a>) but didn’t work.</p>
<p>Appreciate your help.</p>

---

## Post #12 by @lassoan (2023-08-29 06:43 UTC)

<p>Slicer-5.0.3 is an old release, but it is still available for <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/62cc513eaa08d161a31c1372">download on the Slicer package server</a>.</p>

---

## Post #13 by @jcfr (2023-08-29 07:54 UTC)

<p>Using the URL for the form <code>https://download.slicer.org/?version=&lt;RELEASE&gt;</code> may also be convenient.</p>
<p>For example <a href="https://download.slicer.org/?version=5.0.3">https://download.slicer.org/?version=5.0.3</a></p>

---
