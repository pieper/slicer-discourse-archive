---
topic_id: 34253
title: "Igt Volume Reconstruction Output Spacing"
date: 2024-02-12
url: https://discourse.slicer.org/t/34253
---

# IGT volume reconstruction: Output spacing

**Topic ID**: 34253
**Date**: 2024-02-12
**URL**: https://discourse.slicer.org/t/igt-volume-reconstruction-output-spacing/34253

---

## Post #1 by @Olivier (2024-02-12 09:54 UTC)

<p>Hello,<br>
I am using the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/AlgorithmVolumeReconstruction.html" rel="noopener nofollow ugc">Volume reconstruction</a> feature from the IGT module and have a question about the Output spacing parameter specifically.<br>
I am using ultrasound data obtained from manual sweeps, about in the same direction as one of the axes (K) and the other dimensions (I, J) define the 2D images.</p>
<p>Are there instructions somewhere about a systematic method to adjust these values? At the moment I do it by trial and error, by using the original scaling factor for I and J, and by decreasing K incrementally.</p>

---

## Post #2 by @Olivier (2024-03-11 17:43 UTC)

<p>Hi there. It does not look like anyone is inspired by this question <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>
<p>The reason I was asking is because 3D slicer crashes if I use certain resolution settings…</p>

---

## Post #3 by @lassoan (2024-03-12 04:36 UTC)

<p>In general, you set the spacing based on what you need (how small details you want to reconstruct from the image slices) and it does not depend on the imaging settings or how the operator moved the transducer. Available memory on your computer may also be a deciding factor: it is generally advisable to keep the reconstructed image size about 10x smaller than the amount of physical RAM in your computer. If you choose an image size that does not fit in your physical memory limit then your computer will slow down a lot; if you even exceed the virtual memory size that you have configured for your computer then the application will crash (it is practically impossible to prevent crash when you run out of memory).</p>

---

## Post #4 by @Olivier (2024-03-12 10:55 UTC)

<p>Thank you!</p>
<p>Useful rule of thumb. I have however the impression that my laptop crashes with smaller files. It is a Mac with 16GB of RAM and an M1 processor. I have read in the forum that this should not be an issue but when I monitor the PCU activity during reconstruction I can see that it saturates quite fast. Do you know if there are any plans to develop a version of 3D Slicer that would use the GPU for computers with Apple silicon chips?</p>

---
