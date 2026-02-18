# Centroid determination

**Topic ID**: 3541
**Date**: 2018-07-20
**URL**: https://discourse.slicer.org/t/centroid-determination/3541

---

## Post #1 by @Naia (2018-07-20 12:59 UTC)

<p>I am trying to determine the centroid of several previously segmented materials. I can’t find this option in the Quantification module “Segment Statistics” of this software.<br>
Is there any solution to this problem or the software 3D Slicer does’nt have any module that determines the centroid of an already segmented material?</p>
<p>I am currently using version 4.8.1 of the 3D Slicer software.</p>

---

## Post #2 by @laoweijianglin (2018-07-22 03:13 UTC)

<p>I have the same issue as yours.</p>

---

## Post #3 by @lassoan (2018-07-22 11:49 UTC)

<p>It is shown in this example how to get the centroid using numpy and then transform the raw array coordinates to scene RAS coordinates: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates</a></p>

---

## Post #4 by @szhang (2020-09-22 20:19 UTC)

<p>I have some follow-up questions:</p>
<ol>
<li>If there is only vtkMRMLModelNode, how can I find centroid of a VTK model?</li>
<li>If 1) is not possible, how can I convert model to segmentation in a loadable script? I cannot find any associated function from slicer.modules.models.logic()</li>
</ol>
<p>Thank you very much!</p>

---

## Post #5 by @lassoan (2020-09-22 21:01 UTC)

<p>You can get center point very quickly as center of bounding box, with a little more computation from centroid of model points, or the exa t centroid (center of gravity assuming the model is filled with material of uniform density) using Segment statistics module.</p>

---

## Post #6 by @szhang (2020-09-23 01:53 UTC)

<p>I see, thank you.<br>
I ended up implementing it without referring to bounding box, here’s my sample code as future reference for anyone who needs it:</p>
<blockquote>
<p>md = slicer.util.getNode(‘ModelX’)<br>
pd = md.GetPolyData().GetPoints().GetData()<br>
from vtk.util.numpy_support import vtk_to_numpy<br>
import numpy as np<br>
print(np.average(vtk_to_numpy(pd), axis=0))</p>
</blockquote>
<p>The output should print the average coordinate of all points within a vtkMRMLModelNode.</p>

---

## Post #7 by @lassoan (2020-09-23 02:16 UTC)

<p>Thank you for sharing the solution! You can use <code>slicer.util</code> helper functions to simplify things a bit:</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode(‘ModelX’)
pointCoordinates = slicer.util.arrayFromModelPoints(modelNode)
import numpy as np
print(np.average(vtk_to_numpy(pd), axis=0))
</code></pre>
<p>or even shorter (a bit less explicit, so I would only recommend for testing and troubleshooting, not in modules):</p>
<pre><code class="lang-auto">import numpy as np
print(np.average(array('ModelX'), axis=0))
</code></pre>

---

## Post #8 by @szhang (2020-09-23 02:21 UTC)

<p>Oh, great! I like the two line solution, and it reads quite explicit to me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @Optics_Bioeng (2023-07-03 04:55 UTC)

<p>I have a question about getting a centroid of segment.<br>
I ran this code below, but it couldn’t work.</p>
<pre><code class="lang-python">segmentationNode = slicer.util.getNode("vtkMRMLSegmentationNode1")
segmentId = "Segment_1"

# Get array voxel coordinates
seg=slicer.util.arrayFromSegment(segmentationNode, segmentId)
# numpy array has voxel coordinates in reverse order (KJI instead of IJK)
# and the array is cropped to minimum size in the segmentation
mean_KjiCropped = [coords.mean() for coords in np.nonzero(seg)]

# Get segmentation voxel coordinates
segImage = segmentationNode.GetBinaryLabelmapRepresentation(segmentId)
segImageExtent = segImage.GetExtent()
# origin of the array in voxel coordinates is determined by the start extent
mean_Ijk = [mean_KjiCropped[2], mean_KjiCropped[1], mean_KjiCropped[0]] + np.array([segImageExtent[0], segImageExtent[2], segImageExtent[4]])

# Get segmentation physical coordinates
ijkToWorld = vtk.vtkMatrix4x4()
segImage.GetImageToWorldMatrix(ijkToWorld)
mean_World = [0, 0, 0, 1]
ijkToRas.MultiplyPoint(np.append(mean_Ijk,1.0), mean_World)
mean_World = mean_World[0:3]

# If segmentation node is transformed, apply that transform to get RAS coordinates
transformWorldToRas = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(segmentationNode.GetParentTransformNode(), None, transformWorldToRas)
mean_Ras = transformWorldToRas.TransformPoint(mean_World)

# Show mean position value and jump to it in all slice viewers
print(mean_Ras)
slicer.modules.markups.logic().JumpSlicesToLocation(mean_Ras[0], mean_Ras[1], mean_Ras[2], True)
</code></pre>
<p>from <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a><br>
I got error below</p>
<pre><code class="lang-python">TypeError                                 Traceback (most recent call last)
Cell In[15], line 11
      8 mean_KjiCropped = [coords.mean() for coords in np.nonzero(seg)]
     10 # Get segmentation voxel coordinates
---&gt; 11 segImage = segmentationNode.GetBinaryLabelmapRepresentation(segmentId)
     12 segImageExtent = segImage.GetExtent()
     13 # origin of the array in voxel coordinates is determined by the start extent

TypeError: GetBinaryLabelmapRepresentation() takes exactly 2 arguments (1 given)
</code></pre>
<p>Could you teach me the reason why this error happen?<br>
Thank you</p>

---

## Post #10 by @rbumm (2023-07-03 07:01 UTC)

<aside class="quote no-group" data-username="Optics_Bioeng" data-post="9" data-topic="3541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/optics_bioeng/48/66534_2.png" class="avatar"> Optics_Bioeng:</div>
<blockquote>
<p><code>GetBinaryLabelmapRepresentation</code></p>
</blockquote>
</aside>
<p>You should probably call the function <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-representation-of-a-segment" rel="noopener nofollow ugc">as shown in the latest script repository</a>.</p>

---
