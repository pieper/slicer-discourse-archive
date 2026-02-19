---
topic_id: 14585
title: "Creating Volumetric Mesh With Segment Mesher Clever Cli Retu"
date: 2020-11-13
url: https://discourse.slicer.org/t/14585
---

# Creating volumetric mesh with Segment Mesher - Clever-cli returned non-zero exit status

**Topic ID**: 14585
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/creating-volumetric-mesh-with-segment-mesher-clever-cli-returned-non-zero-exit-status/14585

---

## Post #1 by @vincent.serantoni (2020-11-13 15:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Creating volumetric mesh<br>
Actual behavior: Error: Command ‘cleaver-cli.exe’ returned non-zero exit status</p>
<p>Hello everyone,</p>
<p>I have a Nrrd file of a mask of a bone (binary value, 255 or 0 only). I simplified the geometry using Fiji and now I need a volumetric mesh, so I’m using the extension SegementMesher based on this <a href="https://github.com/lassoan/SlicerSegmentMesher#tutorial" rel="noopener nofollow ugc">tuto</a>. For previous bones this solution worked fine for me. But now, whatever the scale value in Advanced parameter, I always have the following error message after few minutes<br>
Error: Command ‘cleaver-cli.exe’ returned non-zero exit status -1073740791<br>
Any advice ?</p>
<p>Thank you all and have a good day.</p>
<p>Vincent</p>

---

## Post #2 by @lassoan (2020-11-13 15:04 UTC)

<p>Please use latest stable or preview release of Slicer and let us know if you encounter any issues with them.</p>

---

## Post #3 by @vincent.serantoni (2020-11-13 17:37 UTC)

<p>Well, thank you<br>
This was enough…</p>

---
