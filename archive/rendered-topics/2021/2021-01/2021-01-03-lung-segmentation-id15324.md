# Lung segmentation

**Topic ID**: 15324
**Date**: 2021-01-03
**URL**: https://discourse.slicer.org/t/lung-segmentation/15324

---

## Post #1 by @sergiGB (2021-01-03 16:03 UTC)

<p>how can I know oxygen lung´s saturation ? first  I have to segment the lung but I dont know what to do after, thanks s much</p>

---

## Post #2 by @rbumm (2021-01-03 17:19 UTC)

<p>What exactly do you mean by “oxygen lung saturation”?</p>
<p>Slicer contains a “Chest Imaging Platform” with many lung-related tools. One way to analyze a CT scan would be:</p>
<p>(1)  create lung masks as shown here:</p><div class="youtube-onebox lazy-video-container" data-video-id="U9PUX-jLF0A" data-video-title="Easy creation of lung masks from lung CT in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=U9PUX-jLF0A" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/U9PUX-jLF0A/maxresdefault.jpg" title="Easy creation of lung masks from lung CT in 3D Slicer" width="" height="">
  </a>
</div>

<p>(2) then segment lung areas of interest (emphysema,inflated,infiltrated,collapsed) as shown here:</p><div class="youtube-onebox lazy-video-container" data-video-id="JcgMnDhlknM" data-video-title="Volumetric COVID-19 lung CT analysis with 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=JcgMnDhlknM" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/JcgMnDhlknM/maxresdefault.jpg" title="Volumetric COVID-19 lung CT analysis with 3D Slicer" width="" height="">
  </a>
</div>

<p>In a CT scan you would not see functional parameters like blood´s oxygen saturation.<br>
If this does not answer your question please describe a bit more with an example.</p>

---

## Post #3 by @sergiGB (2021-01-04 08:42 UTC)

<p>thank you so much .  Oxygen lung´s saturation= oxygen level that pass through lungs blood vessels (10mm^2 for example).<br>
Thanks again!</p>

---

## Post #4 by @rbumm (2021-01-04 08:51 UTC)

<p>The amount of oxygen passing through lung vessels can not be detected in a conventional lung CT. To measure oxygen update in test persons you would need to perform a spiroergometry, to measure lung perfusion you would need to involve scintigraphy.</p>

---

## Post #5 by @mauroccm (2021-01-12 19:57 UTC)

<p>Very nice extension. Thanks for sharing!</p>
<p>I have a problem with the segmentation of the trachea. Some voxels from the background are being segmented in some of the CTs I’m working on. Do you know how I can get around this problem?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee3612eb27b1958fdad01787454a505118053f9a.jpeg" alt="2021-01-12-Scene" data-base62-sha1="xZjuquZf14p85MoHumg7hvxghES" width="320" height="243"></p>
<p>Cheers,<br>
Mauro</p>

---

## Post #6 by @lassoan (2021-01-12 20:04 UTC)

<p>By “Trachea” we just mean “everything else” (not lungs). If there was a strong use case for actually extracting the trachea then we a fourth “other” segment could be added that would allow separating trachea from “everything else”. LungCTSegmenter module is a Python scripted, so you can go on and change the code (wherever you find “trachea” in the code, add a fourth option of “other” or “background”). If it works for you then you can send a pull request so that we can review and integrate your changes.</p>

---

## Post #7 by @rbumm (2021-01-13 13:12 UTC)

<p>Thanks for the comment, Mauro.<br>
I can not clearly see the problem in the image that you provided (too small), but I guess I know what you mean.<br>
The Lung CT Segmenter was mainly created for the purpose of providing a quick way to produce lung masks in CT.  We needed that to be able to further process areas of the CT within these masks. The surface of the lung masks is automatically smoothed, and airway/trachea segmentation is currently not always correct.</p>
<p>We will possibly deal with this in an update (a checkbox “Produce detailed airways” and additional code), in the meantime, you could try to segment the airways by using the “Grow From Seeds” effect in the “Segment Editor”.</p>

