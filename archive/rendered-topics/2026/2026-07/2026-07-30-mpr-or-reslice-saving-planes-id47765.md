---
topic_id: 47765
title: "MPR or reslice, saving planes"
date: 2026-07-30
url: https://discourse.slicer.org/t/47765
last_bumped: 2026-07-30T14:41:53.131Z
---

# MPR or reslice, saving planes

**Topic ID**: 47765
**Date**: 2026-07-30
**URL**: https://discourse.slicer.org/t/mpr-or-reslice-saving-planes/47765

---

## Post #1 by @Deep_Learning (2026-07-30 13:52 UTC)

<p>Is there a mechanism/extension to recall MPR/reslicing (interactive) planes?</p>
<p>eg, I have two volumes in a scene,  I reslice one, then switch to the other volume and reslice.  Want to switch back to volume 1 and have its reslice.</p>
<p>Not sure if there is functionality or an extension available.</p>

---

## Post #2 by @chir.set (2026-07-30 14:41 UTC)

<p>You may sort of <em>half-use</em> the <code>StenosisMeasurement2D</code> module in the <code>SlicerVMTK</code> extension.</p>
<p>A volume is not required for just remembering the orientation of a slice view.</p>
<p>In the selected slice view, after reformatting, place a fiducial point and select it in the module. Then click on the control point, that’s when the orientation is recorded in the point itself. After reformatting again, place another control point in the same slice view and click on it.</p>
<p>The slice view will be restored to the orientation saved with each control point when you click it again.</p>

---
