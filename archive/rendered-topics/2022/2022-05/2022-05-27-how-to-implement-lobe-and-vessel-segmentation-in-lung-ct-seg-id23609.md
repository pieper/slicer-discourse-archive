# How to implement lobe and vessel segmentation in Lung CT Segmenter?

**Topic ID**: 23609
**Date**: 2022-05-27
**URL**: https://discourse.slicer.org/t/how-to-implement-lobe-and-vessel-segmentation-in-lung-ct-segmenter/23609

---

## Post #1 by @rbumm (2022-05-27 13:41 UTC)

<p><a class="mention" href="/u/eserval">@Eserval</a> and <a class="mention" href="/u/rbumm">@rbumm</a>, both thoracic surgeons, have been in a video call recently to address the above question.</p>
<p><a class="mention" href="/u/eserval">@Eserval</a> demonstrated his excellent segmentation recipe (100% 3D Slicer)  which consists of:</p>
<ul>
<li>Lung mask and airway segmentation with Lung CT Segmenter</li>
<li>Creating a vessel mask</li>
<li>Creation of empty a PV and PA segment</li>
<li>Manual placement of seeds in the pulmonary vein and pulmonary artery (complicated stuff)</li>
<li>Grow from seeds vessel segmentation “inside vessel mask”</li>
<li>Creation of upper, middle and lower lobe segments (left) and upper and lower lobe (right)</li>
<li>Slice painting inside right or left lung mask in the lobe segments</li>
<li>Fill between slices to complete the lobes</li>
<li>Duplicate the lobes into lung segments</li>
<li>Use the “Scissor” function to isolate each individual lung segment</li>
<li>Use “Level tracing” to segment the tumor</li>
</ul>
<p>The procedure usually takes <a class="mention" href="/u/eserval">@Eserval</a> about 1-2 hours. <a class="mention" href="/u/eserval">@Eserval</a> if possible please add some cooking stage images and a final result - or a link to a youtube video …</p>
<p><a class="mention" href="/u/eserval">@Eserval</a> and <a class="mention" href="/u/rbumm">@rbumm</a> agreed on closer cooperation, moving parts of this recipe into the lung CT segmenter, and establishing this thread to collect additional ideas from the community. The final goal will be a semiautomatic planning tool for lung surgery, maybe an additional module in the Chest Imaging Platform.</p>

---

## Post #2 by @mau_igna_06 (2022-05-27 15:51 UTC)

<p>Great. I’m eager to see some pictures</p>

---

## Post #3 by @Eserval (2022-05-27 22:59 UTC)

<p>Hello everyone,</p>
<p>Thanks Rudolf for the post. I`ll post the materila ASAP.</p>
<p>best</p>

---

## Post #4 by @rbumm (2022-05-28 08:01 UTC)

<p>Great, it would probably best to get details included in 3D Slicer recipes:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://lassoan.github.io/SlicerSegmentationRecipes/">
  <header class="source">

      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/" target="_blank" rel="noopener">3D Slicer segmentation recipes</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/" target="_blank" rel="noopener">Segmentation recipes for 3D Slicer</a></h3>

  <p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
and post one result image here in this thread.</p>

---

## Post #5 by @Eserval (2022-05-28 15:35 UTC)

<p>Here is the final product of the segmentation. We use it in our institution to plan lung resections.<br>
That case was an S6 segmentectomy where the 3D reconstruction helped manage an anomalous vein for the S2 segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1213548615a084f2d409a58b8aae600a4692b3b2.jpeg" data-download-href="/uploads/short-url/2zU0zf50ZiB759jhU98BF0WIsds.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1213548615a084f2d409a58b8aae600a4692b3b2_2_360x499.jpeg" alt="image" data-base62-sha1="2zU0zf50ZiB759jhU98BF0WIsds" width="360" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1213548615a084f2d409a58b8aae600a4692b3b2_2_360x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1213548615a084f2d409a58b8aae600a4692b3b2_2_540x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1213548615a084f2d409a58b8aae600a4692b3b2_2_720x998.jpeg 2x" data-dominant-color="E7E2E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1042×1445 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02f90d4c312f41ebad62a32290122f66335b4809.jpeg" data-download-href="/uploads/short-url/qixRRmCrMF2XUEnRLWus1UpkFP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02f90d4c312f41ebad62a32290122f66335b4809_2_350x500.jpeg" alt="image" data-base62-sha1="qixRRmCrMF2XUEnRLWus1UpkFP" width="350" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02f90d4c312f41ebad62a32290122f66335b4809_2_350x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02f90d4c312f41ebad62a32290122f66335b4809_2_525x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02f90d4c312f41ebad62a32290122f66335b4809_2_700x1000.jpeg 2x" data-dominant-color="ECE7E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×1374 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6ddb25c36659a5277f1eb3d21605122658039a25.jpeg" data-download-href="/uploads/short-url/fFPz4oypDrNxT33CB1L4v5pwCR7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ddb25c36659a5277f1eb3d21605122658039a25_2_376x500.jpeg" alt="image" data-base62-sha1="fFPz4oypDrNxT33CB1L4v5pwCR7" width="376" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ddb25c36659a5277f1eb3d21605122658039a25_2_376x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ddb25c36659a5277f1eb3d21605122658039a25_2_564x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ddb25c36659a5277f1eb3d21605122658039a25_2_752x1000.jpeg 2x" data-dominant-color="C3AA9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1323×1755 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60ea05da836be3e29b256bcd08573b1a93d8bc74.jpeg" data-download-href="/uploads/short-url/dPlebEZr5jYg51a9zF57MjigHRO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ea05da836be3e29b256bcd08573b1a93d8bc74_2_346x500.jpeg" alt="image" data-base62-sha1="dPlebEZr5jYg51a9zF57MjigHRO" width="346" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ea05da836be3e29b256bcd08573b1a93d8bc74_2_346x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ea05da836be3e29b256bcd08573b1a93d8bc74_2_519x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ea05da836be3e29b256bcd08573b1a93d8bc74_2_692x1000.jpeg 2x" data-dominant-color="D6C4BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">925×1335 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We have an almost done video publication that includes an explanation of the steps. I’ll post on the Segmentation Recipes ASAP.</p>
<p>Best</p>

---

## Post #6 by @Tibor_Krajc (2022-09-17 21:49 UTC)

<p>1-2 hours sounds great! I usually need 4-8hrs but with loads of manual structure coloring with a digitizer pen. were you able to post your workflow to Recipes? could you point us to a link? thanks a lot!</p>

---
