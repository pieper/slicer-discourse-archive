# Segmentation of Mitral valve

**Topic ID**: 14598
**Date**: 2020-11-14
**URL**: https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598

---

## Post #1 by @lorenzo_bennati (2020-11-14 13:34 UTC)

<p>Hi to everyone.<br>
I’m new to 3D Slicer. I have a sequence of Cine-MRI images of 18 evenly rotated long-axis (one every 10°) planes around the axis passing through the annular center of the mitral valve and  aligned with the left ventricle. So i have only 2D slices in time.</p>
<p>My question if in Slicer 3D it is possible to segment for example the mitral valve starting from this kind of acquisition.</p>
<p>To better understand i have attached two images representing of my Cine-MRI Images  acquisition protocol.</p>
<p>Any help would be appreciated.</p>
<p>Thanks.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e930192218af8ee346c1ae429b1e10ec2447845.jpeg" alt="Pic" data-base62-sha1="4mthz24wkw8p4zAHrqXDXFb0AVn" width="524" height="466"></p>

---

## Post #2 by @lassoan (2020-11-14 15:31 UTC)

<p>We do a lot of heart valve and leaflet segmentations on various imaging modalities (ultrasound, MRI, CT), so we should able to help with this.</p>
<p>There are a few options for segmenting the leaflets from such time series:</p>
<p>A. Reconstruct volume(s) from the slices. SlicerIGT extension can reconstruct a Cartesian volume from a set of arbitrarily oriented slices and then you can segment the leaflets as usual (using Segment Editor module). This may require conversion of input MRI into a format that the volume reconstructor module can interpret, which may not be as trivial so if you want to try this option then we would probably need a sample data set (it can be taken of a phantom or any other object, you just need to use the exact same imaging protocol as for patient images).</p>
<p>B. Segment individual frames. Create an empty segmentation and segment the leaflet in each slice. This requires that you load the DICOM series as a “volume sequence”. By default it may be loaded as “multi-volume” in that case you need to change the default setting in menu: Edit / Application settings / DICOM.</p>
<p>C. You may be able to load it as a scalar volume, as the loader supports image interpolation between arbitrarily oriented slices. You need to split the series by content time (an option that you need to enable in Application settings), and then choose the time points you want to load in DICOM module (by enabling “Advanced” option).</p>
<p>None of these options are completely straightforward to learn but they should work well. You can either experiment with them on your own (and we help with advice when you get stuck), or you can share a data set and we figure out what works best and give you step-by-step instructions that you can follow.</p>

---

## Post #3 by @lorenzo_bennati (2020-11-14 15:43 UTC)

<p>Hi <span class="mention">@Iassoan</span>,</p>
<p>Thank you very much for your answer and for providing me with 3 different strategies.<br>
I start immediately with trying them.<br>
In the meantime, I share a OneDrive link to the Cine-MRI images I refer to.</p>
<p>Thanks again</p>
<p>Link: <em>(link is removed due to potentially containing patient identifiable information)</em></p>
<p>Lorenzo</p>

---

## Post #4 by @lassoan (2020-11-16 05:01 UTC)

<p>I had a look at the data set and tried all 3 methods.</p>
<p>Method C does not work because slices intersect each other and therefore cannot be interpolated using a grid transform.</p>
<p>Method B somewhat worked (I had to slightly improve the DICOM importer, the update will be available in tomorrow’s Slicer Preview Release). Since the the volume is quite sparse and the leaflet visibility is not always great, segmenting the leaflets like this can be quite challenging (you need to keep browsing the slices to get the necessary spatial and temporal context for interpreting the current slice).</p>
<p>Method A seems to be the most promising. Volume reconstruction module in SlicerIGSIO extension can manage to fill in the gaps between the slices and creates a full 3D volume, which can be visualized directly using volume rendering, segmented using the common segmentation tools, etc.</p>
<p>This is how the reconstructed 4D volume sequence looks like:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="OLuPh8Q-XUk" data-video-title="4D volume reconstruction from sparse rotational cardiac cine MRI" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=OLuPh8Q-XUk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/OLuPh8Q-XUk/hqdefault.jpg" title="4D volume reconstruction from sparse rotational cardiac cine MRI" width="" height="">
  </a>
