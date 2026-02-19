---
topic_id: 282
title: "View Save Noddi Output"
date: 2017-05-08
url: https://discourse.slicer.org/t/282
---

# View/save NODDI output

**Topic ID**: 282
**Date**: 2017-05-08
**URL**: https://discourse.slicer.org/t/view-save-noddi-output/282

---

## Post #1 by @mrjeffs (2017-05-08 14:24 UTC)

<p>how do i look at and save the NODDI intra-cellular and volume fractions. are they imbedded in the vtk? how to view?<br>
do i need to run the UKF before NODDI? seemed to successfully complete directly…here is the error free comand:</p>
<p>UKF Tractography command line:</p>
<p>/home/toddr/.config/NA-MIC/Extensions-25993/UKFTractography/lib/Slicer-4.7/cli-modules/UKFTractography --dwiFile /tmp/Slicer/IEAC_vtkMRMLDiffusionWeightedVolumeNodeB.nhdr --seedsFile /tmp/Slicer/IEAC_vtkMRMLLabelMapVolumeNodeC.nhdr --labels 1 --maskFile /tmp/Slicer/IEAC_vtkMRMLLabelMapVolumeNodeB.nhdr --tracts /tmp/Slicer/IEAC_vtkMRMLFiberBundleNodeB.vtp --seedsPerVoxel 1 --seedFALimit 0.18 --minFA 0.15 --minGA 0.1 --numThreads -1 --numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 250 --Ql 0 --Qw 0 --noddi --recordVic --recordKappa --recordViso --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 --minBranchingAngle 0</p>

---

## Post #2 by @ljod (2017-05-08 14:42 UTC)

<p>Since you saved them using --recordViso and other record flags, they will be stored in the vtk file. Please see the tutorial on “Slicer Fiber Bundle Selection and Scalar Measurements tutorial” here for information on how to extract these measures into a spreadsheet:<br>
<a href="http://dmri.slicer.org/docs/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/docs/</a><br>
If instead you would like to visualize the measures, you can do this in Tractography Display.</p>

---

## Post #3 by @mrjeffs (2017-05-08 16:18 UTC)

<p>Thanks for the links, tractoghphy display has all advanced options disabled. So selecting vol fraction and lit in pull down like FA for tensor fit isn’t available.</p>

---

## Post #4 by @ljod (2017-05-08 17:57 UTC)

<p>Hi please let us know more information. For example which version of Slicer you are using? Are you able to use the top panel of tractography display and does the vtk file show on this menu? Have you both loaded the vtk as a Fiber Bundle and also installed SlicerDMRI?</p>

---

## Post #5 by @mrjeffs (2017-05-08 18:17 UTC)

<p>using 4.7.0-2017-04-29 with all the diffusion extensions enabled, under tractography i do not see the fibertract scalar measurements option. looks like they all require a tensor to function. how do i set the interface noddi to create volumes directly?</p>

---

## Post #6 by @ljod (2017-05-08 22:41 UTC)

<p>Hi please share a small example vtk file if possible so I can take a look. I do not know why the advanced display would be disabled. Does this happen also for other tractography vtk files? Has it happened in other versions of Slicer?</p>
<p>The scalar measurements should be under Quantify-&gt;Tractography Measurements. This module is to make quantitative measures (e.g. mean of all values stored in tracts) not to visualize.</p>
<p>The UKF tractography module does not produce volumes, just fiber tracts.</p>

---

## Post #7 by @ihnorton (2017-05-09 12:40 UTC)

<p>looks like you are missing <code>--recordTensor</code>?</p>

---

## Post #8 by @ljod (2017-05-11 18:54 UTC)

<p>Does this indicate the advanced options are disabled if tensors are missing? This does not make sense with other models such as NODDI, or even with tensors because still other values are often stored along the tracts.</p>

---