---

## Post #9 by @rbumm (2021-01-13 18:32 UTC)

<p>Produced a video today to show how I currently segment airways from a lung CT with Slicers´s “Grow from Seeds” function.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="9iiOBmaP8bA" data-video-title='Airway segmentation in 3D Slicer with "Grow from Seeds"' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=9iiOBmaP8bA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/9iiOBmaP8bA/maxresdefault.jpg" title='Airway segmentation in 3D Slicer with "Grow from Seeds"' width="" height="">
  </a>
</div>

<p>[sry for the double post]</p>

---

## Post #10 by @mauroccm (2021-01-13 19:42 UTC)

<p>Thank you very much for the tips! I’m new to 3DSlicer.</p>
<p>I’m not exactly trying to segment the airways at the moment. I was wondering how to improve the model because the ‘Lung CT segmenter’ extension prompts the user to click on a point to segment the trachea. However, in some images I am testing, over-segmentation occurs (many voxels are classified as false positives).</p>
<p>In the segmentation shown below, the left and right lungs (light yellow and light green, respectively) are acceptable. The region called ‘trachea’ (in light blue) contains voxels from the background.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b7cbeec549e5e885c1dc5a0386e293859c0d13.jpeg" data-download-href="/uploads/short-url/tVfzzuuziGSHegE7GMdxSgtR9rZ.jpeg?dl=1" title="SceneView_3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1b7cbeec549e5e885c1dc5a0386e293859c0d13_2_558x500.jpeg" alt="SceneView_3D" data-base62-sha1="tVfzzuuziGSHegE7GMdxSgtR9rZ" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1b7cbeec549e5e885c1dc5a0386e293859c0d13_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b7cbeec549e5e885c1dc5a0386e293859c0d13.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b7cbeec549e5e885c1dc5a0386e293859c0d13.jpeg 2x" data-dominant-color="9AAFCA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView_3D</span><span class="informations">707×633 31.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25b1aa8ade92432aa486f7c4ab08454fb8922d01.jpeg" data-download-href="/uploads/short-url/5nsjuJ1yzv2SBWrzNKnbBAEBI77.jpeg?dl=1" title="SceneView_axial" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25b1aa8ade92432aa486f7c4ab08454fb8922d01_2_558x500.jpeg" alt="SceneView_axial" data-base62-sha1="5nsjuJ1yzv2SBWrzNKnbBAEBI77" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25b1aa8ade92432aa486f7c4ab08454fb8922d01_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25b1aa8ade92432aa486f7c4ab08454fb8922d01.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25b1aa8ade92432aa486f7c4ab08454fb8922d01.jpeg 2x" data-dominant-color="595F5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView_axial</span><span class="informations">707×633 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I was wondering if it is possible to have some control over the growing region (stopping criterion or threshold)? I am assuming that segmentation occurs in a similar way to ‘Grow from Seeds’ tool.</p>

---

## Post #11 by @lassoan (2021-01-13 20:56 UTC)

<p>The segment that we call “trachea” now is really just a catch-all for all background structures that we want to exclude from the lung segmentation. Maybe we should just rename “trachea” to “other” to avoid any confusion.</p>

---

## Post #12 by @rbumm (2021-01-14 09:08 UTC)

<p>I renamed the output segments in the source and changed “trachea” to “others”.<br>
Is there anything else I need to push for getting the extension updated on the Slicer extension servers ?<br>
Thanks</p>

---

## Post #13 by @pieper (2021-01-14 19:29 UTC)

