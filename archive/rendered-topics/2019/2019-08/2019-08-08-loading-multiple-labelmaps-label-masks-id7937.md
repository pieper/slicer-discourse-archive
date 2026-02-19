---
topic_id: 7937
title: "Loading Multiple Labelmaps Label Masks"
date: 2019-08-08
url: https://discourse.slicer.org/t/7937
---

# Loading multiple labelmaps (label masks)

**Topic ID**: 7937
**Date**: 2019-08-08
**URL**: https://discourse.slicer.org/t/loading-multiple-labelmaps-label-masks/7937

---

## Post #1 by @EricaMoreira (2019-08-08 10:04 UTC)

<p><strong>Operating system</strong>: macOS Mojave (version 10.14.6)<br>
<strong>Slicer version</strong>: 4.11.0-2019-07-29 r28413<br>
<strong>Expected behavior</strong>: Load the correct labelmap (label mask) for each original image<br>
<strong>Actual behavior</strong>: I can only figure out how to load <em>one</em> labelmap (label mask) at a time</p>
<p><strong>Details</strong>:</p>
<p>Our workflow is currently as follows:</p>
<p><strong>1.</strong> From the Slicer Python Interactor, run a Python script to load a few hundred 2D images. The images are related, but are not from the same 3D volume. The Python script also automatically opens the Segment Editor module, creates three segments with three different names and colors so that a user can paint on top of each of the images and create label masks.</p>
<p><strong>2.</strong> Then, from the Slicer Python Interactor, run a Python script to save each of the label masks as .tiff (as this is the input we need to a separate model we are running outside of Slicer to help complete the segmentation of the image). Here is the code from that script to save the label masks:</p>
<pre><code>###################
# Saving the labels
###################

# Solution from : https://discourse.slicer.org/t/segment-binarylabelmap-to-numpy-array/778

# Create a binary label volume from segmentation
labelmapVolumeNode =     slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')

# To export specific segments instead, edit the following line with another one listed in above solution link
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)

referenceVolumeNode=slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

# Export data as numpy arrays
referenceImg = arrayFromVolume(referenceVolumeNode)
label = arrayFromVolume(labelmapVolumeNode)

# Checking what the label mask looks like
print('Unique values in the label: {0}'.format(np.unique(label)))
print('\nLabel mask shape: {0}'.format(np.shape(label)))
print('\nOriginal image shape: {0}'.format(np.shape(referenceImg)))

# save labels as numpy array
# this will be the output of the initial annotation, and the input to the model
np.save(labels_path_save, label)

# save as tiff 
number_files=np.shape(label)[0]

for i in range(0, number_files):
    string="label"+str(i+1)+".tiff"
    labelpathtiff=os.path.join(labels_path_save, string)
    currentlabel=label[i]
    imsave(labelpathtiff, currentlabel.astype(np.uint8))  ## has to specify type so that data is not scaled 
</code></pre>
<p><strong>3.</strong> Then, we use our external model to basically add to/improve on the label masks in an automated way, and then we save the new and improved label masks as .nrrd files (so that we can load them back into Slicer).</p>
<p><strong>4.</strong> Then, from the Slicer Python Interactor, run a Python script to reload the images and the corresponding label masks so that we can continue to improve on the label masks by erasing/painting. Here is the code from that script to reload the images:</p>
<pre><code>##########################
# Reload images and labels
##########################

# clear the scene
slicer.mrmlScene.Clear(False)

# load the original images
[success, volume] = slicer.util.loadVolume(filename = image_path_slicer, returnNode=True)

# set the layout view in the slicer GUI (in this case to the red/one image only view)
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)

# set the initial module to Segment Editor (allowing us to paint and annotate the image)
slicer.util.mainWindow().moduleSelector().selectModule('SegmentEditor')

# load the labels (as an nrrd file)
# this will be the labels that have been updated by the predictions of the model
# and converted from numpy array back to nrrd
files=os.path.join(labels_path_save, "label1.nrrd")
# we are only able to load one label successfully (in the above line)
# we would like to load all of the labels, but the below line gives errors
# files=os.path.join(labels_path_save, "*.nrrd")

