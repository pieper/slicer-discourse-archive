# Transformation graph for quick calculation of concatenated transforms

**Topic ID**: 326
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/transformation-graph-for-quick-calculation-of-concatenated-transforms/326

---

## Post #1 by @mangotee (2017-05-16 17:23 UTC)

<p>Hi,</p>
<p>I am looking for a quick way to compute an in-between transformation between two volume nodes that are not directly connected in a transformation graph. Here is a figure of what I mean:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/303601b8f03cca77b1b6abbbb1d6c94e2e962c66.jpg" data-download-href="/uploads/short-url/6SuCTY0Rk8tmYq7o4FTw4wxp7RI.jpg?dl=1" title="figSlicerTransformationGraph.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/303601b8f03cca77b1b6abbbb1d6c94e2e962c66_2_286x250.jpg" width="286" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/303601b8f03cca77b1b6abbbb1d6c94e2e962c66_2_286x250.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/303601b8f03cca77b1b6abbbb1d6c94e2e962c66_2_429x375.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/303601b8f03cca77b1b6abbbb1d6c94e2e962c66_2_572x500.jpg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figSlicerTransformationGraph.jpg</span><span class="informations">838×732 46.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Assume I have several MRI contrasts (T1/T2/T2S and HR), and I want to resample T2S in the voxel grid of a high-resolution volume “HR”. Often, I need a direct transform between the two, i.e. “T2SToHR”, e.g. for a module like “Resample Scalar/Vector/DWI Volume” to function.</p>
<p>In PLUS, this is neatly solved with a transformation graph, and I can simply give a string “T2SToHR” which is parsed to calculate the in-between transform via graph traversal.<br>
Is there a similar mechanism in Slicer?<br>
I want to use the “Resample Scalar/Vector/DWI Volume” module, and I want to avoid coding the transformation chain out explicitly every time I want to do such an operation.</p>
<p>Cheers,<br>
Ahmad</p>

---

## Post #2 by @lassoan (2017-05-16 17:31 UTC)

<p>Use <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#acbab274893b3d11cac30c4ee8a036f96">slicer.vtkMRMLTransformNode.GetTransformBetweenNodes</a> method for general transforms (to get a transformation chain that can include any number of non-linear transforms).</p>
<p>If you only have linear transforms between the nodes you can get the concatenated transforms as a single 4x4 matrix by using<br>
<a href="http://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#acbab274893b3d11cac30c4ee8a036f96">slicer.vtkMRMLTransformNode.GetMatrixTransformBetweenNodes</a>.</p>
<p>To use this transform in a CLI module, create a new transform node and set the concatenated transform into that.</p>

---

## Post #3 by @mangotee (2017-05-16 19:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.vtkMRMLTransformNode.GetTransformBetweenNodes</p>
</blockquote>
</aside>
<p>Thanks a lot! This looks exactly like what I need. However, I have problems with executing the command. Given the example above, I tried the following:<br>
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(nT2SToT2.SafeDownCast(vtk.vtkGeneralTransform()), nHRToT1.SafeDownCast(vtk.vtkGeneralTransform()), T.SafeDownCast(vtk.vtkGeneralTransform()))</p>
<p>(note: I had to SafeDownCast() - all transforms are linear - to a vtkGeneralTransform. I could have tried the matrix4x4 version you mentioned, but I wanted to try the general approach for more complex scenarios later).<br>
The command runs, but the result is wrong as I receive the identity matrix.<br>
I also received the following warning in the log:<br>
Generic Warning: In /Users/kitware/Dashboards/Package/Slicer-462/Libs/MRML/Core/vtkMRMLTransformNode.cxx, line 472 vtkMRMLTransformNode::GetTransformToNode failed: transformSourceToTarget is invalid</p>
<p>Could you give a hint regarding the syntax?<br>
Thanks!</p>

---

## Post #4 by @mangotee (2017-05-16 19:46 UTC)

<p>P.S.: the volumes and transforms (as in the figure above) are arranged in the scene as follows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b8ba70bb1c84515d3e7ab449ffd4e0f807cc24c.png" alt="image" data-base62-sha1="8uLnf8rQeqvTfOHyBR7iGXxjYfy" width="168" height="192"></p>

---

## Post #5 by @lassoan (2017-05-16 19:57 UTC)

<p>Example:</p>
<pre><code>transformAToB = vtk.vtkGeneralTransform()
a = getNode('MRHead').GetParentTransformNode()
b = getNode('CTChest').GetParentTransformNode()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(a, b, transformAToB)
</code></pre>
<p>If you want to use transformAToB in a transform node using SetTransformToParent then you have to deep-copy it using slicer.vtkMRMLTransformNode.DeepCopyTransform. If you only have linear transforms it is much simpler and faster to use GetMatrixTransformBetweenNodes and SetMatrixTransformToParent.</p>

---

## Post #6 by @mangotee (2017-05-16 20:00 UTC)

<p>Excellent. I’ll try this out!<br>
Again thanks a lot for the quick reply!</p>

---

## Post #7 by @mangotee (2017-05-17 16:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.vtkMRMLTransformNode.DeepCopyTransform</p>
</blockquote>
</aside>
<p>OK, I wrote a little utility function. In case it helps anyone, I’ll post it here. Apologies for poor naming etc… Also, indentation is wrong - if someone knows how to properly post formatted pieces of code, please let me know.</p>
<pre><code>  def calculateInbetweenLinearTransform(self,nTrfSource,nTrfTarget,nTrfSourceToTarget):
    # Get concatenated transforms from source to target nodes in the MRML scene. Source 
    # and target nodes are allowed to be NULL, which represents the world coordinate 
    # system. Result is written into nTrfSourceToTarget (has to be a
    # vtkMRMLLinearTransformNode)
    matrixAToB = vtk.vtkMatrix4x4()
    if nTrfSource is not None:
      a = nTrfSource.GetParentTransformNode()
    else:
      a = None
    if nTrfTarget is not None:
      b = nTrfTarget.GetParentTransformNode()
    else:
      b = None
    # calculate the matrix transform
    slicer.vtkMRMLTransformNode.GetMatrixTransformBetweenNodes(a,b,matrixAToB)
    # set the matrix transform into target
    nTrfSourceToTarget.SetMatrixTransformToParent(matrixAToB)
