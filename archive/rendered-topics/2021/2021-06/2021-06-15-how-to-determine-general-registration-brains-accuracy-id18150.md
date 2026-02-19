---
topic_id: 18150
title: "How To Determine General Registration Brains Accuracy"
date: 2021-06-15
url: https://discourse.slicer.org/t/18150
---

# How to determine general registration (BRAINS) accuracy?

**Topic ID**: 18150
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/how-to-determine-general-registration-brains-accuracy/18150

---

## Post #1 by @ahopf (2021-06-15 18:10 UTC)

<p>Hi, I am registering MRI and CT images of the scapula using the MMI cost metric in the general registration (BRAINS) module. Is there a way to quantify the accuracy of this registration method?</p>

---

## Post #2 by @lassoan (2021-06-15 19:24 UTC)

<p>There is no easy way of characterizing registration error. The image comparison cost metric value (such as MMI) is not related registration accuracy in any way. Even the residual error of the registration does not characterize accuracy.</p>
<p>Registration accuracy is usually evaluated by identifying matching pairs of landmarks in the region of interest and computing root mean square error. Identifying the points may require considerable skill and effort and limited by the image resolution and what features are in the image.</p>
<p>In addition to accuracy of the registration, it is also important to evaluate its robustness, which is well characterized by convergence range (how far from the global optimum you can start the registration form and still converge to the correct solution). You can do that by restarting the registration many times from randomly perturbed initial positions/orientations and create a statistics of success rate. It is also useful to inspect the shape and smoothness of the cost metric that you plot as a surface while changing two transform parameters.</p>

---

## Post #3 by @ahopf (2021-06-15 19:27 UTC)

<p>Thank you! That is very helpful.</p>

---
