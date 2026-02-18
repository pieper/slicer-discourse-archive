# Why growing segment by 10mm margin is different from growing by 5mm margin twice

**Topic ID**: 11985
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/why-growing-segment-by-10mm-margin-is-different-from-growing-by-5mm-margin-twice/11985

---

## Post #1 by @Mark_Brahier (2020-06-10 17:49 UTC)

<p>Thanks so much for your help. I have another follow-up to this thread. Why is it that the output statistics (volume) are different if you do one 10mm margin growth versus two 5mm margin growths?  It seems counter to my understanding of how this is working. I thought both would result in a 10mm 3D growth from the initial segment.</p>

---

## Post #2 by @lassoan (2020-06-10 19:02 UTC)

<p>Result of each segmentation operation is saved as a binary labelmap. This discretization step can introduce noticeable differences if the margin size is comparable to voxel size. If you grow margin 2x then you perform discretization 2x, therefore you get slightly less accurate results.</p>
<p>Overall, it is not likely that by doing the margin growing in two steps lead to clinically significant differences, I would recommend to perform region growing in a single step.</p>

---

## Post #3 by @Mark_Brahier (2020-06-10 19:08 UTC)

<p>That makes sense. The problem is that my computer is not capable of doing the full 20mm margin that I want in a single step, so I was hoping to break it into smaller pieces (up to 10mm). Slicer eventually crashes before the analysis is complete. Is there a way to correct for it if I need to do multiple steps? Or is there something I can do with my computer to give it the capacity to analyze the full 20mm margin in one step?</p>

---

## Post #4 by @lassoan (2020-06-10 19:41 UTC)

<p>There are several options. Which Slicer version do you use? How much physical RAM do you have in your computer and how much virtual memory have you configured in your operating system? What are the dimensions (how many voxels along each axis) and spacing of your image? Do you see clinically significant difference between doing margin growing in one or more steps?</p>

---

## Post #5 by @Mark_Brahier (2020-06-11 13:13 UTC)

<p>I am using Slicer 10.4.2. RAM is 8 GB 2133 MHz LPDDR3, and I don’t have virtual memory that I know of. The images are around 100 million total voxels (~450 in each axis). As an example, a 10mm margin growth was 21x21x23 pixels and took 9 minutes. I learned that Slicer does eventually complete a 20mm margin growth analysis but it took more than an hour for one CT. The one step 20mm growth does produce a clinically significant difference as compared to breaking it into multiple steps. Do you have any suggestions?</p>

---

## Post #6 by @lassoan (2020-06-11 14:17 UTC)

<p>Use latest Slicer Preview Release, it has significant memory efficiency and speed improvements compared to Slicer-4.10.2. Specifically, margin effect speed has been dramatically improved.</p>
<p>Every modern operating systems uses virtual memory management. You can specify how much memory space (called virtual memory on Windows, swap size on Linux) you want, and if you run out of physical RAM then the operating system starts to use your disk. Of course disk storage is magnitudes slower than RAM, but it can ensure that you never run out of memory and if you need lots of memory only for managing a few peak periods then the performance impact may be acceptable.</p>

---
