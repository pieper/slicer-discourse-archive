---
topic_id: 11248
title: "Fill Or Extract Cavities In Segmentations Using The New Wrap"
date: 2020-04-22
url: https://discourse.slicer.org/t/11248
---

# Fill or extract cavities in segmentations using the new "Wrap Solidify" effect

**Topic ID**: 11248
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248

---

## Post #1 by @lassoan (2020-04-22 11:28 UTC)

<p>Making a segment that has fractured, discontinuous boundary and holes inside to be a simple solid object is a quite common task for segmentation. For example it is needed for creating simple solid bone models from CT images, extracting skin surface, segment thin surfaces, such as orbital bone wall, measuring brain volume, or volumes of various cavities.</p>
<p>Slicer now has a tool for all this: “Wrap Solidify” Segment Editor effect, provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a> and contributed by Sebastien Andress (Ludwig-Maximilians-University of Munich).</p>
<p>The tool can extract outer surface, largest cavity, or a custom region and has option to prevent leaking through small holes. The solidified segment can be also hollowed (converted to shell) out for faster 3D printing. Optionally, surface fractures can be preserved in created shells, which is useful for reproducing thin fractures in the created segmentation.</p>
<p>A short demonstration of cavity extraction feature:</p>
<div class="lazyYT" data-youtube-id="IWo-QlU4J_c" data-youtube-title="Automatic cavity segmentation tool in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Segmentation recipes are updated to use this tool:</p>
<ul>
<li><a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">Skin surface extraction</a></li>
<li><a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">Skull stripping from CT images</a></li>
</ul>

---

## Post #2 by @cpinter (2020-04-22 10:25 UTC)

<p>I just saw the <a href="https://www.youtube.com/watch?v=IWo-QlU4J_c">youtube video about the Wrap Solidify effect</a>, very nice work!</p>
<p>I’d like to ask about its potential usage to fill smaller holes. Looking at this <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/master/Resources/Screenshots/screenshot4.png">screenshot</a>, I can see that there is a Custom region mode, which allows selecting one of the segments. Could this be used to segment smaller cavities such as the soft bone area in the mandible, like in this screenshot below?<br>
Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2446bf5781ad82c09a3627abda2e172309fd851.jpeg" data-download-href="/uploads/short-url/whEv4uruYuumP4lWitjOzPZPFtf.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2446bf5781ad82c09a3627abda2e172309fd851_2_534x500.jpeg" alt="image" data-base62-sha1="whEv4uruYuumP4lWitjOzPZPFtf" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2446bf5781ad82c09a3627abda2e172309fd851_2_534x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2446bf5781ad82c09a3627abda2e172309fd851.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2446bf5781ad82c09a3627abda2e172309fd851.jpeg 2x" data-dominant-color="586059"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">686×642 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-04-22 12:02 UTC)

<p>Yes, this can be very useful for dental applications for bone or teeth segmentation. For example, the result with outer surface extraction with minimum 10mm hole size:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3eb73b5cf8e62a1019cc5239e5ec938bafacafb.jpeg" data-download-href="/uploads/short-url/wwgQ2v4qHWD6TcnXwH4OMbCoTfZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3eb73b5cf8e62a1019cc5239e5ec938bafacafb_2_690x379.jpeg" alt="image" data-base62-sha1="wwgQ2v4qHWD6TcnXwH4OMbCoTfZ" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3eb73b5cf8e62a1019cc5239e5ec938bafacafb_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3eb73b5cf8e62a1019cc5239e5ec938bafacafb_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3eb73b5cf8e62a1019cc5239e5ec938bafacafb_2_1380x758.jpeg 2x" data-dominant-color="636160"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1239 551 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-04-22 13:09 UTC)

