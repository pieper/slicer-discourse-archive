---
topic_id: 4648
title: "Dose Accumulation Weighting Slicerrt"
date: 2018-11-06
url: https://discourse.slicer.org/t/4648
---

# Dose accumulation weighting SlicerRT

**Topic ID**: 4648
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/dose-accumulation-weighting-slicerrt/4648

---

## Post #1 by @Lowey (2018-11-06 01:56 UTC)

<p>Hi there,</p>
<p>I am using SlicerRT (v4.8) to try and accumulate dose for a 30 fraction treatment.</p>
<p>I am hoping someone may be able to explain how SlicerRT dose accumulation weights dose distributions. It seems to NOT be a simple linear weighting. For example, if I weight a single dose distribution with a factor of 1.0 and calculate DVH parameters I get a different result than if I weight the same single dose distribution with a factor of 0.5 (and then multiple the DVH parameters by 2).</p>
<p>Probably I’m missing something obvious but would appreciate any help!</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-11-06 02:31 UTC)

<p>A simple linear weighing is performed. Each dose volume is resampled to the reference volume node’s geometry, multiplied by the specified factor, and added to the accumulated dose volume.</p>

---

## Post #3 by @Lowey (2018-11-06 02:41 UTC)

<p>Thanks for your reply!</p>
<p>Your reply makes sense of course. But for some reason I still get differences when doing the above,</p>
<p><em>If I weight a single dose volume with a factor of 1.0 and calculate DVH parameters I get a different result than if I weight the same single dose volume with a factor of 0.5 (and then manually multiple the DVH parameters by 2).</em></p>
<p>I also keep the reference dose volume and structures constant. So I’m a little perplexed as to why I get the differences. In any case, if it’s not a known bug I will re-examine my method.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2018-11-06 02:44 UTC)

<p>What DVH parameters you multiply by 2? How different the results are?</p>

---

## Post #5 by @cpinter (2018-11-06 14:35 UTC)

<p>You cannot simply scale the DVH parameters (V20, D95 etc).Dose accumulation involves adding up different dose distributions that, when summed and weighted, will look quite different than any of the individual input dose accumulations. At the same time, you use the same structure set, so the boundaries may be different. So you cannot expect to be able to just linearly scale up the metrics.</p>

---

## Post #6 by @Lowey (2018-11-06 20:30 UTC)

<p>Thank you for your replies.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a><br>
Of course one cannot simply scale DVH parameters when using different dose distributions.</p>
<p>But, I’m confused as to why there would be a difference in DVH parameters (D98 etc.) for one single dose distribution when it is weighted with a factor of 1.0 and for the same single dose distribution when it is weighted with a factor of 0.03 with resulting DVH parameters manually multiplied by 33.333</p>
<p>Note the same structure set and dose distribution is being used both times so boundaries are not different.</p>
<p>For example,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38c37bd50339e4971a0f0d24bc045d7aadc23398.png" data-download-href="/uploads/short-url/869yJIO0wcLR94Z5L6JkbvhwGZW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38c37bd50339e4971a0f0d24bc045d7aadc23398.png" alt="image" data-base62-sha1="869yJIO0wcLR94Z5L6JkbvhwGZW" width="690" height="167" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×194 4.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then the DVH parameters are,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b737acd6edff6316f2fe2f656c862f6f1d21eb06.png" data-download-href="/uploads/short-url/q8OEXc6Wuad8g3dvOYO8rkRZ4hM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b737acd6edff6316f2fe2f656c862f6f1d21eb06.png" alt="image" data-base62-sha1="q8OEXc6Wuad8g3dvOYO8rkRZ4hM" width="690" height="379" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">740×407 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But if I do,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cdc207c8b61c2179b762b54d6737b848ff02d13.png" data-download-href="/uploads/short-url/fx1byYlrkncRdFFboTbFM4gAgkr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cdc207c8b61c2179b762b54d6737b848ff02d13.png" alt="image" data-base62-sha1="fx1byYlrkncRdFFboTbFM4gAgkr" width="690" height="164" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">805×192 4.16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then the DVH parameters are,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a7e27652ba8bfeac1404345e144009ff913784.png" data-download-href="/uploads/short-url/O24RHJFicwFdwpm4n3eE4QiAIs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a7e27652ba8bfeac1404345e144009ff913784.png" alt="image" data-base62-sha1="O24RHJFicwFdwpm4n3eE4QiAIs" width="690" height="418" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">721×437 11.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Mean, Max and min dose all seem fine but when I multiply the D98s by 33.333 I get significant differences. E.g.</p>
<p>Using the 0.03 ‘accumulated dose’ - CTV66 D98 = 1.90249<br>
Using the 1 ‘accumulated dose’ - CTV66 D98 = 64.5473</p>
<p>1.90249 x 33.333 = 63.41633 and NOT 64.5473</p>
<p>Am I just missing something obvious with D98s or is this due to rounding?</p>
<p>Many thanks!</p>

---

## Post #7 by @lassoan (2018-11-06 23:55 UTC)

<p>By downscaling the dose by a factor of 33.3x, computing the histogram, and then upscaling the result, you essentially scale up histogram quantization error by 33.3x.<br>
To maintain error at the same level, despite of this aggressive scaling, you need to set a smaller histogram bin width (=DVH step size). You can get current step size by opening the Python console (Ctrl-3) and typing:</p>
<pre><code>slicer.modules.dosevolumehistogram.logic().GetStepSize()
</code></pre>
<p>To set a new value, type for example this:</p>
<pre><code>slicer.modules.dosevolumehistogram.logic().SetStepSize(0.006)</code></pre>

---

## Post #8 by @Lowey (2018-11-07 20:16 UTC)

<p><span class="mention">@Iassoan</span></p>
<p>Thank you kindly, that has resolved my issue</p>

---
