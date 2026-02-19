---
topic_id: 5248
title: "Assigning Thresholded Regions To Different Segments"
date: 2019-01-02
url: https://discourse.slicer.org/t/5248
---

# Assigning thresholded regions to different segments

**Topic ID**: 5248
**Date**: 2019-01-02
**URL**: https://discourse.slicer.org/t/assigning-thresholded-regions-to-different-segments/5248

---

## Post #1 by @ishan_45 (2019-01-02 18:58 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.10<br>
Expected behavior: Different thresholded regions get assigned to respective segments<br>
Actual behavior: Both regions getting assigned to the first threshold segment</p>
<p>Hi everyone,<br>
I am working on an extension to 3D Slicer. The final aim of the extension is to segment the CT scan images to 2 base segments based on the thresholding values. For doing this, I am applying the Thresholding operation on 2 cloned segmentation and volume nodes. After this, I can’t determine how to assign the thresholded regions to a specific segment?</p>
<pre><code class="lang-auto"># Add segments

segmentName = "Threshold-A-B"
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
segment = segmentationNode.GetSegmentation().GetSegment(addedSegmentID)
segment.SetColor(216./256,101./256,79./256)

segmentName = "Threshold-B-MAX"
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
segment = segmentationNode.GetSegmentation().GetSegment(addedSegmentID)
segment.SetColor(200./256,200./256,235./256)	

#Cloning segmentationNode and masterVolumeNode
#Copied from Slicer website, get clonedNode and clonedVolumeNode from here

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Thresholding (From A to B)
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","A")
effect.setParameter("MaximumThreshold","B") 
effect.self().onApply()

displayNode = segmentationNode.GetDisplayNode()
displayNode.SetSliceIntersectionThickness(2)
#Missing: Assign this to segment 'Threshold-A-B'	

#Creating a  second segment editor to apply second thresholding to cloned volume
segmentEditorWidget2 = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget2.setMRMLScene(slicer.mrmlScene)
segmentEditorNode2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget2.setMRMLSegmentEditorNode(segmentEditorNode2)
segmentEditorWidget2.setSegmentationNode(clonedNode)
segmentEditorWidget2.setMasterVolumeNode(clonedVolumeNode)	

# Thresholding 2 (From B to MAX)
segmentEditorWidget2.setActiveEffectByName("Threshold")
effect2 = segmentEditorWidget2.activeEffect()
effect2.setParameter("MinimumThreshold","B")
effect2.self().onApply()

displayNode2 = clonedNode.GetDisplayNode()
displayNode2.SetSliceIntersectionThickness(2)
#Missing: Assign this to the segment 'Threshold-B-MAX' 
</code></pre>

---

## Post #2 by @lassoan (2019-01-02 19:18 UTC)

<p>There is no need to create a second segment editor widget. You can combine segments using Logical operators effect.</p>

---

## Post #3 by @ishan_45 (2019-02-06 09:53 UTC)

<p>Thanks for the help. I found this great example for using the Logical Operators effect, which could be useful for others too: <a href="https://gist.github.com/hherhold/ec3f74d20ca63866555f3e66d1f3621c" class="inline-onebox" rel="noopener nofollow ugc">Find islands in a certain voxel size range. · GitHub</a></p>
<p>I just had a basic question regarding the above file, Is there a way to clear the scene, once the script has run for one image. I have like 50 images that need I want to segment but every time I run this code in Slicer, the segmentation for each next image just appears on top of each other in the scene views.</p>
<p>I tried using the below code at the end</p>
<pre><code>    segmentEditorWidget = None
    slicer.mrmlScene.RemoveNode(segmentationNode)
    slicer.mrmlScene.RemoveNode(masterVolumeNode)
</code></pre>
<p>But this just throws an error</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File "D:/Users/ishan.saxena/TokExData/SlicerScripts/Segmentation_postop.py", line 72, in onSegmentationButtonClicked<br>
self.addSegmentation(dir_path, filename)<br>
File "D:/Users/ishan.saxena/TokExData/SlicerScripts/Segmentation_postop.py", line 172, in addSegmentation<br>
effect.setParameter("Operation", "COPY")<br>
AttributeError: ‘NoneType’ object has no attribute ‘setParameter’</p>
</blockquote>
<p>If I comment these removeNode commands, the code starts working perfectly only the scenes don’t get cleared. Any tips?</p>

