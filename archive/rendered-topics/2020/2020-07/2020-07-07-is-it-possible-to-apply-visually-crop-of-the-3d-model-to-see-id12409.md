# Is it possible to apply visually crop of the 3D model to see it's internal surface?

**Topic ID**: 12409
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/is-it-possible-to-apply-visually-crop-of-the-3d-model-to-see-its-internal-surface/12409

---

## Post #1 by @jarrik (2020-07-07 02:16 UTC)

<p>Operating system: win10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-07-07 02:20 UTC)

<p>This simplest to crop a model is to go to Models module, select your model, open “Clipping planes” section, and check “Clip selected model” and slice viewer planes that you want to clip with.</p>
<p>In recent Slicer Preview Releases, you can use Dynamic modeler module to clip models by one ore more markups planes and/or curves drawn on the surface:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>


---

## Post #3 by @jarrik (2020-07-07 03:15 UTC)

<p>One more question. How to add my model into Models module correctly? I download .mrml file into Slicer, but i couldn’t modify it in Models module.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/423bf078ef344ea645922b9ee5d2285a2de36fd3.jpeg" data-download-href="/uploads/short-url/9rVVOxYQjYC8V3LGdCv7nHSKt2j.jpeg?dl=1" title="slicer1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/423bf078ef344ea645922b9ee5d2285a2de36fd3_2_690x341.jpeg" alt="slicer1" data-base62-sha1="9rVVOxYQjYC8V3LGdCv7nHSKt2j" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/423bf078ef344ea645922b9ee5d2285a2de36fd3_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/423bf078ef344ea645922b9ee5d2285a2de36fd3_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/423bf078ef344ea645922b9ee5d2285a2de36fd3_2_1380x682.jpeg 2x" data-dominant-color="B1B3D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1</span><span class="informations">1775×879 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @jarrik (2020-07-07 03:24 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello everyone.<br>
My question is: I need to crop visyally already rendered 3D model to see it’s internal configuration.<br>
I tryed to use ROI mode of the Volume rendering module, but<br>
unsuccessfully.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a9f3bc6c68fac57d59a64cf8d145d815675ee00.jpeg" data-download-href="/uploads/short-url/1vXVIpCyU6wIP2SfMp8vMITWh8I.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a9f3bc6c68fac57d59a64cf8d145d815675ee00_2_690x341.jpeg" alt="slicer" data-base62-sha1="1vXVIpCyU6wIP2SfMp8vMITWh8I" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a9f3bc6c68fac57d59a64cf8d145d815675ee00_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a9f3bc6c68fac57d59a64cf8d145d815675ee00_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a9f3bc6c68fac57d59a64cf8d145d815675ee00_2_1380x682.jpeg 2x" data-dominant-color="B2B5D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1693×837 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> Maby I doing something wrong?</p>

---

## Post #5 by @lassoan (2020-07-07 03:30 UTC)

<aside class="quote no-group" data-username="jarrik" data-post="4" data-topic="12409">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f17d59/48.png" class="avatar"> jarrik:</div>
<blockquote>
<p>My question is: I need to crop visyally already rendered 3D model to see it’s internal configuration.<br>
I tryed to use ROI mode of the Volume rendering module, but<br>
unsuccessfully.</p>
</blockquote>
</aside>
<p>Volume rendering is for volume nodes, not for model nodes. See above how models can be clipped.</p>
<aside class="quote no-group" data-username="jarrik" data-post="3" data-topic="12409">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f17d59/48.png" class="avatar"> jarrik:</div>
<blockquote>
<p>One more question. How to add my model into Models module correctly? I download .mrml file into Slicer, but i couldn’t modify it in Models module.</p>
</blockquote>
</aside>
<p>What would you like to modify?</p>
<ul>
<li>Display settings? =&gt; you can use Models module</li>
<li>Position, orientation, scale? =&gt; you can apply a transform</li>
<li>Smooth, decimate, … =&gt; you can use Surface toolbox module</li>
<li>Change shape, cut, paint, etc. =&gt; you can convert to Segmentation node and edit using Segment Editor module</li>
</ul>

