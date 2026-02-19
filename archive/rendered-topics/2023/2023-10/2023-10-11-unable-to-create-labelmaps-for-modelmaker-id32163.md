---
topic_id: 32163
title: "Unable To Create Labelmaps For Modelmaker"
date: 2023-10-11
url: https://discourse.slicer.org/t/32163
---

# Unable to create LabelMaps for ModelMaker

**Topic ID**: 32163
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/unable-to-create-labelmaps-for-modelmaker/32163

---

## Post #1 by @BlancaRodriguez (2023-10-11 16:53 UTC)

<p>Hello!</p>
<p>My team and I are currently working in a segmentation project, and have been actively using Slicer. However, we are currently facing some challenges and hope we can get some help from the community.</p>
<p>Specifically, we are trying to generate some <em>vtk volumes</em> from a .nii.gz storing the segmentations done by a DL models. This file contains integer values for each label.  In order to generate the vtk model, we have decided to use the ModelMaker module.</p>
<p>Due to the big number of data we are dealing with, we’ve been using <strong>linux terminal</strong> to automatize the proccess. However, when doing so, models are not being generated. After debugging the process, we realized that our images are not being understood as LabelMaps and, therefore, ModelMaker can’t work with our images. To solve this issue, we have renamed our files as {name}_Label.nii.gz. Although this approach seems to work when using the user’s interface, models are yet not generated when working from terminal.</p>
<p>Is there a way we can <em>transform</em> our original volumes into labelmaps from linux terminal??</p>
<p>Maybe there is a simpler method to generate our models that we are missing out.</p>
<p>Thanks a lot for your help!!</p>

---

## Post #2 by @pieper (2023-10-11 17:56 UTC)

<p>You can use <code>slicer.util.loadLabelVolume()</code> to load as a label volume.  If you are still having trouble you can post your exact script and the command line you execute to run it and we can probably give more targeted advice.</p>

---
