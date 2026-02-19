---
topic_id: 25726
title: "Double Barrel Fibula Flap Mandible Reconstruction On Slicer"
date: 2022-10-16
url: https://discourse.slicer.org/t/25726
---

# Double-barrel fibula flap mandible reconstruction on Slicer

**Topic ID**: 25726
**Date**: 2022-10-16
**URL**: https://discourse.slicer.org/t/double-barrel-fibula-flap-mandible-reconstruction-on-slicer/25726

---

## Post #1 by @mau_igna_06 (2022-10-16 23:50 UTC)

<p>I see double-barrel (i.e. 2 levels) fibula flap mandible reconstruction support on Virtual Surgical Planning and Custom Fibula Surgical Guide Generation as the most "easy"and impactful change to <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#screenshots" rel="noopener nofollow ugc">BoneReconstructionPlanner</a> because currently only allows single level reconstruction (see the picture below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90f64150b2c8265d4e819c65d7e98f5b974cec75.png" data-download-href="/uploads/short-url/kGom0p1ONG8K0SW6L6IocfnGgAZ.png?dl=1" title="screenshotPlanning" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90f64150b2c8265d4e819c65d7e98f5b974cec75_2_651x500.png" alt="screenshotPlanning" data-base62-sha1="kGom0p1ONG8K0SW6L6IocfnGgAZ" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90f64150b2c8265d4e819c65d7e98f5b974cec75_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90f64150b2c8265d4e819c65d7e98f5b974cec75_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90f64150b2c8265d4e819c65d7e98f5b974cec75.png 2x" data-dominant-color="6B697C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshotPlanning</span><span class="informations">1280×983 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This weekend I tried to adapt the pipeline of BRP to support an optional second level, I didn’t achieve it yet.</p>
<p>Code-wise I can create another processing pipeline (duplicate a lot of code but make this feature less complex to develop)</p>
<p>Philosophically I wonder why support double-barrel only, why not triple-barrel or n-barrel (i.e. n-levels)?</p>
<p>Why not use some bone of the forearm or a rib instead of the fibula?</p>
<p>Does the intricate geometry of closing-wedges and opening-wedges that is complex to imagine put a stop to surgeons in the past that now can dream on new surgeries or treatments that Virtual Surgical Plans show are possible?</p>
<p><a class="mention" href="/u/manjula">@manjula</a>, <a class="mention" href="/u/seanchoi0519">@seanchoi0519</a> and any other doctors/dentists interested on mandible reconstruction, can you share your thoughts?</p>
<p>Technically, core-devs, do you have any advice regarding the development of the new feature?</p>

---

## Post #2 by @seanchoi0519 (2022-10-17 02:24 UTC)

<p>Hi Manjula,</p>
<p>What do you mean by double-barrel exactly, do you mean reconstruction planes in 2 different dimensions instead of a straight line (as such in fibula?)<br>
Always open to ideas, I will have a chat with my team once I understand more</p>

---

## Post #3 by @mau_igna_06 (2022-10-19 19:17 UTC)

<p>Hi <a class="mention" href="/u/seanchoi0519">@seanchoi0519</a>.</p>
<p>I mean doing what the picture below to the left shows (two levels of fibula replacing the resected mandible for easier dental implants insertion):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c781ff69d97fee812906d5ea533ebdd3568befb9.jpeg" data-download-href="/uploads/short-url/ssVxcb2uSGsfBRi1963jTBCBvux.jpeg?dl=1" title="Screenshot_20221015-154925_Moon+ Reader Pro" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c781ff69d97fee812906d5ea533ebdd3568befb9_2_690x310.jpeg" alt="Screenshot_20221015-154925_Moon+ Reader Pro" data-base62-sha1="ssVxcb2uSGsfBRi1963jTBCBvux" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c781ff69d97fee812906d5ea533ebdd3568befb9_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c781ff69d97fee812906d5ea533ebdd3568befb9_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c781ff69d97fee812906d5ea533ebdd3568befb9_2_1380x620.jpeg 2x" data-dominant-color="B7B7B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20221015-154925_Moon+ Reader Pro</span><span class="informations">1920×864 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @manjula (2022-10-22 14:22 UTC)

