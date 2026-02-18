# Registration time with CPU speed

**Topic ID**: 11652
**Date**: 2020-05-21
**URL**: https://discourse.slicer.org/t/registration-time-with-cpu-speed/11652

---

## Post #1 by @mmtg (2020-05-21 14:28 UTC)

<p>Hello, I have a rather random question.</p>
<p>I am using BRAINSFit to do some registrations. I am adjusting some parameters, one of them being the “sampling percentage.” Lets say i was to record the registration time when using a sampling percentage of “X” and “Y” and recorded the difference. Would the difference between those two sampling percentages vary with CPU speed significantly?</p>
<p>Thanks, I know this is probably a pretty obscure question and may not be suited for this forum.</p>

---

## Post #2 by @lassoan (2020-05-21 15:07 UTC)

<p>Computing the registration metric (how well the two images are aligned) at each iteration is a significant portion of the registration. The metric is evaluated at each sample point. Therefore, the mor samples you use, the longer one iteration will take.</p>
<p>However, if you use too few samples then your registration accuracy may suffer (not converge to global optimum, not find the optimum accurately). Also, if you use too few samples then the registration may need more iterations to reach convergence.</p>
<p>So, you need to find a good number samples, which ensures convergence and accuracy, but does not take too long time. Usually you determine this number for a registration problem by trial and error.</p>
<p>Since in BRAINSFit, metric is computed on the CPU, the higher the clock rate is, the faster the registration will be. I think metric computation in BRAINSFit is multithreaded, so CPUs with more threads can compute the registration more quickly.</p>
<p>You can also speed up the registration by using an multi-level scheme (first compute a coarse registration and then refine). BRAINSFit may be able to do this, but Elastix (in SlicerElastix extension) is configurable more flexibly, so you can set up sophisticated multi-resolution schemes for all kinds of registration problems.</p>

---

## Post #3 by @mmtg (2020-05-21 16:52 UTC)

<p>Thank you for your detailed answer, appreciate it. That answers most of my questions (particularly good point about the thread count) but does the relative time between different amount of samples not change with the same CPU used? i.e., if I compared 20% sampling vs 50% sampling on a 2Ghz 4 thread vs 3ghz 4 thread, would the relative difference be the same?</p>

---

## Post #4 by @lassoan (2020-05-21 17:13 UTC)

<p>2x more samples will take approximately about 2x more time to compute. 2x more threads will not be able to process 2x more samples in a given timeframe, due to various overheads, but maybe 1.5x. Instead of wondering about what could happen, I would recommend to run tests on your data.</p>
<p>Using a stronger CPU can maybe improve registration speed by a couple of times, but I would not spend too much time on that, as using optimal region of interest, number of samples, multiresolution scheme, optimization parameters, or maybe compute the metric on GPU (I think Elastix can compute some metrics on the GPU) will make a much bigger difference.</p>

---

## Post #5 by @mmtg (2020-05-21 17:30 UTC)

<p>Okay thanks for the input, appreciate it!</p>

---
