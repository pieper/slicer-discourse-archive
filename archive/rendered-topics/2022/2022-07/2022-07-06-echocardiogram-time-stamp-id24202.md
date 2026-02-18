# Echocardiogram time stamp

**Topic ID**: 24202
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/echocardiogram-time-stamp/24202

---

## Post #1 by @Deepthy_Rose_Jose_am (2022-07-06 12:08 UTC)

<p>Hello Everyone,<br>
I’m trying to render an 4D echocardiogram in Slicer3D. The data format is a 3D dcm exported from Qlab software. Please find the attached picture. The volume rendering feature doesn’t show the time stamp feature. And sequence browser wasn’t a help too. Could someone guide me on the same and point out if I am missing out something?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a097fff72c57d948973084e7f739b8f0e2f092.gif" alt="QLAB  2022-06-18 13-49-24 (5)" data-base62-sha1="3vRwQB4UZMI1mpz60Bxe68PjViW" width="640" height="337" class="animated"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a1f7224b18c96e67555a06cc8132852fc06444.png" data-download-href="/uploads/short-url/3vUt2S6pg6epmqNoe80YDIJLvWA.png?dl=1" title="SLICER VIEW" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_690x362.png" alt="SLICER VIEW" data-base62-sha1="3vUt2S6pg6epmqNoe80YDIJLvWA" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_1380x724.png 2x" data-dominant-color="848597"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SLICER VIEW</span><span class="informations">1912×1004 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-07-06 12:46 UTC)

<p>If you cannot select a sequence browser node in the toolbar (in <code>Select a ...eBrowser</code>) then it means you have loaded a single volume, not a volume sequence.</p>

---

## Post #3 by @Deepthy_Rose_Jose_am (2022-07-06 13:32 UTC)

<p>I wanted to do the mpr reconstruction of the volume with time stamp. the other format looks like the following. I’m able to simulate the heart beat but it is not a whole volume render. I wanted to simulate the 4th tab in qlab(previous thread) . Am I missing something?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d469c487fefe791c392b57c63edcc9077edb3112.jpeg" data-download-href="/uploads/short-url/uj5PstihkTenwIh6Up5nyr9ZYoa.jpeg?dl=1" title="view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d469c487fefe791c392b57c63edcc9077edb3112_2_690x391.jpeg" alt="view" data-base62-sha1="uj5PstihkTenwIh6Up5nyr9ZYoa" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d469c487fefe791c392b57c63edcc9077edb3112_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d469c487fefe791c392b57c63edcc9077edb3112_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d469c487fefe791c392b57c63edcc9077edb3112_2_1380x782.jpeg 2x" data-dominant-color="0F100D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">view</span><span class="informations">1398×794 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56677b43ac72db3e499797dba3f4a295a6af9f77.gif" alt="3D-Slicer-502-2022-07-06-18-58-4" data-base62-sha1="ckmLM0iXrem2ZLZWZd65frT9ReT" width="690" height="366" class="animated"></p>

---

## Post #4 by @lassoan (2022-07-06 14:41 UTC)

<aside class="quote no-group" data-username="Deepthy_Rose_Jose_am" data-post="3" data-topic="24202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepthy_rose_jose_am/48/13425_2.png" class="avatar"> Deepthy_Rose_Jose_am:</div>
<blockquote>
<p>I wanted to do the mpr reconstruction of the volume with time stamp. the other format looks like the following.</p>
</blockquote>
</aside>
<p>Those are just 2D screenshots. You can only get 4D volume Philips via Cartesian export from QLab.</p>

---

## Post #5 by @Deepthy_Rose_Jose_am (2022-07-07 12:23 UTC)

<p>The following data is a 3d dcm taken from QLab software. How can i show the animation for the same? Does the exported data from Qlab pose any issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a1f7224b18c96e67555a06cc8132852fc06444.png" data-download-href="/uploads/short-url/3vUt2S6pg6epmqNoe80YDIJLvWA.png?dl=1" title="SLICER VIEW" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_690x362.png" alt="SLICER VIEW" data-base62-sha1="3vUt2S6pg6epmqNoe80YDIJLvWA" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18a1f7224b18c96e67555a06cc8132852fc06444_2_1380x724.png 2x" data-dominant-color="848597"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SLICER VIEW</span><span class="informations">1912×1004 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-07-07 13:15 UTC)

<p>If you cannot select a sequence browser node in the toolbar (in <code>Select a ...eBrowser</code>) then it means you have loaded a single volume, not a volume sequence</p>
<p>What is the file size?</p>

---

## Post #7 by @Deepthy_Rose_Jose_am (2022-07-08 00:46 UTC)

<p>1385386 KB. This is the exported data from Qlab. It doesn’t come in asequence.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d99d3de0fe915b699f13f03029f8e377b6704770.jpeg" alt="file Size" data-base62-sha1="v36uZDN4i4gzl4hCCvnXuKaCW7C" width="655" height="108"></p>

---

