---
topic_id: 36068
title: "Uncheck Toggle Selectable Doesn T Anchor The Model"
date: 2024-05-10
url: https://discourse.slicer.org/t/36068
---

# Uncheck “Toggle Selectable” doesn’t anchor the model

**Topic ID**: 36068
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/uncheck-toggle-selectable-doesn-t-anchor-the-model/36068

---

## Post #1 by @Beatriz_2 (2024-05-10 15:28 UTC)

<p>Operating System: Windows<br>
Slicer Version: Slicer 5.6.1<br>
Headset used: Meta Quest 2<br>
Problem: unchecked the “Toggle Selectable” option doesn’t anchor the model and I can still manipulate it with controllers (e.g. grab it and move it).</p>
<p>Hi,</p>
<p>I’ve experimented the SlicerVirtualReality extension. However, I haven’t succeeded in fixing/anchoring the model even though I have already unselected the “Toggle Selectable” option, as shown in the image. After that, the model keeps moving when I grab it with the controllers.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2f77a7b0de356177a1cb05f0c842a420737bf74.png" alt="Toggle selectable" data-base62-sha1="rOKQF0ZqDGN8nvNMajCD9SGvXbS" width="417" height="320"></p>
<p>Also when I unselect the option “Toggle Selectable” and enable the option “Controllers transforms” from the SlicerVirtualReality extension, the model appears in the same place as the controller. This happens after I apply a transform to the model, as shown in the next photo.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/deb9a8ff05976d53ca31344687b9217814a2ae44.png" alt="VirtuaslReality.RightController_Transform" data-base62-sha1="vMjLXaGGbUdkLtt1wRlDBJqx9Pe" width="451" height="240"></p>
<p>I wanted to anchor the model, because it would help rotate the scene/model. When I try to rotate using grab/grip buttons, the model also moves from its spot. So everytime I try to rotate I also accidentally move the model.</p>
<p>Can someone help me overcome this issue? Do you have any other idea?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2024-05-12 11:29 UTC)

<p>The virtual reality module has been completely reworked and maybe the “Toggle Selectable” feature broke in the process. I would recommend to submit a bug report to the <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues">extension’s issue tracker</a>.</p>

---
