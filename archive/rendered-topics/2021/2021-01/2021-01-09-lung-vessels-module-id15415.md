# Lung Vessels module

**Topic ID**: 15415
**Date**: 2021-01-09
**URL**: https://discourse.slicer.org/t/lung-vessels-module/15415

---

## Post #1 by @sergiGB (2021-01-09 10:37 UTC)

<p>how can I get lung vessels? i want to get lung vessels without lung body<br>
Thanks !</p>

---

## Post #2 by @rbumm (2021-01-09 12:13 UTC)

<p>You need a lung CT with good vessel contrast. In Slicer, you can use the CTACardio demo data set for example. We found that the new “Local Threshold” function in Slicers´s “Segment Editor” works very  well for extracting the pulmonary artery (blue)  and vein (red). The demo dataset has a limited resolution, you will get more detailed vessels with higher resolutions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e92ca0cf454e1c1b94d8bf1820538a60163fbba.jpeg" data-download-href="/uploads/short-url/fMb10C5SoKVNTSojGJI4Ki55L6y.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e92ca0cf454e1c1b94d8bf1820538a60163fbba_2_690x396.jpeg" alt="image" data-base62-sha1="fMb10C5SoKVNTSojGJI4Ki55L6y" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e92ca0cf454e1c1b94d8bf1820538a60163fbba_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e92ca0cf454e1c1b94d8bf1820538a60163fbba_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e92ca0cf454e1c1b94d8bf1820538a60163fbba.jpeg 2x" data-dominant-color="514F57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1348×774 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @sergiGB (2021-01-09 12:29 UTC)

<p>thank you very much !!!<br>
you are the best!</p>

---

## Post #4 by @rbumm (2021-01-09 13:18 UTC)

<p>Another way to achieve vessel segmentation is to use the “Grow from Seeds” function in the “Segment Editor”.  More manual work, but you get additional airways and lung shadow. I usually define lungs, trachea and bifurcation, pulmonary artery, pulmonary vein and “Other” (paint a circle around the thorax in all axes) with a few paint strokes. Select “Grow from Seeds” and “Initialize”. Correct the results by adding a few paint strokes here and there. Press “Apply”.  Go “Segments” and reduce the lung opacity.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10012dc1e52dc128b3b248aa7901b8c4eab7f0fd.jpeg" data-download-href="/uploads/short-url/2hAae7WjB9ebaZr4YlbrAA48Rlj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10012dc1e52dc128b3b248aa7901b8c4eab7f0fd_2_690x346.jpeg" alt="image" data-base62-sha1="2hAae7WjB9ebaZr4YlbrAA48Rlj" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10012dc1e52dc128b3b248aa7901b8c4eab7f0fd_2_690x346.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10012dc1e52dc128b3b248aa7901b8c4eab7f0fd_2_1035x519.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10012dc1e52dc128b3b248aa7901b8c4eab7f0fd_2_1380x692.jpeg 2x" data-dominant-color="828384"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×963 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @TMrt (2021-01-09 13:19 UTC)

<p>Hello,</p>
<p>CIP Lung Segmenter, Flood Fill and Logical Operators Subtract were the only effects I used for these results. The scan slice thickness is .06 mm and most of the iv contrast was in the pulmonary artery.  Hope this helps.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b23574e181b896626c6c88fd983969d6db26ea.jpeg" data-download-href="/uploads/short-url/sDriTjYTRaJq0qi7tPufGUmmkwG.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8b23574e181b896626c6c88fd983969d6db26ea_2_684x500.jpeg" alt="Screenshot" data-base62-sha1="sDriTjYTRaJq0qi7tPufGUmmkwG" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8b23574e181b896626c6c88fd983969d6db26ea_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b23574e181b896626c6c88fd983969d6db26ea.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b23574e181b896626c6c88fd983969d6db26ea.jpeg 2x" data-dominant-color="797483"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">823×601 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @sergiGB (2021-01-09 16:06 UTC)

<p>gracias de nuevo! pero no le eche cuenta a su esposa jajajajaja</p>

---

## Post #7 by @rbumm (2021-01-09 16:30 UTC)

<p>Very interesting, could you post a short workflow ?</p>

---

## Post #8 by @sergiGB (2021-01-09 16:33 UTC)

<p>Muchas gracias! lo voy a mirar y a ver que tal! gracias!</p>

---

## Post #9 by @TMrt (2021-01-10 04:46 UTC)

<p>Sure Rudolf-I used version 4.13.0-2020-12-10 for the following workflow:</p>
<p>CIP&gt;Lung CT Segmenter<br>
Segment Editor&gt;additional segment painted over hilum/cardiac area<br>
Trachea replaced using Flood Filling for deeper segmentation<br>
PA and PV&gt; Flood Filling<br>
Editable Area&gt;Inside All Segments&gt;Allow Overlap<br>
Intensity Tolerance ranged anywhere from 50-120<br>
Logical Operators&gt;Subtraction</p>
<p>Thank you</p>

---

## Post #10 by @Chuns_SS (2021-06-17 10:05 UTC)

<p>Hello, I am relatively new to Slicer so can you explain in further detail exactly what you do when you start using the Segment Editor (“Segment Editor&gt;additional segment painted over hilum/cardiac area”<br>
) for the extracting the pulmonary vessells.<br>
Many thanks</p>

---

## Post #11 by @TMrt (2021-06-17 12:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00da528328774cfa9803561eeffd8782b223771d.jpeg" data-download-href="/uploads/short-url/7xKI4kREgfgtiTQXj61DcaXd1z.jpeg?dl=1" title="LUNG_VESSELS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00da528328774cfa9803561eeffd8782b223771d_2_690x387.jpeg" alt="LUNG_VESSELS" data-base62-sha1="7xKI4kREgfgtiTQXj61DcaXd1z" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00da528328774cfa9803561eeffd8782b223771d_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00da528328774cfa9803561eeffd8782b223771d_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00da528328774cfa9803561eeffd8782b223771d.jpeg 2x" data-dominant-color="B1B4BC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LUNG_VESSELS</span><span class="informations">1366×768 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hello-that refers to Segment_1 circled in red.  I found that by encompassing the entire area of interest, Flood Fill tool gave great results with minimal additional editing in this particular case.  I experimented with this workflow omitting this step and found the segmentation differed.  Hope that helps-Thank you</p>

---

## Post #12 by @Chuns_SS (2021-06-17 15:20 UTC)

<p>Thank-you, I’ll give that a try<br>
Sam</p>

---

## Post #13 by @lassoan (2024-02-27 14:25 UTC)

<p>A post was split to a new topic: <a href="/t/segment-lungs-airways-pulmonary-vessels/34570">Segment lungs, airways, pulmonary vessels</a></p>

---

## Post #14 by @wwwww (2025-05-06 12:15 UTC)

<p>Could you post more detail steps about you method ,thank you very much!</p>

---
