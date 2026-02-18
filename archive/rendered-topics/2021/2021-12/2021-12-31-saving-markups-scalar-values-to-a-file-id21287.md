# Saving Markups Scalar values to a file

**Topic ID**: 21287
**Date**: 2021-12-31
**URL**: https://discourse.slicer.org/t/saving-markups-scalar-values-to-a-file/21287

---

## Post #1 by @Shambhavi_Malik (2021-12-31 06:58 UTC)

<p>I am using the Markups and VMTK module for blood vessel centerline extraction. In the markups module, is there a method to save the blood vessel radius at each node to a file such as JSON or fcsv? In the scalars section, by selecting the radius, I get a color gradient in the 3D view so can I save the node-specific values to a file?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b43ee1172ed822ea857950a65cdeaa622d2394b.png" data-download-href="/uploads/short-url/m9xxVkXbH3l5DZ7693QPOTtVT9p.png?dl=1" title="Screenshot (52)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b43ee1172ed822ea857950a65cdeaa622d2394b_2_690x388.png" alt="Screenshot (52)" data-base62-sha1="m9xxVkXbH3l5DZ7693QPOTtVT9p" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b43ee1172ed822ea857950a65cdeaa622d2394b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b43ee1172ed822ea857950a65cdeaa622d2394b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b43ee1172ed822ea857950a65cdeaa622d2394b_2_1380x776.png 2x" data-dominant-color="BEBFD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (52)</span><span class="informations">1920×1080 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Upon saving the centerline fcsv file the Control Points table values are saved. So is there a way to incorporate the radius at each node also in this file?</p>

---

## Post #2 by @chir.set (2021-12-31 16:45 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="1" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>is there a way to incorporate the radius at each node also in this file?</p>
</blockquote>
</aside>
<p>You can get the diameter at each curve/model point with ‘Cross-section analysis’ module. It allows to show a table widget where you can select and copy data of your interest. Please note that each line corresponds to data measured at each curve/model point, not at curve control points.</p>
<p>If you really need these in the markups storage file, you would need to write some Python code for this specific task. I don’t think it would be wise to expect the markups module to do that, markups being context and purpose agnostic.</p>

---

## Post #3 by @Shambhavi_Malik (2021-12-31 16:48 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a>  Ok, thanks a lot I’ll try this out. Also, I have noticed that while saving a centerline curve as JSON, the radius values in the file do not accommodate for point resampling. For example, if a curve had 50 points initially and I resample to 20, the generated JSON file still shows the data for the original 50 points in regards to the radius. I don’t know if it’s some mistake that I’m making. I’m not able to figure this out.</p>

---

## Post #4 by @chir.set (2021-12-31 17:05 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="3" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>the radius values in the file</p>
</blockquote>
</aside>
<p>Ha, this discussion shows me that the radius at each control point is already saved in the JSON file, so you don’t have any problem with your initial question :</p>
<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="1" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>So is there a way to incorporate the radius at each node also in this file?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="3" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>the generated JSON file still shows the data for the original 50 points in regards to the radius</p>
</blockquote>
</aside>
<p>I cannot confirm that. I just tried resampling a centerline curve from 22 to 15, 20, 5 control points and saved it each time. The JSON file remains coherent each time regarding the radius. Try with latest nightly build.</p>

---

## Post #5 by @Shambhavi_Malik (2021-12-31 17:13 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> ok I’ll try in that version. From where can I download it? On the website I only see stable and preview releases.</p>

---

## Post #6 by @chir.set (2021-12-31 17:17 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="5" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>preview releases.</p>
</blockquote>
</aside>
<p>It’s labelled ‘Preview’ indeed, dinos called it ‘Nightly’ long ago, sorry for the confusion.</p>

---

## Post #7 by @Shambhavi_Malik (2022-01-01 06:50 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> thanks a lot! It works now. I was initially using the 4.11.20210226 version and facing problems. The latest preview release works just fine.</p>

---

## Post #8 by @Shambhavi_Malik (2022-01-02 08:06 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a> while downsampling works just fine, upon upsampling I lose all the radius data. By upsampling from 20 to 25 control points if I save the JSON file, no radius values are given. Also upon running Cross-Sectional Analysis on the upsampled 25 points, only the point coordinates are displayed. The MIS diameter field remains blank.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d37becedb1c272b5bce07544e62972aa773fe41b.png" data-download-href="/uploads/short-url/uaSfPRFFFCw65pg22t1V0WCkwaL.png?dl=1" title="Screenshot (53)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d37becedb1c272b5bce07544e62972aa773fe41b_2_379x500.png" alt="Screenshot (53)" data-base62-sha1="uaSfPRFFFCw65pg22t1V0WCkwaL" width="379" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d37becedb1c272b5bce07544e62972aa773fe41b_2_379x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d37becedb1c272b5bce07544e62972aa773fe41b_2_568x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d37becedb1c272b5bce07544e62972aa773fe41b_2_758x1000.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (53)</span><span class="informations">758×1000 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any way to solve this?<br>
I have tried Cross-Sectional Analysis on downsampled points and it works just fine. I’m using the latest preview version.</p>
<p>Also when I close 3D slicer I get such errors.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f4f8a0b28847cf5f88c4ca354e7d5ab02a5df5c.png" alt="Screenshot (54)" data-base62-sha1="924uxMkh4GOLaYSzNR2zwtLOisc" width="518" height="382"></p>