</div>

<p>Farther from the mitral vale the gap between slices becomes too large, the holes cannot be filled anymore, but that could be addressed by changing the reconstruction parameters (and probably those areas are not interesting anyway).</p>
<p>You need to reconstruct the frames in groups, which requires reorganizing the sequence. Doing this manually for hundreds of frames would takes tens of minutes, so I wrote a script to automate this. You can load the MRI image series, define a ROI box to define where you want to reconstruct the volume, and run this script to get the result that is shown in the video above. It requires Slicer Preview Release downloaded tomorrow or later and installation of SlicerIGSIO and SlicerIGT extension.</p>
<pre><code class="lang-python"># Set inputs
inputVolumeSequenceNode = slicer.util.getFirstNodeByClassByName('vtkMRMLSequenceNode', 'Sequence')
inputVolumeSequenceBrowserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(inputVolumeSequenceNode)
inputVolumeSequenceBrowserNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSequenceBrowserNode')
roiNode = slicer.util.getNode('R')  # Draw an Annotation ROI box that defines the region of interest before running this line
numberOfTimePoints = 30
numberOfInstancess = 540
startInstanceNumbers = range(1,numberOfTimePoints+1)

# Helper function
def reconstructVolume(sequenceNode, roiNode):
    # Create sequence browser node
    sequenceBrowserNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceBrowserNode', 'TempReconstructionVolumeBrowser')
    sequenceBrowserNode.AddSynchronizedSequenceNode(sequenceNode)
    slicer.modules.sequences.logic().UpdateAllProxyNodes()  # ensure that proxy node is created
    # Reconstruct
    volumeReconstructionNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLVolumeReconstructionNode")
    volumeReconstructionNode.SetAndObserveInputSequenceBrowserNode(sequenceBrowserNode)
    proxyNode = sequenceBrowserNode.GetProxyNode(sequenceNode)
    volumeReconstructionNode.SetAndObserveInputVolumeNode(proxyNode)
    volumeReconstructionNode.SetAndObserveInputROINode(roiNode)
    volumeReconstructionNode.SetFillHoles(True)
    slicer.modules.volumereconstruction.logic().ReconstructVolumeFromSequence(volumeReconstructionNode)
    reconstructedVolume = volumeReconstructionNode.GetOutputVolumeNode()
    # Cleanup
    slicer.mrmlScene.RemoveNode(volumeReconstructionNode)
    slicer.mrmlScene.RemoveNode(sequenceBrowserNode)
    slicer.mrmlScene.RemoveNode(proxyNode)
    return reconstructedVolume

# This will store the reconstructed 4D volume
reconstructedVolumeSeqNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode', 'ReconstructedVolumeSeq')

for startInstanceNumber in startInstanceNumbers:
    print(f"Reconstructing start instance number {startInstanceNumber}")
    slicer.app.processEvents()
    # Create a temporary sequence that contains all instances belonging to the same time point
    singleReconstructedVolumeSeqNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode', 'TempReconstructedVolumeSeq')
    for instanceNumber in range(startInstanceNumber, numberOfInstancess, numberOfTimePoints):
        singleReconstructedVolumeSeqNode.SetDataNodeAtValue(
            inputVolumeSequenceNode.GetDataNodeAtValue(str(instanceNumber)), str(instanceNumber),)
    # Save reconstructed volume into a sequence
    reconstructedVolume = reconstructVolume(singleReconstructedVolumeSeqNode, roiNode)
    reconstructedVolumeSeqNode.SetDataNodeAtValue(reconstructedVolume, str(startInstanceNumber))
    slicer.mrmlScene.RemoveNode(reconstructedVolume)
    slicer.mrmlScene.RemoveNode(singleReconstructedVolumeSeqNode)