<p>Hi Mauro,</p>
<p>Sorry for late reply.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="25726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>why support double-barrel only, why not triple-barrel or n-barrel (i.e. n-levels)?</p>
</blockquote>
</aside>
<p>Yes it is possible to do triple barrel but i don’t have experience with it. Why surgeons do not play too much with many levels is that we are discussing about vascular tissue and the more complex it becomes the higher the chance of failure.</p>
<p>What we need to do is try to predict a in a way that the bone segments (1,2, n) can fold on to it self to give the desired shape</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="25726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>ome bone of the forearm or a rib instead of the fibula?</p>
</blockquote>
</aside>
<p>.<br>
I don’t know rib has been used as a vascular-free graft. part of the radial bone (forearm bone) is used with the radial forearm flap but not to form such complex defects. (it is not just the bone length there are main factors when it comes to the selection of a free flap starting from the pedicle, pedicle length, type of tissue etc.</p>
<p>There are other bones like iliac bone (DCIA flap) and scapula flap that can be used. But for them to use in double or triple barrel fashion the length is usually not enough plus when you use them generally there is no need to use a double barrel since you can get enough bone height. (We do the barrelling mainly to chive enough bone height for dental implants and prosthetic rehabilitation.</p>

---

## Post #5 by @mau_igna_06 (2022-10-22 17:57 UTC)

<p>Hi <a class="mention" href="/u/manjula">@manjula</a></p>
<p>I think I got it.</p>
<p>Here is a double-barrel VSP:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7156aa5331e25ae9a6c41637321af5afc76ac8f7.jpeg" data-download-href="/uploads/short-url/gaDDif4fJWN7D2WrMeOuzAiG2EL.jpeg?dl=1" title="DoubleBarrelScreenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7156aa5331e25ae9a6c41637321af5afc76ac8f7_2_685x500.jpeg" alt="DoubleBarrelScreenshot" data-base62-sha1="gaDDif4fJWN7D2WrMeOuzAiG2EL" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7156aa5331e25ae9a6c41637321af5afc76ac8f7_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7156aa5331e25ae9a6c41637321af5afc76ac8f7_2_1027x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7156aa5331e25ae9a6c41637321af5afc76ac8f7_2_1370x1000.jpeg 2x" data-dominant-color="7E7C9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DoubleBarrelScreenshot</span><span class="informations">1572×1146 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please tell me if the order of the fibula pieces assembled on the mandibular vacancy is okay (by looking at the corresponding colors)</p>
<p>The upper-level has it’s own planes, I turned off all mandible planes visualization to not crowd the view. The creation of the upper level planes it’s automatic although it needs much more work to be a really good automatic positioning.</p>
<p>The upper floor of the reconstruction is independent but optional, and there could be n floors, it may take me 1 or 2 more weekends to code it. But, do we really need it? I guess the highest impact would be polishing this feature, integrating it to the main branch without breaking what already works and then try to integrate the inmediate dental implant planning branch as it appears this is the state-of-the-art.</p>
<p>Here is the branch:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/DoubleBarrelV2">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/DoubleBarrelV2" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/DoubleBarrelV2" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner at DoubleBarrelV2</a></h3>

  <p><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/DoubleBarrelV2" target="_blank" rel="noopener nofollow ugc">DoubleBarrelV2</a></p>

  <p><span class="label1">3D Slicer module for planning mandible reconstruction surgery using fibula flap</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Feedback from users is welcomed</p>

---

## Post #6 by @seanchoi0519 (2022-10-23 11:45 UTC)

<p>Hello Maruo,</p>
<p>That’s a cool feature, though it seems like the consensus among my team of surgeons is that double barelling fibular reconstruction is only suitable for shorter mandibular defects. Also, it is not ideal to use a rib, ulna, or distal radius for ex. because of blood supply, and also because you can remove a fib and live a relatively normal life - whereas ulna or distal radius, your arm’s function would be severely limited. I think as we discussed though, scapula or iliac crest have much more potential with regards to this.</p>
<p>I think if we want to shoot for a bigger impact, we may be better off focusing on scapula or iliac application, what do you think? I will get back to you on what features we need to add to develop this, hopefully i can show some detailed animations for you.</p>
<p><a class="mention" href="/u/manjula">@manjula</a> would love to hear  your opinions on this as well</p>

---

## Post #7 by @lassoan (2023-03-21 02:19 UTC)



---
