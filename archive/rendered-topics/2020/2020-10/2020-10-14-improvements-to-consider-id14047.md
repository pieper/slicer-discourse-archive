---
topic_id: 14047
title: "Improvements To Consider"
date: 2020-10-14
url: https://discourse.slicer.org/t/14047
---

# Improvements to consider

**Topic ID**: 14047
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/improvements-to-consider/14047

---

## Post #1 by @CaptainR (2020-10-14 22:53 UTC)

<p>Hi, I really enjoyed using slicer, it is trully a great software.</p>
<p>Few improvements that may be considered:</p>
<ul>
<li>in segment editor: default setting for override other segments should be none (otherwise it is the best way to detroy your work).</li>
<li>when you create a new segment or edit one, when only one volume is loaded it would be great that it sets this volume as master volume automatically.</li>
<li>for reformat module: would be nice to have a way change one slice orientation by moving its projection in the 2 other orthogonal views.</li>
<li>I’ve in the forums that it should be present but I have version 4.10.2 and I don’t have the angle measurements tool.</li>
<li>add an option when saving screenshots to choose resolution and dimensions of the image (in order to have high quality images)</li>
<li>customize the background color of the 3D view (only 3 options so far: white, black and light blue).</li>
<li>when importing multiple files it would be nice to have a way to apply an option to all at once, for example when loading volumes and checking lablelmaps.</li>
<li>change and manually set the center of rotation for the transform module (linear transform for example)</li>
<li>I tried QTtesting and macros for repetitive tasks, it is pretty good but doesn’t really deal with batch processing. A way to implement batch processing that would interact with most modules functions would be awesome and time saving.</li>
<li>segment statistics: add geometric center, maximum diameter, slice maximum diameter, slice minimum diameter measurements could be interesting</li>
<li>not paramount but: drawing geometrical shape in segment editor. For example only sphere is possible, but ellipse mostly or square,…</li>
</ul>
<p>Thank you for this excellent software so far.</p>

---

## Post #2 by @lassoan (2020-10-15 02:38 UTC)

