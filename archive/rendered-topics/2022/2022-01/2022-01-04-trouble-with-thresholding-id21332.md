# Trouble with thresholding

**Topic ID**: 21332
**Date**: 2022-01-04
**URL**: https://discourse.slicer.org/t/trouble-with-thresholding/21332

---

## Post #1 by @Rosalee_Elting (2022-01-04 22:43 UTC)

<p>Operating system:<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Segment of hummingbird bill/head<br>
Actual behavior: Fragmented segment</p>
<p>Hoping for a little input on a set of .tiff files I’m working with. I have uploaded a volume that was CT scanned, and the contrast between the bird and the surrounding area is limited. I have used the Adjust window level setting and adjusted volume properties. When I try to use segment editor to extract the bird, I’m having trouble thresholding it out. I’m sure it can be done, just hoping others might be able to give tips for extracting a segment with this tricky scan.<a href="https://drive.google.com/file/d/1viQTqlgGdQo6kaVVDcgj6CbMR5cBZIJ0/view?usp=sharing" rel="noopener nofollow ugc">download link</a></p>

---

## Post #2 by @muratmaga (2022-01-05 04:18 UTC)

<aside class="quote no-group" data-username="Rosalee_Elting" data-post="1" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>nt with this tricky scan.<a href="https://drive.google.com/file/d/1viQTqlgGdQo6kaVVDcgj6CbMR5cBZIJ0/view?usp=sharing">download link</a></p>
</blockquote>
</aside>
<p>Looks like you only shared the mrml file but not the volume. Without the volume we can only guess what the issues are. If the scan is of poor quality, or poorly reconstructed there is not much you can do. Perhaps you can try some of the image processing filters (median filter), or try to rescale or normalize the intensity.</p>

---

## Post #3 by @Rosalee_Elting (2022-01-05 20:47 UTC)

<p>Thanks, Murat, for the response! I am adding a zipped folder of the .tiff files. The median filter helped some, but I’m still having trouble with these photos. I typically add them using image stacks then keep working on the same scene. We’re contracting someone to make these scans, so I’d be interested to know if the difficulty has to do with these files, or my processing. <a href="https://drive.google.com/file/d/1SkQZLN8UgmHyn_41jybESCFq2Ob3K3Et/view?usp=sharing" rel="noopener nofollow ugc">image folder</a></p>

---

## Post #4 by @muratmaga (2022-01-05 21:43 UTC)

<p>SO there are some really strange issues. First the tiff stacks are in float values, and they only range from 0.1 to 0.7 range. This is not very common for CT scans. What I did was to rescale to image (Simple Filters → RescaleIntensity) and set the minimum 0 and max to 65535. Then I used the Cast Image Filter to turn the rescaled image from float image to unsigned short data type. This also reduces the memory consumption quite a bit (since this is a huge dataset).</p>
<p>This is what I got:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/447fcd3b3c3fcead863a3dff2d19c24ed184e3dd.jpeg" data-download-href="/uploads/short-url/9LYhtnTYF2YXbnxpGBCtvZGkFQ1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/447fcd3b3c3fcead863a3dff2d19c24ed184e3dd_2_688x500.jpeg" alt="image" data-base62-sha1="9LYhtnTYF2YXbnxpGBCtvZGkFQ1" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/447fcd3b3c3fcead863a3dff2d19c24ed184e3dd_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/447fcd3b3c3fcead863a3dff2d19c24ed184e3dd_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/447fcd3b3c3fcead863a3dff2d19c24ed184e3dd_2_1376x1000.jpeg 2x" data-dominant-color="1B1B1B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1509×1096 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then I ran the median filter, which helped, but also lost some of the finer detail.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abf67c39b5e3708b96f27b6af5bac0fbaced0c66.jpeg" data-download-href="/uploads/short-url/oxfJRioxk156gzNmCrZp4jHl8Wi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf67c39b5e3708b96f27b6af5bac0fbaced0c66_2_656x500.jpeg" alt="image" data-base62-sha1="oxfJRioxk156gzNmCrZp4jHl8Wi" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf67c39b5e3708b96f27b6af5bac0fbaced0c66_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf67c39b5e3708b96f27b6af5bac0fbaced0c66_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf67c39b5e3708b96f27b6af5bac0fbaced0c66_2_1312x1000.jpeg 2x" data-dominant-color="121212"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1490×1134 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is a strange scan. First the specimen is not really centered in the field of view, but sits in a corner of a huge image stack, which makes the data import challenging. Then, it appears the specimen is partial (cut during the reconstruction). Whether that’s intentional or not, no idea. There is also the strong background issue. If you are paying for these scans, they should really do a better job.</p>

