---
topic_id: 6307
title: "Problem In Cbct Volume Crop And Modeling Into Stl"
date: 2019-03-27
url: https://discourse.slicer.org/t/6307
---

# Problem in CBCT Volume Crop and Modeling into STL

**Topic ID**: 6307
**Date**: 2019-03-27
**URL**: https://discourse.slicer.org/t/problem-in-cbct-volume-crop-and-modeling-into-stl/6307

---

## Post #1 by @song (2019-03-27 12:25 UTC)

<p>Operating system: Window 10 (×64)<br>
Slicer version:  4.10.1 &amp;; 4.8.1<br>
Expected behavior: I am a graduate dental student and also new user of 3D Slicer. Now I expect to use 3D Slicer to crop the volume of hemi-mandible from a dental cone bean computed tomography (CBCT) and to make the model (STL-format file) as demonstrated in a YouTube tutorial video at <a href="https://www.youtube.com/watch?v=MKLWzD0PiIc&amp;amp;t=28s" class="inline-onebox" rel="noopener nofollow ugc">Tutorial: Preparing Data for 3D Printing Using 3D Slicer - YouTube</a> by 3D Slicer.<br>
Actual behavior:<br>
I was failed achieving the STL-format model for many times, even though I had following the same procedures as in the above video. Here I would like to pose the main procedures and outcomes as follows, and hope some experts or colleagues could help me point out what was the problem.</p>
<ol>
<li>Load DICOM data of patient CBCT into Slicer (Fig 1):</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44887e6d152286f6f5d87db51404051976c03c3c.jpeg" data-download-href="/uploads/short-url/9MgU5K1RYAhkezeFRpkpiyJ6WZK.jpeg?dl=1" title="Fig%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44887e6d152286f6f5d87db51404051976c03c3c_2_690x369.jpeg" alt="Fig%201" data-base62-sha1="9MgU5K1RYAhkezeFRpkpiyJ6WZK" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44887e6d152286f6f5d87db51404051976c03c3c_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44887e6d152286f6f5d87db51404051976c03c3c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44887e6d152286f6f5d87db51404051976c03c3c.jpeg 2x" data-dominant-color="C3C5C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%201</span><span class="informations">765×410 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>Adjust brightness &amp; contrast, and select the module of Volume Rendering (Preset: CT-Bone) (Fig 2):</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95f23729de2f79f955d8ab2cf4b215c8b2fc6995.jpeg" data-download-href="/uploads/short-url/lou5pRUYwMd0UeEpu8a5EpB2cbr.jpeg?dl=1" title="Fig%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95f23729de2f79f955d8ab2cf4b215c8b2fc6995_2_690x370.jpeg" alt="Fig%202" data-base62-sha1="lou5pRUYwMd0UeEpu8a5EpB2cbr" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95f23729de2f79f955d8ab2cf4b215c8b2fc6995_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95f23729de2f79f955d8ab2cf4b215c8b2fc6995_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95f23729de2f79f955d8ab2cf4b215c8b2fc6995_2_1380x740.jpeg 2x" data-dominant-color="99989A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%202</span><span class="informations">1920×1030 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="3">
<li>Enable “Crop” and define ROI (Fig 3):</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a00cf159c2b75ff88ef32ef03f74c96b56f5664.jpeg" data-download-href="/uploads/short-url/hphZ2rcdvHp23M33GP2sXaupH4E.jpeg?dl=1" title="Fig%203" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a00cf159c2b75ff88ef32ef03f74c96b56f5664_2_690x370.jpeg" alt="Fig%203" data-base62-sha1="hphZ2rcdvHp23M33GP2sXaupH4E" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a00cf159c2b75ff88ef32ef03f74c96b56f5664_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a00cf159c2b75ff88ef32ef03f74c96b56f5664_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a00cf159c2b75ff88ef32ef03f74c96b56f5664_2_1380x740.jpeg 2x" data-dominant-color="979699"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%203</span><span class="informations">1920×1030 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="4">
<li>Select and apply the module of Crop Volume （Fig 4）:<br>
Questions: According to the above tutorial, there should be only the selected ROI in three slice viewers. But in my practice, I found that the response is like the above picture after hitting “Apply”. Why is the response different as the video?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fd75ef3ac8748285fdf2b7ea4510ac83aa18e29.jpeg" data-download-href="/uploads/short-url/fXoqC3ZRji425ixPZr7cNFMG0OZ.jpeg?dl=1" title="Fig%204" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fd75ef3ac8748285fdf2b7ea4510ac83aa18e29_2_690x370.jpeg" alt="Fig%204" data-base62-sha1="fXoqC3ZRji425ixPZr7cNFMG0OZ" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fd75ef3ac8748285fdf2b7ea4510ac83aa18e29_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fd75ef3ac8748285fdf2b7ea4510ac83aa18e29_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fd75ef3ac8748285fdf2b7ea4510ac83aa18e29_2_1380x740.jpeg 2x" data-dominant-color="97969A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%204</span><span class="informations">1920×1030 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="5">
<li>Select and implement the module of Editor (Fig 5 &amp; 6):</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01e2feba0d847c1be791bbf8028e411a12b944c3.jpeg" data-download-href="/uploads/short-url/gGOlBpvr6WZHQgzqEmHXeHaizx.jpeg?dl=1" title="Fig%205" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01e2feba0d847c1be791bbf8028e411a12b944c3_2_690x373.jpeg" alt="Fig%205" data-base62-sha1="gGOlBpvr6WZHQgzqEmHXeHaizx" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01e2feba0d847c1be791bbf8028e411a12b944c3_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01e2feba0d847c1be791bbf8028e411a12b944c3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01e2feba0d847c1be791bbf8028e411a12b944c3.jpeg 2x" data-dominant-color="A7A6A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%205</span><span class="informations">778×421 62.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/183ba424a2ef520755828229418a134b1efcc350.jpeg" data-download-href="/uploads/short-url/3sneSk02LZ60B8weiQWFKhLYPn2.jpeg?dl=1" title="Fig%206" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/183ba424a2ef520755828229418a134b1efcc350_2_690x370.jpeg" alt="Fig%206" data-base62-sha1="3sneSk02LZ60B8weiQWFKhLYPn2" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/183ba424a2ef520755828229418a134b1efcc350_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/183ba424a2ef520755828229418a134b1efcc350_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/183ba424a2ef520755828229418a134b1efcc350_2_1380x740.jpeg 2x" data-dominant-color="97979A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%206</span><span class="informations">1920×1030 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="6">
<li>Label “mandible”, choose “ThresholdEffect” icon, adjust the threshold for mandible and hit “Apply” (Fig 7):</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c01bbfb195eb41c8efe57e5b6439917687719fb.jpeg" data-download-href="/uploads/short-url/1IdrBZiAVZZlN6YV4MC8vVjLUUP.jpeg?dl=1" title="Fig%207" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c01bbfb195eb41c8efe57e5b6439917687719fb_2_690x370.jpeg" alt="Fig%207" data-base62-sha1="1IdrBZiAVZZlN6YV4MC8vVjLUUP" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c01bbfb195eb41c8efe57e5b6439917687719fb_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c01bbfb195eb41c8efe57e5b6439917687719fb_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c01bbfb195eb41c8efe57e5b6439917687719fb_2_1380x740.jpeg 2x" data-dominant-color="9E9C9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%207</span><span class="informations">1920×1030 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="7">
<li>Choose “MakeModelEffect” and hit “Apply” (Fig 8):</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01aa597ab26fdd4a059ea224b54eb0aa11b2bb9.jpeg" data-download-href="/uploads/short-url/mQlu7HDEjxbohJMrJMOyGz5f4Mh.jpeg?dl=1" title="Fig%208" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a01aa597ab26fdd4a059ea224b54eb0aa11b2bb9_2_690x370.jpeg" alt="Fig%208" data-base62-sha1="mQlu7HDEjxbohJMrJMOyGz5f4Mh" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a01aa597ab26fdd4a059ea224b54eb0aa11b2bb9_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a01aa597ab26fdd4a059ea224b54eb0aa11b2bb9_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a01aa597ab26fdd4a059ea224b54eb0aa11b2bb9_2_1380x740.jpeg 2x" data-dominant-color="9E9C9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%208</span><span class="informations">1920×1030 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="8">
<li>Finally Save the data (Fig 9):<br>
Problem occurred in this dialogue. My target file “mandible” could not be found. I did not know why there were the last two .nrrd files which could not be converted into .stl format (nonavailable) in the drop-down list. Of course, finally I could not get the STL-format mandible model within my desired ROI. I hope someone could help me point out where were the problems as soon as possible, because I am very urgent to use it in my thesis. Thank you very much in advance.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e9d485b7783699f3053705823f47461587c78e.jpeg" data-download-href="/uploads/short-url/zeir45Uoq6rnPxgr4jHLo7vUx54.jpeg?dl=1" title="Fig%209" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e9d485b7783699f3053705823f47461587c78e_2_690x373.jpeg" alt="Fig%209" data-base62-sha1="zeir45Uoq6rnPxgr4jHLo7vUx54" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e9d485b7783699f3053705823f47461587c78e_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e9d485b7783699f3053705823f47461587c78e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e9d485b7783699f3053705823f47461587c78e.jpeg 2x" data-dominant-color="C5C3C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig%209</span><span class="informations">752×407 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-03-27 12:56 UTC)

