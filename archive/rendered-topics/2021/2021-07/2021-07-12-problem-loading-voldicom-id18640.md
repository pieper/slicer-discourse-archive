---
topic_id: 18640
title: "Problem Loading Voldicom"
date: 2021-07-12
url: https://discourse.slicer.org/t/18640
---

# Problem loading VolDICOM

**Topic ID**: 18640
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/problem-loading-voldicom/18640

---

## Post #1 by @TKhienwad (2021-07-12 12:36 UTC)

<p>Hi all,</p>
<p>I have a question regarding importing the VolDICOM format from echo images with 3D slicer. Does anyone know how to do that?</p>
<p>Best,</p>

---

## Post #2 by @lassoan (2021-07-12 14:10 UTC)

<p>There are many variants of GE .vol ultrasound files and Slicer can load most but not all of them. You need to install SlicerHeart extension and follow <a href="https://github.com/SlicerHeart/SlicerHeart#loading-ge-kretz-ultrasound-images">these instructions</a>.</p>

---

## Post #3 by @TKhienwad (2021-07-12 14:20 UTC)

<p>This is what I got when I drag and dropdown.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6997cc2b023007bbc250af630c64a4b5da054494.jpeg" data-download-href="/uploads/short-url/f47mgptKmgtNPnMCFksxXwKSsIc.jpeg?dl=1" title="PB1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6997cc2b023007bbc250af630c64a4b5da054494_2_690x373.jpeg" alt="PB1" data-base62-sha1="f47mgptKmgtNPnMCFksxXwKSsIc" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6997cc2b023007bbc250af630c64a4b5da054494_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6997cc2b023007bbc250af630c64a4b5da054494_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6997cc2b023007bbc250af630c64a4b5da054494.jpeg 2x" data-dominant-color="9191A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PB1</span><span class="informations">1281×693 87.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-07-12 15:13 UTC)

<p>This looks like screen capture video of the rendering on the ultrasound cart. It might be possible that along with the screen capture the image also contains 3D information, but GE cardiac images typically require you to install <a href="https://github.com/SlicerHeart/SlicerHeart#loading-various-3d4d-ultrasound-images-using-image3dapi">Image3dAPI</a>.</p>

---

## Post #5 by @TKhienwad (2021-07-15 14:30 UTC)

<p>Dear Andras,</p>
<p>Thank you very much for your response. I still did not get any response from GE. So I still could not download Image3dAPI. It was already three days. Is it normal?</p>
<p>Best regards,</p>
<p>Thananya</p>

---

## Post #6 by @lassoan (2021-07-15 14:34 UTC)

<p>It is summer, so things may take a bit longer. If you don’t hear from them by next week then you can try to contact them via twitter.</p>
<p>If you share an anonymized/phantom data set privately (send download link in a private message) then I can check if the Image3dAPI can read it correctly.</p>

---

## Post #7 by @TKhienwad (2021-07-15 14:37 UTC)

<p>Thank you so much for your quick response. How can I send direct message to you?</p>

---

## Post #8 by @lassoan (2021-07-16 22:18 UTC)

<p>Thank you, I’ve received the image.</p>
<p>It seems that GE’s Image3dAPI interface does not support this particular image.</p>
<p>However, I have a very good news: the image is uncompressed, Cartesian (scan-converted), therefore it is very easy to write a reader for it. You won’t even need GE’s reader for it.</p>
<p>I’ll be on vacation next week but I can put together a reader for it the week after. I’ll post here when the reader is ready.</p>

---

## Post #9 by @TKhienwad (2021-07-17 09:04 UTC)

<p>Hi Lassoan,</p>
<p>Thank you very much. Once you read it could you please tell me how you do it?</p>
<p>Have a wonderful holiday.</p>
<p>Thananya</p>

---

## Post #10 by @TKhienwad (2021-07-28 13:23 UTC)

<p>Dear Iassoan,</p>
<p>I hope you enjoy your vacation. May I ask you about the progress of the reader for the GE image data?</p>
<p>Best,</p>
<p>Thananya</p>

---

## Post #11 by @lassoan (2021-07-28 15:40 UTC)

<p>I’ve made some progress, but could not complete it. I won’t have time to work on it more this week, but will continue next week.</p>

---

## Post #12 by @TKhienwad (2021-07-29 07:35 UTC)

<p>Thank you very much for doing this. No worry, just work on it when you have time. Many thanks again.</p>
<p>Have a nice day</p>

---

## Post #13 by @TKhienwad (2021-09-15 13:09 UTC)

<p>Dear Lassoan,</p>
<p>I could already install the Image3DloaderGE from GE and rename the 3Decho file by puting .3dus at the end of the file. Then I drag and drop file into 3D slicer and attached error showed. Do you know what is a problem of reading this file?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbdf37745e231bbba82d920865cb5596d03a0daf.png" data-download-href="/uploads/short-url/vn4NW4sAS5n0GehBSia6NXc6JeD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbdf37745e231bbba82d920865cb5596d03a0daf_2_690x374.png" alt="image" data-base62-sha1="vn4NW4sAS5n0GehBSia6NXc6JeD" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbdf37745e231bbba82d920865cb5596d03a0daf_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbdf37745e231bbba82d920865cb5596d03a0daf_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbdf37745e231bbba82d920865cb5596d03a0daf_2_1380x748.png 2x" data-dominant-color="B9B8BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1043 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc786796eb0781336be14292747bf32d391ce0d5.png" data-download-href="/uploads/short-url/A1shSiqosnukWqNdlXs9v80gDel.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc786796eb0781336be14292747bf32d391ce0d5_2_690x373.png" alt="image" data-base62-sha1="A1shSiqosnukWqNdlXs9v80gDel" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc786796eb0781336be14292747bf32d391ce0d5_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc786796eb0781336be14292747bf32d391ce0d5_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc786796eb0781336be14292747bf32d391ce0d5_2_1380x746.png 2x" data-dominant-color="8F8E96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1039 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,</p>
<p>Thananya</p>

---

## Post #14 by @lassoan (2021-09-15 16:05 UTC)

<p>As I wrote above, GE’s GE_CVUS_Loader plugin (internal identifier: <code>GEHC_CARD_US.Image3dFileLoader</code>) that you get access to by default when ask for access using their web form, cannot read these “GE Vingmed Ultrasound” files.</p>
<p>For now, you can use <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess</a> to manually access single volumes. For example the module can create a header file like this, which allows you to load a volume:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: uchar
dimension: 3
space: left-posterior-superior
sizes: 180 203 180
space directions: (0.8569999999999999, 0.0, 0.0) (0.0, 0.591, 0.0) (0.0, 0.0, 0.8500000000000001)
kinds: domain domain domain
endian: big
encoding: raw
space origin: (0.0, 0.0, 0.0)
byte skip: 55681931
data file: P1_Echo1.3dus
</code></pre>
<p>I still plan to create a reader for these kind of images in SlicerHeart. I’ll update this topic when it’s ready.</p>

---

## Post #15 by @TKhienwad (2021-11-02 14:04 UTC)

<p>Dear Lassoan,</p>
<p>Thank you so much for your update. I just got a new 3D TEE dataset. Could you please help me check this dataset if I can do a segmentation?</p>
<p>Best regards,</p>
<p>Thananya</p>
<p><a href="https://drive.google.com/file/d/18zAqHQPTJGQL5OT_FCkJE_tXGpDEkh1W/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/18zAqHQPTJGQL5OT_FCkJE_tXGpDEkh1W/view?usp=sharing</a></p>

---