---

## Post #5 by @DIV (2022-01-18 12:06 UTC)

<p>This is an interesting case.  I followed <strong>muratmaga</strong>’s advice on rescaling the intensity and casting to uint16.  By doing this the 49.1 GiB set of 2,129 TIFF files (17.6 GiB zipped) was able to be saved from 3D Slicer as a single 24.7 GiB file.</p>
<p>However I am not sure that there is any problem with the specimen or its positioning.</p>
<aside class="quote no-group" data-username="Rosalee_Elting" data-post="1" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>Expected behavior: Segment of hummingbird bill/head</p>
</blockquote>
</aside>
<p>From the 3D rendering the scan indeed looks to me like a long bird’s beak and the front half of its head, more-or-less centred within a cylinder.  Seeing a cylinder generated from a CT scan makes sense to me.  What seems slightly odd to me is that the cylinder axis doesn’t quite line up with the image coordinate system (evident from the bounding box, represented as the ROI below).</p>
<p>10800 rescaled units &amp; up (perspective 3D rendering)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7548811c5d6c30cc08613244aa501561aa42f53.jpeg" data-download-href="/uploads/short-url/nSgQq9DeQKYiWYMYm1CZIbCyaYP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7548811c5d6c30cc08613244aa501561aa42f53_2_517x366.jpeg" alt="image" data-base62-sha1="nSgQq9DeQKYiWYMYm1CZIbCyaYP" width="517" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7548811c5d6c30cc08613244aa501561aa42f53_2_517x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7548811c5d6c30cc08613244aa501561aa42f53_2_775x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7548811c5d6c30cc08613244aa501561aa42f53.jpeg 2x" data-dominant-color="8D93C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>10800 rescaled units &amp; up (orthographic 3D rendering)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e521136ad65f8842b4d3a60152a4ae53acc7b1.jpeg" data-download-href="/uploads/short-url/nf2fWVu89tyILWYkLG3K2gqld8l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2e521136ad65f8842b4d3a60152a4ae53acc7b1_2_517x366.jpeg" alt="image" data-base62-sha1="nf2fWVu89tyILWYkLG3K2gqld8l" width="517" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2e521136ad65f8842b4d3a60152a4ae53acc7b1_2_517x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2e521136ad65f8842b4d3a60152a4ae53acc7b1_2_775x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e521136ad65f8842b4d3a60152a4ae53acc7b1.jpeg 2x" data-dominant-color="8A8FC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>11200 rescaled units &amp; up (perspective 3D rendering)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/572f9bdb96b78d040581a121ade1ed02f18081b9.png" data-download-href="/uploads/short-url/crhxyXRUyiAmw9Bz9zbw1kek2zT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/572f9bdb96b78d040581a121ade1ed02f18081b9_2_517x366.png" alt="image" data-base62-sha1="crhxyXRUyiAmw9Bz9zbw1kek2zT" width="517" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/572f9bdb96b78d040581a121ade1ed02f18081b9_2_517x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/572f9bdb96b78d040581a121ade1ed02f18081b9_2_775x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/572f9bdb96b78d040581a121ade1ed02f18081b9.png 2x" data-dominant-color="979CCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I wonder whether the original CT scan data may have been resampled into a new coordinate system.  (Perhaps that also explains the intensity scaling in the range of 0 to 1 for the TIFF files.)</p>
<p>Based on the ability to get some sensible 3D rendering, I’m not sure that the background poses such a problem.  The suggestion that “the contrast between the bird and the surrounding area is limited” may be a matter of ‘perspective’.  That is, if the window is judiciously chosen, then the contrast looks better.  It might be easier to specify appropriate settings once the above intensity rescaling has been done.</p>
<aside class="quote no-group" data-username="Rosalee_Elting" data-post="1" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>When I try to use segment editor to extract the bird</p>
</blockquote>
</aside>
<p>Do you want just the beak, or the flesh and skin and feathers too?</p>
<p>—DIV</p>
<p>P.S. Here are the contents of the <code>*.VP</code> file containing my 3D rendering settings for the rescaled intensities.</p>
<pre><code class="lang-auto">1
1
1
0.2
0
1
8 -1000 0 11200 0 19000 0.8 83849.5625 1
4 0 1 985.12 1
20 10000 0.3 0.3 1 15000 0.3 1 0.3 22000 1 0 0 49014.53515625 1 0.912535 0.0374849 61858.734375 1 0.3 0.3
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1484f0a6eda17d05030bbbee2f5267ce4244a97d.png" alt="image" data-base62-sha1="2Vwn4wTyIOAoNvTJ2JYQl7CXFwN" width="363" height="219"></p>
<p>P.P.S.  There is a kind of limitation in 3D Slicer that will prevent a user from entering an intensity value in the opacity or colour mapping that’s above some nominal ‘maximum’ by directly typing it in.  (Some people might call this a bug.)  The workarounds are to either drag the rightmost grey circular knob to the far right, or to manually edit the <code>VP</code> file.  It’s not very convenient.</p>

