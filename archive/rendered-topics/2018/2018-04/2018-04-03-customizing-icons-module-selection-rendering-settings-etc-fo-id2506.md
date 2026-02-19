---
topic_id: 2506
title: "Customizing Icons Module Selection Rendering Settings Etc Fo"
date: 2018-04-03
url: https://discourse.slicer.org/t/2506
---

# Customizing icons, module selection, Rendering settings etc for all users

**Topic ID**: 2506
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/customizing-icons-module-selection-rendering-settings-etc-for-all-users/2506

---

## Post #1 by @muratmaga (2018-04-03 19:54 UTC)

<p>Hi,</p>
<p>I am planning to deploy Slicer in on a multi-user workstation. I can customize module selection, GPU options etc for my users, but I don’t want all users to go through this first time they login or use Slicer. Is there a way to make this work on a Linux system? Can .slicerrc.py can contain this kind of options?</p>

---

## Post #2 by @lassoan (2018-04-03 22:09 UTC)

<p>Yes, you can modify all settings in .slicerrc.py - since you can do <em>anything</em>. However, if you just want to set some default settings then it is probably simpler to just copy your Slicer.ini file.</p>

---
