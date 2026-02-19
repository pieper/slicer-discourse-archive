---
topic_id: 34215
title: "Is There A Setter Similar For The Getter Getinteractionhandl"
date: 2024-02-08
url: https://discourse.slicer.org/t/34215
---

# Is there a Setter similar for the Getter GetInteractionHandleToWorldMatrix?

**Topic ID**: 34215
**Date**: 2024-02-08
**URL**: https://discourse.slicer.org/t/is-there-a-setter-similar-for-the-getter-getinteractionhandletoworldmatrix/34215

---

## Post #1 by @Juergen (2024-02-08 20:58 UTC)

<p>Hello,<br>
I am using SlicerJupyter and I’m trying to use the interaction handle for the MarkupsLineNode to control the position and orientation of other objects. That part works fine with this kind of code:</p>
<p>implantlinenode = slicer.vtkMRMLMarkupsLineNode()</p>
<p>implantlinenode.SetName(‘Implant line’)</p>
<p>slicer.mrmlScene.AddNode(implantlinenode)</p>
<p>implantlinenode.AddControlPoint(0, 0, 0, ‘P0’)<br>
implantlinenode.AddControlPoint(0, 10, 0, ‘P1’)</p>
<p>Ldn = implantlinenode.GetDisplayNode()</p>
<p>Ldn.SetVisibility2D(True)<br>
Ldn.SetVisibility3D(True)</p>
<p>Ldn.SetHandlesInteractive(True)</p>
<p>handlematrix = implantlinenode.GetInteractionHandleToWorldMatrix()</p>
<p>However, I also need to update the InteractionHandle orientations programmatically based on the orientation of other objects.</p>
<p>How would I do this? I tried a transformation of the MarkupsLineNode but that does not change the orientation of the InteractionHandle.</p>
<p>Thanks for any ideas</p>

---

## Post #2 by @lassoan (2024-02-09 02:26 UTC)

<aside class="quote no-group" data-username="Juergen" data-post="1" data-topic="34215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juergen/48/66870_2.png" class="avatar"> Juergen:</div>
<blockquote>
<p>I’m trying to use the interaction handle for the MarkupsLineNode to control the position and orientation of other objects.</p>
</blockquote>
</aside>
<p>I have very good news for you! Thanks to <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, it is no longer necessary to create markups to position and orientation nodes. In recent Slicer Preview Releases (since last week), <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/NewInteractionWidgetForTransformsMarkups/">transformation handles can be enabled for any nodes</a>.</p>

---

## Post #3 by @muratmaga (2024-02-09 04:27 UTC)

<p>This looks great. Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> (and andras). Quick question:</p>
<p>I set the MRHead under a transform, and I hit the visibility (eye icon) of the transform node, with the expectation that the widget will become visible. But it didn’t. The only way I managed to turn it on is from the Transforms module’s Interaction tab.</p>
<p>Is there any reason why visibility shouldn’t be considered as the interaction in this context? Or is it specifically referring to the visibility of the Glyphs or Grids?</p>

---

## Post #4 by @Juergen (2024-02-09 13:01 UTC)

<p>Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and Andras. That sounds amazing.<br>
Do you have some documentation on it how to use it in Python or can you roughly tell me how to set it up in Python?<br>
Thanks, such great timing!</p>

---

## Post #5 by @lassoan (2024-02-09 15:11 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="34215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Or is it specifically referring to the visibility of the Glyphs or Grids?</p>
</blockquote>
</aside>
<p>Exactly. This is consistent with how visibility refers to visibility of every other nodes.</p>
<p>To move around a node, the easiest is to go to “Data” module, right-click on the eye icon of the node, and enable “Interaction in 3D view”. This adds a positioning transforms and enables interaction handles. We’ll change the behavior of this menu action so that <a href="https://github.com/Slicer/Slicer/issues/7570">it will show the transformation in 2D as well</a> and we might need to find a better name (maybe “Transform interaction”).</p>

