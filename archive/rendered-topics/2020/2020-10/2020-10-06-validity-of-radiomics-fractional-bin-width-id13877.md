# Validity of Radiomics Fractional Bin Width

**Topic ID**: 13877
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/validity-of-radiomics-fractional-bin-width/13877

---

## Post #1 by @furMan (2020-10-06 02:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I’m analyzing MR images, and am normalizing the images using the following method:</p>
<ol>
<li>Subtract the mean of the non-zero intensities</li>
<li>Divide by the standard deviation of the non-zero intensities</li>
</ol>
<p>This results in a smaller range of intensities (between 0 and on order of ~10).  In order to have a reasonable number of bins, I’ve been using fractional bin width values; e.g., 0.25, for the Radiomics input.</p>
<p>I see that fractional values are accepted, but wanted to verify that using fractional bin widths is valid.   Thank you for any advice.</p>

---

## Post #2 by @fedorov (2020-10-06 02:06 UTC)

<p>Yes, fractional bin width is valid.</p>

---