---

## Post #6 by @jarrik (2020-07-07 04:30 UTC)

<p>I want to cut 3D model  by “Clipping planes” section of the Models module. After loading the .mrml file into Slicer, I can change different parameters in the Model module window, but I couldn’t see the results in 3D model screen. Maybe there are some niceties in visualization, ore I made some mistake in loading data?<br>
What part of the Models module window are responsible for selecting of the 3D model, and what I should see there normal?<br>
As you can see, “information” window in my case stay inactive.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57b53c231bd79a7f2a5abb1aea7ba4894fc45e0a.jpeg" data-download-href="/uploads/short-url/cvTPHDWaFKB42GFyxGElEQIYBPY.jpeg?dl=1" title="slicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57b53c231bd79a7f2a5abb1aea7ba4894fc45e0a_2_690x325.jpeg" alt="slicer2" data-base62-sha1="cvTPHDWaFKB42GFyxGElEQIYBPY" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57b53c231bd79a7f2a5abb1aea7ba4894fc45e0a_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57b53c231bd79a7f2a5abb1aea7ba4894fc45e0a_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57b53c231bd79a7f2a5abb1aea7ba4894fc45e0a_2_1380x650.jpeg 2x" data-dominant-color="AAACD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2</span><span class="informations">1806×853 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Initially, there was no DICOM data, but only .nrrd stack of. jpg images, later processed in Segment Editor module, and saved in .mrml format.</p>

---

## Post #7 by @lassoan (2020-07-07 05:12 UTC)

<p>The scene seems to be invalid or incompatible with the Slicer version you are trying to use. We try to preserve backward compatibility with scenes created by previous major version of Slicer, but not with older scenes; and it is always possible that some minor incompatibilities remain.</p>
<p>Could you try loading this scene with the latest Slicer Preview Release?</p>
<p>Which Slicer version was used to created this scene?</p>
<p>How many models does it contain?  If you only have a few models then it may be simpler to just drag-and-drop the model files instead of trying to load a very old scene.</p>

---

## Post #8 by @jarrik (2020-07-08 07:14 UTC)

<p>To create this scene I used Slicer 4.10.2<br>
I tryed to load latest Slicer Preview Release - with the same result:<br>
I couldn’t cut 3D model not in Models module, nor in Dynamic modeler.<br>
Maybe the problem is in the 3D model itself? In my case it contains several materials, craeted in Segment Editor module. Than 3D scene was saved as .mrml file without merging of the components.<br>
Is there necessary to merge components of the 3D scene in order to Modules mentioned above work right?<br>
If that so, I would like to know the way.</p>

---

## Post #9 by @lassoan (2020-07-08 13:02 UTC)

<aside class="quote no-group" data-username="jarrik" data-post="8" data-topic="12409">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f17d59/48.png" class="avatar"> jarrik:</div>
<blockquote>
<p>I couldn’t cut 3D model not in Models module, nor in Dynamic modeler.</p>
</blockquote>
</aside>
<p>Don’t forget to hide or delete the segmentation node after you exported to model. Otherwise the segmentation will occlude the cut model.</p>

---

## Post #10 by @jarrik (2020-07-13 02:05 UTC)

<p>Excuse me, but I have no experience in using any Modules of 3D slicer besides Segment Editor.<br>
In this case what exactly should I do to export/save  my data and hide/ delete segmentation node in the same time? Anyway I want to segment colors of the 3D model be saved.<br>
Initially there was .nrrd stack of .jpg images, later processed in Segment Editor module and saved in .mrml format without additional modifications.<br>
My final goal is: make different crossections of the 3D model to see it’s internal structure  with Models module, or Dynamic modeler.</p>

---
