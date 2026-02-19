---
topic_id: 7867
title: "Adding Vp File In Scene"
date: 2019-08-04
url: https://discourse.slicer.org/t/7867
---

# Adding .VP file in scene

**Topic ID**: 7867
**Date**: 2019-08-04
**URL**: https://discourse.slicer.org/t/adding-vp-file-in-scene/7867

---

## Post #1 by @sarvpriya1985 (2019-08-04 15:45 UTC)

<p>Hi,</p>
<p>I have .VP file that i want to add to a volume rendered scene and use the file’s transfer function (it was modified for making blood transparent). How can I make use of it for a new volume rendered scene. I am trying to drag and drop it in the scene but not sure where it is going.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2019-08-05 00:04 UTC)

<p>.vp file is loaded as a volume property node that you can use in volume rendering module (in Inputs section).</p>

---
