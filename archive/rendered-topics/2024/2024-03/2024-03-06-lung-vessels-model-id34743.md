# Lung vessels model

**Topic ID**: 34743
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/lung-vessels-model/34743

---

## Post #1 by @Vikram (2024-03-06 14:14 UTC)

<p>I segmented lung vessels model by using 3d slicer but the problem is that i want to print this model but vessels are connected to each other , what i can do there is any other way to do. please help me struck in my research project .</p>

---

## Post #2 by @lassoan (2024-03-07 04:17 UTC)

<p>Why is it a problem that vessels are connected to each other? Can you attach a few screenshots to illustrate?</p>

---

## Post #3 by @Vikram (2024-03-07 05:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f7e83209831ac7ad0c32945e06497e0a837738d.jpeg" data-download-href="/uploads/short-url/ktpkqotDp5hS46RcBco2nUTcUEJ.jpeg?dl=1" title="3D VESSELS WITH SUPPORT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f7e83209831ac7ad0c32945e06497e0a837738d_2_690x338.jpeg" alt="3D VESSELS WITH SUPPORT" data-base62-sha1="ktpkqotDp5hS46RcBco2nUTcUEJ" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f7e83209831ac7ad0c32945e06497e0a837738d_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f7e83209831ac7ad0c32945e06497e0a837738d_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f7e83209831ac7ad0c32945e06497e0a837738d_2_1380x676.jpeg 2x" data-dominant-color="DCDEE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D VESSELS WITH SUPPORT</span><span class="informations">1879×922 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6ed4f2a2877ada6082b183878b831325b1b5129.png" data-download-href="/uploads/short-url/zepTcNqS0DBtcYlga71ktUnj209.png?dl=1" title="VEESELS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6ed4f2a2877ada6082b183878b831325b1b5129_2_690x373.png" alt="VEESELS" data-base62-sha1="zepTcNqS0DBtcYlga71ktUnj209" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6ed4f2a2877ada6082b183878b831325b1b5129_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6ed4f2a2877ada6082b183878b831325b1b5129_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6ed4f2a2877ada6082b183878b831325b1b5129_2_1380x746.png 2x" data-dominant-color="837FA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VEESELS</span><span class="informations">1858×1005 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
sorry typing error i wrote connect , but actually vessels are not connected to each other when i print the 3d lung vessels model due to a lot support material during printing , so it is impossible to clean the vessels from  support material  with out affect to vessels . so what i can do now . my project to lung phantom construction i want to put lung vessels in model .<br>
i also upload my segmented vessels and also vessels during printing with support.<br>
your help very helpful for me</p>

---

## Post #4 by @lassoan (2024-03-12 04:12 UTC)

<p>You can reduce surface smoothing or use Margin effect to connect more vessels. You can then use Islands effect to see what vessel segments are not connected and manually connect them (or further decrease smoothing or increase thickness of all vessels).</p>

---

## Post #5 by @Vikram (2024-03-12 08:36 UTC)

<p>In which software I can use surface smoothing and margin effect ?<br>
Can you please mention any software or it is present in 3d slicer</p>
<p>Thank you so much</p>

---

## Post #6 by @lassoan (2024-03-12 12:06 UTC)

<p>These are all in 3D Slicer’s Segment Editor module.</p>
<p>Surface smoothing is a slider of the <code>Show 3D</code> button’s dropdown menu. Margin effect.</p>
<p>You can find <code>Margin</code> effect in the toolbar in the module panel on the left. Since the minimum size to expand is limited by the resolution of the segmentation’s internal labelmap representation, it may be useful to increase that resolution as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---
