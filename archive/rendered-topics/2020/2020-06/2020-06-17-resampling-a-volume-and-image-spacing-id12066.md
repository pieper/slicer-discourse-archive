# Resampling a volume and Image Spacing

**Topic ID**: 12066
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/resampling-a-volume-and-image-spacing/12066

---

## Post #1 by @Deepa (2020-06-17 07:39 UTC)

<p>Hi All,<br>
I have got a volume with the following dimensions 1702 x1678 x 251.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3cf2a93669feb7d7b65ec6062ca39274812cac2.png" data-download-href="/uploads/short-url/udKB4RMJs99zA56Ib3YYyOAxkNs.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3cf2a93669feb7d7b65ec6062ca39274812cac2_2_345x94.png" alt="Untitled" data-base62-sha1="udKB4RMJs99zA56Ib3YYyOAxkNs" width="345" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3cf2a93669feb7d7b65ec6062ca39274812cac2_2_345x94.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3cf2a93669feb7d7b65ec6062ca39274812cac2_2_517x141.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3cf2a93669feb7d7b65ec6062ca39274812cac2_2_690x188.png 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">854×233 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to reduce the resolution in xy direction and leave z unaltered. May I know which module can be used to do the above?<br>
I’ve checked the crop volume module, the <code>Spacing scale</code> option allows us to scale in all 3 dimensions.<br>
I don’t want to scale in z dimension. May I know if it is a good idea to use <code>Resample Scalar Volume</code> module’s <code>Scaling</code> (2,2,0) if I want to use a <code>Spacing Scale</code> of 2 in x,y dimensions and leave it unaltered in z?</p>
<p>I get the following output :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3b1b1fc06c523c334797ef6eacff4ed13dc1737.png" data-download-href="/uploads/short-url/rVbOEM0u6ukA50TFybuwRSloP9J.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b1b1fc06c523c334797ef6eacff4ed13dc1737_2_345x99.png" alt="Untitled" data-base62-sha1="rVbOEM0u6ukA50TFybuwRSloP9J" width="345" height="99" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b1b1fc06c523c334797ef6eacff4ed13dc1737_2_345x99.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b1b1fc06c523c334797ef6eacff4ed13dc1737_2_517x148.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b1b1fc06c523c334797ef6eacff4ed13dc1737_2_690x198.png 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">845×243 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could someone explain how the image spacing is computed here?<br>
To be honest, I don’t clearly understand what the x,y,z (If I am not wrong, z is the slice thickness) coordinates in the <code>Imaging Spacing </code> tab refer to.</p>
<p>For instance, “the voxel size in this study (pixel size of 0.81 mm)” is mentioned in the documentation of dataset from which I have used the 2D slices to reconstruct 3D volume. If my understanding is right, 0.81mm has to be set for Image Spacing in x,y,z dimensions. May I know if this is correct?</p>

---

## Post #2 by @timeanddoctor (2020-06-17 07:46 UTC)

<p>I think the esayest way is covert the volume to numpy data，and then you can do what you want.</p>

---

## Post #3 by @Deepa (2020-06-17 07:59 UTC)

<p>Thank you. Could you please let me know if such examples are available?</p>

---

## Post #4 by @muratmaga (2020-06-17 16:17 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="1" data-topic="12066">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I’ve checked the crop volume module, the <code>Spacing scale</code> option allows us to scale in all 3 dimensions.<br>
I don’t want to scale in z dimension. May I know if it is a good idea to use <code>Resample Scalar Volume</code> module’s <code>Scaling</code> (2,2,0) if I want to use a <code>Spacing Scale</code> of 2 in x,y dimensions and leave it unaltered in z?</p>
</blockquote>
</aside>
<p><code>ResampleScalarVolume</code> takes physical values. So if you want to reduce xy by 50% and your voxel spacing is 0.81, you should enter 1.62, 1.62, 0 (not 2,2,0)</p>

---

## Post #5 by @Deepa (2020-06-17 16:22 UTC)

<p>Thank you very much for the clarification. Could you please suggest which interpolation method will be apt for resampling? I tried spline interpolation that was mentioned in Luca Antiga’s paper. But, in my opinion, that didn’t work fine. I could find disconnected fragments in 3D volume. Would it be a good idea to use Nearest neighbors?</p>

---

## Post #6 by @muratmaga (2020-06-17 16:25 UTC)

<p>If your data is a labelmap you should use nearest neighbor so that you have exactly the same number of classes that you begin with, otherwise linear is fairly safe.</p>

---

## Post #7 by @Deepa (2020-06-17 17:13 UTC)

<p>Thanks a lot. I would like to confirm if labelmap refers to the volume generated from segment.</p>

---