# Create a sequence browser node for the reconstructed volume sequence
reconstructedVolumeBrowserNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceBrowserNode', 'ReconstructedVolumeBrowser')
reconstructedVolumeBrowserNode.AddSynchronizedSequenceNode(reconstructedVolumeSeqNode)
slicer.modules.sequences.logic().UpdateAllProxyNodes()  # ensure that proxy node is created
reconstructedVolumeProxyNode = reconstructedVolumeBrowserNode.GetProxyNode(reconstructedVolumeSeqNode)
slicer.util.setSliceViewerLayers(background=reconstructedVolumeProxyNode)
slicer.modules.sequences.showSequenceBrowser(reconstructedVolumeBrowserNode)
</code></pre>

---

## Post #5 by @lorenzo_bennati (2020-11-17 10:52 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thanks a lot for the your help. In these days i will try to follow your instructions and i will let you know.</p>
<p>Thank you again</p>
<p>Lorenzo</p>

---

## Post #6 by @lorenzo_bennati (2020-11-22 19:57 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I tried Method A and by means of  your instructions i was able to  run the script you wrote.  However when Slicer stops to run the script, my output named ‘ReconstructedVolumeSeq’ represents only a 3D volume, fixed at a precise time instant.</p>
<p>My question is: how can i obtain the 4D volume similar to the one rapresented in the Youtube video you loaded in the last answer?</p>
<p>P.S. i want to specify that the version of Slicer i am using is the 4.13: The ‘unstable version’, downloanded yesterday.</p>
<p>I want to thank you very much for your help</p>
<p>Lorenzo</p>

---

## Post #7 by @lassoan (2020-11-22 20:01 UTC)

<p>You can play/pause/browse 4D volume sequences using Sequences module or using the Sequence browser toolbar (if this toolbar is not shown then click on “Sequence browser” in View / Toolbars menu).</p>

---

## Post #8 by @lorenzo_bennati (2020-11-22 20:06 UTC)

<p>Dear  <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you very much, it works</p>

---

## Post #9 by @Changing (2020-11-26 02:19 UTC)

<p>Hi,I have something problem like this.I have a series of images(png format) which were captured by rotating long-axis(one every 1°).And I want to recontruct the mitral valve volume by these images in the 3D slicer.But when I import these images and turn on the volume rendering ,I found something wrong like below.</p>
<p>My question is how can I recontruct the volume by these images like you do this.Can you give me some instruction.I have tried to use the script that you provide but I have something confused about it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0fe955e8403e9c967f382d74f58cfc779b7e787.png" data-download-href="/uploads/short-url/mYdPWGFMqAS8i7cs94MEVVDjGJ1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0fe955e8403e9c967f382d74f58cfc779b7e787_2_690x445.png" alt="image" data-base62-sha1="mYdPWGFMqAS8i7cs94MEVVDjGJ1" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0fe955e8403e9c967f382d74f58cfc779b7e787_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0fe955e8403e9c967f382d74f58cfc779b7e787_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0fe955e8403e9c967f382d74f58cfc779b7e787.png 2x" data-dominant-color="7E80AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1337×863 96.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have shared the images to the onedrive.<br>
link:<a href="https://1drv.ms/u/s!AifyPV6kzq9OgkNb0qnYN4cRwjCF?e=v8yCCL" class="inline-onebox" rel="noopener nofollow ugc">Microsoft OneDrive</a></p>
<p>Thanks.</p>

---

## Post #10 by @lassoan (2020-11-26 21:26 UTC)

<p>You can reconstruct volume from these 2D ultrasound rotational sweep very similarly to the cine MRI above.</p>
<p>Result:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="hIxr9OKBvQ8" data-video-title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=hIxr9OKBvQ8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/hIxr9OKBvQ8/maxresdefault.jpg" title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" width="" height="">
  </a>
