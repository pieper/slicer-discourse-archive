# Setting the volume property to be used when a volume is rendered automatically

**Topic ID**: 16653
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/setting-the-volume-property-to-be-used-when-a-volume-is-rendered-automatically/16653

---

## Post #1 by @muratmaga (2021-03-20 04:20 UTC)

<p>When I drag and drop volume to the 3D render, it automatically renders with the volume property MR. I would like it to use one of my custom presets that are registered via the .slicerrc.py (as per this instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets" class="inline-onebox">Volume rendering — 3D Slicer documentation</a>)</p>
<p>How can I set this up?</p>

---

## Post #2 by @lassoan (2021-03-20 04:57 UTC)

<p>Drag-and-drop to views are handled by the subject hierarchy owner plugin associated with the node.</p>
<p>One option is to create a custom subject hierarchy plugin that will recognize your special volume and “claim” it for itself by returning high confidence value for it in <code>canOwnSubjectHierarchyItem</code> method. Then implement in the plugin’s <code>showItemInView</code> any behavior that you need.</p>
<p>Another option is to override the <a href="https://github.com/Slicer/Slicer/blob/431eba37b11025c6e2b43937dc0567714fbd018e/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx#L1436-L1480">default low/medium/high-dynamic-range volume rendering presets</a> (US-Fetal/MR-Default/CT-Chest-Contrast-Enhanced) with your by removing these presets and registering your custom ones with the same names.</p>
<p>There could be many more ways of making this more configurable. Can you write a bit more about your use case?</p>

---

## Post #3 by @muratmaga (2021-03-20 05:14 UTC)

<p>I have about 60 mouse skulls that are scanned and reconstructed the same way. I designed a custom volume property that renders them nicely. I have bunch of LMs to review. I load each volume and the markups file and then I am trying to cut down the number of click I get from loading the volume to rendering it in 3D.</p>
<p>I registered mine as SM_mouse, and is available as a preset now. But when I drag and drop my mouse volume into 3D viewer, it still renders with MR-Default, and I still have to choose my preset from the available preset. The goal is minimizing the interactions.</p>

---

## Post #4 by @muratmaga (2021-03-21 05:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Another option is to override the <a href="https://github.com/Slicer/Slicer/blob/431eba37b11025c6e2b43937dc0567714fbd018e/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx#L1436-L1480">default low/medium/high-dynamic-range volume rendering presets </a> (US-Fetal/MR-Default/CT-Chest-Contrast-Enhanced) with your by removing these presets and registering your custom ones with the same names.</p>
</blockquote>
</aside>
<p>I ended up going with this route and it works quite well for my challenge.</p>
<p>However, this is slightly ‘hacky’ as in, if I distribute a presets.xml that contains various overwritten presets optimized for data that comes out of our scanner (so that my collaborators have the same settings), it is likely to confuse people (since I simply overwrote the MR-Default, and created a copy of it called MR-Default2 in case I do need it for MR datasets).</p>
<p>It would be great if the presets can be more easily added, and that defaults used for drag and dropping can be customizable…</p>

---

## Post #5 by @lassoan (2021-03-25 13:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="16653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It would be great if the presets can be more easily added</p>
</blockquote>
</aside>
<p>There is an issue for this already. If it gets enough <a href="https://discourse.slicer.org/t/about-the-feature-requests-category/30">upvotes</a> then we’ll get to it:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5505">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5505" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5505" target="_blank" rel="noopener">Save current volume rendering setting as a preset</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-05" data-time="15:55:28" data-timezone="UTC">03:55PM - 05 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/alshakhasm" target="_blank" rel="noopener">
          <img alt="alshakhasm" src="https://avatars.githubusercontent.com/u/80116383?v=4" class="onebox-avatar-inline" width="20" height="20">
          alshakhasm
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

I always st<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">art creating my volume rendering from scratch, however, that takes a long time and a lot of time and guessing 

## Describe the solution you'd like

creat a simple " create a custom preset " in the volume rendering module</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="16653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>defaults used for drag and dropping can be customizable</p>
</blockquote>
</aside>
<p>We could allow users to choose 3 custom default presets in the application settings. You can add a feature request in the issue tracker and see how much upvotes it gets.</p>
<p>In general, extensions should not modify user preferences (without explicitly getting approval from the user). So, probably the most appropriate level where an extension can inject its custom behavior into the application is to add a subject hierarchy plugin that recognizes certain volume types where the default VR preset is not optimal (e.g., I can imagine that you can create better preset for dry bone), claims those volumes (gives higher confidence value than all other plugins), and uses your custom volume rendering preset when display in 3D view is requested.</p>
<p>If the problem is that in general you don’t find the default VR presets optimal then we can change those presets or add new presets that will be used as default.</p>

---
