# 3D Slicer 5.10-11 incompatible extensions - TotalSegmentator, UpperAirwaySegmentator, CADSWholeBodyCTSeg

**Topic ID**: 45047
**Date**: 2025-11-11
**URL**: https://discourse.slicer.org/t/3d-slicer-5-10-11-incompatible-extensions-totalsegmentator-upperairwaysegmentator-cadswholebodyctseg/45047

---

## Post #1 by @MaxVs (2025-11-11 21:55 UTC)

<p>Hi guys!<br>
Can you tell me whats going on with TotalSegmentator in 5.10 or 5.11 updates?<br>
After tones of errors and difficulties with installing dependancies I faced this.<br>
I have RTX 4060Ti 8Gb and ryzen 5950x</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/100b20ebe034d688d3036833b49c914b44bb661c.png" data-download-href="/uploads/short-url/2hVtUvbMw0tMXsREnPnTs9PIfMg.png?dl=1" title="Zrzut ekranu 2025-11-11 184649" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/100b20ebe034d688d3036833b49c914b44bb661c.png" alt="Zrzut ekranu 2025-11-11 184649" data-base62-sha1="2hVtUvbMw0tMXsREnPnTs9PIfMg" width="479" height="220"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Zrzut ekranu 2025-11-11 184649</span><span class="informations">479×220 4.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In general I have installed 5.8 version and <strong><a href="https://extensions.slicer.org/view/TotalSegmentator/34045/win" rel="noopener nofollow ugc">TotalSegmentator</a></strong> works as new, but in the newest versions after this error everything freezes and I’m able to unfreeze only after terminating python-real in Task Manager.</p>
<p>Another extensions that does not work are <strong><a href="https://extensions.slicer.org/view/UpperAirwaySegmentator/34045/win" rel="noopener nofollow ugc">UpperAirwaySegmentator</a></strong> and **<a href="https://extensions.slicer.org/view/CADSWholeBodyCTSeg/34045/win" rel="noopener nofollow ugc">CADSWholeBodyCTSeg</a>.<br>
Are these problems due to so new versions of the Slicer and imcompatible codes extensions, or its my PC??</p>
<p>Thank You!**</p>

---

## Post #2 by @muratmaga (2025-11-11 22:07 UTC)

<p>I can’t comment for other things, but screenshot you shared shows that you run out of GPU memory. This would happen if your dataset is large (or you have other things loaded into your GPU taking up memory).</p>
<p>If you run the same dataset on 5.8 on the same GPU, is it working without a crash?</p>

---

## Post #3 by @MaxVs (2025-11-11 22:36 UTC)

<p>Yes, it is CT from sample data in Slicer, and in 5.8 it works perfectly fine - full model in 63 seconds.<br>
The same comunicate is indicated in different extensions, whats interesting with the same numbers of missing Gigabytes.</p>

---

## Post #4 by @muratmaga (2025-11-11 22:38 UTC)

<p>I don’t use totalsegmentator, but it is possible that newer versions use a different model (and with more parameters) than the one working on 5.8. Otherwise not sure why it would need more memory.</p>
<p>Perhaps one of the developers can chime in.</p>

---

## Post #5 by @MaxVs (2025-11-11 23:13 UTC)

<p>Maybe it will be fixed in the following updates.<br>
Thank you so much for your time!</p>

---

## Post #6 by @Alex_Vergara (2025-11-12 10:07 UTC)

<p>A fix has already been proposed for <a href="https://gitlab.com/opendose/opendose3d/-/merge_requests/301" rel="noopener nofollow ugc">OpenDose</a></p>

---

## Post #7 by @eNable_Polska (2025-11-19 20:20 UTC)

<p>404 error, page not found</p>

---

## Post #8 by @alex_He (2025-11-22 08:40 UTC)

<p>I face the same problem with slicer 5.10 and totalsegmentater 2</p>

---

## Post #9 by @Florian_46 (2025-12-19 10:28 UTC)

<p>I have the same issue. nnUNet pretrained models and TotalSegmentator run perfectly on Slicer 5.8, but after upgrading to Slicer 5.10 I systematically get a <strong>“CUDA out of memory”</strong> error.</p>

---

## Post #10 by @MaxVs (2026-01-22 21:48 UTC)

<p>Guys! In my case, problem disappeared in version 5.11.0-2026-01-21.<br>
Everything works perfect <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=15" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"><br>
Topic closed <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
