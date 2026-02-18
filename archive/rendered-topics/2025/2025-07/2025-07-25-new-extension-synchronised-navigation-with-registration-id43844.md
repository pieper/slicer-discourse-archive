# New extension: Synchronised Navigation with Registration

**Topic ID**: 43844
**Date**: 2025-07-25
**URL**: https://discourse.slicer.org/t/new-extension-synchronised-navigation-with-registration/43844

---

## Post #1 by @koeglfryderyk (2025-07-25 15:05 UTC)

<p>I created a new extension for viewing registrations. It implements what is sometimes called “synchronised navigation” - <em>simultaneous visualization of the same spatial location across multiple image series</em></p>
<p>The basic idea is that we load fixed and moving images, the corresponding registration, and when we move the cursor in one image, a markup follows in the second image (the position of the markup is calculated based on the registration).</p>
<p>Here is a sort video demo:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d74f7178bee6a0a890607af72577aeb4250c61f.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfbb7310ebf8d63bdbfe974cdcfbfbe0cc5f8d83.jpeg" data-video-base62-sha1="kbnV2Xzzu6P88vrQWmzshRkfREP.mp4">
  </div><p></p>
<p>Some PACS providers, like <a href="https://medical.sectra.com/product/sectra-radiology-pacs-ris/" rel="noopener nofollow ugc">Sectra</a>, implement this feature (either via slices manually linked by the user or by a commercial registration algorithm).</p>
<p>I have already been using this with a few radiologists, and they seem to like it (when the registration is accurate).</p>
<p>Is this interesting to this community?<br>
If yes:</p>
<ul>
<li>Should it have more features?</li>
<li>Should it be a standalone extension, or does it make sense to integrate it somewhere?</li>
</ul>
<p>This is in some way similar to this concept <a href="https://discourse.slicer.org/t/views-synchronization-after-registration/15613" class="inline-onebox">Views synchronization after registration</a>, however, the main difference is that it shows the original moving image. As far as I understand, radiologists don’t always want to see a deformed moving image.</p>
<p>The code for anyone interested is available here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/koegl-PhD/registrationViewer/tree/registrationViewer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/koegl-PhD/registrationViewer/tree/registrationViewer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/koegl-PhD/registrationViewer/tree/registrationViewer" target="_blank" rel="noopener nofollow ugc">GitHub - koegl-PhD/registrationViewer at registrationViewer</a></h3>

  <p><a href="https://github.com/koegl-PhD/registrationViewer/tree/registrationViewer" target="_blank" rel="noopener nofollow ugc">registrationViewer</a></p>

  <p><span class="label1">Viewer designed for comparing registration results</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>How did I implement this (in short)?</p>
<ul>
<li>create 6 vtkMRMLMarkupsFiducialNode (one for each view)</li>
<li>show the nodes in all views except for the one where the cursor is</li>
<li>use <code>SetSliceOffset()</code> to set the offset of all views to the position of the corresponding Fiducial node (except for the one where the cursor is)
<ul>
<li>for the views from the second image, first transform the corresponding fiducial nodes with the transformation and then set the offsets)</li>
</ul>
</li>
</ul>
<p>One small feature that I included is that when the user double clicks on a view, e.g., the Red one, a compare view opens with the Red and Red+ views side by side.</p>

---

## Post #2 by @manjula (2025-07-25 17:02 UTC)

<p>This is superb. Thanks a lot for your efforts.</p>

---

## Post #3 by @pieper (2025-07-30 21:21 UTC)

<p>Hi <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> I agree this is useful functionality.</p>
<p>But did you look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/comparevolumes.html">CompareVolumes module</a> that already exists in Sllicer?  As far as I know it already has the  features you described, except the part where you show the correspondence but not the transformed volume.  That sounds nice.</p>
<p>Plus CompareVolumes offers several other features, like an arbitrary number of volumes (selectable from all the loaded volumes, with the option to drag-and-drop to specify the order of the display), hot-linking pan/zoom/scroll operations, some animation modes for cross-fading between volumes, and a ‘compare cursor’ that provides an optionally magnified checkerboard inspection tool.</p>
<p>CompareVolumes was created to support some earlier research and it could certainly benefit from improvements, so maybe we could join forces?</p>

