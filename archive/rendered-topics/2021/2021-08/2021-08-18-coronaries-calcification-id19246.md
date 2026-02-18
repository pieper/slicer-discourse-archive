# Coronaries Calcification

**Topic ID**: 19246
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/coronaries-calcification/19246

---

## Post #1 by @Elias_Karabelas (2021-08-18 09:30 UTC)

<p>Dear Team,<br>
I managed to segment an aorta and a coronary tree with VMTK and Slicer. However for my case I would also like to extract calcifications present in the coronaries. I managed to threshold the calcifications, but from what I got from clinicians the calcifications are not completely surrounded by lumen. So I would need a way to make the calcifications stick to parts of the wall. Is there any way of achieving this? I attached a screenshot of my current segmentation.</p>
<p>Best regards<br>
Elias</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d69062f5bb80e3226cd9fd81d622189b6bb9b7f.jpeg" data-download-href="/uploads/short-url/8Lg8C1aNE0qZB7O4OBG7Fn0P2Wz.jpeg?dl=1" title="Bildschirmfoto vom 2021-08-18 11-24-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d69062f5bb80e3226cd9fd81d622189b6bb9b7f_2_690x287.jpeg" alt="Bildschirmfoto vom 2021-08-18 11-24-20" data-base62-sha1="8Lg8C1aNE0qZB7O4OBG7Fn0P2Wz" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d69062f5bb80e3226cd9fd81d622189b6bb9b7f_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d69062f5bb80e3226cd9fd81d622189b6bb9b7f_2_1035x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d69062f5bb80e3226cd9fd81d622189b6bb9b7f_2_1380x574.jpeg 2x" data-dominant-color="989A9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto vom 2021-08-18 11-24-20</span><span class="informations">1920×800 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2021-08-20 18:11 UTC)

<p>Hi,</p>
<p>This is an interesting project.<br>
Cant´you just “hollow” the vessel segmentation, then “add” the calcification segmentation via “logical operators” ?</p>
<p>Regards<br>
rudolf</p>

---

## Post #3 by @Elias_Karabelas (2021-09-01 09:11 UTC)

<p>Hi Rudolf,<br>
thanks for your answer. I tried this but since the hollow algorithm removes symmetrically it will shrink the lumen also at the side where there’s no calcification present or?</p>

---

## Post #4 by @rbumm (2021-09-02 08:54 UTC)

<p>Do you have a test dataset available?</p>

---

## Post #5 by @Elias_Karabelas (2021-09-16 12:17 UTC)

<p>Hi, sorry for the late response, I was on vacation.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://box.medunigraz.at/s/A4iNN7zDrECXXKw">
  <header class="source">
      <img src="https://box.medunigraz.at/themes/mug/core/img/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://box.medunigraz.at/s/A4iNN7zDrECXXKw" target="_blank" rel="noopener nofollow ugc">Box @ Medical University of Graz</a>
  </header>

  <article class="onebox-body">
    <img src="https://box.medunigraz.at/core/img/favicon-fb.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://box.medunigraz.at/s/A4iNN7zDrECXXKw" target="_blank" rel="noopener nofollow ugc">segmentation_new</a></h3>

  <p>Box @ Medical University of Graz - Sustainable living. learning. researching.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>under this link you will find the dataset I’m currently working on.</p>
<p>best regards<br>
Elias</p>

---

## Post #6 by @rbumm (2021-09-19 14:56 UTC)

<p>I was able to download the data.</p>
<p>Isn´t that quite good already for planning an intervention?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c3383678f679a3ea9070c597c4a4a093c9c432.jpeg" data-download-href="/uploads/short-url/a5ZG5U1mgShqDLHSv3EHmg8Ccb8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46c3383678f679a3ea9070c597c4a4a093c9c432_2_613x499.jpeg" alt="image" data-base62-sha1="a5ZG5U1mgShqDLHSv3EHmg8Ccb8" width="613" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46c3383678f679a3ea9070c597c4a4a093c9c432_2_613x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46c3383678f679a3ea9070c597c4a4a093c9c432_2_919x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c3383678f679a3ea9070c597c4a4a093c9c432.jpeg 2x" data-dominant-color="989BCE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×895 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @rbumm (2021-09-19 15:29 UTC)

<p>Made the “COMBINED” segment hollow with a thickness of 0.3 mm and enabled the “CALC” segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35fd9ee8428f481e2f76b0f43ea83c9ef9bee414.jpeg" data-download-href="/uploads/short-url/7HCGwo4k6JTAKq4f3F23Q1Sy3KQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fd9ee8428f481e2f76b0f43ea83c9ef9bee414_2_690x449.jpeg" alt="image" data-base62-sha1="7HCGwo4k6JTAKq4f3F23Q1Sy3KQ" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fd9ee8428f481e2f76b0f43ea83c9ef9bee414_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fd9ee8428f481e2f76b0f43ea83c9ef9bee414_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35fd9ee8428f481e2f76b0f43ea83c9ef9bee414.jpeg 2x" data-dominant-color="7D899D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1353×881 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @Elias_Karabelas (2021-09-21 12:29 UTC)

<p>Hi Rudolf,</p>
<p>yes I’m also quite happy with the segmentation, but the cardiologists I showed this dataset to told me that the calcifications are too much floating in the coronaries, they need to be stuck closest to the lumen wall, that’s why I started to redo some things and asked myself if I can get around without to much manual work.</p>

---

## Post #9 by @rbumm (2021-09-21 17:04 UTC)

