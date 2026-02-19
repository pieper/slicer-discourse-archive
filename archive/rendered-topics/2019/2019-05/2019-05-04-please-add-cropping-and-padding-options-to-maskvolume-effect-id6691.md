---
topic_id: 6691
title: "Please Add Cropping And Padding Options To Maskvolume Effect"
date: 2019-05-04
url: https://discourse.slicer.org/t/6691
---

# Please add cropping and padding options to maskVolume effect in ExtraEffect tools

**Topic ID**: 6691
**Date**: 2019-05-04
**URL**: https://discourse.slicer.org/t/please-add-cropping-and-padding-options-to-maskvolume-effect-in-extraeffect-tools/6691

---

## Post #1 by @muratmaga (2019-05-04 04:47 UTC)

<p>It is common in our field to stuff whole bunch of genetically samples into the same scan to cut down the scanning costs/time (eg 10-15 zebrafish from the same clutch).</p>
<p>We are training our folks to use Slicer to do a quick segmentation to mask and save these specimen as individual datasets for further analysis.</p>
<p>Grow from the seeds and masking works really well in this context. What is missing is an option to cut down the original volume size to the largest extends of the mask and add an option to pad the cropped image. Of course this can be done with already existing tools in Slicer, but from a workflow point of view this might be a useful addition to the existing maskVolume functionality in the SegmentEditorExtraEffects extension.</p>

---

## Post #2 by @lassoan (2019-05-07 23:28 UTC)

<p>I see how such a Segment Editor effect could be useful. It is quite a niche use case, so I don’t think I could allocate time to work on it but maybe you could give it a try and implement it. <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorMaskVolume" rel="nofollow noopener">“Mask volume” effect</a> in SegmentEditorExtraEffects extension is quite similar. You just need to modify it to compute the extent from the segment (similarly to how it is done <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/AbstractScriptedSegmentEditorAutoCompleteEffect.py#L373-L391" rel="nofollow noopener">here</a>).</p>

---

## Post #3 by @pieper (2019-05-24 17:38 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> maybe if you provided a sample dataset with scan and segmentations so we could get an idea what it would look like.  It sounds like this could be just a few lines of numpy code.</p>
<p>-Steve</p>

---

## Post #4 by @muratmaga (2019-05-24 20:11 UTC)

<p>I think <a class="mention" href="/u/smrolfe">@smrolfe</a> is close getting ready for a pull request to add this as an CropSegment effective to segementeditorextraeffects i believe.</p>

---

## Post #5 by @lassoan (2019-05-24 22:23 UTC)

<p>Great! If it’s a completely generic tool then SegmentEditorExtraEffects is a good home for it. If this new effect is tailored for needs of morpho community then you may distribute it in SlicerMorpho extension.</p>

---

## Post #6 by @smrolfe (2019-05-25 01:18 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, its a completely generic tool that uses the current segment to mask and crop to the segment extent, with an option to add padding.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> , I’ve uploaded the extension to your repository for testing.</p>

---

## Post #7 by @lassoan (2019-05-25 02:05 UTC)

<p>Sounds like a good fit for SegmentEditorExtraEffects extension then!</p>

---

## Post #8 by @smrolfe (2019-05-25 22:05 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I have just submitted the pull request.</p>

---

## Post #9 by @lassoan (2023-03-21 03:10 UTC)



---