<aside class="quote no-group" data-username="song" data-post="1" data-topic="6307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ecd19e/48.png" class="avatar"> song:</div>
<blockquote>
<p>Questions: According to the above tutorial, there should be only the selected ROI in three slice viewers. But in my practice, I found that the response is like the above picture after hitting “Apply”. Why is the response different as the video?</p>
</blockquote>
</aside>
<p>You may have multiple ROIs. Make sure you choose the correct one.</p>
<aside class="quote no-group" data-username="song" data-post="1" data-topic="6307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ecd19e/48.png" class="avatar"> song:</div>
<blockquote>
<p>Select and implement the module of Editor (Fig 5 &amp; 6):</p>
</blockquote>
</aside>
<p>The legacy “Editor” module is deprecated. You need to use “Segment editor” module instead.</p>
<p>Before you start editing, hide volume rendering so it does not overlap with the segmentation results that you want to see.</p>

---

## Post #3 by @song (2019-03-27 16:30 UTC)

<p>Hi, Mr. Iassoan, thank you very much for your good suggestions. For the 1st question, I succeed on my another laptop but still not work on the previous one even with the same operation procedure. So I had no idea for this problem. For the second problem, I can also succeed in the second computer. At this moment, I speculated that the final step - modeling by the Editor module might not work, because we could only see the .nrrd files but not the mandible. stl file existing. How do you think about that?</p>
<p>By the way, I still have some more questions for 3D Slicer.  First, my ultimate goal is to get the STL model of a mandible segment containing 4-teeth alveolar ridge with the two cutting cross-sections perpendicular to the long axis of posterior mandible.  I wonder whether I could achieve this goal using the module of Crop Volume. If not, is there any other modules that could enable the free-form cropping to achieve my above goal?  Second, if the answer to the last question is No,  I might still need to use the module of Crop Volume even though two cutting cross-sections are not perpendicular to the long axis of mandible. Under this circumstance, I tried some cases and found that the metal scatting from the artificial teeth (fixed dentures) will severely effect the following thresholding procedure. More importantly, later on I will use these STL files in the programs of Blender, Meshmixer for data refinement and Gom Inspect for the superimposition of two models. So I really need to remove the metal scatting to a great extent at these early steps to get a precise outcome. Could you tell me how to remove the metal scatting within the CBCT data in 3D Slicer? It will be better if you could provide me some tutorial videos for reference. Thank you very much.</p>