<p>No you should be all set.  Since you listed the master branch in your s4ext file it will automatically be used in the next extension build.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/LungCTAnalyzer.s4ext#L10" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/master/LungCTAnalyzer.s4ext#L10" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/master/LungCTAnalyzer.s4ext#L10</a></h4>
<pre class="onebox"><code class="lang-s4ext"><ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
<li>#</li><li># First token of each non-comment line is the keyword and the rest of the line</li><li># (including spaces) is the value.</li><li># - the value can be blank</li><li>#</li><li></li><li># This is source code manager (i.e. svn)</li><li>scm git</li><li>scmurl https://github.com/rbumm/SlicerLungCTAnalyzer</li><li class="selected">scmrevision master</li><li></li><li># list dependencies</li><li># - These should be names of other modules that have .s4ext files</li><li># - The dependencies will be built first</li><li>depends NA</li><li></li><li># Inner build directory (default is ".")</li><li>build_subdirectory .</li><li></li><li># homepage</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #14 by @Alice (2021-03-02 07:25 UTC)

<p>In the latest version, the airway segmentation module in CIP has disappeared.</p>

---

## Post #15 by @rbumm (2021-03-02 11:19 UTC)

<p>Hi,</p>
<p>I am not related to the airway segmentation module - but I can find it in 4.11.20200930  under Chest Imaging Platform → Toolkit → Segmentation → Segment Lung Airways</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3c2d9e6ab245fa68a2b1de256bc69840bd5756f.jpeg" data-download-href="/uploads/short-url/rVMzymNCBu7EDGW4M52Ms4G6gGj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3c2d9e6ab245fa68a2b1de256bc69840bd5756f_2_690x452.jpeg" alt="image" data-base62-sha1="rVMzymNCBu7EDGW4M52Ms4G6gGj" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3c2d9e6ab245fa68a2b1de256bc69840bd5756f_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3c2d9e6ab245fa68a2b1de256bc69840bd5756f_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3c2d9e6ab245fa68a2b1de256bc69840bd5756f.jpeg 2x" data-dominant-color="C2C6C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×715 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @sraina (2021-03-04 16:15 UTC)

