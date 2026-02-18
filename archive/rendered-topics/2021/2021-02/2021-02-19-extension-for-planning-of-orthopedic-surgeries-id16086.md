# Extension for planning of orthopedic surgeries?

**Topic ID**: 16086
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/extension-for-planning-of-orthopedic-surgeries/16086

---

## Post #1 by @MCMF (2021-02-19 14:18 UTC)

<p>Hello</p>
<p>I may start to develop an extension for planning of orthopedic surgeries of the lower extremities.<br>
Focus will be on the hip an knee joint. One important feature will be the definition of bone coordinate systems based on bony landmarks to transform the reconstructed bones and their corresponding (sub)volume data from the CT coordinate system into a “neutral” joint alignment.</p>
<p>Are there any extensions that could serve as basis or inspiration for such project.</p>
<p>Kind regards<br>
MCMF</p>

---

## Post #2 by @lassoan (2021-02-19 14:27 UTC)

<p>There are Slicer-based commercial systems that do this, but I don’t think there is much in open-source extensions.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/Q3DC">Q3DC module</a> in SlicerCMF does something similar for cranial procedures, but it is quite old, so it does not use current Slicer markups infrastructure.</p>
<p>I would recommend to look at methods for establishing bone coordinate systems that are commonly used clinically (and validated on many thousands of patients) and ask here for help if you are not sure how exactly to implement them in Slicer.</p>

---

## Post #3 by @MCMF (2021-02-19 17:32 UTC)

<p>Hi Andras</p>
<p>Thanks for the fast reply. Do you mind sharing links to the commercial systems?</p>
<p>I already figured out which bone coordinate systems would be used.<br>
My concern is rather a good example or basis for the implementation as extension.</p>
<p>Kind regards<br>
MCMF</p>

---

## Post #4 by @lassoan (2021-02-19 19:06 UTC)

<p>The commercial systems that I know of have not been announced publicly, so there is no further information available. Most often companies do not even acknowledge that they use Slicer internally even after the product is released, which demonstrates that the Slicer license is very commercial-friendly (no attribution is required) and the user interface layer can be customized so much that users don’t even realize that they use Slicer. But unfortunately this also means that there are very <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#d-slicer-based-products">few Slicer-based products</a> that we can use as a reference.</p>
<p>If you describe what you want to achieve then we may be able to provide links to relevant examples. Are you thinking about navigated surgery (optical tracked tools and bones), 3D-printed surgical guides, or robotic procedures?</p>

---

## Post #5 by @MCMF (2021-02-22 08:25 UTC)

<p>Hi Andras</p>
<p>The main goal would be preoperative planning with the reconstruction of biomechanical parameters based either on the contralateral leg or anthropometric values, in case the contralateral side cannot be used as reference.</p>
<p>Surgical guides are one option for the intraoperative transfer of the preoperative plan. However, a common CAD software might be used for the design of the guides rather than 3D Slicer.</p>
<p>Kind regards<br>
MCMF</p>

---

## Post #6 by @lassoan (2021-02-22 13:25 UTC)

<aside class="quote no-group" data-username="MCMF" data-post="5" data-topic="16086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f17d59/48.png" class="avatar"> MCMF:</div>
<blockquote>
<p>The main goal would be preoperative planning with the reconstruction of biomechanical parameters based either on the contralateral leg or anthropometric values, in case the contralateral side cannot be used as reference.</p>
</blockquote>
</aside>
<p>This sounds interesting. Let us know if we can help with anything.</p>
<aside class="quote no-group" data-username="MCMF" data-post="5" data-topic="16086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f17d59/48.png" class="avatar"> MCMF:</div>
<blockquote>
<p>Surgical guides are one option for the intraoperative transfer of the preoperative plan. However, a common CAD software might be used for the design of the guides rather than 3D Slicer.</p>
</blockquote>
</aside>
<p>We have recently started to develop an <a href="https://github.com/lassoan/SlicerBoneReconstructionPlanner">extension for automatic 3D-printable surgical cutting guide designer module</a>. It already looks quite promising - see for example this guide created for cutting the fibula:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1efe6c08ed1e50a80b0300ea0d6d77f290e477c.png" data-download-href="/uploads/short-url/tXbMdhXF8uXCWEJCyBmqxlJJPzK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1efe6c08ed1e50a80b0300ea0d6d77f290e477c_2_597x500.png" alt="image" data-base62-sha1="tXbMdhXF8uXCWEJCyBmqxlJJPzK" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1efe6c08ed1e50a80b0300ea0d6d77f290e477c_2_597x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1efe6c08ed1e50a80b0300ea0d6d77f290e477c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1efe6c08ed1e50a80b0300ea0d6d77f290e477c.png 2x" data-dominant-color="9696C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">836×699 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/371079be12c5d69bccbb2d065e1722477174d614.png" data-download-href="/uploads/short-url/7R7yH4og7SaMElRxcj3I4ghWM8A.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371079be12c5d69bccbb2d065e1722477174d614_2_690x133.png" alt="image" data-base62-sha1="7R7yH4og7SaMElRxcj3I4ghWM8A" width="690" height="133" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371079be12c5d69bccbb2d065e1722477174d614_2_690x133.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371079be12c5d69bccbb2d065e1722477174d614_2_1035x199.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/371079be12c5d69bccbb2d065e1722477174d614.png 2x" data-dominant-color="E8E2E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1105×213 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(<a href="https://github.com/lassoan/SlicerBoneReconstructionPlanner/issues/26">source</a>)</p>
<p>If you were interested in going beyond what you can do with commercial packages then you are welcome to join the project.</p>

---
