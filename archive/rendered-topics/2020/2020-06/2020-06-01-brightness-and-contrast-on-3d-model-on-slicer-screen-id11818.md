# Brightness and contrast on 3d model on slicer screen

**Topic ID**: 11818
**Date**: 2020-06-01
**URL**: https://discourse.slicer.org/t/brightness-and-contrast-on-3d-model-on-slicer-screen/11818

---

## Post #1 by @lambrosone (2020-06-01 18:12 UTC)

<p>THE 3D MODEL THAT APPEARS WITH VOLUME RENDERING IS VERY DARK AND CONTRASTY, oops,   almost useless. is there a way to juggle those two to make a more useful image?</p>
<p>thank you</p>

---

## Post #2 by @lassoan (2020-06-01 22:21 UTC)

<p>You can adjust brightness/contrast of the image at described here: <a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284" class="inline-onebox">Recent improvements in window/level management</a></p>

---

## Post #3 by @lambrosone (2020-06-01 23:22 UTC)

<p>Thank you for that, however my problem is not the slice views, my problem is that the 3d model in the upper right of my four up screen is too dark. It is just as dark in 4.11 That is what I want to lighten. Also in Slicer 4.11, where is the metadata control? I can’t find one or find metadata. Also now the 3D model is flying off the screen.</p>
<p>Thank you</p>
<p>VL</p>

---

## Post #4 by @lassoan (2020-06-02 00:01 UTC)

<p>I’m not sure what you mean. If you load a model then it is loaded as gray - the same shade in 4.11 as in all earlier Slicer versions.</p>
<p>Can you reproduce the problem with a publicly available data set or upload your data set somewhere and post the link? Can you post a screenshot?</p>

---

## Post #5 by @lambrosone (2020-06-02 04:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffdee9b66adc11c51e09fc7207714722fed6bb1d.jpeg" data-download-href="/uploads/short-url/AvxljjJpn1oQONnQRs15Wh5egWh.jpeg?dl=1" title="screen shot dark 3d model.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffdee9b66adc11c51e09fc7207714722fed6bb1d_2_690x449.jpeg" alt="screen shot dark 3d model.jpg" data-base62-sha1="AvxljjJpn1oQONnQRs15Wh5egWh" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffdee9b66adc11c51e09fc7207714722fed6bb1d_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffdee9b66adc11c51e09fc7207714722fed6bb1d_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffdee9b66adc11c51e09fc7207714722fed6bb1d_2_1380x898.jpeg 2x" data-dominant-color="767978"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen shot dark 3d model.jpg</span><span class="informations">1669×1088 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>thanks for helping. First of all where’s metadata in 4.11?</p>
<p>here’s a screen shot of what I am asking about. The model in the upper right quadrant is very dark with high contrast., I want to be able to see it better. are there no controls for brightness and contrast on the model?</p>
<p>thanks</p>
<p>VL</p>

---

## Post #6 by @lassoan (2020-06-02 05:53 UTC)

<p>I see now: you use volume rendering to visualize the volume. In most cases, you just need to select a CT preset in Display section to display a nice bone or soft-tissue rendering. Some CBCT scanners are not properly calibrated and you need to slightly adjust the “Shift” slider to compensate for inaccurate voxel values. If voxel values are completely different from Hounsfield unit then you can open the “Advanced” section and adjust the transfer functions.</p>

---

## Post #7 by @lambrosone (2020-06-02 06:15 UTC)

<p>Can you tell me where metadata is found in 4.11? .</p>

---

## Post #8 by @lambrosone (2020-06-02 06:25 UTC)

<p>Slicer is very frustrating. I have found no place that tells me how to get to the 3d model except through volume rendering and the presets thru Volume rendering look bizarre. there does not seem to be a slicer book.</p>

---

## Post #9 by @muratmaga (2020-06-02 07:05 UTC)

<p>Learning a new software takes time. Tutorials are usually good places to start. Your terminology is also not correct. Volume Rendering is not a 3D model, it is simply a visualization technique. To obtain 3D model from a CBCT (or any other voxel data), you have to do a segmentation using <code>Segment Editor</code> module, and then export the segmentation as 3D model. You may find some of these useful:</p>
<ul>
<li>segmentation: <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab03_Slicer_3_Segmentation" rel="nofollow noopener">https://github.com/SlicerMorph/W_2020/tree/master/Lab03_Slicer_3_Segmentation</a>
</li>
<li>volume rendering: <a href="https://github.com/SlicerMorph/S_2019/tree/master/Lab04_Slicer_3_Measurements_Visualization#volume-rendering" rel="nofollow noopener">https://github.com/SlicerMorph/S_2019/tree/master/Lab04_Slicer_3_Measurements_Visualization#volume-rendering</a>
</li>
</ul>

