# How to clean up temp file after cropping volume

**Topic ID**: 12939
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/how-to-clean-up-temp-file-after-cropping-volume/12939

---

## Post #1 by @ungi (2020-08-11 01:55 UTC)

<p>Hi,<br>
I have a script that automatically crops (and resamples) my volumes in Slicer. It works fine, but every time it runs, it leaves a copy of the original volume in the temp folder. In my case, here:<br>
c:\Users\tamas\AppData\Local\Temp\Slicer\</p>
<p>I just realized that this folder was over 100 GB today. I’m not sure if this would be cleaned up automatically after a while. But I would prefer a way to clean it up from my python script immediately after resampling my volumes.<br>
Does anybody know how to clean up the temp folder of Slicer?<br>
Or prevent the crop volume logic to create these large temp files? (I have lots of RAM.)</p>
<p>Here is a minimal script to reproduce the issue. You will need the MRHead image and a ROI in the scene to run this:</p>
<pre><code>inputVolume = slicer.util.getNode('MRHead')
roi = slicer.util.getNode('R')

cropVolumeNode = slicer.vtkMRMLCropVolumeParametersNode()
cropVolumeNode.SetScene(slicer.mrmlScene)
slicer.mrmlScene.AddNode(cropVolumeNode)

cropVolumeNode.SetInputVolumeNodeID(inputVolume.GetID())
cropVolumeNode.SetROINodeID(roi.GetID())
# cropVolumeNode.SetOutputVolumeNodeID(outputVolume.GetID()) # This is optional

cropVolumeLogic = slicer.modules.cropvolume.logic()
cropVolumeLogic.Apply(cropVolumeNode)
</code></pre>
<p>Thanks,<br>
Tamas</p>

---

## Post #2 by @lassoan (2020-08-11 02:30 UTC)

<p>CLI module inputs/outputs are preserved if developer mode is enabled in application settings. You can override this setting by calling <code>DeleteTemporaryFilesOn()</code> for a specific CLI module’s logic.</p>
<p>Probably we should make this a separate checkbox within the developer section in application settings.</p>

---

## Post #3 by @ungi (2020-08-11 04:14 UTC)

<p>Thank you!<br>
It took me a while to figure out, but I realize now that the logic of the crop volume module has a CLI module in it:<br>
<code>slicer.modules.cropvolume.logic().GetResampleLogic().DeleteTemporaryFilesOn()</code></p>

---

## Post #4 by @lassoan (2020-08-11 04:41 UTC)

<p>I’ve added a separate option to control deletion of CLI temporary files in application settings / Developers section: “Preserve CLI module data files”. It’ll be available in tomorrow’s Preview Release.</p>

---

## Post #5 by @ungi (2020-08-11 04:44 UTC)

<p>Thank you for adding this option!</p>

---
