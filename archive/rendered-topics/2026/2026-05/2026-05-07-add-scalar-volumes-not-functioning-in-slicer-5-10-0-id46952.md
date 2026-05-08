---
topic_id: 46952
title: "Add Scalar Volumes Not Functioning In Slicer 5 10 0"
date: 2026-05-07
url: https://discourse.slicer.org/t/46952
---

# Add Scalar Volumes Not Functioning in Slicer 5.10.0

**Topic ID**: 46952
**Date**: 2026-05-07
**URL**: https://discourse.slicer.org/t/add-scalar-volumes-not-functioning-in-slicer-5-10-0/46952

---

## Post #1 by @Hualiama (2026-05-07 13:51 UTC)

<p>Good Day All,</p>
<p>I have been working on a study of the femur with a set of scans that have been split across two DICOM series. See below image for reference.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7facbd6731e702179aabf430b81752f35068bf3f.jpeg" data-download-href="/uploads/short-url/idsJovkmULdkvVamDt3reqCLrOf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7facbd6731e702179aabf430b81752f35068bf3f_2_515x500.jpeg" alt="image" data-base62-sha1="idsJovkmULdkvVamDt3reqCLrOf" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7facbd6731e702179aabf430b81752f35068bf3f_2_515x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7facbd6731e702179aabf430b81752f35068bf3f_2_772x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7facbd6731e702179aabf430b81752f35068bf3f.jpeg 2x" data-dominant-color="3E3E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1016×986 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I intend to reconstruct the femur with the inferior condyle for the purposes of my research. I planned on using the add scalar volumes tool in order to create a single volume to segment the regions of interest, but have not had much luck. I created two regions of interest and used the Crop Volume tool on each series as shown below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25fbbafc26491cd837e9bc101f631ff8d21b63c3.jpeg" data-download-href="/uploads/short-url/5q0ZLRAxxt40hGsKo1DIt4Pm5qz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25fbbafc26491cd837e9bc101f631ff8d21b63c3_2_682x500.jpeg" alt="image" data-base62-sha1="5q0ZLRAxxt40hGsKo1DIt4Pm5qz" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25fbbafc26491cd837e9bc101f631ff8d21b63c3_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25fbbafc26491cd837e9bc101f631ff8d21b63c3_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25fbbafc26491cd837e9bc101f631ff8d21b63c3_2_1364x1000.jpeg 2x" data-dominant-color="B0A5C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1407 468 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f872187d556bb89534346f69aa60d59afe09e445.jpeg" data-download-href="/uploads/short-url/zrQRpBKEpiBzn1FQWlu8xxcYybj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f872187d556bb89534346f69aa60d59afe09e445_2_563x500.jpeg" alt="image" data-base62-sha1="zrQRpBKEpiBzn1FQWlu8xxcYybj" width="563" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f872187d556bb89534346f69aa60d59afe09e445_2_563x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f872187d556bb89534346f69aa60d59afe09e445_2_844x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f872187d556bb89534346f69aa60d59afe09e445_2_1126x1000.jpeg 2x" data-dominant-color="AAA7C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1290×1144 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, whenever I attempt to user the Add Scalar Volumes tool it will only produce the following result, which is just <strong>Input Volume 1</strong> that is chosen in the tool menu.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71eb49d4119f4835901dab02e4c17a1477ca78ee.jpeg" data-download-href="/uploads/short-url/gfM3xWbEJ2iCWGw2PcjXuLNd8x8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71eb49d4119f4835901dab02e4c17a1477ca78ee_2_167x500.jpeg" alt="image" data-base62-sha1="gfM3xWbEJ2iCWGw2PcjXuLNd8x8" width="167" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71eb49d4119f4835901dab02e4c17a1477ca78ee_2_167x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71eb49d4119f4835901dab02e4c17a1477ca78ee_2_250x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71eb49d4119f4835901dab02e4c17a1477ca78ee_2_334x1000.jpeg 2x" data-dominant-color="A6A3C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">468×1400 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee171300981ec7a111a38d008e288eed8d87cb6.png" data-download-href="/uploads/short-url/vNH0n2S45iX1AhL9UM7IgQvMZEy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee171300981ec7a111a38d008e288eed8d87cb6_2_690x233.png" alt="image" data-base62-sha1="vNH0n2S45iX1AhL9UM7IgQvMZEy" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee171300981ec7a111a38d008e288eed8d87cb6_2_690x233.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee171300981ec7a111a38d008e288eed8d87cb6_2_1035x349.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee171300981ec7a111a38d008e288eed8d87cb6_2_1380x466.png 2x" data-dominant-color="414141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1587×536 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have attempted using the Add Scalar Volumes tool across multiple Slicer versions (5.4.0 and 5.11.0) and have found no success with the tool. I can confirm that both of the volumes are of Type Scalar. I haven’t found any threads reporting this issue, and thus am writing this support thread to see if anyone might have a solution to fix this issue.</p>
<p>If anyone has any advice or has encountered this issue as well and found a way to overcome it I would greatly appreciate their input. Thank you for your time.</p>

---

## Post #2 by @pieper (2026-05-07 13:56 UTC)

<p>You could try this module from the sandbox extension: <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">https://github.com/PerkLab/SlicerSandbox#stitch-volumes</a></p>

---

## Post #3 by @Hualiama (2026-05-07 14:19 UTC)

<p>Thank you, this worked quite well!</p>

---