---

## Post #6 by @Juergen (2024-02-09 15:56 UTC)

<p>I appreciate your work on the continuous Slicer improvements.</p>
<p>However, I find it very hard to switch to a new version because I have to re-install all the Extensions I’ve been using, set up another Slicer Kernel for Jupyter, and possibly also re-check my slicerrc file to be in the right location even if it was in a default location. The same applies to the DICOM database location and sometimes version.</p>
<p>Is there a less painful way to do all this? Do you have a post-installation script that does all this repetitive work automatically but fails gracefully when it can’t do some parts?</p>
<p>Any suggestions would be greatly appreciated. Thanks.</p>

---

## Post #7 by @lassoan (2024-02-09 16:07 UTC)

<p>It should be painless to upgrade. You can bookmark all your installed extensions and reinstall them in the new Slicer version by a single click. All other settings are preserved. There is a whole new DICOM browser (another reason to upgrade), with a slightly different DICOM database schema, so you may need to upgrade the DICOM database (it should be a single click when you are asked). If you find any unnecessary inconvenience then let us know.</p>

---

## Post #8 by @Juergen (2024-02-09 16:14 UTC)

<p>Thanks, Andras.</p>
<p>Until now I had not noticed the Bookmark feature. That’s really great to know. If it was described in a Manual somewhere I certainly failed to catch it. My apologies.</p>

---

## Post #9 by @lassoan (2024-02-09 16:51 UTC)

<p>It is described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions">How to install extensions</a>. Feel free to make any suggestions on how to improve the documentation.</p>

---

## Post #10 by @Juergen (2024-02-09 19:55 UTC)

<p>This is how far I’ve gotten:</p>
<p>arcmodel = modelsLogic.AddModel(extrude_arc.GetOutputPort())</p>
<p>arcmodel.SetName(‘arc’)</p>
<p>dn = arcmodel.GetDisplayNode()<br>
dn.SetSliceIntersectionVisibility(True)<br>
dn.SetSliceDisplayModeToIntersection()<br>
dn.SetSliceIntersectionThickness(3)<br>
dn.SetColor(0.902, 0.020, 0.902)</p>
<p>dn.SetVisibility2D(True)<br>
dn.SetVisibility3D(True)</p>
<p><strong>Now I have to manually right click on arcmodel node and set “Interaction in 3D view” to create an Interaction_arc transformation node. How can I do this programmatically?</strong></p>
<p>arctransform = arcmodel.GetParentTransformNode()<br>
print(arctransform)</p>
<p>tdn = arctransform.GetDisplayNode()</p>
<p>tdn.SetVisibility(True)</p>
<p>tdn.SetVisibility2D(False)<br>
tdn.SetVisibility3D(False)</p>
<p>tdn.SetEditorVisibility(True)<br>
tdn.SetEditorSliceIntersectionVisibility(True)</p>
<p>tdn.SetEditorTranslationEnabled(True)<br>
tdn.SetTranslationHandleComponentVisibility(True, True, True, True)<br>
tdn.SetEditorRotationEnabled(True)<br>
tdn.SetRotationHandleComponentVisibility(True, True, True, True)<br>
tdn.SetEditorScalingEnabled(True)<br>
tdn.SetScaleHandleComponentVisibility(True, True, True, True)</p>
<p><strong>Now I can do several things:</strong></p>
<p>arctransform.SetCenterOfTransformation(0, 0, 0)<br>
arctransform.SetMatrixTransformToParent(slicer.util.vtkMatrixFromArray(newtransform))</p>
<p><strong>But how can I set the scaling in my program? Where can I read the scaling that I manipulate in the GUI?</strong></p>
<p>Thanks</p>

---

## Post #11 by @lassoan (2024-02-09 20:23 UTC)