---

## Post #6 by @DIV (2022-01-18 12:32 UTC)

<p>There’re some minor artefacts creating dull and bright streaks in the background.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb083b068f23470cc867f4a0c2e45c3d1b39ae5.jpeg" data-download-href="/uploads/short-url/Al5so4jJ4o05lgzJ1ebvjUyrBfD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb083b068f23470cc867f4a0c2e45c3d1b39ae5_2_517x366.jpeg" alt="image" data-base62-sha1="Al5so4jJ4o05lgzJ1ebvjUyrBfD" width="517" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb083b068f23470cc867f4a0c2e45c3d1b39ae5_2_517x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb083b068f23470cc867f4a0c2e45c3d1b39ae5_2_775x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb083b068f23470cc867f4a0c2e45c3d1b39ae5.jpeg 2x" data-dominant-color="121010"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slices viewed with <code>Manual Min/Max</code> set to <code>10300</code> and <code>14100</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0848a1017c5f076e612dee655d2f9de1bb94a249.png" data-download-href="/uploads/short-url/1bhqrz7O1SSlk8Ld2yHg6E9164N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0848a1017c5f076e612dee655d2f9de1bb94a249_2_690x489.png" alt="image" data-base62-sha1="1bhqrz7O1SSlk8Ld2yHg6E9164N" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0848a1017c5f076e612dee655d2f9de1bb94a249_2_690x489.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0848a1017c5f076e612dee655d2f9de1bb94a249.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0848a1017c5f076e612dee655d2f9de1bb94a249.png 2x" data-dominant-color="2F303A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78039e4e06cf4d879825bc5d9f87b5c92f97de0e.jpeg" data-download-href="/uploads/short-url/h7H31yMCRCtPcavDeBj0LlJZvr0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78039e4e06cf4d879825bc5d9f87b5c92f97de0e_2_690x489.jpeg" alt="image" data-base62-sha1="h7H31yMCRCtPcavDeBj0LlJZvr0" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78039e4e06cf4d879825bc5d9f87b5c92f97de0e_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78039e4e06cf4d879825bc5d9f87b5c92f97de0e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78039e4e06cf4d879825bc5d9f87b5c92f97de0e.jpeg 2x" data-dominant-color="2E2F39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Note:  displaying or hiding the ROI can change the 3D rendering, per <a href="https://discourse.slicer.org/t/volume-rendering-appearance-changes-if-roi-box-is-shown/20575" class="inline-onebox">Volume rendering appearance changes if ROI box is shown</a> .</p>

---

## Post #7 by @DIV (2022-01-18 13:15 UTC)

