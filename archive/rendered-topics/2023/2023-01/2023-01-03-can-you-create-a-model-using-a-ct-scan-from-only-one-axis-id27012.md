---
topic_id: 27012
title: "Can You Create A Model Using A Ct Scan From Only One Axis"
date: 2023-01-03
url: https://discourse.slicer.org/t/27012
---

# Can you create a model using a CT scan from only one axis?

**Topic ID**: 27012
**Date**: 2023-01-03
**URL**: https://discourse.slicer.org/t/can-you-create-a-model-using-a-ct-scan-from-only-one-axis/27012

---

## Post #1 by @studyskin (2023-01-03 03:01 UTC)

<p>hello, i downloaded a file for a fossa skull from morphosource but the scan is only from one axis and doesnt load up in slicer, is there a way to create a model from a scan like this? it shows as a model in<br>
morphosource’s inbuilt rendering software<br>
heres the files i am trying to use<br>
<a href="https://drive.google.com/drive/folders/1v1U0WpTqCZBoR_Ohvh2Ghy53FU7gKIsT?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1v1U0WpTqCZBoR_Ohvh2Ghy53FU7gKIsT?usp=sharing</a><br>
thank you to anyone who can help! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2023-01-03 04:31 UTC)

<p>This is a huge image (16GB), so you need a strong computer to load it or load at lower resolution. I would recommend to use the <strong>ImageStacks</strong> module of <a href="https://slicermorph.github.io/#two">SlicerMorph extension</a>, which allows loading large image stacks conveniently, optionally at half or quarter resolution and/or cropped to the relevant region of interest.</p>
<p>For example, I was able load and volume render the image without issues at half resolution (2GB):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c70c1d1eb50f9278735b633f3c56326376bd9b57.jpeg" data-download-href="/uploads/short-url/soQY9tSC0CwuvccmMpktW6UZPMj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70c1d1eb50f9278735b633f3c56326376bd9b57_2_690x363.jpeg" alt="image" data-base62-sha1="soQY9tSC0CwuvccmMpktW6UZPMj" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70c1d1eb50f9278735b633f3c56326376bd9b57_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70c1d1eb50f9278735b633f3c56326376bd9b57_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70c1d1eb50f9278735b633f3c56326376bd9b57_2_1380x726.jpeg 2x" data-dominant-color="343234"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1011 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Volume rendering of the full-resolution - 16GB - image failed with my GPU, which has only 12GB RAM.</p>
<p>For volume rendering, enable SlicerMorph customization options in application settings, use the 16-bit preset, and adjust the offset slider.</p>
<hr>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I would recommend to update SlicerMorph extension so that it always registers its extra volume rendering presets (or allow registering of the presets separately from other customization options).</p>
<p>I would also consider adding the 8-bit and 16-bit preset to Slicer core (with names such as “CT bone low-dynamic-range” and “CT bone high-dynamic range”?). <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a> what do you think?</p>

---

## Post #3 by @muratmaga (2023-01-03 05:55 UTC)

<p><a class="mention" href="/u/studyskin">@studyskin</a> you may want to get yourself familiar with SlicerMorph tutorials which covers all steps of importing, visualizing and segmenting microCT data. <a href="https://github.com/SlicerMorph/Tutorials/#readme" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></p>
<p>you want to complete sections on ImageStacks, Volume Rendering and Segmentation.</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> pointed out, this is a quite large dataset. Our rule of thumb in slicer is 6-8 times more memory than the dataset size. So you will need about 128GB of RAM. If you do want to benefit from GPU based rendering, which will be fast, you need a GPU with at least 16GB of RAM. So as advised, please proceed with downsampled datasets…</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> adding the presets to Slicer would be great. Feel free to take it from SlicerMorph and add them. But again, we still need a way of people easily adding their presets to the Slicer, as a feature. Also how would you go about automatically adding volume rendering presets? Simply move them into another resource file that always gets executed?</p>

---

## Post #4 by @pieper (2023-01-03 15:21 UTC)

<p>The functionality already exists to save and load custom volume properties but it’s not well exposed in the UI.  You can save .vp files and reload them, and then pick them using the volume rendering module (inputs section not preset menu, so no icon).</p>
<p>If someone has time, it would be pretty easy to add something that saves the current volume property and a screen capture of the 3D view in a form that could be used as a preset along with an application setting to reload them when the app starts.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#register-custom-volume-rendering-presets" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#register-custom-volume-rendering-presets</a></p>

---

## Post #5 by @studyskin (2023-01-04 20:55 UTC)

<p>thank you so much everyone! i really appreciate it, im just doing this for personal interest so not very familiar with all the terms but i understand it alot better now!</p>

---

## Post #6 by @muratmaga (2023-01-04 21:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="27012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to update SlicerMorph extension so that it always registers its extra volume rendering presets</p>
</blockquote>
</aside>
<p>This is now incorporated to SlicerMorph. Now all three volume rendering presets should be visible to users regardless they choose to enable customizations or not.</p>

---

## Post #7 by @lassoan (2023-01-05 01:04 UTC)

<p>Thank you! I’ve started to clean up and improve the presets. As part of this work, I’ll propose to add these 3 presets to Slicer core and remove some of the less useful ones.</p>

---
