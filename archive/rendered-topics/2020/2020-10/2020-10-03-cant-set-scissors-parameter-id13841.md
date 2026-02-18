# Can't set Scissors parameter

**Topic ID**: 13841
**Date**: 2020-10-03
**URL**: https://discourse.slicer.org/t/cant-set-scissors-parameter/13841

---

## Post #1 by @Amn3s14 (2020-10-03 17:46 UTC)

<p>Hello,</p>
<p>I am trying to access the Scissors effect from Segment Editor in my scripted module. When I run print(slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSegmentEditorNode”)), I see that Scissors.Operation:EraseInside. I would like for the operation to be EraseOutside.</p>
<p>My code is:</p>
<p>segmentEditorWidget.setActiveEffectByName(“Scissors”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“Operation”, “Erase Outside”)</p>
<p>I have also tried “EraseOutside” and 1 (since it’s a radio button), but none of these have changed the value of Operation. I looked at the source code for the scissors effect and I can’t figure out why this isn’t working. Any help would be appreciated. Thanks.</p>

---

## Post #2 by @Amn3s14 (2020-10-04 18:23 UTC)

<p>I didn’t change my code at all but suddenly effect.setParameter(“Operation”, “EraseOutside”) started working.</p>
<p>Another question: I want to trigger an event after the scissor cuts. I have tried adding an observer to the segment like so:<br>
self.observerTag = self.segmentationNode.GetSegmentation().GetSegment(addedSegmentID).AddObserver(‘ModifiedEvent’, self.printStatus)</p>
<p>This seems to trigger when I apply a threshold but not when I cut with the scissors, I think since there isn’t an onApply() method for the Scissors effect. What would be the best way to trigger an event after a cutting occurs?</p>
<p>Thanks for any advice.</p>

---

## Post #3 by @lassoan (2020-10-04 23:29 UTC)

<p>You can add an observer to segment changes. In your callback function you can check if the Scissors effect is active.</p>
<p>Why do you need to trigger an action after Scissors is used?</p>

---

## Post #4 by @Amn3s14 (2020-10-05 01:38 UTC)

<p>I’m trying to develop a streamlined method for determining breast volume from MRI. After scissoring I want to advance the program.</p>
<p>I’m having another issue that is related to the initial topic. I’m trying to use the Margin effect and I can’t seem to get it to Shrink instead of Grow. My code is:</p>
<pre><code>    self.segmentEditorWidget.setActiveEffectByName("Margin")
    effect = self.segmentEditorWidget.activeEffect()
    effect.setParameter('Operation', 'Shrink')
    effect.self().onApply()
</code></pre>
<p>However, the margin grows instead of shrinks. What is unusual is when I print the SegmentEditorNode I see “Margin.Operation:Shrink” yet the margin is clearly growing. Any advice?</p>

---

## Post #5 by @lassoan (2020-10-05 04:25 UTC)

<p>I’ve added documentation for all segment editor effect parameters. See Margin effect parameters here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#margin">https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#margin</a></p>

---

## Post #6 by @Amn3s14 (2020-10-05 17:51 UTC)

<p>I thought I was cheating when I set MarginSizeMm negative but I see now that is the proper way. Thanks!</p>

---
