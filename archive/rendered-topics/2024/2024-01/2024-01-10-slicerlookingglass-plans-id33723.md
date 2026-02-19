---
topic_id: 33723
title: "Slicerlookingglass Plans"
date: 2024-01-10
url: https://discourse.slicer.org/t/33723
---

# SlicerLookingGlass plans

**Topic ID**: 33723
**Date**: 2024-01-10
**URL**: https://discourse.slicer.org/t/slicerlookingglass-plans/33723

---

## Post #1 by @cpinter (2024-01-10 16:07 UTC)

<p>Hi all,</p>
<p>I updated my development environment to the latest Slicer, and bumped into the issue that apparently the SlicerLookingGlass extension does not build anymore.</p>
<p>I did some digging and it seems that the last time it was build successfully was the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-11-22&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=lookingglass">nightly of November 22</a>.<br>
The problem seems to be related to the event delegation improvements (<a href="https://github.com/Slicer/Slicer/commit/1cc3b2c62bf5d3836802d3aab4ce37feee6500f0" class="inline-onebox">ENH: Improve Event Delegation in qMRMLThreeDView and qMRMLSliceView · Slicer/Slicer@1cc3b2c · GitHub</a>), at least that is my guess.</p>
<p>My question is whether it is planned to fix SlicerLookingGlass in the future? If not, do you (<a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a>) think that the extension could be fixed simply by just updating the calls according to the change, or some more profound change is needed?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @cpinter (2024-01-24 10:05 UTC)

<p>Does anyone know about plans regarding SlicerLookingGlass?</p>
<p>It would be nice to know what to expect in respect to supporting this hardware.</p>
<p>Thank you!</p>

---

## Post #3 by @cpinter (2024-02-07 12:41 UTC)

<p>Hi again, I’d just like to know if this device is planned to be kept supported in Slicer or not. Thanks!</p>

---

## Post #4 by @cpinter (2024-10-28 12:16 UTC)

<p>Hi there! Is there any news about this? Is the work with LookingGlass completely stopped, or left for the community, or something is ongoing… Thanks a lot for any answer!</p>

---

## Post #5 by @jcfr (2024-10-28 13:02 UTC)

<p>Thanks for reaching out <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Considering the underlying VTK modules is still maintained <img src="https://emoji.discourse-cdn.com/twitter/sparkles.png?v=12" title=":sparkles:" class="emoji" alt=":sparkles:" loading="lazy" width="20" height="20"> (see details <a href="https://github.com/Kitware/LookingGlassVTKModule">here</a>), we need to update the associated Slicer module to adapt to the recent VTK changes.</p>
<p>I will  discuss with the team and follow-up</p>

---

## Post #6 by @cpinter (2024-10-28 14:30 UTC)

<p>Great, thank you!</p>
<p>We do not use this technology directly anymore, but it would be great to know if it is expected to work again in the future or not. Thanks again</p>

---
