---
topic_id: 14666
title: "Volume Rendering Staircase Artifacts"
date: 2020-11-17
url: https://discourse.slicer.org/t/14666
---

# Volume rendering - staircase artifacts

**Topic ID**: 14666
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/volume-rendering-staircase-artifacts/14666

---

## Post #1 by @lassoan (2020-11-17 20:32 UTC)

<p>We have been discussing <a href="https://twitter.com/jmhuiee/status/1328537684176822272">this tweet</a> that compares volume rendering in Slicer to the commercial VG Studio software. The question of staircase artifacts came up and thought that the discussion could be of general interest.</p>
<p>Image volumes consists of discrete point samples, which can create two main type of rendering artifacts: staircase artifacts and Moire pattern.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86167f028bffe39ee005737be66741171463533f.jpeg" alt="image" data-base62-sha1="j8cb5eL2kCs9g48YW0b1apgaEp1" width="409" height="286"></p>
<p><strong>1. Moire pattern on the surface</strong></p>
<p>The pattern looks like elevation lines (points along a line are at equal distance from the camera). The pattern changes as the camera rotates. It is caused by finite sampling distances along the casted ray.</p>
<p>Oversampling (Volume rendering module / Advanced / Techniques / Quality → Maximum) fixes it by taking many samples of a single voxel along the casted ray. There might still remain some visible structured pattern in the image, but that is actually a staircase artifact.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4797d4c783ea6fce727763f8a4c36b94cc18fd33.jpeg" alt="image" data-base62-sha1="adlcdXZiTDv6SwFEPaf121Mj2AH" width="487" height="380"></p>
<p>Surface smoothing (a.k.a. jittering, in Volume rendering module / Advanced / Techniques / Surface smoothing) removes the Moire pattern in a clever way, by slightly shifting the starting position of the samples. This replaces the elevation lines by a random noise pattern. Since the number of sampling points remains the same, it does not slow down the rendering.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5ae05969b32ca61ea008ffb69971f6c621d4866.jpeg" alt="image" data-base62-sha1="z3nORgNqSs3R5Y0LO3wFl7geOBU" width="486" height="379"></p>
<p><strong>2. Staircase artifact</strong></p>
<p>Most visible in regions where there are big differences between neighbor slices. Most commonly visible along Z axis, between slices of a CT image. It is caused by insufficient sampling.</p>
<p>The volume renderer assumes that the voxels are samples of a sufficiently densely sampled continuous 3D signal. However, a continuous signal can only be reconstructed from discrete samples if the Shannon-Nyquist sampling criteria is fulfilled (sampling frequency is at least 2x higher than maximum frequency in the image). In CT imaging this criteria is often violated: rate of change between neighbor slices is usually not limited by sampling distance along the Z axis. Not sufficiently dense sampling can cause slight staircase artifacts along other axes, too, typically only visible as slight color patterns (see second image from the top).</p>
<p>Since information is due to insufficient sampling, there is no way to recover all the details of the original signal. However, a bandwidth-limited signal can be reconstructed by applying low-pass filter (e.g., a simple Gaussian smoothing) to ensure the Shannon-Nyquist criteria is not violated. For example, by applying Gaussian smoothing (Simple Filters module / SmoothingRecursiveGaussianImageFilter, Sigma: 0.1, 0.1, 3.0), staircase artifacts are suppressed:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2542385e1115720e7a58a2e251230259c773d336.jpeg" alt="image" data-base62-sha1="5jBxDmNgr1A4J57xo0LLmZDy3mm" width="488" height="374"></p>
<p>Stronger smoothing can remove all the staircase artifacts but may also remove relevant details from the image.</p>
<p><strong>Next steps</strong></p>
<p>There is room for improvement, for example the Gaussian smoothing could be performed in the GPU on-the-fly and maybe some more sophisticated image reconstruction algorithms could be used instead of Gaussian smoothing (e.g., using deep learning).</p>
<p>However, instead of improving volume raycasting in Slicer, it is probably a better time investment to make <a href="https://blog.kitware.com/vtk-pbr/">VTK’s new physically based rendering surface rendering</a> and evolving <a href="https://discourse.vtk.org/t/ospray-cinematic-rendering/2455">photorealistic volume rendering</a> available in Slicer.</p>

---

## Post #2 by @jmhuie (2020-11-18 16:27 UTC)

