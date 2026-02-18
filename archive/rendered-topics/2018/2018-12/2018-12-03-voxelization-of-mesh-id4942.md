# Voxelization of mesh

**Topic ID**: 4942
**Date**: 2018-12-03
**URL**: https://discourse.slicer.org/t/voxelization-of-mesh/4942

---

## Post #1 by @zjx1805 (2018-12-03 20:56 UTC)

<p>Is there a way in 3D Slicer to voxelize a 3D mesh (preferably through python interpreter)? I would also like to be able to specify the voxel size and shape, if possible. BTW, my complete mesh consists of 100+ separate .vtk mesh files, so is there a way to merge all these separate meshes into one single mesh (preferably through python interpreter) in order to do the voxelization? Thank you for your time!</p>

---

## Post #2 by @cpinter (2018-12-03 22:02 UTC)

<p>Yes you can do this through the Segmentations infrastructure. What you need to do is similar to this<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a><br>
but the opposite way: going from closed surface to labelmap. So instead of ImportLabelmapToSegmentationNode you need to use ImportModelToSegmentationNode, and instead of CreateClosedSurfaceRepresentation you need to call CreateBinaryLabelmapRepresentation. You can load the 100+ vtk files as 100+ models in Slicer, call the ImportModelToSegmentationNode 100+ times on the same segmentation. Then you can convert them together with the CreateBinaryLabelmapRepresentation function. Finally, you can merge them together using a Segment Editor effect called Logical operators (refer to this one for help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a>).</p>
<p>To specify the voxel size, you can set the conversion parameter before doing the conversion (the CreateBinary…call). You can do it like this: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationGeometryWidget.cxx#L445-L448" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationGeometryWidget.cxx#L445-L448</a> . However, for this you’ll need to know the geometry exactly. I suggest you try using the segmentation geometry widget and see how it works (Segment Editor box icon in the row of the Master volume).</p>

---

## Post #3 by @zjx1805 (2018-12-03 23:08 UTC)

<p>Hi Csaba,</p>
<p>Thank you for the quick response. I still have a few questions:</p>
<ol>
<li>Could you please tell me where ImportModelToSegmentationNode is? I could not seem to find it under slicer.logic(). And how do I check what are the conversion parameters (names and their default value) in python?</li>
<li>Do I need to create an empty volume and set it as the master volume in segmentation node before calling CreateBinaryLabelmapRepresentation function or using the editor effect? If so, how should I do it in python?</li>
<li>How do I extract the numpy array from the resulting labelmap/voxel representation?</li>
</ol>
<p>Thank you for your time!</p>

---

## Post #4 by @cpinter (2018-12-04 00:18 UTC)

<ol>
<li>In slicer.modules.segmentations.logic() (as I said it’s to replace the ImportLabelmapToSegmentationNode call in the snippet I linked to). It’s important to set the master representation to closed surface before you do the import so that you can do the conversion yourself (vtkMRMLSegmentationNode::SetMasterRepresentationToClosedSurface)</li>
<li>Not necessarily. All you need is the conversion parameter which is a string. It is easier to set it if you have an actual volume, but not necessary. The conversion parameter describes volume geometry, from which the position and dimensions components are not necessary (as it will be calculated for each segment), only the spacing and directions. So for example if you want a labelmap which is aligned to the RAS directions and has 1x1x1.3mm spacing, then this will be your conversion parameter: ‘1;0;0;0;0;1;0;0;0;0;1.3;0;0;0;0;1;0;0;0;0;0;0;’ (direction matrix first row then second, third, fourth, then extent xMin, xMax etc - but you only need the spacing information, that’s why everything else is 0)</li>
<li>Why do you need it? There are probably already modules in Slicer that can calculate what you want.</li>
</ol>

---

## Post #5 by @zjx1805 (2018-12-04 05:23 UTC)

<p>Thank you for the reply. For the third point, I would like to save the resulting labelmap (i.e., the voxelized result) into a numpy array so that I could perform other operations in python (not necessarily in slicer). Am I going to get a labelmapNode after doing the logical union operation (to put together all the separate meshes)?</p>

---

## Post #6 by @lassoan (2018-12-04 06:14 UTC)

<p>In Slicer you have access to numpy, SimpleITK, VTK, etc. and can <a href="https://github.com/Slicer/SlicerJupyter" rel="nofollow noopener">use Slicer directly from a Jupyter notebook</a> kernel, etc. so you should be able to do all processing there (let us know if there are any processing operations that you don’t find).</p>
<p>Anyway, if you must process the data outside of Slicer then you can save the labelmap it in a standard medical image volume file format, which stores all essential metadata (image origin, spacing, axis directions). We most commonly use nrrd for simple images but mha (metaimage) or nii (nifti) work, too. All these file formats have several file reader/writer implementations in Python.</p>

---

## Post #7 by @zjx1805 (2018-12-04 06:50 UTC)

<p>Thank you Andras for your reply!</p>

---

## Post #8 by @zjx1805 (2018-12-05 17:44 UTC)