<p>There is/was a module called “Airway Segmentation” too in CIP version (<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/AirwaySegmentation" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.10/Modules/AirwaySegmentation - Slicer Wiki</a>). The “Segment Lung Airways” has similar functionality so maybe one was removed for the sake of redundancy.</p>

---

## Post #17 by @ROBERTO_TONELLI (2023-04-17 10:48 UTC)

<p>Hi, it seems that in the latest version, the lung segmenter module in CIP has disappeared. Isn’t it?</p>

---

## Post #18 by @rbumm (2023-04-17 12:06 UTC)

<p>You can find the “Airway segmentation” tool in the"Chest Imaging Platform" extension, which you can load from the extension manager. Please note, that this tool has not been maintained for several years and is not always working well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b11ca058ccf31abe23f437dc1c99d3058cabd691.png" data-download-href="/uploads/short-url/pgNQk9r6sDJTFha5ZZb4YzE1Dod.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b11ca058ccf31abe23f437dc1c99d3058cabd691_2_690x410.png" alt="image" data-base62-sha1="pgNQk9r6sDJTFha5ZZb4YzE1Dod" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b11ca058ccf31abe23f437dc1c99d3058cabd691_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b11ca058ccf31abe23f437dc1c99d3058cabd691_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b11ca058ccf31abe23f437dc1c99d3058cabd691.png 2x" data-dominant-color="888A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1127×670 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @ROBERTO_TONELLI (2023-04-17 12:07 UTC)

<p>Thanks you for the reply!</p>

---

## Post #20 by @rbumm (2023-04-17 12:09 UTC)

<p>The Lung CT Segmenter module is installed automatically if you choose the Lung CT Analyzer extension. It features its own airway segmentation. Best airway segmentation results are obtained by using high-resolution CTs and a slice thickness of 1 mm. CT volumes generated with soft tissue kernels (Br36) work better than lung kernels (Bl57). If you need to fine-tune your airway segmentations, I would go directly into the 3D Slicer Segment Editor and issue the “Local Threshold” effect directly (that is what we do in Lung CT Segmenter).</p>

---

## Post #21 by @ROBERTO_TONELLI (2023-04-17 12:10 UTC)

<p>Yes, I got it right now.<br>
Sorry for the silly question <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Best,<br>
R</p>
<p>Roberto Tonelli, MD<br>
Laboratory of Experimental Pneumology<br>
<a href="http://www.experimentalpneumology.unimore.it/" rel="noopener nofollow ugc">http://www.experimentalpneumology.unimore.it/</a><br>
Respiratory Diseases Unit and Center for Rare Lung Disease<br>
Department of Surgical and Medical Sciences,<br>
University Hospital of Modena<br>
Via del Pozzo, 71 - 41125 Modena (Italy)<br>
PhD Course Clinical and Experimental Medicine (CEM)<br>
University of Modena &amp; Reggio Emilia<br>
Via Università 4 - 41121 Modena (Italy)<br>
E-mail: <a href="mailto:roberto.tonelli@me.com">roberto.tonelli@me.com</a><br>
Office e-mail: roberto.tonelli@unimore.it<br>
PEC: tonelli.roberto@pec.it<br>
Skype: roberto.tonelli150288</p>

---

## Post #22 by @ROBERTO_TONELLI (2023-04-22 10:11 UTC)

<p>I am experiencing troubles when try to launch AI lungmask in the CT Segmenter module.<br>
It reports the following note</p>
<p>Failed to compute results: [Errno 2] No such file or directory: ‘R231’</p>
<p>Any help?</p>

---

## Post #23 by @rbumm (2023-04-22 10:25 UTC)

<p>Could you provide some more information?<br>
On which operating system are you?<br>
Which Lung CT Analyzer version do you use?</p>
<p>I get a good result with R231 lungmask AI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ce6f62ba25ebbe1a93241a2787316eede837ab0.jpeg" data-download-href="/uploads/short-url/hOW2r1zR6RcygJuVeFO97ygSHba.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ce6f62ba25ebbe1a93241a2787316eede837ab0_2_690x442.jpeg" alt="image" data-base62-sha1="hOW2r1zR6RcygJuVeFO97ygSHba" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ce6f62ba25ebbe1a93241a2787316eede837ab0_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ce6f62ba25ebbe1a93241a2787316eede837ab0_2_1035x663.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ce6f62ba25ebbe1a93241a2787316eede837ab0.jpeg 2x" data-dominant-color="9C9C99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1203×772 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #24 by @ROBERTO_TONELLI (2023-04-22 14:56 UTC)

<p>Thank for the reply. I’m working on MacOS Monterey, the Lung CT analyzer version is 2.66. If I do the segmentation without AI it seems to work properly. When I add AI lung mask this is what I got<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1af4edf2bcc328338859efddb66b3f61bd086138.jpeg" data-download-href="/uploads/short-url/3QtaJUmV4y0dOfKBZwWd9qQFR7W.jpeg?dl=1" title="Schermata 2023-04-22 alle 16.48.49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1af4edf2bcc328338859efddb66b3f61bd086138_2_690x334.jpeg" alt="Schermata 2023-04-22 alle 16.48.49" data-base62-sha1="3QtaJUmV4y0dOfKBZwWd9qQFR7W" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1af4edf2bcc328338859efddb66b3f61bd086138_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1af4edf2bcc328338859efddb66b3f61bd086138_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1af4edf2bcc328338859efddb66b3f61bd086138_2_1380x668.jpeg 2x" data-dominant-color="BBBABF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermata 2023-04-22 alle 16.48.49</span><span class="informations">1920×930 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #25 by @rbumm (2023-04-22 17:26 UTC)

<p>For the lungmask AI segmentation you only need to select “Use AI” and “lungmask R231”, then press “Start” and wait approx. 2 minutes. No placement of additional markups.</p>

---
