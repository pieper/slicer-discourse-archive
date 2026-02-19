---
topic_id: 25566
title: "Spharm Pdm Segpostprocess Produces Errors"
date: 2022-10-05
url: https://discourse.slicer.org/t/25566
---

# SPHARM-PDM SegPostProcess produces errors

**Topic ID**: 25566
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/spharm-pdm-segpostprocess-produces-errors/25566

---

## Post #1 by @aohowens (2022-10-05 22:42 UTC)

<p>I’ve been trying to run SPHARM-PDM on some limb bones - both adult and embryonic. I need the post processing step to fill holes in the adult bone before I can move on to the next step, but for the embryonic bones I’ve been able to skip the post processing step because they are already fully closed and solid. However, whenever I run SegPostProcess using default parameters on either the adult or embryonic bones, I get an error, which I’ve pasted below. I’m not sure how to solve this, and I’m not sure if it’s alright to proceed to the next steps for my embryonic samples that don’t seem to need SegPostProcess.</p>
<p>Thanks!<br>
-Aidan</p>
<p>The error:<br>
Found CommandLine Module, target is  /Applications/Slicer.app/Contents/Extensions-30893/SPHARM-PDM/lib/Slicer-5.0/cli-modules/SegPostProcessCLP<br>
ModuleType: CommandLineModule<br>
SegPostProcess command line:</p>
<p>/Applications/Slicer.app/Contents/Extensions-30893/SPHARM-PDM/lib/Slicer-5.0/cli-modules/SegPostProcessCLP --var 1.0,1.0,1.0 --RMS 0.01 --iter 50 --label 1 --space 0.75,0.75,0.75 --WM 1 --GM 2 --CSF 3 --MWM -1 /private/var/folders/_7/1pgsgwjx47j5f85fll81r0s40000gn/T/Slicer-aohowens/IJJGF_vtkMRMLLabelMapVolumeNodeF.nrrd /private/var/folders/_7/1pgsgwjx47j5f85fll81r0s40000gn/T/Slicer-aohowens/IJJGF_vtkMRMLLabelMapVolumeNodeG.nrrd</p>

---
