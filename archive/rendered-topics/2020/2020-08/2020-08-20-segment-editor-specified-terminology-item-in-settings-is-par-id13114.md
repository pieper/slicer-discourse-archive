---
topic_id: 13114
title: "Segment Editor Specified Terminology Item In Settings Is Par"
date: 2020-08-20
url: https://discourse.slicer.org/t/13114
---

# Segment editor : specified terminology item in settings is partially taken into account

**Topic ID**: 13114
**Date**: 2020-08-20
**URL**: https://discourse.slicer.org/t/segment-editor-specified-terminology-item-in-settings-is-partially-taken-into-account/13114

---

## Post #1 by @chir.set (2020-08-20 14:41 UTC)

<p>‘Application settings / Segmentations’ section allows to define a default terminology entry when we add the first segment in ‘Segment editor’ module, or ‘Segmentations’ module. I select ‘Tissue/Artery’ there.</p>
<p>After restarting Slicer and adding a first segment in ‘Segment editor’, the tooltip does show ‘Tissue/Artery’, but the segment color remains green, that of ‘Tissue/Tissue’, whilst it should be red.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62370eec9c32afe465ed35b745c83f9815be9603.png" alt="bad_color" data-base62-sha1="e0QKKexqBdA3xpWrXZOniv1NHDZ" width="684" height="164"></p>
<p>Complicating matters, manually selecting ‘Tissue/Artery’ again does not change the color. Another terminology item must be selected, and lastly, selecting ‘Tissue/Artery’ would set the right color.</p>
<p>A fix would be welcome, nothing urgent of course.</p>

---

## Post #2 by @lassoan (2020-08-23 15:05 UTC)

<p>Colors for new segments don’t use the default term’s color because then all the segments would have the same color.</p>
<blockquote>
<p>Manually selecting ‘Tissue/Artery’ again does not change the color</p>
</blockquote>
<p>It does, but to actually select it, you need to select another term (clicking on the already selected item in a list has no effect). To make this easier, I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/0e190aa347242e47bd56a55c8f3b99edaebd17e5">fix</a>, so that you can easily reset to the default color by clicking the “Reset color to default” button.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd7b2ce8768137e129ade4b8d6f371316545c10.png" data-download-href="/uploads/short-url/jX6v0Qq880XEVC9UpM4fcxMCoPC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bd7b2ce8768137e129ade4b8d6f371316545c10_2_453x500.png" alt="image" data-base62-sha1="jX6v0Qq880XEVC9UpM4fcxMCoPC" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bd7b2ce8768137e129ade4b8d6f371316545c10_2_453x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd7b2ce8768137e129ade4b8d6f371316545c10.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd7b2ce8768137e129ade4b8d6f371316545c10.png 2x" data-dominant-color="484F55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">669×738 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @chir.set (2020-08-23 15:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>because then all the segments would have the same color.</p>
</blockquote>
</aside>
<p>Makes sense. However, the very first created segment only could use the default terminology specified in settings. Else, what would be the purpose of a default terminology ?</p>
<p>Anyway, it’s not a big issue. It’s just to avoid double-clicking the first segment every time, to select the preferred terminology item which is always the same in my case. Most users have probably broader workflows. Don’t waste more time on this.</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2020-08-23 15:55 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="13114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Else, what would be the purpose of a default terminology ?</p>
</blockquote>
</aside>
<p>The main use is setting the segmentation category. This allows you to create a custom list of terms that are relevant for your particular segmentation task. The default term should be something generic, to be safe (if you set it to be something too specific, then it may be assumed that the user specifically selected that term because he determined that the segment corresponds to that term).</p>
<p>If we used the term’s default color for the first segment then it would add lots of extra complications (e.g., when we add a second segment then we would need to check if the color is that is not too similar to the first one). Also, I don’t see a workflow where setting the first segment’s color based on the default color would make things significantly better: if you segment vessels then you don’t want all your vessels to be red; if you segment various structures then you don’t want your default term to be a vessel.</p>
<p>Default segment colors are now generated in <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationDisplayNode.cxx#L897">vtkMRMLSegmentationDisplayNode::GenerateSegmentColor</a> by taking them from <code>GenericAnatomyColors</code> color table. We could add an option to set a custom color table node as input, if setting specific default colors turns out to be important for some use cases.</p>

---
