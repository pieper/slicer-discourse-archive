# Feedback requested: How to improve mouse interaction in views?

**Topic ID**: 6420
**Date**: 2019-04-06
**URL**: https://discourse.slicer.org/t/feedback-requested-how-to-improve-mouse-interaction-in-views/6420

---

## Post #1 by @lassoan (2019-04-06 04:15 UTC)

<p>Redesigned markups allow us to add a lot of new features, and we need to ensure that these new features are conveniently accessible via keyboard shortcuts and mouse gestures.</p>
<p>Since number of mouse buttons and modifier keys are limited, one way of making more features accessible is to introduce more mouse modes. In each mouse mode, gestures could be mapped to different actions.</p>
<p>As a first step, we’ve introduced “Window/level” mode in latest nightly version, to prevent accidentally changing volume window/level (left-click-and-drag only changes window/level in the window/level mouse mode) and also to allow more sophisticated window/level adjustments (left-click-and-drag works as before; Ctrl + left-click-and-drag to highlight a region and optimize window/level for that; pressing Escape or right-click cancels the operation):</p>
<div class="lazyYT" data-youtube-id="u1B0F1KcVsk" data-youtube-title="3D Slicer - new mouse mode for window/level" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>What mouse modes would you like to have (instead of/in addition to, binding it to some complicated keyboard&amp;mouse gesture)?</p>
<ul>
<li>node select (we could select/unselect objects by clicking on them)</li>
<li>node translate, rotate</li>
<li>slice intersection move/rotate (in recent Slicer versions you can rotate intersecting slices if you show slice intersections and use Ctrl+Alt+Left-click-and-drag - but many people will not discover this)</li>
<li>split view zoom, pan, rotate, slice selection to a few different modes</li>
<li>…?</li>
</ul>

---

## Post #2 by @jamesobutler (2019-04-06 12:23 UTC)

<p>I just wanted to say this is welcomed improvement. The group I work with has implemented some things in the past that this now addresses.</p>
<p>Prevent accidentally changing volume window/level is a major one. We had always locked it and made the current volume lock/unlock window level with a keyboard shortcut.</p>
<p>Also we have moving slice intersections done by mouse hovering over an intersection and left click and dragging it to a new position. We implemented this because we observed users trying to do this instead of mouse scrolling in other slice views as a way of changing slice intersection shown in another view. Also I don’t think they knew about the shift+mouse move ability to move slice intersections.</p>

---

## Post #3 by @lassoan (2019-04-06 14:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Also we have moving slice intersections done by mouse hovering over an intersection and left click and dragging it to a new position.</p>
</blockquote>
</aside>
<p>Since slice intersections are  ow shown by a widget, too, we can easily implement moving the center or rotate it by drag-and-drop (I think it’s already implented, we just have not activated it in Slicer master version).</p>

---

## Post #4 by @pieper (2019-04-06 14:02 UTC)

<p>This is great <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>One additional ww/wl mode to consider: similar to the rectangle, draw a line and use that to define the range for the ww/wl.  For example if you really wanted to focus on the range of intensities in the skull, you could draw a kind of wavy curve through the bone (I had done this in a system many years ago and it was really handy).</p>
<p>Also, ideally these roi-based ww/wl adjustments should hot-update on every mouse move.</p>

---

## Post #5 by @Fernando (2019-04-12 10:52 UTC)

<p>I’ve seen many users accidentally change the window when trying to change the slices offset as in ITK-SNAP or MITK. I think enabling this by default could be useful, or maybe adding a button for it.</p>
<p>Quite unrelated, but I think the automatic window settings algorithm should be improved. I almost always have to adjust the contrast, no matter which image I’m loading. I think the automatic contrast adjustment of ITK-SNAP (Ctrl + J, I think) works great. I once looked into it to try to implement it for Slicer, but it all seemed out of my league and I finally gave up. Happy to participate in a potential effort, though.</p>

---

## Post #7 by @lassoan (2019-04-12 16:36 UTC)

