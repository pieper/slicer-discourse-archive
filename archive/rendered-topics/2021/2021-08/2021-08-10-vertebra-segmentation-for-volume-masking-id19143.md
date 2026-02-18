# Vertebra segmentation for volume masking

**Topic ID**: 19143
**Date**: 2021-08-10
**URL**: https://discourse.slicer.org/t/vertebra-segmentation-for-volume-masking/19143

---

## Post #1 by @ni5h (2021-08-10 14:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Operating system: windows<br>
Slicer version: 4.11.2021<br>
Expected behavior: i need to annotate off one level only (L1). I cannot crop this because this is not we require for analysis (we need all of the anatomy to landmark the point of our annotation). I have tried to mask this, I have watched the perklab research youtube video ‘mask volume for tools’ for support but I am unsure when I complete the annotation the whole annotation is saved in nrrd.<br>
Actual behavior: when I mask the l1 level it fills inside and the tool works approriately but i cannot annotate further on the masked level (in 3d it is an expected block). when i use the scissors to mask everything but L1 level the mask volume tool does not work and blanks out the level I need.</p>
<p>I just need to mask everything but the l1 level and complete the annotations of all the areas i require (fat and muscle) and when I save in nrrd it should save the whole raw data giving a landmark of the level annotated for analysis?</p>

---

## Post #2 by @lassoan (2021-08-10 16:11 UTC)

<aside class="quote no-group" data-username="ni5h" data-post="1" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>I have tried to mask this, I have watched the perklab research youtube video ‘mask volume for tools’ for support but I am unsure when I complete the annotation the whole annotation is saved in nrrd.</p>
</blockquote>
</aside>
<p>It is a separate volume. It does not change the original volume. You can save it as a separate nrrd.</p>
<aside class="quote no-group" data-username="ni5h" data-post="1" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>when I mask the l1 level it fills inside and the tool works approriately but i cannot annotate further on the masked level</p>
</blockquote>
</aside>
<p>You can switch the master volume to choose either the original volume or the blanked out volume.</p>
<aside class="quote no-group" data-username="ni5h" data-post="1" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>when i use the scissors to mask everything but L1 level the mask volume tool does not work and blanks out the level I need</p>
</blockquote>
</aside>
<p>What do you mean by “does not work”? What do you do exactly, what do you expect to happen, and what happens instead?</p>
<aside class="quote no-group" data-username="ni5h" data-post="1" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>when I save in nrrd it should save the whole raw data giving a landmark of the level annotated for analysis?</p>
</blockquote>
</aside>
<p>What would you like to save in the nrrd? The segmentation, the original, volume, or the blanked out volume (containing only L1 vertebra)?</p>
<p>What do you mean by “giving a landmark of the level”? Is landmark a 3D point, a segmentation, …?</p>
<p>What kind of analysis would you like to do? What is the clinical problem that you are trying to solve?</p>

---

## Post #3 by @ni5h (2021-08-10 16:47 UTC)

<p>difficult to explain - i have found a workaround that allow me to segment the desired level that I need;</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What would you like to save in the nrrd? The segmentation, the original, volume, or the blanked out volume (containing only L1 vertebra)?</p>
<p>What do you mean by “giving a landmark of the level”? Is landmark a 3D point, a segmentation, …?</p>
<p>What kind of analysis would you like to do? What is the clinical problem that you are trying to solve?</p>
</blockquote>
</aside>
<p>What I need to annotate is fat, bone and muscle at l1 level - only this level - each level above and below and liver etc is not required.</p>
<p>I have found if I crop the image, annotate what I need and then switch back to the master volume I can see what i have annotated within that level.</p>
<p>the issue I am having is when i come to export - I use mri cron to visualise my annotation - i can only see the area, which I have annotated obviously, but what i need to see when I export is the whole series so that the ‘landmark’  is definitely L1 and the rest of the seires L2/3/4/5 and T10/11/12. Therefore, can I mask the area above and below - would that export? will i need to create another segment calling this oustide_AOI, which will definitely export - but in this case, how can i complete this task quickly, drawing each slice is time consuming and can imapct the rest of the series that I have annotated already.</p>
<p>I hope this makes sense and thanks for your help!</p>

---

## Post #4 by @lassoan (2021-08-10 16:58 UTC)

<aside class="quote no-group" data-username="ni5h" data-post="3" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>I use mri cron to visualise my annotation</p>
</blockquote>
</aside>
<p>What visualization mode is that you could not set up in Slicer?</p>
<aside class="quote no-group" data-username="ni5h" data-post="3" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>i can only see the area, which I have annotated obviously, but what i need to see when I export is the whole series</p>
</blockquote>
</aside>
<p>You can save the whole image as well.</p>
<aside class="quote no-group" data-username="ni5h" data-post="3" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>Therefore, can I mask the area above and below - would that export?</p>
</blockquote>
</aside>
<p>Yes, of course. You can have unlimited number of volumes, segmentations, segments in the scene and you can export all of them to files.</p>
<aside class="quote no-group" data-username="ni5h" data-post="3" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>drawing each slice is time consuming and can imapct the rest of the series that I have annotated already</p>
</blockquote>
</aside>
<p>Slicer has many tools for spine segmentation.</p>
<p>For example, using classic tools, you can quickly segment the entire spinal column (each vertebra in a separate segment) using Grow from seeds effect, and filling internal holes using <a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d">this code snippet</a>.</p>
<p>There are also several fully automatic neural networks for spine segmentation. There is a pre-trained model for entire spine segmentation in <a href="https://github.com/Project-MONAI/MONAILabel#readme">MONAILabel</a>, but you can also train your own network for segmenting a single vertebra.</p>

---

## Post #5 by @ni5h (2021-08-11 14:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, of course. You can have unlimited number of volumes, segmentations, segments in the scene and you can export all of them to files.</p>
</blockquote>
</aside>
<p>can you merge/combine annotations? I wish to threshold muscle, intercostal muscles on that level and with low resolution it is difficult to do, my method atm is to threshold muscle, split them via islands and then remove the areas which are not muscle, can I combine the segments once I have split them?</p>

---

## Post #6 by @lassoan (2021-08-11 16:35 UTC)

<p>Yes, you can merge segments. If you need to merge many segments at once then the most efficient is to take advantage of masking settings. See details in this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/MergeSegments/">segmentation recipe</a>.</p>
<p>As a side note, for discussions in the Slicer forum, use the “segmentation” (for a set of structures) or “segment” (for a single structure) term instead of “annotation” (it refers to measurements in Slicer). See list of terms used in Slicer here in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#glossary">Glossary</a>.</p>

---
