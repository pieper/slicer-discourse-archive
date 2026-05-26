---
topic_id: 46762
title: "Developing a vessel analysis module for 3D Slicer – guidance needed"
date: 2026-04-17
url: https://discourse.slicer.org/t/46762
last_bumped: 2026-04-18T00:34:24.050Z
---

# Developing a vessel analysis module for 3D Slicer – guidance needed

**Topic ID**: 46762
**Date**: 2026-04-17
**URL**: https://discourse.slicer.org/t/developing-a-vessel-analysis-module-for-3d-slicer-guidance-needed/46762

---

## Post #1 by @Benny_Zamir (2026-04-17 03:36 UTC)

<p>Hi,</p>
<p>I’ve been working on a Python-based vessel analysis tool and uploaded it here:<br>
<a href="https://github.com/bz1977/VesselAnalyzer" rel="noopener nofollow ugc">https://github.com/bz1977/VesselAnalyzer</a></p>
<p>Current status:</p>
<ul>
<li>
<p>Branch segmentation and marker placement still need improvement</p>
</li>
<li>
<p>Lesion detection needs refinement</p>
</li>
</ul>
<p>I’d appreciate feedback on:</p>
<ul>
<li>
<p>How to best integrate this into 3D Slicer</p>
</li>
<li>
<p>Code structure and overall approach</p>
</li>
</ul>
<p>Any suggestions or guidance would be very helpful.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2026-04-17 19:11 UTC)

<p>There are lots of examples in the <a href="https://github.com/slicer/extensionsindex">Slicer Extension Index</a>.  Try installing some extensions that sound similar and then look at the code.</p>

---

## Post #3 by @lassoan (2026-04-18 00:34 UTC)

<p><a href="https://github.com/vmtk/SlicerExtension-VMTK#the-vmtk-extension-for-3d-slicer">VMTK extension</a> has lots of vascular quantification and analysis tools, including very fast and robust fully automatic centerline and branch extraction, cross-section analysis, etc. Check it out, as you may be able to reuse and build on these modules, so you could reduce the amount of code you need to maintain.</p>
<p>FYI, many more, very sophisticated vascular tools are coming to 3D Slicer soon, as the <a href="https://simvascular.github.io/">SimVascular</a> community is planning to port their modules into 3D Slicer. I would recommend to have a look at it, too, and focus on working on features that are not yet covered.</p>

---
