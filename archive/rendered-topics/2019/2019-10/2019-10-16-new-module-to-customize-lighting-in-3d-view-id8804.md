# New module to customize lighting in 3D view

**Topic ID**: 8804
**Date**: 2019-10-16
**URL**: https://discourse.slicer.org/t/new-module-to-customize-lighting-in-3d-view/8804

---

## Post #1 by @lassoan (2019-10-16 20:24 UTC)

<p>A new experimental module, “Lights”, was added to “Sandbox” extension that allows you to change lightkit parameters with a simple GUI. See a short demo video here:</p>
<div class="lazyYT" data-youtube-id="rQZ9enRbn0w" data-youtube-title="Customize 3D view lighting in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If we get the feedback that this module is useful then we’ll consider adding it to the Slicer core.</p>

---

## Post #2 by @Melodicpinpon (2019-10-16 23:22 UTC)

<p>Really beautifull. Thank you for the share.</p>

---

## Post #3 by @muratmaga (2019-10-16 23:32 UTC)

<p>This looks really cool. Thanks Andras.</p>

---

## Post #4 by @lassoan (2019-10-17 01:09 UTC)

<p>If there is interest for more photorealistic rendering then we could consider exposing additional rendering backends that VTK supports. You can already try VTK’s NVidia Optix and OSPray rendering backends in Paraview. They are very nice for rendering surface meshes with shadows and reflections. I did not have much luck with producing nice volume renderings with them.</p>

---

## Post #5 by @muratmaga (2019-10-17 03:07 UTC)

<p>FYI Sandbox does not show up in the extension search, while it is listed under examples.</p>

---

## Post #6 by @muratmaga (2019-10-17 04:03 UTC)

<p>I think it looks good enough to be used as is.</p>
<p>Couple things I would suggest when you have a chance (in terms of priority):</p>
<ol>
<li>Button to revert back to defaults (or a way to unset them).</li>
<li>Option to save and load light settings (like volume properties).</li>
<li>Can warmth be a color palette?</li>
<li>I am not sure how to make use of create View functionality. I know it is something to do with Slice Controllers module, but it is not clear to me how to control different views with a single 3D render window.</li>
</ol>
<p>But I think it is looking great, would rather see it part of core sooner than later. Thanks again.<br>
M</p>

---

## Post #7 by @lassoan (2019-10-17 13:10 UTC)

<p>These are good suggestions, you can <a href="https://github.com/PerkLab/SlicerSandbox/issues">submit them as issues</a> to keep track of them.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="8804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not sure how to make use of create View functionality. I know it is something to do with Slice Controllers module, but it is not clear to me how to control different views with a single 3D render window.</p>
</blockquote>
</aside>
<p>I’m not sure what you mean. Could you please clarify?</p>

---

## Post #8 by @muratmaga (2019-10-18 01:09 UTC)

<p>Here are my steps:<br>
Download MRHEad.nrrd, go to volume rendering set MR preset, switch to lights, create a new view, and set the lights such that effect should clear (e.g., very high intensity), click setup lightkit. Go back to volume rendering, expand the inputs tab, and select the newly created view as view (as oppose to view1 explicitly or all options, which is default). In my case I am getting a blank scene.</p>
<p>If I switch to view controllers, then I can see the new view doesn’t layout number like view1 does. Whether that matters or not I don’t know.</p>

---

## Post #9 by @lassoan (2019-10-18 03:10 UTC)

<blockquote>
<p>Download MRHEad.nrrd, go to volume rendering set MR preset</p>
</blockquote>
<p>Do you enable show volume rendering?</p>
<blockquote>
<p>switch to lights</p>
</blockquote>
<p>Do you create lightkit, too?</p>
<blockquote>
<p>create a new view</p>
</blockquote>
<p>by switching to a different layout?</p>
<blockquote>
<p>and set the lights such that effect should clear (e.g., very high intensity)</p>
</blockquote>
<p>Do you mean just set up some lighting that looks different? With the current version of the module I cannot make the rendering look burnt in.</p>
<blockquote>
<p>click setup lightkit. Go back to volume rendering, expand the inputs tab, and select the newly created view as view (as oppose to view1 explicitly or all options, which is default). In my case I am getting a blank scene.</p>
</blockquote>
<p>What do you mean? The volume rendering should appear in each view that is checked in the View list.</p>
<p>Maybe a few screenshots should help me to understand what you do and what your question is.</p>

