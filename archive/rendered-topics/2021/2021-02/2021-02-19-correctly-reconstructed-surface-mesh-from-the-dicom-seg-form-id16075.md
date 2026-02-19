---
topic_id: 16075
title: "Correctly Reconstructed Surface Mesh From The Dicom Seg Form"
date: 2021-02-19
url: https://discourse.slicer.org/t/16075
---

# Correctly reconstructed surface mesh from the DICOM-seg format

**Topic ID**: 16075
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/correctly-reconstructed-surface-mesh-from-the-dicom-seg-format/16075

---

## Post #1 by @hwkim0325 (2021-02-19 07:11 UTC)

<p>Hello!,</p>
<p>I am trying to use brain segmentations in the Finite Element Method. So far, I could develop codes successfully to convert contours of DICOM-RT structure set to surface mesh by myself.</p>
<p>Now, I’m trying to use Dicom-Segmentation objects. However, I found lots of self-intersections in STL files exported from Dicom-SEG files in the Slicer.</p>
<p>Question: Is there any way to extract surface mesh from segmentation without intersection issues.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-02-19 13:10 UTC)

<p>DICOM Segmentation Object can represent arbitrarily complex segmentations, so it might not always possible to create a closed surface representation that is both smooth <em>and</em> accurate <em>and</em> error-free. Slight mesh errors, such as non-manifold edges, inverted face directions, or nearly coincident points or faces might appear in challenging cases, but there should not be self-intersection.</p>
<p>To make surface generation feasible you have a few options:</p>
<ul>
<li>let the smooth mesh generation requirement go: disable or reduce “Surface smoothing” (applied during binary labelmap to closed surface conversion)</li>
<li>apply slight smoothing to the segmentation using Segment Editor’s Smoothing effect</li>
<li>increase the resolution of the segmentation’s internal labelmap representation and apply slight smoothing (this will create mesh with smaller triangles, which may be able to represent intricate and also have smooth transitions)</li>
</ul>
<p>If these techniques don’t help then provide us example segmentations that you have trouble with.</p>

---
