---
topic_id: 14655
title: "Head Circumference Or Cranial Deformation Measures From Ct"
date: 2020-11-17
url: https://discourse.slicer.org/t/14655
---

# Head circumference or cranial deformation measures from CT

**Topic ID**: 14655
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/head-circumference-or-cranial-deformation-measures-from-ct/14655

---

## Post #1 by @Gonzalo_Rojas_Costa (2020-11-17 04:10 UTC)

<p>Hi:<br>
How can I measure the head circumference or cranial deformation measures using CT and 3D Slicer? Automatic or semi-automatic method.</p>

---

## Post #2 by @lassoan (2020-11-17 05:26 UTC)

<p>Circumference: <a href="https://discourse.slicer.org/t/measure-the-circumference-of-an-object/13079" class="inline-onebox">Measure the circumference of an object</a></p>
<p>Cranial deformation can be assessed many ways. What would you like to quantify exactly?</p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2021-02-19 13:28 UTC)

<p>I only know the two methods that appears in the book that I attached… <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e8fd96103cc693daf92138aa22ba197aa0b8746.jpeg" data-download-href="/uploads/short-url/bcZr9RhJrN7BfGf7qpDiClRkSZo.jpeg?dl=1" title="20200413_153624" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8fd96103cc693daf92138aa22ba197aa0b8746_2_375x500.jpeg" alt="20200413_153624" data-base62-sha1="bcZr9RhJrN7BfGf7qpDiClRkSZo" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8fd96103cc693daf92138aa22ba197aa0b8746_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8fd96103cc693daf92138aa22ba197aa0b8746_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8fd96103cc693daf92138aa22ba197aa0b8746_2_750x1000.jpeg 2x" data-dominant-color="CFC4B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200413_153624</span><span class="informations">3024×4032 1.09 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92bd5a6678109ac98dea4c7ca0adc2b9af7b5bff.jpeg" data-download-href="/uploads/short-url/kW7oFtDMM2ErFU8DWxajZAC3OzR.jpeg?dl=1" title="20200413_153729" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92bd5a6678109ac98dea4c7ca0adc2b9af7b5bff_2_375x500.jpeg" alt="20200413_153729" data-base62-sha1="kW7oFtDMM2ErFU8DWxajZAC3OzR" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92bd5a6678109ac98dea4c7ca0adc2b9af7b5bff_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92bd5a6678109ac98dea4c7ca0adc2b9af7b5bff_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92bd5a6678109ac98dea4c7ca0adc2b9af7b5bff_2_750x1000.jpeg 2x" data-dominant-color="CDC2B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200413_153729</span><span class="informations">3024×4032 1.25 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you know any automatic method with 3D Slicer that measures that? I have the CT images and the cranial mesh. Or do you know any method to measure cranial deformation?</p>

---

## Post #4 by @lassoan (2021-02-19 14:17 UTC)

<p>You can write a script that automatically identifies points and planes and computes all values. However, developing such a script may take several days (plus learning of some Python, numpy, VTK, Slicer if you are not familiar with these), so it may not pay off if you just need to measure a few hundred cases and otherwise you would not want to spend time with learning and programming.</p>
<p>Probably a good tradeoff is to automatically get points and planes that are easy to compute automatically (e.g., superior and posterior planes) and provide some landmark points manually. Then, from the list of planes and points it should be trivial to compute distances, angles, etc.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> are there any general morphometrics tools that could be used here?</p>

---

## Post #5 by @muratmaga (2021-02-19 15:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="14655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> are there any general morphometrics tools that could be used here?</p>
</blockquote>
</aside>
<p>I am not aware of any automated tools for this. <a class="mention" href="/u/ezgimercan">@ezgimercan</a> was working on similar questions, she might have some suggestions.</p>

---

## Post #6 by @ezgimercan (2021-02-19 18:37 UTC)

<p>I would suggest the closed curve method as in the topic <a class="mention" href="/u/lassoan">@lassoan</a> shared.</p>
<p>My only suggestion would be to use the CT with the reformat tool to get the axial plane you want to measure the circumference at. Then mark a closed curve on the reformatted axial plane.</p>
<p>Ideally, if you also have the model (mesh) for the CT (you can create it easily with Threshold and Islands tools in Segment Editor), you can get away with marking 3-4 points on the CT and resampling it on the model.</p>
<p>Most of these steps can be automated in Python but I don’t have any scripts for it.</p>

---

## Post #7 by @Chuan (2022-12-06 16:14 UTC)

<p>Hi Gonzalo,</p>
<p>Recently I also have the same question. Did you find a good way to measure the head shape information?</p>
<p>Best,<br>
Chen</p>

---

## Post #8 by @Gonzalo_Rojas_Costa (2022-12-06 16:32 UTC)

<p>No. I don´t found any good way to measure the head shape. I think that the ShapePopulationViewer extension could be useful, but I haven’t test it.</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #9 by @lassoan (2022-12-06 17:08 UTC)

