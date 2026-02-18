# Stitching overlapping volumes

**Topic ID**: 21337
**Date**: 2022-01-05
**URL**: https://discourse.slicer.org/t/stitching-overlapping-volumes/21337

---

## Post #1 by @mohammed_alshakhas (2022-01-05 13:44 UTC)

<p>I have a case of lesion extending from neck to lungs</p>
<p>I have both ct chest and ct neck. I’m trying to merge both through the registration method with no success.</p>
<p>any other way to do it?</p>
<p>thanks ahead</p>

---

## Post #2 by @hherhold (2022-01-05 19:14 UTC)

<p>I typically use FIJI to stitch together CT volumes.</p>

---

## Post #3 by @muratmaga (2022-01-05 19:57 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="21337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>through the registration method with no success.</p>
</blockquote>
</aside>
<p>Do you mean registration didn’t work (i.e. two scans didn’t line up correctly), or it worked but you couldn’t find a way to merge them?</p>
<p>If there is very little overlap between two volumes, automated registration may fail. Try the fiducial registration in SlicerIGT and see if that helps. You need 4-5 landmarks digitized on both volumes. Order is important</p>
<p>Once you get them aligned, you need to create an new volume that will be as big as the full extend of two scans. Easiest way to do that is to use the Crop Volume. The you have a bunch of option to stitch them together. You can use the AddScalarVolumes to merge them into a single volume.</p>
<p>Keep in mind, SimpleITK has bunch more filters that might be more useful. Perhaps XorImageFilter might be better (so that overlapped areas will have intensities identical to one of the scan).</p>

---

## Post #4 by @lassoan (2022-10-20 15:08 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> recently contributed the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> for this purpose. It is available in Sandbox extension.</p>

---
