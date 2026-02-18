# Import labelmap to segmentation node - in batch processing

**Topic ID**: 2360
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/import-labelmap-to-segmentation-node-in-batch-processing/2360

---

## Post #1 by @anandmulay3 (2018-03-19 14:10 UTC)

<p>slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, seg)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: arguments do not match any overloaded methods</p>
<p>i’m trying to make segmentation please help…</p>

---

## Post #2 by @cpinter (2018-03-19 14:43 UTC)

<p>There are four signatures for that function:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L221" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L221" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L221</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="197" style="counter-reset: li-counter 196 ;">
<li>/// Import all labels from a labelmap node to a segmentation node, each label to a separate segment.</li>
<li>/// The colors of the new segments are set from the color table corresponding to the labelmap volume.</li>
<li>/// \param insertBeforeSegmentId New segments will be inserted before this segment.</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkMRMLLabelMapVolumeNode* labelmapNode,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, std::string insertBeforeSegmentId="");</li>
<li>
</li>
<li>/// Import all labels from a labelmap image to a segmentation node, each label to a separate segment</li>
<li>/// The colors of the new segments are randomly generated, unless terminology context is specified, in which case the terminology</li>
<li>///   entries are attempted to be mapped to the imported labels</li>
<li>/// LabelmapImage is defined in the segmentation node's coordinate system</li>
<li>/// (parent transform of the segmentation node is not used during import).</li>
<li>/// \param baseSegmentName Prefix for the names of the new segments. Empty by default, in which case the prefix will be "Label"</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkOrientedImageData* labelmapImage,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, std::string baseSegmentName="", std::string insertBeforeSegmentId="") ;</li>
<li>
</li>
<li>/// Update segmentation from segments in a labelmap node.</li>
<li>/// \param updatedSegmentIDs Defines how label values 1..N are mapped to segment IDs (0..N-1).</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkMRMLLabelMapVolumeNode* labelmapNode,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, vtkStringArray* updatedSegmentIDs);</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L221" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>You need to make sure the arguments match one of these.</p>
<p>Also the functions are static, so it’s possible that the error you get is because in python when you call a member function the first argument that is passed is <code>self</code>. Try to call the function as static, like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py#L122" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py#L122" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py#L122</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="112" style="counter-reset: li-counter 111 ;">
<li>del featureImage</li>
<li># Pixel type of watershed output is the same as the input. Convert it to int16 now.</li>
<li>if labelImage.GetPixelID() != sitk.sitkInt16:</li>
<li>  labelImage = sitk.Cast(labelImage, sitk.sitkInt16)</li>
<li># Write result from SimpleITK to Slicer. This currently performs a deep copy of the bulk data.</li>
<li>sitk.WriteImage(labelImage, sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))</li>
<li>mergedLabelmapNode.GetImageData().Modified()</li>
<li>mergedLabelmapNode.Modified()</li>
<li>
</li>
<li># Update segmentation from labelmap node and remove temporary nodes</li>
<li class="selected">slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(mergedLabelmapNode, segmentationNode, visibleSegmentIds)</li>
<li>slicer.mrmlScene.RemoveNode(masterVolumeNode)</li>
<li>slicer.mrmlScene.RemoveNode(mergedLabelmapNode)</li>
<li>
</li>
<li>qt.QApplication.restoreOverrideCursor()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @anandmulay3 (2018-03-20 06:46 UTC)

<p>sorry but i need more help in this, actually im trying this simple code from the nightly documentation.</p>
<p><strong>Create a segmentation from a labelmap volume and display in 3D</strong><br>
labelmapVolumeNode = getNode(‘label’)<br>
seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
<em>slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, seg)</em><br>
seg.CreateClosedSurfaceRepresentation()<br>
slicer.mrmlScene.RemoveNode(labelmapVolumeNode)</p>

---

## Post #4 by @lassoan (2018-03-20 18:08 UTC)

<p>Do you have a labelmap node with the name ‘label’ in your scene?<br>
Is labelmapVolumeNode a valid labelmap volume node?<br>
What do you see on the console if you type <code>labelmapVolumeNode</code> and press enter?</p>

---

## Post #5 by @brhoom (2018-04-10 20:26 UTC)

<p>I have a problem related to this. The import works in Slicer Python Interactor but not in the terminal i.e.</p>
<pre><code>    `Slicer --no-main-window --python-script  myScript.py`
</code></pre>
<p>I get an error</p>
<pre><code>arguments do not match any overloaded methods
</code></pre>
<p>Here is the part from the script, I also tried the commented line as well:</p>
<p>[success, labelmapVolumeNode] = slicer.util.loadVolume(labelmapPath, returnNode=True)<br>
segVolumeNode = slicer.vtkMRMLSegmentationNode()</p>
<pre><code>#slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segVolumeNode)
slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(labelmapVolumeNode, segVolumeNode)</code></pre>

---

