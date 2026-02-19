---
topic_id: 4116
title: "Want To Use Slicer Which Is Installed On Cloud Virtual Machi"
date: 2018-09-14
url: https://discourse.slicer.org/t/4116
---

# Want to use , slicer which is installed on cloud virtual machine

**Topic ID**: 4116
**Date**: 2018-09-14
**URL**: https://discourse.slicer.org/t/want-to-use-slicer-which-is-installed-on-cloud-virtual-machine/4116

---

## Post #1 by @anandmulay3 (2018-09-14 09:19 UTC)

<p>Hi ,<br>
I’m trying to use slicer on cloud virtual machine, i tried to use Nomachine, team viewer, and real Vnc, please suggest me a rdp client or if i’m missing any settings in these software’s.</p>
<p>Thanks</p>

---

## Post #2 by @anandmulay3 (2018-09-14 11:36 UTC)

<p>Okay , so finally i got logged in using noMachine,<br>
the thing is it’s a virtual machine on Azure, and whwnever i try to open Slicer its fails to start.<br>
Please suggest me a cloud machine requirement and configuration needed to run slice.</p>
<p>Thank you, and waiting for your replay <a class="mention" href="/u/lassoan">@lassoan</a>  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #3 by @lassoan (2018-09-14 12:20 UTC)

<p>VNC and TeamViewer works, too. You need a virtual machine that supports OpenGL 3.2 to run Slicer. If that’s an issue and hardware-accelerated fast rendering is not needed, then you should be able to build a custom 3D Slicer that uses software OpenGL renderer.</p>

---