</code></pre>

---

## Post #8 by @Fernando (2017-05-17 17:09 UTC)

<p>You just need to add 4 spaces to your code, there’s even a button for it on the Discourse GUI.</p>
<pre><code>def calculateInbetweenLinearTransform(self, nTrfSource, nTrfTarget, nTrfSourceToTarget):
    # Get concatenated transforms from source to target nodes in the MRML scene. Source 
    # and target nodes are allowed to be NULL, which represents the world coordinate 
    # system. Result is written into nTrfSourceToTarget (has to be a
    # vtkMRMLLinearTransformNode)
    matrixAToB = vtk.vtkMatrix4x4()
    if nTrfSource is not None:
        a = nTrfSource.GetParentTransformNode()
    else:
        a = None
    if nTrfTarget is not None:
        b = nTrfTarget.GetParentTransformNode()
    else:
        b = None
    # calculate the matrix transform
    slicer.vtkMRMLTransformNode.GetMatrixTransformBetweenNodes(a,b,matrixAToB)
    # set the matrix transform into target
    nTrfSourceToTarget.SetMatrixTransformToParent(matrixAToB)</code></pre>

---

## Post #9 by @Fernando (2017-05-21 18:28 UTC)

<p>Andras’ answer should be the solution of this topic, not mine.</p>

---

## Post #10 by @xxzhou (2018-09-11 15:15 UTC)

<p>Hi! I am new for 3D Slicer, and when I to used your method to calculate the transform matrix, I found that<br>
a = getNode().GetParentTransformNode,<br>
a is NONE, same as b. This resulted in transformAToB equaled to Identity Matrix.</p>
<p>But if I directly use<br>
a,b = getNode(),<br>
transformAToB = slicer.vtkMRMLTransformNode()<br>
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(a, b, transformAToB)</p>
<p>I was told method requires a vtkMRMLTransformNode, a vtkMRMLScalarVolumeNode was provided.</p>
<p>I am wondering if anyone could help me find out why this problem comes out.</p>
<p>Appreciate your help!<br>
Thank you.<br>
Cheers,<br>
xxzhou</p>

---

## Post #11 by @cpinter (2018-09-11 15:54 UTC)

<aside class="quote no-group" data-username="xxzhou" data-post="10" data-topic="326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/13edae/48.png" class="avatar"> xxzhou:</div>
<blockquote>
<p>a = getNode().GetParentTransformNode</p>
</blockquote>
</aside>
<p>Please post your actual code that doesn’t work because the one above for example is not valid, and it’s impossible like this to figure out what is going wrong.</p>

---

## Post #12 by @xxzhou (2018-09-11 16:22 UTC)

<p>Thank you for responding! Sure.</p>
<p>My code is as below:</p>
<p>source = getNode(‘preop’).GetParentTransformNode()<br>
target = getNode(‘intraop’).GetParentTransformNode()<br>
transformNode = vtk.vtkGeneralTransform()<br>
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(source, target, transformNode)</p>
<p>Then I use:<br>
print(transformNode)</p>
<p>Output is:<br>
vtkGeneralTransform (0x608000134fa0)<br>
Debug: Off<br>
Modified Time: 2504871<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Inverse: (0)<br>
Input: (0)<br>
InverseFlag: 0<br>
NumberOfConcatenatedTransforms: 0</p>
<p>There is no error, but actually source and target all equal to NONE, so it seems that transformNode = NONE</p>
<p>When I try to change as below:</p>
<p>source = getNode(‘preop’)<br>
target = getNode(‘intraop’)<br>
TransformMatrix = vtk.vtkGeneralTransform()<br>
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(source, target, TransformMatrix)</p>
<p>GetTransformBetweenNodes argument 1: method requires a vtkMRMLTransformNode, a vtkMRMLScalarVolumeNode was provided.</p>
<p>I think it is because source and target are both vtkMRMLScalarVolumeNode. I am wondering how to change the vtkMRMLScalarVolumeNode to vtkMRMLTransformNode, which is not NONE.</p>
<p>I am also wondering how to apply this transform matrix on the source image. I have tried the code above:</p>
<p>nTrfSourceToTarget = slicer.vtkMRMLTransformNode<br>
nTrfSourceToTarget.SetMatrixTransformToParent(transformNode)</p>
<p>but it seems do not work. The error is:<br>
TypeError: unbound method requires a vtkCommonCorePython.vtkMRMLTransformNode as the first argument</p>
<p>Too many questions…<br>
Thank you for your help!</p>

---

## Post #13 by @cpinter (2018-09-11 17:55 UTC)

<p>How about this:</p>
<pre><code>source = getNode(‘preop’)
target = getNode(‘intraop’)
sourceToTargetTransformNode = slicer.vtkMRMLLinearTransformNode()
slicer.mrmlScene.AddNode(sourceToTargetTransformNode)
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(source, target, sourceToTargetTransformNode)
</code></pre>
<p>You can set a parent transform with <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLTransformableNode.h#L59">SetAndObserveTransformNodeID</a></p>
<p>The problem in your code has been using the wrong types in each case. You need to make sure that you pass/create/get the object you need, and not some related object of a different type.</p>

---
