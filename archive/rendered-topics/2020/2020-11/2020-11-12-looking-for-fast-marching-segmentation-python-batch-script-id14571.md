---
topic_id: 14571
title: "Looking For Fast Marching Segmentation Python Batch Script"
date: 2020-11-12
url: https://discourse.slicer.org/t/14571
---

# Looking for Fast Marching segmentation Python Batch Script

**Topic ID**: 14571
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/looking-for-fast-marching-segmentation-python-batch-script/14571

---

## Post #1 by @epearlstone (2020-11-12 17:59 UTC)

<p>Hello,<br>
I work for DICOM Director, a company that uses slicer modules such as Grow From Seed and Thresholding in our own platform, outside of the Slicer UI. Currently I am looking to integrate the Fast Marching segmentation method into our system. I have the Fast Marching python code, <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorFastMarching" rel="noopener nofollow ugc">here</a>, that works within the 3D Slicer UI, but I am looking for a script of this module that we can use on our own.</p>
<p>Does anyone know how to apply this existing code through python, in order to evoke the method externally (Python or Batch script)? As I said, we know how to call Grow From Seed from external sources, but are looking to do the same with Fast Marching.</p>
<p>Looking at the UI code available does anyone know where it is catching the inputs from the user? For example, we know that the Grow From Seed method accepts seeds as an array of coordinates.</p>
<p>I have already checked <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="noopener nofollow ugc">here</a> but I do not think this is what I am looking for.</p>
<p>Any information or a direction to look in would be a huge help.</p>
<p>Thank you in advance!<br>
-Ethan</p>

---

## Post #2 by @lassoan (2020-11-12 19:33 UTC)

<p>It’s great that you find Slicer useful in your product.</p>
<p>Fast marching can be used the same way as Thresholding and Grow from seeds. You generate preview by calling <code>onMarch</code>, you can then adjust the volume, and when you like the result, write it to the segment by calling <code>onApply</code>.</p>
<p>Note that Fast marching method is not that great, because it is prone to leaking and you cannot do easily fix the leak (you need to adjust your segment and/or lower the volume). Instead, you will find that Local thresholding effect works much robustly. It requires just an intensity range and a single point as input.</p>

---

## Post #3 by @epearlstone (2020-11-16 17:37 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>. Do you know how I might begin to write an external script for this module though? I was told that you can take what you are doing in the interactive tool and run it as the batch scripting, but I am not sure how to get a batch script from this.</p>
<p>Do you mean that my script should include the parts of the code I have linked that define <code>onMarch</code> and <code>onApply</code>? I’m new to script writing so I’m confused about the steps of taking the code that works within Slicer and altering it to work within our own portal. Again, any suggestion or resources would be a huge help.</p>

---

## Post #4 by @epearlstone (2020-11-16 17:44 UTC)

<p>I would also like to do the same thing for the Watershed method, if it is possible. Is <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py" rel="noopener nofollow ugc">this</a> the correct code to start with if I would like to create a script for external use?</p>

---

## Post #5 by @lassoan (2020-11-16 19:25 UTC)

<p>You can look at the source code of a segment editor effect to see its API, but the easiest to get started is to use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">segmentation examples in the script repository</a>. For example, <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b">brain tumor segmentation using grow from seeds effect</a> example shows how to use “Grow from seeds” effect, which has almost the same API as Watershed (probably it is enough to replace the “Grow from seeds” effect name by “Watershed”).</p>

---

## Post #6 by @epearlstone (2020-11-17 15:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You generate preview by calling <code>onMarch</code> , you can then adjust the volume, and when you like the result, write it to the segment by calling <code>onApply</code> .</p>
</blockquote>
</aside>
<p>Thank you again. So do <code>onApply</code> and passing seeds work similar with watershed? Also, do you know if Watershed requires less seeds than Grow from Seeds?</p>

---

## Post #7 by @lassoan (2020-11-17 21:14 UTC)

<aside class="quote no-group" data-username="epearlstone" data-post="6" data-topic="14571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/7ab992/48.png" class="avatar"> epearlstone:</div>
<blockquote>
<p>Also, do you know if Watershed requires less seeds than Grow from Seeds?</p>
</blockquote>
</aside>
<p>The main difference between “grow from seeds” and “watershed” that watershed can enforce a spatial smoothness constrain. In some cases, this might help in getting better segmentation result with smaller or less seeds.</p>

---
