---
topic_id: 8468
title: "Vmtk Vesselness Filtering Without Seed Point"
date: 2019-09-17
url: https://discourse.slicer.org/t/8468
---

# Vmtk Vesselness Filtering without seed point?

**Topic ID**: 8468
**Date**: 2019-09-17
**URL**: https://discourse.slicer.org/t/vmtk-vesselness-filtering-without-seed-point/8468

---

## Post #1 by @Tommaso_Di_Noto (2019-09-17 12:45 UTC)

<p>Hi everyone!</p>
<p>I was studying tutorials about vmtk and I saw the Vesselness Filtering module. I find it really useful for a single patient, and I manged to make it work by manually specifying the initial seed (fiducial) point.</p>
<p>But what if I have 300 cases? Is there a way to perform a batch filtering (ideally from command line) WITHOUT the manual seed (even less accurate, but automatic)?</p>
<p>Thanks a lot in advance!</p>

---

## Post #2 by @lassoan (2019-09-17 13:36 UTC)

<p>Seed point is used only to automatically compute min/max diameter and contrast setting. If you work with similar images then you can determine on a few images what values tend to work well and use those in all images.</p>

---

## Post #3 by @Tommaso_Di_Noto (2019-09-17 13:41 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
So to my next question…how can I run the tool from command line so that I can then encapsulate everything as subprocess in a python script looping over all my cases?</p>
<p>In other words, how can I access this  slicer module (and in general any module) from command line, knowing the args, etc?</p>
<p>Thanks again!</p>

---

## Post #4 by @lassoan (2019-09-17 13:48 UTC)

<p>It is a Python scripted module, so instead of old-school and platform-dependent bash/batch scripting, you can write a short Python script or <a href="https://github.com/Slicer/SlicerJupyter" rel="nofollow noopener">Jupyter notebook</a> to iterate through your data sets.</p>
<p>You can run vessel filtering by calling <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L460" rel="nofollow noopener">computeVesselnessVolume method</a> of the VesselnessFiltering module logic:</p>
<pre><code class="lang-python">import VesselnessFiltering
vfl=VesselnessFiltering.VesselnessFilteringLogic()
vfl.computeVesselnessVolume(inputVolumeNode, outputVolumeNode, minimumDiameterMm=0.2, maximumDiameterMm=25, alpha=0.3, beta=0.3, contrastMeasure=150)
</code></pre>

---

## Post #5 by @Tommaso_Di_Noto (2019-09-17 13:52 UTC)

<p>Ok great, that sounds even easier. I’ll give it a try and let you know how it goes.</p>
<p>Thank you very much again!</p>

---

## Post #6 by @Tommaso_Di_Noto (2019-09-17 14:43 UTC)

<p>So, I’ve opened a New-&gt;Slicer4.9 notebook using Binder but when I import VesselnessFiltering, I get:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
ImportError: No module named VesselnessFiltering
</code></pre>
<p>I tried running the example <code>01_Data_Loading_and_Visualization</code> and that works.</p>

---

## Post #7 by @lassoan (2019-09-17 16:06 UTC)

<p>VMTK extension is not installed in Slicer version that runs in Binder. You could <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Download_and_install_extension" rel="nofollow noopener">install it using a Python script</a>, but for batch processing, it would not be convenient to upload/download data anyway, so I would recommend to run the processing script on your local computer.</p>

---

## Post #8 by @Tommaso_Di_Noto (2019-09-18 15:10 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>, going through a local script on jupyter worked.</p>
<p>So, I’ve been trying the two following snippets and none of them work.</p>
<p><strong>Option 1</strong>:</p>
<pre><code>import numpy as np
import VesselnessFiltering
import SimpleITK as sitk
import sitkUtils as su

one_patient_path = "/home/newuser/.../sub-204_ses-20110825_angio_brain.nii.gz"
InputVolumeNode = slicer.util.loadVolume(one_patient_path, returnNode=True)

# Create output volume
OutputVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")  # add new node
OutputVolume.SetName("output_volume_trial")  # Set name for output volume
OutputVolume.CreateDefaultDisplayNodes()

