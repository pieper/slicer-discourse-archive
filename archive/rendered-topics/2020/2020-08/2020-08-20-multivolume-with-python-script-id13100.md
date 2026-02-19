---
topic_id: 13100
title: "Multivolume With Python Script"
date: 2020-08-20
url: https://discourse.slicer.org/t/13100
---

# MultiVolume with python script

**Topic ID**: 13100
**Date**: 2020-08-20
**URL**: https://discourse.slicer.org/t/multivolume-with-python-script/13100

---

## Post #1 by @Chintha_Siva_Prasad (2020-08-20 07:57 UTC)

<p>How can I create multi volumes from python script and map them to different view nodes in slicer 3d?</p>

---

## Post #2 by @lassoan (2020-08-21 23:54 UTC)

<p>It is quite limited what you can do with MultiVolume, for example you can only have one or two volumes extracted from a sequence. However, if you load the volume as a Volume Sequence then there are no such limitations.</p>
<p>You can find in this example how to show different volumes in slice views: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images</a></p>

---
