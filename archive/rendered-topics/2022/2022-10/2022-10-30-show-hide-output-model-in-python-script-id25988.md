# Show/hide output model in Python script

**Topic ID**: 25988
**Date**: 2022-10-30
**URL**: https://discourse.slicer.org/t/show-hide-output-model-in-python-script/25988

---

## Post #1 by @seanchoi0519 (2022-10-30 13:56 UTC)

<p>Hi,</p>
<p>I’m trying to implement a function where the user is able to show and hide the output model compared to the input model. For example, when a user presses 1, the input model (before the effect of the dynamicModel) shows. When a user presses 2, the input model gets cut by the planes, and the output node is then shown.</p>
<p>What would be the easiest way to do this?<br>
I’ve not dealt with vtkMRMLDynamicModelNode so this is quite new to me. My initial thought was to use SetVisibility function to show/hide the DisplayNode but then dynamic model node does not seem to have a displaynode</p>

---

## Post #2 by @lassoan (2022-10-31 19:32 UTC)

<p>Dynamic modeler nodes specify the operation type and all inputs, and outputs. You thought it correctly that you need to call <code>SetVisibility</code> of model display nodes. You can get the display nodes by calling <code>GetDisplayNode()</code> method of the input and output model nodes referenced in the dynamic modeler node.</p>

---
