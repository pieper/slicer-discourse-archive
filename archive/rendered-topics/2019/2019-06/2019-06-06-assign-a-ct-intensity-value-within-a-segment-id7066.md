# Assign a CT intensity value within a segment

**Topic ID**: 7066
**Date**: 2019-06-06
**URL**: https://discourse.slicer.org/t/assign-a-ct-intensity-value-within-a-segment/7066

---

## Post #1 by @kmalexander (2019-06-06 20:59 UTC)

<p>Hi -</p>
<p>I’m looking to assign an intensity value to a CT image for every voxel within a segment, and the voxels outside that segment should stay the same.  I imagine there is a filter for this, but there are so many to choose!  Anyone able to point me in the right direction?</p>
<p>Thanks,<br>
Kevin</p>

---

## Post #2 by @pieper (2019-06-06 21:17 UTC)

<p>Hi -</p>
<p>A direct way to do this is to use numpy.  <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_the_values_of_all_voxels_for_a_label_value" rel="nofollow noopener">This example</a> shows how to get the coordinates of all voxels corresponding to a particular label value and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume" rel="nofollow noopener">this example</a> shows how to modify the values.  You’d just need to export the segmentation as a labelmap to use these.</p>

---

## Post #3 by @cpinter (2019-06-07 17:51 UTC)

<p>Hi Kevin,</p>
<p>The Mask volume effect in Segment Editor is just for this. You’ll need to install the SegmentEditorExtraEffects extension to have that.</p>
<p>I just tested it in 4.10.2, and it does not work.</p>
<details>
<summary>
Summary</summary>
<p>I’m getting this error:</p>
<pre><code>Traceback (most recent call last):
  File "C:/Users/pinter/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py", line 347, in onApply
    self.maskVolumeWithSegment(segmentationNode, segmentID, operationMode, fillValues, inputVolume, outputVolume)
TypeError: maskVolumeWithSegment() takes at least 7 arguments (6 given)
</code></pre>
</details>
<p>There are even more errors in the nightly. <a class="mention" href="/u/lassoan">@lassoan</a> I see that you have worked on this effect, could you look at this? Maybe it’s something trivial.</p>
<p><a class="mention" href="/u/kmalexander">@kmalexander</a> please stand by. Thanks!</p>

---

## Post #4 by @kmalexander (2019-06-07 17:52 UTC)

<p>In an older version, it works well.  Nightly wasn’t working - as you reported.</p>
<p>Thanks for the advice!</p>
<p>Kevin</p>

---

## Post #5 by @lassoan (2019-06-07 18:29 UTC)

<p>Sorry, I broke this yesterday when added a new effect (Split volume). I’ve fixed the issues now, all effects in SegmentEditorExtraEffects work in both Slicer-4.10 and Slicer-4.11 in releases downloaded tomorrow or later.</p>

---

## Post #6 by @kmalexander (2019-06-19 14:53 UTC)

<p>Awesome - thanks, Andras!</p>

---