</div>

<p>Script that reorganizes the volume into a sequence of frames, adds position&amp;orientation information to each frame, and reconstructs a volume:</p>
<pre><code class="lang-python"># Input 3D volume that contains each frame as a slice
inputFrameVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLVolumeNode')
imageSpacingMm = 0.2  # this needs to be replaced with the actual spacing
outputSpacingMm = imageSpacingMm * 1.0  # Make the reconstructed volume spacing larger to reduce memory usage and make computations faster

# Get volume size
inputFrameVolume = inputFrameVolumeNode.GetImageData()
extent = inputFrameVolume.GetExtent()
numberOfFrames = extent[5]-extent[4]+1

# Set up frame geometry and rotation
centerOfRotationIJK = [(extent[0]+extent[1])/2.0, extent[2], 0]
rotationAxis = [0, 1, 0]
rotationDegreesPerFrame = 180.0/numberOfFrames

# Convert RGB/RGBA volume to grayscale volume
if inputFrameVolume.GetNumberOfScalarComponents() &gt; 1:
    componentToExtract = 0
    print(f"Using scalar component {componentToExtract} of the image")
    extract = vtk.vtkImageExtractComponents()
    extract.SetInputData(inputFrameVolume)
    extract.SetComponents(componentToExtract)
    extract.Update()
    inputFrameVolume = extract.GetOutput()

# Create an image sequence that contains the frames as a time sequence
# and also contains position/orientation for each frame.
outputSequenceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", inputFrameVolumeNode.GetName()+"_frames")
outputSequenceNode.SetIndexName("frame")
outputSequenceNode.SetIndexUnit("")

# This temporary node will be used to add frames to the image sequence
tempFrameVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")

for frameIndex in range(numberOfFrames):
    # set current image from multiframe
    crop = vtk.vtkImageClip()
    crop.SetInputData(inputFrameVolume)
    crop.SetOutputWholeExtent(extent[0], extent[1], extent[2], extent[3], extent[4] + frameIndex, extent[4] + frameIndex)
    crop.ClipDataOn()
    crop.Update()
    croppedOutput = crop.GetOutput()
    croppedOutput.SetExtent(extent[0], extent[1], extent[2], extent[3], 0, 0)
    croppedOutput.SetOrigin(0.0, 0.0, 0.0)
    tempFrameVolumeNode.SetAndObserveImageData(croppedOutput)
    # set current transform
    ijkToRasTransform = vtk.vtkTransform()
    ijkToRasTransform.Scale(imageSpacingMm, imageSpacingMm, imageSpacingMm)
    ijkToRasTransform.RotateWXYZ(frameIndex * rotationDegreesPerFrame, *rotationAxis)
    ijkToRasTransform.Translate(-centerOfRotationIJK[0], -centerOfRotationIJK[1], -centerOfRotationIJK[2])
    tempFrameVolumeNode.SetIJKToRASMatrix(ijkToRasTransform.GetMatrix())
    # add to sequence
    added = outputSequenceNode.SetDataNodeAtValue(tempFrameVolumeNode, str(frameIndex))

slicer.mrmlScene.RemoveNode(tempFrameVolumeNode)

# Create a sequence browser node for the reconstructed volume sequence
outputSequenceBrowserNode = slicer.mrmlScene.AddNewNodeByClass(
    'vtkMRMLSequenceBrowserNode', outputSequenceNode.GetName() + '_browser')
outputSequenceBrowserNode.AddSynchronizedSequenceNode(outputSequenceNode)
slicer.modules.sequences.logic().UpdateAllProxyNodes()  # ensure that proxy node is created
outputSequenceProxyNode = outputSequenceBrowserNode.GetProxyNode(outputSequenceNode)
slicer.util.setSliceViewerLayers(background=outputSequenceProxyNode)
slicer.modules.sequences.showSequenceBrowser(outputSequenceBrowserNode)

