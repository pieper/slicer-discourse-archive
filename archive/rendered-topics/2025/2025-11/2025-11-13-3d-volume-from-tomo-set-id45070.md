---
topic_id: 45070
title: "3D Volume From Tomo Set"
date: 2025-11-13
url: https://discourse.slicer.org/t/45070
---

# 3D volume from Tomo Set

**Topic ID**: 45070
**Date**: 2025-11-13
**URL**: https://discourse.slicer.org/t/3d-volume-from-tomo-set/45070

---

## Post #1 by @jmac (2025-11-13 19:45 UTC)

<p>New to slicer via recommendation from colleague.  Very nice tool.</p>
<p>Trying to see a 3D volume of mouse from a tomosynthesis dataset (height stack of 24 slices). I know its not going to be a perfect 3D dataset but just want to see it anyway.</p>
<p>I can see the 3 independant views but not the 3D volume view.</p>
<p>Can someone help figure out why it is not loading.</p>
<p>I uploaded dataset here</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://limewire.com/d/Bd3N4?lmwr-ftv=1">
  <header class="source">
      <img src="https://limewire.com/favicon-32x32.ico" class="site-icon" alt="" width="256" height="256">

      <a href="https://limewire.com/d/Bd3N4?lmwr-ftv=1" target="_blank" rel="noopener nofollow ugc">LimeWire</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://limewire.com/img/remix/twitter_card_image_file_sharing.png" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://limewire.com/d/Bd3N4?lmwr-ftv=1" target="_blank" rel="noopener nofollow ugc">Download mouse.zip | LimeWire</a></h3>

  <p>Download mouse.zip on LimeWire</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>here is a screen shot. I would assume the volume would show up on the box in the top right corner.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c841b0dfa17beefb61312e082eae8251f1b7c8.png" data-download-href="/uploads/short-url/iw6DLRZHNymJcLA0nGrhrgCwW12.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c841b0dfa17beefb61312e082eae8251f1b7c8_2_690x409.png" alt="image" data-base62-sha1="iw6DLRZHNymJcLA0nGrhrgCwW12" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c841b0dfa17beefb61312e082eae8251f1b7c8_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c841b0dfa17beefb61312e082eae8251f1b7c8_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c841b0dfa17beefb61312e082eae8251f1b7c8_2_1380x818.png 2x" data-dominant-color="7A797F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1138 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-11-13 19:47 UTC)

<p>You can try RTK: <a href="https://www.openrtk.org/">https://www.openrtk.org/</a></p>

---

## Post #3 by @lassoan (2025-11-13 19:53 UTC)

<p>If it is a “height stack” then you can display it in 3D using volume rendering (go to Data module and drag-and-drop the image to the 3D view). You can find more information on basic visualization options in the <a href="https://training.slicer.org/#STC-VIS-102">STC-VIS-102 visualization tutorial</a>.</p>
<p>If you have a sinogram (projection from different directions) then you need to reconstruct it first into a Cartesian image as <a class="mention" href="/u/pieper">@pieper</a> described above. I could not check what kind of images you have because the link did not work for me (limewire reported “Incomplete or wrong Download URL.”).</p>

---

## Post #4 by @muratmaga (2025-11-14 02:53 UTC)

<aside class="quote no-group" data-username="jmac" data-post="1" data-topic="45070">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/258eb7/48.png" class="avatar"> jmac:</div>
<blockquote>
<p>I can see the 3 independant views but not the 3D volume view.</p>
</blockquote>
</aside>
<p>Go to data module, and than drag the <code>mini_mini</code> object onto the 3D viewer. It will render but it will be pretty bad. You have two orders of magnitude difference in the resolution between your XY and Z planes.</p>

---

## Post #5 by @jmac (2025-12-10 20:35 UTC)

<p>hi Andras.   I am trying to reference the link STC-VIS 102 but keep getting error messages</p>

---

## Post #6 by @jmac (2025-12-10 20:55 UTC)

<p>sometimes  good enough is all the application needs and that is the goal here</p>
<p>bigger challenge is limited angular range too but just need to get some detail but not going for perfect.</p>
<p>I believe we just have to scale it in slicer → volume→ volume information tab:     0.048,0.048,1</p>
<p>Question.. I cant seem to figure out how to drag “minimini” object into the 3D volume</p>
<p>is this correct  ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/347e4fb98d50c35d28a5b7d78ab65e9ef2aaaa91.png" data-download-href="/uploads/short-url/7unrREX6hp6W4vK5MxtPXHNXw41.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347e4fb98d50c35d28a5b7d78ab65e9ef2aaaa91_2_690x265.png" alt="image" data-base62-sha1="7unrREX6hp6W4vK5MxtPXHNXw41" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347e4fb98d50c35d28a5b7d78ab65e9ef2aaaa91_2_690x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347e4fb98d50c35d28a5b7d78ab65e9ef2aaaa91_2_1035x397.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347e4fb98d50c35d28a5b7d78ab65e9ef2aaaa91_2_1380x530.png 2x" data-dominant-color="75777A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1547×596 54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>this in in matlab, its all i need but the 3D is crashing unless i upgrade matlab again and really hoping for someting more powerful anyway</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b027a15b6a9b38892dea29b3ec67d39e9568194.png" data-download-href="/uploads/short-url/hyc2cN5l4dxMk4jl5V5PrT0qqQ4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b027a15b6a9b38892dea29b3ec67d39e9568194_2_690x402.png" alt="image" data-base62-sha1="hyc2cN5l4dxMk4jl5V5PrT0qqQ4" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b027a15b6a9b38892dea29b3ec67d39e9568194_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b027a15b6a9b38892dea29b3ec67d39e9568194_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b027a15b6a9b38892dea29b3ec67d39e9568194_2_1380x804.png 2x" data-dominant-color="818385"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1500×876 84.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2025-12-10 21:08 UTC)

