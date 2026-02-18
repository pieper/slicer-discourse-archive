# Registering a volume rendering default presets automatically

**Topic ID**: 32964
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/registering-a-volume-rendering-default-presets-automatically/32964

---

## Post #1 by @muratmaga (2023-11-22 17:59 UTC)

<p>We have a diceCT preset in SlicerMorph for our contrast-enhanced microCTs of mouse embryos. I would like this preset to be automatically applied to volumes I drag into 3D viewer, like it currently does for MRHead (it chooses the MRI preset, without me specifying).</p>
<p>How can I accomplish this?</p>

---

## Post #2 by @lassoan (2023-11-22 19:41 UTC)

<p>Simplest, not very clean solution: add an observer to the scene for node added events, whenever volume rendering display node is added then check if it belongs to your contrast-enhanced microCT type and if yes then change the preset.</p>
<p>Nicer solution: Add a subject hierarchy plugin that recognizes your “contrast-enhanced microCT” volume type (from value range, spacing value, etc. or any other attributes that the importer may set on the volume) and override the <code>showItemInView</code> method (e.g., call the default one but then change the volume rendering preset to your preferred one). It would take just a few ten lines of Python code, but unfortunately it seems that currently <code>showItemInView</code> is not Python-wrapped, so you would need to write the plugin in C++. It would be easy to add Python wrapping to <code>showItemInView</code>, and this design would be quite flexible and would also allow you to specify custom icon, context menu items, etc. for this type of volumes.</p>
<p>Another approach could be to change <code>vtkSlicerVolumeRenderingLogic::SetRecommendedVolumeRenderingProperties</code> to check the node attributes and if it finds a certain attribute (e.g., <code>DefaultVolumeRenderingPreset</code>) then use that as default preset for volume rendering. The attribute could be set by the importer or could be added in a callback function that is called whenever a new node is added to the scene.</p>
<p>Maybe the best solution would be to implement <a href="https://discourse.slicer.org/t/hanging-protocol-for-displaying-pet-ct-images/28598#!">hanging protocols</a>, where not just the volume rendering preset but view layout, window/level preset, etc. would be set up based on the type of the loaded data. For example, you could define a “Contrast-enhanced microCT” protocol that would be offered automatically when the input data matches requirements specified in the protocol. See more information here:</p>
<aside class="quote" data-post="1" data-topic="28598">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f0a364/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/hanging-protocol-for-displaying-pet-ct-images/28598#">Hanging protocol for displaying PET/CT images</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Is is possible to add on a feature that saves a user’s preferred modality-specific viewing settings.  I view PET/CT images regularly and it would be great to be able to have my view settings saved so I’m always viewing PET with PET-Heat in 0-20SUV, then CT in CT Abdomen Window without having to adjust this every single time I load a new case.  Having custom view settings for a given user where it loads up the same way each time would be great!
  </blockquote>
</aside>


---

## Post #3 by @smrolfe (2023-11-29 20:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="32964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Simplest, not very clean solution: add an observer to the scene for node added events, whenever volume rendering display node is added then check if it belongs to your contrast-enhanced microCT type and if yes then change the preset.</p>
</blockquote>
</aside>
<p>I gave this a quick try, but at the time the volume rendering display node is added to the scene, the displayable node has not been assigned. Is there another way to get the associated node, or an event I could catch by monitoring the volume rendering display node?</p>

---

## Post #4 by @mau_igna_06 (2023-11-29 21:01 UTC)

<p>Hi</p>
<p>Did you try a QTimer with a lambda? This may delay the execution of your code enough for your use case</p>
<p>Hope it helps</p>

---

## Post #5 by @smrolfe (2023-11-29 21:28 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="4" data-topic="32964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Did you try a QTimer with a lambda?</p>
</blockquote>
</aside>
<p>Works perfectly, thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>!</p>

---
