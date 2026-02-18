# Comparison of the Dose Comparison and DVH Comparison modules results

**Topic ID**: 9655
**Date**: 2019-12-30
**URL**: https://discourse.slicer.org/t/comparison-of-the-dose-comparison-and-dvh-comparison-modules-results/9655

---

## Post #1 by @aseman (2019-12-30 06:23 UTC)

<p>Slicer version:4.10.1<br>
Hi 3D Slicer experts and all<br>
I have 2 RT Dose (RT Dose1 and RT Dose2) and a segmentation (renamed PTV). I compared 2 dose distribution for PTV, with Dose Comparison module; and the Pass Fraction was calculated 96.46%. Also, I calculated DVHs for them with Dose Volume Histogram module and Exported them into a CSV File(figure1), which the results up to 1.7 Gy are similar; but the Agreement acceptance is 92.31%. can you help me about my questions:</p>
<p>1- As shown in figure1, the received dose for PTV , up to 1.7 Gy is similar with RT Dose1 and RT Dose2. so, why is the Agreement acceptance = 92.31%?  shouldn’t it be more than 92.31%?</p>
<p>2- Pass Fraction in Dose comparison module is 96.46% and Agreement acceptance is 92.31%. what is the reason for this difference?</p>
<p>Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce7a39a99e9bd4b6f7d89633a3a444a427ff961.png" data-download-href="/uploads/short-url/mo2LJcW37ldeM5ckXGj0xUEqdGh.png?dl=1" title="CSV File Exportation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce7a39a99e9bd4b6f7d89633a3a444a427ff961.png" alt="CSV File Exportation" data-base62-sha1="mo2LJcW37ldeM5ckXGj0xUEqdGh" width="517" height="276" data-dominant-color="F6F2EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CSV File Exportation</span><span class="informations">897×480 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-01-15 02:27 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> <a class="mention" href="/u/cpinter">@cpinter</a> do you know if the results above can be normal or they are unexpected?</p>

---

## Post #3 by @cpinter (2020-01-15 09:18 UTC)

<ol>
<li>
<p>Why do you think it “should be more than 92.31%” ? The dose comparison module compares the dose volumes themselves, using the Gamma comparison method [1]. It is based on dose difference and distance-to-agreement, and has many parameters, such as the acceptance thresholds of these two components. SlicerRT’s gamma algorithm has been validated against other implementations, and it was found to have a 100% match to the baselines [2].</p>
</li>
<li>
<p>Dose comparison is based on the dose volumes themselves, while DVH comparison compares derived metrics: the DVHs, which are a considerably simplified representation of the dose volumes considering the segmented structures. The DVHs are compared using a simplified Gamma method [3], and has similar but different parameters, and different defaults for those.</p>
</li>
</ol>
<p>[1] Low, D. a., &amp; Dempsey, J. F. (2003). Evaluation of the gamma dose distribution comparison method. Medical Physics, 30(9), 2455. <a href="https://doi.org/10.1118/1.1598711">https://doi.org/10.1118/1.1598711</a><br>
[2] Alexander, K. M., Pinter, C., Fichtinger, G., Olding, T., &amp; Schreiner, L. J. (2018). Streamlined Open-Source Gel Dosimetry Analysis in 3D Slicer. Biomed. Phys. Eng. Express, 1–23.<br>
[3] Ebert, M. a, Haworth, a, Kearvell, R., Hooton, B., Hug, B., Spry, N. a, … Joseph, D. J. (2010). Comparison of DVH data from multiple radiotherapy treatment planning systems. Physics in Medicine and Biology, 55(11), N337-46. <a href="https://doi.org/10.1088/0031-9155/55/11/N04">https://doi.org/10.1088/0031-9155/55/11/N04</a></p>

---
