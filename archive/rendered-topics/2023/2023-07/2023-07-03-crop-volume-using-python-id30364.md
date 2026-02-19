---
topic_id: 30364
title: "Crop Volume Using Python"
date: 2023-07-03
url: https://discourse.slicer.org/t/30364
---

# Crop volume using python

**Topic ID**: 30364
**Date**: 2023-07-03
**URL**: https://discourse.slicer.org/t/crop-volume-using-python/30364

---

## Post #1 by @Mani_Barathi (2023-07-03 11:48 UTC)

<p>why some dicom data are not cropped in 3d slicer? Once after setting the ROI and click apply button, its not cropping the selected region. Please help to resolve this issue.</p>

---

## Post #2 by @rbumm (2023-07-03 14:46 UTC)

<p>Please explain <strong>in detail</strong> what you are trying to achieve, which 3D Slicer version you use, and which extension you use. Why is “using Python” in your title and not in your question?</p>
<p>If you want to crop a volume in 3D Slicer 5.2.2 you will want to use the “Crop Volume” model. Create a new ROI. Set the parameters. Press “Apply”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14552b31af10b6f51b7c916881b3d665ee1c7d0.jpeg" data-download-href="/uploads/short-url/yqnAQyDtcnkzLwi44bJJ0Yi14Yw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f14552b31af10b6f51b7c916881b3d665ee1c7d0_2_690x295.jpeg" alt="image" data-base62-sha1="yqnAQyDtcnkzLwi44bJJ0Yi14Yw" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f14552b31af10b6f51b7c916881b3d665ee1c7d0_2_690x295.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f14552b31af10b6f51b7c916881b3d665ee1c7d0_2_1035x442.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f14552b31af10b6f51b7c916881b3d665ee1c7d0_2_1380x590.jpeg 2x" data-dominant-color="9D9CA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1868×799 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Mani_Barathi (2023-07-04 10:22 UTC)

<p>We are trying to crop the dicom to segment specific regions of brain. We can’t do the ROI based cropping  for some of the datasets. We are able to set ROI and set parameters. But when we click the apply button it is not cropping the ROI region. We tried this both manually and with python scripting. But we couldn’t make it. Please help me.</p>

---

## Post #4 by @rbumm (2023-07-04 12:11 UTC)

<p>GPT-4:</p>
<p>Here are a few potential solutions:</p>
<ol>
<li>
<p><strong>Check for software updates</strong>: Check if you have the latest stable version. If not, you may need to update or try a nightly build which might have the issue fixed.</p>
</li>
<li>
<p><strong>Verify that the region of interest (ROI) is correctly defined</strong>: Make sure the ROI you’re trying to crop is correctly placed and defined in your data. If the ROI is outside the image boundaries or not properly aligned with the data, it could cause issues.</p>
</li>
<li>
<p><strong>Investigate data issues</strong>: The problem could be with the data itself. It might be worth checking if there are any unusual features of the datasets where cropping isn’t working. For example, they could have different orientations, voxel sizes, or other metadata compared to the datasets where cropping works.</p>
</li>
<li>
<p><strong>ROI not visible</strong>: It might be that your ROI is being cropped, but it’s not immediately visible in the view you’re looking at. Try adjusting the view settings or zooming out to see if the cropped ROI appears.</p>
</li>
<li>
<p><strong>Reinstall 3D Slicer</strong>: If all else fails, you might need to reinstall 3D Slicer to make sure there are no issues with the installation.</p>
</li>
</ol>
<p>In case you’re looking for a sample Python script to crop volumes based on ROI, here’s a basic example (untested)</p>
<pre><code class="lang-python"># Get the current active volume node
inputVolume = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')

# Create a new ROI node
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")

# Set the ROI to encompass the whole input volume
roiNode.Initialize(slicer.vtkMRMLAnnotationROINode.PlaceWidget, inputVolume)

# Now let's crop the volume
cropVolumeNode = slicer.modules.cropvolume.logic()

# Create a new output volume node
outputVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")

# Set parameters
cropVolumeNode.SetInputVolume(inputVolume.GetID())
cropVolumeNode.SetROINode(roiNode.GetID())
cropVolumeNode.SetOutputVolumeNode(outputVolume.GetID())

# Apply cropping
cropVolumeNode.Apply()
</code></pre>
<p>Please replace <code>'vtkMRMLScalarVolumeNode1'</code> with the ID of your current active volume node. Also, this script assumes that you want to crop the whole volume. You will need to adjust the ROI position and size if you want to crop a specific area. Please ensure you have the correct volume and ROI IDs.</p>

---

## Post #5 by @Celina_Amber_Gilmore (2024-02-29 19:21 UTC)

