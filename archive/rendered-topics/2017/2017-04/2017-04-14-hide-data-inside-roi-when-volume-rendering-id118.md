# Hide data inside ROI when Volume Rendering

**Topic ID**: 118
**Date**: 2017-04-14
**URL**: https://discourse.slicer.org/t/hide-data-inside-roi-when-volume-rendering/118

---

## Post #1 by @Fernando (2017-04-14 15:25 UTC)

<p>Hi slicers,</p>
<p>Is there a way to make the ROI hide the data inside instead of cropping it? Like in this capture of <code>mrview</code>:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f01296bb9b5b3d6df81d54ecbedb0548da8c04ba.png" data-download-href="/uploads/short-url/yfMpZvS3RBR9KzFCKbKUqLVMgEq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01296bb9b5b3d6df81d54ecbedb0548da8c04ba_2_441x500.png" alt="image" data-base62-sha1="yfMpZvS3RBR9KzFCKbKUqLVMgEq" width="441" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01296bb9b5b3d6df81d54ecbedb0548da8c04ba_2_441x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01296bb9b5b3d6df81d54ecbedb0548da8c04ba_2_661x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f01296bb9b5b3d6df81d54ecbedb0548da8c04ba.png 2x" data-dominant-color="343434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×909 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Fernando</p>
<p>P. S.: I’m trying to add the tag “volume rendering”, but I didn’t manage.</p>

---

## Post #2 by @lassoan (2017-04-14 15:57 UTC)

<p>Use the <code>Volume clip with ROI</code> module in <code>Volume Clip</code> extension to remove an arbitrary rectangular section. You can also use <code>Volume clip with model</code> module (in the same extension) to remove an arbitrarily shaped region.</p>

---

## Post #3 by @Fernando (2017-04-14 16:14 UTC)

<p>Hi Andras,</p>
<p>I forgot to say “interactively”, like in the <code>Volume Rendering</code> module.</p>

---

## Post #4 by @lassoan (2017-04-14 18:08 UTC)

<p>If clicking the Apply button is so bad then you can slightly modify the Crop volume with ROI module to apply cropping immediately whenever the ROI is changed.</p>
<p>Instead of immediate update you may allow a few-second delay: (re)start a timer whenever the ROI is changed and re-crop the volume when the timer expires.</p>

---

## Post #5 by @Fernando (2017-04-15 10:53 UTC)

<p>I don’t think clicking the Apply button <em>is so bad</em>. I just think that might not be what the user wants, specially if he’s clipping a very large image just for visualization.</p>
<p>Thanks for your answer. I’ll experiment and try to modify the Volume Rendering volume if I get a result.</p>

---

## Post #6 by @lassoan (2017-04-15 11:32 UTC)

<p>Volume renderer in VTK does not support arbitrary Boolean operators between clipping planes: you can only do rectangular cropping or masking with binary labelmap. Everything else must be done by modifying the input volume.</p>
<p>If VTK’s volume renderer will be able to do such clipping then we can make that available in Slicer till then the simplest is to pre-process the volume. Note that you can still show the original unclipped volume in slice viewers.</p>

---

## Post #7 by @lassoan (2017-04-15 11:35 UTC)

<p>Also note that you can get almost the same result by showing slice views (with thresholding enabled for the volume, to remove black borders) and a skin surface model (slice clipping enabled to be able to see inside the head).</p>
<p>Example (<a href="https://1drv.ms/u/s!Arm_AFxB9yqHr5BI0Hag1rewSdETWg">download the scene from here</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" data-download-href="/uploads/short-url/wVWnFZhfQCwWyiXKAJMVk58R6OO.gif?dl=1" title="ClipIntoBrainS.gif"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e6d24c90190c1e4315521adc7bae274d303e861e_2_555x500.gif" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e6d24c90190c1e4315521adc7bae274d303e861e_2_555x500.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6d24c90190c1e4315521adc7bae274d303e861e.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6d24c90190c1e4315521adc7bae274d303e861e.gif 2x" data-dominant-color="4A484E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ClipIntoBrainS.gif</span><span class="informations">718×646 701 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @SteveRobbins (2022-09-16 06:19 UTC)

<p>I tried the Volume clip with ROI.  I can’t get it to do anything.  I watched the video but it was all about the other Volume Clip module.  Is there a basic step-by-step for the Volume Clip with ROI somewhere?</p>

---

## Post #9 by @SteveRobbins (2022-09-16 14:32 UTC)

<p>I figured it out – see <a href="https://discourse.slicer.org/t/volume-rendering-with-cut-planes/25290/3" class="inline-onebox">Volume Rendering with cut planes - #3 by SteveRobbins</a></p>

---