# Make slice view move with the image (just for visualization)
driver = slicer.modules.volumereslicedriver.logic()
redSliceNode = slicer.util.getFirstNodeByClassByName("vtkMRMLSliceNode", "Red")
driver.SetModeForSlice(driver.MODE_TRANSVERSE, redSliceNode)
driver.SetDriverForSlice(outputSequenceProxyNode.GetID(), redSliceNode)


# Reconstruct
volumeReconstructionNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLVolumeReconstructionNode")
volumeReconstructionNode.SetAndObserveInputSequenceBrowserNode(outputSequenceBrowserNode)
volumeReconstructionNode.SetAndObserveInputVolumeNode(outputSequenceProxyNode)
volumeReconstructionNode.SetOutputSpacing(outputSpacingMm, outputSpacingMm, outputSpacingMm)
volumeReconstructionNode.SetFillHoles(True)
slicer.modules.volumereconstruction.logic().ReconstructVolumeFromSequence(volumeReconstructionNode)
reconstructedVolume = volumeReconstructionNode.GetOutputVolumeNode()
reconstructedVolume.SetName(outputSequenceProxyNode.GetName()+"_recon")
roiNode = volumeReconstructionNode.GetInputROINode()
# Cleanup
slicer.mrmlScene.RemoveNode(volumeReconstructionNode)
# Show reconstruction result
roiNode.SetDisplayVisibility(False)
slicer.util.setSliceViewerLayers(background=reconstructedVolume,fit=True)
</code></pre>

---

## Post #11 by @Changing (2020-11-27 01:54 UTC)

<p>Thank you so much ,it works well.</p>

---

## Post #12 by @rlorenzoni (2021-08-07 02:28 UTC)

<p>Hello,</p>
<p>This community is wonderful and the tutorials and feedback regarding questions have been great.  I have a similar question to others in the community working with Cine MRI imaging, but have not had success troubleshooting based on the community responses.  I would like to create a segmentation of a specific cardiac phase (time point in the cardiac beat) using cine MRI data.</p>
<p>When I load the cine sequence, it results in (what has been described by other Slicer responses) as the standard way cine MRI files are viewed in Slicer.  Is there a way in Slicer to have the program bring up three 2D images in the viewing window at a given time point as happens in a static (non 4D) cross sectional volume? …and then allow me to segment/seedgrow at one time point?</p>
<p>I attempted to follow the advice above including A, B, and C without much luck.  I was able to start to Paint after I changed the DICOM settings from Multivolume to Sequence, but I cannot Paint more than one slice at a time (see image below).  Some of the visualizations in that last video are impressive, but I cannot replicate them.  See the picture below for what I see and please let me know if the recent iterations of Slicer have the tools built in to perform segmentation on cine 4D images.</p>
<p>Appreciate it, -Ray</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f28a50ac398f10f1e675dc1c530b3a07d46a737.png" data-download-href="/uploads/short-url/2a6f3LuYjnCZpjVelOjF8ce8JN5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f28a50ac398f10f1e675dc1c530b3a07d46a737_2_639x500.png" alt="image" data-base62-sha1="2a6f3LuYjnCZpjVelOjF8ce8JN5" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f28a50ac398f10f1e675dc1c530b3a07d46a737_2_639x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f28a50ac398f10f1e675dc1c530b3a07d46a737_2_958x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f28a50ac398f10f1e675dc1c530b3a07d46a737.png 2x" data-dominant-color="32323E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1121×877 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2021-08-07 20:52 UTC)

<p>Have you acquired a time sequence of a 3D volume, or a time sequence of a 2D slice?</p>
<p>Have you managed to reconstruct a 3D volume?</p>

---

## Post #14 by @rlorenzoni (2021-08-08 05:41 UTC)

<p>It is a 3D cine MRI of the heart with 15 slices in this instance, each with 30 phases. Thank you for your help with this.</p>

---

## Post #15 by @lassoan (2021-08-08 12:24 UTC)

