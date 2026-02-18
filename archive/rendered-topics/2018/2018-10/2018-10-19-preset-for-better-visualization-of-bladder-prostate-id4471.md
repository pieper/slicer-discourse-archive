# Preset for better visualization of bladder/prostate.

**Topic ID**: 4471
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/preset-for-better-visualization-of-bladder-prostate/4471

---

## Post #1 by @AJR (2018-10-19 18:07 UTC)

<p>As the title suggests, I am hoping to find a preset which will give me a better visualization of the bladder/prostate area.  I’ve been searching all over and have so far been unsuccessful.</p>
<p>3d Slicer is a bit complex and I am just starting out with it so I am not really familiar with all the ins and outs.  Any help would be most appreciated.</p>
<p>Thanks in advance</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-10-19 18:09 UTC)

<p>What imaging modality do you have? What is the purpose of visualization, what exactly you would like to see? Would you like to visualize in 2D or 3D? Have you segmented the bladder and prostate or would you be ready to do it?</p>

---

## Post #3 by @AJR (2018-10-19 18:50 UTC)

<p>Thanks for the reply.</p>
<p>Not sure what you mean by modality, but I am using dicomm images from a CT scan and using the volume renderer.  I have cropped the image down to that area.  Not sure how to go about segmenting, unless that’s the same thing.  Would prefer 3d, but probably wouldn’t hurt to have 2d as well.  I am hoping to see the overall condition of the general area with respect to cancer, or other abnormalities.  I’m ready any time - I’ve been spending hours on trying to figure this stuff out.  As an old geezer I’m not as quick on my feet or as sharp as I used to be.</p>
<p>Thanks again!!</p>

---

## Post #4 by @lassoan (2018-10-19 18:57 UTC)

<p>Prostate is barely visible in CT images. Due to lack of contrast between image intensity of prostate and surrounding structures, you will not get good quality volume rendering.</p>
<p>You can segment images using Segment Editor module and then you can visualize the prostate and any other structures very nicely. There are manual and automatic tools - you can find several tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a>.</p>

---

## Post #5 by @AJR (2018-10-21 11:30 UTC)

<p>I think what you are suggesting is that to really get a good image it needs to be separated out?  One of the problems I am having is even seeing it, due to it’s unusual size (BPH), the pelvic bones, and my inexperience looking at this stuff.  It doesn’t seem very well defined.  I was thinking if the bone could be separated out I might be able to see it more clearly.  I looked at the tutorials you suggested but that stuff seems complicated to me.</p>
<p>Thanks again for your reply.</p>

---

## Post #6 by @lassoan (2018-10-21 12:21 UTC)

<aside class="quote no-group" data-username="AJR" data-post="5" data-topic="4471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/74df32/48.png" class="avatar"> AJR:</div>
<blockquote>
<p>One of the problems I am having is even seeing it</p>
</blockquote>
</aside>
<p>If a human cannot discern a structure then the computer has no chance to do it at all. Using <em>Paint</em> or <em>Draw</em> effect on all slices will work for sure but somewhat tedious work. You can make the process faster by segmenting only on a few slices using <em>Paint</em> or <em>Draw</em> effect (probably 4-6 slices would be enough) and then create a complete segmentation using <em>Fill between slices</em> effect. You may <em>Watershed</em> method (available after you install <em>SegmentEditorExtraEffects</em> extension), which requires you to paint seed regions inside and outside the prostate (it works similarly to <em>Grow from seeds</em> effect, which is demonstrated in several tutorials).</p>
<p>On CT images, you can segment bones easily by Threshold effect.</p>
<aside class="quote no-group" data-username="AJR" data-post="5" data-topic="4471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/74df32/48.png" class="avatar"> AJR:</div>
<blockquote>
<p>I looked at the tutorials you suggested but that stuff seems complicated to me.</p>
</blockquote>
</aside>
<p>Yes, it is not easy, but probably you cannot avoid learning this if you want to work in this field. If you have any specific questions then let us know.</p>

---

## Post #7 by @AJR (2018-10-22 01:05 UTC)

