# Screenshot with transparent background in GUI

**Topic ID**: 26095
**Date**: 2022-11-06
**URL**: https://discourse.slicer.org/t/screenshot-with-transparent-background-in-gui/26095

---

## Post #1 by @mcranium (2022-11-06 23:43 UTC)

<p>Dear 3D Slicer community,</p>
<p>I have a question regarding the option to export screenshots with transparent backgrounds:<br>
There is the option to do so using a python snippet (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-3d-view-into-png-file-with-transparent-background" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>). Why is this not implemented in the GUI? Is there a technical reason why this is not implemented?</p>
<p>Most of the people that I know who work with 3D Slicer do not have basic skills in using scripting languages and are likely to be intimidated by the necessity of having to modify a section of python code. Moreover, I would consider exporting PNGs with transparencies as one of the core functionalities of a program such as 3D Slicer. PNGs with transparencies are so much easier to work with, when preparing figures and I think offering this functionality in the GUI would help a lot with the adoption of the program among the more visual-minded potential users. We have such nice visualization techniques already present in 3D Slicer and it is overall such a nice and intuitive experience even for students with little previous experience in other software. Making this option more accessible would really provide a more consistent experience for new  users.</p>
<p>I think in this respect there is also room for other improvements such as a GUI tool for setting the background color (including a gradient option) but having screenshots with transparent backgrounds available through the GUI is much more pressing.</p>
<p>Best wishes,<br>
Mario</p>

---

## Post #2 by @jamesobutler (2022-11-07 00:01 UTC)

<aside class="quote no-group" data-username="mcranium" data-post="1" data-topic="26095">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcranium/48/17153_2.png" class="avatar"> mcranium:</div>
<blockquote>
<p>PNGs with transparencies are so much easier to work with, when preparing figures and I think offering this functionality in the GUI would help a lot with the adoption of the program among the more visual-minded potential users.</p>
</blockquote>
</aside>
<p>I know many users that provide figures with the background specifically included. I’m not sure what a figure for a paper would look like with a transparent background. Can you post a few images of what you have created for your papers? Preferably the images that you created with 3D Slicer that you wish were easier to create than what you had to do.</p>

---

## Post #3 by @lassoan (2022-11-07 04:49 UTC)

<p>Right-click to copy the image to clipboard is added relatively recently (maybe a year ago), so we appreciate any feedback.</p>
<p>The current implementation is due to that we did not want to add two separate menu items for almost the same feature (copy with with/without background), so we chose the simpler, safer option to copy exactly what you see. I agree with <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that most users are fine with having a background (may not even realize that backgrounds can be transparent) and they just change the background to black or white if they want to blend in the image better with the background.</p>
<p>There is no technical difficulty in allowing taking screenshots with transparent background.<br>
This option is already available in Screen Capture module (in Advanced section). However, I don’t see where we could add an option for the “Copy image” option in the view context menu. We could add an option to the application settings, but most users would not find it. Do you have any suggestion how the option could be offered for users without making the GUI more busy (one more option in the menu) or less convenient (e.g., adding one more click)?</p>

---

## Post #4 by @mcranium (2022-11-07 10:08 UTC)

<p>Thank you for your replies!</p>
<p>I also think that many users will not use this feature, whether this accounts for most users, I am not sure.<br>
As for my workflow and that of most of my colleagues (zoomorphologists/palaeontologist): I like to save all my rendered images at more than enough resolution and as PNG with transparent background. This way I can later decide, maybe weeks afterwards how my background should look like when arranging the figure plates, while not having to go back to 3D Slicer or other Programs like Blender or Drishti. For many models a grey or slightly colored background has visual advantages to either a black or a white background. With a black background it is possible that the contrast to the darkest part of the model is a bit too high and with a white background it can be vice versa. Here an example of one of my colleagues (unfortunately does not use 3D Slicer, yet).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bd28bc9e0cde82b5433ec513dc4850dbb656cac.jpeg" data-download-href="/uploads/short-url/3Y7Z2xyilkdviVg02YYoaZN8n6I.jpeg?dl=1" title="ixac013_fig4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bd28bc9e0cde82b5433ec513dc4850dbb656cac_2_637x500.jpeg" alt="ixac013_fig4" data-base62-sha1="3Y7Z2xyilkdviVg02YYoaZN8n6I" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bd28bc9e0cde82b5433ec513dc4850dbb656cac_2_637x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bd28bc9e0cde82b5433ec513dc4850dbb656cac_2_955x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bd28bc9e0cde82b5433ec513dc4850dbb656cac_2_1274x1000.jpeg 2x" data-dominant-color="C9BAAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ixac013_fig4</span><span class="informations">1920×1505 332 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I also agree that menus should be kept as simple as possible. But I also think that adding this feature would not add much clutter to the menu. When I was looking for the feature this would be the place where I would expect the option to save the image with transparent background (quick sketch) and where I looked for it in the first place.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77c652ae6b03c287e9972ebd6b7ac32edabff5d1.png" data-download-href="/uploads/short-url/h5zIT2ncFOxgHT2bNtUQMUynsoF.png?dl=1" title="3dslicer_tr_bg_mockup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c652ae6b03c287e9972ebd6b7ac32edabff5d1_2_690x445.png" alt="3dslicer_tr_bg_mockup" data-base62-sha1="h5zIT2ncFOxgHT2bNtUQMUynsoF" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c652ae6b03c287e9972ebd6b7ac32edabff5d1_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c652ae6b03c287e9972ebd6b7ac32edabff5d1_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c652ae6b03c287e9972ebd6b7ac32edabff5d1_2_1380x890.png 2x" data-dominant-color="CACADE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer_tr_bg_mockup</span><span class="informations">2000×1291 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for pointing out that I can use and recommend the screen capture module in the meanwhile. Still I think such an option should be a bit more easily accessible to the user.</p>

---

## Post #5 by @lassoan (2022-11-27 02:49 UTC)

<p>If we changed the toolbar button so that it opens the Screen Capture module (instead of the very limited Annotation screenshot popup) would that be easy enough to find? Or we should also move out the transparent background option from the Advanced section?</p>

---

## Post #6 by @mcranium (2022-11-28 12:57 UTC)

<p>From the perspective of a new user, having the toolbar button link to the Screen Capture Module is probably not the best experience. A new user wants something to easily save a 2D view to their drive (so that they can share it or embed it in a figure plate. Having to use a more complex UI (the Screen Capture module where “screenshots” are only one option is probably not the best experience.</p>
<p>In my opionion, a perfect version of the “Annotation Screenshot” Dialog should be named “Save image” or “Save Screenshot”, so that it is clear that this is not only for annotating, and should save images immediately - not only after pressing CTRL + S to save everything. In this regard one could think of a nomenclatural distinction between saving/exporting still images and setting up reproducible screen capture instances. I suspect only the more experienced users will make efficient use of the latter and most users would prefer the former because of its simplicity. Then, it should contain an option to have a transparent background as well as an option to adjust the final size of the rendered (“scale factor”, this is already well implemented, I like the simplicity because there is no confusion about what will be visible in the captured image).</p>

---
