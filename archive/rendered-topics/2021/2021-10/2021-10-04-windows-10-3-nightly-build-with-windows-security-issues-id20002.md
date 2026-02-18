# Windows 10-3 nightly build with Windows Security issues

**Topic ID**: 20002
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/windows-10-3-nightly-build-with-windows-security-issues/20002

---

## Post #1 by @hherhold (2021-10-04 19:51 UTC)

<p>99% of the time, I use Slicer on a Mac, so 1000 apologies if this is something obvious.</p>
<p>I downloaded the latest nightly on my Windows machine (Windows 10) and I get a ton of “This content is blocked” errors when I try to run it or even go to the directory with Slicer.exe in it.</p>
<p>Anybody else run into this? I have recently run windows update and everything should be up to date. Note that I do not have Admin on this machine and cannot tell these warnings to just go away.</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @jcfr (2021-10-04 20:17 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="20002">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I get a ton of “This content is blocked” errors when I try to run it or even go to the directory with Slicer.exe</p>
</blockquote>
</aside>
<p>This is likely explained by the fact we do not sign the preview build.</p>
<p>Do you get similar message with other builds ?</p>
<p>To obtain older build, you can use URL like the following: <a href="https://download.slicer.org/?offset=-4">https://download.slicer.org/?offset=-4</a></p>

---

## Post #3 by @hherhold (2021-10-04 20:25 UTC)

<p>The only other build I have on this machine is months old (May or June nightly build) and it runs fine. I’ll try to download a more recent one and see what happens.</p>

---

## Post #4 by @lassoan (2021-10-05 18:33 UTC)

<p>During the expected (admittedly somewhat annoying process) of installing a Slicer Preview Release on Windows (downloaded using Edge browser) requires you to confirm 3 times (each time with two clicks) that you indeed want to install Slicer:</p>
<ul>
<li>Click the download link and wait for the download to complete</li>
<li><strong>Click on “…” button of the downloaded item, click "Keep"</strong></li>
<li>
<strong>Click “Show more”, click “Keep anyway”</strong> and wait for the automatic scan to complete (may take 10-20 seconds)</li>
<li><strong>Click on the installer, click “More info”, click "Run anyway"</strong></li>
<li>Click through the installer (Next/Agree/Install)</li>
</ul>
<p>This does not happen with the signed installer, but we only sign the Slicer Stable Release.</p>

---
