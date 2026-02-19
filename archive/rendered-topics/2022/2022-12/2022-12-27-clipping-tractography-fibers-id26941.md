---
topic_id: 26941
title: "Clipping Tractography Fibers"
date: 2022-12-27
url: https://discourse.slicer.org/t/26941
---

# Clipping Tractography fibers

**Topic ID**: 26941
**Date**: 2022-12-27
**URL**: https://discourse.slicer.org/t/clipping-tractography-fibers/26941

---

## Post #1 by @L_Zikarsky (2022-12-27 15:07 UTC)

<p>Slicer version: 4.10.2<br>
I’ve performed UKF tractography sometimes fibers seem to be too long and don’t follow any anatomic paths. Is there any way to clip fibers at a certain point? When using exclusion ROIs the whole fiber tract disappears but I only want to use a certain section of the fiber bundle.<br>
Varying the stopping criterions when performing UKF Tractography hasn’t helped so far.<br>
Thanks for the help!</p>

---

## Post #2 by @L_Zikarsky (2022-12-27 15:07 UTC)

<p>Slicer version: 4.10.2<br>
I’ve performed UKF tractography sometimes fibers seem to be too long and don’t follow any anatomic paths. Is there any way to clip fibers at a certain point? When using exclusion ROIs the whole fiber tract disappears but I only want to use a certain section of the fiber bundle.<br>
Varying the stopping criterions when performing UKF Tractography hasn’t helped so far.<br>
Thanks for the help!</p>

---

## Post #3 by @yrathi (2022-12-27 17:21 UTC)

<p>Generally, if the stopping criteria is made stronger the tracts should stop. You can check that again by putting the stopping criteria to stoping FA at 0.2.</p>
<p>Currently there isn’t an automated way to “cut” the tracts if they are “unruly”. The only way is to remove the entire tract.</p>

---
