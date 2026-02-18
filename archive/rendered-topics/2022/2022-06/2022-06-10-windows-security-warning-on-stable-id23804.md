# Windows security warning on Stable

**Topic ID**: 23804
**Date**: 2022-06-10
**URL**: https://discourse.slicer.org/t/windows-security-warning-on-stable/23804

---

## Post #1 by @muratmaga (2022-06-10 02:25 UTC)

<p>I am seeing this message for the stable on my Windows 11 machine.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/334539dada7138083edf1a19e9e32e16097ba757.png" data-download-href="/uploads/short-url/7jyFlXSzCfsvQiQWYwCuM2fz9j1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/334539dada7138083edf1a19e9e32e16097ba757.png" alt="image" data-base62-sha1="7jyFlXSzCfsvQiQWYwCuM2fz9j1" width="460" height="500" data-dominant-color="1F2020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">507×550 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-06-10 04:22 UTC)

<p>This is a heuristic “detection” (indicated by the <code>!ml</code> tag), which tends to randomly flag executables as unwanted or malicious.</p>
<p>Kitware will request Microsoft to fix this - see:</p>
<aside class="quote quote-modified" data-post="1" data-topic="23613">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/windows-defender-quarantined-slicer-exe/23613">Windows Defender quarantined Slicer.exe</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    On my university-managed computer, Slicer.exe disappeared from the install tree. Windows Defender quarantined the executable due to “potentially unwanted behavior”. 
[image] 
It states that it detected Program:Win32/Beareuws.A!ml, which must be a false positive. I’ve submitted the executable to VirusTotal and nothing was detected (just one bogus engine out of 68 indicated “unsafe” without any more information). 
<a class="mention" href="/u/jcfr">@jcfr</a> You have submitted false positives to Microsoft before. Would you be able to s…
  </blockquote>
</aside>


---
