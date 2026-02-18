# New Colorize Volume module

**Topic ID**: 32254
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/new-colorize-volume-module/32254

---

## Post #1 by @jaimigray (2023-10-16 15:15 UTC)

<p>Just added to 3D Slicer 5.5 is the new <strong>Colorize Volume</strong> module! I tried it on a fully segmented rattlesnake skull with really nice results comparable to the expensive proprietary software VGStudio Max. I played around with the Volume Rendering settings, as well as Lights module (from the SandBox extension), and cropping to an ROI in the Volume Rendering module to bisect and view the inside of the skull. I am still exploring the various functions of this module but I am excited to see what else I can do with it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda8f8234713a05d8d52ffa8b145d7bff0827a2f.jpeg" data-download-href="/uploads/short-url/r3OfVHieROIFQgQKGtvt1T9p8L5.jpeg?dl=1" title="rattlesnake-color-lights-bisect" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bda8f8234713a05d8d52ffa8b145d7bff0827a2f_2_690x381.jpeg" alt="rattlesnake-color-lights-bisect" data-base62-sha1="r3OfVHieROIFQgQKGtvt1T9p8L5" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bda8f8234713a05d8d52ffa8b145d7bff0827a2f_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bda8f8234713a05d8d52ffa8b145d7bff0827a2f_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bda8f8234713a05d8d52ffa8b145d7bff0827a2f_2_1380x762.jpeg 2x" data-dominant-color="302C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rattlesnake-color-lights-bisect</span><span class="informations">1506×832 52.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/039ac97dd8e946c82a47b3fdeb66a68427f5332a.jpeg" data-download-href="/uploads/short-url/vT3R4pNo2qLypKaIjc43SzMQvE.jpeg?dl=1" title="rattlesnake-color-lightsagain" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/039ac97dd8e946c82a47b3fdeb66a68427f5332a_2_690x381.jpeg" alt="rattlesnake-color-lightsagain" data-base62-sha1="vT3R4pNo2qLypKaIjc43SzMQvE" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/039ac97dd8e946c82a47b3fdeb66a68427f5332a_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/039ac97dd8e946c82a47b3fdeb66a68427f5332a_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/039ac97dd8e946c82a47b3fdeb66a68427f5332a_2_1380x762.jpeg 2x" data-dominant-color="3A302D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rattlesnake-color-lightsagain</span><span class="informations">1506×832 50.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc1cd8a1ce3878874c60f10011477b4f33f44e22.jpeg" data-download-href="/uploads/short-url/zYi7LCEjdcC1Z4hBB8VeRLugD7k.jpeg?dl=1" title="rattlesnake-color-difflight" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1cd8a1ce3878874c60f10011477b4f33f44e22_2_690x381.jpeg" alt="rattlesnake-color-difflight" data-base62-sha1="zYi7LCEjdcC1Z4hBB8VeRLugD7k" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1cd8a1ce3878874c60f10011477b4f33f44e22_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1cd8a1ce3878874c60f10011477b4f33f44e22_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1cd8a1ce3878874c60f10011477b4f33f44e22_2_1380x762.jpeg 2x" data-dominant-color="2C2523"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rattlesnake-color-difflight</span><span class="informations">1506×832 60.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bb6139f3e1c43f798de349073076fca5300cdcd.jpeg" data-download-href="/uploads/short-url/mdu6wVuYlgFKFoqhktSTVzBBgsZ.jpeg?dl=1" title="rattlesnake-color-opacity" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb6139f3e1c43f798de349073076fca5300cdcd_2_690x381.jpeg" alt="rattlesnake-color-opacity" data-base62-sha1="mdu6wVuYlgFKFoqhktSTVzBBgsZ" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb6139f3e1c43f798de349073076fca5300cdcd_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb6139f3e1c43f798de349073076fca5300cdcd_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb6139f3e1c43f798de349073076fca5300cdcd_2_1380x762.jpeg 2x" data-dominant-color="211C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rattlesnake-color-opacity</span><span class="informations">1506×832 40.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e678bdf6276dfe56694cbd29343bb9703a1d5bc4.jpeg" data-download-href="/uploads/short-url/wSQvqeBlgNWygytCuIv9UaIB53u.jpeg?dl=1" title="rattlesnake-color-lights" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e678bdf6276dfe56694cbd29343bb9703a1d5bc4_2_690x381.jpeg" alt="rattlesnake-color-lights" data-base62-sha1="wSQvqeBlgNWygytCuIv9UaIB53u" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e678bdf6276dfe56694cbd29343bb9703a1d5bc4_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e678bdf6276dfe56694cbd29343bb9703a1d5bc4_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e678bdf6276dfe56694cbd29343bb9703a1d5bc4_2_1380x762.jpeg 2x" data-dominant-color="342B29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rattlesnake-color-lights</span><span class="informations">1506×832 56.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2023-10-16 16:37 UTC)

