---
topic_id: 16944
title: "Is It Possible To Create A Custom Toolbars On Slicercat Slic"
date: 2021-04-05
url: https://discourse.slicer.org/t/16944
---

# Is it possible to create a custom toolbars on SlicerCAT/Slicer3d

**Topic ID**: 16944
**Date**: 2021-04-05
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-a-custom-toolbars-on-slicercat-slicer3d/16944

---

## Post #1 by @oren (2021-04-05 05:34 UTC)

<p>Operating system:Windows<br>
Slicer version:latest<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi<br>
Is it possible to create a custom toolbars on Slicer3d / SlicerCAT ?<br>
I wish to that the ‘favorites toolbar’ will be visible when opening Slicer3d<br>
I wish to custom ‘favorites toolbar’ automatically and not manually<br>
I wish to control all tool bars visibility using some configuration file<br>
is it possible ?<br>
thanks</p>

---

## Post #2 by @lassoan (2021-04-06 13:40 UTC)

<p>Yes, this is all just standard Qt. You can have a look at how Sequences module in creates and displays a custom toolbar.</p>

---
