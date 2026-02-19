---
topic_id: 10417
title: "Ui State Management In Scripted Modules"
date: 2020-02-24
url: https://discourse.slicer.org/t/10417
---

# UI state management in scripted modules

**Topic ID**: 10417
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/ui-state-management-in-scripted-modules/10417

---

## Post #1 by @James_Hoctor (2020-02-24 21:27 UTC)

<p>I need design guidance for choosing where to keep canonical UI state in a scripted Slicer module. The module in question is <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PickAndPaint" rel="nofollow noopener">PickAndPaint</a>. The complicated design of the data structures in this module seems to be the root cause of many bugs.</p>
<p>Like other modules, PickAndPaint registers callbacks with various UI widgets in order to be notified of changes. I think that ideally these callbacks would update a vtkMRMLNode representing (fairly literally) the UI state, and then launch any required computation. This would allow UI state to be reinitialized from a scene file. For simplicity and correctness, code would prefer to rederive values from this representation of the UI state, instead of keeping additional state in the logic module, with exceptions only where absolutely necessary for performance reasons.</p>
<p>This solution would also allow QT functions that query the UI state to be completely avoided. Is avoiding these desirable? Or can I safely use the QT widget itself in place of a vtkMRMLNode in what I described above? If it is safe, couldn’t UI persistence (such as model selection persistence) be implemented in Slicer for all scripted modules by serializing any UI state referenced in the .ui file into XML and stuffing it into a Node? I can explain why I think querying state with QT might not be safe if anyone wants to know, but I’m really ignorant of QT.</p>
<p>It seems that a vtkMRMLNode like what I describe is <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/MRML#Creating_Custom_MRML_Node_Classes" rel="nofollow noopener">recommended</a> for modules written in C++. See also <a href="https://github.com/Kitware/BoneTextureExtension/blob/master/BoneTexture/BoneTexture.py#L79" rel="nofollow noopener">this cryptic code comment</a> which seems to recommend something similar for scripted modules.</p>

---

## Post #2 by @pieper (2020-02-24 21:54 UTC)

<p>There’s room for developers to have some flexibility here, and different tasks may require more or less complexity to address performance issues, but at least for some cases I have had good luck with just saving a json representation of the state as an attribute of a scripted module node.  This will automatically be saved/restored with the scene, and it’s pretty low overhead to parse to populate the GUI and to serialize when the user interacts with the GUI.</p>
<p>An example is implemented in the <a href="https://github.com/pieper/SlicerAnimator">SlicerAnimator</a> project which has a reasonably sophisticated GUI.</p>
<p>We discourage people from using the GUI to store the state, since we want it to be possible for more than one user interface element to display and edit the same state (e.g. a markup that is active in 2D, 3D, and GUI displays that all hot update).</p>

---

## Post #3 by @lassoan (2020-02-25 05:13 UTC)

<p>When PickAndPaint module was developed, Python scripted module development was still quite immature. Nowadays I would recommend to create the module using Qt Designer and use updateParameterNodeFromGUI/updateGUIFromParameterNode methods to synchronize parameter node content with GUI. See <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedDesigner/TemplateKey.py">ScriptedDesigner module template</a> as an example and <a href="https://discourse.slicer.org/t/how-to-save-slicer-scene-with-both-slicer-data-and-with-self-variables-within-custom-widget/9830/11">this discussion</a> for some more details.</p>
<p>Also note that the new markups widgets offer possibilities that were not feasible before. For example, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> just implemented drawing of open and closed curves on surfaces (will be announced tomorrow) and you can use these surfaces for defining surface regions. It would be also feasible now to implement constraining of markup points to a selected surface in Slicer core (and in 3D views, markups snap to visible surfaces already).</p>
<p>There are a few other small issues, such as:</p>
<ul>
<li>Node ID must never be stored in a node attribute, because node IDs can be changed when a scene is loaded and the existing scene contains nodes by the same IDs. Always use node references instead.</li>
<li>Logic should never use and GUI functions (currently the logic may display popup windows)</li>
<li>Logging macros should be used instead of <code>print</code>
</li>
</ul>

---