vfl = VesselnessFiltering.VesselnessFilteringLogic()
vfl.computeVesselnessVolume(InputVolumeNode, OutputVolume, minimumDiameterMm=0, maximumDiameterMm=25, alpha=0.3, beta=0.3, contrastMeasure=150)
</code></pre>
<p>and this gives me the following error:</p>
<pre><code>File "/home/newuser/.config/NA-MIC/Extensions-27931/SlicerVMTK/lib/Slicer-4.10/qt-scripted- 
modules/VesselnessFiltering.py", line 492, in computeVesselnessVolume
inImage.DeepCopy(currentVolumeNode.GetImageData())
AttributeError: 'tuple' object has no attribute 'GetImageData'
</code></pre>
<p><strong>Option 2:</strong></p>
<pre><code># same imports...

# go through sitk
input_volume = sitk.ReadImage(one_patient_path)  # load nifti volume as sitk image
InputVolumeNode = su.PushVolumeToSlicer(input_volume, None)

# Create output volume
OutputVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")  # add new node
OutputVolume.SetName("output_volume_trial")  # Set name for output volume
OutputVolume.CreateDefaultDisplayNodes()
</code></pre>
<p>and in this case the last cell below never ends and the output volume is not created.</p>
<pre><code>vfl = VesselnessFiltering.VesselnessFilteringLogic()
vfl.computeVesselnessVolume(InputVolumeNode, OutputVolume, minimumDiameterMm=0, maximumDiameterMm=25, alpha=0.3, beta=0.3, contrastMeasure=150)
</code></pre>
<p>What am I doing wrong?</p>
<p>Thank you very much again!</p>

---

## Post #9 by @lassoan (2019-09-18 16:27 UTC)

<aside class="quote no-group quote-modified" data-username="Tommaso_Di_Noto" data-post="8" data-topic="8468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>inImage.DeepCopy(currentVolumeNode.GetImageData()) AttributeError: ‘tuple’ object has no attribute ‘GetImageData’</p>
</blockquote>
</aside>
<p>The problem is what the error message tells: <code>currentVolumeNode</code> is a Python <code>tuple</code>. It is not a MRML node. Maybe you used <code>slicer.util.loadVolume</code> in Slicer-4.10 and earlier, which returns a tuple of <code>(success, node)</code> instead of just the <code>node</code>. Check the API documentation.</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="8" data-topic="8468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>and in this case the last cell below never ends and the output volume is not created.</p>
<pre><code class="lang-auto">vfl = VesselnessFiltering.VesselnessFilteringLogic()
vfl.computeVesselnessVolume(InputVolumeNode, OutputVolume, minimumDiameterMm=0, maximumDiameterMm=25, alpha=0.3, beta=0.3, contrastMeasure=150)
</code></pre>
</blockquote>
</aside>
<p>Does this work with the same input and output volumes if you use the vesselness filtering module GUI? Is there any error displayed in the console? You can check the application log in Slicer or type the commands in the Python console in Slicer. If Slicer hangs then you can restart it and find logs of the previous sessions in menu: Help / Report a bug.</p>

---

## Post #10 by @Tommaso_Di_Noto (2019-09-19 08:23 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, apologies for not reading the API doc carefully. I now modified as:</p>
<pre><code>_, InputVolumeNode = slicer.util.loadVolume(one_patient_path, returnNode=True)
dim = InputVolumeNode.GetImageData().GetDimensions()
spacing = InputVolumeNode.GetSpacing()
</code></pre>
<p>and following <a href="https://discourse.slicer.org/t/display-issue-with-volume-node-created-programmatically/2346/2">this thread</a>, I created the Output Node with:</p>
<pre><code>def createEmptyVolume(imageSize, imageSpacing, nodeName):
    voxelType=vtk.VTK_FLOAT
    # Create an empty image volume
    imageData=vtk.vtkImageData()
    imageData.SetDimensions(imageSize)
    imageData.AllocateScalars(voxelType, 1)
    thresholder=vtk.vtkImageThreshold()
    thresholder.SetInputData(imageData)
    thresholder.SetInValue(0)
    thresholder.SetOutValue(0)
    thresholder.Update()
    # Create volume node
    volumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
    volumeNode.SetSpacing(imageSpacing)
    volumeNode.SetAndObserveImageData(thresholder.GetOutput())
    volumeNode.CreateDefaultDisplayNodes()
    volumeNode.CreateDefaultStorageNode()
    return volumeNode  

