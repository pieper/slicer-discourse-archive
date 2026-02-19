---
topic_id: 45993
title: "Saving Parameter Preset In Ants Extension Changes Initializa"
date: 2026-01-29
url: https://discourse.slicer.org/t/45993
---

# Saving parameter preset in ANTs extension changes initialization value

**Topic ID**: 45993
**Date**: 2026-01-29
**URL**: https://discourse.slicer.org/t/saving-parameter-preset-in-ants-extension-changes-initialization-value/45993

---

## Post #1 by @sulli419 (2026-01-29 22:49 UTC)

<p>In the General ANTs 3D slicer extension I noticed something rather odd.  I can take one of the default parameter presets, say “QuickSyn”, change nothing, and click “save as preset”.  The new .json preset saves in the correct folder, but comparing this file with the original shows one key difference:  <span class="bbcode-u">The initializationfeature switches from 1 to -2</span> <span class="bbcode-u">(yes minus 2, not 2!)</span>.  See the line of code below.</p>
<p>Can anyone else recreate this?  My two volumes have in fact already been very crudely aligned, so I would actually like there to be no initial transform.  Is there a value for this, blank, or maybe just delete the command entirely from the .json file?</p>
<p>According to this website 0,1,2 do very different things.  I have no idea what the minus sign does, but maybe it errors and prevents there from being any initial registration whatsoever?<br>
<em>”An initial moving transform is used to quickly align the images before registration. The optimization process requires images to roughly overlap and will fail if images are too far apart in physical space.<br>
There are various options for the initialization:<br>
0-match by mid-point (i.e., center voxel of one image will be brought in line with center voxel of the other)<br>
1-match by center of mass<br>
2-match by point of origin (i.e. physical coordinates 0,0,0, as defined by the image headers) The center of mass alignment usually works well.”</em></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/ANTsX/ANTs/wiki/Anatomy-of-an-antsRegistration-call">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/ANTsX/ANTs/wiki/Anatomy-of-an-antsRegistration-call" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/f78e7c83f54bbec01079a9e4912938dc9729dfe12657f734806b90aeced9ffb1/ANTsX/ANTs" class="thumbnail" alt="" width="690" height="345"></div>

