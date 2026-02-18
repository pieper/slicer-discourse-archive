# SAM 2 with video support

**Topic ID**: 37717
**Date**: 2024-08-05
**URL**: https://discourse.slicer.org/t/sam-2-with-video-support/37717

---

## Post #1 by @dzenanz (2024-08-05 22:20 UTC)

<p>Meta’s <a href="https://ai.meta.com/blog/segment-anything-2/" rel="noopener nofollow ugc">Segment Anything Model 2</a> was announced last week. Are there any thoughts about its applicability to 3D images?</p>

---

## Post #2 by @mau_igna_06 (2024-08-06 00:56 UTC)

<p>Maybe this is of interest:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://the-decoder.com/oxford-researchers-unveil-medsam-2-an-ai-that-could-change-how-doctors-analyze-medical-images/">
  <header class="source">
      <img src="https://the-decoder.com/resources/favicons/favicon-32x32.png?v=3" class="site-icon" width="" height="">

      <a href="https://the-decoder.com/oxford-researchers-unveil-medsam-2-an-ai-that-could-change-how-doctors-analyze-medical-images/" target="_blank" rel="noopener nofollow ugc" title="12:53PM - 05 August 2024">THE DECODER – 5 Aug 24</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/387;"><img src="https://the-decoder.com/wp-content/uploads/2024/08/MedSAM-2-title-1.png" class="thumbnail" width="690" height="388"></div>

<h3><a href="https://the-decoder.com/oxford-researchers-unveil-medsam-2-an-ai-that-could-change-how-doctors-analyze-medical-images/" target="_blank" rel="noopener nofollow ugc">Oxford researchers unveil MedSAM-2, an AI that could change how doctors...</a></h3>

  <p>Researchers have developed a new AI model called MedSAM-2 that significantly improves the segmentation of 2D and 3D medical images. With just a single manual annotation, it can process entire series of images.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Fernando (2024-08-14 21:09 UTC)

<p>Also this: <a href="https://arxiv.org/abs/2408.03322" class="inline-onebox" rel="noopener nofollow ugc">[2408.03322] Segment Anything in Medical Images and Videos: Benchmark and Deployment</a></p>
<p>With a Slicer module! <a href="https://github.com/bowang-lab/MedSAMSlicer/tree/SAM2" class="inline-onebox" rel="noopener nofollow ugc">GitHub - bowang-lab/MedSAMSlicer at SAM2</a></p>
<div class="youtube-onebox lazy-video-container" data-video-id="kt1WN5BciVg" data-video-title="SAM2 3D Slicer Plugin: Usage" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=kt1WN5BciVg" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/kt1WN5BciVg/maxresdefault.jpg" title="SAM2 3D Slicer Plugin: Usage" width="690" height="388">
  </a>
</div>


---

## Post #4 by @dzenanz (2024-08-14 21:18 UTC)

<p>I was aware of MedSAMSlicer, I didn’t notice they have a <code>SAM2</code> branch <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"> Thank you for pointing it out.</p>

---

## Post #5 by @Fernando (2024-08-14 21:22 UTC)

<p>They uploaded their preprint five days after the <a href="https://arxiv.org/abs/2408.00714" rel="noopener nofollow ugc">SAM 2 preprint</a>…</p>

---

## Post #6 by @lassoan (2024-08-15 09:09 UTC)

<p>Many people celebrate performance of SAM when they see some demo videos, but they don’t realize that they are looking at trivial segmentation tasks (e.g., kidney segmentation on a single CT slice where no similar structures are nearby) and they don’t notice when the segmentation spectacularly fails on moderately difficult tasks (such as missing half of the liver). See for example <a class="mention" href="/u/alireza">@alireza</a>’s recent experiments with SAM2 for 3D medical image segmentation - with quite poor results: <a href="https://www.linkedin.com/feed/update/urn:li:activity:7223849584127619072/" class="inline-onebox">Alireza Sedghi on LinkedIn: SAM 2 Released: 3D Medical Image Segmentation Solved? I got a screen… | 18 comments</a></p>
<p>SAM performance is remarkable when used interactively on 2D images of everyday objects, the well-engineered web demos make SAM easily available for the crowds, and open-sourcing the model is examplary. It is also nice that it is a general-purpose tool that could be made to work on any imaging modality to interactively segment any structure. However, 99% users will not want any interactivity in the segmentation, and don’t want to work slice-by-slice; they just want fast, fully automatic 3D segmentation for free - and they can already get it via TotalSegmentator, MONAIAuto3DSeg, DentalSegmentator, etc. So, my overall impression is that considering their clinical relevance and impact, SAM-based models may not deserve as much attention as they are getting.</p>

---

## Post #7 by @dzenanz (2024-08-15 13:48 UTC)

<blockquote>
<p>TotalSegmentator, MONAIAuto3DSeg, DentalSegmentator, etc.</p>
</blockquote>
<p>Ground truth for training them needs to come from somewhere. SAM is a great interactive segmentation tool.</p>

---

