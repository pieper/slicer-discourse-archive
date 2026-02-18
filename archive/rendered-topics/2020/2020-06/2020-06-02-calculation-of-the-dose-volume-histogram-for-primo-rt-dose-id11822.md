# Calculation of the Dose Volume Histogram for Primo RT Dose

**Topic ID**: 11822
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/calculation-of-the-dose-volume-histogram-for-primo-rt-dose/11822

---

## Post #1 by @aseman (2020-06-02 03:43 UTC)

<p>Slicer version: 4.10.1<br>
Hi 3d Slicer Experts and all<br>
I want to calculate Dose Volume Histograms for two RT Dose ,which the first has been obtained from Treatment Planning System (TPS), and the second from Mont Carl code (Primo software), using Dose Volume Histogram Module in 3D slicer. The Primo software inputs are CT image, RT Structure, RT Plan and its output is RT Dose. this output is a text file and we converted it to a Dose volume. when I calculate DVHs for them, The maximum and mean dose values for Primo Dose are zero, while the DVHs of the TPS are non-zero as shown in the figures.<br>
can you help me about this problem? and how can I calculate DVHs for Primo dose?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/179ddc62efde50961ac40bcdf1a61649ea4b4753.jpeg" data-download-href="/uploads/short-url/3mVce3Gig8J1dSUCCir2QpZFQBB.jpeg?dl=1" title="dose volume histogram" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179ddc62efde50961ac40bcdf1a61649ea4b4753_2_517x291.jpeg" alt="dose volume histogram" data-base62-sha1="3mVce3Gig8J1dSUCCir2QpZFQBB" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179ddc62efde50961ac40bcdf1a61649ea4b4753_2_517x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179ddc62efde50961ac40bcdf1a61649ea4b4753_2_775x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179ddc62efde50961ac40bcdf1a61649ea4b4753_2_1034x582.jpeg 2x" data-dominant-color="88888C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dose volume histogram</span><span class="informations">4128×2322 1.68 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2020-06-02 08:03 UTC)

<p>The first thing to make sure is that the dose volume and the structure sets align well. Please try to visualize the CT and the Primo dose and the contours in the slice views and see if it shows up as it should.</p>

---
