# Request for segmenting suggestions

**Topic ID**: 13342
**Date**: 2020-09-04
**URL**: https://discourse.slicer.org/t/request-for-segmenting-suggestions/13342

---

## Post #1 by @DiamondKMG (2020-09-04 18:05 UTC)

<p>Hello I am trying to create models from a segmentation of a ct scan. The original ct scans are low resolution and have a considerable amount of noise. I am trying to create a model of a zebrafish skull with as much detail as I can get from the scans that I have.</p>
<p>My current processing pipeline is:</p>
<ol>
<li>Resample the image geometry so that the all portions of the skull &gt;1 vx thick</li>
<li>Use the threasholding, islands (remove small islands), and smoothing tools in the segment editor to create the best segmentation possible</li>
<li>Convert the segment to a model.</li>
</ol>
<p>I would eventually like to use the spherical sampling and ALPACA tools in slicer morph to place semilandmarks on a group of fish for a comparison of shape and am looking for a pipeline that will produce models that consistently represent the morphology of the fish from these scans. I’m open to any suggestions and have a link below of an example file. Thank you for any suggestions!</p>
<p><a href="https://drive.google.com/file/d/1bk2S1xvFtcAy0nh0gInVwd8Zt04zZS5B/view?usp=sharing" rel="nofollow noopener">example file</a></p>

---

## Post #2 by @pieper (2020-09-04 19:03 UTC)

<p>Hi <a class="mention" href="/u/diamondkmg">@DiamondKMG</a> -</p>
<p>Sorry, I didn’t see your post here so I’ll paste in some of the things I sent you and <a class="mention" href="/u/muratmaga">@muratmaga</a> by email so others can comment.</p>
<blockquote>
<p>I didn’t try a lot of options, but this is a Median Filter with a 2x2x2 kernel and then oversampled segmentation.  I think you can even do better with other denoising filters, but of course there will be a limit.</p>
</blockquote>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=f2012bca9c&amp;attid=0.3&amp;permmsgid=msg-a:r7323136225519440682&amp;th=1745a5b194b34ba5&amp;view=fimg&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ93wxMd5vAAmSFgc-4JOYt4bctI-Bzrl73Z049Z4qIsdPzksTp2vnLCZT5WY5QlvM6TR1dVtQa_K8wQ-N_UoelLljhoqGDRlDZ673PVQzQX5znwgH7k6qGtSjs&amp;disp=emb&amp;realattid=ii_keokeac52" alt="image.png" width="503" height="500"></p>
<blockquote>
<p>I applied it to msbl_96.ab_plod2_01_transformed using the Filters-&gt;Denoising-&gt;Median Filter module.  But there are many other things to try.  The nonlinear filters can be very good at edge preserving, and may be even better for this task.  Median filtering addresses speckly kinds of noise, while something like gradient anisotropic filtering smooths out consistent areas while preserving strong edges, which helps give crisper results for thresholding volume rendering bone.</p>
</blockquote>

---

## Post #3 by @lassoan (2020-09-04 20:06 UTC)

<p>I got reasonably good surfaces without filtering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acfbeedaeb211f49cfd9892e873c3fe208fc6a20.jpeg" data-download-href="/uploads/short-url/oGhT75lhElHYohrff2Co7TvnMGs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acfbeedaeb211f49cfd9892e873c3fe208fc6a20_2_524x500.jpeg" alt="image" data-base62-sha1="oGhT75lhElHYohrff2Co7TvnMGs" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acfbeedaeb211f49cfd9892e873c3fe208fc6a20_2_524x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acfbeedaeb211f49cfd9892e873c3fe208fc6a20_2_786x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acfbeedaeb211f49cfd9892e873c3fe208fc6a20_2_1048x1000.jpeg 2x" data-dominant-color="5B5762"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1165×1110 421 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In addition to median and anisotropic noise filtering, you may also try unsharp masking (that has been reported to help with segmentation of thin structures, such as orbital bone), but with a few quick tests, I did not get significant improvements.</p>
<p>If you need to have continuous surfaces then you can try Wrap Solidify effect in Segment Editor (provided by SurfaceWrapSolidify extension).</p>

---
