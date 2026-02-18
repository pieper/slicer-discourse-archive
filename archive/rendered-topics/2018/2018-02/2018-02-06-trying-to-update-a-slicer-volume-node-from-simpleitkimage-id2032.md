# Trying to update a slicer volume node from SimpleITKImage

**Topic ID**: 2032
**Date**: 2018-02-06
**URL**: https://discourse.slicer.org/t/trying-to-update-a-slicer-volume-node-from-simpleitkimage/2032

---

## Post #1 by @drusmanbashir (2018-02-06 11:59 UTC)

<p>Operating system: Window 7<br>
Slicer version: 4.8.1</p>
<p>Hi All,</p>
<p>I am a newbie. I am trying to develop a segmentation module using python. The main function takes as input  a vtkMRMLLabelMapVolumeNode and a vtkMRMLScalarVolumeNode as well as an ‘outputVolumeNode’ which is a newly created (in slicer gui) vtkMRMLLabelMapVolumeNode. The algorithm produces a new label map volume (a numpy array) based on the input volume and labelmap and is trying to push the new label map volume into the output node as so:</p>
<p>sitkImageOutput = sitk.GetImageFromArray(numpyArray)<br>
sitkUtils.PushVolumeToSlicer(sitkImageOutput,outputVolumeNode)</p>
<p>But nothing happens - the outputVolumeNode inside slicer remains empty. Is there an update function or something i am missing?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2018-02-06 16:54 UTC)

<p>You could play with the SimpleFilters module and try using the same approach as is used there:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py#L476-L492" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py#L476-L492" target="_blank" rel="nofollow noopener">SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py#L476-L492</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="476" style="counter-reset: li-counter 475 ;">
<li>def updateOutput(self,img):</li>
<li>
</li>
<li>  nodeWriteAddress=sitkUtils.GetSlicerITKReadWriteAddress(self.outputNodeName)</li>
<li>  sitk.WriteImage(img,nodeWriteAddress)</li>
<li>
</li>
<li>  node = slicer.util.getNode(self.outputNodeName)</li>
<li>
</li>
<li>  applicationLogic = slicer.app.applicationLogic()</li>
<li>  selectionNode = applicationLogic.GetSelectionNode()</li>
<li>
</li>
<li>  if self.outputLabelMap:</li>
<li>    selectionNode.SetReferenceActiveLabelVolumeID(node.GetID())</li>
<li>  else:</li>
<li>    selectionNode.SetReferenceActiveVolumeID(node.GetID())</li>
<li>
</li>
<li>  applicationLogic.PropagateVolumeSelection(0)</li>
<li>  applicationLogic.FitSliceToAll()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2018-02-06 22:58 UTC)

<p><code>numpyArray</code> does not specify image geometry (origin, spacing, axis directions). You have to call <code>outim.CopyInformation(some_reference_image)</code> or set the image geometry some other way.</p>
<aside class="quote no-group" data-username="drusmanbashir" data-post="1" data-topic="2032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drusmanbashir/48/1282_2.png" class="avatar"> drusmanbashir:</div>
<blockquote>
<p>outputVolumeNode inside slicer remains empty</p>
</blockquote>
</aside>
<p>What is empty? Does not show up in slice viewer? If you go to Volumes module, what do you see in Volume Information section? If you open the Histogram at the bottom of the module GUI, do you see a histogram there?</p>

---

## Post #4 by @lassoan (2018-02-06 23:06 UTC)

<p>Maybe you have just forgot to show the created volume in the slice viewers. This code works for me:</p>
<pre><code>import numpy as np
import sitkUtils
numpyArray = np.random.randint(0,10,[30,40,50])

sitkImageOutput = sitk.GetImageFromArray(numpyArray)
volumeNode = sitkUtils.PushVolumeToSlicer(sitkImageOutput,None)
slicer.util.setSliceViewerLayers(background=volumeNode)</code></pre>

---

## Post #5 by @drusmanbashir (2018-03-04 15:48 UTC)

<p>Eventually setting origin and spacing got the code working like so:</p>
<pre><code>  sitkUtils.PushVolumeToSlicer(sitkImageOutput,outputVolumeNode)
  outputVolumeNode.SetOrigin(inputVolumeNode.GetOrigin())
  outputVolumeNode.SetSpacing(inputVolumeNode.GetSpacing())</code></pre>

---

## Post #6 by @lassoan (2018-03-04 21:29 UTC)

<p>Thanks for the update. Yes, numpy arrays cannot store image geometry, so you have to define the image geometry by setting origin, spacing, and axis directions in your SimpleITK image or Slicer volume node.</p>

---

## Post #7 by @Jan_Alexander (2021-03-01 11:07 UTC)

<p>Thank you, I was able to get it working eventually with</p>
<p><code>slicernb.MatplotlibDisplay(matplotlib.pyplot)</code></p>

---
