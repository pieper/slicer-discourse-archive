---
topic_id: 11386
title: "Simulate Mr Noise And Patient Related Artifacts In Slicer"
date: 2020-05-02
url: https://discourse.slicer.org/t/11386
---

# Simulate mr noise and patient related artifacts in slicer

**Topic ID**: 11386
**Date**: 2020-05-02
**URL**: https://discourse.slicer.org/t/simulate-mr-noise-and-patient-related-artifacts-in-slicer/11386

---

## Post #1 by @GMA (2020-05-02 21:50 UTC)

<p>is there a way to simulate image noise in MR images using slicer? Is it possible to simulate patient movement?</p>
<p>I found in the simple itk filters “add gaussian noise” but i’m not sure this could be appropriate, for patient movement artifact i didn’t find any references</p>
<p>Thank you!</p>
<p>Giorgio</p>

---

## Post #2 by @lassoan (2020-05-04 13:57 UTC)

<aside class="quote no-group" data-username="GMA" data-post="1" data-topic="11386">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gma/48/4221_2.png" class="avatar"> GMA:</div>
<blockquote>
<p>is there a way to simulate image noise in MR images using slicer?</p>
</blockquote>
</aside>
<p>Lots of kinds of noise and artifacts may appear on MRI images. I don’t think there is any simulator readily available as a Slicer module. If you want to have something simple, such as simulating Rician Noise then you can easily add it using a few lines of Python code in Slicer (see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_noise_to_image">here</a>). If you want to do generate more sophisticated noise or artifacts then you try various MRI simulators (there must be ones implemented in Python that you can use directly in Slicer).</p>
<p>To add simulated distortion (e.g., due to soft-tissue motion) then a simple method is to create a warping transform by prescribing displacements at selected control points. See complete example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Apply_random_deformations_to_image">here</a>. Hardening of the transform using this example script does not work in latest Slicer Preview Release, but I’ve already fixed the issue and it will work in tomorrow’s version.</p>

---

## Post #3 by @JanWitowski (2020-05-04 17:36 UTC)

<p>In addition to what <a class="mention" href="/u/lassoan">@lassoan</a> said, you might look into <a href="https://github.com/fepegar/torchio" rel="nofollow noopener">torchio library</a> that implemented a number of MR artifacts, including ones you’re interested in. You should be able to use it within Slicer with a Python snippet, extending the “Add noise to image” example.</p>

---

## Post #4 by @GMA (2020-05-04 18:34 UTC)

<p>thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/janwitowski">@JanWitowski</a> for your useful replies. I’ll try the solution you posted</p>

---
