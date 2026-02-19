---
topic_id: 28268
title: "Extract Local Coordinates From A Line And Plane In A Coordin"
date: 2023-03-10
url: https://discourse.slicer.org/t/28268
---

# Extract local Coordinates from a line and plane in a coordinate model

**Topic ID**: 28268
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/extract-local-coordinates-from-a-line-and-plane-in-a-coordinate-model/28268

---

## Post #1 by @MAURICIO_ALBERTO_LED (2023-03-10 01:17 UTC)

<p>Operating system: win 11<br>
Slicer version:5.0.2</p>
<p>I need to calculate the local coordinates of a Line and a Plane, in a new coordinate system.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cc5b5c73c1567de82fad1ce8d12f6a3d09730f.jpeg" data-download-href="/uploads/short-url/qvEacPtp8bzWQbuw6r4CBPMGoBF.jpeg?dl=1" title="Captura de pantalla 2023-03-09 201659" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9cc5b5c73c1567de82fad1ce8d12f6a3d09730f_2_582x499.jpeg" alt="Captura de pantalla 2023-03-09 201659" data-base62-sha1="qvEacPtp8bzWQbuw6r4CBPMGoBF" width="582" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9cc5b5c73c1567de82fad1ce8d12f6a3d09730f_2_582x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cc5b5c73c1567de82fad1ce8d12f6a3d09730f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cc5b5c73c1567de82fad1ce8d12f6a3d09730f.jpeg 2x" data-dominant-color="9A9AC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-03-09 201659</span><span class="informations">811×696 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I execute this code I can retrieve the coordinates in a world coordinate system. But I need the local coordinates of the L_1 (blue line) Line with respect to the yellow coordinate system. Thanks for the help.</p>
<p>import multiprocessing as mp<br>
import numpy as np # import library</p>
<p>lineNodeNames = [“L_1”]</p>
<p>lineNode = slicer.util.getFirstNodeByClassByName(“vtkMRMLMarkupsLineNode”, lineNodeNames[0]) # Return the first node in the scene that matches the specified node class(“vtkMRMLMarkupsLineNode” in this case ) and node name(ech plane "lineNodeName " in the list lineNodeNames ) .<br>
print(“lineNode:”, lineNode)<br>
lineStartPos = np.zeros(3) # Return a new array of given shape and type, filled with “3” zeros and saves in lineStartPos<br>
print(“lineStartPos:”, lineStartPos)<br>
lineEndPos = np.zeros(3) # Return a new array of given shape and type, filled with “3” zeros and saves in lineEndPos<br>
print(“lineEndPos:”, lineEndPos)<br>
lineNode.GetNthControlPointPositionWorld(0, lineStartPos) # Get the position of the Nth control point in World coordinate system Returns 0 on failure, 1 on success.<br>
print(“lineNode _ 0:”, lineStartPos)<br>
lineNode.GetNthControlPointPositionWorld(1, lineEndPos) # Get the position of the Nth control point in World coordinate system Returns 0 on failure, 1 on success.</p>
<p>print(“lineNode _ 1:”, lineEndPos)</p>

---

## Post #2 by @chir.set (2023-03-10 18:21 UTC)

<p>If you know the world coordinates of the desired origin (yellow intersection), the first idea that comes to mind is to subtract this yellow  origin from lineStartPos and lineEndPos. Does this fit your requirements? It could be I didn’t fully understand the problem.</p>

---
