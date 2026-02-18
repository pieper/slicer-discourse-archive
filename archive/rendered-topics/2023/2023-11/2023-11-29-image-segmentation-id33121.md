# Image segmentation

**Topic ID**: 33121
**Date**: 2023-11-29
**URL**: https://discourse.slicer.org/t/image-segmentation/33121

---

## Post #1 by @S_Esmaeili (2023-11-29 17:49 UTC)

<p>i have many 2d dicoms and want to segment them with bounding box, could someone please help me about the easiest way to segment them? (actually, i want to determine the segmentation parts(names, colors,…) for once and then use it for segmenting other images)<br>
also i have another problem, when i load a new image, bounding boxes that i have drawn for the previous image is shown in the new image. how can i address this problem?</p>

---

## Post #2 by @yuanw (2023-11-30 07:42 UTC)

<p>you can use the Total Segmentator extension.</p>

---

## Post #3 by @S_Esmaeili (2023-12-01 15:28 UTC)

<p>thank you. when running total segmentator i get this message: No module named ‘torch’</p>

---

## Post #4 by @rbumm (2023-12-01 18:27 UTC)

<p>Please install torch with the Pytorch extension first. Keep in mind that you need a computer with a strong GPU to run AI programs like TotalSegmentator.</p>

---

## Post #5 by @S_Esmaeili (2023-12-01 19:53 UTC)

<p>Thanks, i installed pytorch extension but i get this message" Failed to compute results. No module named ‘torch’ " again.</p>

---

## Post #6 by @muratmaga (2023-12-01 19:56 UTC)

<p>Did you actually run the pytorch extension? (i.e., switch to Pytorch utils and choose automatic install)?</p>

---

## Post #7 by @S_Esmaeili (2023-12-07 20:29 UTC)

<p>i used extension manager and install total segmentator. pytorch extension installed automatically beside total segmentator.<br>
i install them on my laptop, which does not have very high GPU( NVDIA GeForce MX) could it be because of this?</p>

---

## Post #8 by @muratmaga (2023-12-07 21:07 UTC)

<p>Your error is torch library is missing.</p>
<p>Extension manager just installs the extension. I don’t know how totalsegmentator is doing, it but it is still worthwhile to switch (CTRL+F) pyTorch utils and check that torch is installed. If its not, hit automatic install and the module will load the torch most appropriate for your computer (if you don’t have Nvidia GPU, it will install the CPU version of torch).</p>

---

## Post #9 by @S_Esmaeili (2023-12-08 20:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e643697c15bb30bd017f47a0c7cf7e7bbf1a7be7.jpeg" data-download-href="/uploads/short-url/wR0fmKqVXyd4qdvWeKtfsKureRh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e643697c15bb30bd017f47a0c7cf7e7bbf1a7be7_2_477x500.jpeg" alt="image" data-base62-sha1="wR0fmKqVXyd4qdvWeKtfsKureRh" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e643697c15bb30bd017f47a0c7cf7e7bbf1a7be7_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e643697c15bb30bd017f47a0c7cf7e7bbf1a7be7_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e643697c15bb30bd017f47a0c7cf7e7bbf1a7be7.jpeg 2x" data-dominant-color="E0E0DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">797×834 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
yes it’s not installed.</p>

---

## Post #10 by @muratmaga (2023-12-09 01:08 UTC)

<p>What happens when you click Install PyTorch button?</p>

---

## Post #11 by @S_Esmaeili (2023-12-09 07:14 UTC)

<p>This message appears. I tried Uninstaller and then installed it again. But there is no difference.</p>
<p>در تاریخ شنبه ۹ دسامبر ۲۰۲۳،‏ ۰۴:۳۸ Murat Maga via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt; نوشت:</p>

---

## Post #12 by @muratmaga (2023-12-09 23:07 UTC)

<p>Does the path you have installed Slicer and the extensions contain any non-English characters? Those occassionally cause some problems. Perhaps try installing something like C:\Slicer and then try installing the pytorch extension, and running the automatic installation.</p>

---