<p>I’ve had a look at how ITK-Snap computes window/level (<code>AbstractContinuousImageDisplayMappingPolicy::AutoFitContrast()</code>) and it seems that it just uses linear scale between 0.1%-99.9% range of the image. We do the same in the regional auto-contrast (Ctrl + Left-click-and-drag in Adjust window/level mode). The limitation is that it always creates relatively low-contrast images (does not try to determine what is the relevant signal in the image).</p>
<p>Slicer’s auto window/level algorithm performs bimodal analysis of the image - it assumes that image consists of signal corrupted by noise and determines a window/level that optimizes visibility of the signal. In general this creates images with much better contrast, but it may make the image contrast too high if the image histogram’s first local maximum is not the actual signal’s peak.</p>
<p>Example: MRBrainTumor1 sample data set</p>
<p>ITK-Snap auto-adjust contrast produces very dark, low-contrast image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b00201f617a410e2b1600819875dd5b3ee8062b0.png" data-download-href="/uploads/short-url/p72kQklf3o6ENtqA9UPTQLCQq3K.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b00201f617a410e2b1600819875dd5b3ee8062b0_2_510x500.png" alt="image" data-base62-sha1="p72kQklf3o6ENtqA9UPTQLCQq3K" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b00201f617a410e2b1600819875dd5b3ee8062b0_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b00201f617a410e2b1600819875dd5b3ee8062b0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b00201f617a410e2b1600819875dd5b3ee8062b0.png 2x" data-dominant-color="1C1D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">658×645 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer’s auto window/level makes relevant details more visible:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3079c36a3690e2f42170437550a380b44c30a268.jpeg" data-download-href="/uploads/short-url/6UPNjg9J5Vojn2UZQfg1fjqZ6Ig.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3079c36a3690e2f42170437550a380b44c30a268_2_544x500.jpeg" alt="image" data-base62-sha1="6UPNjg9J5Vojn2UZQfg1fjqZ6Ig" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3079c36a3690e2f42170437550a380b44c30a268_2_544x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3079c36a3690e2f42170437550a380b44c30a268.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3079c36a3690e2f42170437550a380b44c30a268.jpeg 2x" data-dominant-color="4F4F5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">717×659 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The new mouse mode makes it easy to get ITK-Snap-like broad, low contrast images by selecting a large region of interest:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a528d088c6437fa931c802472a90db59d59597b.jpeg" data-download-href="/uploads/short-url/jJEKPTd30kBeQIjfC1UDmUVFPmj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a528d088c6437fa931c802472a90db59d59597b_2_548x500.jpeg" alt="image" data-base62-sha1="jJEKPTd30kBeQIjfC1UDmUVFPmj" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a528d088c6437fa931c802472a90db59d59597b_2_548x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a528d088c6437fa931c802472a90db59d59597b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a528d088c6437fa931c802472a90db59d59597b.jpeg 2x" data-dominant-color="41404C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">718×655 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or you can get good contrast in a very specific region:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80ed24a71fee801c5e74b61f5180c08163999bd0.png" data-download-href="/uploads/short-url/ioxbYnyHGwtzsr1H8i7O0Xmj8dy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80ed24a71fee801c5e74b61f5180c08163999bd0_2_545x500.png" alt="image" data-base62-sha1="ioxbYnyHGwtzsr1H8i7O0Xmj8dy" width="545" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80ed24a71fee801c5e74b61f5180c08163999bd0_2_545x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80ed24a71fee801c5e74b61f5180c08163999bd0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80ed24a71fee801c5e74b61f5180c08163999bd0.png 2x" data-dominant-color="5C5C68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">718×658 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, I think the current options for manual window/level adjustments cover most use cases quite well. Of course, there is always room for improvement, for example what may be missing:</p>
<ul>
<li>loading of default window/level preset from DICOM and other file formats that can store window/level</li>
<li>setting WW/WL to multiple volumes at the same time could be useful, but I don’t know where and how on the GUI we should offer this feature (maybe it could be added as a menu action in the subject hierarchy tree)</li>
</ul>
<p>If anybody would want to see improvements in these then we can discuss it further here and/or add an item in the <a href="https://issues.slicer.org/">issue tracker</a>.</p>