<p>That all sounds like gobbledegook to me!  lol…  I have no plans to make a living with this stuff, it’s just for my own personal use for my health problems.  It was easy enough to get the images loaded and volume render them, but the rest is over my head.  I assumed that it would be easy and had no idea how much would be involved.   Perhaps someone will be kind enough to offer to do it for me or walk me through it.  I wouldn’t mind learning it, but the tutorials I’ve seen so far don’t really help me.</p>
<p>Thanks again…</p>

---

## Post #8 by @lassoan (2018-10-22 03:51 UTC)

<aside class="quote no-group" data-username="AJR" data-post="7" data-topic="4471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/74df32/48.png" class="avatar"> AJR:</div>
<blockquote>
<p>I have no plans to make a living with this stuff, it’s just for my own personal use</p>
</blockquote>
</aside>
<p>It is perfectly understandable that you are not confident in interpreting the images and not sure what to do with them. However, in this case I’m not sure how we could help you.</p>

---

## Post #9 by @AJR (2018-10-22 05:04 UTC)

<p>I can’t possibly interpret the images without first being able to see the relevant data (prostate/bladder).  If nothing else I would like to get a visualization of the size of the prostate (doctor says it is 20x normal) and with any luck, scope for cancer cells, which AFAICT my doctor is leaning more towards just BPH.  But I’d like to see that for myself.  I would rest a bit easier, and have a better grasp of what I am dealing with.</p>
<p>I did run into one tutorial which seems to have helped by breaking down a couple of barriers, but it is still a daunting process.  I’ll try to slog through it but so far most of the tutorials were not designed for dummies like me.  I understand now what segmentation is at least, so that’s a start.  My first goal is to strip the bone structure out because I think that is impairing a good 3d view.</p>
<p>Anyhow, hopefully as I get stuck you will be around to answer some questions.  I would really appreciate it.</p>
<p>Thanks…</p>

---

## Post #10 by @fedorov (2018-10-22 12:12 UTC)

<p><a class="mention" href="/u/ajr">@AJR</a> CT is not the optimal modality for visualizing prostate cancer. It is used for radiotherapy planning (and in that case, I am pretty sure it is used to contour just the prostate gland, but not the tumor region), but it would be unusual if it was acquired for evaluation. It does not sound from your posts that radiotherapy treatment is being planned in your case. Perhaps you are looking at an incidental finding on a CT scan? Typically MRI is done for detection and staging of suspected disease. There many papers that compare various imaging approaches for prostate cancer, if you are interested. Here’s one: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4777886/">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4777886/</a>.</p>

---

## Post #11 by @gcsharp (2018-10-22 14:23 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>  Yes, but I would normally expect a 20x size difference to be apparent in CT.</p>
<p><a class="mention" href="/u/ajr">@AJR</a> There is insufficient contrast of the prostate gland in CT to easily view using volume rendering. I recommend using the 2D viewers (“Four-up”) instead. You will need to familiarize yourself with human anatomy.  It takes time, but you will get there.</p>
<p>Below is a 2D sagittal view, first unannotated, and then with bladder (green), prostate (yellow), and rectum (red) outlined.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6da4e2ccb93c9eaca8e9fc73b24eea2468564a7.png" alt="Selection_204" data-base62-sha1="nO2YAkTGNWomjKolUrkCPxwe99B" width="555" height="414"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd7dfb232c3160a48204e1e41c7f8b48c8beafe3.png" alt="Selection_203" data-base62-sha1="vBpqUpa2zioA8Xyhg7WSBWZgnxV" width="555" height="414"></p>

---

## Post #12 by @fedorov (2018-10-22 15:11 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> yes, I was just wondering why CT was acquired in the first place. Is it commonly used to assess BPH? Or maybe it is used when no alternative is available at the practice.</p>

---

## Post #13 by @AJR (2018-10-23 23:30 UTC)

<p>i am not sure why doc ordered CT as I would have preferred an MRI, but the catalyst for him ordering anything was gross hematuria, which I had one occurrence of.  I have a high PSA but I refuse to have a biopsy taken,   Doctor says based on the results of the CT he just thinks now that it is BPH.  I’ll have to ask him for clarification.</p>
<p>Thanks for the link - I’ll check it out…<br>
<a class="mention" href="/u/gcsharp">@gcsharp</a> - thanks for the pics…</p>

---