---

## Post #4 by @koeglfryderyk (2025-07-31 11:35 UTC)

<p>I’d love to join forces on the Compare Volumes module!</p>
<p>I could fork your <a href="https://github.com/pieper/CompareVolumes" rel="noopener nofollow ugc">repo</a> and implement the synchronised navigation feature, but I think we have to discuss a few things</p>
<p><strong>Synchronised navigation feature</strong></p>
<p>Initially, I thought I could implement it with the built-in crosshair, but for this feature, two decoupled crosshairs would be needed - one for the fixed and one for the moving. As far as I understood, you can only have one crosshair; creating another one would involve significant changes to the MRML Lib in Slicer (I think in vtkMRMLCrosshairDisplayableManager)</p>
<p>Therefore, I implemented it with markups for each view, which can then be transformed with the registration- it works well, but seems a bit hacky - do you have a better idea for how this could be done?</p>
<p><strong>UI</strong></p>
<ol>
<li>How should the user choose the transformation?</li>
<li>How should the user choose the fixed and moving images?</li>
<li>How should the user enable the synchronisation (I would also like to have a keyboard shortcut in addition to a button)</li>
</ol>
<p>For example, like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd10851b60e54d4e5a11e7637b5657094029e49.png" data-download-href="/uploads/short-url/jWSdxJ4Y45hZ3s9k2gXatOtBdPj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bd10851b60e54d4e5a11e7637b5657094029e49.png" alt="image" data-base62-sha1="jWSdxJ4Y45hZ3s9k2gXatOtBdPj" width="473" height="146"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">473×146 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2025-07-31 14:31 UTC)

<p>Hi <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> -</p>
<p>What’s the nature of your transformations and what is the area of interest for your research (i.e. torso CT mainly?).  That is, what is your target use case, since things like UI options and keyboard shortcuts are best considered in the context of a concrete clinical application.</p>
<p>I agree it’s not good to show clinicians distorted scans, as that could lead to misinterpretation.  And yes, showing the corresponding points using two crosshairs would make sense, but using a markup as a fallback is also not a bad idea.  If you look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/landmarkregistration.html">LandmarkRegistration</a> module (code <a href="https://github.com/Slicer/LandmarkRegistration">here</a>), which uses the CompareVolumes logic under the hood, there is some code for managing per-volume markup lists of corresponding points.  This way they can be moved interactively in either view and the other views are update through the transform to show the corresponding point.  It’s probably very similar to the code you have, and maybe we can factor it out for reusability.</p>
<p>Another thing I’ve been playing with related to this is using segmentation results (e.g. from TotalSegmentator) to define correspondence between scans even when the patient’s body position is different.  I.e. if you are looking at a tumor that’s a few centimeters from the femur, then registering the two femurs with a rigid transform puts the two tumors in close approximation even if the hip angles are very different in the two scans.  There’s a prototype implementation <a href="https://github.com/pieper/SegmentationRegistration/blob/main/Prototypes/idc-segreg.py">here</a>, where you can pick the anatomy you want to use for the local registration.  Of course the registration is very good close to the rigid structures but can be very bad far from the selected structures.  One feature I considered is that when you pick a point to compare, the either the single closest structures is used, or maybe the nearest few are used to define a blended rigid transform.</p>
<p>It would be great if we could develop layers of functionality, from general utilities through very dedicated task-specific interfaces.</p>

---

## Post #6 by @koeglfryderyk (2025-07-31 16:31 UTC)

