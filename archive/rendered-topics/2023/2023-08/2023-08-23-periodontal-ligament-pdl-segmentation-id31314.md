# Periodontal ligament (PDL) segmentation

**Topic ID**: 31314
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/periodontal-ligament-pdl-segmentation/31314

---

## Post #1 by @balakonvict (2023-08-23 11:14 UTC)

<p>I have successfully segmented a tooth and maxilla from my imaging data. However, I am facing challenges with segmenting the periodontal ligament (PDL). I attempted to use shelling techniques to create the PDL, but unfortunately, the shelling process was not successful, possibly due to complexities in the geometry. Consequently, I am seeking alternative methods to accurately generate the PDL without relying on shelling.</p>
<p>If anyone has experience or expertise in effectively segmenting the periodontal ligament or can suggest alternative approaches, I would greatly appreciate your assistance. My goal is to ensure a precise representation of the PDL within the segmented tooth and maxilla model. Thank you in advance for any guidance, suggestions, or techniques you can provide.</p>

---

## Post #2 by @lassoan (2023-08-23 11:38 UTC)

<p>Could attach a few images that shows the kind of images that you work with, the structure that you try to segment, and your results so far? It may help us to give you some hints.</p>

---

## Post #3 by @balakonvict (2023-08-24 05:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af54d5e124443f6fb3a1294af149a35f5a41f5bd.png" data-download-href="/uploads/short-url/p13jCxtgWlvt7qlPKw0iserl0D3.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af54d5e124443f6fb3a1294af149a35f5a41f5bd_2_488x304.png" data-base62-sha1="p13jCxtgWlvt7qlPKw0iserl0D3" alt="image.png" width="488" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af54d5e124443f6fb3a1294af149a35f5a41f5bd_2_488x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af54d5e124443f6fb3a1294af149a35f5a41f5bd_2_732x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af54d5e124443f6fb3a1294af149a35f5a41f5bd_2_976x608.png 2x" data-dominant-color="737373"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1003×624 30.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35f094cead887d0734bdc02f84c26820ab87463a.png" data-download-href="/uploads/short-url/7HaKqWPugxw1GEyTuy5b7DIarNw.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35f094cead887d0734bdc02f84c26820ab87463a_2_488x346.png" data-base62-sha1="7HaKqWPugxw1GEyTuy5b7DIarNw" alt="image.png" width="488" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35f094cead887d0734bdc02f84c26820ab87463a_2_488x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35f094cead887d0734bdc02f84c26820ab87463a_2_732x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35f094cead887d0734bdc02f84c26820ab87463a.png 2x" data-dominant-color="424242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">933×661 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Having successfully extracted both the maxilla model and 16 individual teeth from my imaging data, I meticulously closed any gaps or voids within the model structure. My utilization of Blender facilitated a sculpting process that significantly refined and elevated the overall quality of the maxilla model.</p>
<p>Currently, I’m confronted with the task of manually crafting a 0.2mm thick periodontal ligament (PDL) layer that remains consistent across all teeth. Regrettably, the specific PDL thickness I require couldn’t be accurately extracted from the original CT scan data. In light of this, my intention is to manually delineate the PDL layer onto the surfaces of the teeth using appropriate software tools.</p>
<p>I’m seeking insights regarding effective techniques to accomplish this endeavour. I’m particularly interested in understanding if a plausible approach exists for manually generating the PDL layer from the tooth surfaces. Any suggestions, guidance, or expertise in this regard would be immensely valuable.</p>
<p>It’s worth noting that I’m specifically looking for alternative methods that go beyond the conventional options such as shelling, upscaling/downscaling, or utilizing boolean operations. If anyone possesses novel ideas or distinct methodologies to create the PDL manually, I eagerly anticipate the opportunity to benefit from your innovative perspectives and expertise.</p>

---

## Post #4 by @lassoan (2023-08-24 06:56 UTC)

<aside class="quote no-group" data-username="balakonvict" data-post="3" data-topic="31314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/balakonvict/48/15095_2.png" class="avatar"> balakonvict:</div>
<blockquote>
<p>Currently, I’m confronted with the task of manually crafting a 0.2mm thick periodontal ligament (PDL) layer that remains consistent across all teeth. Regrettably, the specific PDL thickness I require couldn’t be accurately extracted from the original CT scan data. In light of this, my intention is to manually delineate the PDL layer onto the surfaces of the teeth using appropriate software tools.</p>
</blockquote>
</aside>
<p>Do you want to extract the shape of the PDL from the CT scan or you are just looking for tools that allow you to paint a thin layer on the tooth surface?</p>
<p>What is the purpose of this? Creating a highly detailed model for one specific case (for example, for 3D visualization for educational purposes) or you would want to do some clinical analysis?</p>

---

## Post #5 by @balakonvict (2023-08-24 07:19 UTC)

<p>I’m looking for tools that let me paint a thin layer on tooth surfaces of 0.2mm thickness for all teeth. After this, I’ll turn these models into CAD files, assemble them, and analyze them using ANSYS. I come from a mechanical engineering background and am researching dental biomechanics as part of my PhD work.</p>

---

## Post #6 by @lassoan (2023-08-24 07:52 UTC)

<p>Since you don’t rely on images and it is hard to represent thin layers as labelmap images, it makes sense to grow the thin layer in mesh representation, from the tooth surface. Extracting the tooth surface areas where you want to grow from should be straightforward (you can easily do it in Slicer, but I guess in Blender or in the CAD software, too). The typical methods for growing layers that you dismissed (shelling, growing, subtracting, etc.) should mostly work. Self-intersection at sharp edges may be a problem but if you have time then you can fix them by local manual editing.</p>
<p>If you want a more automated pipeline then you can implement something similar that is used for cortical thickness measurement (such as in <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferAnalysisPipelineOverview">FreeSurfer</a>), but it would only worth the effort if you had to analyse many cases or you would want to measure the actual PDL thickness.</p>

---

## Post #7 by @Alin_Iacob (2024-11-03 12:32 UTC)

<p>I am pretty much doing something similar and trying to obtain those files. Have you finally obtained them successfully?</p>

---