<p>Hi, this is a great discussion topic.</p>
<p>I would like share the files (<a href="https://drive.google.com/file/d/1seo20xh_fdY8oDEeCHxQ_VE8rR8saucE/view?usp=sharing" rel="noopener nofollow ugc">Google Drive Link</a>) used to generate the 3D Slicer image in the original twitter post, as well as the original photo. I think it’s important to note that I did downsample the original CT data by a factor of 2, just to make the process run a little smoother on my computer.</p>
<p>Unfortunately, I do not have the original VG Studios Max files, since I did not create it. The photo in my tweet was pulled from <a href="https://twitter.com/danpaluh/status/1265019669867409409?s=20" rel="noopener nofollow ugc">here</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa8e951e74000369ae265ff45544042ec3f965f1.jpeg" data-download-href="/uploads/short-url/zKwQEkma9bTgpthDo9YhTNc5nwt.jpeg?dl=1" title="Proteus_anguinius" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa8e951e74000369ae265ff45544042ec3f965f1_2_690x262.jpeg" alt="Proteus_anguinius" data-base62-sha1="zKwQEkma9bTgpthDo9YhTNc5nwt" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa8e951e74000369ae265ff45544042ec3f965f1_2_690x262.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa8e951e74000369ae265ff45544042ec3f965f1_2_1035x393.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa8e951e74000369ae265ff45544042ec3f965f1_2_1380x524.jpeg 2x" data-dominant-color="393027"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Proteus_anguinius</span><span class="informations">2041×776 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @muratmaga (2020-11-18 17:07 UTC)

<p>This is great, thank you for sharing. As I understand, you downsampled the original volume by 2, then do a segmentation for skull, and used SplitVolume to extract the volume under the segment and rendered it. If that’s the case it is normal that the staircase are more prominent. Couple suggestions.</p>
<p>If you can import the full dataset into your computer (i.e, you don’t have memory problems etc), what you can do is go to SplitVolume and use the master volume as the full resolution image. That will crop out  the same region as your current one but at the full resolution. Going by the numbers in your downsampled volume that should result in a  560x472x1452 which is not all that big for most laptop GPUs.</p>
<p>Also your segmentation has sharp edges, when you mask/split the volume based on that mask, this might cause issues. If the goal with the segmentation is to just isolate skull, then you can grow your segment a little bit, and then run smoothing, this should also take care of some of the small holes in your mask.</p>
<p>Also, make sure you switch to Normal in the Techniques setting of the Volume Rendering. Adaptive gives a poorer image, and for most cases interactivity is better with Normal.</p>

---

## Post #4 by @lassoan (2020-11-18 17:21 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="3" data-topic="14666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Adaptive gives a proper image, and for most cases interactivity is better with Normal</p>
</blockquote>
</aside>
<p>For final rendering, you can set quality to Maximum (which removes the Moire pattern without adding any noise). You can render a rotating animation using Screen Capture module.</p>

---

## Post #5 by @jmhuie (2020-11-18 17:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="14666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>As I understand, you downsampled the original volume by 2, then do a segmentation for skull, and used SplitVolume to extract the volume under the segment and rendered it</p>
</blockquote>
</aside>
<p>You described my process correctly. When I created the image, my focus was primarily on the matching the color palette of the VG studio image. I was aware of the staircases but I wasn’t actively trying to minimize them. I can certainly see why downsampling would make the staircase effect more prominent.</p>
<p>I tried some of your suggestions of using the full res data and growing the segment before using SplitVolume. I would argue that the results are not necessarily better.</p>
<p>First, here’s the downsample data where I grew the segment before using SplitVolume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf4b7b8d8d03bec4311ac4130425f84bcdf67715.jpeg" data-download-href="/uploads/short-url/tzOyxKY08xwWHviU5ZETdrhYF7L.jpeg?dl=1" title="down_smooth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf4b7b8d8d03bec4311ac4130425f84bcdf67715_2_517x213.jpeg" alt="down_smooth" data-base62-sha1="tzOyxKY08xwWHviU5ZETdrhYF7L" width="517" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf4b7b8d8d03bec4311ac4130425f84bcdf67715_2_517x213.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf4b7b8d8d03bec4311ac4130425f84bcdf67715_2_775x319.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf4b7b8d8d03bec4311ac4130425f84bcdf67715_2_1034x426.jpeg 2x" data-dominant-color="352D25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">down_smooth</span><span class="informations">2134×880 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see, the staircase effect is reduced but some definition is arguable lost but overall I think it’s an improvement.</p>
<p>Now, here’s when I used the SplitVolume on the full resolution data without growing the segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752da30f6548fea3e0916dbff9c8a57016c1abde.jpeg" data-download-href="/uploads/short-url/gIBDJ6ctt421RzjT7HGSRuna0pM.jpeg?dl=1" title="full res" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752da30f6548fea3e0916dbff9c8a57016c1abde_2_517x216.jpeg" alt="full res" data-base62-sha1="gIBDJ6ctt421RzjT7HGSRuna0pM" width="517" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752da30f6548fea3e0916dbff9c8a57016c1abde_2_517x216.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752da30f6548fea3e0916dbff9c8a57016c1abde_2_775x324.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/752da30f6548fea3e0916dbff9c8a57016c1abde_2_1034x432.jpeg 2x" data-dominant-color="332B23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">full res</span><span class="informations">2204×920 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The image is very sharp! However, the staircase effect is still there. The steps have just been made smaller.</p>
<p>Lastly, the full resolution data with segment grown before spliting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e4e41b37082741b0639582652f25e6ab8eaf8bd.jpeg" data-download-href="/uploads/short-url/8TbgzkkXnSRAYaUiV3LKasC36Xj.jpeg?dl=1" title="fulles_grow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e4e41b37082741b0639582652f25e6ab8eaf8bd_2_517x244.jpeg" alt="fulles_grow" data-base62-sha1="8TbgzkkXnSRAYaUiV3LKasC36Xj" width="517" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e4e41b37082741b0639582652f25e6ab8eaf8bd_2_517x244.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e4e41b37082741b0639582652f25e6ab8eaf8bd_2_775x366.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e4e41b37082741b0639582652f25e6ab8eaf8bd_2_1034x488.jpeg 2x" data-dominant-color="2E2720"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fulles_grow</span><span class="informations">2174×1030 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s better but I’m not sure that it’s great. I was hoping to see something more similar to the first image up top with the down sampled data and a grown segment, but with more definition. Here, the staircase effect is reduced but still present. However, overall I still think this is a great rendering and better than when I didn’t grow the segment before using SplitVolume.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="14666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For final rendering, you can set quality to Maximum (which removes the Moire pattern without adding any noise). You can render a rotating animation using Screen Capture module.</p>
</blockquote>
</aside>
<p>I personally didn’t notice any difference when setting the quality to Maximum vs Normal vs Adaptive.</p>

