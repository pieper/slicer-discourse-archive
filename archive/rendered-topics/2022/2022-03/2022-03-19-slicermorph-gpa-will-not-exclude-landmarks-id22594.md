# SlicerMorph GPA will not exclude landmarks

**Topic ID**: 22594
**Date**: 2022-03-19
**URL**: https://discourse.slicer.org/t/slicermorph-gpa-will-not-exclude-landmarks/22594

---

## Post #1 by @Jasmine_Croghan (2022-03-19 00:36 UTC)

<p>Hi all,</p>
<p>I have run an auto3DGM analysis and used Markup to identify landmarks in areas I am not interested in, thinking I can easily exclude those landmarks for downstream analysis in SlicerMorph’s GPA module. I created a comma, not space, delimited list of those landmarks, and the python viewing window indicates that the landmarks were excluded, the analysis.log of the GPA indicates that the landmarks were excluded, but the results in the GPA module still contain the supposedly excluded landmarks.  What am I doing wrong here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/055979ff45cc9592ba35c708a310b000a974aa57.jpeg" data-download-href="/uploads/short-url/Lk5zSDkeKJYKX5FWApT9kXHfz9.jpeg?dl=1" title="Will_not_exclude_commas_no_space" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/055979ff45cc9592ba35c708a310b000a974aa57_2_690x375.jpeg" alt="Will_not_exclude_commas_no_space" data-base62-sha1="Lk5zSDkeKJYKX5FWApT9kXHfz9" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/055979ff45cc9592ba35c708a310b000a974aa57_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/055979ff45cc9592ba35c708a310b000a974aa57_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/055979ff45cc9592ba35c708a310b000a974aa57_2_1380x750.jpeg 2x" data-dominant-color="BFB9C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Will_not_exclude_commas_no_space</span><span class="informations">1915×1041 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For the record I’m using the latest (non-stable) build from github, as is required by auto3DGM according to the installation instructions.</p>
<p>Thanks for any help you can provide.</p>

---

## Post #2 by @muratmaga (2022-03-19 01:07 UTC)

<aside class="quote no-group" data-username="Jasmine_Croghan" data-post="1" data-topic="22594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jasmine_croghan/48/14714_2.png" class="avatar"> Jasmine_Croghan:</div>
<blockquote>
<p>but the results in the GPA module still contain the supposedly excluded landmarks.</p>
</blockquote>
</aside>
<p>How do you know that excluded landmarks are actually included in the GPA? How many landmarks did your auto3DGM analysis had? GPA reports 371 included landmarks for the analysis. Usually people specify some round numbers like 400-500 points in auto3Dgm.</p>

---

## Post #3 by @Jasmine_Croghan (2022-03-19 01:12 UTC)

<p>Hi, there were 512 original points, and all the output files have 371 landmarks. The ‘mean shape’ point cloud displays landmarks that were removed, like the highlighted landmark, 135.</p>

---

## Post #4 by @muratmaga (2022-03-19 12:07 UTC)

<p>If you have started with 512 and the gpa reports 371 LMs, then it means 141 LMs were excluded in the analysis.</p>
<p>I am not seeing any landmark numbers more than 371 on the screenshot, which tells me that after the exclusion the landmarks were reorderer consecutively. Thus your the landmark 135 in GPA output is not the same landmark as the excluded 135.</p>
<p>Do you want to retain the original LM indices?<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #5 by @Jasmine_Croghan (2022-03-19 12:52 UTC)

<p>Oh, interesting, you’re right there are no landmarks labelled higher than 371! The thing that really stumps me, though, is that all the landmarks that I removed are on the surface you see (inside the braincase), so there should be NO visible landmarks in this view. I have confirmed multiple times that there are landmarks where I have specifically removed them.</p>
<p>What could be making it redistribute landmarks? Is it somehow related to the auto3DGM landmarking method?</p>

---

## Post #6 by @muratmaga (2022-03-19 21:38 UTC)

<aside class="quote no-group" data-username="Jasmine_Croghan" data-post="5" data-topic="22594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jasmine_croghan/48/14714_2.png" class="avatar"> Jasmine_Croghan:</div>
<blockquote>
<p>What could be making it redistribute landmarks?</p>
</blockquote>
</aside>
<p>Hard to tell without looking at the data. Can you provide 3-4 lmk files, a model and the list of lm you want to be excluded?</p>

