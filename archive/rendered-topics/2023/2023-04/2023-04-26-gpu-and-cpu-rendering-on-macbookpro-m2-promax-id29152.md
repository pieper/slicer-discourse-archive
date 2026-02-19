---
topic_id: 29152
title: "Gpu And Cpu Rendering On Macbookpro M2 Promax"
date: 2023-04-26
url: https://discourse.slicer.org/t/29152
---

# GPU and CPU rendering on MacBookPro M2 ProMax

**Topic ID**: 29152
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/gpu-and-cpu-rendering-on-macbookpro-m2-promax/29152

---

## Post #1 by @Adam_Summers (2023-04-26 20:58 UTC)

<p>I have the latest Apple MacBook with Apple silicon, 96GB of RAM running Ventura. I am using the most recent build of Slicer for Mac from 2023-4-25. My fairly large data sets are rendering well, though slowly, using the CPU, but when I swap to GPU the volume is a uniform prism of color. Here is an example data set of a clingfish.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1QuvrOBHKEmS8R2eTxm63hN5pN1qB7I5N/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1QuvrOBHKEmS8R2eTxm63hN5pN1qB7I5N/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1QuvrOBHKEmS8R2eTxm63hN5pN1qB7I5N/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1QuvrOBHKEmS8R2eTxm63hN5pN1qB7I5N/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Clinger_genC_sp3#2_6.0um_2k female.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I expect the answer is that Apple silicon is just not working well with Slicer, but if someone has a workaround it would be great.</p>

---

## Post #2 by @muratmaga (2023-04-26 21:07 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> this the screenshot <a class="mention" href="/u/adam_summers">@Adam_Summers</a> sent me earlier, if it helps…</p>
<p>CPU rendering<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b72636af7d9620a021352b4b78c35aa6506d3d7.png" alt="image" data-base62-sha1="aLqSWx9PkULbsVcwhraLQ0JVsVh" width="640" height="153"></p>
<p>GPU rendering.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efde0c17e82c73debb3cb04374920ed98b564f72.png" alt="image" data-base62-sha1="ydXQFiNje4vLYeSZft9Tym6u9DI" width="640" height="167"></p>

---

## Post #3 by @pieper (2023-04-27 14:43 UTC)

<p>Thanks for sharing the data.  I could use GPU rendering on a mac pro, but on a mac book air m2 I got this error:</p>
<pre><code class="lang-auto">[VTK] Invalid texture dimensions [447, 318, 2308]

[FD] UNSUPPORTED (log once): POSSIBLE ISSUE: unit 1 GLD_TEXTURE_INDEX_3D is unloadable and bound to sampler type (Float) - using zero texture because texture unloadable
</code></pre>
<p>so it must be a hardware or driver limit, probably to 2048 max dimension</p>
<p>I used CropVolume with a 1.5x multiplier on the spacing and then GPU rendering worked on the m2 machine:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98c5caf030a045e663f25fe532aa24ddfe3cce7.jpeg" alt="image" data-base62-sha1="qtr3uwFPE78T5h4On65tyKmZs35" width="680" height="492"></p>

---

## Post #4 by @Adam_Summers (2023-04-27 15:20 UTC)

<p>Dear Steve, thanks so much for identifying the issue. You have given me a path to a work around. I really appreciate it.</p>
<p>-Adam</p>

---

## Post #5 by @muratmaga (2023-04-27 16:19 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="29152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>so it must be a hardware or driver limit, probably to 2048 max dimension</p>
</blockquote>
</aside>
<p>This is an unfortunate limitation, particularly if this is true for the top of the line M2 macbook pro <a class="mention" href="/u/fishguy">@Fishguy</a> has. I don’t have this problem on my 2018 intel macbook pro.</p>
<p>Do you know if there is a way to report this to apple? I am concerned because a lot of biology folks use Slicer on Mac, and that’s a limitation we can’t do much.</p>

---

## Post #6 by @Adam_Summers (2023-04-27 16:33 UTC)

<p>Just to follow up. Steve has found the issue. More than 2048 slices and the GPU won’t work. I have tested this with 5 data sets that were not working, and by cutting down the number of slices they work just fine. The InputStack module in SlicerMorph (which I think Steve wrote) has a ‘Skip Slices’ option that allows you to tune the total slices in the Z direction. That is a work around until Apple gets itself in order on this.</p>
<p>Thanks a lot.</p>
<p>Adam</p>

---

## Post #7 by @pieper (2023-04-27 16:53 UTC)

<p>From what I can tell this is a hardware limit on Apple GPUs.  This document says that all the apple GPUs, including the “Metal 3” in the M2 have a max size of 2048 in all dimensions.  It’s hard to know if they will relax this in the future.  For. now I’m afraid downsampling is the best option.</p>
<p><a class="mention" href="/u/adam_summers">@Adam_Summers</a> if skipping slices give you okay image quality then that’s a good workaround.  Using CropVolume to downsample a larger volume will be less lossy, but more time consuming of course.</p>
<aside class="onebox pdf" data-onebox-src="https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf">
  <header class="source">

      <a href="https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf" target="_blank" rel="noopener">developer.apple.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf" target="_blank" rel="noopener">Metal-Feature-Set-Tables.pdf</a></h3>

  <p class="filesize">2.80 MB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a254d0583e36c1838ba1fe5a05e29c859e8529.png" data-download-href="/uploads/short-url/7Et697W1ykbnqn5BIngFhcKJipr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35a254d0583e36c1838ba1fe5a05e29c859e8529_2_690x394.png" alt="image" data-base62-sha1="7Et697W1ykbnqn5BIngFhcKJipr" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35a254d0583e36c1838ba1fe5a05e29c859e8529_2_690x394.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a254d0583e36c1838ba1fe5a05e29c859e8529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a254d0583e36c1838ba1fe5a05e29c859e8529.png 2x" data-dominant-color="CDD6E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1018×582 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @jcfr (2025-05-20 00:50 UTC)

<p>As a follow-up, this is being addressed by <a class="mention" href="/u/lassoan">@lassoan</a> through <a href="https://github.com/Slicer/Slicer/pull/8430">PR-8430</a>:</p>
<blockquote>
<p>On macOS graphics hardware, maximum 3D texture size (along any axis) is typically 2048. This commit sets volume partitioning partitioned to not exceed this size by default.</p>
<p>On other systems volume is maximum size is set to 4096 by default, which will not split up the volume in most cases (which was the behavior before this commit).</p>
</blockquote>

---