<p><a class="mention" href="/u/jaimigray">@jaimigray</a> these are gorgeous. Hope biologists trying to migrate away from proprietary software will find these inspirational.</p>
<p>This is a very new feature not completely test, with other extension. perhaps you can find the time to try with the <code>Animator</code> module of SlicerMorph, and see if the cropping other features within the animator works well to make mp4s of these.</p>
<p>Thanks for sharing.</p>

---

## Post #3 by @jaimigray (2023-10-17 16:06 UTC)

<p>To continue this thread, I would like to show you more rattlesnake images, this time I used to Colorize volume module to render the skull inside the transparent skin<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d650ff08eb9fc46d32be5aa8848c2358339798f.jpeg" data-download-href="/uploads/short-url/kaPQACpUtzzgxqCdmMPV1jigIfZ.jpeg?dl=1" title="72544-skull-with-skin" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d650ff08eb9fc46d32be5aa8848c2358339798f_2_690x431.jpeg" alt="72544-skull-with-skin" data-base62-sha1="kaPQACpUtzzgxqCdmMPV1jigIfZ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d650ff08eb9fc46d32be5aa8848c2358339798f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d650ff08eb9fc46d32be5aa8848c2358339798f_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d650ff08eb9fc46d32be5aa8848c2358339798f_2_1380x862.jpeg 2x" data-dominant-color="15110F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">72544-skull-with-skin</span><span class="informations">1920×1202 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I tried without the skull segment, using the whole volume to render the skull instead. This gave me control over the skull colormap.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/992a55ed9daacfe0c7672a7756b738718d647978.jpeg" data-download-href="/uploads/short-url/lQXKUM6cMtAPLxaclcRLuqW6cFG.jpeg?dl=1" title="72544-skull-with-skin-volren" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/992a55ed9daacfe0c7672a7756b738718d647978_2_690x431.jpeg" alt="72544-skull-with-skin-volren" data-base62-sha1="lQXKUM6cMtAPLxaclcRLuqW6cFG" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/992a55ed9daacfe0c7672a7756b738718d647978_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/992a55ed9daacfe0c7672a7756b738718d647978_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/992a55ed9daacfe0c7672a7756b738718d647978_2_1380x862.jpeg 2x" data-dominant-color="1B1613"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">72544-skull-with-skin-volren</span><span class="informations">1920×1202 82.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then a density colormap for fun!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87746e5d62bfd825491c6ffb108542083ce6e15c.jpeg" data-download-href="/uploads/short-url/jkhUtXeNwqNyjq60bPl6mQphUmw.jpeg?dl=1" title="72544-skull-with-skin-colmap-redyellow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87746e5d62bfd825491c6ffb108542083ce6e15c_2_690x431.jpeg" alt="72544-skull-with-skin-colmap-redyellow" data-base62-sha1="jkhUtXeNwqNyjq60bPl6mQphUmw" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87746e5d62bfd825491c6ffb108542083ce6e15c_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87746e5d62bfd825491c6ffb108542083ce6e15c_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87746e5d62bfd825491c6ffb108542083ce6e15c_2_1380x862.jpeg 2x" data-dominant-color="211309"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">72544-skull-with-skin-colmap-redyellow</span><span class="informations">1920×1202 88.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2023-10-17 16:39 UTC)