<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>in segment editor: default setting for override other segments should be none (otherwise it is the best way to detroy your work).</p>
</blockquote>
</aside>
<p>Most commonly, segmentation is used for partitioning a volume (each voxel is assigned to one structure), which can be achieved by making the segments overwrite each other. Users that prefer allowing overlapping segments can change the default as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_default_segmentation_options">here</a>.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>when you create a new segment or edit one, when only one volume is loaded it would be great that it sets this volume as master volume automatically</p>
</blockquote>
</aside>
<p>It is already implemented like this: load a volume and switch to Segment Editor → a segmentation node is created automatically and the current background volume is chosen as master volume.</p>
<p>If you manually create a new segmentation then the current master volume is not selected by default to make it easier to choose any volume as initial master volume. This initial master volume has a special role: it determines the geometry (origin, spacing, axis directions) of the segmentation’s binary labelmap representation, so users may want to make this decision more carefully.</p>
<p>Since the behavior was designed, we added a button to change geometry of the segmentationafter the initial master volume selection. So, we could reconsider the decision and auto-select current background volume as master volume by default for manually created segmentation nodes, too.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>for reformat module: would be nice to have a way change one slice orientation by moving its projection in the 2 other orthogonal views.</p>
</blockquote>
</aside>
<p>This is already available. You can do that by showing slice intersections and holding down <kbd>Ctrl/Cmd</kbd> + <kbd>Alt</kbd> while click-and-dragging in the view. See list of keyboard/mouse shortcuts for viewers <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html">here</a>.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>I’ve in the forums that it should be present but I have version 4.10.2 and I don’t have the angle measurements tool.</p>
</blockquote>
</aside>
<p>You need to use the latest Slicer Stable Release. If you have any problem with this release then let us know.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>add an option when saving screenshots to choose resolution and dimensions of the image (in order to have high quality images)</p>
</blockquote>
</aside>
<p>It is available in the Screenshot tool in the toolbar. Unfortunately, the feature is currently broken (<a href="https://github.com/Slicer/Slicer/issues/3885" class="inline-onebox">Update qMRMLScreenShotDialog to support high-resolution magnified screenshot · Issue #3885 · Slicer/Slicer · GitHub</a>). We are upgrading VTK to new version, which might fix the issue.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>customize the background color of the 3D view (only 3 options so far: white, black and light blue)</p>
</blockquote>
</aside>
<p>This is not commonly needed, so we will not add GUI for this, but you can set any background color or gradient as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color">here</a>.</p>
<p>In general, you can customize everything by a few lines of Python code, but it would be impossible to expose everything on the GUI or even describe it. We list most commonly needed code snippets in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>. If you cannot find how to change some settings then just let us know.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>when importing multiple files it would be nice to have a way to apply an option to all at once, for example when loading volumes and checking lablelmaps</p>
</blockquote>
</aside>
<p>You can give hint to Slicer to interpret a volume as labelmap or segmentation by default. Use .seg.nrrd file extension to load as segmentation; or <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-image-file-as-labelmap-volume">use -seg or -label filename suffix in the file name</a>.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>change and manually set the center of rotation for the transform module (linear transform for example)</p>
</blockquote>
</aside>
<p>What would you use this for? Achieving alignment in 3D (3 degrees of freedom rotation and 3 degrees of freedom translation) is not practically feasible using manual translation/rotation, therefore more accurate and much easier, non-iterative landmark-based method (you don’t just specify a pivot point but multiple landmark points). Several landmark registration modules are available in Slicer: “Landmark   registration” module is well suited for correcting small misalignments of images; while “Fiducial registration wizard” module (in SlicerIGT extension) is suitable for any kind of data sets an large misalignments.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<ul>
<li>I tried QTtesting and macros for repetitive tasks, it is pretty good but doesn’t really deal with batch processing. A way to implement batch processing that would interact with most modules functions would be awesome and time saving.</li>
</ul>
</blockquote>
</aside>
<p>You can put together automation macros using code snippets from the script repository.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>segment statistics: add geometric center, maximum diameter, slice maximum diameter, slice minimum diameter measurements could be interesting</p>
</blockquote>
</aside>
<p>These (and many more) are all available in Segment statistics module in recent Slicer versions.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="1" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>not paramount but: drawing geometrical shape in segment editor. For example only sphere is possible, but ellipse mostly or square,…</p>
</blockquote>
</aside>
<p>I’m not sure how much a square-shaped brush would improve things.</p>
<p>Instead, you can effectively get custom brush shape (dynamic shape that takes into account the image content) by adjusting “editable intensity range”. You may also use “Local threshold” effect, which allows quick automatic intensity range selection and paint with automatic leak prevention.</p>

---

## Post #3 by @CaptainR (2020-10-15 22:43 UTC)

<p>Mr Lasso, thank you so much for all those answers. This is very helpful.<br>
I started customizing using the links you sent and the script repository. Unfortunately some don’t work when I just copy and paste, so I guess I’ll have to get working in Python coding now.</p>
<p>I am in the Interventional Radiology field and the idea behind the shape and the center of rotation for transforms is that I needed to modelize an ablation zone as an ellipse of 4x3 cm and then move it and oriente it to specific coordinates. I imported an .stl ellipse and then tried to move it around using the transform module, but wasn’t very precise.</p>
<p>Thanks again for your time.</p>

---

## Post #4 by @lassoan (2020-10-15 23:29 UTC)

<aside class="quote no-group" data-username="CaptainR" data-post="3" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>Unfortunately some don’t work when I just copy and paste</p>
</blockquote>
</aside>
<p>All examples should work as is. If you have problems with any of them then let us know.</p>
<aside class="quote no-group" data-username="CaptainR" data-post="3" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>shape and the center of rotation for transforms is that I needed to modelize an ablation zone as an ellipse of 4x3 cm and then move it and oriente it to specific coordinates.</p>
</blockquote>
</aside>
<p>Iterative translation/rotation works well for positioning in 2D, but in 3D but it is just too tedious (you need to move the object and continuously evaluate in multiple views if its position is optimal).</p>
<p>Instead, it is recommended to mark your targets (and optionally, regions to avoid) with markups points/lines/planes and/or segmentation. From these inputs, optimal treatment plan (such as ablation zone shape and size) can be computed automatically using a simple logic. You may then review the plan and make small adjustments.</p>
<p>There have been a number of thermal/laser/radio ablation planning systems built on Slicer for spine, liver, prostate, etc. so if you have specific questions about how to implement anything then we may be able to help. For example, using SlicerRT extension, you can visualize not just a sphere but thermal dose in 2D and 3D as isodose lines/surfaces, compute dose volume histograms for target organs and organs at risk, etc. Using SlicerIGT extension, you can implement real-time navigation of the ablator, optionally using image guidance (CT, MRI, live ultrasound, etc.) and do all the necessary patient registrations and tool calibrations.</p>

---

## Post #5 by @muratmaga (2020-10-16 01:17 UTC)

<aside class="quote no-group" data-username="CaptainR" data-post="3" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/da6949/48.png" class="avatar"> CaptainR:</div>
<blockquote>
<p>Unfortunately some don’t work when I just copy and paste, so I guess I’ll have to get working in Python coding now.</p>
</blockquote>
</aside>
<p>İf there are any, make sure indentation are preserved correctly when you are pasting the code as those matter in python.</p>

---

## Post #6 by @Rodrigo_Visconti (2020-10-17 22:21 UTC)

<p>I would suggest another one. Some sort of partial smooth. Smoothing occasionally reduces significant details from the segmentation.</p>

---

## Post #7 by @lassoan (2020-10-18 15:04 UTC)

<aside class="quote no-group" data-username="Rodrigo_Visconti" data-post="6" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rodrigo_visconti/48/3436_2.png" class="avatar"> Rodrigo_Visconti:</div>
<blockquote>
<p>Some sort of partial smooth. Smoothing occasionally reduces significant details from the segmentation.</p>
</blockquote>
</aside>
<p>I’ve gave this a try yesterday and managed to implement it (it works like sphere paint but instead of adding to the segment, it smoothes the painted region). It works really well! I’ll test and tune it some more and make it available in a few days.</p>

---

## Post #8 by @Rodrigo_Visconti (2020-10-18 17:48 UTC)

<p>Great! This tool will help us to save a lot of time. Thanks again</p>

---

## Post #9 by @lassoan (2020-10-20 04:05 UTC)

<p>Smoothing brush (you can left-click and drag in slice or 3D views when Smoothing effect is active to locally smooth the segment) will be available in tomorrow’s Slicer Preview Release. Unfortunately, slice views don’t work in the preview release (and there are some other issues - see <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+label%3Adomain%3Avtk9">list</a>), but you can still try this smoothing tool.</p>

---

## Post #10 by @Rodrigo_Visconti (2020-10-20 19:19 UTC)

<p>Thanks. I’ve managed to download it but some extensions still unavailable and 3D view doesn’t work as well</p>

---

## Post #11 by @Rodrigo_Visconti (2020-10-20 19:42 UTC)

<p>The 3D view worked turning smooth factor off</p>

---

## Post #12 by @lassoan (2020-10-20 19:51 UTC)

<p>A post was split to a new topic: <a href="/t/manual-registration-and-warping-of-volume/14169">Manual registration and warping of volume</a></p>

---

## Post #13 by @Rodrigo_Visconti (2020-10-21 04:42 UTC)

<p>It worked shutting smooth factor down but if I try to make a joint smooth the 3D image disappear</p>

---

## Post #14 by @lassoan (2020-10-21 04:50 UTC)

<p>Joint smoothing is probably broken in latest preview release (it uses model smoothing, which <a href="https://github.com/Slicer/Slicer/issues/5223">does not work yet in latest preview</a> - it will take a few more days to get the VTK9 issues fixed).</p>

---

## Post #15 by @Rodrigo_Visconti (2020-10-21 04:53 UTC)

<p>Great. It’s good news the possibility of having both working together. Some extensions are unavailable too like slicer heart</p>

---

## Post #16 by @lassoan (2020-10-21 04:57 UTC)

<p>Yes, we know about the extension errors. Once we fix basic errors (slice view, model smoothing, …) then we’ll get to the extensions, too.</p>

---

## Post #17 by @lassoan (2020-10-23 00:13 UTC)

<p>A post was split to a new topic: <a href="/t/configure-segmentation-defaults/14207">Configure segmentation defaults</a></p>

---

## Post #18 by @lassoan (2020-11-13 00:56 UTC)

<p>For reference - Slicer Preview Releases are working now and so the new Smoothing brush is available for testing. See more information and demo video here: <a href="https://discourse.slicer.org/t/new-segment-editing-feature-smoothing-brush/14577" class="inline-onebox">New segment editing feature: Smoothing brush</a></p>

---

## Post #19 by @Rodrigo_Visconti (2020-11-24 11:47 UTC)

<p>Hi Andras I’m really enjoying the brush smoothing. Very helpful. I’m thinking of other improvements and thought of a way to tilt one plane without affecting others during segmentation. Is it possible?</p>

---

## Post #20 by @manjula (2020-11-24 14:07 UTC)

<p>You can rotate of the slice views independently using reformat module</p>

---

## Post #21 by @lassoan (2020-11-24 18:06 UTC)

<aside class="quote no-group" data-username="Rodrigo_Visconti" data-post="19" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rodrigo_visconti/48/3436_2.png" class="avatar"> Rodrigo_Visconti:</div>
<blockquote>
<p>a way to tilt one plane without affecting others during segmentation. Is it possible?</p>
</blockquote>
</aside>
<p>Do you know that you can rotate views by Ctrl + Alt + Left-click-and-drag in a slice view (while slice intersections are displayed)? This rotates all the other views so that their relative angles are preserved, which is useful because otherwise your views can easily end up having similar orientation, showing almost the same thing.</p>
<p>You can also reslice a volume along an arbitrary curve using “Cross-section analysis” module in SlicerVMTK extension.</p>
<p>What is your use case? What would you like to visualize?</p>

---

## Post #22 by @chir.set (2020-11-25 08:06 UTC)

<aside class="quote no-group" data-username="Rodrigo_Visconti" data-post="19" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rodrigo_visconti/48/3436_2.png" class="avatar"> Rodrigo_Visconti:</div>
<blockquote>
<p>a way to tilt one plane without affecting others</p>
</blockquote>
</aside>
<p>In addition to <a class="mention" href="/u/manjula">@manjula</a> and <a class="mention" href="/u/lassoan">@lassoan</a>  replies, each slice view may display its own Reformat Widget in the 3D view. You can then move around the handles and centre of rotation freely for each Reformat Widget independently.</p>

---

## Post #23 by @Rodrigo_Visconti (2020-11-25 12:32 UTC)

<p>I’ll try it. Thanks<br>
I’m using for cardiac valve segmentation.</p>

---

## Post #24 by @lassoan (2020-11-25 14:30 UTC)

<aside class="quote no-group" data-username="Rodrigo_Visconti" data-post="23" data-topic="14047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rodrigo_visconti/48/3436_2.png" class="avatar"> Rodrigo_Visconti:</div>
<blockquote>
<p>I’m using for cardiac valve segmentation.</p>
</blockquote>
</aside>
<p>We segmented many hundreds of valves on various imaging modalities and we always keep rotating the views so that remain orthogonal. Rotating only one, without adjusting the others, would make the others much less informative and confusing.</p>

---

## Post #25 by @Rodrigo_Visconti (2020-11-28 15:19 UTC)

<p>Great but my issue is subvalvar apparatus with is out of plane. Have you done this too?</p>

---

## Post #26 by @lassoan (2020-11-28 16:49 UTC)

<p>Yes, of course, you can rotate in each view until all your view axes line up with the valve axes.</p>

---

## Post #27 by @Rodrigo_Visconti (2020-12-20 17:05 UTC)

<p>Can you show how? Thanks again</p>

---

## Post #28 by @lassoan (2020-12-20 17:42 UTC)

<p>You can rotate slice views by using <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Left-click-and-drag</kbd> with slice intersections displayed. See documentation of <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">keyboard&amp;mouse shortcuts in slice views</a>.</p>

---
