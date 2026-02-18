# Can we check and rescale pixel intensity values in Slicer?

**Topic ID**: 34709
**Date**: 2024-03-05
**URL**: https://discourse.slicer.org/t/can-we-check-and-rescale-pixel-intensity-values-in-slicer/34709

---

## Post #1 by @Windy (2024-03-05 01:41 UTC)

<p>I have a few Micro CT datasets. When I check in Python, I can see some intensity values are between 0 and 255 while some are like between 54 and 223. Since I am working with a machine learning model, I want all of them to be between 0 and 255, so my input is identical to each other. Is there a way to do this using Slice GUI, without scripting?</p>

---

## Post #2 by @muratmaga (2024-03-05 01:52 UTC)

<p>It is about four lines of code in python, and if you have a lot of samples, running them through UI will probably take longer.<br>
Anyways, you can do it through Simple Filters-&gt;NormalizeImageFilter, and before feeding them into your ML pipeline, you can multiply the values by 255 (if you need to have them 0-255).</p>
<p>The more crucial question is why you have so much difference, which may have substantial effect on your ML pipeline if for example are 0-255 ones are full spectrum of the data, whereas 54-223 are somehow volumes cropped and there are no background voxels.</p>

---

## Post #3 by @Windy (2024-03-05 21:35 UTC)

<p>Thank you for your input.</p>
<p>I used AHE from Simple Filters on each dataset to enhance contrast. This range difference happened after that. My original datasets were all between 0-255. I am wondering if I am doing something wrong.</p>

---

## Post #4 by @Windy (2024-03-05 23:28 UTC)

<p>This happens only when the Adaptive Histogram Equalization is applied after the Gaussian filter.</p>

---

## Post #5 by @muratmaga (2024-03-06 01:36 UTC)

<p>So there is no real consensus about whether this type of preprocessing is helping or hurting ML pipelines. My preference would have been to start with unprocessed data and then see if preprocessing improves (or deteriorates) the results compared to raw.</p>

---

## Post #6 by @Windy (2024-03-06 02:10 UTC)

<p>Thank you for your input <img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=12" title=":innocent:" class="emoji" alt=":innocent:" loading="lazy" width="20" height="20"> I will try that out.</p>

---
