---
topic_id: 46227
title: "Alpaca Error Version 5 10 0 Stable"
date: 2026-02-20
url: https://discourse.slicer.org/t/46227
---

# ALPACA error; Version 5.10.0 (stable)

**Topic ID**: 46227
**Date**: 2026-02-20
**URL**: https://discourse.slicer.org/t/alpaca-error-version-5-10-0-stable/46227

---

## Post #1 by @juliangallaun (2026-02-20 09:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322.jpeg" data-download-href="/uploads/short-url/4YSpoNet2TFp6ygLVtfOoaJQ84q.jpeg?dl=1" title="Screenshot_alpaca_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_690x247.jpeg" alt="Screenshot_alpaca_error" data-base62-sha1="4YSpoNet2TFp6ygLVtfOoaJQ84q" width="690" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_690x247.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_1035x370.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_1380x494.jpeg 2x" data-dominant-color="272525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_alpaca_error</span><span class="informations">1525×548 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><span lang="EN-GB">Hello all,</span></p>
<p><span lang="EN-GB">  </span></p>
<p><span lang="EN-GB">I have a problem opening the ALPACA extension, with the stable version of 3D slicer 5.10.0 .</span></p>
<p><span lang="EN-GB">The error code says, it can’t find a certain file. I should have installed all additional extensions to run the extension. I reinstalled the extension again, without solving the problem. On the version 5.8.1 ALPACA works on my device.</span></p>
<p><span lang="EN-GB">Thank you for your help and advice.</span></p>

---

## Post #2 by @drnoorfatima (2026-02-20 10:29 UTC)

<p>Hi!</p>
<p>The issue is a missing itk Python package in Slicer 5.10.0’s environment. Open the Python Interactor in Slicer and run:</p>
<p>slicer.util.pip_install(‘itk’)</p>
<p>Then restart Slicer and try opening ALPACA again. That should fix it!</p>

---

## Post #3 by @juliangallaun (2026-02-20 10:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08.jpeg" data-download-href="/uploads/short-url/A5kWywGOC3iEFaiaBGHRun4Pxfq.jpeg?dl=1" title="Screenshot_alpaca_error1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_690x275.jpeg" alt="Screenshot_alpaca_error1" data-base62-sha1="A5kWywGOC3iEFaiaBGHRun4Pxfq" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_690x275.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_1035x412.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_1380x550.jpeg 2x" data-dominant-color="282524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_alpaca_error1</span><span class="informations">1505×601 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did run the command and this was the reply. Nothing changed regarding the problem.</p>

---

## Post #4 by @muratmaga (2026-02-20 16:43 UTC)

<p>It appears your slicer 5.10 installation is problematic for some reason. E.g., the real issue is the first error (Application Does Not exist).</p>
<p>I suggest freshly installing it to a new place (like your desktop), install SlicerMorph and retry.</p>

---

## Post #5 by @juliangallaun (2026-02-20 17:00 UTC)

<p>Ok, I did that and got the exact same error as the first time.</p>
<p>I did save it on the desktop as you suggested.</p>

---

## Post #6 by @muratmaga (2026-02-20 19:15 UTC)

<p>what happens when you do the <code>pip_install(“itk”)</code></p>

---
