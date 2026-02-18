# Two markupsROI (Cropping module)

**Topic ID**: 39956
**Date**: 2024-10-31
**URL**: https://discourse.slicer.org/t/two-markupsroi-cropping-module/39956

---

## Post #1 by @Dawid_Szczawinski (2024-10-31 14:35 UTC)

<p>Hello everyone!<br>
I try to create my own extension to using nnunetv2 model.<br>
First step is cropping data, because segmentation full file is not necessary and I have too little ram.<br>
So I try to cropp Volume using ROI.<br>
Is it normally that I receive two markups after click Create new ROI?<br>
I guess that vtkMRMLMarkupsROINode both and vtkMRMLCropVolumeParametersNode causes create new markups.<br>
I would like the user to be able to interactively select the area to be cropped.<br>
Code responsible for marking area:</p>
<pre data-code-wrap="python"><code class="lang-python">def onCreateNewROI(self):
        if not self._parameterNode.inputVolume:
            slicer.util.errorDisplay("Proszę wybrać obraz wejściowy przed 
            utworzeniem ROI.")
            return

        if not self._parameterNode.roinode:
            self._parameterNode.roinode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
            slicer.util.infoDisplay("Nowy ROI został utworzony. Możesz teraz edytować ROI na obrazie.")
        

        if not self._parameterNode.cropVolume:
            self._parameterNode.cropVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
        
        self._parameterNode.cropVolume.SetInputVolumeNodeID(self._parameterNode.inputVolume.GetID())
        self._parameterNode.cropVolume.SetOutputVolumeNodeID(self._parameterNode.inputVolume.GetID())  
        self._parameterNode.cropVolume.SetROINodeID(self._parameterNode.roinode.GetID())

        slicer.modules.cropvolume.logic().FitROIToInputVolume(self._parameterNode.cropVolume)
        
        slicer.util.infoDisplay("Nowy ROI został utworzony. Możesz teraz edytować ROI na obrazie.")
</code></pre>

---

## Post #2 by @lassoan (2024-10-31 14:43 UTC)

<p>The code above looks good, it only creates a single ROI node. I’ve tested it on this snippet created from your code above:</p>
<pre data-code-wrap="python"><code class="lang-python">inputVolume  = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
roinode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")

cropVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolume.SetInputVolumeNodeID(inputVolume.GetID())
cropVolume.SetOutputVolumeNodeID(inputVolume.GetID())  
cropVolume.SetROINodeID(roinode.GetID())

slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolume)
</code></pre>
<p>If you get two ROI nodes that is due to some issues somewhere else in your module.</p>
<p>I’ve noticed the Polish text in your module. Note that Slicer has an internationalization framework, so you can develop modules that can be translated to any language. You can find more information <a href="https://github.com/Slicer/SlicerLanguagePacks/blob/main/DevelopersManual.md">here</a>.</p>

---

## Post #3 by @Dawid_Szczawinski (2024-10-31 16:24 UTC)

<p>Thank you for your feedback!<br>
All time when I first time use this function (eg. after restart Slicer) create two MarkupsRoi<br>
First in this part:</p>
<pre><code>   if not self._parameterNode.roinode:
        self._parameterNode.roinode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
        slicer.util.infoDisplay("Nowy ROI został utworzony. Możesz teraz edytować ROI na obrazie.")
</code></pre>
<p>and second in this part:</p>
<pre><code>    if not self._parameterNode.cropVolume:
        self._parameterNode.cropVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode") 
</code></pre>
<p>First of created Markups does not have visualization.<br>
Interesting is that when I create next Roi is only one.</p>
<p>To activate this function I use connection:</p>
<p>self.ui.roiSelector.connect(“nodeAddedByUser(vtkMRMLNode*)”,<br>
self.onCreateNewROI)</p>

---