---

## Post #10 by @muratmaga (2019-10-18 03:33 UTC)

<p>This is what threw me off:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/843afdceccb4817f7d09d7f3c3e523fbd16e01c0.png" alt="image" data-base62-sha1="iRLpHZnVeKPrTfx9K2dEAqp9o9G" width="484" height="252"></p>
<p>I thought I can create a new view, and then choose it in the Volume Rendering options, so that I can have control over when to use the lights settings (View1 for default, the newly create view for lights on rendering etc). But as far as I can tell the view created in the Lights module has no usability in volume rendering.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7df48bf276af4e2fba3b48fc9060cc5a6ca1262f.png" alt="image" data-base62-sha1="hYfCBnqoHHO0SQvDzrPSfXNi6Sz" width="484" height="209"></p>

---

## Post #11 by @lassoan (2019-10-18 14:23 UTC)

<p>I see, the “Create new View” is just a bug, I’ve forgot to disable the “Create new” option in the node selector. Creating a new view involves much more than just creating a new view node. I’ll disable the option.</p>

---

## Post #12 by @muratmaga (2019-10-18 16:31 UTC)

<p>Thanks Andras. This is great</p>

---

## Post #13 by @Melodicpinpon (2019-11-25 12:55 UTC)

<p>Good afternoon,</p>
<p>I try to use it and although I found the Sandbow extension in the exemples of the extensions and installed it; closed and restarted 3DSlicer; I still do not find the Lights module.</p>
<p>Did I miss a step?</p>

---

## Post #14 by @pieper (2019-11-25 13:22 UTC)

<p>Are there any clues in the error log?</p>

---

## Post #15 by @Fishguy (2020-07-02 20:55 UTC)

<p>This is fabulous. We would use this a lot.</p>

---

## Post #16 by @Ugi_Mikla (2020-10-22 17:37 UTC)

<p>did u manage? i have the same problem.</p>

---

## Post #17 by @Ugi_Mikla (2020-10-22 17:39 UTC)

<p>I think ist’s Slicers version</p>

---

## Post #18 by @muratmaga (2020-10-22 18:27 UTC)

<aside class="quote no-group" data-username="Ugi_Mikla" data-post="16" data-topic="8804" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ugi_mikla/48/7603_2.png" class="avatar"> Ugi_Mikla:</div>
<blockquote>
<p>did u manage? i have the same problem.</p>
</blockquote>
</aside>
<p>You mean Lights module is not available to you after installing the Sandbox extension? If so, try with the latest stable.</p>

---

## Post #19 by @manjula (2020-10-22 19:35 UTC)

<p>This is great and many thanks for this great tool this will save lot of time when its come to taking nice photos for publication <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:">.  … reset/undo button as suggested earlier would be fabulous too.</p>
<p>Thank you again.</p>

---

## Post #20 by @lassoan (2020-10-22 20:59 UTC)

<p>I’ve added presets to Lights button (default, ceiling, side, sunset, opera). The “default” preset can be used to reset to default. It’ll be available in the stable and preview releases tomorrow.</p>
<p>Feel free to suggest changes to these presets or define new ones.</p>
<p>Slicer Preview Release now uses <a href="https://blog.kitware.com/vtk-pbr/">VTK9, which has lots of new photorealistic rendering features</a>. If someone has time to play with these options and come up with code snippets that set up interesting visualizations then we can integrate those into the Lights module.</p>

---

## Post #21 by @lzekelma (2021-10-07 19:55 UTC)

<p>Hello, I’m new to Slicer and I would like to use the Lights module to make a nice figure for my paper.  However, I cannot seem to find the Sandbox extension in the extension manager.  Do you have any suggestions on where I may find the Lights module? Many thanks!</p>

---

## Post #22 by @lassoan (2021-10-07 20:02 UTC)

<p>Extensions are only provided for the latest Slicer Stable Release or latest Slicer Preview Release. I would recommend the latest Slicer Preview Release (downloaded yesterday or today).</p>

---

## Post #23 by @rbumm (2021-10-11 11:58 UTC)

<p>Tried this in Preview and think this will be very helpful for preparing slides or illustrations.</p>

---
