---
topic_id: 32828
title: "Material Mapping For Bones"
date: 2023-11-15
url: https://discourse.slicer.org/t/32828
---

# Material mapping for bones

**Topic ID**: 32828
**Date**: 2023-11-15
**URL**: https://discourse.slicer.org/t/material-mapping-for-bones/32828

---

## Post #1 by @ElaniaDiBart (2023-11-15 05:46 UTC)

<p>Hi all,</p>
<p>I’m attempting material mapping for mechanical properties in bones. I’ve previously achieved this in MITK-Gem by correlating Hounsfield Units (HU units) with bone density, followed by computing the elastic modulus. Now, I’d like to replicate a similar process in 3D Slicer.</p>
<p>I segmented a femur from a CT scan, meshed it using the Segment Mesher extension, utilized probe volume with a model for mapping, and employed segment statistics to compute the minimum, maximum, and mean values of HU units.</p>
<p>How can I proceed to obtain material mapping or bone density and apply the same equation or a similar method as in the MITK-Gem process? Does anyone have any ideas?</p>

---