<p>Until now I used my extension for rigid and deformable transformations - I was hoping to make a general tool for any transformation type.</p>
<p>I guess you’re right, let’s not focus on the UI options and shortcuts for now, I can always just create them for my specific use case.</p>
<p>I’m currently evaluating registration algorithms with this tool in a reader study with a head &amp; neck CT dataset (the example from my video was just from the <a href="https://zenodo.org/records/3835682" rel="noopener nofollow ugc">Learn2Reg LungCT</a> dataset as I can’t share my head &amp; neck data).</p>
<p>The local registration seems really interesting, my radiology Prof already mentioned multiple times that he’s usually only interested in registration at specific sites of interest. Could you update the link to the prototype implementation of the local registration? I get a 404 error, maybe this repo is private?</p>
<p>Then my question is what should be our or my next steps?</p>
<p>I could take a look at the LandmarkRegistration code and see if there is any common code to factor out.</p>

---

## Post #7 by @pieper (2025-07-31 17:42 UTC)

<p>Ah, right - the repo was private since it’s a work in progress, but I <a href="https://github.com/pieper/SegmentationRegistration/blob/main/Prototypes/idc-segreg.py">made it public now</a>.</p>
<p>In terms of next steps, it would be great if you could try the CompareVolumes on some of your data an registration results and see if the features and Lib code are a good fit for what you need.  For example, in the LandmarkRegistration it sets up three rows of axi/sag/cor with the fixed, moving, and blended fixed/moving, which I find helpful for reviewing segmentation.  You can do similar things with CompareVolumes by setting one of the volumes as the common background and unselecting it from the checklist.  But I think the workflow is probably not so intuitive and maybe we can repackage into a dedicated one-to-one registration review module, like your current version but with more features.</p>

---

## Post #8 by @koeglfryderyk (2025-08-04 11:11 UTC)

<p>thanks</p>
<p>I used CompareVolumes before and liked the functionality. I think we could use most of the code and then, e.g., just integrate my code into it.</p>
<p>The only thing that was not intuitive for me was that I had to click ‘Compare’ Checked Volumes’ every time I made a change, but this can easily just be explained or done automatically when the user makes some changes (e.g., checks a different box).</p>
<p>We could, for now, limit the module to two images only (Fixed and Moving), and in the future, think of integrating more images and deformations if we have, e.g., a sequence of registered images from multiple time points.</p>
<p>I think we could have two modes:</p>
<ul>
<li>Mode 1:
<ul>
<li>Use the deformed moving image (as it is now in CompareVolumes and Landmark Registration)</li>
</ul>
</li>
<li>Mode 2:
<ul>
<li>Use the original moving image and link the images with the registration</li>
</ul>
</li>
</ul>
<p>In terms of features, I would keep all CompareVolumes features (common background/label, hot link cursor, visualization options, and the layer reveal cursor), and maybe add two more features:</p>
<ul>
<li>Difference image between the Fixed and deformed Moving</li>
<li>Jacobian Determinant of the displacement field, as this is often used in papers to evaluate the quality of the displacement field (folding, volume growth, shrinkage)</li>
</ul>

---

## Post #9 by @pieper (2025-08-04 14:58 UTC)

<p>Sounds good <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> - it makes sense to me that we have generic functionality in the CompareVolumesLogic and also make generic widgets that can be reused in various special purpose modules like the one you want with only two volumes and registration comparison features.  We can still have the CompareVolumes module itself expose the more generic features for selections from all the volumes.</p>
<p>Regarding determinant of the Jacobian, maybe that should be added to the Transforms module visualization, and then the registration inspection module it could have streamlined ways of enabling it or other transform visualization modes.</p>

---

