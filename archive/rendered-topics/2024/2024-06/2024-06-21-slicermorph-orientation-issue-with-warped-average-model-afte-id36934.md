---
topic_id: 36934
title: "Slicermorph Orientation Issue With Warped Average Model Afte"
date: 2024-06-21
url: https://discourse.slicer.org/t/36934
---

# Slicermorph orientation issue with warped/average model after GPA

**Topic ID**: 36934
**Date**: 2024-06-21
**URL**: https://discourse.slicer.org/t/slicermorph-orientation-issue-with-warped-average-model-after-gpa/36934

---

## Post #1 by @coco (2024-06-21 09:19 UTC)

<p>Dear Murat,<br>
What I have done below is to run a GPA on three landmark sets for a single reference brain, done all three by three users.<br>
I’m still facing another issue regarding making an average model.<br>
as you can see from the image below, where I have my segments and markups on the left and the PCA warped volume on the right which is inverted relative to the original coordinates and somehow a bit larger than my original volume even though the two should be identical.<br>
There seem to be orientation issues here, could you advise ?<br>
thanks again</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40cfd95c19e82742cec8ab658b030015d09457e2.jpeg" data-download-href="/uploads/short-url/9flS6xz4PxZzxPYGB5IzLQOX0MW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40cfd95c19e82742cec8ab658b030015d09457e2_2_645x500.jpeg" alt="image" data-base62-sha1="9flS6xz4PxZzxPYGB5IzLQOX0MW" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40cfd95c19e82742cec8ab658b030015d09457e2_2_645x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40cfd95c19e82742cec8ab658b030015d09457e2_2_967x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40cfd95c19e82742cec8ab658b030015d09457e2_2_1290x1000.jpeg 2x" data-dominant-color="8D8EA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1745×1351 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-06-21 16:11 UTC)

<p>I think there are bunch of things going on here:</p>
<ol>
<li>GPA 3D visualization would work on a “single” model. So you have to merge all those segments into a single model and then try.</li>
<li>I never seen flip like you shown before, and I suspect that because you actually not looking at the real reference model, but segmentation (since GPA cannot input a bunch of segmentation).</li>
</ol>
<p>I think if you take care of those issues, you should be able to get an correctly average model. Or if you can share your data, I can try to take a look.</p>

---

## Post #3 by @coco (2024-06-22 05:26 UTC)

<p>Dear Murat,<br>
I apologise, did not explain myself properly.<br>
I used a single model indeed (made of all segments into one single model). But I wanted to show the flip relative to the original segments and I’m still unsure where this is coming from. I’ll look into this a bit more but please confirm that when creating models from a segment then doing the GPA+PCA should not change orientation of your models relative to original segments, correct?<br>
As for the average model, yes, I can now do it, very easy indeed.<br>
Many thanks</p>

---

## Post #4 by @muratmaga (2024-06-22 05:57 UTC)

<aside class="quote no-group" data-username="coco" data-post="3" data-topic="36934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>please confirm that when creating models from a segment t</p>
</blockquote>
</aside>
<p>There is randomness in how GPA aligned coordinates are calculated. These may or may not be in the same orientation of your original data. (for example if you had one model that’s in a different orientation then everything else, and that get’s picked up as the first specimen to align everything else, then yes, things maybe flipped with respect to most other things). So in short GPA coordinates are only internally consistent, they almost guaranteed not to be in the same space as the original data (because the reference coordinate system is arbitrary and centered on the mean shape of the data).</p>
<p>Why do you want the GPA mean shape model to be in the same orientation as your original volume?</p>
<p>what are you trying to do specifically?</p>

---

## Post #5 by @coco (2024-06-22 06:25 UTC)

