---
topic_id: 23835
title: "Shut Down Suddenly"
date: 2022-06-11
url: https://discourse.slicer.org/t/23835
---

# Shut down suddenly

**Topic ID**: 23835
**Date**: 2022-06-11
**URL**: https://discourse.slicer.org/t/shut-down-suddenly/23835

---

## Post #1 by @Akila22 (2022-06-11 19:29 UTC)

<p>Hello,</p>
<p>Slicer version :5.0.2<br>
Operating System :Microsoft Windows 10</p>
<p>3D Slicer shut downs suddenly when cropping a hollowed model from DICOM data ,<br>
Starting by a threshhold selection, then hollowing the model , the first crop can be done,  then 3D slicer shut downs if I try a second one .</p>
<p>Thank you in advance</p>

---

## Post #2 by @lassoan (2022-06-11 20:06 UTC)

<p>Most likely you have run out of memory. What is the size of your data set? In your system information, what are the “Total physical memory” and “Total virtual memory” values?</p>

---

## Post #3 by @Akila22 (2022-06-11 21:01 UTC)

<p>Total Physical memory is 8GB , available 3.9 GB<br>
Total virtual memory 13.9 GB , still 9.94GB</p>
<p>But don’t see the size of my dataset on Slicer?</p>

---

## Post #4 by @lassoan (2022-06-11 23:12 UTC)

<p>You can go to Volumes module and copy here these values from the <code>Volume information</code> section for all the volumes:</p>
<ul>
<li>Image Dimensions</li>
<li>Number of scalars</li>
<li>Scalar type</li>
</ul>
<p>Have you changed the geometry of your segmentation (set an oversampling value of &gt;1)?</p>
<p>While you are editing your segmentation how much physical memory and virtual memory still available?</p>
<p>Can you describe the list of steps that leads to the application crashing? If possible, use one of the sample data sets, so that we can reproduce what you do without the need to get your data.</p>

---

## Post #5 by @Davide_Cester (2022-06-17 09:31 UTC)

<p>Hi,</p>
<p>I just ran into this problem - shutdown during segment editing - and the culprit was indeed memory size.</p>
<p>I was monitoring the RAM usage and it never went above 70%, however I guess Slicer hit the limit before the monitoring could report 99% or similar.</p>
<p>Today I added 16 GB to the existing 16 GB and everything works like a charm. Actually, memory usage never seems to exceed 50%, but I guess there are short peak usages that just go unreported and this can cause the crashes.</p>
<p>I wish Slicer could somehow be able to react to the impossibility to allocate memory, but I understand it may not be straightforward. I wonder why the system did not start to swap, although the performance would probably not have been that great…</p>

---

## Post #6 by @pieper (2022-06-17 12:07 UTC)

<p>Often the memory allocation errors come from the VTK layer that Slicer uses.  More information <a href="https://discourse.vtk.org/t/handling-allocation-errors-in-python/7451">in this thread</a>. If you are working with bigger data, of course save often, but also use the rule of thumb that you need about RAM or virtual memory about 10x the size of your data volumes.</p>

---

## Post #7 by @Akila22 (2022-06-17 12:25 UTC)

<p>Actually I did’nt encouter this trouble after my first essay ! i will check  with your recommandations if it happens again.</p>
<p>Thank you for your assistance</p>

---

## Post #8 by @Akila22 (2022-06-17 12:27 UTC)

<p>Thank you for your clarification</p>

---
