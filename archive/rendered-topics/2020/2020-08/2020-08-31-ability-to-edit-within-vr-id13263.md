---
topic_id: 13263
title: "Ability To Edit Within Vr"
date: 2020-08-31
url: https://discourse.slicer.org/t/13263
---

# Ability to edit within VR

**Topic ID**: 13263
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/ability-to-edit-within-vr/13263

---

## Post #1 by @apeta (2020-08-31 19:34 UTC)

<p>Hi all,</p>
<p>I was wondering if there was an extension to edit models while you are in virtual reality? Similar to what VR Sketch does for Sketchup files?</p>
<p>Basically it would be nice to be able to interact with and move/transform/extrude different parts of an object while in VR… any thoughts on if this is possible?</p>

---

## Post #2 by @cpinter (2020-08-31 21:07 UTC)

<p>I have been wanting to do it for a long time, but there have been some obstacles so far. Now the last of these obstacles are being removed, namely upgrading to VTK 9, see <a href="https://github.com/Slicer/Slicer/pull/5141">here</a>. Once we can show interactive widgets in VR (VTK 9 is needed for that), we can use some of the already implemented VR widgets (see <a href="https://github.com/cpinter/SlicerVirtualReality/tree/virtual-widget">here</a>), one of which is Segment Editor VR. So if everything goes well, you’ll have an initial version of this feature in a few months. Of course, any help is welcome!</p>

---
