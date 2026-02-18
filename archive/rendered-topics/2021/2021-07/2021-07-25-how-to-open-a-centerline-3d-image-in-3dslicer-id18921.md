# How to open a centerline 3d image in 3dslicer?

**Topic ID**: 18921
**Date**: 2021-07-25
**URL**: https://discourse.slicer.org/t/how-to-open-a-centerline-3d-image-in-3dslicer/18921

---

## Post #1 by @parvaneh.a (2021-07-25 20:41 UTC)

<p>Operating system: ubuntu 20<br>
Slicer version:4.11.20210226<br>
Expected behavior: open a centerline image as expected<br>
Actual behavior: opens the centerline image abnormally</p>
<p>Hi,<br>
I have extracted the center line of my label map images using bwskel function in matlab. I would like to open them in slicer. When I open them in matlab with volumeViewer it show that correctly as image below but when I open in slicer it shows a weird image. Why this happen and a how can I see the center line binary image in slicer as I see in matlab?</p>
<p>In matlab centerline image appeared as yellow lines:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/230aa558b8867ad22fbc9c1aaba56217f61754aa.png" data-download-href="/uploads/short-url/4ZZwfwSDxWo2Ld9PjvpkYHVC9qW.png?dl=1" title="Screenshot from 2021-07-25 16-34-15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/230aa558b8867ad22fbc9c1aaba56217f61754aa.png" alt="Screenshot from 2021-07-25 16-34-15" data-base62-sha1="4ZZwfwSDxWo2Ld9PjvpkYHVC9qW" width="690" height="497" data-dominant-color="58C2EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-07-25 16-34-15</span><span class="informations">997×719 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In slicer centerline image appeared as :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77a0215ad7ea62bb56a5f1a19b36eb7f270ba46c.png" data-download-href="/uploads/short-url/h4fTAlBuMZdhroLpRrFfu0erhla.png?dl=1" title="Screenshot from 2021-07-25 16-38-07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a0215ad7ea62bb56a5f1a19b36eb7f270ba46c_2_558x499.png" alt="Screenshot from 2021-07-25 16-38-07" data-base62-sha1="h4fTAlBuMZdhroLpRrFfu0erhla" width="558" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a0215ad7ea62bb56a5f1a19b36eb7f270ba46c_2_558x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a0215ad7ea62bb56a5f1a19b36eb7f270ba46c_2_837x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77a0215ad7ea62bb56a5f1a19b36eb7f270ba46c.png 2x" data-dominant-color="979AD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-07-25 16-38-07</span><span class="informations">973×871 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,</p>

---

## Post #2 by @pieper (2021-07-25 22:01 UTC)

<p>Probably the matlab code is saving with options Slicer doesn’t expect.  What format do you use for saving?</p>

---

## Post #3 by @parvaneh.a (2021-07-25 23:12 UTC)

<p>I am using nii.gz format for saving. Might be related to data type (uint, o so?)?</p>

---

## Post #4 by @pieper (2021-07-26 14:43 UTC)

<p>Most .nii.gz file load fine in Slicer but it’s not a great format for general purpose work for a lot of reasons.  You could try nrrd or another format.</p>

---

## Post #5 by @lassoan (2021-07-26 21:18 UTC)

