# Gamma calculation in Dose Comparison

**Topic ID**: 29486
**Date**: 2023-05-16
**URL**: https://discourse.slicer.org/t/gamma-calculation-in-dose-comparison/29486

---

## Post #1 by @mckirk (2023-05-16 04:38 UTC)

<p>HI, I’m able to calculate the gamma pass rate for 3%//3mm for two dose volumes and get ~ 99% pass rate.  If I click calculate gamma again, my pass rate falls dramatically to like 7% with the same 3%/3mm criteria.  After calculating gamma, do I need to Clear Scene and reload my dose volumes?  The gamma pass rate only seem accurate the first time I calculate or after I clear Scene.</p>
<p>Thanks,<br>
Mike</p>

---

## Post #2 by @gcsharp (2023-05-16 13:03 UTC)

<p>No, it shouldn’t be necessary to clear the scene.  I just tried and was not able to reproduce the problem.  Please do double check that both of your dose volumes are correct.  What version of Slicer are you using?</p>

---

## Post #3 by @mckirk (2023-05-16 13:23 UTC)

<p>Hi Greg,</p>
<p>I’m using 5.2.2. Here are couple screenshots illustrating what I’m seeing.</p>
<ol>
<li>
<p>Initial gamma at 2%.2mm pass rate 98%<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c2819e3c628fde0b55d4fafe566b1e3e71074c5.png" data-download-href="/uploads/short-url/mhqoU0TKXK2BSvxjpq5deW9F4Md.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c2819e3c628fde0b55d4fafe566b1e3e71074c5.png" data-base62-sha1="mhqoU0TKXK2BSvxjpq5deW9F4Md" alt="image.png" width="311" height="462" data-dominant-color="404040"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">440×654 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>Click ‘Calculate Gamma’ a second time without changing parameters. Pass rate falls to 8%</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5edc8a10ce01592a041f8de833bc12dac1506c60.png" data-download-href="/uploads/short-url/dxbnTZvtgzpIMeiP8Rba3O2p1PG.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5edc8a10ce01592a041f8de833bc12dac1506c60.png" data-base62-sha1="dxbnTZvtgzpIMeiP8Rba3O2p1PG" alt="image.png" width="338" height="499" data-dominant-color="404040"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">446×659 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks<br>
Mike</p>

---

## Post #4 by @gcsharp (2023-05-16 13:32 UTC)

<p>Ah, ok, I see what happened.  In the top image, your output gamma volume is set to “43: RTDOSE: Eclipse Doses” which is also your input reference dose.  In other words, the first calculation overwrote one of your input volumes.</p>
<p>If you instead set the Gamma volume to “Create new volume” and it will work as expected.</p>

---

## Post #5 by @mckirk (2023-05-16 13:33 UTC)

<p>Thanks for the help Greg!</p>

---