# creat output node with same dim and spacing of InputNode
OutputNode = createEmptyVolume(dim, spacing, 'VesselnessFiltered')  # invoke function 
</code></pre>
<p>Now, if I try to apply the VesselNessFiltering from the GUI with these two volumes (and with the manual seed point), the “VesselnessFiltered” volume is created correctly.</p>
<p>However, when I run in Jupyter:</p>
<pre><code>vfl = VesselnessFiltering.VesselnessFilteringLogic()
vfl.computeVesselnessVolume(InputVolumeNode, OutputVolume, minimumDiameterMm=0, maximumDiameterMm=25, alpha=0.3, beta=0.3, contrastMeasure=150) 
</code></pre>
<p>I get the following log in Slicer (from Help/Report a bug):</p>
<pre><code>[DEBUG][Python] 19.09.2019 10:04:22 [Python] (/home/newuser/.config/NA-MIC/Extensions-27931
SlicerVMTK/lib/Slicer-4.10/qt-scripted-modules/VesselnessFiltering.py:465) - Vesselness filtering 
started: diameter min=0, max=25, alpha=0.3, beta=0.3, contrastMeasure=150
[CRITICAL][Stream] 19.09.2019 10:04:23 [] (unknown:0) - ERROR: during execute_request
[CRITICAL][Stream] 19.09.2019 10:04:23 [] (unknown:0) - /work/Stable/Slicer-4101- 
build/ITK/Modules/Filtering/Smoothing/include/itkRecursiveGaussianImageFilter.hxx:344:
[CRITICAL][Stream] 19.09.2019 10:04:23 [] (unknown:0) - itk::ERROR: 
RecursiveGaussianImageFilter(0xb7ded90): Sigma must be greater than zero.
</code></pre>
<p>The [DEBUG] tells us that the VesselnessFiltering started, but then the <code>itkRecursiveGaussianImageFilter</code> raises the CRITICAL error about the Sigma. What I don’t understand is where, inside <code>computeVesselnessVolume</code>, this itk function is invoked.</p>
<p>Pardon me if the question is trivial, but how could I find this out? Or, in other words, how can I debug in  cases like this to understand what calls <code>itkRecursiveGaussianImageFilter</code>?</p>
<p>Thanks again for your time!</p>

---

## Post #11 by @lassoan (2019-09-19 12:12 UTC)

<aside class="quote no-group quote-modified" data-username="Tommaso_Di_Noto" data-post="10" data-topic="8468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>[CRITICAL][Stream] 19.09.2019 10:04:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - /work/Stable/Slicer-4101- build/ITK/Modules/Filtering/Smoothing/include/itkRecursiveGaussianImageFilter.hxx:344: [CRITICAL][Stream] 19.09.2019 10:04:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - itk::ERROR: RecursiveGaussianImageFilter(0xb7ded90): Sigma must be greater than zero.</p>
</blockquote>
</aside>
<p>This error message suggests that the minimum vessel diameter must be greater than zero. Default 0.0 value in computeVesselnessVolume method definition is misleading, it should be probably set to 0.2 (this value is used in the GUI).</p>

---

## Post #12 by @Tommaso_Di_Noto (2019-09-23 12:11 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>, thanks again for the tip!! It worked.</p>
<p>Finally, following several threads and examples, I think I managed to obtain what I wanted. Below, a code snippet for whomever might encounter a similar task (i.e. batch brain vessel extraction from MRA using VMTK and Jupyter Notebook). As the code is now, everything works, but please let me know in case you notice any imprecisions or avoidable passages (e.g. I’m not quite sure that the passage LabelNode–&gt;SegNode–&gt;LabelNodeAgain is very efficient):</p>
<pre><code># data_path is the folder where I have all my subfolders containing the MRA volumes

