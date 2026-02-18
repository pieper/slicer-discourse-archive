# How to get the transform edited in 3D views interactively in Python Interacter

**Topic ID**: 20322
**Date**: 2021-10-24
**URL**: https://discourse.slicer.org/t/how-to-get-the-transform-edited-in-3d-views-interactively-in-python-interacter/20322

---

## Post #1 by @Springle (2021-10-24 13:20 UTC)

<p>Operating system: win10 64 20H2<br>
Slicer version: 4.11.20200930<br>
Expected behavior: get the transform edited in 3D views interactively in Python Interacter<br>
Actual behavior:</p>
<p>I am trying to automate my segmentation process using Python Interacter, but sometimes still needs manual opreation. After the ROI drawing, i need to rotate the segmentation label, so i create a new transformnode  and link it to the segmentation node. But i can not find a way to get the transform edited in 3D views interactively, as the “interation in 3d view” function do in the GUI. The following is the code patch:</p>
<p>SegNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSegmentationNode”)<br>
transformNode = slicer.vtkMRMLTransformNode()<br>
slicer.mrmlScene.AddNode(transformNode)<br>
SegNode.SetAndObserveTransformNodeID(transformNode.GetID())<br>
SegNode.CreateClosedSurfaceRepresentation()</p>
<p>and the next code is to get the transform edited in 3D views interactively.</p>
<p>Is there a way to do it?</p>
<p>Any help is much appreciated!</p>

---

## Post #2 by @ungi (2021-10-25 02:56 UTC)

<p>Hi, I used your code, then edited the transform interactively, and then printed the edited transformation matrix with this code in the python interactor:<br>
<code>print(transformNode.GetMatrixTransformToParent())</code><br>
The printed transform matrix was the same as what I see in the Transforms module. So I guess you can use “transformNode” to get the results of your interactions.</p>

---

## Post #3 by @Springle (2021-10-25 03:45 UTC)

<p>Hi, Tamas,</p>
<p>Thank you very much for you reply. What i need is to get a boundary or bounding box of my segmentation in 3D view window and then to drag or rotate the segmentation boundary to modify the position of my segmentation. This can be achieved in the GUI as this post did:</p>
<aside class="quote quote-modified" data-post="3" data-topic="14886">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/moving-segmentation/14886/3">Moving segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can do all this in the Data module, by right-clicking on the transforms column: 
[interactive_transform] 
Transform is rotated by left-click-and-drag, and translated by Shift+left-click-and-drag. 
“Harden transform” in the end if for permanently applying the transformation to the selected node, which is probably not needed for what the use case described above.
  </blockquote>
</aside>

<p>But i can not find a code way to do it.</p>

---

## Post #4 by @Springle (2021-10-25 09:57 UTC)

<p>According to the FAQ:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>I found this action is defined in qSlicerSubjectHierarchyTransformsPlugin.cxx file, and the connected method is: void qSlicerSubjectHierarchyTransformsPlugin::toggleInteractionBox(bool visible). It is defined in “<a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Transforms/SubjectHierarchyPlugins/qSlicerSubjectHierarchyTransformsPlugin.cxx" class="inline-onebox" rel="noopener nofollow ugc">Slicer/qSlicerSubjectHierarchyTransformsPlugin.cxx at 0094e9a35bd266cc8b0e677858dabce797c9928f · Slicer/Slicer · GitHub</a>” in line 443.</p>
<p>However i still fail to emulate this “interaction in 3d view” action. I thought i need to access the qSlicerSubjectHierarchyTransformsPlugin object, but i fail to access it using slicer.qSlicerSubjectHierarchyTransformsPlugin().toggleInteractionBox.</p>
<p>I also failed to emulate it trying to using the code inside the “toggleInteractionBox” function.</p>
<p>Anyone has some suggestions?</p>

---

## Post #5 by @mikebind (2021-10-25 18:34 UTC)

<p>You were on the right track.  In the toggleInteractionBox code in <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Transforms/SubjectHierarchyPlugins/qSlicerSubjectHierarchyTransformsPlugin.cxx#L473" class="inline-onebox" rel="noopener nofollow ugc">Slicer/qSlicerSubjectHierarchyTransformsPlugin.cxx at 0094e9a35bd266cc8b0e677858dabce797c9928f · Slicer/Slicer · GitHub</a> I saw displayNode.SetEditorVisibility(visible), which helped me find the following</p>
<p><code>transformNode.GetDisplayNode().SetEditorVisibility(True)</code></p>
<p>to show the interactive controls (setting visibility to False would hide them).  I think that’s what you were looking for, if not, please clarify and ask again.</p>

---

## Post #6 by @Springle (2021-10-26 00:23 UTC)

<p>Thanks Mike,</p>
<p>i tried what you told me. But <code>transformNode.GetDisplayNode()</code> returns NULL, and can not call <code>SetEditorVisibility</code> method.</p>
<p>The newly create transform do not have transform display node. Maybe i should create a new display node and try to link it to the transform node.</p>

---

## Post #7 by @Springle (2021-10-26 00:31 UTC)

<p>Thank you very much, Mike.</p>
<p>I finally made it.</p>
<p>The code should be</p>
<pre><code class="lang-auto">SegNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
transformNode = slicer.vtkMRMLTransformNode()
slicer.mrmlScene.AddNode(transformNode)
SegNode.SetAndObserveTransformNodeID(transformNode.GetID())
SegNode.CreateClosedSurfaceRepresentation()
transformNode.CreateDefaultDisplayNodes()
transformNode.GetDisplayNode().SetEditorVisibility(True)
</code></pre>

---
