# Airway Segmentation is working fine on sample CT but raises an error when running on my CT 

**Topic ID**: 30235
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/airway-segmentation-is-working-fine-on-sample-ct-but-raises-an-error-when-running-on-my-ct/30235

---

## Post #1 by @Matteboo (2023-06-26 14:55 UTC)

<p>Hello,<br>
As I say in the title I’m using a toolbox (airway segmentation). When I use it on a CT from “Sample Data” the toolbox runs fine and give the appropriate results. However, when I try to run it on my CTs I have an error. (the program doesn’t finish and I don’t have a result)<br>
The error is <strong>AttributeError: ‘NoneType’ object has no attribute ‘SetTag’</strong> if that helps</p>
<p>Has anyone ever run into a similar issue ?<br>
Is there something I should check about my CTs ?<br>
Thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @rbumm (2023-06-26 17:10 UTC)

<p>Hello,</p>
<p>Which airway segmentation are you using?</p>
<p>This</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8fe363d6269f65ffa15e9c4231610ecbb77e6b2.png" data-download-href="/uploads/short-url/uXBMmuGabYVw0ScJ0Vrm1qGYzCO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8fe363d6269f65ffa15e9c4231610ecbb77e6b2_2_289x500.png" alt="image" data-base62-sha1="uXBMmuGabYVw0ScJ0Vrm1qGYzCO" width="289" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8fe363d6269f65ffa15e9c4231610ecbb77e6b2_2_289x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8fe363d6269f65ffa15e9c4231610ecbb77e6b2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8fe363d6269f65ffa15e9c4231610ecbb77e6b2.png 2x" data-dominant-color="CFCFE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">290×501 60.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>is unstable and has not been maintained for a long time.</p>
<p>Try the LungCTSegmenter from the LungCTAnalyzer package.<br>
It has an airway segmentation option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e868f10df6a2348da32398c9b3298c318fcdeb7.png" data-download-href="/uploads/short-url/i3is2AlAGW9uVeTlDi4yXroe98P.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e868f10df6a2348da32398c9b3298c318fcdeb7.png" alt="image" data-base62-sha1="i3is2AlAGW9uVeTlDi4yXroe98P" width="298" height="499" data-dominant-color="EFEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">317×531 18.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
