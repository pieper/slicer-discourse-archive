---
topic_id: 202
title: "Callback For Breach Warning"
date: 2017-04-27
url: https://discourse.slicer.org/t/202
---

# Callback for breach warning

**Topic ID**: 202
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/callback-for-breach-warning/202

---

## Post #1 by @banderies (2017-04-27 00:20 UTC)

<p>Hello all,</p>
<p>I am trying to get my scripted extension to send a message to my Arduino when the breach warning (in SlicerIGT) is activated. However, I can’t figure out what to attach a callback to. For example, the “vtkSlicerOpenIGTLinkCommand” objects have a “CommandCompletedEvent,” which allows a callback to read the response message. Is there something equivalent for the breach warning objects? I have referenced the LumpNav extension, as it does something similar to what I want to do, but I don’t want to use vtk.vtkCommand.ModifiedEvent, which appears to be activated whenever the tool moves, not when the tool breaches the model. If breach warning does not have an equivalent to the “CommandCompletedEvent” in “vtkSlicerOpenIGTLinkCommand,” is there a simple way that I can have Slicer send my Arduino a message when the breach warning is activated (i.e. my tool breaches the model)?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-04-27 01:57 UTC)

<p>Observe the vtk.vtkCommand.ModifiedEvent event. In the callback method check the state of the node (IsToolTipInsideModel,  GetClosestDistanceToModelFromToolTip) and act accordingly.</p>
<p>If you need to monitor cutting into one of multiple objects then you can get a pointer to the caller breach warning node as described here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function</a></p>

---