<aside class="quote no-group" data-username="Juergen" data-post="10" data-topic="34215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juergen/48/66870_2.png" class="avatar"> Juergen:</div>
<blockquote>
<p>Now I have to manually right click on arcmodel node and set “Interaction in 3D view” to create an Interaction_arc transformation node. How can I do this programmatically?</p>
</blockquote>
</aside>
<p>You can find examples for every commonly needed operations in the script repository. For example, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-transform-to-a-transformable-node">apply a transform</a>.</p>
<aside class="quote no-group" data-username="Juergen" data-post="10" data-topic="34215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juergen/48/66870_2.png" class="avatar"> Juergen:</div>
<blockquote>
<p>But how can I set the scaling in my program?</p>
</blockquote>
</aside>
<p>You can either get familiar with homogeneous transformation matrices and set the matrix values directly (e.g., scaling is the column norm) or you can use <a href="https://vtk.org/doc/nightly/html/classvtkTransform.html">vtkTransform</a> to compute the matrix from a sequence of operations (scale, rotate, translate, etc.).</p>
<p>What is your end goal? Planning needle insertion with a stereotactic frame (guessing from the “arc” word)? If yes then check out the <a href="https://github.com/IM2Neuroing/SlicerStereotactic">Stereotactic extension</a>. There are many other extensions that can be relevant, depending on what you plan to do.</p>

---

## Post #12 by @Juergen (2024-02-09 20:43 UTC)

<p>Ok, thanks. I did not understand that now any transform node has the interaction display attach to it? I’ve done the transform before, so thanks for the clarification.</p>
<p>With respect to the scaling, I had not noticed that the transformation matrix changed in a way that the column vectors weren’t just normalized direction vectors any more, but had scaling information. Thanks for pointing that out.</p>
<p>Eventually I want to parameterize the location and shape of an implant that will get 3D printed. I will print different versions according to some parameters and then test them on the benchtop. The implant shape is derived from a couple of prototypical shapes, that’s why one of them is called ‘arc’ because it’s been made from the vtkEllipseArcSource to make an elliptical cylinder.</p>

---

## Post #13 by @lassoan (2024-02-10 17:04 UTC)

<p>Sounds interesting. Keep us updated on your progress, maybe post some pictures when you have some success (and feel free to ask any questions if you get stuck with something).</p>

---

## Post #14 by @Juergen (2024-02-12 19:30 UTC)

<p>Sure, I will post some pictures when I get it all working.</p>
<p>I’m trying to set up everything programmatically, so right now I’m still stuck at the point where I want to enable the new visualization for the transformation node:</p>
<p>arctransform = slicer.vtkMRMLTransformNode()<br>
arctransform.SetName(‘Transform arc’)</p>
<p>slicer.mrmlScene.AddNode(arctransform)</p>
<p>arcmodel.SetAndObserveTransformNodeID(arctransform.GetID())</p>
<p>But, if I want to modify the DisplayNode of the transform node, I get None:<br>
arctransform.GetDisplayNode() → None</p>
<p>Only when I manually right-click on the transform node in Data (Edit propertires) and then manually expand/open the Display submenu, then I can programmatically modify the DisplayNode:<br>
&lt;MRMLCorePython.vtkMRMLTransformDisplayNode(0x000001E85A8304C0) at 0x000001E861DF3640&gt;</p>
<p>I tried to manually add some display node but that did not work, it did not create the new manipulation handle display:<br>
tdn = slicer.vtkMRMLTransformDisplayNode()<br>
arctransform.AddAndObserveDisplayNodeID(tdn.GetID())</p>
<p>Has this not been implemented yet?<br>
Thanks, Juergen</p>

---

## Post #15 by @lassoan (2024-02-12 20:30 UTC)

<p>You can call <code>displayableNode.CreateDefaultDisplayNodes()</code> to create default display node.</p>
<p>For future postings on the forum: if you include code snippets in your post, you can put it between <a href="https://www.markdownguide.org/extended-syntax/#fenced-code-blocks">triple-backticks</a> for better formatting.</p>

---
