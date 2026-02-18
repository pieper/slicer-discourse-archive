# DICOM and STL don't match.

**Topic ID**: 22114
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/dicom-and-stl-dont-match/22114

---

## Post #1 by @Asagami-Fujino (2022-02-22 13:49 UTC)

<p>I loaded the DICOM (it is a TRUS image) and the STL (the segmentation result) but the result turned out like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e24591551c6cddaac90c9ac12fdb4ca6626d19a.jpeg" data-download-href="/uploads/short-url/khrFUwyIgmaohBtr9GRN7IdrOBA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e24591551c6cddaac90c9ac12fdb4ca6626d19a_2_690x376.jpeg" alt="image" data-base62-sha1="khrFUwyIgmaohBtr9GRN7IdrOBA" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e24591551c6cddaac90c9ac12fdb4ca6626d19a_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e24591551c6cddaac90c9ac12fdb4ca6626d19a_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e24591551c6cddaac90c9ac12fdb4ca6626d19a_2_1380x752.jpeg 2x" data-dominant-color="43434D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1048 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The DICOM volume and the STL model did not match. So how to solve this problem?</p>

---

## Post #2 by @cpinter (2022-02-22 15:12 UTC)

<p>You will need to tell us more about how this data was created.</p>

---

## Post #3 by @Asagami-Fujino (2022-02-22 15:34 UTC)

<p>the data were downloaded from Prostate-MRI-US-Biopsy, TCIA (URL: <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=68550661" class="inline-onebox" rel="noopener nofollow ugc">Prostate MRI and Ultrasound With Pathology and Coordinates of Tracked Biopsy (Prostate-MRI-US-Biopsy) - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a>), and I simply chose the 0001case. The MRI image matched the model but the US did not. I think it might due to the mismatch of the two docs in origin or space.</p>

---

## Post #4 by @fedorov (2022-02-22 18:58 UTC)

<p><a class="mention" href="/u/asagami-fujino">@Asagami-Fujino</a> did you follow the “Instructions for the proper use of the STL files” outlined on the collection page under “Detailed description”?</p>
<p><a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=68550661#68550661171ba531fc374829b21d3647e95f532c" class="onebox" target="_blank" rel="noopener">https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=68550661#68550661171ba531fc374829b21d3647e95f532c</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e8022e4885df7f449f44a19d8a9dd831700deca.png" data-download-href="/uploads/short-url/mC9YcRaGKS7DDOJjD1U7Vc1imfg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e8022e4885df7f449f44a19d8a9dd831700deca_2_690x261.png" alt="image" data-base62-sha1="mC9YcRaGKS7DDOJjD1U7Vc1imfg" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e8022e4885df7f449f44a19d8a9dd831700deca_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e8022e4885df7f449f44a19d8a9dd831700deca_2_1035x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e8022e4885df7f449f44a19d8a9dd831700deca_2_1380x522.png 2x" data-dominant-color="E7E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1430×542 98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Asagami-Fujino (2022-02-23 01:55 UTC)

<p>yeah，I simply followed the procedure without any ajustment.</p>

---

## Post #6 by @fedorov (2022-02-23 16:28 UTC)

<p>I’ve just tried that for case 0001, and it worked for me as demonstrated in the screenshot below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5298720f2c9a47478a9856832e7d371fe5574f0.jpeg" data-download-href="/uploads/short-url/s8b29j2l0e0f99x0YjXcYCNGm6A.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5298720f2c9a47478a9856832e7d371fe5574f0_2_521x500.jpeg" alt="image" data-base62-sha1="s8b29j2l0e0f99x0YjXcYCNGm6A" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5298720f2c9a47478a9856832e7d371fe5574f0_2_521x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5298720f2c9a47478a9856832e7d371fe5574f0_2_781x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5298720f2c9a47478a9856832e7d371fe5574f0_2_1042x1000.jpeg 2x" data-dominant-color="5C5D5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1078×1033 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Make sure you install SlicerHeart extension prior to loading US series. Your screenshots potentially indicate US volumes were not loaded correctly. Without SlicerHeart geometry of the series will not be parsed.</p>
<p>I have to say, I next tried to repeat the steps, but it didn’t work for me. I experienced unexpected behavior with the transforms, where it would not apply when I drag the surface under the transform in the Data module (I am not sure if that is a bug or expected behavior). I then tried to repeat the steps with stable release, but was unable to install SlicerHeart extension/dependencies. I am not sure what is going on, but I do not have time to debug this.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7114d1dc723b40109a21e18f92e35e9c8fa2dd2c.png" alt="image" data-base62-sha1="g8myJQ5MdgQfF7lZgK41IELIdsw" width="463" height="224"></p>

---

## Post #7 by @lassoan (2022-02-23 19:41 UTC)

<p>The popup indicates that installation of these extensions have not completed yet (still in progress, most likely due to network communication error). Click OK to continue to wait. If you still get this popup after 10 minutes then restart Slicer and try again. If it still fails then describe the exact steps that you perform and we’ll try to reproduce it.</p>
<p>I’ve just tried installing SlicerProstate and SlicerIGT extensions on macOS with Slicer-4.13.0 2022-02-16 and everything was OK.</p>

---

## Post #8 by @Asagami-Fujino (2022-02-24 02:46 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="22114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>licerHear</p>
</blockquote>
</aside>
<p>Thanks! I finally found that simply dragging the dicom file may cause this problem. And I tried to load the dicom and the result seemed ok. Your suggestion really helps me a lot!</p>

---
