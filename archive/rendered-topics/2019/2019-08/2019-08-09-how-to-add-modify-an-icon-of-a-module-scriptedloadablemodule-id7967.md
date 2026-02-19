---
topic_id: 7967
title: "How To Add Modify An Icon Of A Module Scriptedloadablemodule"
date: 2019-08-09
url: https://discourse.slicer.org/t/7967
---

# How to add/modify an icon of a module (ScriptedLoadableModule)?

**Topic ID**: 7967
**Date**: 2019-08-09
**URL**: https://discourse.slicer.org/t/how-to-add-modify-an-icon-of-a-module-scriptedloadablemodule/7967

---

## Post #1 by @aiden.zhu (2019-08-09 15:21 UTC)

<p>Hi all,<br>
I am trying to make a new module of ScriptedLoadableModule. The default icon is like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7e0c3a767db4a0f15e6b695046eaeb585fb4905.png" alt="image" data-base62-sha1="x5hQKTds28s2ZZ0ku00JwfCQ1DL" width="45" height="45"><br>
Would you please give me some advice on this modification of module icons?<br>
Thanks in advance!</p>

---

## Post #2 by @Sunderlandkyl (2019-08-09 16:02 UTC)

<p>You can change the icon of a scripted module by placing a new icon in this location: “MODULE_DIR\Resources\Icons\MODULE_NAME.png”.</p>
<p>For reference, here is the icon for the SegmentEditor module icon: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentEditor/Resources/Icons/SegmentEditor.png" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentEditor/Resources/Icons/SegmentEditor.png</a></p>

---

## Post #3 by @aiden.zhu (2019-08-09 17:42 UTC)

<p>@ Sunderlandkyl<br>
Thank you so much, Kyle! Your instruction is straight clear! Exactly what I need do!</p>

---