<p>Solidify effect can be used for automatic removal of table from CT images, too. See <a href="https://discourse.itk.org/t/how-segment-the-board-in-the-red-line-of-the-picture/2973/8?u=lassoan">this post</a> for details.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38116f8779fde38e74b41a83a1831f71fc6f7a24.jpeg" data-download-href="/uploads/short-url/8005PD3tssqUOeCn7UUhvmBg5jC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38116f8779fde38e74b41a83a1831f71fc6f7a24_2_690x306.jpeg" alt="image" data-base62-sha1="8005PD3tssqUOeCn7UUhvmBg5jC" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38116f8779fde38e74b41a83a1831f71fc6f7a24_2_690x306.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38116f8779fde38e74b41a83a1831f71fc6f7a24_2_1035x459.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38116f8779fde38e74b41a83a1831f71fc6f7a24_2_1380x612.jpeg 2x" data-dominant-color="5C5B5E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2778×1235 717 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If there is interest, we can create a dedicated module for this.</p>

---

## Post #5 by @cpinter (2020-04-22 13:25 UTC)

<p>Thanks! What settings should be used so that the mandible is filled like this?</p>

---

## Post #6 by @lassoan (2020-04-22 13:33 UTC)

<p>Region: “outer surface”, carve holes: enabled, minimum hole size: 10mm. Hole carving is enabled so that concave are segmented accurately. Minimum hole size of 10mm ensures that you don’t carve into the bone through holes smaller than 10mm.</p>

---

## Post #7 by @avarghes24 (2022-10-13 16:33 UTC)

<p>Hi!</p>
<p>I am trying to use the SurfaceWrapSolidify extension in Slicer 5.0.3 however, when I search for it using the “Find module” tool, I am unable to find it. I installed the extension conventionally using the Install Slicer Extensions module, searched for the extension, installed it, and then restarted Slicer. To confirm the extension was installed properly I went to Applications &gt;&gt; Slicer &gt;&gt; Show Package Contents &gt;&gt; Contents &gt;&gt; Extensions-30893 and I see SurfaceWrapSolidify as one of the folders. Please let me know what I can do to launch this extension.</p>
<p>For reference: Slicer 5.0.3 running on MacOS Monterey 12.4</p>
<p>Thanks in advance!</p>
<p>Anish</p>

---

## Post #8 by @lassoan (2022-10-13 16:41 UTC)

<aside class="quote no-group" data-username="avarghes24" data-post="7" data-topic="11248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/90db22/48.png" class="avatar"> avarghes24:</div>
<blockquote>
<p>when I search for it using the “Find module” tool, I am unable to find it.</p>
</blockquote>
</aside>
<p>SurfaceWrapSolidify extension does not add any module that would show up in the module finder, but instead it adds the “Wrap solidify” effect to the Segment Editor module.</p>

---

## Post #9 by @avarghes24 (2022-10-13 16:42 UTC)

<p>Ah, i understand. My mistake. Thank you sir</p>

---

## Post #10 by @avarghes24 (2022-10-13 17:54 UTC)

<p>This extension is absolutely amazing and saved hours of painting and erasing with a threshold or messing around with level tracing for me! Thank you so much to everyone that developed this</p>

---

## Post #11 by @lassoan (2022-10-13 17:58 UTC)

<p>Awesome, thanks for the feedback! It would be great if you could share some of the images of what you achieved with the tool (I’m just curious).</p>

---

## Post #12 by @mangotee (2022-10-25 14:28 UTC)

<p><a class="mention" href="/u/sandress">@sandress</a> - you should see this <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @sandress (2022-10-25 14:35 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> thangs Ahmad <a class="mention" href="/u/mangotee">@mangotee</a><br>
Also <a class="mention" href="/u/lassoan">@lassoan</a> for the many contributions!</p>

---

## Post #14 by @lassoan (2022-10-29 05:57 UTC)

<p>A post was split to a new topic: <a href="/t/wrapsolidify-is-amazing-for-preprocessing-before-volumetric-mesh-generation/25961">WrapSolidify is amazing for preprocessing before volumetric mesh generation</a></p>

---
