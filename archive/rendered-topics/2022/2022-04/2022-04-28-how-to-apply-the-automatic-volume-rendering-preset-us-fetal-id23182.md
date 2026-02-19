---
topic_id: 23182
title: "How To Apply The Automatic Volume Rendering Preset Us Fetal"
date: 2022-04-28
url: https://discourse.slicer.org/t/23182
---

# How to apply the automatic volume rendering preset "US-Fetal" on 3D visualizations after segmentation?

**Topic ID**: 23182
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/how-to-apply-the-automatic-volume-rendering-preset-us-fetal-on-3d-visualizations-after-segmentation/23182

---

## Post #1 by @Martin_E (2022-04-28 16:47 UTC)

<p>Hi everyone,</p>
<p>I hope my question hasn’t already been asked but I haven’t found a solution.</p>
<p>I’m currently working on µCT-scans and I’m using the 3D visualization to make illustrations from screenshots. Sometimes there are parasitic elements that I would like to remove, as it is the case on the picture I am attaching where I would like to remove the elements on the top right (they partially obscure the skull in dorsal view). I know that I could easily remove them by making a segmentation, with the scissors tool for example. But when I do that I lose the original coloration of my skull and I can’t find it again, which is a problem for the aesthetics of the illustrations I want to make. From what I understand, the coloration of my 3D object is determined by an automatic volume rendering preset called “US-Fetal”, I like this one and I already used it for many illustrations so I would like to keep it.</p>
<p>My question is: how can I apply this automatic coloring/preset to my segments after removing the artifacts?</p>
<p>Or how to remove the unwanted objects directly without going through segmentation?</p>
<p>Thank you very much for your help, as you can see I am a beginner with 3D Slicer.</p>
<p>Have a nice day,</p>
<p>Martin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a299a5e7f6aa5b43f763e224f1475bfd6512a0f7.jpeg" data-download-href="/uploads/short-url/ncqxsyiW9iJaZHGzhd9cPfvLWzZ.jpeg?dl=1" title="Image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a299a5e7f6aa5b43f763e224f1475bfd6512a0f7_2_690x388.jpeg" alt="Image" data-base62-sha1="ncqxsyiW9iJaZHGzhd9cPfvLWzZ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a299a5e7f6aa5b43f763e224f1475bfd6512a0f7_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a299a5e7f6aa5b43f763e224f1475bfd6512a0f7_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a299a5e7f6aa5b43f763e224f1475bfd6512a0f7.jpeg 2x" data-dominant-color="AFAAC4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image</span><span class="informations">1280×720 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-04-28 20:49 UTC)

<p>Hi - you can use the MaskVolume effect as <a href="https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699">described here</a> to make a copy of the volume data with the segmented portions blanked out.  Then you used the masked version in the volume rendering.</p>

---

## Post #3 by @Martin_E (2022-04-28 21:01 UTC)

<p>Hi, thank you so much for your answer! I’ll try it, it seems to be exactly what I’m looking for.</p>

---
