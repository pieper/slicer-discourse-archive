# Lateral Ventricles of the Brain

**Topic ID**: 29763
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/lateral-ventricles-of-the-brain/29763

---

## Post #1 by @elliotw4 (2023-06-01 00:08 UTC)

<p>I’m currently trying to export STL models of the lateral ventricles of the brain of various sizes: enlarged, average, and slit. Almost all of my smaller or slit ventricle models have some kind of tissue (I believe choroid plexus) or are collapsed in the inferior horns, which makes using the threshold tool in segment editing nearly impossible. This can be seen circled in red in my first picture.</p>
<p>Currently I am using the wand tool in the legacy editor mode and going through these MRIs slide by slide, which takes a long time and produces subpar results (third picture) that I later have to fix in Rhino or Meshmixer.</p>
<p>Does anyone have experience extracting smaller fluid regions from MRIs? Is there a tool or extension that would help me better threshold or detect these regions?</p>
<p>Thanks in advance,</p>
<p>Elliot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc5a1d53ae0b6e80540316edb2fa351c34ff8400.jpeg" data-download-href="/uploads/short-url/t9MtmdwVWucWmm38sxFY4vqdxFS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc5a1d53ae0b6e80540316edb2fa351c34ff8400_2_269x375.jpeg" alt="image" data-base62-sha1="t9MtmdwVWucWmm38sxFY4vqdxFS" width="269" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc5a1d53ae0b6e80540316edb2fa351c34ff8400_2_269x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc5a1d53ae0b6e80540316edb2fa351c34ff8400_2_403x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc5a1d53ae0b6e80540316edb2fa351c34ff8400_2_538x750.jpeg 2x" data-dominant-color="686B7B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">897×1246 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> (Thresholded region, missing inferior horns circled)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a353ebc7821fd727a2ecd009ebeb9eb43d9f168.png" alt="image" data-base62-sha1="3JQusnvOrYHBtpMW4dtPYHhiylG" width="316" height="136"> (Thresholding parameters for above)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9a298311bd156137fb610e6c03eda426cb4e346.jpeg" data-download-href="/uploads/short-url/xkPBG5n7SaD3llw2SJEni4vgC34.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a298311bd156137fb610e6c03eda426cb4e346_2_315x375.jpeg" alt="image" data-base62-sha1="xkPBG5n7SaD3llw2SJEni4vgC34" width="315" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a298311bd156137fb610e6c03eda426cb4e346_2_315x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a298311bd156137fb610e6c03eda426cb4e346_2_472x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a298311bd156137fb610e6c03eda426cb4e346_2_630x750.jpeg 2x" data-dominant-color="676A7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1034×1227 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> (Model using legacy editor wand tool)</p>

---