<p>You can visualize in slice views all the measurement planes that are shown in the book, and then you can use line and curve markup tools to make the measurements. Let us know if you have any difficulty in either finding a good slice view or measuring distance or curve length.</p>

---

## Post #10 by @Chuan (2022-12-07 12:34 UTC)

<p>Hi Lassoan,</p>
<p>I am trying with your method. But I may meet a basic question of how to adjust my slice position at the first step. I put a figure here, where the yellow and red lines are interaction plane. Could you tell me how could I adjust the head position to make the yellow line in the middle of the head (like this black line.)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/859ae9a09707112150a235a059698a294414b53b.jpeg" alt="image" data-base62-sha1="j3VoWr44BDvRy6R1KCcZBlHLe2L" width="546" height="386"></p>

---

## Post #11 by @Chuan (2022-12-07 13:25 UTC)

<p>Aha, I can manually adjust the angle in transform. Now I figure it out.</p>

---

## Post #12 by @Chuan (2022-12-07 13:30 UTC)

<p>Hi Gonzalo,</p>
<p>Could you tell me the name of this book? I am looking for the formal measurement method for heads. If you know the literature about the regulated way for measuring the head, I will appreciate.</p>

---

## Post #13 by @Gonzalo_Rojas_Costa (2022-12-07 14:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0960e4016023b292adba96c1062ee740a59de07a.jpeg" data-download-href="/uploads/short-url/1kXSPXHL2GRf0tBF2eysxfkAfA6.jpeg?dl=1" title="20200413_153816" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0960e4016023b292adba96c1062ee740a59de07a_2_375x500.jpeg" alt="20200413_153816" data-base62-sha1="1kXSPXHL2GRf0tBF2eysxfkAfA6" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0960e4016023b292adba96c1062ee740a59de07a_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0960e4016023b292adba96c1062ee740a59de07a_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0960e4016023b292adba96c1062ee740a59de07a_2_750x1000.jpeg 2x" data-dominant-color="827566"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200413_153816</span><span class="informations">1920×2560 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @Gonzalo_Rojas_Costa (2022-12-07 14:51 UTC)

<aside class="quote no-group" data-username="Chuan" data-post="12" data-topic="14655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>o</p>
</blockquote>
</aside>
<p>And will the SlicerMorph extension be useful to measure cranial deformation ?</p>

---

## Post #15 by @Gonzalo_Rojas_Costa (2022-12-07 14:52 UTC)

<p>And will the SlicerMorph extension be useful to measure cranial deformation ?</p>

---

## Post #16 by @muratmaga (2022-12-07 16:21 UTC)

<p>SlicerMorph provides tools for landmark based shape analysis and visualization. While it can be useful, if you are doing lengths and ratios for skull deformation, there is not much to offer to you.</p>

---

## Post #17 by @Chuan (2022-12-09 15:34 UTC)

<p>I have not tried that. But one method could be export the stl first and import the stl to Meshy, where you can directly measure the circumference.<br>
<a href="https://0x00019913.github.io/meshy/" rel="noopener nofollow ugc">Meshy (0x00019913.github.io)</a></p>

---

## Post #18 by @Chuan (2022-12-09 15:37 UTC)

<p>Hello Muratmaga, could you please tell me what is the name for that tool of landmark based shape analysis and visualization? It could be very useful for me. Because currently what I am doing is extract the landmarks’ locations and do the regression analysis to investigate the relationship between skull shape information and the skull morphology.</p>

---

## Post #19 by @muratmaga (2022-12-09 15:40 UTC)

<p>It is the GPA module in slicermorph. It does Procrustes superimposition and PCA decomposition of gpa aligned coordinates. However for regression analyses you need to either use tools in R, or write your own python snippets.</p>
<p>You can find more information at <a href="https://GitHub.com/slicermorph/Slicermorph" class="inline-onebox">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in Slicer</a></p>

---

## Post #20 by @Chuan (2022-12-09 15:40 UTC)

<p>Hi Gonzalo, I didn’t find the pdf version of this book. But could you please help me have a look to see whether it also records the regulated method for skull circumference measurement?<br>
I want to know how they measure the skull/</p>

---

## Post #21 by @Chuan (2022-12-09 15:43 UTC)

<p>Aha, gotcha, Now I see. I have my own code already, seems it does the same thing. Thanks for your reply, and hope you have a nice weekend!</p>

---

## Post #22 by @Gonzalo_Rojas_Costa (2022-12-09 18:26 UTC)

<p>Hi Chuan. But, what does your code do?</p>

---

## Post #23 by @lassoan (2022-12-10 00:39 UTC)

<p>I’ve uploaded a short video that shows how to find the correct measurement planes and perform circumference and distance measurements in 2D and 3D:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="l81bhCrWfYs" data-video-title="Simple 2D and 3D measurements on CT image" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l81bhCrWfYs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l81bhCrWfYs/maxresdefault.jpg" title="Simple 2D and 3D measurements on CT image" width="" height="">
  </a>
</div>


---

## Post #24 by @Chuan (2022-12-12 14:21 UTC)

<p>PCA similar analysis</p>

---
