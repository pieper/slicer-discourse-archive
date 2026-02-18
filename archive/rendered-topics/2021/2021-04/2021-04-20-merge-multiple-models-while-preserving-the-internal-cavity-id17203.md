# Merge multiple models while preserving the internal cavity

**Topic ID**: 17203
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/merge-multiple-models-while-preserving-the-internal-cavity/17203

---

## Post #1 by @lazymark2 (2021-04-20 12:28 UTC)

<p>Hi everyone, new to slicer 3D here.<br>
Recently I want to prepare a mandible model for 3D printing.<br>
Now I have a mandibular dentition model with root canal system existed as internal cavity (hollow):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a07aa5d8a2efe02d917355b9b0cdb66c107a94b.jpeg" data-download-href="/uploads/short-url/jH4jtCG5YTA4aIBDhySFNMKmvfZ.jpeg?dl=1" title="model_extraction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a07aa5d8a2efe02d917355b9b0cdb66c107a94b_2_690x333.jpeg" alt="model_extraction" data-base62-sha1="jH4jtCG5YTA4aIBDhySFNMKmvfZ" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a07aa5d8a2efe02d917355b9b0cdb66c107a94b_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a07aa5d8a2efe02d917355b9b0cdb66c107a94b_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a07aa5d8a2efe02d917355b9b0cdb66c107a94b_2_1380x666.jpeg 2x" data-dominant-color="929290"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model_extraction</span><span class="informations">1715×828 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and a mandible model without any teeth:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c00ffea504fb4b363737c5985302322fa07bdba6.png" alt="2021-04-20 15-00-23屏幕截图" data-base62-sha1="rp3WsdwzvN6kr3EWqRXPdwdehKu" width="300" height="241"></p>
<p>Then the desired result is to merge these two models, while preserving the internal root canal system.</p>
<p>But when I try to use the logical operator of segment editor or merge models method in 3D slicer, the internal cavity will disappear in the intersect part of merged model. So I am wondering if there is any method that could preserve the internal root canal system and what should I do to achieve this goal. Any help would be appreciated!</p>

---

## Post #2 by @mikebind (2021-04-20 23:13 UTC)

<p>I would suggest that you make a copy of the hollow teeth and fill the root canal systems in the copy (could use “Smoothing → Closing (fill holes)”).  Then you can use logical subtraction to subtract the filled teeth from mandible.  Next, delete the filled tooth copies. Now the original (unfilled) teeth should fit into the mandible gaps without the root canal systems being filled.</p>

---

## Post #3 by @mikebind (2021-04-21 16:18 UTC)

<p>I thought about this a little more and have another suggestion.  If the outer surface of each tooth is closed (i.e. the root canal cavity does not extend to an opening at the bottom of the tooth), then you could use your initial process (without making copies of the teeth and filling them) and just use the “Islands” tool and “Keep largest island” on the mandible segment.  As long as the root canal systems don’t have openings, the bits you don’t want should be separate islands and will disappear if you only keep the largest island.  This method is simpler and more efficient if it will work for you.</p>

---