<p>Thanks again for your prompt reply,<br>
I’m learning but most likely still lack basic understandings so there may be inconstancies in my dataset I have not seen yet but as far as I can tell, all models and segments are centered, and in the correct (A/P, S/I, L/R) and same orientation from the start. So the flipping is strange. I’m still investigating.</p>
<p>What I wanted to do: I have fiducials created by three users and I was trying to get the average of these three sets in the same 3D space as the original dataset. I was wrong as I assumed doing the GPA could get me the mean fiducials coordinates I was looking for. How should I do it instead ?<br>
Also, I’m not sure you noticed in the figure posted earlier but one of my “annotators” has procrustes distances twice as high as the two others even though they all use the same segments to place their landmarks. This is also something I have not figured out yet.</p>
<p>One problem arising from averaged fiducials is how I then project these averaged fiducials on the correct surface of the original model used for placing fiducials. If there’s a way to do this, one additional difficulty is that my model is made of 24 segments combined into one single file. So if I end up with a point, not on a surface, it may get projected on a different surface that it is supposed to be on.</p>
<p>Again, thank you for your help and great work for the community<br>
s</p>

---

## Post #6 by @muratmaga (2024-06-22 14:04 UTC)

<aside class="quote no-group" data-username="coco" data-post="5" data-topic="36934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>What I wanted to do: I have fiducials created by three users and I was trying to get the average of these three sets in the same 3D space as the original dataset. I was wrong as I assumed doing the GPA could get me the mean fiducials coordinates I was looking for. How should I do it instead</p>
</blockquote>
</aside>
<p>This depends on whether those three “annotators” have landmark the same sample (three different landmarking attempts of the same scan), or all did different scans. If the former, because the coordinate space is defined by that single scan, you can simply average them. No need to align or do GPA on them.  But then there is no point in trying to reconstruct a “mean model” out of this, since you have only one specimen anyway. So probably this is not what you are doing.</p>
<p>If you are doing the latter, then you are doing it right.</p>
<aside class="quote no-group" data-username="coco" data-post="5" data-topic="36934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>Also, I’m not sure you noticed in the figure posted earlier but one of my “annotators” has procrustes distances twice as high as the two others even though they all use the same segments to place their landmarks. This is also something I have not figured out yet.</p>
</blockquote>
</aside>
<p>If you have one surface landmarked by three different people, the PD will reflect differences in the interpretation how these annotators placed the landmarks. PD is not a very good metric to evaluate this type of variation since it is dimensionless. You probably want to evaluate this in the world coordinate, i.e., take the average of three as I described before. This is your best guess for location of landmarks. Then you can calculate how different each annoator is, and since this will be in millimeters (or microns) you can then decide this type of variation is something you are comfortable with or not.</p>
<p>If you have three different surfaces from three different scans, the PD are bound to be different, because their shapes are different.</p>
<aside class="quote no-group" data-username="coco" data-post="5" data-topic="36934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>One problem arising from averaged fiducials is how I then project these averaged fiducials on the correct surface of the original model used for placing fiducials.</p>
</blockquote>
</aside>
<p>This is generally not possible. If you have three shapes their average after alignment will create a new space, and this has nothing to do with the original data anymore. That’s why you need to specifically have both a model and its corresponding set of manual landmarks to visualize it as a 3D model (GPA mean coordinate to manual landmark set is used to create a mapping between those two, and then that mapping is applied to the model for visualization). Otherwise we would have asked for only the model.</p>
<p>But then if you have one surface landmarked three times by three people, it is not meaningful to try to extract a mean shape model, since you only have one thing.</p>
<p>I am still a little blurry about what you are trying to do.</p>
<p>If you have multiple different models landmarked, you can create a mean model. This model is guaranteed not to be in the orientation of your origina data. if you want to bring your original data to this orientation (not sure why you would want to do that) you can use FastModelAlign to rigidily register them.</p>
<p>If you have you one model landmarked by three people, you cannot derive a mean model, because there is no pool of samples, only one. You can assess how different your annotators are doing, and few other things, but  then GPA is probably not the most convenient way of doing this.</p>

