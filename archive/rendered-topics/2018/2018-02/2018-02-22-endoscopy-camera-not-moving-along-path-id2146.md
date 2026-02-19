---
topic_id: 2146
title: "Endoscopy Camera Not Moving Along Path"
date: 2018-02-22
url: https://discourse.slicer.org/t/2146
---

# Endoscopy - camera not moving along path?

**Topic ID**: 2146
**Date**: 2018-02-22
**URL**: https://discourse.slicer.org/t/endoscopy-camera-not-moving-along-path/2146

---

## Post #1 by @hherhold (2018-02-22 15:34 UTC)

<p>OK, I’m pretty sure this is pilot error, but I’ve tried to do a fly through on a couple of datasets and I’m not sure what I’m doing wrong. To make a fly though, I am:</p>
<ol>
<li>Load example dataset (CTACardio)</li>
<li>Volume render</li>
<li>Pick preset to make it look snazzy</li>
<li>Place 3-4 fiducials to define path</li>
<li>Go to endoscopy module</li>
<li>Pick my fiducial list, leave camera as “Default scene camera” (pretty sure this is where I’m going wrong)</li>
<li>Hit “Create path”</li>
</ol>
<p>When I hit “Play” or drag through the frames, the camera view rotates and pans like it’s following the path, but the camera doesn’t travel along the path - it maintains its original viewpoint. Let me know if this isn’t clear and I can post a video. (I think.)</p>
<p>I did a quick look through the docs and tutorials on YouTube for a tutorial on the Endoscopy module - can someone point me in the right direction?</p>
<p>Many thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2018-02-22 15:56 UTC)

<p>Hmm, I tried those steps and things looked fine.  What version of Slicer and I assume you did this from a fresh start of Slicer?  You should see a curved line passing through your fiducials.  Yes, a movie might help troubleshoot.</p>

---

## Post #3 by @hherhold (2018-02-22 16:48 UTC)

<p>Yes, this is from a fresh start. I’m using a nightly from early January (4.9, probably Jan 3 or so). It’s possible I just don’t understand what the endoscopy view is supposed to look like - my understanding is that the camera view would follow the path defined by the fiducials (I do see the curved line). I’ve shared a screen capture in a Dropbox folder (link below). Let me know if you can’t play the video.</p>
<p>Any ideas?</p>
<p>Thanks!!!</p>
<p>-Hollister</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/lga76qoia59drin/AACbZ132VbGyuhyeTngEeqE2a?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/lga76qoia59drin/AACbZ132VbGyuhyeTngEeqE2a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/lga76qoia59drin/AACbZ132VbGyuhyeTngEeqE2a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - Error</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @hherhold (2018-02-22 17:10 UTC)

<p>Oh yeah, MacOS 10.12.6. Downloading more recent nightly now to try.</p>

---

## Post #5 by @hherhold (2018-02-22 17:37 UTC)

<p>Latest nightly does the same thing, as does 4.8.1. (GPU volume rendering on MacOS is kinda wonky on latest nightly, I think I already saw something about that come across a few days ago.)</p>
<p>It’s gotta be something I’m doing wrong.</p>

---

## Post #6 by @pieper (2018-02-22 18:20 UTC)

<p>Yes, the volume rendering back end has changed in the current nightlies and there could be a clipping plane problem or similar.</p>
<p>Maybe to narrow things down you could try turning off volume rendering and instead make a simple bone segmentation and confirm that the camera is behaving correctly.</p>

---

## Post #7 by @pieper (2018-02-22 18:21 UTC)

<p>On my local mac build of the trunk endoscopy is definitely working and looks good with CPU volume rendering but there are some artifacts with GPU.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbe3959717c2e1649322c767e9b01ab154128cb9.jpeg" data-download-href="/uploads/short-url/qO8SOJFOMinMjxmMbVmGWmujrWV.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbe3959717c2e1649322c767e9b01ab154128cb9_2_690x391.jpg" alt="image" data-base62-sha1="qO8SOJFOMinMjxmMbVmGWmujrWV" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbe3959717c2e1649322c767e9b01ab154128cb9_2_690x391.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbe3959717c2e1649322c767e9b01ab154128cb9_2_1035x586.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbe3959717c2e1649322c767e9b01ab154128cb9_2_1380x782.jpg 2x" data-dominant-color="A3A3A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1867×1060 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @hherhold (2018-02-22 20:21 UTC)

<p>I made a quick video of the steps I’m doing from startup to hitting “Play” and uploaded it to the dropbox link below (same as before), called “Pilot_error.mov”. Could you take a quick look at it and let me know what I’m doing wrong?</p>
<p>Thank you very much!</p>
<p>-Hollister</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/lga76qoia59drin/AACbZ132VbGyuhyeTngEeqE2a?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/lga76qoia59drin/AACbZ132VbGyuhyeTngEeqE2a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/lga76qoia59drin/AACbZ132VbGyuhyeTngEeqE2a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - Error</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2018-02-22 21:34 UTC)

<p>Works well for me, too. It may help if you reset the camera’s clipping range by zooming in/out of the 3D view after the animation is started.</p>

---

## Post #10 by @hherhold (2018-02-23 21:02 UTC)

<p>OK, I think I figured out my misunderstandings. First off, the scene I was trying to do a fly through of initially (before going to CTACardio to just figure out how it worked) wound up with like 5 Default Cameras, so I have no idea which one was actually being acted on.</p>
<p>Zooming in and out to reset the clipping range was extremely useful - thank you very much for that tip.</p>
<p>Thanks Steve and Andras for your responses - very helpful, as always!</p>
<p>-Hollister</p>

---
