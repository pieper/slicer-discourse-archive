# Generating surface triangulation (mesh) based on sequence of segmentation

**Topic ID**: 22324
**Date**: 2022-03-05
**URL**: https://discourse.slicer.org/t/generating-surface-triangulation-mesh-based-on-sequence-of-segmentation/22324

---

## Post #1 by @BraveDistribution (2022-03-05 14:28 UTC)

<p>Hi all,</p>
<p>I have a motion dataset tracking liver with segmentation available throughout the whole sequence. I’d like to generate a mesh from the first segmentation and then continuously deform it throughout the time. Of course, the set of nodes and adjacency matrix should stay the same.</p>
<p>I know that there is the extension “Segment Mesher” that generates the mesh from segmentation, but it works only on one segmentation from the sequence. If the organ is deformed significantly, I expect that number of nodes will be lower than the non-deformed organ.</p>
<p>TLDR: I have a temporal sequence of segmentation (therefore tracked motion of organ under observation) and I’d like to have temporal sequence of meshes, while the meshes have the same adjacency matrix.</p>
<p>Is something like that possible in 3d Slicer?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2022-03-05 16:15 UTC)

<p>On option could be to use the <a href="https://github.com/SlicerRt/SegmentRegistration">SegmentRegistration</a> tool to calculate the transforms between sequence time points and then transfer the same mesh through the sequence.</p>

---

## Post #3 by @BraveDistribution (2022-03-09 23:53 UTC)

<p>Could you elaborate a bit more? I can perform the segment registration, but how to <em>transfer the same mesh through the sequence</em>?</p>

---

## Post #4 by @pieper (2022-03-10 00:03 UTC)

<p>I was thinking you can just make a copy of the mesh from the first time point, apply the transform from time 1 to time 2, and harden it.  Then make a copy of this hardened one, transform it to time point 3, harden, etc.  There may be some drift, but if the features are distinct enough I’d think the vertices would say pretty much in the same places with respect to surface features.</p>

---