---

## Post #7 by @coco (2024-06-23 07:50 UTC)

<aside class="quote no-group" data-username="coco" data-post="5" data-topic="36934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>What I wanted to do: I have fiducials created by three users and I was trying to get the average of these three sets in the same 3D space as the original dataset.</p>
</blockquote>
</aside>
<p>Dear Murat,<br>
again, sorry for not beeing very clear, it’s a new field and new vocabulary for me. Some of your detailed answers are definitely helping. I need to go back to textbooks on GPA…</p>
<p>Allow me to ask a couple more questions re slicer fonctionalities after clarifying what I want to do:</p>
<p>I am investigating several things.<br>
First how my annotators are reproducbibly taking their landmarks on the same sample (to check for obvious errors)<br>
Then, since each annotator did the whole set of samples, how they are reproducibly taking their landmarks on two sets of samples (dataset split by a factor : genotype).  This is to check for overall reproducibility.<br>
Finally, answer if there are morphological differences between the many samples on the basis of the genotype (two genotypes).</p>
<p>I now understand that to evaluate the landmarking quality by the three people per sample, I simply have to do a mean of all coordinates and check standard error or something. I actually did something like this outside of slicer but can it be done directly in slicer since I need it for what is coming below ?</p>
<p>To evaluate genotype effect, I would use the mean landmarks (for all 3 annotator per sample), followed by GPA and procrustes ANOVA. This is where I would have a difficulty because as you explained, I must have both the model and the landmarks. But if I am doing an average per sample and landmarks of the coordinates for the three annotators, I end up with a mean coordinate that is not necessarily on the original model’s surface. So I have to do a projection. The latest is feasible but I have another problem, my model is very complicated because I have 24 segments to start with. I opted for combining as a single model. Some of the segments are fairly small so projection would end up with a markup beeing projected on the wrong surface.</p>
<p>How can I proceed ?</p>

---

## Post #8 by @muratmaga (2024-06-23 15:58 UTC)

<p>For some of these question, you have to consult a text book on statistical design for biological experiments. You can find how it is done in context geometric morphometrics in the textbook by Zelditch et al (Geometric morphometrics for biologists), and also the help pages and vignettes of geomorph R package is very useful.</p>
<p>The statistical model then would evaluate whether the inter-observer variability is exceeding inter-subject variability (which is of course a problem). For that you need replicates by each landmarker. That why it get a bit tedious. Keep the model simple, and it would be something like:</p>
<p>ID + Rater:Replicate, in which<br>
ID: is the name of your subject<br>
Rater: if the name of your people doing the landmarking<br>
Replicate: however many replicates of the landmarking done by raters (minimum two of course).</p>
<p>If the Rater:Replicate term is statistically significant, then it means your raters have are doing things a bit differently, and you have to decide what to do with that.</p>
<p>The reason it get tedious, if you have three specimens (ID=3), three raters, and minimum of two replicates, you have to do 3x3x2 landmark sets, and people usually do this like a dozen samples.</p>
<p>Also, because this is based on GPA aligned coordinates, it uses the procrustes distance (total amount of error) in the model. Hence, you cannot tell whether it is the 2-3 landmarks causing a problem; simply whether the raters are doing the same or not.</p>
<p>That’s why I personally preferred to look at this without the GPA framework. For any specimen, I can calculate a mean landmark set based on all observations, then evaluate how different each person was on a landmark basis. I simply use basic algebra to do this.</p>
<p>You cannot do any of this in GPA in SlicerMorph. We do not have support for statistical models. The factor/covariate framework is there to only change plot colors. As is, GPA module in SlicerMorph is mostly for visualizing the outcomes of landmarking and making sure that there are no digitization or data errors. We leave the statistical inference side to the user, most of whom use R. In future we do plan to have an integration with R, particularly geomorph to do exactly this type of analysis but that’s about a year out.</p>

---
