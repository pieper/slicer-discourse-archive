---
topic_id: 32704
title: "Lung Segmentation With Lungctsegmenter"
date: 2023-11-09
url: https://discourse.slicer.org/t/32704
---

# Lung segmentation with LungCTSegmenter

**Topic ID**: 32704
**Date**: 2023-11-09
**URL**: https://discourse.slicer.org/t/lung-segmentation-with-lungctsegmenter/32704

---

## Post #1 by @klc (2023-11-09 22:03 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a><br>
Dear Prof. Rudolf Bumm,</p>
<p>Hi, I am using the LungCTSegmenter to segment the lungs with AIrwaySegmentation, Vessel Segmentation following this video: <a href="https://www.youtube.com/watch?v=bw1IaxVkOM4&amp;ab_channel=medec021" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=bw1IaxVkOM4&amp;ab_channel=medec021</a><br>
The difference is that I use “total segmentator lung extended” instead of “lungmask r231”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2566ad57df33da2e5e987e81324eb314813cb884.png" alt="image" data-base62-sha1="5kREmVzRaHRM4VgjPOcd17i1EJ6" width="483" height="133"></p>
<p>The result is shown below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c384ed9348deaf059117ce880cbd7be85dc9e6.png" data-download-href="/uploads/short-url/f5D20LMR3wMT8raR1jpW5USPXRs.png?dl=1" title="Screenshot 2023-11-10 032330" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c384ed9348deaf059117ce880cbd7be85dc9e6_2_482x500.png" alt="Screenshot 2023-11-10 032330" data-base62-sha1="f5D20LMR3wMT8raR1jpW5USPXRs" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c384ed9348deaf059117ce880cbd7be85dc9e6_2_482x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c384ed9348deaf059117ce880cbd7be85dc9e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c384ed9348deaf059117ce880cbd7be85dc9e6.png 2x" data-dominant-color="8B859F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-10 032330</span><span class="informations">570×591 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72255111529391dd3f1c79088023ab2b4e9d258.jpeg" data-download-href="/uploads/short-url/wYHQQ7MyKYFzFLDqqZJbBCpL8cU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72255111529391dd3f1c79088023ab2b4e9d258.jpeg" alt="image" data-base62-sha1="wYHQQ7MyKYFzFLDqqZJbBCpL8cU" width="690" height="433" data-dominant-color="8E7E8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">862×541 74.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/705ac5762d78bbd5d7b591dce7b40caff4e8c76a.jpeg" data-download-href="/uploads/short-url/g1VX6MyPFR90DspSw7b5j5Bzu0q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/705ac5762d78bbd5d7b591dce7b40caff4e8c76a.jpeg" alt="image" data-base62-sha1="g1VX6MyPFR90DspSw7b5j5Bzu0q" width="690" height="457" data-dominant-color="7B7378"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">961×637 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>May I know what should be the vessels threshold value since it can be seen from the picture that the vessels are not segmenting well? it will perform even worse if I use the default values. I have tried different values with no luck<br>
Attached below please find the values<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e02526585f1d03921c0e68d5824e0a0bd623359.png" alt="image" data-base62-sha1="6z0WasOBGWQhViO0ZiR8vdoh4xP" width="495" height="286"></p>
<p>I also noticed that 2 of the videos your provide can yield good results of vessel segmentation, may I know is it possible that I can combine the work of airway segmentation with the lungSegmentation created from lungCTSegmenter and produced a merged OBJ as final. I can export them to OBJ using OPEN anatomy individually but I am not sure of how to combine them.</p><div class="youtube-onebox lazy-video-container" data-video-id="mcGqcxU5qBE" data-video-title="Airway Segmentation Tutorial" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=mcGqcxU5qBE" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/mcGqcxU5qBE/maxresdefault.jpg" title="Airway Segmentation Tutorial" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="9iiOBmaP8bA" data-video-title="Airway segmentation in 3D Slicer with &quot;Grow from Seeds&quot;" data-video-start-time="541s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=9iiOBmaP8bA&amp;t=541s" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/9iiOBmaP8bA/maxresdefault.jpg" title="Airway segmentation in 3D Slicer with &quot;Grow from Seeds&quot;" width="" height="">
  </a>
</div>

<p>Thank you very much.</p>
<p>Slicer: 5.4.0<br>
Pytorch:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c1666d507439e03541d3e4afc60f133a4434190.png" alt="image" data-base62-sha1="6i10fJY2sOmDOcDOecLwK4iJM0o" width="488" height="213"></p>