## Post #8 by @lassoan (2022-07-08 03:06 UTC)

<p>This size is much larger than usual. Normally size of 4D cardiac ultrasound images are about a few 10 megabytes, while this file is more than a 1000 megabytes. It should definitely more than just a single volume.</p>
<p>How long was this recording (in seconds)?<br>
What transducer was used?<br>
Can you share a phantom or anonymized data set (upload to dropbox/onedrive/google drive and post the link) so that we can investigate?</p>

---

## Post #9 by @Deepthy_Rose_Jose_am (2022-07-08 03:46 UTC)

<p>The transducer used is X72 of Philips. The time shown is 4.15 seconds based on the qlab details as shown in the attached picture . Please find the attached google drive link: <a href="https://drive.google.com/drive/folders/1Nv_Aat3U3NohLkNzOK1rwP-QjMbA3apN?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">sample data - Google Drive</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3662cd3d0a6d2ac095227fdc9400a62d7e901e9.jpeg" data-download-href="/uploads/short-url/pB2nkKWnAm86NzvfOO4qcFwneiJ.jpeg?dl=1" title="time taken for recording" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3662cd3d0a6d2ac095227fdc9400a62d7e901e9_2_690x230.jpeg" alt="time taken for recording" data-base62-sha1="pB2nkKWnAm86NzvfOO4qcFwneiJ" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3662cd3d0a6d2ac095227fdc9400a62d7e901e9_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3662cd3d0a6d2ac095227fdc9400a62d7e901e9_2_1035x345.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3662cd3d0a6d2ac095227fdc9400a62d7e901e9_2_1380x460.jpeg 2x" data-dominant-color="232321"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">time taken for recording</span><span class="informations">1510×504 65.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2022-07-10 14:30 UTC)

<p>You’ve almost got it, the only step you missed was to fix up the invalid DICOM that QLab generates to a valid DICOM image, as described <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#import-philips-4d-cardiac-images">here</a>.</p>
<p>After patching, the image loads correctly:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/defacbdc02d3194e988477b07b2905b30a0f7376.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/defacbdc02d3194e988477b07b2905b30a0f7376.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/defacbdc02d3194e988477b07b2905b30a0f7376.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #11 by @Deepthy_Rose_Jose_am (2022-07-22 09:24 UTC)

<p>Hello lassoan ,<br>
Thank you for your quick reply! Was not physically well for a week. I will check this method and let you know at the earliest.</p>

---

## Post #12 by @Deepthy_Rose_Jose_am (2022-07-29 06:24 UTC)

<p>Hello Lassoan,</p>
<p>I’m glad to say I was able to obtain timestamp out of the data. I converted the data to nrrd files using philips dicom patcher and it helped in obtaining the timestamp.</p>
<ol>
<li>Also, could you please mention which modules you are using in the video you sent which is titled Preprocessing and Volume rendering.</li>
<li>If we convert the data in nrrd format to dcm using slicer 3d, would it retain the time stamp/ animation. When I tried it, the time stamp/animation was not retained. Am i missing something?</li>
<li>I wanted to visualise the said data in Unity3D. Does slicer3d has any module pertaining to it?</li>
</ol>

---

## Post #13 by @lassoan (2022-07-29 11:00 UTC)

<aside class="quote no-group" data-username="Deepthy_Rose_Jose_am" data-post="12" data-topic="24202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepthy_rose_jose_am/48/13425_2.png" class="avatar"> Deepthy_Rose_Jose_am:</div>
<blockquote>
<p>Also, could you please mention which modules you are using in the video you sent which is titled Preprocessing and Volume rendering.</p>
</blockquote>
</aside>
<p>That is the Echo Volume Render module that will be publicly released in SlicerHeart extension from tomorrow.</p>
<aside class="quote no-group" data-username="Deepthy_Rose_Jose_am" data-post="12" data-topic="24202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepthy_rose_jose_am/48/13425_2.png" class="avatar"> Deepthy_Rose_Jose_am:</div>
<blockquote>
<p>If we convert the data in nrrd format to dcm using slicer 3d, would it retain the time stamp/ animation. When I tried it, the time stamp/animation was not retained. Am i missing something?</p>
</blockquote>
</aside>
<p>Timestamps are preserved in the 4D nrrd file (saved by default as with .seq.nrrd extension).</p>
<aside class="quote no-group" data-username="Deepthy_Rose_Jose_am" data-post="12" data-topic="24202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepthy_rose_jose_am/48/13425_2.png" class="avatar"> Deepthy_Rose_Jose_am:</div>
<blockquote>
<p>I wanted to visualise the said data in Unity3D. Does slicer3d has any module pertaining to it?</p>
</blockquote>
</aside>
<p>Unity is just a good game engine. It has no built-in support for volume rendering (and just a few paid plugins that can do basic volume rendering), so you won’t be able to view echo volumes in any Unity-based applications without very significant development effort. Instead, I would recommend to use SlicerVirtualReality extension if you want to view 4D echo in virtual reality.</p>

---
