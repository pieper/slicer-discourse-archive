---
topic_id: 11998
title: "How Can I Speed Up The Registration Process In The Elastix M"
date: 2020-06-12
url: https://discourse.slicer.org/t/11998
---

# How can I speed up the registration process in the Elastix module?

**Topic ID**: 11998
**Date**: 2020-06-12
**URL**: https://discourse.slicer.org/t/how-can-i-speed-up-the-registration-process-in-the-elastix-module/11998

---

## Post #1 by @kuba_grepl (2020-06-12 05:27 UTC)

<p>Hello everybody.<br>
I use Elastix module for deformable multimodal registration of 3DCT and 3DMRI scans of human head and neck. It works very well. Thank you for this amazing software tool!!!<br>
Unfortunately, one registration takes about  45 minutes and I have approximately 150 data sets to be registered (a huge amount of time). Do you have any idea how to speed up the registration process??? CPU is used to 70% and memory only approx.4GB during the calculation.</p>
<p>My computer configuration is:<br>
Intel® Core(TM i5-8400 CPU at 2.80Ghz, 16GB Memory, 64bit system Win10Pro</p>
<p>Dedicated graphical hardware is missing. Do you think that an additional graphic card can speed up the process dramatically? Our IT department offered me a multithreaded processor. Can it help?</p>
<p>Thank you for any idea. Greetings from the heart of Europe.</p>

---

## Post #2 by @muratmaga (2020-06-12 05:49 UTC)

<p>Depending on the size of the datasets, 45 minutes is actually acceptable. You can downsample your volumes with CropVOlume, which will definitely help with the speed, but at the expense of detail. Alternatively, you can try to find a computer that has many cores (your laptop has only 6). That will speed up the process.</p>
<p>Regardless though, if you have 150 samples to register, this is usually done as a batch job using a dedicated computer running 24h.</p>

---

## Post #3 by @pieper (2020-06-12 11:58 UTC)

<p>I agree with Murat, 45 minutes is not bad if you are getting useful results.  It was not so long ago that people couldn’t imagine doing that kind of registration task at all.  Another thing to consider is a cloud computing system like <a href="https://aws.amazon.com/workspaces/">amazon workspaces</a> or similar from google or microsoft and get a bunch of machines working at the same time.</p>

---

## Post #4 by @lassoan (2020-06-12 16:18 UTC)

<p>I would expect that a simple rigid+bspline registration can be completed in a couple of minutes, but you may need to tune the registration parameters to reduce computation time without impacting accuracy.</p>
<p>However, learning about how Elastix works and experiment with various parameter sets may take longer than just run the registration on all your data sets as is (which should complete within 5 days). Maybe the best is to start the batch registration as is on one computer and if you have nothing else to do then experiment with different parameters (how you initialize the registration, how many samples do you use, what is the stopping condition, maximum number of iterations, etc.).</p>

---

## Post #5 by @kuba_grepl (2020-06-15 12:27 UTC)

<p>Thank you muratmaga, pieper and lassoan. Now I know that I use Elastix right and can happily continue my research.</p>

---
