---
topic_id: 33306
title: "Does Slicervirtualreality Work With 5 6"
date: 2023-12-09
url: https://discourse.slicer.org/t/33306
---

# Does SlicerVirtualReality work with 5.6?

**Topic ID**: 33306
**Date**: 2023-12-09
**URL**: https://discourse.slicer.org/t/does-slicervirtualreality-work-with-5-6/33306

---

## Post #1 by @mikebind (2023-12-09 01:05 UTC)

<p>I have a colleague who is interested in trying SlicerVirtualReality for visualization of cardiac data.  I don’t have any experience trying to use Slicer with VR because I don’t have the equipment, but I know I have seen examples here on the forum.  However, SlicerVirtualReality does not show up on the list of possible extensions in the Extension Manager on 5.6.  Is there currently an incompatibility?</p>

---

## Post #2 by @cpinter (2023-12-11 13:02 UTC)

<p>It is currently Windows only (it requires Steam and SteamVR). What operating system does your colleague use?</p>

---

## Post #3 by @cpinter (2023-12-11 16:09 UTC)

<p>Sorry it seems that currently it is not available on Windows either, see <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerVirtualReality" class="inline-onebox">CDash</a></p>
<p>Apparently the extension was not updated to follow VTK updates. Engineers at Kitware are working to completely overhaul the backend of VR/AR in VTK (and thus Slicer), so it is possible that keeping the extension functional until then is not a priority.</p>
<p>Also worth following this: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/126" class="inline-onebox">No SlicerVirtualReality extension built for Slicer 5.6.0 (Windows) · Issue #126 · KitwareMedical/SlicerVirtualReality · GitHub</a></p>

---
