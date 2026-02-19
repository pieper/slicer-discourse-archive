---
topic_id: 29273
title: "Automatic Swi Venography Segmentation Using Vmtk"
date: 2023-05-03
url: https://discourse.slicer.org/t/29273
---

# Automatic SWI venography segmentation using VMTK

**Topic ID**: 29273
**Date**: 2023-05-03
**URL**: https://discourse.slicer.org/t/automatic-swi-venography-segmentation-using-vmtk/29273

---

## Post #1 by @OVSofia (2023-05-03 15:53 UTC)

<p>Hello,<br>
Does anyone know how I could use VMTK to automatically segment vessels from SWI images? (particularly .nii format) I have been trying to get the vessel segmentation using vmtk (and vtk), but so far I can not do it automatically since have to give the range of the threshold. Is there a way to automatically get the values of the threshold for each image? And if not, is there any other method to get the segmentation automatically?<br>
Thank you a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2023-05-10 04:35 UTC)

<p>You can use various segmentation tools in Segment Editor module. You can start with figuring out a good workflow for manual/semi-automatic segmentation tools and then automate it using Python scripting. Alternatively, you can segment a few hundred (but at least a few dozens) of cases and then train a fully automatic segmentation AI model using MONAILabel extension.</p>

---

## Post #3 by @OVSofia (2023-05-22 14:26 UTC)

<p>Thank you for your suggestions</p>

---