---

## Post #7 by @smrolfe (2022-03-19 23:23 UTC)

<p>One issue I see is that the landmark index in the exclusion list should correspond to the index in the control points table. This index starts at 1, so 0 is an invalid. I will add error catching to alert the user of this. If you can provide some sample landmark files we can check if there is something else going on too<br>
.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d67230881e4b660d4539156ff77c29594cbc526a.png" data-download-href="/uploads/short-url/uB4PnAlztY74nES68fpqW1TZ5qy.png?dl=1" title="Screen Shot 2022-03-19 at 4.15.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67230881e4b660d4539156ff77c29594cbc526a_2_446x500.png" alt="Screen Shot 2022-03-19 at 4.15.31 PM" data-base62-sha1="uB4PnAlztY74nES68fpqW1TZ5qy" width="446" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67230881e4b660d4539156ff77c29594cbc526a_2_446x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67230881e4b660d4539156ff77c29594cbc526a_2_669x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d67230881e4b660d4539156ff77c29594cbc526a_2_892x1000.png 2x" data-dominant-color="E8ECF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-03-19 at 4.15.31 PM</span><span class="informations">1450×1622 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @Jasmine_Croghan (2022-03-22 19:42 UTC)

<p>Interesting, I thought it would go by the name of the landmark. I will have to fix that on the next run. That may well be the issue! Currently waiting for it to finish another auto3DGM run that is taking quite a while. Here is a link for now of a couple of the .fcsv files, a .ply, and a list of landmarks to be removed.</p>
<p><a href="https://drive.google.com/drive/folders/1SuQfq9RE7V71z5hK8aNLgHDmLueMFVMr?usp=sharing" rel="noopener nofollow ugc">Link to requested files</a></p>
<p>Thank you for your help!</p>

---

## Post #9 by @muratmaga (2022-03-22 20:32 UTC)

<aside class="quote no-group" data-username="Jasmine_Croghan" data-post="8" data-topic="22594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jasmine_croghan/48/14714_2.png" class="avatar"> Jasmine_Croghan:</div>
<blockquote>
<p>I thought it would go by the name of the landmark.</p>
</blockquote>
</aside>
<p>That’s not possible, because there is no standard landmark naming convention. What if they are not numeric? Everything is based on the order of the landmarks.</p>
<p>I ran the samples provided, and I can confirm that GPA is definitely excluding the landmarks you have specified. But while doing that it also reorders them, so landmark names in the GPA output no longer matches the input. If this is critical for you, we might consider making that change. If so, please submit an feature request at <a href="https://github.com/SlicerMorph/SlicerMorph/issues" class="inline-onebox">Issues · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>Meanwhile, the scale of your dataset seems totally off. The coordinates are tiny. You may run into precision issues with such small coordinates. Make sure you are using the output from the auto3Dgm under OSS (original subject space) folder.</p>

---

## Post #10 by @Jasmine_Croghan (2022-03-22 20:35 UTC)

<p>Okay, I was wondering about how tiny those were!  I had always used the aligned landmarks and meshes in the R implementation, but I will switch to the OSS landmark output folder.</p>
<p>Thank you so much for helping me solve these issues! I was beyond frustrated last week and these are very simple solutions (to my ignorance).</p>
<p>-Jasmine</p>

---

## Post #11 by @muratmaga (2022-03-22 20:40 UTC)

<aside class="quote no-group" data-username="Jasmine_Croghan" data-post="10" data-topic="22594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jasmine_croghan/48/14714_2.png" class="avatar"> Jasmine_Croghan:</div>
<blockquote>
<p>Okay, I was wondering about how tiny those were! I had always used the aligned landmarks and meshes in the R implementation, but I will switch to the OSS landmark output folder.</p>
</blockquote>
</aside>
<p>If you are going to use aligned meshes and landmarks, you really shouldn’t do a GPA. Those are considered already superimposed (AFAIK).</p>

---

## Post #12 by @coco (2024-06-13 08:03 UTC)

<p>Interesting, I questionned that myself yesterday and wondered if indexes would shift after discarding landmarks so that you can keep track of landmarks by their displayed name. I think that change is needed if it has not been done so (I’ll check later)…</p>

---
