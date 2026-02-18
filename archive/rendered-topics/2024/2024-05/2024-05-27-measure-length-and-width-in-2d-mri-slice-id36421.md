# Measure length and width in 2D MRI slice

**Topic ID**: 36421
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/measure-length-and-width-in-2d-mri-slice/36421

---

## Post #1 by @therapistlee (2024-05-27 15:57 UTC)

<p>Hello,</p>
<p>I am a new user of the 3D slicer community who is currently engaged in speech studies using MRI and seeking advice on using the 3D slicer program.</p>
<p>The aim of my study is to measure the length and width of the 2D vocal tract images captured by MRI using the 3D slicer.<br>
(The images obtained from the MRI have a resolution of 752x512 pixels, JPEG file)</p>
<p>My primary concern is whether the measurements taken using 3D slicer will correspond accurately to the actual dimensions (the matter of calibration).</p>
<p>As a novice in both 3D slicer program and MRI-related research, I would greatly appreciate any guidance or insights you could provide on this topic. Even the smallest piece of advice would be immensely helpful to me.</p>
<p>Thank you so much in advance!</p>
<p>Sincerely,</p>
<p>Jeong Min Lee<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b9957f3cf5b8c7d0e2242ee4a0309655fca9f69.jpeg" data-download-href="/uploads/short-url/1EBMVRkd4XVBVDg7QZ6jQDjaGdr.jpeg?dl=1" title="JML_ah" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b9957f3cf5b8c7d0e2242ee4a0309655fca9f69_2_684x500.jpeg" alt="JML_ah" data-base62-sha1="1EBMVRkd4XVBVDg7QZ6jQDjaGdr" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b9957f3cf5b8c7d0e2242ee4a0309655fca9f69_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b9957f3cf5b8c7d0e2242ee4a0309655fca9f69_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b9957f3cf5b8c7d0e2242ee4a0309655fca9f69_2_1368x1000.jpeg 2x" data-dominant-color="292423"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">JML_ah</span><span class="informations">1677×1225 71.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-05-27 18:50 UTC)

<p>It looks to me like you have loaded a screenshot instead of having the original MR in DICOM.  JPEG files don’t have spacing information so you need to specify it in the Volumes module to get accurate measurements.  Way better would be to get the DICOM.</p>

---

## Post #3 by @therapistlee (2024-06-07 08:08 UTC)

<p>Thank you for your reply!<br>
I got the original DICOM file (which is a real-time MRI file during speech production) from our research.</p>
<p>Using this DICOM file, I have several questions:</p>
<ol>
<li>
<p>I measured the length between the tongue and the soft palate using the ‘Create New Line’ function from a 3d slicer. Is there a better/more accurate way to measure?</p>
</li>
<li>
<p>I’m also trying to measure the volume of the oral cavity during vowel production in this DICOM file. However, I’m a novice 3D slicer. Could you recommend any wiki pages or how-to pages for me to try the volume segmentation and measurement?</p>
</li>
<li>
<p>When I open the real-time MRI files using 3d slicer, I’ve noticed that it doesn’t show all the information. That is, the files do not show all speech movements conducted from the study. Could someone help me with opening (or understanding how to open) real-time MRI files using a 3D slicer?</p>
</li>
</ol>
<p>Thank you so much for all your guidance.<br>
It is a tremendous help for our research!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9079ddfd2e42b5cf96cfb871f4bddd00e41cae0a.png" data-download-href="/uploads/short-url/kC5R0e1gjJasZWHSaUsqzHhmcBA.png?dl=1" title="HBC_dicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9079ddfd2e42b5cf96cfb871f4bddd00e41cae0a_2_690x409.png" alt="HBC_dicom" data-base62-sha1="kC5R0e1gjJasZWHSaUsqzHhmcBA" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9079ddfd2e42b5cf96cfb871f4bddd00e41cae0a_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9079ddfd2e42b5cf96cfb871f4bddd00e41cae0a_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9079ddfd2e42b5cf96cfb871f4bddd00e41cae0a_2_1380x818.png 2x" data-dominant-color="9D9E9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HBC_dicom</span><span class="informations">2548×1513 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2024-06-08 23:18 UTC)

<aside class="quote no-group" data-username="therapistlee" data-post="3" data-topic="36421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/therapistlee/60/78299_2.png" class="avatar"> therapistlee:</div>
<blockquote>
<p>I measured the length between the tongue and the soft palate using the ‘Create New Line’ function from a 3d slicer. Is there a better/more accurate way to measure?</p>
</blockquote>
</aside>
<p>Yes, using a Markup line makes sense.</p>
<aside class="quote no-group" data-username="therapistlee" data-post="3" data-topic="36421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/therapistlee/60/78299_2.png" class="avatar"> therapistlee:</div>
<blockquote>
<p>I’m also trying to measure the volume of the oral cavity during vowel production in this DICOM file. However, I’m a novice 3D slicer. Could you recommend any wiki pages or how-to pages for me to try the volume segmentation and measurement?</p>
</blockquote>
</aside>
<p>It’s not clear if you have a volume sequence (3D) or just a series of 2D slices.  You can’t get an accurate volume calculation if you only have 2D.  See the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">SegmentStatistics</a> module for more info on 3D calculations.</p>
<aside class="quote no-group" data-username="therapistlee" data-post="3" data-topic="36421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/therapistlee/60/78299_2.png" class="avatar"> therapistlee:</div>
<blockquote>
<p>When I open the real-time MRI files using 3d slicer, I’ve noticed that it doesn’t show all the information. That is, the files do not show all speech movements conducted from the study. Could someone help me with opening (or understanding how to open) real-time MRI files using a 3D slicer?</p>
</blockquote>
</aside>
<p>That information is probably not in the DICOM files.  You can look at the DICOM metadata to confirm, but probably you need to get the info from somewhere else, like something that was recorded at the time of the acquisition.</p>

---