<p>Thank you for the previous questions and clarifying how to use Python script to crop volume. We manually created ROI regions and are trying to crop them using Python script. We assigned inputROI using getNode(“nameOfROIBox”) and used the code above to create a new outputVolume node. The problem we are having is with the inputVolume. How do we set inputVolume? When we tried using the code above, we had trouble knowing how to access the ID of our current active volume node.</p>
<p>Additionally, running these three lines of codes results in AttributeErrors saying the following…</p>
<h1><a name="p-107652-set-parameters-1" class="anchor" href="#p-107652-set-parameters-1" aria-label="Heading link"></a>Set parameters</h1>
<p>cropVolumeNode.SetInputVolume(inputVolume.GetID())<br>
cropVolumeNode.SetROINode(roiNode.GetID())<br>
cropVolumeNode.SetOutputVolumeNode(outputVolume.GetID())</p>
<ol>
<li>‘vtkSlicerCropVolumeModuleLogicPython.vtkSlicerCrop’ object has no attribute ‘SetROINode’</li>
<li>‘vtkSlicerCropVolumeModuleLogicPython.vtkSlicerCrop’ object has no attribute ‘SetInputVolume’</li>
<li>‘vtkSlicerCropVolumeModuleLogicPython.vtkSlicerCrop’ object has no attribute ‘SetOutputVolumeNode’</li>
</ol>
<p>Thank you for helping us with this!</p>

---

## Post #6 by @mikebind (2024-02-29 19:43 UTC)

<p>That would be because the ChatGPT-generated code supplied above is not correct. This slightly modified code from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">Slicer script repository</a> should get you started:</p>
<pre><code class="lang-auto">ct = getNode('myImageName')
roi = getNode('myROIName')
cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolumeParameters.SetInputVolumeNodeID(ct.GetID())
cropVolumeParameters.SetROINodeID(roi.GetID())
slicer.modules.cropvolume.logic().Apply(cropVolumeParameters)
croppedCT = cropVolumeParameters.GetOutputVolumeNode()
</code></pre>

---

## Post #7 by @chir.set (2024-02-29 19:58 UTC)

<aside class="quote no-group" data-username="Celina_Amber_Gilmore" data-post="5" data-topic="30364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/celina_amber_gilmore/48/69534_2.png" class="avatar"> Celina_Amber_Gilmore:</div>
<blockquote>
<p>How do we set inputVolume?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Celina_Amber_Gilmore" data-post="5" data-topic="30364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/celina_amber_gilmore/48/69534_2.png" class="avatar"> Celina_Amber_Gilmore:</div>
<blockquote>
<p>these three lines of codes results in AttributeErrors</p>
</blockquote>
</aside>
<p>You may find a function <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/master/00-Lib.py.txt?ref_type=heads#L70" rel="noopener nofollow ugc">here</a> to crop volumes using Python.</p>
<p>To get any node in Slicer, use a qMRMLNodeComboBox as a GUI widget. You will have to go through the API to know how to use it.</p>
<p>If you just want to draw a ROI and crop a volume, you may consider implementing <a href="https://gitlab.com/chir-set/RcHacks7/" rel="noopener nofollow ugc">this</a> project. It’s just copy and paste.</p>
<p>If you want to go deeper and do things yourself, you’ll have to go through scripting basics and get familiar with <a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html" rel="noopener nofollow ugc">Slicer’s internals</a>.</p>
<p>Good luck.</p>

---

## Post #8 by @Celina_Amber_Gilmore (2024-02-29 20:10 UTC)

<p>Thank you for providing reference to the script. The modified script was a tremendous help! The code worked. Now that we have the cropped volume from running the script, is there a way to write another line of code that automatically renames the obtained cropped volume for us?</p>

---

## Post #9 by @mikebind (2024-02-29 20:13 UTC)

<p>This should work:<br>
<code>croppedCT.SetName('myNewName')</code></p>

---

## Post #10 by @Celina_Amber_Gilmore (2024-03-07 01:26 UTC)

<p>Hi again. We are integrating our code into Jupyter notebook, since the Python Console in Slicer is inconvenient to use directly. The code we previously had works in Slicer but now we have to adapt it to run in Jupyter notebook, and we encountered an error in recognizing the CT scan files we are working with. When we run the following lines of code, the second line is able to perform the getNode function on the given ROI. However, the first line gives us the following error message: <strong>MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘substack_name’</strong></p>
<p>ct = slicer.util.getNode(“substack_name”)<br>
roi = slicer.util.getNode(“ROI_name”)</p>
<p>What is the function to be able to get the substack in Jupyter notebook?</p>

---
