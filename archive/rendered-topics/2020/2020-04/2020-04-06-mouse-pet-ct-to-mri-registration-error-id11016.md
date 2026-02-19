---
topic_id: 11016
title: "Mouse Pet Ct To Mri Registration Error"
date: 2020-04-06
url: https://discourse.slicer.org/t/11016
---

# Mouse PET/CT to MRI registration error

**Topic ID**: 11016
**Date**: 2020-04-06
**URL**: https://discourse.slicer.org/t/mouse-pet-ct-to-mri-registration-error/11016

---

## Post #1 by @Kate_Day (2020-04-06 16:47 UTC)

<p>I’m new to Slicer. I need to register an MRI with a PET/CT. The PET and CT register easily though they were taken by the same equipment at the same time. When I attempt to register the MRI with the CT it gives me an error. Ultimately I’d like to draw an ROI around a brain tumor on the MR and get a corresponding ROI on the PET. Sidenote: these are preclinical mouse images.</p>

---

## Post #2 by @lassoan (2020-04-06 18:27 UTC)

<p>How much the images are pre-aligned? It is especially important to have approximately matching orientation, as most registration methods cannot converge if the initial error is more that a few ten degrees. You can use landmark registration with 3-4 points for a quick initial alignment.</p>
<p>Which registration module have you tried to use? I would recommend SlicerElastix extension.</p>

---

## Post #3 by @Kate_Day (2020-04-20 14:04 UTC)

<p>Okay, Sorry for the slow response. I got sidetracked with some other work.</p>
<p>The images are cropped to a similar area and in the same orientation. I tried a bunch of different settings on the regular general reg. I get a “completed with errors” message the times it doesn’t fail completely. I downloaded the Elastix reg extension which you suggested and it also tells me “completed” but there is no change in the 3D view. The images are very clearly separated by a large distance.</p>
<p>I have not tried the landmark reg because I have no way to pinpoint the same exact areas in both sets of images.</p>

---

## Post #4 by @lassoan (2020-04-20 14:21 UTC)

<p>Can you share a sample data set (upload somewhere and post the link here)?</p>

---

## Post #5 by @Kate_Day (2020-04-20 14:50 UTC)

<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/jus4prc9iduy4c8/AADWWY7-YfHZ6YJI05B_o4N4a?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/jus4prc9iduy4c8/AADWWY7-YfHZ6YJI05B_o4N4a?dl=0" target="_blank" rel="nofollow noopener">Sample Data</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2020-04-20 16:23 UTC)

<p>I could make this work very nicely. All I had to do is to specify 3 landmarks that were visible in both the CT and MRI (two in the middle of the eye, one in the tube near the brain stem), register using Fiducial registration wizard (in SlicerIGT extension). After that BRAINS adjusted the registration very nicely, with default settings.</p>
<p>Initial CT and MR positions, displayed using Volume rendering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d905dcc0302b96e603ea45b319327483ac004f9.jpeg" data-download-href="/uploads/short-url/1VZvF5tL6ep0UqeLIx0Xx2AgWfL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d905dcc0302b96e603ea45b319327483ac004f9_2_690x441.jpeg" alt="image" data-base62-sha1="1VZvF5tL6ep0UqeLIx0Xx2AgWfL" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d905dcc0302b96e603ea45b319327483ac004f9_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d905dcc0302b96e603ea45b319327483ac004f9_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d905dcc0302b96e603ea45b319327483ac004f9_2_1380x882.jpeg 2x" data-dominant-color="77767B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 531 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>MRI landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d5645294c3d777d4cacd3914cdeeac5b6812806.jpeg" data-download-href="/uploads/short-url/b29B5s7XF5UBXGkqwkSzXEC5uWa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d5645294c3d777d4cacd3914cdeeac5b6812806_2_690x441.jpeg" alt="image" data-base62-sha1="b29B5s7XF5UBXGkqwkSzXEC5uWa" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d5645294c3d777d4cacd3914cdeeac5b6812806_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d5645294c3d777d4cacd3914cdeeac5b6812806_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d5645294c3d777d4cacd3914cdeeac5b6812806_2_1380x882.jpeg 2x" data-dominant-color="858388"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 553 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>CT landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d02eaf39589475a104a27745c32ed41e932c839.jpeg" data-download-href="/uploads/short-url/k7rzCWnJDqEYnU8AX1clylqVq6B.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02eaf39589475a104a27745c32ed41e932c839_2_690x441.jpeg" alt="image" data-base62-sha1="k7rzCWnJDqEYnU8AX1clylqVq6B" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02eaf39589475a104a27745c32ed41e932c839_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02eaf39589475a104a27745c32ed41e932c839_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d02eaf39589475a104a27745c32ed41e932c839_2_1380x882.jpeg 2x" data-dominant-color="8C898D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 669 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Fiducial registration:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d449f4b4e9305dc33b5f4d6ccbebc52ad5020fec.jpeg" data-download-href="/uploads/short-url/uhZFKTiWmDwFxtpmAANprkZS3oM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d449f4b4e9305dc33b5f4d6ccbebc52ad5020fec_2_690x441.jpeg" alt="image" data-base62-sha1="uhZFKTiWmDwFxtpmAANprkZS3oM" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d449f4b4e9305dc33b5f4d6ccbebc52ad5020fec_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d449f4b4e9305dc33b5f4d6ccbebc52ad5020fec_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d449f4b4e9305dc33b5f4d6ccbebc52ad5020fec_2_1380x882.jpeg 2x" data-dominant-color="8A888D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 646 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Apply and harden fiducial registration results to the MRI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5935143acbd79bc6d3dea81d0b468f8103393854.png" data-download-href="/uploads/short-url/cJadoSHUwjLixWvcXFpdz1xQNJq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5935143acbd79bc6d3dea81d0b468f8103393854_2_690x383.png" alt="image" data-base62-sha1="cJadoSHUwjLixWvcXFpdz1xQNJq" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5935143acbd79bc6d3dea81d0b468f8103393854_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5935143acbd79bc6d3dea81d0b468f8103393854_2_1035x574.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5935143acbd79bc6d3dea81d0b468f8103393854.png 2x" data-dominant-color="C0CCCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1108×616 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b17bfc8aee18eb3300c15a2108f34e119c33085a.png" data-download-href="/uploads/short-url/pk69qI005O4pxf0eUu50ORG30F4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b17bfc8aee18eb3300c15a2108f34e119c33085a_2_690x246.png" alt="image" data-base62-sha1="pk69qI005O4pxf0eUu50ORG30F4" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b17bfc8aee18eb3300c15a2108f34e119c33085a_2_690x246.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b17bfc8aee18eb3300c15a2108f34e119c33085a_2_1035x369.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b17bfc8aee18eb3300c15a2108f34e119c33085a.png 2x" data-dominant-color="D0E0CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×373 27.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result of fiducial registration and setup of BRAINS registration:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b5da2e5d58faf6d70c53d8e8603821202869701.jpeg" data-download-href="/uploads/short-url/6bD93G9s4xaP6MYHg9azxwlxU0p.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b5da2e5d58faf6d70c53d8e8603821202869701_2_690x441.jpeg" alt="image" data-base62-sha1="6bD93G9s4xaP6MYHg9azxwlxU0p" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b5da2e5d58faf6d70c53d8e8603821202869701_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b5da2e5d58faf6d70c53d8e8603821202869701_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b5da2e5d58faf6d70c53d8e8603821202869701_2_1380x882.jpeg 2x" data-dominant-color="8C8A8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 641 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
