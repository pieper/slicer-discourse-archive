# Interaction Mode

**Topic ID**: 1602
**Date**: 2017-12-06
**URL**: https://discourse.slicer.org/t/interaction-mode/1602

---

## Post #1 by @lcoram (2017-12-06 09:04 UTC)

<p>Hi Slicer developers,</p>
<p>When communicating an interaction state/mode within a module (or potentially between modules in an extension) it feels like the best way to do this would be use the vtkMRMLInteractionNodeSingleton. However, this currently only allows for the predefined states (place, viewTransform, &amp; select) - as the function SetCurrentInteractionMode is limited to switch between these enums.</p>
<p>Is there a suggested “best practice” for this, if we need different states? Would it ever make sense to have the vtkMRMLInteractionNode class be more flexible so that states can be added?</p>
<p>Currently I am thinking I will encode the state inside a MRML node particular to the module (which is handling some stuff related to the interaction mode). Another option might be to create a child class of the interaction node to extend the modes?</p>
<p>Thanks for your help,</p>
<p>Louise</p>

---

## Post #2 by @lassoan (2017-12-06 17:28 UTC)

<p>Modules that needs custom interaction (such as Segment editor) often just set interaction mode to default (ViewTransform) and capture events directly from window interactors. This is OK for cases when you only need to capture mouse events temporarily.</p>
<p>If you want to show a “tool” in the mouse mode list in the toolbar, then you need to register your own mouse mode (with a corresponding name and icon) - see <a href="http://apidocs.slicer.org/master/classvtkMRMLSelectionNode.html#a6296d84bf723e805eb0ccb85639904dc">AddNewPlaceNodeClassNameToList</a>. Then in your custom displayable manager, you would <a href="https://github.com/Slicer/Slicer/blob/bcfe8d37b88451f8765cd65d523b6991ad0a33ba/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationDisplayableManager.cxx#L1974">check for the current place node class name</a>, and if it is yours then you process the event, otherwise you ignore it.</p>

---