---

## Post #9 by @chir.set (2022-01-02 10:32 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="8" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>while downsampling works just fine, upon upsampling I lose all the radius data. By upsampling from 20 to 25 control points if I save the JSON file, no radius values are given. Also upon running Cross-Sectional Analysis on the upsampled 25 points, only the point coordinates are displayed.</p>
</blockquote>
</aside>
<p>I’m afraid I have not observed this. I just tried resampling a 63 control points markups curve to 100, after re-applying in ‘Cross-section analysis’, all metrics are rightly displayed. Using 4.13.0-2021-12-31 r30519 / 5ea103f.</p>
<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="8" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>Also when I close 3D slicer I get such errors.</p>
</blockquote>
</aside>
<p>This probably has other sources.</p>

---

## Post #10 by @Shambhavi_Malik (2022-01-03 07:41 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> if possible could you upload screenshots of the process, maybe I’m going wrong somewhere.</p>

---

## Post #11 by @chir.set (2022-01-03 16:07 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="10" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>if possible could you upload screenshots of the process, maybe I’m going wrong somewhere.</p>
</blockquote>
</aside>
<p>It would be wiser for you to send a link to a video of what you’re doing. A larger audience may study your workflow and advise.</p>

---

## Post #12 by @Shambhavi_Malik (2022-01-04 07:34 UTC)

<p>Yes sure here is the workflow.<br>
<a href="https://drive.google.com/file/d/1eZ-Cya0U5n1CujF7r7ZJpz1m4phuUWsp/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1eZ-Cya0U5n1CujF7r7ZJpz1m4phuUWsp/view?usp=sharing</a></p>

---

## Post #13 by @Shambhavi_Malik (2022-01-05 08:01 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> could you please take a look at the workflow and let me know where I’m going wrong.</p>

---

## Post #14 by @chir.set (2022-01-05 11:14 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="13" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>could you please take a look at the workflow and let me know where I’m going wrong.</p>
</blockquote>
</aside>
<ol>
<li>
<p>I didn’t find anything wrong in the workflow itself. Repeating the same steps, I could not confirm your findings with an input model surface. The MIS diameter is always reported when the input curve is over sampled, or down sampled.</p>
</li>
<li>
<p>But I did found another problem. The module’s logic assumes that the input surface is always a segmentation node, while you are using an input model surface. This is a separate problem, I’ll fix it ASAP.</p>
</li>
</ol>

---

## Post #15 by @Shambhavi_Malik (2022-01-05 12:36 UTC)

<p>Ok, thanks for letting me know <a class="mention" href="/u/chir.set">@chir.set</a>. Is there any work around this issue that I’m facing?</p>

---

## Post #16 by @Shambhavi_Malik (2022-01-05 16:07 UTC)

<p>Also, I have noticed that the centerline curves with sharp nodes such as those in Centerline Curve (1) have this issue of not generating radius upon upsampling.<br>
I don’t know how but the Centerline Curve (0) has curved changes at nodes and this one works fine upon upsampling as you had mentioned. So is there a method to convert the sharp nodes of Centerline Curve (1) to be the same as those of Centerline Curve (0)? I don’t see any differences in their properties.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d66166291b19b895ec0682551677a3d2132c1d6.png" data-download-href="/uploads/short-url/dkf7OFX5LcaJmovranGihqn5R78.png?dl=1" title="Screenshot (55)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d66166291b19b895ec0682551677a3d2132c1d6_2_639x500.png" alt="Screenshot (55)" data-base62-sha1="dkf7OFX5LcaJmovranGihqn5R78" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d66166291b19b895ec0682551677a3d2132c1d6_2_639x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d66166291b19b895ec0682551677a3d2132c1d6_2_958x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d66166291b19b895ec0682551677a3d2132c1d6.png 2x" data-dominant-color="989BD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (55)</span><span class="informations">1004×785 48.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @chir.set (2022-01-05 16:42 UTC)

<aside class="quote no-group" data-username="Shambhavi_Malik" data-post="15" data-topic="21287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shambhavi_malik/48/12961_2.png" class="avatar"> Shambhavi_Malik:</div>
<blockquote>
<p>Is there any work around this issue that I’m facing?</p>
</blockquote>
</aside>
<p>Not to my knowledge unfortunately.</p>

---

## Post #18 by @lassoan (2022-01-05 21:16 UTC)

<p>If you can upload an example file where scalar (static control point measurement) interpolation does not work as expected then I can have a look.</p>

---

## Post #19 by @Shambhavi_Malik (2022-01-13 06:15 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>. Apologies for the delayed response. The problem does not occur when I separately load a centerline curve file. Upon loading the files separately, each centerline curve has non-static control points. But if I perform Centerline Extraction and then immediately try to modify the control points, I face this issue. Only the 0th centerline curve is non-static and works as it is supposed to. The rest are composed of static control points and show problems. Then when I save these files and load them again, they all are non-static and work fine.</p>

---