<p>Have you managed to reconstruct 3D volume for each phase? If not, how far did you get? What problems did you run into? Could you hate an anonymized data set?</p>

---

## Post #16 by @rlorenzoni (2021-08-08 17:40 UTC)

<p>Although segmenting all the phases (time points) within each slice would be useful for creating a moving 3D segmentation, I really only wish to segment the same phase (time point) within each slice to create a segmentated volume of (for example) cardiac diastole. My image above shows my attempt to do this… Slicer would not let me paint outside a single slice. I wish to do this with our cine MRI bc the contrast between the blood pool and tissue is excellent and it would allow segmentations of multiple cardiac cycles for comparison and other post processing.</p>
<p>I can try to send an anonymized data set, but would need to send it to a secure email address. Please DM me at <span class="mention">@DrBabyHearts</span> on Twitter. Thanks.</p>

---

## Post #17 by @lassoan (2021-08-08 21:35 UTC)

<p>You can send me a direct message here (click on my name and then the message icon).</p>

---

## Post #18 by @lassoan (2021-08-09 15:23 UTC)

<p>I’ve added a module to SlicerHeart extension: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/Reconstruct4DCineMRI.md#reconstruct-4d-cine-mri">Reconstruct 4D cine-MRI</a>. This module provides a convenient GUI for the 4D Cartesian volume reconstruction, so Python scripting is no longer needed. It’ll be available in the latest Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #19 by @rlorenzoni (2021-08-09 17:58 UTC)

<p>Thank you very much… above and beyond as usual.  I will let you know how it goes.</p>

---

## Post #20 by @rlorenzoni (2021-12-04 00:53 UTC)

<p>Hello again Slicer Community, I tried the Reconstruct 4D cine-MRI module shortly after the 4.13 build came out, but noted that I could not load the required extensions.  I just tried it again and am having the same issues.  Specifically, if I try to download SlicerHeart or IGSIO from the “Install Extensions” tab I get the error: “Failed downloading: <a href="https://slicer.packages.kitware" rel="noopener nofollow ugc">https://slicer.packages.kitware</a>…”.  Then, if I try to “Restore Extensions” (they are both in this list) and select one or both of these extensions, nothing seems to happen when I click “Install Selected” and if I try to exit, I get the message “Install/uninstall operations are still in progress…” even after I wait about two hours.  The “Reconstruct 4D cine-MRI” module is therefore not available for use in my install of 4.13.</p>
<p>Troubleshooting to-date: Uninstalling 4.11 and 4.13, restarting my computer, and re-installing 4.13 did not solve the problem.  Being on a different network did not solve it either.  When I reverted to 4.11, I can reinstall the extensions, but I obviously get an error message when I try to use the “Reconstruct 4D cine-MRI” module (Error: “This module requires Slicer core version Slicer-4.13…”).  I have tried installing 4.13 on three machines, one of which never had any version of 3D Slicer installed on it previously.</p>
<p>Have others had this issue?  Is there a fix?  Thanks for the help!  -Ray</p>

---

## Post #21 by @lassoan (2021-12-04 02:56 UTC)

<p>Everything should work well in the latest Slicer Preview Release. Please follow the suggestions <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions">here</a> and let us know if they helped.</p>

---

## Post #22 by @rlorenzoni (2021-12-04 03:09 UTC)

<p>Thank you. I will try the new build.</p>

---

## Post #23 by @Isabella_Romero (2022-10-05 10:16 UTC)

<p>Hi,<br>
I am trying to do a reconstruction. I have an ultrasound video (seq.mha file) and I have done a segmentation using the module Segmentation UNet. Now, I am trying to do the reconstruction of the segmentation using the module “IGT Volume Reconstruction”, as you did in this example.</p>
<p>My question is, can I use the same code you used for the mitral valve? Or do you know how can I approach it.</p>

---

## Post #24 by @lassoan (2023-03-21 02:18 UTC)



---