## Post #10 by @koeglfryderyk (2025-08-13 17:23 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>I incorporated the orientation widget, hot linking, and view management from CompareVolumes, while trying to reuse as much code as I could (from CompareVolumes and RegistrationLib).</p>
<p>The code is available <a href="https://github.com/koegl-PhD/registrationViewer/tree/registrationViewer" rel="noopener nofollow ugc">here</a>, and some sample data is available <a href="https://github.com/koegl-PhD/registrationViewer/releases/tag/exampleData" rel="noopener nofollow ugc">here</a>.</p>
<p>I left out all the functionality concerning the visualisation of overlays (common background/label, cursor reveal, flicker/rock, etc), as to me, these functionalities don’t make sense when working with the original moving image (and not the warped one).</p>
<p>From the CompareVolumes module, I imported the <code>CompareVolumesLogic</code> class - that was pretty straightforward. The only thing that could be changed to help with my module is for <code>viewerPerVolume</code> and <code>viewersPerVolume</code> to return <code>sliceNodesByViewName</code> grouped by volume node.</p>
<p>However, I had to reimplement the orientation widget</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce234d41f0470823054a8eb185d3305569134f92.png" data-download-href="/uploads/short-url/tpzZxIF5iMTeJ0SXXfguls5kXSy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce234d41f0470823054a8eb185d3305569134f92.png" alt="image" data-base62-sha1="tpzZxIF5iMTeJ0SXXfguls5kXSy" width="322" height="116"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">322×116 4.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>- so maybe this could be a candidate for a generic widget</p>
<p>This is the current UI of my extension</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/535db145908d21d68e3e10c03904ffa0dbba8edb.png" data-download-href="/uploads/short-url/bTumDXobkjUyZeCpPzaQqrtPBkn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/535db145908d21d68e3e10c03904ffa0dbba8edb.png" alt="image" data-base62-sha1="bTumDXobkjUyZeCpPzaQqrtPBkn" width="473" height="283"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">473×283 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @pieper (2025-08-13 18:15 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="10" data-topic="43844">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p><code>viewerPerVolume</code> and <code>viewersPerVolume</code> to return <code>sliceNodesByViewName</code> grouped by volume node.</p>
</blockquote>
</aside>
<p>If you can find a way to do this in a backwards-compatible way that would be great.  If not maybe helper methods that re-organize the results could be added.</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="10" data-topic="43844">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>maybe this could be a candidate for a generic</p>
</blockquote>
</aside>
<p>Yes, that could make sense.</p>
<p>I don’t know how much time/effort you have available but if you could contribute back to  improve the slicer cade base that would be great.</p>

---

## Post #12 by @koeglfryderyk (2025-08-19 09:06 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="43844">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If you can find a way to do this in a backwards-compatible way that would be great. If not maybe helper methods that re-organize the results could be added.</p>
</blockquote>
</aside>
<p>I created a <a href="https://github.com/pieper/CompareVolumes/pull/15" rel="noopener nofollow ugc">pull request</a> to CompareVolumes where I implemented this in a backwards-compatible way by using a default false argument, through which an additional dict can be returned.</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="10" data-topic="43844">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>so maybe this could be a candidate for a generic widget</p>
</blockquote>
</aside>
<p>And I just realised that LanmdarkRegistration already has the orientation panel integrated into its Visualization widget, so I just reused it (by hiding the other elements, like it was done in CompareVolumes).</p>
<p>If you want, I can also integrate the orientation panel from LandmarkRegistration into CompareVolumes - currently, the orientation widget is made from scratch in CompareVolumes</p>

---

## Post #13 by @pieper (2025-08-21 18:27 UTC)

<p>Thanks again for working on this <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="12" data-topic="43844">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>If you want, I can also integrate the orientation panel from LandmarkRegistration into CompareVolumes - currently, the orientation widget is made from scratch in CompareVolumes</p>
</blockquote>
</aside>
<p>Yes, if we can make the code cleaner and more reusable that’s great.</p>

---

## Post #14 by @koeglfryderyk (2025-08-25 08:47 UTC)

<p>I created a new <a href="https://github.com/pieper/CompareVolumes/pull/16" rel="noopener nofollow ugc">pull request</a> that reused the widget from LandmarkRegistration</p>

---
