# Referencing a module widget from another module

**Topic ID**: 7419
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/referencing-a-module-widget-from-another-module/7419

---

## Post #1 by @MattTroke (2019-07-04 17:52 UTC)

<p>I have 2 extensions, both built into a custom build of slicer. I have set it up so that ExtensionA (with ModuleABC) depends on ExtensionB (with Module XYZ). I would like to be able to get a handle on ExtensionBModuleXYZModuleWidget from ExtensionAModuleABCModuleWidget (for example to determine the value of a dropdown in the other widget). Is this possible to do in Slicer?</p>
<p>Thanks,<br>
Matt</p>

---

## Post #2 by @lassoan (2019-07-04 18:11 UTC)

<p>A module should never ever access the widget of another module. Always communicate through MRML nodes.</p>
<p>If a module is implemented correctly then GUI changes are immediately reflected in changes in the associated parameter node. Other modules can observe changes in nodes and perform any actions as needed. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">PerkLab Slicer programming tutorials</a> for more details and explanations.</p>

---

## Post #3 by @MattTroke (2019-07-04 18:17 UTC)

<p>Fair enough. My specific issue is with the Sequences extension. I want to know which is the active sequence browser selected in the Sequence Browser module. From what I can tell, there is no property of vtkMRMLSequenceBrowserNode that will communicate this.</p>

---

## Post #4 by @lassoan (2019-07-04 19:43 UTC)

<p>You are not supposed to use the selection in the Sequence Browser module (selection can change when new sequence is loaded or the user modifies the selection for any reason, etc).</p>
<p>If you expect to have only a single sequence browser in the scene then you can get it from the MRML scene using <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLScene.html#a21560f853d73548021e75d991d5aa34d" rel="nofollow noopener">GetFirstNodeByClass()</a>.</p>
<p>If you have multiple sequence browser nodes then you can add a node selector widget in your module GUI. You can make the chosen sequence browser node selected in the toolbar using <a href="https://github.com/SlicerRt/Sequences/blob/master/SequenceBrowser/qSlicerSequenceBrowserModule.h#L79" rel="nofollow noopener"><code>showSequenceBrowser</code> method</a>.</p>
<p>If you want to mirror browser node selection of the toolbar then you can retrieve the toolbar from the sequence browser module and add a connection to its <a href="https://github.com/SlicerRt/Sequences/blob/master/SequenceBrowser/Widgets/qMRMLSequenceBrowserToolBar.h#L60" rel="nofollow noopener">activeBrowserNodeChanged signal</a>.</p>
<p>If all these still cannot satisfy your use case then we would need to learn a bit more about what would you like to do and how. We could add an accessor to the currently selected browser node in the toolbar or maybe save the currently selected browser node on the toolbar to the singleton Selection node.</p>

---
