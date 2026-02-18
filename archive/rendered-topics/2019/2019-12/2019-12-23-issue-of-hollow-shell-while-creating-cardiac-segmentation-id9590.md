# Issue of hollow shell while creating cardiac segmentation

**Topic ID**: 9590
**Date**: 2019-12-23
**URL**: https://discourse.slicer.org/t/issue-of-hollow-shell-while-creating-cardiac-segmentation/9590

---

## Post #1 by @sarvpriya1985 (2019-12-23 13:44 UTC)

<p>Hi everyone,</p>
<p>After creating hollow shell (2mm) in cardiac segmentation, when I visualize the structures in virtual reality- The wall appears double-shelled and is not easily understandable and somehow obscures the internal anatomy. Is there any way to prevent that double wall appearance after hollowing. On the slice view, it only appears as a single wall and I don’t see any space bewteen the shell layers. I am attaching a screenshot of slice layer and video of virtual reality view here.</p>
<p>Thanks,<br>
Sarv<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88a2d8b09834fbc009a064393a2be8f5e907a2e0.jpeg" alt="Capture" data-base62-sha1="juJPDAwpoyJRtZSIULWQ0MSpF6M" width="428" height="360"> <a href="https://www.dropbox.com/s/5r63hmgj2gef2mo/VIDEO.mp4?dl=0" rel="noopener nofollow ugc">Double shell view virtual reality</a></p>

---

## Post #2 by @lassoan (2019-12-23 14:28 UTC)

<p>Since in virtual reality it is very easy to clip the model with the headset, you don’t need to hollow out the segments. In virtual reality, probably the best is to show the structures as simple solid closed surfaces (without hollowing).</p>

---

## Post #3 by @sarvpriya1985 (2019-12-23 14:51 UTC)

<p>Thanks for replying Andras. I tried that too (like without hollowing). The issue I faced in that was that there would be a “barrier” kind of appearance at the site of true defects like septal defects or going from right atrium to right ventricle. To avoid that I hollowed the heart. Is there any way to avoid this double-shell appearance. I was hoping once we create a shell, it is a solid shell, so as not to distort the anatomy. Any way around to get rid of these.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #4 by @lassoan (2019-12-23 17:35 UTC)

<p>That’s true, with solid blobs, you’ll have boundaries between surfaces. One solution would be to extract a single surface and color it using scalars (you can set scalars of a mesh from volume using “Probe volume with model” volume).</p>
<p>Another option is to use volume rendering. However, colored volume rendering usually does not produce very smooth surfaces. Multi-volume rendering would work nicely, but multi-volume rendering implementation in VTK is incomplete.</p>

---

## Post #5 by @sarvpriya1985 (2019-12-23 17:58 UTC)

<p>Thanks Andras. I agree that those solid blobs obscure easy visualization of defects. Based on your suggestion, I have few questions.</p>
<ol>
<li>When you say extract a singe surface-Does that mean via threshold segmentation?.</li>
<li>Color using scalar-I haven’t used this before. Is there any link/tutorial of this being used before in other applications just to get an idea.</li>
<li>Probe volume with model volume- For this, do I need to first convert the segmentation into model.<br>
Thanks again,<br>
Sarv</li>
</ol>

---

## Post #6 by @lassoan (2019-12-23 19:25 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="5" data-topic="9590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>When you say extract a singe surface-Does that mean via threshold segmentation?</p>
</blockquote>
</aside>
<p>I mean that you could segment the blood pool as one segment and export that to model.</p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="5" data-topic="9590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Color using scalar-I haven’t used this before. Is there any link/tutorial of this being used before in other applications just to get an idea.</p>
</blockquote>
</aside>
<p>It may have been described in tutorials, but it’s just going to Models module, Scalars section, and choosing a scalar array and a colormap.</p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="5" data-topic="9590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Probe volume with model volume- For this, do I need to first convert the segmentation into model</p>
</blockquote>
</aside>
<p>Probe volume with model module takes two input nodes: a volume node (labelmap volume exported from segmentation) and a model (blood pool exported as a model from segmentation).</p>

---

## Post #7 by @sarvpriya1985 (2019-12-24 15:38 UTC)

<p>Hi Andras,</p>
<p>I tried using probe model module but i am not sure what information i am getting to use to color different parts of one segment. I am attaching screenshot of what i got from that module and when i used it in models module.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45e77aeb1febe94df215b857b1172e1276e74b65.jpeg" data-download-href="/uploads/short-url/9YoT8PRBmy9N8eCvZPKV1crLGCh.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45e77aeb1febe94df215b857b1172e1276e74b65_2_690x338.jpeg" alt="Capture" data-base62-sha1="9YoT8PRBmy9N8eCvZPKV1crLGCh" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45e77aeb1febe94df215b857b1172e1276e74b65_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45e77aeb1febe94df215b857b1172e1276e74b65_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45e77aeb1febe94df215b857b1172e1276e74b65_2_1380x676.jpeg 2x" data-dominant-color="C3B9C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1904×933 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f062a92cec6a482eb628283cc3cf68184d47a5a2.jpeg" data-download-href="/uploads/short-url/yixYjodfxjzRcTANKqe4ZLRAWK6.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f062a92cec6a482eb628283cc3cf68184d47a5a2_2_690x337.jpeg" alt="Capture2" data-base62-sha1="yixYjodfxjzRcTANKqe4ZLRAWK6" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f062a92cec6a482eb628283cc3cf68184d47a5a2_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f062a92cec6a482eb628283cc3cf68184d47a5a2_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f062a92cec6a482eb628283cc3cf68184d47a5a2_2_1380x674.jpeg 2x" data-dominant-color="C2BDD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1911×934 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, while looking for some discussion in slicer forum for the same, I caame across this thread" coloring in VR view"-The solution given is confusing and not very clear. <a href="https://discourse.slicer.org/t/colorize-model-for-vr/6299">https://discourse.slicer.org/t/colorize-model-for-vr/6299</a>.<br>
Would appreciate further directions.</p>
<p>Thanks,<br>
Sarv</p>

---
