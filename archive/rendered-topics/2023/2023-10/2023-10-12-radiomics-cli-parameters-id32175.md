---
topic_id: 32175
title: "Radiomics Cli Parameters"
date: 2023-10-12
url: https://discourse.slicer.org/t/32175
---

# Radiomics cli parameters

**Topic ID**: 32175
**Date**: 2023-10-12
**URL**: https://discourse.slicer.org/t/radiomics-cli-parameters/32175

---

## Post #1 by @Saima (2023-10-12 05:23 UTC)

<p>Hi,<br>
I am trying to do batch processing to extract radiomic features using the radiomicscli module. The error are:<br>
/media/useradmin/Disk2/Nathaniel/Testing_radiomics/APT034</p>
<p>[VTK] No input data assigned to “input Source Image”</p>
<p>[VTK] No input data assigned to “input Source Image”</p>
<p>[VTK] No input data assigned to “input Source Image”</p>
<p>[VTK] No input data assigned to “input Source Image”</p>
<p>Below is the code to run the cli module. could anyone please help me in this regard. did i define the correct params for the radiomics cli module.</p>
<p>apt_data = slicer.util.loadVolume(startPatientDirPath+“/T1c.nii.gz”)</p>
<pre><code>        #segmentation of the tumour loaded as volume and then converted to segmnetation node
        seg = slicer.util.loadSegmentation(startPatientDirPath+"/outputFinal/transSimple-label.nrrd")
        #seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
        #slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, seg)
        
        params = {}
        params["image"] = slicer.util.getNode(apt_data.GetID())
        params["mask"] = slicer.util.getNode(seg.GetID())
        params["out"] = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
        
        for i in range(1,4):
            if i == 3:
                continue;
            params["label"] = i
            cliModule = slicer.modules.slicerradiomicscli
            cliNode = slicer.cli.runSync(cliModule, None, params)
        slicer.mrmlScene.RemoveNode(cliNode)
</code></pre>

---

## Post #2 by @Saima (2023-10-12 05:57 UTC)

<p>Hi,<br>
i found the problem was with the params. It is<br>
params[“Image”] = slicer.util.getNode(apt_data.GetID())<br>
params[“Mask”] = slicer.util.getNode(seg.GetID())</p>
<p>Now i am having problem figuring out the table node. I want only one table and all the features extracted in one table in different rows. Also I wanted to add a column in table which specifies the label from which it is extracting the features and the patient ID.</p>
<p>Any help?</p>
<p>thank you so much.</p>
<p>regards.<br>
saima</p>

---
