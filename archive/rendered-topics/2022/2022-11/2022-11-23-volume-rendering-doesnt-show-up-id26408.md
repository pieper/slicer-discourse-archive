# Volume Rendering doesn't show up

**Topic ID**: 26408
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/volume-rendering-doesnt-show-up/26408

---

## Post #1 by @kaveh_yousefpouran (2022-11-23 14:45 UTC)

<p>Operating System: Win 11<br>
Slicer Version 5.0.3 / 5.0.2</p>
<p>Problem: When I load a scene, 3d volume rendering doesn’t show up, but when I load a fresh DICOM bunch, 3d volume rendering works just fine. I tried all rendering options (CPU, GPU and whatnot) with no success.</p>
<p>P.S.: I’ve been using Slicer for years, so I did NOT forget to appoint my data to the renderer, or put a tick in the view box, etc. I updated to the newest version (5.0.3), but it didn’t fix anything. On the Linux system, however,  I don’t have this problem. this is something related to Windows.</p>
<p>I’m not sure if this is a brand-new bug or an intended feature (to make things more complex for users, because why not !), but I appreciate any suggestion on fixing the issue.</p>

---

## Post #2 by @lassoan (2022-11-23 14:48 UTC)

<p>Do you have an Intel graphics card in that computer?<br>
Does volume rendering appear if you disable and re-enable depth peeling (in the 3D view controller, in the drop-down menu of the <code>...</code> button)?</p>

---

## Post #3 by @kaveh_yousefpouran (2022-11-23 21:20 UTC)

<p>Thank you very much. I updated the NVIDIA driver, re-install the slicer and applied your suggestion, and the problem was fixed. I have two graphic cards on my machine, intel and NVIDIA, and windows switch them on demand. This switching act sometimes messes up some of my applications, and maybe this is the culprit. Nonetheless, thanks again.</p>

---
