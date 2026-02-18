# Slicer app crashing when SegmentEditor Islands effect is run on an empty segment

**Topic ID**: 10348
**Date**: 2020-02-19
**URL**: https://discourse.slicer.org/t/slicer-app-crashing-when-segmenteditor-islands-effect-is-run-on-an-empty-segment/10348

---

## Post #1 by @ezgimercan (2020-02-19 02:53 UTC)

<p>Slicer Preview version 4.11.0-2020-02-17, on both Windows 10 and Mac OS X. All extensions disabled.<br>
When I download sample data, MRHead, create a segmentation, add a segment, and run Islands tool with any of the enabled options, Slicer crashes. The expected behavior is that nothing happens.</p>
<p>It doesn’t happen with the version 4.11.0-2019-08-30.</p>
<p>The log doesn’t have any errors, the last entry is:<br>
[INFO][Python] 18.02.2020 18:50:46 [Python] (C:\Users\ezgim\Documents\Slicer 4.11.0-2020-02-17\lib\Slicer-4.11\qt-scripted-modules\SegmentEditorEffects\SegmentEditorIslandsEffect.py:155) - 0 islands created (0 ignored)</p>

---

## Post #2 by @lassoan (2020-02-19 02:58 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you have a look at this?</p>

---

## Post #3 by @Sunderlandkyl (2020-02-19 18:20 UTC)

<p>This should be fixed in the preview version tomorrow.</p>

---

## Post #4 by @Demi_Trimino (2020-05-08 16:47 UTC)

<p>This was happening to me. I had to downsample my data and then it worked afterwards.</p>

---

## Post #5 by @Sunderlandkyl (2020-05-08 17:13 UTC)

<p><a class="mention" href="/u/demi_trimino">@Demi_Trimino</a> What version of Slicer were you using, and how large was your volume?</p>

---

## Post #6 by @Demi_Trimino (2020-05-08 17:33 UTC)

<p>4.11.0-2020-03-15 and I’m not sure how large the volume was. My computer will only tell me the size of each individual stack, not the entire folder size</p>

---

## Post #7 by @Sunderlandkyl (2020-05-08 17:52 UTC)

<p>Sorry, I meant to ask what the dimensions of the volume are?</p>

---

## Post #8 by @Demi_Trimino (2020-05-08 18:05 UTC)

<p>0.0026921mm for all dimensions</p>

---

## Post #9 by @Sunderlandkyl (2020-05-08 18:07 UTC)

<p>How many voxels are there in each axis? Ex 512x512x256.</p>

---