<p>You may try to turn off smoothing (in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#create-new-representation-in-segmentation-conversion">“Advanced create…”</a> in Segmentations module), because smoothing may remove isolated voxels and very thin structures.</p>
<p>However, your rendering in Matlab looks like a quite low quality centerline extraction (looks like a very basic skeletonization). I would not bother even trying to read this data because it is unlikely that you could use it for anything. Instead, you can extract high-quality centerline, metrics, statistics, connectivity information, etc. using <a href="https://github.com/vmtk/SlicerExtension-VMTK#the-vmtk-extension-for-3d-slicer">SlicerVMTK extension</a>.</p>

---

## Post #6 by @parvaneh.a (2021-07-26 22:57 UTC)

<p>Thanks for helping . Unfortunately I could not find the option of "Advanced create’ in segmentation module. I have attached the picture which I see in the segmentation module and would be thankful if you could elaborate on the steps to find the advanced create for turning off the smoothing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/aba2599b592bde589a3392212b80db1f7b986544.png" data-download-href="/uploads/short-url/oultO65j3qKtp52TuN2rOFCUoqo.png?dl=1" title="Screenshot from 2021-07-26 18-50-32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/aba2599b592bde589a3392212b80db1f7b986544_2_403x500.png" alt="Screenshot from 2021-07-26 18-50-32" data-base62-sha1="oultO65j3qKtp52TuN2rOFCUoqo" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/aba2599b592bde589a3392212b80db1f7b986544_2_403x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/aba2599b592bde589a3392212b80db1f7b986544_2_604x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/aba2599b592bde589a3392212b80db1f7b986544.png 2x" data-dominant-color="DDE0E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-07-26 18-50-32</span><span class="informations">712×883 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have seen the skeletonization filter in 3d slicer and that does not have skeletonization in 3D. Also about the slicervmtk , it requires that I define the beginning and end of the path of center line manually which is not possible for many data that I have. Furthermore, as seen , my image has 4 main branches of pulmonary veins and providing the seed point of each of four takes so much time and is impossible. Even with trying the seed points the results with slicer was not acceptable. Please let me know if I have missed anything.</p>

---

## Post #7 by @lassoan (2021-07-27 04:11 UTC)

<aside class="quote no-group" data-username="parvaneh.a" data-post="6" data-topic="18921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>Unfortunately I could not find the option of "Advanced create’ in segmentation module.</p>
</blockquote>
</aside>
<p>Long-click (hold down the left mouse button until the menu appears):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bfecd8bd000dfbea3d38729b6d38bd340c07ac3.png" alt="image" data-base62-sha1="3ZENSdWOAZvCpVJfAuoJgHeJfJ9" width="678" height="276"></p>
<aside class="quote no-group" data-username="parvaneh.a" data-post="6" data-topic="18921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>I have seen the skeletonization filter in 3d slicer and that does not have skeletonization in 3D</p>
</blockquote>
</aside>
<p>The module performs skeletonization in 3D. Why do you think it is not doing that?</p>
<aside class="quote no-group" data-username="parvaneh.a" data-post="6" data-topic="18921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>about the slicervmtk , it requires that I define the beginning and end of the path of center line manually which is not possible for many data that I have.</p>
</blockquote>
</aside>
<p>You have the option of specifying endpoints manually, which is a very useful feature, but normally you just click “Auto-detect” to get all the endpoints automatically in a few seconds.</p>
<aside class="quote no-group" data-username="parvaneh.a" data-post="6" data-topic="18921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>Furthermore, as seen , my image has 4 main branches of pulmonary veins and providing the seed point of each of four takes so much time and is impossible</p>
</blockquote>
</aside>
<p>No problem at all, automatic endpoint detection should work well. If the segmented surface is noise then you may have more endpoints than you want, in that case you may either slightly smooth the segmentation, cut of small branches, or remove some of the detected endpoints.</p>
<aside class="quote no-group" data-username="parvaneh.a" data-post="6" data-topic="18921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>Even with trying the seed points the results with slicer was not acceptable.</p>
</blockquote>
</aside>
<p>It should be good. Something like this (blue network, green is centerline extraction result):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0ce7ef2b996c20e827fda09b92fe2d71cc54f3e.jpeg" data-download-href="/uploads/short-url/mWyOgflhESN50yioG8cUb8Vr2Mu.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0ce7ef2b996c20e827fda09b92fe2d71cc54f3e_2_690x417.jpeg" alt="image" data-base62-sha1="mWyOgflhESN50yioG8cUb8Vr2Mu" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0ce7ef2b996c20e827fda09b92fe2d71cc54f3e_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0ce7ef2b996c20e827fda09b92fe2d71cc54f3e_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0ce7ef2b996c20e827fda09b92fe2d71cc54f3e_2_1380x834.jpeg 2x" data-dominant-color="C9C6DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1163 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you attach a screenshot that illustrates the problem you ran into?</p>

---

## Post #8 by @parvaneh.a (2021-07-28 21:52 UTC)

<p>Thanks a lot the issue was resolved with turn off the smoothing and I can see the binary centerline correctly.<br>
I had not tried the automatic end point detection and just tried it and it works very well with a bit error as some end points are joined together as seen. How to correct them and how to write a code in python to be able to automatically extract centerline for all images without loading them one by one in slicer and save them?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/619d9bcaca1e4730b778abf8829532eac8c186e4.jpeg" data-download-href="/uploads/short-url/dVxZll6O9qqllT0TmnGaSGSuDDC.jpeg?dl=1" title="Screen Shot 2021-07-28 at 5.45.57 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/619d9bcaca1e4730b778abf8829532eac8c186e4_2_690x373.jpeg" alt="Screen Shot 2021-07-28 at 5.45.57 PM" data-base62-sha1="dVxZll6O9qqllT0TmnGaSGSuDDC" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/619d9bcaca1e4730b778abf8829532eac8c186e4_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/619d9bcaca1e4730b778abf8829532eac8c186e4_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/619d9bcaca1e4730b778abf8829532eac8c186e4_2_1380x746.jpeg 2x" data-dominant-color="B7BECF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-28 at 5.45.57 PM</span><span class="informations">1920×1040 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @pieper (2021-07-28 22:46 UTC)

<p>If you search the forum archives for vmtk and centerlines I’m pretty sure this has already been answered.  Maybe someone who uses vmtk can jump in here.</p>

---

## Post #10 by @parvaneh.a (2021-07-29 02:49 UTC)

<p>Thanks.<br>
In some cases it does not provide the centerline on some branches. here I first used automatic endpoint and then added manually some on the parts that did not get the endpoint . However, still the centerline cannot be obtained on some branches. Hoe can I get those in?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63bc2dc94969804bd210ee8e3fc9fb415cdd7025.jpeg" data-download-href="/uploads/short-url/eeirkQryrmZWlzzmxMwHGIM3zdb.jpeg?dl=1" title="Screen Shot 2021-07-28 at 10.44.23 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63bc2dc94969804bd210ee8e3fc9fb415cdd7025.jpeg" alt="Screen Shot 2021-07-28 at 10.44.23 PM" data-base62-sha1="eeirkQryrmZWlzzmxMwHGIM3zdb" width="636" height="500" data-dominant-color="8F9ABA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-28 at 10.44.23 PM</span><span class="informations">1072×842 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @lassoan (2021-08-03 16:28 UTC)

<p>Which Slicer version did you encounter this problem with?</p>

---

## Post #12 by @parvaneh.a (2021-08-19 00:55 UTC)

<p>the version was 4.11</p>

---

## Post #13 by @lassoan (2021-08-20 18:47 UTC)

<p>That should work. Then most likely the issue is that inside the left atrium, the concept of a centerline does not exist. You may want to specify a vessel endpoint at the origin of each vessel branch.</p>

---
