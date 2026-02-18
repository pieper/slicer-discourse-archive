# Segment comparison: how to interpret true negatives? Precision and recall

**Topic ID**: 41588
**Date**: 2025-02-09
**URL**: https://discourse.slicer.org/t/segment-comparison-how-to-interpret-true-negatives-precision-and-recall/41588

---

## Post #1 by @Bernard_Victor (2025-02-09 16:57 UTC)

<p>Operating system: MacOS 15.3<br>
Slicer version: 5.8.0</p>
<p>Hello,<br>
I’m new to 3DSlicer. I’d like to understand how to interpret true negatives in the ‘Segment comparison’ module. I compare the very close segmentation of a nerve on a ultrasound sequence that occupy about 5% of the screen, and true negative appear to be 25% while it should be around 95% (or a similar order of magnitude).<br>
On the other side, can I use the TN, TP and FN % to calculate precision and recall?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/825d5bb304129228be44f5e314c919e7aa5677a7.jpeg" data-download-href="/uploads/short-url/iBg5AEr6s5Lmq6t5um8aT8XpfQH.jpeg?dl=1" title="Capture d’écran 2025-02-09 à 01.35.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825d5bb304129228be44f5e314c919e7aa5677a7_2_690x389.jpeg" alt="Capture d’écran 2025-02-09 à 01.35.59" data-base62-sha1="iBg5AEr6s5Lmq6t5um8aT8XpfQH" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825d5bb304129228be44f5e314c919e7aa5677a7_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825d5bb304129228be44f5e314c919e7aa5677a7_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/825d5bb304129228be44f5e314c919e7aa5677a7_2_1380x778.jpeg 2x" data-dominant-color="928F8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2025-02-09 à 01.35.59</span><span class="informations">1920×1084 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much.</p>
<p>Bernard</p>

---

## Post #2 by @cpinter (2025-02-11 10:08 UTC)

<p>For performance reasons, segments are stored only using their “effective extent” i.e. the region that contains non-background voxels. Considering this, the values seem correct. You can potentially extend the segments to the whole image (without checking, I think the best way to do this is to export the segmentation to labelmap using the image as a reference - in the Segmentations module - and then importing it back to segmentation). However, I find Dice a quite vague metric, due to its many dependencies (one is what you just demonstrated, another is that it works very differently with round shapes vs elongated shapes), and I recommend using Hausdorff instead.</p>

---

## Post #3 by @Bernard_Victor (2025-02-11 12:39 UTC)

<p>Hello and thank you for your kind answer.<br>
Could you please elaborate about non-background voxels? Or point to a tutorial that I could learn from?<br>
Actually the most important is: do the percentages TP, FN and FP here correspond to true overlap of the 2 segments or segmentation without overlap for FN and FP. I want to evaluate segmentation of one user against another one here. So I’m in 2D. I’ll use the software later for 3D analysis and training.</p>
<p>I’m aware of the limitations of DSC. Thank you for the suggestion I’ll add the Hausdorff distance indeed. In nerve segmentation, clinicians (I’m one of them, an anesthesiolgist)  like to stick with easy to understand metrics, so DSC is used a lot (a well as IoU). Even precision and recall are hardly mentionned.</p>
<p>Thank you very much in any case.</p>

---

## Post #4 by @cpinter (2025-02-11 12:56 UTC)

<aside class="quote no-group" data-username="Bernard_Victor" data-post="3" data-topic="41588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bernard_victor/48/79395_2.png" class="avatar"> Bernard_Victor:</div>
<blockquote>
<p>Could you please elaborate about non-background voxels? Or point to a tutorial that I could learn from?</p>
</blockquote>
</aside>
<p>This is the paper about the segmentations infrastructure. A few things have changed since then, for example now we use layers for more efficient storage of segments, but the gist is the same.</p>
<p>Pinter, C., Lasso, A., &amp; Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. <a href="https://doi.org/10.1016/j.cmpb.2019.02.011" class="inline-onebox">Redirecting</a></p>
<aside class="quote no-group" data-username="Bernard_Victor" data-post="3" data-topic="41588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bernard_victor/48/79395_2.png" class="avatar"> Bernard_Victor:</div>
<blockquote>
<p>In nerve segmentation, clinicians (I’m one of them, an anesthesiolgist) like to stick with easy to understand metrics, so DSC is used a lot</p>
</blockquote>
</aside>
<p>I’m quite surprised, as I don’t think DSC is easier to understand than mean/max mm distances, and with elongated structures such as nerves it is borderline useless (1mm difference with a 1mm diameter structure results in a score of 0).</p>

---

## Post #5 by @Bernard_Victor (2025-02-12 18:43 UTC)

<p>Thank you very much for your kind help and for your advice.<br>
The nerves we study are bigger nerve (5-15 mm diameter). But yes DSC has many problems, including not distinguishing between FP and FN.<br>
I will definitely use also Hausdorf distance in my work too thanks to your knowledgable advice.</p>

---
