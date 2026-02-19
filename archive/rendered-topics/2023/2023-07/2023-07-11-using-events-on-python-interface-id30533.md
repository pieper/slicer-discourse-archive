---
topic_id: 30533
title: "Using Events On Python Interface"
date: 2023-07-11
url: https://discourse.slicer.org/t/30533
---

# Using Events on Python interface

**Topic ID**: 30533
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/using-events-on-python-interface/30533

---

## Post #1 by @Patrick_Li (2023-07-11 20:46 UTC)

<p>Hello all.<br>
I’m trying to work with observer events. Mainly, I want to invoke a function when you click on a curve markup node. I looked in the reposity and found</p>
<pre><code class="lang-auto">pointListNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, UpdateSphere, 2)
</code></pre>
<p>I edited it a little to make it work for my program, but I ran into an issue similar to the one in my last post.</p>
<pre><code class="lang-auto">AttributeError: type object 'vtkSlicerMarkupsModuleMRML.vtkMRMLMarkupsNode' has no attribute 'PointClickedEvent'
</code></pre>
<p>If I can’t use these events on the Python interface, is there any alternative way to achieve my end goal?</p>

---

## Post #2 by @lassoan (2023-07-12 04:01 UTC)

<p>Correct, there is no such event as <code>PointClickedEvent</code>. The reason is that clicking on a point is an interaction event that can be translated to various widget events. By default <a href="https://github.com/Slicer/Slicer/blob/0e2cec5168d1e670d80edc5a086b329dc0c2b064/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L100">left-click is translated to <code>WidgetEvenJumpCursor</code></a>.</p>
<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#make-the-3d-view-rotate-using-right-click-and-drag">remove this default translation</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#assign-custom-actions-to-markups">add your own translation to a markupsWidget.WidgetEventCustomAction1 event, which you can observe</a>.</p>

---

## Post #3 by @Patrick_Li (2023-07-12 14:37 UTC)

<p>Thanks for the advice! I’m now trying to get this to work with my custom module. I don’t think I’ve interpreted the examples correctly, as I’m getting an error. I put the following code in my custom module’s .py file.</p>
<pre><code class="lang-auto"># Remove old mapping
self.SetEventTranslation(vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier)
# Make left click highlight the curve in the curve list
self.SetKeyboardEventTranslation(self.WidgetStateOnWidget, vtk.vtkEvent.NoMidifier,
                                 '\0', 0, vtk.vtkCommand.LeftButtonPressEvent,
                                 self.WidgetEventCustomAction1)
# Add observer to custom action
markupsNode.AddObserver(markupsNode.ActionEvent, self.customFunction)
</code></pre>
<p>I get this error.</p>
<pre><code class="lang-auto">AttributeError: 'MyFirstModuleWidget' object has no attribute 'SetKeyboardEventTranslation'
</code></pre>
<p>When I comment out the first line, I get the same error for .SetKeyboardEventTranslation()</p>

---

## Post #4 by @lassoan (2023-07-13 00:57 UTC)

<p>Instead of <code>self.</code> you need to use a <code>markupsWidget</code>. You can find example in the script repository for how to get the markups widget for a markups node.</p>

---

## Post #5 by @Patrick_Li (2023-07-13 18:21 UTC)

<p>Thanks for the help! My program is now running without any crashes, but it still doesn’t seem to work as nothing happens when I click. Here’s what I used.</p>
<pre><code class="lang-auto">  # Create new curve and place it in the nodule folder
  markupsNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsClosedCurveNode')
  
  # Remove old mapping
  threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
  markupsDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName(
    'vtkMRMLMarkupsDisplayableManager')
  displayNode = markupsNode.GetMarkupsDisplayNode()
  markupsWidget = markupsDisplayableManager.GetWidget(displayNode)
  markupsWidget.SetEventTranslation(markupsWidget.WidgetStateIdle, vtk.vtkCommand.LeftButtonPressEvent,
                                  vtk.vtkEvent.NoModifier)
  # Make left click highlight the curve in the curve list
  markupsWidget.SetKeyboardEventTranslation(markupsWidget.WidgetStateOnWidget, vtk.vtkEvent.NoModifier,
                                            '\0', 0, "LeftButtonPressEvent",
                                            markupsWidget.WidgetEventCustomAction1)
  # Add observer to custom action
  displayNode.AddObserver(displayNode.CustomActionEvent1, self.onSelectContour)
</code></pre>

---

## Post #6 by @lassoan (2023-07-25 12:32 UTC)

<p>Your need to first remove the existing translation and then set the new translation. Also, do not mix keyboard and mouse events. Follow closely the examples in the script repository as they allow how to do this right.</p>

---
