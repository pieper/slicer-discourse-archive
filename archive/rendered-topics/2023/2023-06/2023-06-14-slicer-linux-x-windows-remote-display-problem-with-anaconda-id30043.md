---
topic_id: 30043
title: "Slicer Linux X Windows Remote Display Problem With Anaconda"
date: 2023-06-14
url: https://discourse.slicer.org/t/30043
---

# Slicer Linux X Windows remote display problem with Anaconda .bashrc setup

**Topic ID**: 30043
**Date**: 2023-06-14
**URL**: https://discourse.slicer.org/t/slicer-linux-x-windows-remote-display-problem-with-anaconda-bashrc-setup/30043

---

## Post #1 by @NormandRobert (2023-06-14 21:15 UTC)

<p>Operating system: Ubuntu 22.04 remote and local<br>
Slicer version: 5.2.2<br>
Expected behavior: Start<br>
Actual behavior:  Window paint does not complete</p>
<p>I have discovered that if the remote shell running Slicer has the anaconda setup in .bashrc Slicer does not display properly. Is this widely known?</p>

---

## Post #2 by @lassoan (2023-06-16 14:24 UTC)

<p>Yes, anaconda often seriously messes up the environment. With some experimentation you may figure out exactly what environment variables or paths causing trouble and revert those to their default value before launching Slicer. Slicer launcher tries to override all environment variables that can cause trouble, but some may be missed. Let us know if you managed to figure out what caused the problem.</p>

---
