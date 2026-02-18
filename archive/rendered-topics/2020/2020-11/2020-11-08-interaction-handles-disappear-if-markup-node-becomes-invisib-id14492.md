# Interaction handles disappear if markup node becomes invisible

**Topic ID**: 14492
**Date**: 2020-11-08
**URL**: https://discourse.slicer.org/t/interaction-handles-disappear-if-markup-node-becomes-invisible/14492

---

## Post #1 by @mau_igna_06 (2020-11-08 18:18 UTC)

<p>The objetive was to translate and rotate a model using the interaction handles. To do this I was recommended that I do the translation/rotation using the interaction handles to a plane and then to get it’s PointModifiedEvent connected to a UpdateTransform function that uses GetPlaneToWorldMatrix method to set up the linear transform node I apply to the model. Like it says here:</p><aside class="quote" data-post="2" data-topic="14483">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/interaction-handle-for-one-fiducial-connected-to-a-model/14483/2">Interaction Handle for one Fiducial connected to a Model</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We’ll add a transform widget that will support the features that you describe, probably within a few months. Until then, I would recommend to use a markups plane node to specify position/orientation using the interaction handles (you can hide the plane itself). You can get the transform corresponding to the position/orientation of the plane using <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsPlaneNode.html#aee11e275c748479d7a7232f36e291563" rel="noopener nofollow ugc">GetPlaneToWorldMatrix</a> method.
  </blockquote>
</aside>
<p>
I was able to make the model rotate and translate with the plane’s interaction handles:</p>
<blockquote>
<p>A = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsPlaneNode”, “Plane”)<br>
A.SetOrigin([0,0,-150])<br>
A.SetNormal([0,0,1])<br>
A.SetAxes([100,0,0],[0,100,0],[0,0,100])<br>
A.SetAxes([100,0,0],[0,100,0],[0,0,100])</p>
<p>def UpdateTransform(param1=None, param2=None):<br>
<span class="hashtag-raw">#You</span> have to create a linear transform called LinearTransform_3 in the Transforms module<br>
transformFid = slicer.mrmlScene.GetFirstNodeByName(‘LinearTransform_3’)<br>
matrixScrew = vtk.vtkMatrix4x4()<br>
A.GetPlaneToWorldMatrix(matrixScrew)<br>
transformFid.SetMatrixTransformToParent(matrixScrew)<br>
transformFid.UpdateScene(slicer.mrmlScene)</p>
<p>A.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,UpdateTransform)</p>
<p><span class="hashtag-raw">#Turn</span> on the interaction handles<br>
B = getFirstNodeByClassByName(“vtkMRMLMarkupsDisplayNode”,‘MarkupsDisplay’)<br>
B.SetHandlesInteractive(True)</p>
</blockquote>
<p>But the interaction handles disappear if set up the plane invisible like I was suggested above. I expected the interaction handles remained there so I can move the model.</p>
<blockquote>
<p>B.SetVisibility(False)</p>
</blockquote>

---

## Post #2 by @lassoan (2020-11-08 18:36 UTC)

<p><code>SetVisibility</code> controls visibility of all parts of the markups in all views. If you just want to hide the plane itself then you can set fill and outline opacity to 0.0.</p>

---
