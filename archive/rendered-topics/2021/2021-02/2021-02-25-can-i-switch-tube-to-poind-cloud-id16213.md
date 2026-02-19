---
topic_id: 16213
title: "Can I Switch Tube To Poind Cloud"
date: 2021-02-25
url: https://discourse.slicer.org/t/16213
---

# Can I switch tube to poind cloud?

**Topic ID**: 16213
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/can-i-switch-tube-to-poind-cloud/16213

---

## Post #1 by @timeanddoctor (2021-02-25 14:43 UTC)

<p>I created a tube from two points, and I need show it in PLC as a pointCloud. Can I resample it as a pointcloud file(Just many points vtx coordinate). I exported cube as a ply but the file is still be a mesh model.</p>

---

## Post #2 by @lassoan (2021-02-25 16:39 UTC)

<p>A surface mesh is a point cloud (with some additional information), so you don’t need to do any conversion create point cloud from a mesh.</p>
<p>What is PLC?</p>
<p>What is your overall goal?</p>

---

## Post #3 by @timeanddoctor (2021-02-26 12:43 UTC)

<p>The cube.ply(export from slicer) just contains top and button circle points, but no body points.<br>
I donnot know vtk/slicer could fill the tube body with points.<br>
What am I doing is following the picture:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d301fb7da3c147114d665edc0e955cb2150648f.jpeg" alt="image" data-base62-sha1="6rKAEnfA7MKzX9Hr3wb4pKlCNll" width="468" height="326"></p>

---

## Post #4 by @lassoan (2021-02-26 12:45 UTC)

<p>It is not clear why this is a problem.</p>
<p>What is PLC?</p>
<p>What is your overall goal?</p>

---

## Post #5 by @timeanddoctor (2021-02-26 12:48 UTC)

<p>sorry the “plc” is pcl.<br>
I need show the cube created from slicer in pcl</p>

---

## Post #6 by @lassoan (2021-02-26 13:09 UTC)

<p>To get help with this, you need to be more specific about what point cloud do you need and why. The “why” (high-level goal) is important because it helps in understanding the task even if requirements are incomplete; and it ensures we solve the right problem.</p>

---