---

## Post #2 by @rbumm (2023-11-09 22:26 UTC)

<p>What you see is a typical airway/vessel leak.  Stat with airway segmentation → “low detail” and leave out vessel segmentation for a test.<br>
Ii is in he plans to offer a lung segmentation course during the upcoming PW week in Las Palmas. Jan 24.</p>

---

## Post #3 by @klc (2023-11-10 02:19 UTC)

<p>Thank you for your reply, I can obtain good results with only airway segmentation. But what I want to achieve is vessel segmentation. May I know if the lungCTSegmenter can’t produce good results with vessel segmentation at the moment?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f547df1751e521dbf5af84ff165f5c40b2dcdc7.jpeg" alt="WhatsApp Image 2023-11-09 at 15.00.39_b4319be3" data-base62-sha1="bjMK5v969t67QXj3igo7bPGhMJF" width="362" height="301"></p>
<p>Moreover, if I generate the airway from the “grow from seeds” function or airway segmentation module, is it possible that I can combine this result with the result I got from previous screenshot: e.g. lung Segmentation with airway segmentation enabled?</p>
<p>Thank you very much</p>

---

## Post #4 by @rbumm (2023-11-10 15:01 UTC)

<p>This is the kind of vesselmask you can automatically  generate with Lung CT Segmenter.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f001b5949b7de7c96d4a6a8fdc754eaf151f7cf.jpeg" data-download-href="/uploads/short-url/kp2vrwb6IFZXXelouQM0a828MUv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f001b5949b7de7c96d4a6a8fdc754eaf151f7cf.jpeg" alt="image" data-base62-sha1="kp2vrwb6IFZXXelouQM0a828MUv" width="609" height="500" data-dominant-color="858CA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">832×682 54.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is no differenciation between the pulmonary artery and vein.</p>

---

## Post #5 by @klc (2023-11-10 15:24 UTC)

<p>Thank you for your reply. May I know how can I acheive the result you posted in the comment?<br>
What vessel threshold should I set ?is there any tutorial that I can follow?</p>
<p>Thank you</p>
<p>「Rudolf Bumm via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;」在 2023年11月10日 週五，下午11:01 寫道：</p>

---

## Post #6 by @rbumm (2023-11-10 20:38 UTC)

<p>Yes, sure, here you are:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="w5vWBiZeJO4" data-video-title="Automatic lung, airway and vesselmask segmentation with Lung CT Segmenter and 3D slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=w5vWBiZeJO4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/w5vWBiZeJO4/maxresdefault.jpg" title="Automatic lung, airway and vesselmask segmentation with Lung CT Segmenter and 3D slicer" width="" height="">
  </a>
</div>


---

## Post #7 by @klc (2023-11-11 04:21 UTC)

<p>Thank you very much for your tutorial</p>

---

## Post #8 by @klc (2023-11-16 13:37 UTC)

