---
topic_id: 42421
title: "Unable To See Slicer Autoscoper In Extensions"
date: 2025-04-03
url: https://discourse.slicer.org/t/42421
---

# Unable to see slicer autoscoper in extensions

**Topic ID**: 42421
**Date**: 2025-04-03
**URL**: https://discourse.slicer.org/t/unable-to-see-slicer-autoscoper-in-extensions/42421

---

## Post #1 by @Melanie (2025-04-03 10:42 UTC)

<p>I am unable to see slicer autoscoper in my extensions.</p>
<p>Slicer version Slicer-5.9.0-2025-04-01-macosx-amd64 (Preview)<br>
Mac<br>
Hardware : MacBook Pro 2020 M1<br>
OS - macOS Sonoma 14.5 (23F79)</p>
<p>Could you pls advise</p>

---

## Post #2 by @Amy_Morton (2025-04-03 14:14 UTC)

<p>Hi Melanie, it’s awesome to see your interest in SAM. Are you able to instead install the newest stable <a href="https://download.slicer.org/bitstream/67c53d1129825655577d0b13" rel="noopener nofollow ugc">Slicer release</a> rather than preview?</p>
<p>Regardless, I’ll investigate why you may not see SAM on the index with 5.9.0 (perhaps you could add a screenshot of your screen which captures your search results?)</p>

---

## Post #3 by @Melanie (2025-04-03 18:04 UTC)

<p>Hi <a class="mention" href="/u/amy_morton">@Amy_Morton</a><br>
Pls see below<br>
I. have tried with the stable version, same results</p>
<p>Screenshot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2eb8efeb542304963a6fa2a8345a5bd2e191588.jpeg" data-download-href="/uploads/short-url/yEYefdFfOGfJh9vAf0Pwgi5Lrew.jpeg?dl=1" title="Screenshot 2025-04-03 at 11.31.54 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2eb8efeb542304963a6fa2a8345a5bd2e191588_2_690x430.jpeg" alt="Screenshot 2025-04-03 at 11.31.54 PM" data-base62-sha1="yEYefdFfOGfJh9vAf0Pwgi5Lrew" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2eb8efeb542304963a6fa2a8345a5bd2e191588_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2eb8efeb542304963a6fa2a8345a5bd2e191588_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2eb8efeb542304963a6fa2a8345a5bd2e191588_2_1380x860.jpeg 2x" data-dominant-color="CDCDD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-03 at 11.31.54 PM</span><span class="informations">1920×1199 83.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I search up extensions on web, through my slicer extension manager , I can only see a Linux version of Autoscope</p>
<p>Thanks</p>

---

## Post #4 by @Amy_Morton (2025-04-03 18:26 UTC)

<p>Sorry about that, it’s not you! <a href="https://extensions.slicer.org/catalog/All/30822/macosx?q=auto" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a> is in fact missing the macosx SlicerAutoscoperM extension. We’re on it!</p>

---

## Post #5 by @Amy_Morton (2025-04-03 20:01 UTC)

<p>Sadly, I have some disappointing news.</p>
<p>Considering that (1) CUDA is not available on macOS and (2) OpenCL is also deprecated (see <a href="https://developer.apple.com/opencl/" rel="noopener nofollow ugc">1</a> and <a href="https://github.com/BrownBiomechanics/Autoscoper/issues/43#issuecomment-1284372065" rel="noopener nofollow ugc">2</a>), we cannot expect the extension to be available on macOS.</p>
<p>I know this is not the reply you were hoping for.. do you have access to a windows machine on which you may access SAM?</p>

---

## Post #6 by @Amy_Morton (2025-04-21 14:20 UTC)

<p><a class="mention" href="/u/melanie">@Melanie</a> Please visit the extension index again and test for our mac enabled slicerautoscoperM extension efforts!</p>

---

## Post #7 by @Melanie (2025-04-21 16:48 UTC)

<p>Thank you so much <a class="mention" href="/u/amy_morton">@Amy_Morton</a><br>
Will check this out right away</p>

---