<p>Thanks for sharing, really nice!<br>
(and kind of scary, too)</p>

---

## Post #5 by @pieper (2023-10-17 17:03 UTC)

<p>Perfect for Halloween!</p>

---

## Post #6 by @KSL (2024-01-18 06:24 UTC)

<p>It looks astonishing. Could you please tell me how you did? Do you first run the Total segmentator module and then the Colorize volume?</p>

---

## Post #7 by @muratmaga (2024-01-18 06:37 UTC)

<p>You need a segmentation to work with Colorize Volume. You can run TotalSegmentator on one of the sample CT datasets from Slicer to obtain a segmentaiton and play with the module.</p>
<p>There is also a very short tutorial with self-contained data, if you want to give it a try:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume" target="_blank" rel="noopener">//github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @KSL (2024-01-18 08:52 UTC)

<p>Thank you very much, Sir.</p>

---

## Post #9 by @Unicom (2025-08-10 14:12 UTC)

<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ColorizeVolume" target="_blank" rel="noopener nofollow ugc">Tutorials/ColorizeVolume at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>Hit CTRL+F (Module Finder shortcut) and search for , or from Module selector navigate to <strong>SlicerMorph-&gt;Input and Output-&gt;ImportFromURL</strong> .</p>
</blockquote>
<p>Now in the current latest version,</p>
<pre><code class="lang-auto">3D Slicer Version: 5.8.1
SlicerMorph Version: c944db9 (2025-06-26)
</code></pre>
<p>it has become:</p>
<blockquote>
<p>Hit CTRL+F (Module Finder shortcut) and search for , or from Module selector navigate to <strong>SlicerMorph-&gt;SlicerMorph hUtilities-&gt;ImportFromURL</strong> .</p>
</blockquote>
<p>The effect is excellent.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40f94d1e612539d4f58fee92af9cf7ae7b875278.png" data-download-href="/uploads/short-url/9gMGnC3hvbzN7cRUDOPfPcOHUxi.png?dl=1" title="2025-08-10_22-10-55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40f94d1e612539d4f58fee92af9cf7ae7b875278.png" alt="2025-08-10_22-10-55" data-base62-sha1="9gMGnC3hvbzN7cRUDOPfPcOHUxi" width="597" height="492"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-08-10_22-10-55</span><span class="informations">597×492 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Esteban_Barreiro (2026-01-06 01:29 UTC)

<p>Wow! Looks great!</p>
<p>I cant find this Module on 5.10.0… where did it go?</p>

---

## Post #11 by @jamesobutler (2026-01-06 01:48 UTC)

<p>The Colorize Volume module is still available in the Sandbox extension as described at:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/54727e8b7f1a8f85d8f07774c00b41ea28d37b8d/ColorizeVolume/README.md?plain=1#L1-L2">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/54727e8b7f1a8f85d8f07774c00b41ea28d37b8d/ColorizeVolume/README.md?plain=1#L1-L2" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/54727e8b7f1a8f85d8f07774c00b41ea28d37b8d/ColorizeVolume/README.md?plain=1#L1-L2" target="_blank" rel="noopener nofollow ugc">ColorizeVolume/README.md?plain=1</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/54727e8b7f1a8f85d8f07774c00b41ea28d37b8d/ColorizeVolume/README.md?plain=1#L1-L2" rel="noopener nofollow ugc"><code>54727e8b7</code></a>
</div>



    <pre class="onebox"><code class="lang-md?plain=1">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>## Colorize Volume</li>
          <li>ColorizeVolume is a module available through the `SandBox` extension. It allows you to turn a graycale scalar volume to an RGB volume (aka VectorVolume in Slicer) using its segmentation to map the colors. The resultant RGB volume then can be volume rendered, which provides much more detail compared to the surface rendering of the corresponding segmentation. </li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