---

## Post #6 by @muratmaga (2020-11-18 17:53 UTC)

<aside class="quote no-group" data-username="jmhuie" data-post="5" data-topic="14666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>It’s better but I’m not sure that it’s great.</p>
</blockquote>
</aside>
<p>In the last one did you run a smoothing filter after you expand the segment? I think you did on your 1st of the three images (one name downsampled_smooth).</p>

---

## Post #7 by @muratmaga (2020-11-18 19:04 UTC)

<p>So I pulled the original data from <a href="https://www.morphosource.org/Detail/MediaDetail/Show/media_id/25294">MorphoSource</a>.</p>
<p>Here is the rendering with a simple ramp from 15,000 to Max. You can see there are almost no staircase effects or moire patterns. This is with Normal quality, with surface smoothing enabled.</p>
<p>Unfortunately your VGStudio volume property didn’t work with this image, because original data was 16bit and along the way it got converted to 8 bit. The point is, all conversions (plus the segmentation) does impact the image quality. 8 bit representation is usually ok for dry skulls, but this appears to be wet tissue specimen (skin + soft tissue + bones). So if you need to use 8 bit representation, you will have to experiment with rescaleIntensity filter to preserve as much of the dynamic range associated with bones at the expense of soft tissue.</p>
<p>I do not have much more time today to comment on this, but we covered some of these discussion from <a href="https://discourse.slicer.org/t/image-quantization-techniques/13420">16 bit and 8 bit previously on the forum</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf39ed174653c2fc650a8f21ddc8f960682da197.jpeg" data-download-href="/uploads/short-url/rhFiMQGhB5TNsu3modnnGBdKUNp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39ed174653c2fc650a8f21ddc8f960682da197_2_689x322.jpeg" alt="image" data-base62-sha1="rhFiMQGhB5TNsu3modnnGBdKUNp" width="689" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39ed174653c2fc650a8f21ddc8f960682da197_2_689x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39ed174653c2fc650a8f21ddc8f960682da197_2_1033x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39ed174653c2fc650a8f21ddc8f960682da197_2_1378x644.jpeg 2x" data-dominant-color="898A9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2392×1118 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @pieper (2020-11-18 19:13 UTC)

<p>I did some experiments too with the original volume rather than the output of the segmentation and while it’s better, the version you shared is only 8 bits per pixel so the stairsteps are “baked in” to the data.</p>
<p>I cast it to float and did a gaussian smooth with sigma of 0.02 and it’s a bit better, but I agree with Murat that using the original data without casting to 8 bit is much better.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/683a694d8e43ff9fbed0f69c95dc879a177d3170.jpeg" alt="image" data-base62-sha1="eS2NLmIvwzjF2h1rucqJEw3WJws" width="619" height="255"></p>
<p>If you want to use your segmentation to remove the other bones, probably the best is to segment the region you want, grow it by a bit, then use the Mask Volume from Segment Editor Extra Effects to remove everything that’s not in your segment and then volume render the result.</p>

---