# Load that file as a labelmap volume and import it into segmentation
segmentationNode =     slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
[success, labelmapVolumeNode] = slicer.util.loadLabelVolume(filename = files, returnNode=True)
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segmentationNode)
slicer.mrmlScene.RemoveNode(labelmapVolumeNode)
</code></pre>
<p>I am very new to Slicer, and I have a feeling that perhaps we should be saving and reloading everything as part of a “scene”, even though the images are not part of a 3D volume. Can anyone help me determine if we should be using a scene or if there is another solution to load the correct labelmaps (label masks) associated with each original image?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2019-08-08 12:59 UTC)

<p>Hi -</p>
<p>Did you try looping over the nrrd files in <code>labels_path_save</code>? (You can use <a href="https://docs.python.org/3/library/glob.html" rel="nofollow noopener">glob</a> to get a list of files matching the wildcard).</p>

---

## Post #3 by @EricaMoreira (2019-08-16 08:56 UTC)

<p>Hi Steve,</p>
<p>Thanks so much for your response! I did try looping over the nrrd files, and it worked, but it made loading the labelmaps a very slow process.</p>
<p>I actually figured out how to make it work, though, so I thought I’d share what I did here in case that helps anyone else. Essentially, as long as I point to one of the labelmap files in a folder with all of the labelmap files in it, it will load the rest of them correctly.</p>
<p>This is the same way that loading in the volume works in that it automatically searches for and loads in other similar images files in the folder to make up the volume (unless you use <code>singleFile=True</code> when loading the volume, which will force it not to search for other similar images). I know you already know all of this, of course, I’m just explaining in case someone else is searching for this answer as well.</p>
<p>I also was having some issues essentially recreating segments out of the labelmaps so that I could continue to edit the segments manually in Slicer, so here is how I fixed that as well:</p>
<pre><code class="lang-python"># clear the scene
slicer.mrmlScene.Clear(False)  

# load the original images
[success, volume] = slicer.util.loadVolume(filename = image_path_slicer, returnNode=True) 

# set the layout view in the slicer GUI (in this case to the red/one image only view)
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)

# set the initial module to Segment Editor (allowing us to paint and annotate the image)
slicer.util.mainWindow().moduleSelector().selectModule('SegmentEditor')

# load the labels (as an nrrd files)
# this will be the labels that have been updated by the predictions of the model
# and converted from numpy array back to nrrd
# here I am just pointing to the first labelmap, but it actually loads all 400 of the labelmaps in the folder!
labels=os.path.join(labels_path_save, "label_0001.nrrd")    
[success, labelmapVolumeNode] = slicer.util.loadLabelVolume(filename = labels, returnNode=True)
print(success)

# Import labelmap to segmentation:
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segmentationNode)

# Create segment editor to get access to effects
#segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()  # This creates a separate window, so instead use the following
segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volume)

segmentEditorWidget.setActiveEffectByName("Paint")
# This is how you would automatically set the brush size, but documentation is limited
# see source code here: https://github.com/Slicer/Slicer/blob/7cf1daed5654dd57dccae3f8b0c7f6f758aeb000/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.cxx
#paintEffect = segmentEditorWidget.activeEffect()
#paintEffect.setParameter("BrushAbsoluteDiameter", 1)

# Change the names of the segmentations
segmentation = segmentationNode.GetSegmentation()
segment0 = segmentation.GetSegment(segmentation.GetNthSegmentID(0))
#segment0.SetColor(1,0,0)
segment0.SetName('Collagen')

segment1 = segmentation.GetSegment(segmentation.GetNthSegmentID(1))
#segment0.SetColor(0,1,0)
segment1.SetName('Background')

segment2 = segmentation.GetSegment(segmentation.GetNthSegmentID(2))
#segment0.SetColor(0,1,0)
segment2.SetName('Cells')

</code></pre>
<p>Thanks again for your help!</p>

---