<h3><a href="https://github.com/ANTsX/ANTs/wiki/Anatomy-of-an-antsRegistration-call" target="_blank" rel="noopener nofollow ugc">Anatomy of an antsRegistration call</a></h3>

  <p>Advanced Normalization Tools (ANTs)  . Contribute to ANTsX/ANTs development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><strong>Original</strong><br>
},<br>
“initialTransformSettings”: {<br>
“initializationFeature”: 1<br>
}</p>
<p><strong>After saving (changed nothing in GUI</strong><br>
“initialTransformSettings”: {“initializationFeature”: -2}</p>

---

## Post #2 by @muratmaga (2026-01-30 03:22 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="1" data-topic="45993">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>so I would actually like there to be no initial transform. Is there a value for this, blank, or maybe just delete the command entirely from the .json file?</p>
</blockquote>
</aside>
<p>If you don’t need the initial transform, then just delete it. It is not a mandatory field to specify.</p>

---

## Post #3 by @sulli419 (2026-02-02 18:09 UTC)

<p>There are still cases where this initial transform feature might be useful for me, so I tried to see if the values change anything using a dummy comfiguration that should’t move my image other than the this initial transform, but it doesn’t seem to do anything.  Can anyone get this to work?</p>
<p>Also, still curious if anyone can reproduce this odd -2 initialization value writing during the preset save.</p>
<p>Thanks</p>

---

## Post #4 by @mikebind (2026-02-02 18:27 UTC)

<p>The meaning of the parameter values for -2 and -1 are:</p>
<ul>
<li>-2: use no initialization transform, i.e. assume that the images are already nearly aligned</li>
<li>-1: use the transform from a supplied transform node as the starting point for registration</li>
</ul>
<p>This does not appear to be documented anywhere, but I sorted this out by looking at the interface code and module code a while back.</p>
<p>It sounds like there is probably a bug in the code for saving or loading a preset, or possibly in the GUI update.  What happens for you if you:</p>
<ol>
<li>Load a preset like QuickSyN.</li>
<li>Change the initialization feature to something else and then change it back to what you want.</li>
<li>Save as a new preset</li>
</ol>
<p>I wonder if something in the loading code is failing to fully update the transform initialization setting upon load, and then interprets nothing being set as -2.</p>

---

## Post #5 by @sulli419 (2026-02-02 18:41 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="45993">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<ul>
<li>Load a preset like QuickSyN.</li>
<li>Change the initialization feature to something else and then change it back to what you want.</li>
<li>Save as a new preset</li>
</ul>
</blockquote>
</aside>
<p>Thanks.  As far as I can tell the intialization feature can only be changed in the .json file not the GUI, so how to attempt this?  Or maybe there is a field I’m missing in the GUI?  So far I’ve started with the QuickSyN intitialization 1 .json file, resaving writes it to -2.  If I create a new .json with any value (0,1,2) it doesn’t seem to move my image (similar to -2?).<br>
Cheers</p>

---

## Post #6 by @mikebind (2026-02-02 18:45 UTC)

<p>In the GUI, you set it here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cf4a27e87ccaa6c1a62e2a0283094e6e14a1abf.png" data-download-href="/uploads/short-url/aYMpKjsVqTIWG9RK8zgoNIMe0CX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cf4a27e87ccaa6c1a62e2a0283094e6e14a1abf_2_536x500.png" alt="image" data-base62-sha1="aYMpKjsVqTIWG9RK8zgoNIMe0CX" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cf4a27e87ccaa6c1a62e2a0283094e6e14a1abf_2_536x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cf4a27e87ccaa6c1a62e2a0283094e6e14a1abf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cf4a27e87ccaa6c1a62e2a0283094e6e14a1abf.png 2x" data-dominant-color="EFEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">704×656 38.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @sulli419 (2026-02-02 22:54 UTC)

<p>Oh funny.  I had been ignoring that menu because I thought it was only for loading in custom intial transform files.  If I change the values in the GUI it now has the expected consequeces on the registration.  Interestingly though, no matter how many times I change it, when I save it in the GUI it writes a .json with the value -2.  Maybe this is by design, maybe a bug?</p>
<p>But now that I understand the odd behavior, it seems like I can still get the full flexibility.  I just need to remember to always manually change the initial transform in the GUI, if I don’t want the default -2 “no tranform” setting.</p>
<p>Thanks for the help.</p>

---

## Post #8 by @sulli419 (2026-02-02 22:55 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="45993">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>The meaning of the parameter values for -2 and -1 are:</p>
<ul>
<li>-2: use no initialization transform, i.e. assume that the images are already nearly aligned</li>
<li>-1: use the transform from a supplied transform node as the starting point for registration</li>
</ul>
<p>This does not appear to be documented anywhere, but I sorted this out by looking at the interface code and module code a while back.</p>
<p>It sounds like there is probably a bug in the code for saving or loading a preset, or possibly in the GUI update.</p>
</blockquote>
</aside>
<p>*treating this part as the solution</p>

---

## Post #9 by @mikebind (2026-02-03 00:40 UTC)

<p>Yes, it feels like there is perhaps some confusion within the module about whether it conceptually considers the intitialization transform selection to be part of a preset or not.  It includes a section with the setting in a saved preset, but it sounds like it doesn’t properly save or reload it, instead treating it like a choice which is separate from the preset.  The “correct” transform initialization setting is mostly dependent on the choice of moving and fixed images, so I could certainly understand someone saying: “that’s not really part of the generic registration settings”.  However, I can also understand someone saying, “for my images, the right place to start is always to align the center of the imaged volume, why can’t I include that in my saved settings in my preset?”   The current module doesn’t seem to fully commit one way or the other.</p>

---
