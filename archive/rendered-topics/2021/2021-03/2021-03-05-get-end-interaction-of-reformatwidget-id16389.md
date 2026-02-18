# Get end interaction of reformatWidget

**Topic ID**: 16389
**Date**: 2021-03-05
**URL**: https://discourse.slicer.org/t/get-end-interaction-of-reformatwidget/16389

---

## Post #1 by @riep (2021-03-05 08:51 UTC)

<p>Dear everyone,</p>
<p>I am trying to observe the end interaction event of the reformat widget.<br>
To do that I have tried to observe the Interaction node of the vtkMRMLThreeDReformatDisplayableManager using slicer.vtkMRMLInteractionNode.EndPlacementEvent.<br>
Unfortunately, I was not able to get signals.</p>
<p>Is it the right way to do this? Any advice would be great!</p>
<p>Cheers,<br>
Pierre</p>

---

## Post #2 by @lassoan (2021-03-09 14:57 UTC)

<p>I don’t think this widget event is exposed in MRML now. You could probably inspect the VTK renderer and find the widget and add an observer to the event, but it would not be very clean and within about a year the whole widget will be replaced with a more sophisticated one (developed specifically for image slices, with thickness adjustment, right-click menu, etc.).</p>
<p>What would you like to achieve? Maybe there are other events in the MRML scene that you could observe.</p>

---

## Post #3 by @riep (2021-03-10 11:42 UTC)

<p>Thank you for the details.<br>
I have implemented a workaround using qt.timer that is working.</p>
<blockquote></blockquote>
<pre><code>sliceNode.AddObserver(vtk.vtkCommand.ModifiedEvent, self.reformatObserverFunction)
</code></pre>
<blockquote></blockquote>
<pre><code>def reformatObserverFunction(self, sliceNodeCaller, event):
"""
Start/reset a 500ms timer each time we receive user MultiplanarReformatFlag. ParameterNode update is triggered at trigger timeout
"""    
if sliceNodeCaller.GetInteractionFlags() == sliceNodeCaller.MultiplanarReformatFlag: # Pass signals coming from the reformatWidget
  print("reformatObserverFunction")
  if self.reformatWidgetTimer:
    # If a time was already on, stop it
    self.reformatWidgetTimer.stop()
    self.reformatWidgetTimer.deleteLater()

  self.reformatWidgetTimer = qt.QTimer()
  self.reformatWidgetTimer.setSingleShot(True)
  self.reformatWidgetTimer.start(500)
  self.reformatWidgetTimer.timeout.connect(self.yourfunction)
</code></pre>
<p>Could you give us some details about the new reformat widget? Is it a module for now?</p>

---

## Post #4 by @cpinter (2021-03-10 12:11 UTC)

<p>Would the <code>EndSliceNodeInteraction</code> event work? See here <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLThreeDReformatDisplayableManager.cxx#L456" class="inline-onebox">Slicer/vtkMRMLThreeDReformatDisplayableManager.cxx at master · Slicer/Slicer · GitHub</a></p>
<p>Although the workaround may work, I strongly suggest not relying on such mechanics for handling events. QTimer should only be used as a last resort. As a comment about the implementation of the workaround, I’d suggest not deleting and re-creating the timer, there is no apparent reason to do so, and <code>deleteLater</code> is not a reliable way to delete an object in Qt, so should not be relied on either.</p>

---

## Post #5 by @riep (2021-03-10 13:07 UTC)

<p>Hi Csaba,<br>
Well, we saw that lines in the DisplayableManager/vtkMRMLThreeDReformatDisplayableManager.cxx . But, if I understand the code correctly EndSliceNodeInteraction does not trigger an event.<br>
Pierre</p>

---

## Post #6 by @cpinter (2021-03-10 13:15 UTC)

<p>Hm that’s right, it’s not an event, my bad. An event like is what would be helpful in your case.</p>

---

## Post #7 by @riep (2021-03-10 13:22 UTC)

<p>Do you know where I can find the new reformat widget, just to play around with it.</p>

---

## Post #8 by @cpinter (2021-03-10 13:30 UTC)

<p>Based on <a class="mention" href="/u/lassoan">@lassoan</a>’s comment</p>
<blockquote>
<p>within about a year the whole widget will be replaced with a more sophisticated one</p>
</blockquote>
<p>the widget will be available in the future.</p>

---

## Post #9 by @riep (2021-03-10 13:35 UTC)

<p>ok thanks so there is nothing published yet.</p>

---
