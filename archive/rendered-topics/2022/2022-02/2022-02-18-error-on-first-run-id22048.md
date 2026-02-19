---
topic_id: 22048
title: "Error On First Run"
date: 2022-02-18
url: https://discourse.slicer.org/t/22048
---

# Error on first Run

**Topic ID**: 22048
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/error-on-first-run/22048

---

## Post #1 by @Trystan (2022-02-18 16:07 UTC)

<p>Hello all,</p>
<p>I’m posting this cry for help on behalf my work colleague who would like to use Slicer for his Medical research work.</p>
<p>On starting Slicer we are presented with this message:</p>
<blockquote>
<p>Graphics capabilities of this computer:<br>
Renderer does not support required OpenGL capabilities</p>
</blockquote>
<p>Which is odd, the laptop computer has an nvidia rtx a4000 graphics card so in theory should be fine.</p>
<p>Running other applications that require 3D hardware appears to work fine too.</p>
<p>Has anyone encountered this before?</p>
<p>Thank you all.</p>

---

## Post #2 by @lassoan (2022-02-18 16:08 UTC)

<p>What operating system does your colleague use?<br>
Is he accessing the computer via remote desktop?</p>

---

## Post #3 by @Trystan (2022-02-18 16:12 UTC)

<p>Hello,</p>
<p>Thank you for reponding.</p>
<p>OS is Windows 10 Enterprise (64-bit) version 20H2<br>
He is accessing the computer directly.</p>

---

## Post #4 by @Trystan (2022-02-18 16:14 UTC)

<p>On start-up this message is displayed.  When I click on show details, I am presented with the message I originally posted.   It’s like Slicer is not able to take advantage of the graphics card?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f40758156b1078dfefe5b00d2b565ceb90c40d7.jpeg" data-download-href="/uploads/short-url/4ssU4nrUmD2qMtVKZZLB9LRxfef.jpeg?dl=1" title="Err" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f40758156b1078dfefe5b00d2b565ceb90c40d7_2_690x143.jpeg" alt="Err" data-base62-sha1="4ssU4nrUmD2qMtVKZZLB9LRxfef" width="690" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f40758156b1078dfefe5b00d2b565ceb90c40d7_2_690x143.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f40758156b1078dfefe5b00d2b565ceb90c40d7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f40758156b1078dfefe5b00d2b565ceb90c40d7.jpeg 2x" data-dominant-color="F0F0EB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Err</span><span class="informations">767×160 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-02-18 16:16 UTC)

<p>What is the CPU brand and model?</p>

---

## Post #6 by @Trystan (2022-02-18 16:18 UTC)

<p>Graphics: NVIDIA Quadro RTX 4000 4.0 GB</p>
<p>Computer: Dell Precision 7760 laptop</p>

---

## Post #7 by @lassoan (2022-02-18 16:35 UTC)

<p>This laptop was released a year or so ago, so Slicer can run on it. Configure the graphics settings so the Slicer can access the GPU (not the integrated graphics). If that does not help then maybe its driver configuration is messed up - try to install the latest drivers.</p>
<p>If these don’t help then try if <a href="https://www.paraview.org/">Paraview</a> (a scientific visualization application that uses the same libraries - VTK and Qt - as Slicer) works well or have the same issue.</p>
<p>Just as an experiment, you can try to use a software renderer as described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start" class="inline-onebox">Get Help — 3D Slicer documentation</a></p>

---

## Post #8 by @Trystan (2022-02-18 16:53 UTC)

<p>Thank you Andras, i’ll pass this information on to my colleague and report back.</p>

---