## Post #8 by @lassoan (2024-08-15 14:56 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="7" data-topic="37717">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>SAM is a great interactive segmentation tool</p>
</blockquote>
</aside>
<p>Yes, and this is its main limitation: it requires interaction. If the user needs to interact with the image for several (potentially tens of) seconds then the value is questionable, because the clinician can make the standard, well-proven measurements in about the same time, without 3D segmentation. Having a 3D segmentation may have some extra value, but the cost of required extra time of the clinician usually makes this a tough sell.</p>
<p>In contrast, fully automatic segmentation is clinically useful and impactful, because it both reduces the clinician’s effort and can provider richer results. Interactive segmentation tools cannot ever come close to automatic methods in routine clinical use.</p>
<p>Interactive methods may still play a role for research, in generating ground truth training data, or help with very difficult segmentations. But this is a very small arena, very crowded with various tools, and SAM-based tools do not seem to stand out in any way - they are not particularly well positioned for solving very hard problems, for doing 3D segmentations, for providing robust, bias-free, consistent, or anatomically correct segmentations.</p>
<p>SAM/SAM2/MedSAM/SAM-Med3D/etc. might find their niche where they can be useful in medical imaging, maybe in the future they can even carve out a larger area where they are successful. I guess I just don’t understand the excitement about them, when neither the current performance nor future prospects look so great. Anyway, if anybody can set up a nice 3D segmentation <a href="https://www.slicer.org/wiki/Documentation-Rons-Rules-For-Tools">tool</a> in Slicer based on SAM then let me know, I’ll try it and I’m ready to change my mind and will be excited and will happily advertise it if it works very well.</p>

---

## Post #9 by @chir.set (2024-08-15 15:47 UTC)

<p>SAM is foreign to me, I won’t comment about SAM.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="37717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>reduces the clinician’s effort</p>
</blockquote>
</aside>
<p>This means that clinicians want already processed data; i.e, results only. For decades, radiologists have provided that and are still doing that.</p>
<p>‘AI’ tools are trained with normal data and certainly provide ‘good enough’ results with new near normal data, though on a well defined ‘major organs’ target. ‘Good enough’ because they are far from being an immediate and doubtless reference for discrete measurements.</p>
<p>Clinicians deal with pathological situations that do not correspond to normal inputs. The spectrum of anomalous anatomies is very wide, near infinite. Feeding those ‘AI’ algorithms with such diverse anatomies would take more than infinite time… and funding that clinicians are not ready to provide.</p>
<p>To me, the current situation is that clinicians are having excessive expectations from ‘auto-tools’. Digital tools are not yet ready for effortless consuming in a click. Manual segmentation will prevail in the coming decade or more. The best bet for clinicians remains the radiologist if they find it too hard to invest in understanding and segmenting.</p>
<p>As for technologists, they should not over-sell an easy life to clinicians neither.</p>

---

## Post #10 by @muratmaga (2024-08-15 18:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="37717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SAM/SAM2/MedSAM/SAM-Med3D/etc. might find their niche where they can be useful in medical imaging, maybe in the future they can even carve out a larger area where they are successful.</p>
</blockquote>
</aside>
<p>I agree with this comment. My experience with SAM has been less than ideal for real segmentation tasks. However, I can possibly see two specific cases that might be useful for SlicerMorph community:</p>
<ol>
<li>
<p>We often work with organisms and scans where there is no standard anatomy, orientation and calibration, and there will be no automated tools (specifically ML tools) that will guide us. Often in those situations, users tend to do slice-by-slice segmentation with a lot of interaction anyways. So, if SAM can be integrated into Slicer as a segmentation editor effect, can be used like that, I am willing to give it a try.</p>
</li>
<li>
<p>We do have a very specific use case in which we need to remove background (which may or may not be very uniform) from 2D photographs of specimens taken at various angles to prepare them for 3D photogrammetry. Most of the time algorithms like SIFT does that OK programmatically, but sometimes “eats” into the specimen if the contrast is not high. If a SAM like tool can do this better with user guidance, then I am happy to try.</p>
</li>
</ol>
<p>These are not sufficiently wide use cases and there are alternative solutions for them, hence I am not motivated to spend time and resources to work on the integration. But if someone wants to do it, and do it any robust way (I couldn’t even get start with the previous extensions, installation steps  were not trivial), I am of course willing to try, use and promote it, if it works.</p>

---

## Post #11 by @Fernando (2024-08-27 08:58 UTC)

<p>For awareness, here’s a new preprint by NVIDIA discussing this topic: <a href="https://arxiv.org/abs/2408.11210" rel="noopener nofollow ugc">A Short Review and Evaluation of SAM2’s Performance in 3D CT Image Segmentation | Abstract (arxiv.org)</a></p>

---

## Post #12 by @Xiaojie_Guo (2024-10-11 02:40 UTC)

<p>Does SAM2 in Slicer only run tiny model?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30ee0d440733e689bee998e26c3a8067e15116ca.png" data-download-href="/uploads/short-url/6YQWq14o2d02OEh7NbcB9ZGBMuK.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30ee0d440733e689bee998e26c3a8067e15116ca.png" alt="图片" data-base62-sha1="6YQWq14o2d02OEh7NbcB9ZGBMuK" width="690" height="166" data-dominant-color="DEE7ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">761×184 6.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @David-H-Chang (2025-07-01 07:36 UTC)