<p>Hi Csaba,</p>
<p>I am having some problems with applying the editor effects. Below is my current code:</p>
<pre><code>def voxelizeMeshes():
    # Close current scene
    slicer.mrmlScene.Clear(0)
    
    # Load files
    dataDirectory = dirname + 'brainVesselMeshes/'
    filenameList = glob.glob(dataDirectory + '*.vtk')
    nodeNameList = loadFiles(filenameList)

    nodeCollection = slicer.mrmlScene.GetNodesByClass('vtkMRMLModelNode')
    nodeNameList = [node.GetName() for node in list(nodeCollection) if 'SW' in node.GetName()]
    
    # Create empy volume
    masterVolumeNode = mt.createEmptyVolume([500, 500, 500], [0.1, 0.1, 0.1], 'volume')

    segmentationNodeName = 'seg'
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", segmentationNodeName)
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
   
    
    # Import model to segmentation
    for nodeName in nodeNameList:
        modelNode = slicer.util.getNode(nodeName)
        slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode, segmentationNode)
    
    segmentationNode.CreateBinaryLabelmapRepresentation()
    
    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

    # Logical operators
    segmentEditorWidget.setActiveEffectByName("Logical operators")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter(......)
    effect.self().onApply()
</code></pre>
<p>Then I am not sure how should I programmatically add all the meshes together. I tried to add two segments together in the GUI, but nothing seems to happen after I clicked the ‘Apply’ button (i.e., I don’t see any new nodes containing the results). Could you help me with that? Thank you for your time!</p>

---

## Post #9 by @cpinter (2018-12-05 18:57 UTC)

<p>Look at this function <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py#L105" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py#L105</a></p>
<p>What you’ll need to do is set the parameters as they are used here. For example</p>
<pre><code>effect.setParameter('Operation', 'UNION')
</code></pre>
<p>By the way in your code you use the variable segmentEditorNode without defining it so that will be an error.</p>

---

## Post #10 by @zjx1805 (2018-12-05 22:51 UTC)

<p>Hi Csaba,</p>
<p>I took a look at the file you referred to and I see that I can specify the modifier segment by</p>
<pre><code>effect.setParameter("ModifierSegmentID", modifierSegmentIDs)
</code></pre>
<p>From the comment on Line 154, <code>modifierSegmentIDs</code> is a semicolon-separated list. However, I could not choose more than one modifier segment within the GUI. Does that mean I have to add segment2 to segment1, segment3 to segment1… and keep repeating this process until all the segments are merged together?</p>
<p>I am also wondering how to specify the <code>selectedSegmentID</code>. In the file that you referred to, it is set by <code>self.scriptedEffect.parameterSetNode().GetSelectedSegmentID()</code>. But I would like to know how I can set it in my code.</p>
<p>And how do I get the merged result, i.e., the labelmap, out of the segmentation node?</p>
<p>Thank you for your time!</p>

---

## Post #11 by @zjx1805 (2018-12-06 21:31 UTC)

<p>Hi Andras,</p>
<p>I took a look at the file Csaba referred to and I see that I can specify the modifier segment by</p>
<pre><code>effect.setParameter("ModifierSegmentID", modifierSegmentIDs)
</code></pre>
<p>From the comment on Line 154, <code>modifierSegmentIDs</code> is a semicolon-separated list. However, I could not choose more than one modifier segment within the GUI. Does that mean I have to add segment2 to segment1, segment3 to segment1… and keep repeating this process until all the segments are merged together?</p>
<p>I am also wondering how to specify the <code>selectedSegmentID</code>. In the file that you referred to, it is set by <code>self.scriptedEffect.parameterSetNode().GetSelectedSegmentID()</code>. But I would like to know how I can set it in my code.</p>
<p>And how do I get the merged result, i.e., the labelmap, out of the segmentation node?</p>
<p>Since Csaba did not reply to my post, I am wondering if you could help me with this. Thank you for your time!</p>

---

## Post #12 by @lassoan (2019-01-11 04:48 UTC)

<p>Currently, only a single modifier is supported. It would be great if you could edit the file to allow multiple selections.</p>
<p>To add all meshes into one mesh, you can select them one by one and click Apply each time. However, it is typically faster to use masking for this:</p>
<ul>
<li>select Logical operators effect</li>
<li>set “Operation” to “Fill”</li>
<li>uncheck “Bypass masking”</li>
<li>in Masking section, set “Editable area” to “Inside all segments”</li>
<li>click Apply</li>
</ul>

---

## Post #13 by @Saima (2021-02-09 05:01 UTC)

<p>Hi Andras,<br>
How can I get voxelized mesh of a labelmap/segment in slicer?</p>
<p>Thanks</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #14 by @Andinet_Enquobahrie (2021-02-09 11:40 UTC)

<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="15" height="15">
      <a href="https://github.com/lassoan/SlicerSegmentMesher" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/307929?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/lassoan/SlicerSegmentMesher" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSegmentMesher</a></h3>


  <p><span class="label1">Create volumetric mesh from segmentation using Cleaver2 or TetGen</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
