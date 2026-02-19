---
topic_id: 4489
title: "Has Anyone Tested A Nightly Build On Windows Server 2016"
date: 2018-10-22
url: https://discourse.slicer.org/t/4489
---

# Has anyone tested a nightly build on windows server 2016?

**Topic ID**: 4489
**Date**: 2018-10-22
**URL**: https://discourse.slicer.org/t/has-anyone-tested-a-nightly-build-on-windows-server-2016/4489

---

## Post #1 by @jamesjcook (2018-10-22 15:49 UTC)

<p>I’m getting ready to set up a new development VM and would love to know if anyone has traveled this path and failed ahead of me.</p>
<p>Has anyone tried to build on a window server 2016 system? I’ll be following the nightly instructions with VS 2015 and qt 5.10.1.</p>

---

## Post #2 by @lassoan (2018-10-22 17:44 UTC)

<p>We used a Windows Server system as a development PC a couple of years ago. It was not pleasant to use (it looked outdated compared to regular desktop Windows versions and it has some minor differences in behavior that we had to learn), but overall it worked OK.</p>
<p>You may have issues with OpenGL, GPU drivers, may not have virtual reality support, etc., especially now that Slicer requires minimum OpenGL 3.2, so if you don’t have a good reason to use a server version of Windows, then you are probably better off with a regular desktop version.</p>

---

## Post #3 by @jamesjcook (2018-10-23 13:25 UTC)

<p>Thanks for the heads up. My reason for server windows is that, it is what our institution likes to put on vm’s. It looks like 2016 supports adequate opengl, so, I’m going to try it and see what happens.</p>

---