---

## Post #8 by @pieper (2019-04-12 18:24 UTC)

<p>Nice investigation Andras <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>A couple more notes:</p>
<ul>
<li>slicer’s bimodal analysis does almost always do a good job for me, but I know <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> told me years ago that when he loads masked images he gets bad result (e.g. skull stripped MR neuro).  This is because the bimodal assumes the two modes of the histogram will be air (ignored) and tissue (used to define the ww/wl).  For masked images the air is typically all 0, so the histogram is not really bimodal and the contrast is somewhat arbitrary.  We never dug deeper at the time, but maybe now we should and probably a simple heuristic could solve this case.</li>
<li>Also I thing context menu option to pick a strategy or just having a hotkey to cycle through strategies could be good.</li>
<li>window width / window center values from DICOM are loaded and applied, at least for scalar volumes,  If there are multiple they will all be available.  These are in the window/level presets portion of the Volume Information section of the Volumes module.</li>
</ul>

---

## Post #9 by @Fernando (2019-05-22 14:42 UTC)

<p>Just in case this is useful:<br>
I’ve been doing visual inspection of a lot of T1-weighted images recently. Most of the sequences are FSPGR 3D, FSPGR BRAVO or MPRAGE. Typically, the automatic windowing is good for BRAVO and MPRAGE and bad for FSPGR. Here are some screenshots of Slicer and ITK-SNAP for FSPGR 3D and FSPGR BRAVO of the same patient:</p>
<p>Slicer BRAVO:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e48e3397b263100012f0acca709770ccc9fb6a1.jpeg" data-download-href="/uploads/short-url/baxp1CPUuyePg982CvF9aBR1kM9.jpeg?dl=1" title="bravo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e48e3397b263100012f0acca709770ccc9fb6a1_2_690x478.jpeg" alt="bravo" data-base62-sha1="baxp1CPUuyePg982CvF9aBR1kM9" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e48e3397b263100012f0acca709770ccc9fb6a1_2_690x478.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e48e3397b263100012f0acca709770ccc9fb6a1_2_1035x717.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e48e3397b263100012f0acca709770ccc9fb6a1.jpeg 2x" data-dominant-color="666A6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bravo</span><span class="informations">1330×923 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>ITK-SNAP BRAVO:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1801dbdd8244202d166bb5fed679990e7e62c39.png" data-download-href="/uploads/short-url/rBMDE0YQItXqgU9ceRIL142FAeJ.png?dl=1" title="24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1801dbdd8244202d166bb5fed679990e7e62c39_2_471x500.png" alt="24" data-base62-sha1="rBMDE0YQItXqgU9ceRIL142FAeJ" width="471" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1801dbdd8244202d166bb5fed679990e7e62c39_2_471x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1801dbdd8244202d166bb5fed679990e7e62c39_2_706x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1801dbdd8244202d166bb5fed679990e7e62c39.png 2x" data-dominant-color="212222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">24</span><span class="informations">911×966 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer FSPGR:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58ebd7a9e04973faea77195d295835c43bcf2a6d.jpeg" data-download-href="/uploads/short-url/cGDj3YZqhksubURi6UutFQtvHf7.jpeg?dl=1" title="fspgr" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ebd7a9e04973faea77195d295835c43bcf2a6d_2_690x478.jpeg" alt="fspgr" data-base62-sha1="cGDj3YZqhksubURi6UutFQtvHf7" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ebd7a9e04973faea77195d295835c43bcf2a6d_2_690x478.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ebd7a9e04973faea77195d295835c43bcf2a6d_2_1035x717.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58ebd7a9e04973faea77195d295835c43bcf2a6d.jpeg 2x" data-dominant-color="808381"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fspgr</span><span class="informations">1330×923 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>ITK-SNAP FSPGR:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4df5378eaf7044a47403c60c7ee01e0d16dc342c.png" data-download-href="/uploads/short-url/b7E8Hc1qe8ajaE8PBVJo5UcfJVy.png?dl=1" title="19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4df5378eaf7044a47403c60c7ee01e0d16dc342c_2_538x500.png" alt="19" data-base62-sha1="b7E8Hc1qe8ajaE8PBVJo5UcfJVy" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4df5378eaf7044a47403c60c7ee01e0d16dc342c_2_538x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4df5378eaf7044a47403c60c7ee01e0d16dc342c_2_807x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4df5378eaf7044a47403c60c7ee01e0d16dc342c.png 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">19</span><span class="informations">1042×967 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here are the files (the link expires on 29/05/2019): <a href="https://we.tl/t-xj01qkb25s" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a></p>