<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>By doing this the 49.1 GiB set of 2,129 TIFF files (17.6 GiB zipped) was able to be saved from 3D Slicer as a single 24.7 GiB file.</p>
</blockquote>
</aside>
<p>By cropping down from the original volume (2529×2278×2129) to just the region of interest (~1813×932×993) this can be reduced much further to a single 2.4 GiB <code>NRRD</code> file.</p>
<p>With the rescaled intensities in the cropped volume a first (rough) try at a segmentation, with a Threshold of <code>11500</code> intensity units, is given below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ac83f75558a88eadb449bc46b9983dd3231ae7.png" data-download-href="/uploads/short-url/3wh4sSCfKKttJNjrYYuAxs8atz9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18ac83f75558a88eadb449bc46b9983dd3231ae7_2_690x489.png" alt="image" data-base62-sha1="3wh4sSCfKKttJNjrYYuAxs8atz9" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18ac83f75558a88eadb449bc46b9983dd3231ae7_2_690x489.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ac83f75558a88eadb449bc46b9983dd3231ae7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ac83f75558a88eadb449bc46b9983dd3231ae7.png 2x" data-dominant-color="31393B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Obviously there are some artefacts present.  The beak looks like one continuous piece (with some hollows in it).  The feathers(?) are little isolated ‘islands’, but I would have thought that that was essentially realistic.</p>
<p>I guess that the required fidelity of the segmentation would depend upon your purpose (<em>e.g.</em> 3D printing, mechanical analysis, …).</p>
<p>—DIV</p>

---

## Post #8 by @muratmaga (2022-01-18 16:32 UTC)

<aside class="quote no-group" data-username="DIV" data-post="7" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>By cropping down from the original volume (2529×2278×2129) to just the region of interest (~1813×932×993) this can be reduced much further to a single 2.4 GiB <code>NRRD</code> file.</p>
</blockquote>
</aside>
<p>The issue is not so much that the data is not workable. Given that this is a paid service, it should have been delivered in a better condition than a 48GB file whose 95% of it is just air, not the specimen. Many other dubious choices for reconstruction such as no adjustment of intensities tells me the lab did this has no to very little experience, or just doesn’t care for customer service, and either way probably should be avoided.</p>

---

## Post #9 by @DIV (2022-01-20 00:31 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="8" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Given that this is a paid service, it should have been delivered in a better condition […].</p>
</blockquote>
</aside>
<p>I will take your word for it.<br>
As I mentioned, the thing I found most notable was the skew of the cylindrical ‘scan volume’ within the adopted coordinate system;  that also contributed to adding unnecessary (useless) voxels.<br>
(Unless the cylinder represented a block of resin that the bird was embedded in???)</p>
<aside class="quote no-group quote-modified" data-username="DIV" data-post="6" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>[…] some minor artefacts creating dull and bright streaks in the background.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb083b068f23470cc867f4a0c2e45c3d1b39ae5.jpeg" data-download-href="/uploads/short-url/Al5so4jJ4o05lgzJ1ebvjUyrBfD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb083b068f23470cc867f4a0c2e45c3d1b39ae5_2_690x489.jpeg" alt="image" data-base62-sha1="Al5so4jJ4o05lgzJ1ebvjUyrBfD" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb083b068f23470cc867f4a0c2e45c3d1b39ae5_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb083b068f23470cc867f4a0c2e45c3d1b39ae5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb083b068f23470cc867f4a0c2e45c3d1b39ae5.jpeg 2x" data-dominant-color="121010"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×612 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
</aside>
<p>Out of interest, do you know whether there is a particular name given to the ‘streak’ artefacts, and also whether there are imaging settings that could have avoided this (rather than having to try to deal with them afterwards with some sort of filtering or other post-processing)?</p>

---

## Post #10 by @muratmaga (2022-01-20 00:38 UTC)

<aside class="quote no-group" data-username="DIV" data-post="9" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>streak’ artefacts</p>
</blockquote>
</aside>
<p>Beam hardening. Normally should be handled too some extend during reconstruction.</p>

---

## Post #11 by @Rosalee_Elting (2022-03-02 01:44 UTC)

<p>Thank you both for the help with this! Hoping to circle back on the scan and try these methods. Really appreciate your help.</p>

---
