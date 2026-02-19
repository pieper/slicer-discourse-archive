---
topic_id: 35600
title: "Plus Remote Necessity"
date: 2024-04-18
url: https://discourse.slicer.org/t/35600
---

# Plus remote necessity

**Topic ID**: 35600
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/plus-remote-necessity/35600

---

## Post #1 by @MReza (2024-04-18 13:39 UTC)

<p>Hello everyone,</p>
<p>I am currently using 3D Slicer for freehand ultrasound via IGT. My process involves running Plus and activating my server through OpenIGTLinkIF, which allows me to reconstruct the volume using live reconstruction without any issues. However, the SlicerIGT tutorials and a volume reconstruction video on YouTube recommend connecting the plus remote in Slicer. My question is: What is the purpose of Plus Remote, and what are its advantages if I can perform all necessary functions using OpenIGTLink?</p>
<p>Additionally, I’ve noticed that Plus Remote will not connect unless I first launch the server from the Plus software. This requirement has me puzzled about the necessity of Plus Remote. Could someone clarify its benefits and why it might be essential for my workflow?</p>
<p>I would greatly appreciate any explanation or insight into this matter.</p>

---

## Post #2 by @Sunderlandkyl (2024-04-18 15:00 UTC)

<p>Plus remote has 2 different tabs:</p>
<ol>
<li>
<p>Plus Launcher Control: Requires that PlusServerLauncher is running. Allows you to start and stop Plus servers remotely. You can also save/modify the Plus config files within the scene as text nodes.</p>
</li>
<li>
<p>Plus Server Control: Requires that a PlusServer is running. Allows you to record sequences and reconstruct volumes within Plus. Before volume reconstruction was included in SlicerIGT, this was the primary way of reconstructing volumes using Plus and Slicer. Currently I think that doing volume reconstruction from the “Volume Reconstruction” module is the better approach.</p>
</li>
</ol>
<p>The main benefit for your workflow could be the Plus Launcher Control, as you would be able to start/stop servers from within Slicer. It can also automatically restart servers that are stopped for any reason.</p>

---

## Post #3 by @MReza (2024-04-18 15:03 UTC)

<p>Hello Kyle<br>
Thanks for this quick explanation.</p>

---
