---
topic_id: 36605
title: "Slicer Crashed After Run This Script"
date: 2024-06-05
url: https://discourse.slicer.org/t/36605
---

# Slicer crashed after run this script

**Topic ID**: 36605
**Date**: 2024-06-05
**URL**: https://discourse.slicer.org/t/slicer-crashed-after-run-this-script/36605

---

## Post #1 by @Xiaojie_Guo (2024-06-05 13:26 UTC)

<p>Hi, all<br>
After running <a href="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f" rel="noopener nofollow ugc">MaskVolumeHistogramPlot.py</a>, delete the segmentation, which includes Tumor, Reference, and Background, from Data module, Slicer crashed. How to fix this?</p>

---

## Post #2 by @cpinter (2024-06-05 13:53 UTC)

<p>I ran the script in Slicer 5.7.0-2024-05-29, everything was OK, then deleted the segmentation in Data module and there was no crash or anything strange.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb0f6e75115f6ee51be3432e11d806216ba4fcd3.jpeg" data-download-href="/uploads/short-url/sYlZgX6UFne5LjfV2l2w4VPwfLB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f6e75115f6ee51be3432e11d806216ba4fcd3_2_690x393.jpeg" alt="image" data-base62-sha1="sYlZgX6UFne5LjfV2l2w4VPwfLB" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f6e75115f6ee51be3432e11d806216ba4fcd3_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f6e75115f6ee51be3432e11d806216ba4fcd3_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f6e75115f6ee51be3432e11d806216ba4fcd3_2_1380x786.jpeg 2x" data-dominant-color="7E7F7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1096 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In general it is a good idea to include information about at least Slicer version and operating system when reporting an issue. Can you please provide these details? Thanks.</p>

---

## Post #3 by @Xiaojie_Guo (2024-06-06 01:33 UTC)

<p>The system is Win10. The version is Slicer-5.6.1. And I tried Slicer-5.4.0 on the same Win10, there was no crash. In my PC, the difference between Slicer-5.6.1 and Slicer-5.4.0 was the installed extensions were different. Is it possible that the extensions that make the problem?</p>

---

## Post #4 by @lassoan (2024-06-06 03:28 UTC)

<p>Let us know if you have any issues with the latest Slicer Preview Release or the latest Slicer Stable Release.</p>

---

## Post #5 by @Xiaojie_Guo (2024-06-06 13:48 UTC)

<p>They are both stable versions.</p>
<p>By now I can use Slicer-5.4.0 to finish my work. Thanks a lot.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/795842380f305bf86e1c3eafd8296adf53897591.png" alt="022" data-base62-sha1="hjsRLHx2SCjT7SpKKg9aCjQsTpD" width="664" height="426"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4be17e421dec7abdbc8cbe8e3cdca9675e37231.png" alt="023" data-base62-sha1="um0uNIAAeJc2wMpnbNfydRdZQsh" width="664" height="425"></p>

---

## Post #6 by @lassoan (2024-06-06 17:28 UTC)

<p>5.6.1 is not the latest stable. Please try 5.6.2. If that works well thej you can switch to use this version.</p>
<p>If the error is reproducible there then please test in latest preview release as well. If the error is reproducible there, too, then we will try to reproduce and fix it in an upcoming preview release.</p>

---