---

## Post #10 by @lassoan (2019-05-23 14:37 UTC)

<p>Thanks for the follow-up. I agree that FSPGR_3D volume is displayed overexposed with Slicer’s global auto WW/WL setting (double-click on the image in WW/WL adjustment mode), while it looks nice with the area-based auto WW/WL (ctrl-left-click-and-drag in the middle of the image and drag it to cover the entire image).</p>
<p>It is because the global WW/WL setting detects the blanked out region in the image (red) as background and tries to improve visibility of the noisy background region (orange) by making it brighter.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f41e605b873176164e1d5c481b4b1a1c12d042c.png" data-download-href="/uploads/short-url/krjsQh970IeAVTOn7bJcp29dQlu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41e605b873176164e1d5c481b4b1a1c12d042c_2_690x435.png" alt="image" data-base62-sha1="krjsQh970IeAVTOn7bJcp29dQlu" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41e605b873176164e1d5c481b4b1a1c12d042c_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41e605b873176164e1d5c481b4b1a1c12d042c_2_1035x652.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41e605b873176164e1d5c481b4b1a1c12d042c_2_1380x870.png 2x" data-dominant-color="B6B6BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2273×1434 470 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We could probably tune the histogram analysis to make it a more robust against small blanked out regions. Or maybe allow users to choose between automatic WW/WL strategies (stretch WW to 0.1-99% range or to auto-detected range).</p>

---

## Post #11 by @fedorov (2019-05-23 16:06 UTC)

<p>Wouldn’t it be reasonable to completely ignore 0 intensity by the auto WW/WL setting algorithm? I guess this could cause problems when loading segmentations as grayscale images, but in other situations 0 can probably be ignored safely, since some level of noise will be present in the real image region. In MRI I believe those are not blanked regions, they are probably 0 because of how the image was reconstructed.</p>

---

## Post #12 by @lassoan (2019-05-26 14:19 UTC)

