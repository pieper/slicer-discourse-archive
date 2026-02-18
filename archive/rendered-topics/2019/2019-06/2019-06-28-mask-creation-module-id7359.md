# Mask Creation Module

**Topic ID**: 7359
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/mask-creation-module/7359

---

## Post #1 by @Jainey (2019-06-28 18:20 UTC)

<p>Is it possible to apply a mask to a four D volume using mask creation, please?</p>
<p>I have about 30 volumes of moving bones that I need to mask a few out of them If I apply a mask to the first frame or volume is there a way that it would propagate along the sequence. These are just CT images, not segmented ones.</p>
<p>Thanks</p>
<p>Tom</p>

---

## Post #2 by @lassoan (2019-06-28 22:56 UTC)

<p>Right now you need to do this manually (click Apply on Mask volume effect, then hit the key comvination to go to next frame - I think Ctrl-Alt-RightArrow, and repeat for each frame) or do a very little Python scripting.</p>
<p>I’ve added a module for cropping volume sequences (Crop volume sequence), which does something very similar. You could clone this module and change the <a href="https://github.com/SlicerRt/Sequences/blob/d0635ab179ed4c75e52fa4cb3c64efa2cbcdeee8/CropVolumeSequence/CropVolumeSequence.py#L163" rel="nofollow noopener">run method</a> in the logic to mask the volume instead of cropping it.</p>

---
