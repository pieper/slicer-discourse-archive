---
topic_id: 10345
title: "Surface Scan Registration"
date: 2020-02-18
url: https://discourse.slicer.org/t/10345
---

# Surface Scan Registration

**Topic ID**: 10345
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/surface-scan-registration/10345

---

## Post #1 by @manjula (2020-02-18 21:56 UTC)

<p>Dear all,</p>
<p>This is again regarding surface scan registration issues with 3Shape Trios scans. The scan output is “stl”</p>
<p>when we try to superimposes the scans again it is very very difficult with 3D Slicer.</p>
<p>We used the Geomagic CX and the results were impressive and it was very quick. took less than one minute in  a virtual machine.  (Auto - without manual landmarks)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f22b9ba348d0a6043a01d041f7eb9dd47441929.png" data-download-href="/uploads/short-url/29TyMPWwTx96W0vmLKXUe8GxAqR.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f22b9ba348d0a6043a01d041f7eb9dd47441929_2_690x435.png" alt="1" data-base62-sha1="29TyMPWwTx96W0vmLKXUe8GxAqR" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f22b9ba348d0a6043a01d041f7eb9dd47441929_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f22b9ba348d0a6043a01d041f7eb9dd47441929_2_1035x652.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f22b9ba348d0a6043a01d041f7eb9dd47441929.png 2x" data-dominant-color="B5BDC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1321×834 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried the IGT Fiducial registration, CMF Surface registration and ROI registration.</p>
<p>CMF registration with max settings lot of time and the results are not very good. IGT fiducial registration is quick but we have to put the manual landmarks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b32df0ae7a4f6af5f768543e164b81b2eb92b03e.jpeg" data-download-href="/uploads/short-url/pz5ToOZhpmAerLtFwMF4ePSyfYa.jpeg?dl=1" title="Screenshot from 2020-02-18 22-38-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b32df0ae7a4f6af5f768543e164b81b2eb92b03e_2_647x500.jpeg" alt="Screenshot from 2020-02-18 22-38-00" data-base62-sha1="pz5ToOZhpmAerLtFwMF4ePSyfYa" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b32df0ae7a4f6af5f768543e164b81b2eb92b03e_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b32df0ae7a4f6af5f768543e164b81b2eb92b03e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b32df0ae7a4f6af5f768543e164b81b2eb92b03e.jpeg 2x" data-dominant-color="A2999D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-18 22-38-00</span><span class="informations">967×747 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can some one with good experience with this can have a look at this please ? Perhaps help me where i am going wrong or is this not possible with 3D Slicer and will we have to stick to Geomagic for this step  ?</p>
<p><a href="https://drive.google.com/file/d/1_IV4qa3gq0E8B_Zwbmv-zxG4MgmEkUbN/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1_IV4qa3gq0E8B_Zwbmv-zxG4MgmEkUbN/view?usp=sharing</a></p>
<p><a href="https://drive.google.com/open?id=1COx1TdRqpsVpkJ_WnsZOEVKk2013wk-p" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/open?id=1COx1TdRqpsVpkJ_WnsZOEVKk2013wk-p</a></p>

---

## Post #2 by @lassoan (2020-02-19 03:34 UTC)

<p>I could get perfect registration results (0.025mm RMS error) with basic methods:</p>
<ol>
<li>Crop the part of the rod that is not visible in the bone surface scan image (I used MeshLab for this for now)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e69d6dc7ace61475e41f8160be2f7e8cec9f078e.png" data-download-href="/uploads/short-url/wU76GOposSRNDJpLHIe4g95Kvq6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e69d6dc7ace61475e41f8160be2f7e8cec9f078e_2_690x451.png" alt="image" data-base62-sha1="wU76GOposSRNDJpLHIe4g95Kvq6" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e69d6dc7ace61475e41f8160be2f7e8cec9f078e_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e69d6dc7ace61475e41f8160be2f7e8cec9f078e_2_1035x676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e69d6dc7ace61475e41f8160be2f7e8cec9f078e.png 2x" data-dominant-color="857997"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1282×839 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>
<p>Do a very quick, approximate registration on 3 points using Fiducial registration wizard, harden the transform</p>
</li>
<li>
<p>Use Model registration to fine tune the alignment</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca9cb7c1ef8ca1a533f6851f9afcb8cac9a95f34.png" data-download-href="/uploads/short-url/sUodlTU0SVsPJfGVeJglESqNBEo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca9cb7c1ef8ca1a533f6851f9afcb8cac9a95f34_2_532x500.png" alt="image" data-base62-sha1="sUodlTU0SVsPJfGVeJglESqNBEo" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca9cb7c1ef8ca1a533f6851f9afcb8cac9a95f34_2_532x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca9cb7c1ef8ca1a533f6851f9afcb8cac9a95f34_2_798x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca9cb7c1ef8ca1a533f6851f9afcb8cac9a95f34.png 2x" data-dominant-color="2D2B2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×927 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Good: All computations are instant (takes fraction of a second). Alignment is perfect.</p>
<p>Not so good: Manual cutting of non-common surfaces and manual prealignment is needed. It takes just 1-2 minutes, but requires attention.</p>
<p>There is a good chance that more sophisticated 3D surface template matching methods would work robustly without these manual steps (see for example <a href="https://docs.opencv.org/3.0-beta/modules/surface_matching/doc/surface_matching.html">OpenCV surface matching algorithm</a>).</p>

---

## Post #3 by @manjula (2020-02-19 11:05 UTC)

<p>Dear Prof Lasso,</p>
<p>Thank you and this helped alot. I did the trimming and i think now the results are very good. My mean distance after registration is 0.027.</p>
<p>Also i have no clue how you get the cross sectional view of the models ? How do i see the cross sectional views in red,yellow and green slices as you have shown in your post ?  the way i was doing it was after registering, converting the models to segmentations, but this does not give a nice outline as in your photos.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb9b0a9d613a0f321270ed11362fc822aa24b2d8.png" data-download-href="/uploads/short-url/qLDsD4JEZfqyug8aAemIrDoHkes.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9b0a9d613a0f321270ed11362fc822aa24b2d8_2_643x500.png" alt="Screenshot" data-base62-sha1="qLDsD4JEZfqyug8aAemIrDoHkes" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9b0a9d613a0f321270ed11362fc822aa24b2d8_2_643x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9b0a9d613a0f321270ed11362fc822aa24b2d8_2_964x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9b0a9d613a0f321270ed11362fc822aa24b2d8_2_1286x1000.png 2x" data-dominant-color="645D6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1400×1087 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @manjula (2020-02-19 18:35 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="10345">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Also i have no clue how you get the cross sectional view of the models</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> – I figured that out !!! Models → Slice Display → Visible … <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=14" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2020-02-20 03:52 UTC)

<p>You also have full control over how segmentation is displayed in slice views: you can change the opacity of the filling and outline separately and choose outline thickness.</p>
<p>You can rotate slice views by enabling slice intersections and Ctrl + Alt + Left-click-and-drag in a slice view.</p>

---
