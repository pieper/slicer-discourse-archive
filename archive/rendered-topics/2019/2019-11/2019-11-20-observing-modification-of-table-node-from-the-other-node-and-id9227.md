# Observing modification of table node from the other node and logic

**Topic ID**: 9227
**Date**: 2019-11-20
**URL**: https://discourse.slicer.org/t/observing-modification-of-table-node-from-the-other-node-and-logic/9227

---

## Post #1 by @Mik (2019-11-20 10:01 UTC)

<p>Greetings,</p>
<p>A couple of questions of loadable module development, some general stuff.</p>
<ol>
<li>
<p>What king of event generated when cells in table node are modified<br>
via “Tables” module or in table viewer?<br>
<code>vtkCommand::ModifiedEvent</code>,<br>
<code>vtkMRMLTableNode::ReferencedNodeModifiedEvent</code>,<br>
<code>vtkMRMLTableNode::ReferenceModifiedEvent</code></p>
</li>
<li>
<p>What overridden methods in logic must be modified to process a table node modifications?<br>
<code>vtkMyModuleLogic::ProcessMRMLNodesEvents</code>,<br>
<code>vtkMyModuleLogic::OnMRMLSceneNodeAdded</code>,<br>
<code>vtkMyModuleLogic::SetMRMLSceneInternal</code></p>
</li>
<li>
<p>When module logic is ready to process table node events, and table node on the same scene with other node , how should i observe table node from other node?<br>
<code>other_node-&gt;SetNodeReferenceID( "Role", tableNode-&gt;GetID());</code><br>
or<br>
<code>other_node-&gt;SetAndObserveNodeReferenceID( "Role", tableNode-&gt;GetID());</code></p>
</li>
</ol>
<p>Best regards,<br>
Mikhail</p>

---

## Post #2 by @lassoan (2019-11-20 16:53 UTC)

<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="9227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>What king of event generated when cells in table node are modified<br>
via “Tables” module or in table viewer?<br>
<code>vtkCommand::ModifiedEvent</code> ,<br>
<code>vtkMRMLTableNode::ReferencedNodeModifiedEvent</code> ,<br>
<code>vtkMRMLTableNode::ReferenceModifiedEvent</code></p>
</blockquote>
</aside>
<p>When you modify a cell in a table, it invokes <code>vtkCommand::ModifiedEvent</code> event on the vtkMRMLTableNode.</p>
<p><code>vtkMRMLNode::ReferencedNodeModifiedEvent</code> and <code>vtkMRMLNode::ReferenceModifiedEvent</code> invoked on a node that references another node. If you reference a table node from node A, then ReferencedNodeModifiedEvent will be invoked on A if the table is modified; and ReferenceModifiedEvent will be invoked if you switch which table node you reference.</p>
<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="9227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>What overridden methods in logic must be modified to process a table node modifications?</p>
</blockquote>
</aside>
<p>If you want to observe all changes of all table nodes in the scene then you need to observe all scene setting and scene node added/removed/batch update events so that you can add observer to all table nodes, and then override ProcessMRMLNodesEvents to get notification about changes in any nodes. See for example <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/Logic/vtkSlicerBreachWarningLogic.cxx">vtkSlicerBreachWarningLogic</a>.</p>
<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="9227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>When module logic is ready to process table node events, and table node on the same scene with other node , how should i observe table node from other node?</p>
</blockquote>
</aside>
<p>You observe changes of another node from a module logic as I described above.</p>
<p>If you want to observe referenced node changes from another node then you need to declare the node reference role in the constructor (specifying which events you want to observe) and add node reference using SetAndObserveNodeReferenceID. See for example <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLTransformableNode.cxx#L40">vtkMRMLTransformableNode</a>.</p>

---

## Post #3 by @Mik (2019-11-22 18:19 UTC)

<p>Thank you for explanation!</p>
<p>The easiest method was using logic class by adding observer to table node modified event in<br>
<a href="https://github.com/MichaelColonel/SlicerRT/blob/multi-leaf-collimators/Beams/Logic/vtkSlicerBeamsModuleLogic.cxx#L109-#L114" rel="nofollow noopener">OnMRMLSceneNodeAdded</a>, and then process table node events in <a href="https://github.com/MichaelColonel/SlicerRT/blob/multi-leaf-collimators/Beams/Logic/vtkSlicerBeamsModuleLogic.cxx#L239-#L261" rel="nofollow noopener">ProcessMRMLNodesEvents</a>.</p>
<p>Offtopic: The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#Can_I_use_C.2B.2B11.2F14.2F17_language_features_.3F" rel="nofollow noopener">developer manual</a> doesn’t recommend using C++11 elements, but many modules have <em>override</em>, <em>default</em> keywords, <em>std::array</em> variables and <em>nullptr</em>. What about using java-like cycles, auto, lambda expressions and initializer lists?</p>

---

## Post #4 by @lassoan (2019-11-22 19:48 UTC)

<aside class="quote no-group" data-username="Mik" data-post="3" data-topic="9227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#Can_I_use_C.2B.2B11.2F14.2F17_language_features_.3F">developer manual </a> doesn’t recommend using C++11 elements,</p>
</blockquote>
</aside>
<p>The developer manual has not been updated. I would say Slicer follows VTK conventions in this (which is now accepts usage of most C++11 features).</p>

---
