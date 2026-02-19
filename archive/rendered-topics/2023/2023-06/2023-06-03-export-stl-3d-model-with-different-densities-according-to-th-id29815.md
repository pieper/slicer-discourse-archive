---
topic_id: 29815
title: "Export Stl 3D Model With Different Densities According To Th"
date: 2023-06-03
url: https://discourse.slicer.org/t/29815
---

# Export STL 3D Model with different densities according to the HU of DICOM

**Topic ID**: 29815
**Date**: 2023-06-03
**URL**: https://discourse.slicer.org/t/export-stl-3d-model-with-different-densities-according-to-the-hu-of-dicom/29815

---

## Post #1 by @gonzalozar (2023-06-03 17:23 UTC)

<p>Does the exported STL output file (when segmenting) also considers the densities of the DICOM image (more or less HU units)? If not, is there any way to obtain a exported STL that also considers the densities?</p>
<p>Please if I’m wrong in some way, correct me, because I’m just learning about this and how it works!</p>

---

## Post #2 by @lassoan (2023-06-03 17:25 UTC)

<p>STL is very limited, so probably you would need to use a different file format. What is your end goal?</p>

---

## Post #3 by @gonzalozar (2023-06-04 09:45 UTC)

<p>Thank you very much for your suggestion, my main goal is to 3D print a portion (or slice) of a CAT, but not only its geometry, also its different tissues densities (tissue heterogeneity and homogeneity) that varies proportionately on the radiation attenuation (HU) each voxel or tissue have.</p>
<p>I’m planning to achieve this by getting the HU array of said DICOM file as well as its STL, and (somehow) import the HU array values to the STL, to get a new STL that also have different tissues densities. Then, I will obtain its G-Code and the 3D printer will use either “extrusion speed” or “linear motor speed” to vary these densities while printing.</p>
<p>Altough not entirely sure if this is the correct way, I think this should somehow work. But I’m open to suggestion and if I need to change the whole idea from its roots I will.</p>

---

## Post #4 by @lassoan (2023-06-04 15:35 UTC)

<p>Standard STL files cannot store densities (it cannot even store surface normals or color). Probably the best would be to use a multimaterial printer and the file format that it can take for modulation material properties.</p>
<p>However, if the idea is to but if your idea is to post-process the g-code based on position then I would recommend not try to export the density information to a surface mesh file (how would you know the density inside then?) but instead use the CT volume as input for your post-processing script. The reason is that a volume contains exactly what you need, it can tell the density of the material at any 3D position.</p>

---
