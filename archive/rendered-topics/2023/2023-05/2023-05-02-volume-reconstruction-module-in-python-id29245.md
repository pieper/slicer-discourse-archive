---
topic_id: 29245
title: "Volume Reconstruction Module In Python"
date: 2023-05-02
url: https://discourse.slicer.org/t/29245
---

# Volume Reconstruction Module in python

**Topic ID**: 29245
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/volume-reconstruction-module-in-python/29245

---

## Post #1 by @Albags (2023-05-02 13:59 UTC)

<p>Hi 3D Slicer team,</p>
<p>I am trying to create a new module in python and for one of the functionalities that I want to implement I need as an input a reconstructed volume of live ultrasound data. I saw that I can reconstruct live data using the “Volume Reconstruction” module, however I was wondering if it is possible to implement that module, or the main functions of the module, in my new module, so most of the parameters are hardcoded and I only need to press a “start” button in my module to get the reconstructed volume.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @Sunderlandkyl (2023-05-02 15:11 UTC)

<p>Volume reconstruction can be controlled outside of the module by setting parameters on the “<a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/VolumeReconstruction/MRML/vtkMRMLVolumeReconstructionNode.h" rel="noopener nofollow ugc">vtkMRMLVolumeReconstructionNode</a>”, and calling methods on the <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/VolumeReconstruction/Logic/vtkSlicerVolumeReconstructionLogic.h" rel="noopener nofollow ugc">vtkSlicerVolumeReconstructionLogic</a>.</p>
<p>In the case of live volume reconstruction, you would set the input image, ROI, and output volume and then call:</p>
<pre><code class="lang-auto">slicer.modules.volumereconstruction.logic().StartLiveVolumeReconstruction(volumeReconstructionNode)
...
slicer.modules.volumereconstruction.logic().StopLiveVolumeReconstruction(volumeReconstructionNode)
</code></pre>

---

## Post #3 by @Albags (2023-05-02 16:17 UTC)

<p>Thank you very much for the fast answer! It works <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
