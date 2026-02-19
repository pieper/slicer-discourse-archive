---
topic_id: 17327
title: "Cpack Is Broken Because Of Wrong Dcmtk Path On Ubuntu 20"
date: 2021-04-26
url: https://discourse.slicer.org/t/17327
---

# Cpack is broken because of wrong dcmtk path on Ubuntu 20

**Topic ID**: 17327
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/cpack-is-broken-because-of-wrong-dcmtk-path-on-ubuntu-20/17327

---

## Post #1 by @aymeric.chataigner (2021-04-26 08:29 UTC)

<p>Hi,</p>
<p>OS: Linux Ubuntu 20<br>
3d slicer version: 4.11.20210226</p>
<p>I’m working on a 3d slicer custom app which uses slicelets.<br>
3d slicer cpack is used to generate the install archive.<br>
Unfortunately cpack process fails because it uses wrong path to copy dcmtk executables (for instance storescu).<br>
It is due to a FindDCMTK script into the CTK repository, here is the fix I proposed: <a href="https://github.com/commontk/CTK/pull/960" class="inline-onebox" rel="noopener nofollow ugc">COMP: FindDCMTK: fix wrong DCMTK_DIR in CTK-build/CTKConfig.cmake by achataigner · Pull Request #960 · commontk/CTK · GitHub</a></p>
<p>Could you have a look at it ?</p>
<p>Best regards,</p>
<p>Aymeric</p>

---

## Post #2 by @lassoan (2021-04-26 23:17 UTC)

<p>Thank you, we will review it as soon as we can. The best is to keep the discussion at the CTK bugtracker.</p>

---

## Post #3 by @aymeric.chataigner (2021-05-07 09:43 UTC)

<p>Issue added in ctk bugtracker: <a href="https://github.com/commontk/CTK/issues/966" class="inline-onebox" rel="noopener nofollow ugc">FindDCMTK.cmake can overwrite DCMTK_DIR previously set · Issue #966 · commontk/CTK · GitHub</a></p>

---
