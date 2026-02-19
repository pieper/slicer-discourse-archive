---
topic_id: 31029
title: "Alpaca Bilateral Symmetry"
date: 2023-08-07
url: https://discourse.slicer.org/t/31029
---

# ALPACA + Bilateral Symmetry

**Topic ID**: 31029
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/alpaca-bilateral-symmetry/31029

---

## Post #1 by @AaronHardgrave (2023-08-07 16:39 UTC)

<p>I am using Geometric Morphometrics to discern differences across life stages of a single species. I used PseudoLMGenerator with a plane down the center of my vertebra and used ALPACA to transfer landmarks across specimens to capture whole vertebrae morphology. Would I still need to run a program like ‘bilat.symmetry’ in <em>geomorph</em> to remove asymmetry or would that be redundant?</p>
<p>If I need to remove asymmetry, what do you recommend? I have seen in other topics posted in this forum that the ‘bilat.symmetry’ function requires replicates but is also typically used for manual landmarking.</p>
<p>Thanks,</p>
<p>Aaron</p>

---

## Post #2 by @agporto (2023-08-07 20:16 UTC)

<aside class="quote no-group" data-username="AaronHardgrave" data-post="1" data-topic="31029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aaronhardgrave/48/67100_2.png" class="avatar"> AaronHardgrave:</div>
<blockquote>
<p>bilat.symmetry</p>
</blockquote>
</aside>
<p>Hi Aaron,<br>
ALPACA will simply transfer the landmarks. So, it will not remove asymmetry. You would have to do it downstream.<br>
I am not too familiar with the bilat.symmetry function in geomorph, but my understanding is that you wouldn’t necessarily need replicates. It is an optional argument.<br>
Hope that helps<br>
Arthur</p>

---

## Post #3 by @AaronHardgrave (2023-08-07 20:56 UTC)

<p>Thank you for the quick response Dr. Porto! You and the rest of the SlicerMorph team have been super helpful.</p>
<p>Okay, so I set up my initial PseudoLandmark template to look like the example (Figure 1b) in the <a href="https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13669" rel="noopener nofollow ugc">SlicerMorph publication</a>. I was assuming the symmetry will remain while the landmarks get translated between specimens but now it seems like doing it downstream makes the most sense.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9945eb821db24314e97a7980a1156586d14a93e.jpeg" data-download-href="/uploads/short-url/v2Nuwyt1a4JDSNv0n6UWBT4teua.jpeg?dl=1" title="Screenshot 2023-08-07 at 4.42.36 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9945eb821db24314e97a7980a1156586d14a93e_2_345x249.jpeg" alt="Screenshot 2023-08-07 at 4.42.36 PM" data-base62-sha1="v2Nuwyt1a4JDSNv0n6UWBT4teua" width="345" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9945eb821db24314e97a7980a1156586d14a93e_2_345x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9945eb821db24314e97a7980a1156586d14a93e_2_517x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9945eb821db24314e97a7980a1156586d14a93e_2_690x498.jpeg 2x" data-dominant-color="BEC26B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-07 at 4.42.36 PM</span><span class="informations">886×640 82.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2023-08-07 20:58 UTC)

<p>The purpose of the symmetry plane in PseudoLMGenerator is to prepare the dataset in a way that’s suitable to do symmetry analysis.</p>
<p>Whether you need replicates or not depends on what you want to do with the data. if you want to see whether symmetry scores (FA or DA) are different between your groups, you will need to have replicates (as bilat.symmetry will require replicates to calculate significance levels). If your goal is to just us the symmetric component of the shape for downstream analysis (like PCA), then you do not need the replicates.</p>

---

## Post #5 by @AaronHardgrave (2023-08-07 20:59 UTC)

<p>Perfect! That’s exactly what I was looking for. Thank you Murat</p>

---
