---
topic_id: 7712
title: "Resampling For Radiomics"
date: 2019-07-22
url: https://discourse.slicer.org/t/7712
---

# Resampling for Radiomics

**Topic ID**: 7712
**Date**: 2019-07-22
**URL**: https://discourse.slicer.org/t/resampling-for-radiomics/7712

---

## Post #1 by @J_C (2019-07-22 22:07 UTC)

<p>Hello there, I’ve been trying Radiomics module for a little bit. I’m trying to analize T2 weighted images, but unfortunately they are not equally spaced. So I was thinking, it would be best to resample the entire scan before (or maybe after segmentation) and then extract features, or it would be better to just extract features from the segmentation as it is and use the resampling built in the module? And what parameters would be best to set?<br>
Hope that wasn’t too confusing, I’m not sure I’m getting it all right.</p>

---

## Post #2 by @fedorov (2019-07-24 13:57 UTC)

<p><a class="mention" href="/u/j_c">@J_C</a> there is no one simple answer to what is the best way to configure extraction of features for your data. I suggest you read the studies done for similar applications in the literature to learn about best practices.</p>
<p>To your question about resampling and sample parameter settings, please consider reading this post: <a href="https://discourse.slicer.org/t/do-we-need-to-create-an-isotropic-image-in-radiomics-study/1779" class="inline-onebox">Do we need to create an isotropic image in radiomics study?</a>.</p>

---

## Post #3 by @J_C (2019-07-25 22:53 UTC)

<p>I read some works, however often it’s not stated if they resampled and how. Moreover it is harder to understand if resampling was made with the resample module, in this case I suppose it’s not necessary to resample with the Radiomics module feature extractor, or if it was made as part of the feature extraction procedure.<br>
In the post you suggest it’s not so specific… Maybe I could force a 2d extraction (I would easily have a bidimensional isotropy), but can’t figure how to force it.</p>

---

## Post #4 by @fedorov (2019-07-26 00:37 UTC)

<aside class="quote no-group" data-username="J_C" data-post="3" data-topic="7712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c0e974/48.png" class="avatar"> J_C:</div>
<blockquote>
<p>however often it’s not stated if they resampled and how</p>
</blockquote>
</aside>
<p>Yes, this is unfortunately often true.</p>
<aside class="quote no-group" data-username="J_C" data-post="3" data-topic="7712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c0e974/48.png" class="avatar"> J_C:</div>
<blockquote>
<p>In the post you suggest it’s not so specific… Maybe I could force a 2d extraction (I would easily have a bidimensional isotropy), but can’t figure how to force it.</p>
</blockquote>
</aside>
<p>You can use <code>force2D</code> setting in the configuration file, which you can supply to the Radiomics module. See example settings here: <a href="https://github.com/Radiomics/pyradiomics/blob/master/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" class="inline-onebox">pyradiomics/examples/exampleSettings/exampleMR_NoResampling.yaml at master · AIM-Harvard/pyradiomics · GitHub</a>.</p>

---

## Post #5 by @J_C (2019-07-29 15:14 UTC)

<p>Thank you for the link, pretty useful; there’s even an example for normalization, though I assume you can either get adjusting binwidth in radiomics module, right?<br>
Gonna try this evening.</p>
<p>Just a question: let’s assume that my axial slices are not pure but slightly oblique, should I (and how) reformat so that slicer goes parallale to them? Don’t know if I’m clear.</p>

---

## Post #6 by @fedorov (2019-07-29 15:32 UTC)

<p>Yes, you can definitely adjust binwidth in the user interface. You should use settings file only if there are settings that are not exposed in the interface.</p>
<aside class="quote no-group" data-username="J_C" data-post="5" data-topic="7712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c0e974/48.png" class="avatar"> J_C:</div>
<blockquote>
<p>Just a question: let’s assume that my axial slices are not pure but slightly oblique, should I (and how) reformat so that slicer goes parallale to them?</p>
</blockquote>
</aside>
<p>You can use the Reformat button in the slice viewer menu to rotate the view to the slice plane. Is this what you were looking for?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2cae12a3d54e65461a3379af4b37876d6e9726.png" alt="image" data-base62-sha1="t8d858OrmejGIlLnMtWLuVJtRmS" width="422" height="149"></p>

---

## Post #7 by @J_C (2019-07-29 15:38 UTC)

<p>Yeah… was that easy?<br>
I didn’t found that button and was trying with reformat and transformation module</p>

---

## Post #8 by @fedorov (2019-07-29 15:45 UTC)

<p>You might want to go over the GUI overview here, may save you time down the road: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MainApplicationGUI" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MainApplicationGUI</a></p>

---

## Post #9 by @J_C (2019-07-29 16:41 UTC)

<p>Ok, thanks.<br>
Let’s assume that I’d like to normalize gray level, should I only set the Binwidth or should force normalization along with 2D extraction (there’s normalization too in the script).</p>

---

## Post #10 by @fedorov (2019-07-30 14:07 UTC)

<aside class="quote no-group" data-username="J_C" data-post="9" data-topic="7712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c0e974/48.png" class="avatar"> J_C:</div>
<blockquote>
<p>Let’s assume that I’d like to normalize gray level, should I only set the Binwidth or should force normalization along with 2D extraction (there’s normalization too in the script).</p>
</blockquote>
</aside>
<p>I am afraid I don’t have the answer here. Indeed, normalization of gray level and binning are interrelated, but I don’t think there is a clear recommendation in the community. In this recent paper below we explored a variety of normalizations to better understand MR feature repeatability in the prostate:</p>
<p>Schwier, M., van Griethuysen, J., Vangel, M. G., Pieper, S., Peled, S., Tempany, C., Hugo J W, Kikinis, R., Fennessy, F. M. &amp; Fedorov, A. Repeatability of Multiparametric Prostate MRI Radiomics Features. <em>Sci. Rep.</em> <strong>9,</strong> 9441 (2019). <a href="https://www.nature.com/articles/s41598-019-45766-z" class="inline-onebox">Repeatability of Multiparametric Prostate MRI Radiomics Features | Scientific Reports</a></p>
<p>If you have a similar test-retest dataset for your application, experimentation with achieving improved repeatability could be one approach to fine-tuning feature extraction parameters.</p>

---