<p>I’ve created a <a href="https://gist.github.com/lassoan/8dde0bda226b20943a8b9dc430ed520b" rel="nofollow noopener">script</a> to test Slicer’s current (bimodal analysis based) auto window/level method and compare it to fixed percentile based method, on all Slicer sample images.</p>
<details>
<summary>
Description of methods used for generating the images</summary>
<ul>
<li>baseline: current method in Slicer</li>
<li>hist-0.1-99.9: minimum at 0.1th percentile, maximum at 99.9th percentile, no expansion (this setting is used by <a href="https://github.com/pyushkevich/itksnap/blob/0c31d9c1e0027d4f08b07d14a1e1494ceb56cf6f/Logic/ImageWrapper/DisplayMappingPolicy.cxx#L343-L390" rel="nofollow noopener">ITK-Snap</a>)</li>
<li>hist-1.0-99.9: minimum at 1th percentile, maximum at 99.9th percentile, min expanded by 10%</li>
<li>hist-1.0-99.0-x0.10: minimum at 1th percentile, maximum at 99th percentile, min expanded by 10%, max expanded by 10%</li>
<li>hist-1.0-99.0-x0.20: minimum at 1th percentile, maximum at 99th percentile, min expanded by 10%, max expanded by 20%</li>
</ul>
<p>The fixed percentile based method is implemented in <a href="https://vtk.org/doc/nightly/html/classvtkImageHistogramStatistics.html#a318e0294f2cdf6baf1a11691a1182e1b" rel="nofollow noopener">vtkImageHistogramStatistics</a>: window min/max is set at a certain percentile of the histogram, optionally extended by a fraction of the window size.</p>
</details>
<p>From the <a href="https://1drv.ms/f/s!Arm_AFxB9yqHt7kuycGJhF1gDKH_lA" rel="nofollow noopener">results</a> it is clear that the <strong>current auto window/level method is not optimal</strong>. Suppressing the first peak in the histogram is not necessarily a good idea for general use, as important signal may be in the first (“noise”) peak and it is hard to reliably detect boundaries of the “signal” peak. It would probably better to switch to the simple percentile method.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fernando">@Fernando</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
Could you have a look at the <a href="https://1drv.ms/f/s!Arm_AFxB9yqHt7kuycGJhF1gDKH_lA" rel="nofollow noopener">generated images</a> and tell if you have any preference for which method we should use in Slicer?</p>
<p>If you want to test it on your images then send the link to those or you can run this <a href="https://gist.github.com/lassoan/8dde0bda226b20943a8b9dc430ed520b" rel="nofollow noopener">code snippet</a> on your computer.</p>

---

## Post #13 by @pieper (2019-05-26 17:53 UTC)

<p>Thanks for doing this analysis <a class="mention" href="/u/lassoan">@lassoan</a>!  I’m fine with changing to one of the histogram methods.  Matching ITK-Snap could make sense if nothings obviously better.</p>
<p>Also useful would be to give users an easier way to discover window/level settings and presets, probably through a context menu on the slice viewers or similar.</p>

---

## Post #14 by @Fernando (2019-05-26 23:29 UTC)

<p>Nice analysis!</p>
<p>Methods 3 and 4 look best to me. Do you know why the CT scans “look good” (air and background are black) only sometimes? For example CT-cardio vs CT-chest.</p>

---

## Post #15 by @lassoan (2019-05-27 02:43 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="14" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Do you know why the CT scans “look good” (air and background are black) only sometimes?</p>
</blockquote>
</aside>
<p>It mainly depends on what intensity the background (outside the cylinder) is set to. Background in CTACardio is -1024, in CTChest it is -3024.</p>
<aside class="quote no-group" data-username="Fernando" data-post="14" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Methods 3 and 4 look best to me</p>
</blockquote>
</aside>
<p>Method 3 (hist-1.0-99.9) seems to be the best to me, too, as it produces somewhat lighter images than method 2. However, method 2 (hist-0.1-99.9) has the advantages that:</p>
<ul>
<li>it is symmetric (so, for example, if you invert the image you get the same min/max values; and it works the same way regardless the background is bright or dark)</li>
<li>it is the same setting as ITK-Snap uses</li>
</ul>
<aside class="quote no-group" data-username="pieper" data-post="13" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>useful would be to give users an easier way to discover window/level settings and presets, probably through a context menu on the slice viewers or similar.</p>
</blockquote>
</aside>
<p>I agree, it should be more discoverable. Adding menu (subject hierarchy menu items and some others, such as mouse mode) is on my list.</p>

---

## Post #16 by @lassoan (2019-05-27 15:56 UTC)

<p>I’ve submitted a <a href="https://github.com/Slicer/Slicer/pull/1143" rel="nofollow noopener">pull request</a> for using fixed 0.1 and 99.9 percentile for setting window/level automatically (Method 3, hist-1.0-99.9, same as ITK-Snap).</p>

---

## Post #17 by @talmazov (2019-07-08 20:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer’s auto window/level makes relevant details more visible:</p>
</blockquote>
</aside>
<p>Can this feature be accessed through python in an extension? If so, how?</p>