<p>First of all, I think you need to rework your calcification (CALC) segmentation a bit.</p>
<p>This slice</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ec1553ea70c15dba2efd38de09bbf61e4ae8f6.png" alt="image" data-base62-sha1="ap6bpqFyRGWJ4PCL9Lyauh5lWt0" width="404" height="344"></p>
<p>produces this segmentation:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64368ab87ef6a70ecfa1282010ec820f3464e2a1.png" alt="image" data-base62-sha1="eiwBlVAReRCvAy8fKPHV5Fuk8j7" width="442" height="359"></p>
<p>which may just be a little overdone in size and smoothed too much.</p>
<p>From the literature, the thickness of the coronary artery wall is around 0.75 mm.</p>
<p>Use this as the thickness in the “Hollow” tool With the hollow tool settings of</p>
<p><em>thickness: 0.75 and</em><br>
<em>Use current segment as: medial surface</em></p>
<p>I get this result</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8507dd5b322030260678cad21f3385ae2ab3c3de.jpeg" alt="image" data-base62-sha1="iYQlV3GIAY4553A5PdGTrjofgQu" width="450" height="364"></p>
<p>with your segmentation which leaves the calcifications sticking or very close to the artery walls.<br>
If you rework the CALC segmentation maybe you can switch to</p>
<p><em>Use current segment as: inside surface</em></p>
<p>which should actually be the case here.</p>

---

## Post #10 by @rbumm (2021-09-21 18:17 UTC)

<p>… you may also try a combination of volume rendering as shown here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="aeOFl19fh_c" data-video-title="Coronary vessel segmentation on cardiac CT images" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=aeOFl19fh_c" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/aeOFl19fh_c/maxresdefault.jpg" title="Coronary vessel segmentation on cardiac CT images" width="" height="">
  </a>
</div>

<p>and adding the calcifications as separate segmentations</p>

---

## Post #11 by @ames (2021-09-23 06:13 UTC)

<p>Hi Elias,</p>
<p>May I ask how you segmented the coronary arteries and what threshold you are using to identify the calcifications? Thanks in advance!</p>

---

## Post #12 by @chir.set (2021-10-09 17:13 UTC)

<aside class="quote no-group" data-username="Elias_Karabelas" data-post="8" data-topic="19246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elias_karabelas/48/11286_2.png" class="avatar"> Elias_Karabelas:</div>
<blockquote>
<p>the calcifications are too much floating in the coronaries, they need to be stuck closest to the lumen wall</p>
</blockquote>
</aside>
<p>I could segment the LAD with <a href="https://github.com/chir-set/MetaCenterlineExtraction/tree/main/CurveCenterlineExtraction/" rel="noopener nofollow ugc">this</a> tool (with calcifications outside the lumen). The key part is placing control points as close as possible to its center for such small arteries. That’s tedious still.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b05ae23316db4b53f5c8c7f6414067084c14ccd7.jpeg" data-download-href="/uploads/short-url/pa6KCFWizLAiQwcIQiVECRDKPhd.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05ae23316db4b53f5c8c7f6414067084c14ccd7_2_683x499.jpeg" alt="Screenshot" data-base62-sha1="pa6KCFWizLAiQwcIQiVECRDKPhd" width="683" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05ae23316db4b53f5c8c7f6414067084c14ccd7_2_683x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05ae23316db4b53f5c8c7f6414067084c14ccd7_2_1024x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05ae23316db4b53f5c8c7f6414067084c14ccd7_2_1366x998.jpeg 2x" data-dominant-color="1C1D1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1842×1347 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Used parameters :</p>
<p>27 control points<br>
Intensity tolerance : 60<br>
Neighbourhood size : 2.0<br>
Tube diameter : 4 mm</p>
<p>The calcifications were segmented with usual tools of the ‘Segment editor’:<br>
Threshold<br>
Masking<br>
Paint : with sphere brush in 3D.</p>
<p>Centerline extraction failed, I suppose because of a very tight stenosis.</p>
<p>N.B : This tool is still experimental and not conventional inside. And it’s one tube at a time.</p>
<p>Regards.</p>

---

## Post #14 by @suculent (2025-05-19 14:23 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> Can you share which tool you used (link doesn’t work), is this tool available as a module in 3D Slicer?</p>

---

## Post #15 by @chir.set (2025-05-19 14:40 UTC)

<aside class="quote no-group" data-username="suculent" data-post="14" data-topic="19246">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/suculent/48/80131_2.png" class="avatar"> suculent:</div>
<blockquote>
<p>(link doesn’t work)</p>
</blockquote>
</aside>
<p>Yep, I even forgot I ever had this repository.</p>
<p>It’s <code>Guided artery segmentation</code> module in the <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerVMTK</a> extension. Many things have changed since this post. If you have segmented a coronary, you can segment the calcifications very quickly with <code>Arterial calcification pre-processor</code> module in the same extension. Other kinds of tinkering can be helpful to segment coronaries when they are not too diseased, it’s still tedious however. Since I don’t work with these arteries, I did not spend too much time with this.</p>

---

## Post #16 by @liam26 (2025-12-22 22:33 UTC)

<p>I’m trying to evaluatate calcification, but I’m a bit confussed on your process. I used the arterial calcification pre-processor. Is that a subsitute for using threshold?</p>

---

## Post #17 by @chir.set (2025-12-23 07:53 UTC)

<aside class="quote no-group" data-username="liam26" data-post="16" data-topic="19246">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/858c86/48.png" class="avatar"> liam26:</div>
<blockquote>
<p>a subsitute</p>
</blockquote>
</aside>
<p>No, it’s just one more tool. You can use any tool with which you are comfortable. With <code>Arterial calcification pre-processor</code>, you need a lumen segment first, that’s the hardest part, for tiny blood vessels like coronaries.</p>

---
