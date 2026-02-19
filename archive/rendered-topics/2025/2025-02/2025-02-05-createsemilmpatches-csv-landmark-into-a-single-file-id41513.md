---
topic_id: 41513
title: "Createsemilmpatches Csv Landmark Into A Single File"
date: 2025-02-05
url: https://discourse.slicer.org/t/41513
---

# CreateSemiLMPatches CSV Landmark into a Single File

**Topic ID**: 41513
**Date**: 2025-02-05
**URL**: https://discourse.slicer.org/t/createsemilmpatches-csv-landmark-into-a-single-file/41513

---

## Post #1 by @Esra_Karacan (2025-02-05 10:48 UTC)

<p>Operating system:Windows 10<br>
Slicer version:5.6.2<br>
Expected behavior: I am facing technical problems in the process of converting the selected landmarks into a single file using the ‘CreateSemiLMPatches’ module in the program and converting this file to CSV format. How can I solve this problem?<br>
Actual behavior: how can I solve this problem?</p>

---

## Post #2 by @muratmaga (2025-02-05 15:41 UTC)

<p><a class="mention" href="/u/esra_karacan">@Esra_Karacan</a></p>
<p>So you have multiple markup files and you want to turn them into a single file and save it as csv? Is that correct?</p>
<p>if so, you can do this manually copying the control points from one markup object to the other. Go to the Markups module, expand the control points select all points and copy them<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc868481ef581d8006efc9a4519c226c79e42d6.png" data-download-href="/uploads/short-url/aXfEPmiD3TPFRfRPo21ikQazsKW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cc868481ef581d8006efc9a4519c226c79e42d6_2_387x500.png" alt="image" data-base62-sha1="aXfEPmiD3TPFRfRPo21ikQazsKW" width="387" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cc868481ef581d8006efc9a4519c226c79e42d6_2_387x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc868481ef581d8006efc9a4519c226c79e42d6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc868481ef581d8006efc9a4519c226c79e42d6.png 2x" data-dominant-color="D3E1EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">536×691 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Open your excel or any other spreadsheet program, and then paste these values.Then move on to the next markup object and repeat the procedure.</p>
<p>If you have lots of files, this is a fairly tedious and error prone process. In that case you might want to write a small python or R script to read and flatten your landmarks into a single CSV.</p>
<p>May I ask why you are doing that? For example if your goal is to do shape analysis, you can do it inside the Slicer via SlicerMorph extension and not have to do any of this. If you can tell more about your use case, we might be able to help you better.</p>

---

## Post #3 by @Esra_Karacan (2025-02-05 21:51 UTC)

<p>In my mandible shape analysis I want to create semi-landmarks between the homologous points I have selected in the Markups module. However, when I go to the CreateSemiLMPatches module, only the points I have selected as F_1 and F_2 appear in the Landmark Set field and therefore I cannot create the semi-landmarks.<br>
Do I have to do it manually using Markups Control Point to create a landmark set?</p>
<p>I wanted to upload a picture but I couldn’t because the system doesn’t allow it, I apologize.</p>

---

## Post #4 by @muratmaga (2025-02-05 23:43 UTC)

<p>You</p>
<aside class="quote no-group" data-username="Esra_Karacan" data-post="3" data-topic="41513">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/esra_karacan/48/79341_2.png" class="avatar"> Esra_Karacan:</div>
<blockquote>
<p>However, when I go to the CreateSemiLMPatches module, only the points I have selected as F_1 and F_2 appear in the Landmark Set field and therefore I cannot create the semi-landmarks.</p>
</blockquote>
</aside>
<p><code>CreateSemiLMPatches</code> will require at least three points. It creates triangular patches of dense semiLMs. You can look at the tutorial here. <a href="https://github.com/SlicerMorph/Tutorials/tree/main/CreateSemiLMPatches" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/CreateSemiLMPatches at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>However, we have now introduced a new method that is more flexible than those triangular patches. You may want to check that out. It is called <code>PlaceLandmarkGrid</code>. Take a look at the tutorial first: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GridBasedLandmarking" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/GridBasedLandmarking at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #5 by @Esra_Karacan (2025-02-06 00:25 UTC)

<p>Thank you very much for your suggestion. I will look at the PlaceLandmarkGrid method which is more flexible compared to the triangle patch method. I will review the tutorial first.</p>

---