<aside class="quote no-group" data-username="jmac" data-post="6" data-topic="45070">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/258eb7/48.png" class="avatar"> jmac:</div>
<blockquote>
<p>is this correct ?</p>
</blockquote>
</aside>
<p>Yes, but you need to center the field of view (+ sign in the top bar) in the 3d view and probably zoom in a bit. See this for explanation of things in the 3D view:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" target="_blank" rel="noopener nofollow ugc">Ctrl - User Interface — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @lassoan (2025-12-10 21:29 UTC)

<aside class="quote no-group" data-username="jmac" data-post="5" data-topic="45070">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/258eb7/48.png" class="avatar"> jmac:</div>
<blockquote>
<p>I am trying to reference the link STC-VIS 102 but keep getting error messages</p>
</blockquote>
</aside>
<p>What error messages are you getting? Where?</p>
<p>The link to download the slides or access the website work well for me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd75d7acbb4b6c1d80e27696a591c1f43401be9.jpeg" data-download-href="/uploads/short-url/keMJWAUHZbDroUrUVpNwmqLCWNz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd75d7acbb4b6c1d80e27696a591c1f43401be9_2_690x443.jpeg" alt="image" data-base62-sha1="keMJWAUHZbDroUrUVpNwmqLCWNz" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd75d7acbb4b6c1d80e27696a591c1f43401be9_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd75d7acbb4b6c1d80e27696a591c1f43401be9_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd75d7acbb4b6c1d80e27696a591c1f43401be9_2_1380x886.jpeg 2x" data-dominant-color="DBDEE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1235 396 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @jmac (2025-12-11 17:45 UTC)

<p>Sorry, Im not sure what i clicked, it might have been the STC-VIS-101 or otherwise 102</p>
<p>The 102 is working when i just clinked on it, but if i click on 101 (PDF English) I get the error shown below  (atleats now).  Maybe that was the one I clicked?</p>
<p>note i figured it was a better place to start out</p>
<p>I do appreciate the literature you have made and am thankful to use it it</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b57e4170a8293634066688592437dd5d3d76b9.png" data-download-href="/uploads/short-url/wcIhfqWkyZFhwELP4qWRk8xDcSt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b57e4170a8293634066688592437dd5d3d76b9_2_690x432.png" alt="image" data-base62-sha1="wcIhfqWkyZFhwELP4qWRk8xDcSt" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b57e4170a8293634066688592437dd5d3d76b9_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b57e4170a8293634066688592437dd5d3d76b9_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b57e4170a8293634066688592437dd5d3d76b9_2_1380x864.png 2x" data-dominant-color="EEEEEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1908×1195 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @jmac (2025-12-11 18:21 UTC)

<p>does anyone have a CT dataset I can use to try to learn to use slicer with?   I think doing something with tomo is not ideal and really need to see normal behavior with a CT dataset first.</p>
<p>for the tomo, we are trying to just get data that is good enough to decide basic properties such as delineation of boundaries of the skin in the height axis, not trying to complete with MRI or CT</p>

---

## Post #11 by @pieper (2025-12-11 18:31 UTC)

<p>There are several CT datasets in the SampleData module.</p>
<p>From the pictures you shared it looks like you may not have reconstructed the volume on your scanner.  Slicer doesn’t work with the raw projection images.  As I mentioned above you may be able to use rtk, but using the scanner itself is usually easiest and best.</p>

---

## Post #12 by @jmac (2025-12-11 18:38 UTC)

<p>thank you I will look at RTK</p>
<p>However, this is the reconstructed dataset and you can sort through the height stack to see it is properly made. Otherwise you would see angular effects from each projection.</p>

---

## Post #13 by @jmac (2025-12-11 18:41 UTC)

<p>this is the dataset, reuploaded</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://limewire.com/d/HAxId?lmwr-ftv=1">
  <header class="source">
      <img src="https://limewire.com/favicon-32x32.ico" class="site-icon" alt="" width="256" height="256">

      <a href="https://limewire.com/d/HAxId?lmwr-ftv=1" target="_blank" rel="noopener nofollow ugc">LimeWire</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://limewire.com/img/remix/twitter_card_image_file_sharing.png" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://limewire.com/d/HAxId?lmwr-ftv=1" target="_blank" rel="noopener nofollow ugc">Download mouse | LimeWire</a></h3>

  <p>Download mouse on LimeWire</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #14 by @pieper (2025-12-11 20:30 UTC)

<p>Okay, I see, it’s just a little slab.  These aren’t valid dicom, so I loaded them as an image stack and changed the spacing to be isotropic (made the slice spacing 0.048.  You just don’t have the full specimen in the scan.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe7cf3276777c5c8277ea7cdcfb69eaea9a90a0.jpeg" data-download-href="/uploads/short-url/kx2Vvu4nKoDbP3nzeE32RLjn476.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7cf3276777c5c8277ea7cdcfb69eaea9a90a0_2_690x482.jpeg" alt="image" data-base62-sha1="kx2Vvu4nKoDbP3nzeE32RLjn476" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7cf3276777c5c8277ea7cdcfb69eaea9a90a0_2_690x482.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7cf3276777c5c8277ea7cdcfb69eaea9a90a0_2_1035x723.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7cf3276777c5c8277ea7cdcfb69eaea9a90a0_2_1380x964.jpeg 2x" data-dominant-color="6A6A6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1342 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
