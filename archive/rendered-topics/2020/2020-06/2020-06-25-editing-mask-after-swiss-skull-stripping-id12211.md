# Editing mask after Swiss Skull Stripping

**Topic ID**: 12211
**Date**: 2020-06-25
**URL**: https://discourse.slicer.org/t/editing-mask-after-swiss-skull-stripping/12211

---

## Post #1 by @AT3432984 (2020-06-25 00:40 UTC)

<p>Hi, I have used the Swiss Skull Stripper module to create a mask of a brain from an MRI. However, the mask that was generated includes some of the eye. Is there a way I can remove this from my mask? I have tried using the segment editor but it says there are no segments, so I can’t erase anything.</p>

---

## Post #2 by @lassoan (2020-06-25 00:49 UTC)

<p>To allow editing of a labelmap volume in Segment Editor module, you first need to convert it to a segmentation. You can do that by right-clicking on it in Data module and choosing “Convert labelmap to segmentation node”.</p>
<p>You can use “Mask volume” effect in Segment Editor to apply the modified mask to the MRI image. “Mask volume” effect is available after you install “SegmentEditorExtraEffects” extension.</p>

---

## Post #3 by @AT3432984 (2020-06-26 05:18 UTC)

<p>Hi,</p>
<p>I have converted the mask to a labelmap and edited it. I wanted to save the binary mask to use Pyradiomics. I did this by right clicking the patient mask label in the ‘data’ module, and selecting ‘export visible segments to binary map’. However, when I try to run this with Pyradiomics, it does not work (it works when I run it with the original mask created using swiss skull stripper, but does not run with the edited mask). Is there another way I am supposed to save this new mask?</p>

---

## Post #4 by @lassoan (2020-06-26 13:07 UTC)

<p>Could you try to use the export/import section in Segmentations module and choose the original mask as reference volume? If it still fails then please tell us what error pyradiomics reported.</p>

---

## Post #5 by @AT3432984 (2020-06-26 23:10 UTC)

<p>I ended up clicking the 2 boxes on the right hand side of ‘master volume’ in the segment editor. I think the geometries were slightly different. It all works now. Thanks for all your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