## Post #6 by @Nicole_Aucoin (2018-04-10 20:46 UTC)

<p>When I pass None as the first argument to the ImportLabelmapToSegmentationNode call I get the error you’re seeing, but if I pass a valid volume node, it returns True.<br>
Did the label map volume load? What’s the value of “success”?</p>

---

## Post #7 by @brhoom (2018-04-10 21:04 UTC)

<p>The label map volume is loaded successfully, I get “True” when I print “success” .</p>
<p>I needed the import to use the segmentation later for getting the statistics. I did a workaround and computed it manually and it works .</p>
<pre><code>    tmpSegArray = slicer.util.array(labelmapVolumeNode.GetID())
    tmpSegArraySpacing = labelmapVolumeNode.GetSpacing()

    vxSize = reduce(lambda x,y: x*y, tmpSegArraySpacing)
    
    S1Count= len(tmpSegArray[tmpSegArray==7])
    S2Count= len(tmpSegArray[tmpSegArray==300])
    
    S1Size= S1Count * vxSize
    S2Size= S2Count * vxSize</code></pre>

---

## Post #8 by @lassoan (2018-04-10 21:16 UTC)

<p>We can investigate if you post a complete example script that reproduces the error.</p>

---

## Post #9 by @brhoom (2018-04-10 21:40 UTC)

<p>Here is a complete script:</p>
<pre><code># myScript  
# to run: ~/sw/Slicer-4.8.1/Slicer --no-main-window --python-script myScript.py "

from __main__ import vtk, qt, ctk, slicer
from copy import deepcopy
import Tkinter, tkFileDialog, sys ,math 
import os, re , time , datetime
import sitkUtils,   numpy as np, SimpleITK as sitk
from shutil import copyfile
print("                   myScript ")        
[success, labelmapVolumeNode] = slicer.util.loadVolume("./myImg-label.nrrd", returnNode=True)    
print ("labelmapVolumeNoderesult : "  + str(success))
segVolumeNode = slicer.vtkMRMLSegmentationNode()   slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode,segVolumeNode)
 #slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(labelmapVolumeNode, segVolumeNode)
print(" All tasks are done!  ") 
exit() 
</code></pre>
<p>And here is the output:</p>
<pre><code>  Slicer --no-main-window --python-script ./myScript.py
  Number of registered modules: 150 
  Number of instantiated modules: 150 
  Number of loaded modules: 150 
               myScript 
  Loaded volume from file: ~/myImg-label.nrrd. 
  Dimensions: 80x80x20. Number of components: 1. Pixel type: short.
 "Volume" Reader has successfully read the file "./myImg-label.nrrd" "[0.02s]" 
 labelmapVolumeNoderesult : True
 Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
  File "./myScript.py", line 20, in &lt;module&gt;    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode,segVolumeNode)
  TypeError: arguments do not match any overloaded methods</code></pre>

---

## Post #10 by @lassoan (2018-04-11 02:20 UTC)

<p>There were a couple of problems:</p>
<ul>
<li>It is not enough to create the segmentation node but you need to also add to the scene. You can use <code>slicer.mrmlScene.AddNewNodeByClass</code> to create a node and add it to the scene in one step.</li>
<li>
<code>slicer.util.loadVolume</code> loads file as scalar volume, while <code>ImportLabelmapToSegmentationNode</code> expects a labelmap volume; you need to use <code>slicer.util.loadLabelVolume</code> instead</li>
<li>Relative path was used for the input image. I’m not sure what is the working directory of Slicer. It is safer to use absolute path.</li>
</ul>
<p>After fixing these issues, a full working example:</p>
<pre><code>[success, labelmapVolumeNode] = slicer.util.loadLabelVolume(r"c:\Users\msliv\OneDrive\Projects\SlicerTesting3\20180410-StartupSegmentation\Segmentation-label.nrrd", returnNode=True)
segNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segNode)</code></pre>

---

## Post #11 by @brhoom (2018-04-11 08:39 UTC)

<blockquote>
<p>It is not enough to create the segmentation node but you need to also add to the scene. You can use slicer.mrmlScene.AddNewNodeByClass to create a node and add it to the scene in one step.</p>
</blockquote>
<p>I thought we don’t need a scene when we run from a script, I was wrong.</p>
<blockquote>
<p>slicer.util.loadVolume loads file as scalar volume, while ImportLabelmapToSegmentationNode expects a labelmap volume; you need to use slicer.util.loadLabelVolume instead</p>
</blockquote>
<p>I guess this is the main cause of the error.</p>
<p>It works now thanks for investigating the error.</p>

---

## Post #12 by @lassoan (2018-04-11 13:26 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="11" data-topic="2360">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>I thought we don’t need a scene when we run from a script</p>
</blockquote>
</aside>
<p>Modules usually require all input and output nodes to be in the same scene. Without a scene, you cannot specify parent transforms or any other relationship between nodes.</p>

---
