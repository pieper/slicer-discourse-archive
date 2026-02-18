# Breach Warning ScriptRepository

**Topic ID**: 16767
**Date**: 2021-03-25
**URL**: https://discourse.slicer.org/t/breach-warning-scriptrepository/16767

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-03-25 19:37 UTC)

<p>Hi,</p>
<p>I am trying to use Breach Warning function from IGT extension in our project which seems to be very useful. Are there any resources / Python scripting for developer regarding this Breach Warning Module ? I am using Slicer 4.11.0</p>
<p>Thank you !!</p>

---

## Post #2 by @Raj_Kumar_Ranabhat (2021-03-29 15:31 UTC)

<p>Is there any short script for parameter set, inputs, and parameters selection. It would be a great help for us.</p>
<p>thank you !!</p>

---

## Post #3 by @Raj_Kumar_Ranabhat (2021-03-31 17:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/cpinter">@cpinter</a> : I hope you can help me out with this topic.</p>

---

## Post #4 by @lassoan (2021-04-03 01:54 UTC)

<p>The simplest is to set up the breach warning using the GUI and save the scene. If you reload the scene then everything will work the same way when you saved the scene.</p>
<p>If you want to set up things from scratch in Python then all you need to do is to create add a <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/MRML/vtkMRMLBreachWarningNode.h">vtkMRMLBreachWarningNode</a> to the scene and set its inputs and outputs. You can find a few convenience functions for these in the <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/Logic/vtkSlicerBreachWarningLogic.h">BreachWarning module logic</a>.</p>

---