---

## Post #10 by @lambrosone (2020-06-02 11:30 UTC)

<p>Thank you. I was just talking about the visualization which appears muddy. Which i was trying to correct.</p>
<p>I export 3d models as stl.</p>
<p>Btw can you tell me where metadata is found in 4.11?</p>

---

## Post #11 by @pieper (2020-06-02 12:40 UTC)

<aside class="quote no-group" data-username="lambrosone" data-post="10" data-topic="11818">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/9d8465/48.png" class="avatar"> lambrosone:</div>
<blockquote>
<p>Btw can you tell me where metadata is found in 4.11?</p>
</blockquote>
</aside>
<p>It seems we’re not understanding what you mean by “metadata” - can you explain?</p>

---

## Post #12 by @lambrosone (2020-06-02 13:13 UTC)

<p>In 4.8 the were two buttons at the bottom of the dicom screen. One said “load” and one said “metadata”. In 4.11 there is a load button but not a metadata button. I cant find the metadata for the selected image</p>

---

## Post #13 by @lassoan (2020-06-02 13:25 UTC)

<p>DICOM metadata display (any several other options) are now available in the DICOM browser on right-click.</p>

---

## Post #14 by @lambrosone (2020-06-02 13:41 UTC)

<p>Thank you. How is a user supposed to know that? Maybe there should be a whats new screen to document recent changes. If there is one , where is it?</p>

---

## Post #15 by @chir.set (2020-06-02 13:58 UTC)

<p>You are expecting too much without paying, and expressing your expectations in an overbearing way.</p>
<p>Sorry all, couldn’t withhold this one.</p>

---

## Post #16 by @lassoan (2020-06-02 14:13 UTC)

<aside class="quote no-group" data-username="lambrosone" data-post="14" data-topic="11818">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/9d8465/48.png" class="avatar"> lambrosone:</div>
<blockquote>
<p>How is a user supposed to know that?</p>
</blockquote>
</aside>
<p>Software nowadays does not come with a manual (unless you need to provide something to meet regulatory requirements), because users don’t have time to read through thousands of pages of documentation. We do what everyone else is doing: make sure that most common questions are answered by simple web search (by finding relevant user manual or forum posts) and answer all remaining questions as they come up.</p>
<p>For example: google search for <code>Slicer DICOM metadata</code>, open the first page that shows up in the search results and search on the page for <code>metadata</code>.</p>

---

## Post #17 by @lambrosone (2020-06-02 14:58 UTC)

<p>Not overbearing at all. I appreciate the help offered. It is highly frustrating to work with as complex a piece of software like slicer that was not designed to be user friendly.</p>
<p>When a new version comes up and nothing was where it was, and the user is not as as proficient in the field as the moderators, you might have a little empathy as to the struggle of trying to figure it out on your own, especially if you are a newbie.<br>
It is not an unreasonable request to put in a whats new text file with new versions.</p>

---

## Post #18 by @muratmaga (2020-06-02 15:06 UTC)

<aside class="quote no-group" data-username="lambrosone" data-post="17" data-topic="11818">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/9d8465/48.png" class="avatar"> lambrosone:</div>
<blockquote>
<p>It is not an unreasonable request to put in a whats new text file with new versions.</p>
</blockquote>
</aside>
<p>A reasonable request, but unfortunately not quite practical due to the way changes are incorporated nightly. There tens of thousands of big and small changes between 4.8 from three years ago and the current preview 5.0 that’s not going to be possible to list.</p>
<p>Most of the SLicer documentation is done on volunteer basis. If you would like to help for the parts that you find frustrating, we can always use more hands…</p>

---

## Post #19 by @lambrosone (2020-06-02 15:25 UTC)

<p>Slicer has enormous value and i applaud the people who develop and maintain it. If i knew enough to contribute i would.</p>

---

## Post #20 by @lassoan (2020-06-02 16:02 UTC)

<p>You are already contributing to Slicer by asking questions, as it lets us know what things are too difficult for users to figure out on their own.</p>
<p>I understand your frustration, as I have the same feeling when using basically any software. For example Google and Skype hides/moves features around all the time, without making any sense to me. I assume that they have a good reason for making the changes, but it is still frustrating. I guess the alternative would be to slow down, not make too many changes, but then users would leave the software because it does not keep up with changes that are happening in the world.</p>

---
