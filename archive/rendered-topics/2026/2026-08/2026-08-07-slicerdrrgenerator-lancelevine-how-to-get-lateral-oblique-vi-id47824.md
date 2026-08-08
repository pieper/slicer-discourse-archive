---
topic_id: 47824
title: "SlicerDRRGenerator (lancelevine) — how to get lateral/oblique views? Rotation parameters undocumented"
date: 2026-08-07
url: https://discourse.slicer.org/t/47824
last_bumped: 2026-08-07T10:06:46.843Z
---

# SlicerDRRGenerator (lancelevine) — how to get lateral/oblique views? Rotation parameters undocumented

**Topic ID**: 47824
**Date**: 2026-08-07
**URL**: https://discourse.slicer.org/t/slicerdrrgenerator-lancelevine-how-to-get-lateral-oblique-views-rotation-parameters-undocumented/47824

---

## Post #1 by @anuragp2018 (2026-08-07 10:06 UTC)

<p>Hi all,</p>
<p>I’m using the <strong>SlicerDRRGenerator</strong> extension ( <a href="http://github.com/lancelevine/SlicerDRRGenerator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lancelevine/SlicerDRRGenerator: A 3D Slicer extension that generates Digitally Reconstructed Radiographs · GitHub</a> ) to generate DRRs from a pelvis CT for comparison against intraoperative X-rays.</p>
<p>I’ve successfully generated an <strong>AP view</strong> using:</p>
<ul>
<li>Rotation: X=90, Y=0, Z=0</li>
<li>Translation: X=0, Y=200, Z=0</li>
<li>Center: 0,0,0</li>
<li>Focal Point: 400, Threshold: 0, Direction: 2</li>
<li>DRR Size: 512 x 494</li>
</ul>
<p>This produces a clean AP radiograph of the pelvis. However, I can’t figure out the correct rotation values to get a <strong>lateral</strong> or <strong>oblique</strong> view. I’ve tried:</p>
<ul>
<li>X=90, Y=90, Z=0 → produces what looks like a superior/inferior (axial-style) view, not lateral</li>
<li>X=90, Z=90, Y=0 → [describe what you got, or delete this line if you didn’t try it]</li>
</ul>
<p>The module has no documentation on what the Rotation X/Y/Z, Center, or Direction parameters actually mean geometrically, and I haven’t been able to find this explained anywhere (checked the GitHub repo, the published paper ).</p>
<p><strong>Questions:</strong></p>
<ol>
<li>Does anyone know the rotation convention this module uses (e.g., is it Euler angles applied in a specific order, and relative to which axis is “Direction: 2” defined)?</li>
<li>Has anyone successfully generated a lateral or oblique DRR with this specific module and can share working parameter values?</li>
</ol>
<p>Thanks in advance!</p>

---
