---
topic_id: 10722
title: "Registration Of Mr And Ct Volumes"
date: 2020-03-17
url: https://discourse.slicer.org/t/10722
---

# Registration of MR and CT volumes

**Topic ID**: 10722
**Date**: 2020-03-17
**URL**: https://discourse.slicer.org/t/registration-of-mr-and-ct-volumes/10722

---

## Post #1 by @Anonymous (2020-03-17 17:44 UTC)

<p>Hello, I am working on registering a CT volume with an MR volume. The slice thicknesses are 5mm and 2.6mm, respectively. To do the registration, I first cropped the MR and CT volumes so that only the head region was selected, then I changed the CT slice thickness to 2.6mm in the volumes tab before manually registering. Could you please let me know how the interpolation takes place when I change the slice thickness from 5mm to 2.6mm and if this is a fair way to do the registration. Many slices do not appear registered if I keep the 5mm slice thickness for the CT volume and 2.6mm slice thickness for the MR volume.<br>
Thank you very much,<br>
Emily</p>

---

## Post #2 by @pieper (2020-03-18 00:36 UTC)

<p>Hi Emily -</p>
<p>Changing the spacing via the Volumes module is probably not what you want.  Instead, if you need to you can change the sampling resolution during the Crop Volume operation.  But you may not need to do that, since registration algorithms should all be operating in physical space.</p>
<p>Hope that helps</p>

---

## Post #3 by @juday (2020-03-19 03:26 UTC)

<p>Hi Emily,</p>
<p>Changing slice thickness in volumes will adjust the distance between slices but not its resolution. To change slice thickness of CT, you can try resample scalar volumes. But, you can totally skip resampling if you are registering volumes. The resolution of ‘Moving volume’ is matched with ‘Fixed volume’. In your case, have MR volume as Fixed image volume and CT as moving image volume.</p>
<p>I suggest the following steps (it works for me all the time)</p>
<ol>
<li>Center both volumes in ‘Volumes’ module</li>
<li>Roughly align CT to MR using ‘Transforms’ module</li>
<li>Register both volumes with 'General Registration (BRAINS) with MR as fixed and CT as moving image volumes. You can try different options under Registration phases (Rigid+scale works for me)</li>
</ol>

---

## Post #4 by @Anonymous (2020-04-10 15:25 UTC)

<p>Thank you for this good advice. I am using the MMI cost metric and I am wondering if there is a way to view the results of this metric before and after registration. Also, do you know if there is the ability to record multiple steps into a script so that I can more efficiently register multiple patients?</p>

---

## Post #5 by @lassoan (2020-04-10 23:36 UTC)

<aside class="quote no-group" data-username="Anonymous" data-post="4" data-topic="10722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anonymous/48/5985_2.png" class="avatar"> Anonymous:</div>
<blockquote>
<p>Thank you for this good advice. I am using the MMI cost metric and I am wondering if there is a way to view the results of this metric before and after registration.</p>
</blockquote>
</aside>
<p>You can find parameter values and metric values in each iteration in the application log. However, metric values that are encountered during a registration process are usually not very informative. If you want to get an idea of how robust or accurate the metric is then you can re-run the registration many times with slightly perturbed input parameters and see what percentage of the runs converge. It may be also useful to explore the metric values by setting parameters to the optimum value and change two parameters in a range of +/- 10-20 millimeters or degrees and plot the resulting surface (it is good if the surface is smooth and has a sharp peak at the optimum).</p>
<aside class="quote no-group" data-username="Anonymous" data-post="4" data-topic="10722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anonymous/48/5985_2.png" class="avatar"> Anonymous:</div>
<blockquote>
<p>Also, do you know if there is the ability to record multiple steps into a script so that I can more efficiently register multiple patients?</p>
</blockquote>
</aside>
<p>Recording should not be necessary. You can access all Slicer features in Python that you can run scripts directly in Slicer’s built-in Python interpreter. There are lots of examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">Slicer script repository</a> and you can find scripting tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">here</a>. If you are unsure about how to access a specific functionality from Python and google search does not help then feel free to ask here.</p>

---