---

## Post #4 by @pieper (2019-02-06 13:06 UTC)

<p>This should work:</p>
<pre><code>slicer.mrmlScene.Clear(0)</code></pre>

---

## Post #5 by @lassoan (2019-02-06 13:41 UTC)

<p>Also, it should be enough to clear the scene and no need to delete <code>segmentEditorWidget</code> when you switch between data sets.</p>

---

## Post #6 by @ishan_45 (2019-02-07 08:55 UTC)

<p>Thanks for the responses, however the error remains the same even after adding slicer.mrmlScene.Clear(0) at the end of the script and deleting segmentEditorWidget=None and the other RemoveNode commands.</p>
<p>I am guessing there is something wrong with the way I define the Segmentation nodes and volume nodes under addSegmentation which doesn’t match with the Logical Operators effect script I used from the link <a href="https://gist.github.com/hherhold/ec3f74d20ca63866555f3e66d1f3621c" rel="nofollow noopener">above</a>.<br>
My current definitions are:</p>
<pre><code>slicer.app.processEvents()
masterVolumeNode = slicer.util.loadVolume(file_complete, returnNode = True)[1]
# Create segmentation
segmentationNode_name = filename + "_" + welcheOP + "_segmentation"
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", segmentationNode_name)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</code></pre>

---

## Post #7 by @lassoan (2019-02-07 12:44 UTC)

<p>The error is in your script. Value of <code>effect</code> variable is None. I would recommend to use a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging" rel="nofollow noopener">Python debugger</a> and execute your code step by step to see where it does something different than you would expect.</p>

---

## Post #8 by @ishan_45 (2019-02-13 10:05 UTC)

<p>I made some observations from the debugging process. Since I am using the SegmentEditor module in a loop in my script, it sets the ActiveEffect to None after the first iteration through the loop, and then during the next iteration, I am unable to set the ActiveEffect using</p>
<blockquote>
<p>segmentEditorWidget.setActiveEffectByName(“Logical operators”)</p>
</blockquote>
<p>Any ideas, why I am unable to do that?</p>

---

## Post #9 by @jamesobutler (2019-02-13 12:47 UTC)

<p>Without seeing your code and since you say it works for the first time through the loop, I’m going to guess you haven’t set SementationNode or MasterVolumeNode correctly at the time of setting active effect to logical operators. This might be because you are removing the nodes from the scene after the first iteration?</p>
<p>You might want to consider interacting with the segment editor widget within Slicer and using the python interactor as a way of debugging. Then you could see looking at the GUI what might be going wrong following specific commands.</p>

---

## Post #10 by @ishan_45 (2019-02-14 08:58 UTC)

<p>I have uploaded my code here: <a href="https://gist.github.com/ishansaxena45/2ef0ec665e371a0ff8b91c866129f722" rel="nofollow noopener">https://gist.github.com/ishansaxena45/2ef0ec665e371a0ff8b91c866129f722</a></p>
<p>I am sorry I could not really identify the problem while debugging it manually.</p>

---

## Post #11 by @ishan_45 (2019-03-14 15:01 UTC)

<p>Hi again,</p>
<p>the problem with clearing the scene still remains. I have uploaded my script <a href="https://drive.google.com/drive/folders/1PA85ENYcrxBHwoUaKg8zzx1tm1PlpoPD?usp=sharing" rel="nofollow noopener">here</a> and am also sharing some test data <a href="https://drive.google.com/drive/folders/1PA85ENYcrxBHwoUaKg8zzx1tm1PlpoPD?usp=sharing" rel="nofollow noopener">here</a>. Can someone please help?</p>

---

## Post #12 by @lassoan (2019-03-14 15:07 UTC)

<p>A few weeks ago I’ve implemented an example script that creates segments from a CT based on predefined intensity ranges. You may use this as is, or as a starting point.</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37</a></h4>
<h5>SegmentByThresholding.py</h5>
<pre><code class="Python"># Download a sample data set (chest CT)
import SampleData
masterVolumeNode = SampleData.SampleDataLogic().downloadCTChest()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @ishan_45 (2019-03-15 08:56 UTC)

<p>Thanks so much for your code. The problem is now solved. I was wrong in the definitions of the SegmentEditorWidget and not using SegmentEditorNode. Now everything works as expected.</p>

---