---

## Post #18 by @jcfr (2019-07-08 20:55 UTC)

<p>It is available in the preview release of Slicer published daily. See <a href="https://download.slicer.org/">https://download.slicer.org/</a></p>
<p>See this video for example of use:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u1B0F1KcVsk" data-video-title="3D Slicer - new mouse mode for window/level" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u1B0F1KcVsk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u1B0F1KcVsk/maxresdefault.jpg" title="3D Slicer - new mouse mode for window/level" width="" height="">
  </a>
</div>

<blockquote>
<p>Can this feature be accessed through python in an extension?</p>
</blockquote>
<p>You should be able to access the corresponding method from python by getting a reference to the display node associated with the scalar volume node.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume"> Change window/level (brightness/contrast) or colormap of a volume</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Make_mouse_left-click_and_drag_on_the_image_adjust_window.2Flevel"> Make mouse left-click and drag on the image adjust window/level</a></p>

---

## Post #19 by @lassoan (2019-07-09 00:20 UTC)

<p>See these code snippets to set default window/level or use custom percentiles for higher or lower contrast: <a href="https://gist.github.com/lassoan/8dde0bda226b20943a8b9dc430ed520b#file-autowindowleveltest-py-L12-L25" rel="nofollow noopener">https://gist.github.com/lassoan/8dde0bda226b20943a8b9dc430ed520b#file-autowindowleveltest-py-L12-L25</a></p>

---

## Post #20 by @chir.set (2019-07-17 08:44 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="1" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What mouse modes would you like to have (instead of/in addition to, binding it to some complicated keyboard&amp;mouse gesture)?<br>
…</p>
<ul>
<li>slice intersection move/rotate (in recent Slicer versions you can rotate intersecting slices if you show slice intersections and use Ctrl+Alt+Left-click-and-drag - but many people will not discover this)</li>
</ul>
</blockquote>
</aside>
<p>This concerns rotate in 2D views. It might be useful to have handles at the ends of each intersection line, that would rotate the current view only, or the corresponding view only (red handle for red view), without affecting the third view, like what is done by the ‘Reformat widget’. The idea is to rotate a single view quickly, without need for the reformat widget, which requires zooming and positioning.</p>
<p>Of course, the Reformat widget does the job already.</p>

---

## Post #21 by @lassoan (2019-07-17 18:00 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="20" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>like what is done by the ‘Reformat widget’.</p>
</blockquote>
</aside>
<p>Do you mean you would like to rotate the slices by interacting in the 2D or 3D views?</p>

---

## Post #22 by @chir.set (2019-07-17 19:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="6420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you mean you would like to rotate the slices by interacting in the 2D or 3D views?</p>
</blockquote>
</aside>
<p>I mean interacting in the 2D views, each view independantly.</p>
<p>The problem with Ctrl+Alt+LeftClick+Move is that the two other 2D views rotate at the same time while remaining at 90° intersection. This can be definitely useful (I saw the case today). If a 2D view can be independantly rotated, we can have the three views at different intersecting angles, and it can also be useful.</p>
<p>Just saw that a view can be temporarily frozen during above mentioned mouse gesture using :</p>
<p><code>slicer.app.layoutManager().sliceWidget('Green').mrmlSliceNode().DisableModifiedEventOn()</code></p>
<p>But when DisableModifiedEventOff() is applied again, on next rotation with that mouse gesture, pending events catch up and reset the views at 90°.</p>
<p>If you wish to consider it further, my take would be to provide a toggle button in each 2D view’s advanced settings (that widget appearing on mouse move in the upper left icon of the view) , meaning : ‘lock/unlock rotate’. I suppose this would require minimal coding on your side, while rotation is still done by above mentioned mouse gesture.</p>
<p>Other option would be to add handles to the each colored axis in each 2D view. Grabbing and moving the handle would rotate the view in the corresponding widget. This would obviously require more coding. It would be an additional rotation tool.</p>
<p>Regards</p>

---
