---
topic_id: 28527
title: "Construct A Model Of Coronaries From Ccta Scans"
date: 2023-02-17
url: https://discourse.slicer.org/t/28527
---

# Construct a model of coronaries from CCTA scans

**Topic ID**: 28527
**Date**: 2023-02-17
**URL**: https://discourse.slicer.org/t/construct-a-model-of-coronaries-from-ccta-scans/28527

---

## Post #1 by @smoudour (2023-02-17 11:28 UTC)

<p>Hi,<br>
I’m following the exact directions in the video and I get a weird ‘not-responding’ problem while I press ctrl+left click. It loads for some time (sometimes presenting ‘not responding’ status, and then program doesn’t crash but I am not getting any 3d model. When monitoring for cpu/gpu use, it does use 100% of my cpu. I tried explicitly telling Slicer-real.exe to use my gpu (GTX1060 Ti mobile) for the computations in case its a computation problem but still get nothing. Maybe it has something to do with python? Any ideas? Also, I cannot locate Sandbox extension in the extensions tab – I’m using slicer version 4.11.20210226.</p>
<p>Also - in another tone - I would like to ask if there is any updated tutorial for using vmtk in python explicitly.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-03-21 18:23 UTC)

<aside class="quote no-group" data-username="smoudour" data-post="1" data-topic="28527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smoudour/48/18451_2.png" class="avatar"> smoudour:</div>
<blockquote>
<p>It loads for some time (sometimes presenting ‘not responding’ status, and then program doesn’t crash but I am not getting any 3d model.</p>
</blockquote>
</aside>
<p>Local thresholding effect can work very well for cases when the vessel has strong contrast compared to surrounding regions, but may not work for more challending cases. If you use Ctrl+click starts the computation and depending on your settings and where you click and the quality of the image, indeed, the result may be that nothing can be segmented there. If adjusting parameters and click position does not help then you can use other segmentation tools, such as the <code>Grow from seeds</code> effect.</p>

---

## Post #4 by @smoudour (2023-03-22 14:49 UTC)

<p>Hi Andras and thanks for the reply. After messing around a bit with different versions and different tools I manged to kind of reach my goal. Specifically what I’m trying to do is <strong>construct a model of the three main coronary arteries from CCTA scans</strong>, which proved to be a rather difficult task.</p>
<p>For anyone trying the same, the most succesfull workflow until now has been the one below:</p>
<p><strong>ROI extraction with oversampling</strong> → <strong>VMTKvesselness filtering</strong> → Segmentation using <strong>local thresholding</strong> → Isolation of coronaries using <strong>Islands tool</strong> → <strong>VMTKextract centerline</strong> with auto-detection of centerline endpoints.</p>
<p>Using VMTK level set segmentation didn’t work for me because I want to extract the coronary arteries <em>with</em> all their bifurcations.</p>
<p>Currently my question is how exactly is the torsion value calculated for each centerline segment and if there is a way to calculate bifurcation angles using the python console.</p>

---
