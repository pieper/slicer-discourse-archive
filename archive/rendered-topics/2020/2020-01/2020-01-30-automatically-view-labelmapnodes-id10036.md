# Automatically view LabelMapNodes

**Topic ID**: 10036
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/automatically-view-labelmapnodes/10036

---

## Post #1 by @kleingeo (2020-01-30 19:27 UTC)

<p>I developed a segmentation module and want to be able to display the segmentation after it is generated, but I am unsure how to do it. This is what I have so far (for the relevant parts). Any help would be much appreciated.</p>
<pre><code class="lang-python">segVolumeNode = sitkUtils.PushVolumeToSlicer(seg,
                                             name='segPrediction',
                                             className='vtkMRMLLabelMapVolumeNode')
slicer.mrmlScene.AddNode(segVolumeNode)
segVolumeNode.CreateDefaultDisplayNodes()
segVolumeNode.GetModelDisplayNode().SetVisibility(1)

</code></pre>

---

## Post #2 by @lassoan (2020-01-30 19:29 UTC)

<p>This example in the script repository probably does what you need: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a></p>

---

## Post #4 by @kleingeo (2020-01-30 20:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10036">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This example in the script repositor</p>
</blockquote>
</aside>
<p>I do not want to create a segmentation class. I simply want to have the label map display after it is created.</p>

---

## Post #5 by @lassoan (2020-01-30 20:45 UTC)

<p>Labelmap volume nodes have several important limitations - you cannot show them in 3D, you can only show one at a time in a slice view, you cannot edit them using Segment Editor. Do you store segmentation information in the labeImap volume node? Is there a specific reason you do not want to store it in a segmentation node?</p>

---

## Post #7 by @kleingeo (2020-01-30 21:49 UTC)

<p>It is simply easier for me to have them as a label map as I only need them to overlay on the 2D orthogonal slices, and I only need the binary pixel information.</p>

---

## Post #8 by @lassoan (2020-01-30 21:56 UTC)

<p>Segmentation nodes are saved as labelmaps (nrrd format, in recent Slicer preview versions, it is saved as a simple 3D volume if segments don’t overlay) and you can load a labelmap from file directly as segmentation (use the .seg.nrrd file extension or choose “Segmentation” in Add data dialog). If you want to process the segmentation you can access the internal binary labelmap representation as a single vtkImageData object. If you experience any specific complications when you try to use segmentations instead of labelmaps then let us know. If labelmaps fulfill all your needs then you can of course keep using them for now and switch later, when needed (to display in 3D, edit them, compute advanced statistics, etc.).</p>

---

## Post #9 by @kleingeo (2020-01-31 16:58 UTC)

<p>Again, I would prefer to use the label maps. I am only using Slicer to select parts of the image I want to segment and using the segmentation I built in the backend module.</p>
<p>However, this does not still answer how to have the label map display automatically.</p>

---

## Post #10 by @lassoan (2020-01-31 17:51 UTC)

<p>You can import a labelmap volume from SimpleITK and display it as labelmap like this:</p>
<pre><code class="lang-python">segVolumeNode = sitkUtils.PushVolumeToSlicer(seg, name='segPrediction', className='vtkMRMLLabelMapVolumeNode') 
slicer.util.setSliceViewerLayers(label=segVolumeNode, labelOpacity=0.5)
</code></pre>
<p>You can import a labelmap volume from SimpleITK and display it as segmentation like this:</p>
<pre><code class="lang-python">segVolumeNode = sitkUtils.PushVolumeToSlicer(seg, name='segPrediction', className='vtkMRMLLabelMapVolumeNode') 
segNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(segVolumeNode, segNode)
slicer.mrmlScene.RemoveNode(segVolumeNode)
segNode.CreateClosedSurfaceRepresentation() # show in 3D - optional
</code></pre>

---