<p>Dear rbumm,</p>
<p>After testing with numerous dataSets, I found that the dataSet from slicer in built demoChest CT produce the best results:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff3da3887ac66d228e5e21cd6e2f3cdf13d8db13.jpeg" data-download-href="/uploads/short-url/ApXOyJqfWgfWNKnHsWoNSgs5eCf.jpeg?dl=1" title="WhatsApp Image 2023-11-14 at 22.31.42_58f8232f" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff3da3887ac66d228e5e21cd6e2f3cdf13d8db13_2_598x500.jpeg" alt="WhatsApp Image 2023-11-14 at 22.31.42_58f8232f" data-base62-sha1="ApXOyJqfWgfWNKnHsWoNSgs5eCf" width="598" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff3da3887ac66d228e5e21cd6e2f3cdf13d8db13_2_598x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff3da3887ac66d228e5e21cd6e2f3cdf13d8db13.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff3da3887ac66d228e5e21cd6e2f3cdf13d8db13.jpeg 2x" data-dominant-color="898192"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2023-11-14 at 22.31.42_58f8232f</span><span class="informations">661×552 83.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, if I tried to use my own datasets obtained from:<br>
<a href="https://nbia.cancerimagingarchive.net/nbia-search/?MinNumberOfStudiesCriteria=1&amp;CollectionCriteria=Lung-PET-CT-Dx" class="onebox" target="_blank" rel="noopener nofollow ugc">https://nbia.cancerimagingarchive.net/nbia-search/?MinNumberOfStudiesCriteria=1&amp;CollectionCriteria=Lung-PET-CT-Dx</a><br>
I cant clearly show the airway segmentations:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b3a807803ae7d359e6527c778233b7c980c77b8.jpeg" data-download-href="/uploads/short-url/m9dlxQz75tD474VqdSGPQdqCA3u.jpeg?dl=1" title="WhatsApp Image 2023-11-09 at 14.47.33_c26497ae" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b3a807803ae7d359e6527c778233b7c980c77b8_2_683x500.jpeg" alt="WhatsApp Image 2023-11-09 at 14.47.33_c26497ae" data-base62-sha1="m9dlxQz75tD474VqdSGPQdqCA3u" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b3a807803ae7d359e6527c778233b7c980c77b8_2_683x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b3a807803ae7d359e6527c778233b7c980c77b8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b3a807803ae7d359e6527c778233b7c980c77b8.jpeg 2x" data-dominant-color="819093"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2023-11-09 at 14.47.33_c26497ae</span><span class="informations">809×592 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have also used the grow from seeds function to try to obtain better results but the result is shown above,</p>
<p>I have tried 3 different samples :<br>
and the results are more or less the same:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eb4d1610adb797ba0d5756badfc973e753e2c26.jpeg" alt="image" data-base62-sha1="2665hd4PuTvojEzj7wwHSsQ0IMm" width="482" height="500"></p>
<p>Do you think what are the possible problems?<br>
Do I need to do a little bit of preprocessing like resampling on the DICOM data before segmentation?</p>
<p>Thank you.</p>

---

## Post #9 by @rbumm (2023-11-16 17:40 UTC)

<p>My results using your widely spaced data are not as bad when I use Slicer 5.5.0 and CT calibration. However, there is still room for better airway segmentation. At least I do not get these nasty airway leaks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269d5abb93510dadcd5fd829245e28a4d3749655.jpeg" data-download-href="/uploads/short-url/5vBgZW4XvM9qJv0PGCd6Eonfqkt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/269d5abb93510dadcd5fd829245e28a4d3749655_2_595x500.jpeg" alt="image" data-base62-sha1="5vBgZW4XvM9qJv0PGCd6Eonfqkt" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/269d5abb93510dadcd5fd829245e28a4d3749655_2_595x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269d5abb93510dadcd5fd829245e28a4d3749655.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269d5abb93510dadcd5fd829245e28a4d3749655.jpeg 2x" data-dominant-color="918AA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">749×629 93.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for putting work into this.</p>
<p>So please use 3D Slicer 5.5.0 and the Totalsegmentator extension that belongs to it.</p>

---

## Post #10 by @klc (2023-11-23 16:38 UTC)

<p>Sorry for asking again. Sometimes this error will come out when there are too many images. Is there any way to configure the settings or prevent this from happening.</p>
<p>Thank you very much.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/309eda3781843df0a3722afc272617da02726bdd.png" data-download-href="/uploads/short-url/6W7g0TVruTRTr3Al2QTFIyyGjqR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309eda3781843df0a3722afc272617da02726bdd_2_690x429.png" alt="image" data-base62-sha1="6W7g0TVruTRTr3Al2QTFIyyGjqR" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309eda3781843df0a3722afc272617da02726bdd_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309eda3781843df0a3722afc272617da02726bdd_2_1035x643.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309eda3781843df0a3722afc272617da02726bdd_2_1380x858.png 2x" data-dominant-color="C8C5C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1499×933 360 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @pieper (2023-11-23 16:54 UTC)

<p>That just means you’ve run out of memory.  For best results, upgrade your computer.</p>

---

## Post #12 by @EvelynBundy (2023-12-07 11:54 UTC)

<p>To improve vessel segmentation, experiment with different threshold values. For combining airway and lung segmentation, export as separate OBJ files and merge using software like Blender.</p>

---

## Post #13 by @mau_igna_06 (2023-12-07 12:06 UTC)

<aside class="quote no-group" data-username="EvelynBundy" data-post="12" data-topic="32704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/c5a1d2/48.png" class="avatar"> EvelynBundy:</div>
<blockquote>
<p>For combining airway and lung segmentation, export as separate OBJ files and merge using software like Blender.</p>
</blockquote>
</aside>
<p>I think you can use CombineModels module from Sandbox Slicer’s extension for this</p>

---