<p>Hey! I have followed all the instruction to download and setup medsam2 pluggin in slicer. But the slicer just dead between segmentation and downloading results. I see the cmd line of python server running just all right. I have tried different models and all failed. What could be the problem?<br>
The slicer just dead like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/972978f224cb0960ee46c0ef13eb3468191db652.png" data-download-href="/uploads/short-url/lzeX2NxdZwmvwI8px3VjJkD91g6.png?dl=1" title="38e518a6e5c3b426382317f4281ba41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972978f224cb0960ee46c0ef13eb3468191db652_2_690x356.png" alt="38e518a6e5c3b426382317f4281ba41" data-base62-sha1="lzeX2NxdZwmvwI8px3VjJkD91g6" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972978f224cb0960ee46c0ef13eb3468191db652_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972978f224cb0960ee46c0ef13eb3468191db652_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972978f224cb0960ee46c0ef13eb3468191db652_2_1380x712.png 2x" data-dominant-color="A5A3A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">38e518a6e5c3b426382317f4281ba41</span><span class="informations">1966×1016 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what shown in my miniconda prompt</p>
<pre><code class="lang-auto">(base) C:\Users\dell&gt;cd C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer

(base) C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer&gt;conda activate medsam2

(medsam2) C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer&gt;python server.py
 * Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.0.100:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 477-329-984
127.0.0.1 - - [01/Jul/2025 15:15:32] "POST /upload HTTP/1.1" 200 -
infering img_data.npz
C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer\sam2\modeling\sam\transformer.py:270: UserWarning: Memory efficient kernel not used because: (Triggered internally at C:\cb\pytorch_1000000000000\work\aten\src\ATen\native\transformers\cuda\sdp_utils.cpp:773.)
  out = F.scaled_dot_product_attention(q, k, v, dropout_p=dropout_p)
C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer\sam2\modeling\sam\transformer.py:270: UserWarning: Memory Efficient attention has been runtime disabled. (Triggered internally at C:\cb\pytorch_1000000000000\work\aten\src\ATen/native/transformers/sdp_utils_cpp.h:558.)
  out = F.scaled_dot_product_attention(q, k, v, dropout_p=dropout_p)
C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer\sam2\modeling\sam\transformer.py:270: UserWarning: Flash attention kernel not used because: (Triggered internally at C:\cb\pytorch_1000000000000\work\aten\src\ATen\native\transformers\cuda\sdp_utils.cpp:775.)
  out = F.scaled_dot_product_attention(q, k, v, dropout_p=dropout_p)
C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer\sam2\modeling\sam\transformer.py:270: UserWarning: Torch was not compiled with flash attention. (Triggered internally at C:\cb\pytorch_1000000000000\work\aten\src\ATen\native\transformers\cuda\sdp_utils.cpp:599.)
  out = F.scaled_dot_product_attention(q, k, v, dropout_p=dropout_p)
C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer\sam2\modeling\sam\transformer.py:270: UserWarning: CuDNN attention kernel not used because: (Triggered internally at C:\cb\pytorch_1000000000000\work\aten\src\ATen\native\transformers\cuda\sdp_utils.cpp:777.)
  out = F.scaled_dot_product_attention(q, k, v, dropout_p=dropout_p)
C:\device\researches\Hepatoma\MRIV\MRIV - Code\SAM2\MedSAMSlicer\sam2\modeling\sam\transformer.py:270: UserWarning: Expected query, key and value to all be of dtype: {Half, BFloat16}. Got Query dtype: float, Key dtype: float, and Value dtype: float instead. (Triggered internally at C:\cb\pytorch_1000000000000\work\aten\src\ATen/native/transformers/sdp_utils_cpp.h:110.)
  out = F.scaled_dot_product_attention(q, k, v, dropout_p=dropout_p)
C:\Users\dell\miniconda3\envs\medsam2\Lib\site-packages\torch\nn\modules\module.py:1747: UserWarning: Flash Attention kernel failed due to: No available kernel. Aborting execution.
Falling back to all available kernels for scaled_dot_product_attention (which may have a slower speed).
  return forward_call(*args, **kwargs)
Middle Slice Mask Calculated
127.0.0.1 - - [01/Jul/2025 15:15:38] "POST /run_script HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [01/Jul/2025 15:15:38] "POST /run_script HTTP/1.1" 200 -
</code></pre>
<p>see also in <a href="https://github.com/bowang-lab/MedSAMSlicer/issues/59" rel="noopener nofollow ugc">Issues · bowang-lab/MedSAMSlicer</a></p>

---

## Post #14 by @Esteban_Barreiro (2025-12-07 07:48 UTC)

<p>Hi!</p>
<p>Maybe SAM 3D can help you nowadays to remove background easily to help you with your SFM Photogrammetry work.</p>
<p>I have’t used it yet, but it sounds very promising, I don’t know if it works with batch editing.</p>
<p><a href="https://ai.meta.com/blog/sam-3d/" rel="noopener nofollow ugc">https://ai.meta.com/blog/sam-3d/</a></p>

---
