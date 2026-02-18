# How to use Resample Scalar/Vector/DWI Volume

**Topic ID**: 23090
**Date**: 2022-04-22
**URL**: https://discourse.slicer.org/t/how-to-use-resample-scalar-vector-dwi-volume/23090

---

## Post #1 by @koeglfryderyk (2022-04-22 23:06 UTC)

<p>I’m trying to resample a volume with the “Resample Scalar/Vector/DWI Volume” module.</p>
<p>However, the output is cropped, so I must be doing something wrong.</p>
<p>The only three things that I’m changing are ‘Input volume,’ ‘Output Volume,’ and ‘Spacing’ (the last one I set to 0.5,0.5,0.5)</p>
<p>That’s the scene before applying the resampling:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/eff20c12e673ea5e142b5d344a6bec38b872c925.jpeg" data-download-href="/uploads/short-url/yeEHljudGiV5JdVjTUQw8GNVzHD.jpeg?dl=1" title="Screenshot 2022-04-22 at 19.01.47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eff20c12e673ea5e142b5d344a6bec38b872c925_2_664x500.jpeg" alt="Screenshot 2022-04-22 at 19.01.47" data-base62-sha1="yeEHljudGiV5JdVjTUQw8GNVzHD" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eff20c12e673ea5e142b5d344a6bec38b872c925_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eff20c12e673ea5e142b5d344a6bec38b872c925_2_996x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eff20c12e673ea5e142b5d344a6bec38b872c925_2_1328x1000.jpeg 2x" data-dominant-color="A8A8AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-22 at 19.01.47</span><span class="informations">2806×2112 557 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
And that’s the scene after hitting ‘Apply’<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e19f1fa61f0c9debb47e8986bd23784011941cca.jpeg" data-download-href="/uploads/short-url/wbWlNKJDV21EPgJkxwlC2rpcBke.jpeg?dl=1" title="Screenshot 2022-04-22 at 19.02.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19f1fa61f0c9debb47e8986bd23784011941cca_2_664x500.jpeg" alt="Screenshot 2022-04-22 at 19.02.09" data-base62-sha1="wbWlNKJDV21EPgJkxwlC2rpcBke" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19f1fa61f0c9debb47e8986bd23784011941cca_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19f1fa61f0c9debb47e8986bd23784011941cca_2_996x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e19f1fa61f0c9debb47e8986bd23784011941cca_2_1328x1000.jpeg 2x" data-dominant-color="A7A8AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-22 at 19.02.09</span><span class="informations">2806×2112 535 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-23 05:28 UTC)

<p>If you use the low-level API of the module to specifying image geometry manually then you need to set all parameters (origin, spacing, axis directions).</p>
<p>Usually the output geometry is set by choosing a <code>Reference volume</code> - the resampled volume will have the exact same geometry as the reference volume.</p>
<p>If you don’t have a reference volume then you can use <code>Crop volume</code> module to compute the image geometry. The module sets the image geometry based on the ROI box, the <code>Spacing scale</code> value, and <code>Isotropic spacing</code> flag. The module uses <code>Resample Scalar/Vector/DWI Volume</code> module internally for the resampling.</p>

---