---

## Post #4 by @lassoan (2019-03-31 04:48 UTC)

<p>Use Segment Editor module, not the legacy Editor module.</p>
<p>Segment Editor provides Scissors effect, which allows you to cut segments without the need to crop the segmented volume - either free-form or with a rectangular shape.</p>
<p>You may be able to remove major metal artifacts by using Scissors effect and touch up using Paint and Erase.</p>

---

## Post #5 by @song (2019-03-31 05:51 UTC)

<p>Hi, thank you very much the same for your kindly suggestions, though I did it two days as you suggested after watching some Youtube tutorial videos. I have some other questions: as we know, the grayscale level of CBCT images is not so correlated to the bone density and Housefied Unit in multi-slice CT, which might cause not so accurate segmentation by manual thresholding. I am a dental student and not familiar too much with the computational functions or algorithms for image processing in 3D Slicer.  I wonder what modality and algorithm for the thresholding in 3D Slicer, global or local thresholding or others? Then, I am not sure the underlying rationale for the workflow from CBCT Dicom data to STL data through the sequential proccedures (CBCT data import—Volume—Segment Editor—Segementation—Export) .  According to my understanding, the process should be: DICOM Data Input — Bone Segmentation by Thresholding Techniques and Slice Edge Detection — Point Cloud Generation — Target Volume Refinement/Editing by Scissoring — Point Cloud Visualization — Surface Reconstruction/Point Cloud Conversion using Fitting or Interpolation Techniques into Watertight Polygon/Triangle Meshes (STL) / Surface through Various Computational Functions/Algorithms. Could you help me confirm it?  Thank you very much.</p>

---