for subdir, dirs, files in os.walk(data_path):  # loop over folders and sub-folders
    for file in files:

        # load input volume
        input_volume_path = os.path.join(subdir,file)
        _, InputVolumeNode = slicer.util.loadVolume(input_volume_path, returnNode=True)  # load input volume
        dim_in = InputVolumeNode.GetImageData().GetDimensions()  # save input volume shape
        spacing_in = InputVolumeNode.GetSpacing()  # save input volume spacing
        
        # Create output volume with same dim and spacing of InputVolume
        OutputNode = createEmptyVolume(dim_in, spacing_in, 'VesselnessFiltered')  # invoke function
        
        # create vesselness filtering logic
        vfl = VesselnessFiltering.VesselnessFilteringLogic()  
        # compute VesselnessFiltering
        vfl.computeVesselnessVolume(InputVolumeNode, OutputNode, minimumDiameterMm=0.5, maximumDiameterMm=30, alpha=0.3, beta=0.3, contrastMeasure=130)
        
        # Create temporary labelmap from output volume
        labelVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
        slicer.vtkSlicerVolumesLogic().CreateLabelVolumeFromVolume(slicer.mrmlScene, labelVolumeNode, OutputNode)
        
        # Fill temporary labelmap by thresholding
        thresholdValue = 0.08  # set a threshold value
        voxelArray = slicer.util.arrayFromVolume(OutputNode)  # extract numpy array from output volume
        labelVoxelArray = slicer.util.arrayFromVolume(labelVolumeNode)  # extract numpy array from labelmap volume
        labelVoxelArray[voxelArray &lt; thresholdValue] = 0 # set all voxels below thr to 0
        labelVoxelArray[voxelArray &gt;= thresholdValue] = 1 # set all voxels above thr to 1
        
        # Import labelmap to segmentation
        segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')  # create segmentation node
        slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelVolumeNode, segmentationNode)
        segmentationNode.CreateClosedSurfaceRepresentation()  # make segmentation visible in 3D
        
        # Create segment editor to get access to effects
        segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
        segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
        segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
        segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
        segmentEditorWidget.setSegmentationNode(segmentationNode)
        segmentEditorWidget.setMasterVolumeNode(OutputNode)
        
        # Remove small islands from segmentation
        segmentEditorWidget.setActiveEffectByName("Islands")
        effect = segmentEditorWidget.activeEffect()
        effect.setParameter('Operation','REMOVE_SMALL_ISLANDS')  # remove islands smaller than a certain dimension
        effect.setParameter('MinimumSize', 170)
        effect.self().onApply()
        
        # Clean up
        segmentEditorWidget = None
        slicer.mrmlScene.RemoveNode(segmentEditorNode)  # remove segmentation editor node
        slicer.mrmlScene.RemoveNode(labelVolumeNode)  # remove temporary LabelMapVolume but keep segmentation node
        
        # Convert again from segmentation node to labelnode matching input volume dimensions
        reference = getNode("VesselnessFiltered") # this will be the volume the segmentation was drawn on
        labelmapVolumeNodeClosed = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
        seg = getNode("Segmentation")  # set segmentation node            
        ids = vtk.vtkStringArray()
        seg.GetDisplayNode().GetVisibleSegmentIDs(ids)
        smsl = slicer.modules.segmentations.logic()
        smsl.ExportSegmentsToLabelmapNode(segmentationNode,ids,labelmapVolumeNodeClosed,reference)
        
        dim_out_lab = labelmapVolumeNodeClosed.GetImageData().GetDimensions()  # save output shape
        spacing_out_lab = labelmapVolumeNodeClosed.GetSpacing()  # save output spacing
        
        # make sure that shape and spacing match from input to final output nodes
        assert(dim_in == dim_out_lab)
        assert(spacing_in == spacing_out_lab)
        
        # save final node
        file_name = os.path.basename(file)
        index_of_dot = file_name.index('.')
        file_name_without_extensions = file_name[:index_of_dot]  # remove extensions
        output_file_path = os.path.join(subdir, file_name_without_extensions) + "_vessels.nii.gz"
        
        slicer.util.saveNode(labelmapVolumeNodeClosed, output_file_path)  # save output node
        print("Vessel mask saved for {0}".format(file))
        
        # clear Slicer scene (it removes all volumes)
        slicer.mrmlScene.Clear(0)
</code></pre>
<p>P.S. if you modify the minimum diameter to 0.2 in your <a href="https://discourse.slicer.org/t/vmtk-vesselness-filtering-without-seed-point/8468/4">first answer</a>, I think we can (I can) mark it as “Solution” answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #13 by @Tommaso_Di_Noto (2020-02-20 16:18 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Is there, to your knowledge, a way to obtain a smoothed (i.e. probabilistic) vesselness filtering rather than  a binary one as in this post, either in VMTK or with another software?</p>
<p>Thanks a lot in advance!</p>

---

## Post #14 by @lassoan (2020-02-20 18:58 UTC)

<p>VMTK’s vesselness filter computes a probablilistic image with values is between 0.0 and 1.0. By default we display the computed vesselness image by applying a threshold value in display options, so it may appear binary, but it is actually not.</p>

---

## Post #15 by @Tommaso_Di_Noto (2020-02-21 10:53 UTC)

<p>Oh, you are right!</p>
<p>The <code>OutputNode</code> in the example is indeed probabilistic after applying <code>vfl.computeVesselnessVolume</code>, so I can just save that.</p>
<p>Thanks a lot, as usual, for the super quick answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
