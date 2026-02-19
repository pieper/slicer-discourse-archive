---
topic_id: 14235
title: "Can Not Launch Nighty Build In Ubuntu"
date: 2020-10-25
url: https://discourse.slicer.org/t/14235
---

# Can not launch nighty build in ubuntu

**Topic ID**: 14235
**Date**: 2020-10-25
**URL**: https://discourse.slicer.org/t/can-not-launch-nighty-build-in-ubuntu/14235

---

## Post #1 by @ragwing_mmh (2020-10-25 06:48 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.13.0<br>
Expected behavior: Start 3D slicer nighty build<br>
Actual behavior: not launch</p>
<p>Detail:<br>
I have already run 3D slicer stable version(4.11) successfully in ubuntu device<br>
Otherwisely, after download the nighty build(4.13) and run it in same machine, it only shows a error window<br>
After closing the error window, double-click the slicer application again but nothing happen</p>
<p>Dose it mean I can only choose stable or nighty version in one device at same time?<br>
Or Could I install both versions in same ubuntu devices?</p>
<p>Thank you for everything</p>

---

## Post #2 by @lassoan (2020-10-25 12:45 UTC)

<p>Each installed Slicer package are completely independent except they share a common Slicer.ini application settings. So, the most likely way of your not-yet-stable Slicer-4.13 could interfere with the latest stable is through this application settings file. Delete <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=slicer.ini#settings-file-location">Slicer.ini</a> and see if it solves the issue.</p>
<p>Slicer preview releases are expected to be stabilized in the coming weeks.</p>

---
