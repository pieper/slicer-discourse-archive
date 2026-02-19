---
topic_id: 15654
title: "Image Guided Surgery Too Slow"
date: 2021-01-25
url: https://discourse.slicer.org/t/15654
---

# Image Guided Surgery too slow

**Topic ID**: 15654
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/image-guided-surgery-too-slow/15654

---

## Post #1 by @l.koopman (2021-01-25 14:12 UTC)

<p>Hi all, I am trying to make Image Guided Surgery possible with 3D Slicer (v4.11) using 6 NDI Aurora trackers. The movement of the trackers needs to be measured and corrected in real-time. I use the Fiducial Registration Wizard (auto update mode) to make the registration between the preoperative and the perioperative trackers/pointer and OpenIGTLinkIF and PlusServer to make the connection with the EM system.</p>
<p>When testing it, everything works, so the locations of the trackers and of the pointer are updated continuously. However, the scene is really slow. Anyone has an idea why? Is the registration just too computationally expensive or is there a problem somewhere else? When I play the scene back at home at my laptop, the scene is not slow anymore. Does this mean it has something to do with the recording in the Sequence Browser?</p>
<p>The preoperative model included is not that big (38MB), all other programs are closed, the used programs are up to date. My laptop has an i7 processor, and the computer in the OR a Xeon processor.</p>
<p>Thanks in advance!</p>

---
