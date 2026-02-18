# Reducing opacity of individual sections of a 3D model

**Topic ID**: 16840
**Date**: 2021-03-30
**URL**: https://discourse.slicer.org/t/reducing-opacity-of-individual-sections-of-a-3d-model/16840

---

## Post #1 by @Pseudoceros (2021-03-30 04:25 UTC)

<p>Hi all,</p>
<p>I managed to create a 3D reconstruction out of 2D histology slices but I’m having trouble with transparency. Basically, the organs that I want to visualised are “inside” the 3D object, meaning that there are slices on the foreground that are blocking them from view (since the slices are opaque images). Is there are a way to adjust the transparency of the slices so that the sections at the front are less opaque, and the sections where the organs appear overlap with each other creating a shape/outline? I have kind of managed to make it work by playing with the opacity slider in the volume rendering module but it creates blurry/incomplete results.</p>
<p>In case it helps, what I’ve done is align the individual slices with TrakEM2, then load those as a single object on 3Dslicer, make a scalar volume and then use the volume rendering module (basically followed the video tutorial on youtube). The presets on the volume rendering are all related to human body parts so those don’t work for me (I’m using sections from a worm).</p>
<p>Thank you in advance.</p>

---

## Post #2 by @muratmaga (2021-03-30 05:04 UTC)

<aside class="quote no-group" data-username="Pseudoceros" data-post="1" data-topic="16840">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/919ad9/48.png" class="avatar"> Pseudoceros:</div>
<blockquote>
<p>Is there are a way to adjust the transparency of the slices so that the sections at the front are less opaque, and the sections where the organs appear overlap with each other creating a shape/outline?</p>
</blockquote>
</aside>
<p>If you obtain the intensity values of the region you are trying to hide, you should be able to set up a scalar opacity map that will essentially mask these regions. (See the documentation of VOlume Rendering module here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="inline-onebox">Volume rendering — 3D Slicer documentation</a>)</p>
<p>However, if those intensity values are also similar to the structure you want to visualize inside, then this won’t work. In that case, you may have to segment those regions…</p>
<p>Eg, this is the sample data from Slicer (CTBrain.nrrd), where the default volume rendering map shows a solid cylinder:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ab631bea9cdc57dbdc97f11278d2bc1ec30f16.png" data-download-href="/uploads/short-url/3weEA6KucrhcEyeypCUvL470Vcq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18ab631bea9cdc57dbdc97f11278d2bc1ec30f16_2_690x436.png" alt="image" data-base62-sha1="3weEA6KucrhcEyeypCUvL470Vcq" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18ab631bea9cdc57dbdc97f11278d2bc1ec30f16_2_690x436.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ab631bea9cdc57dbdc97f11278d2bc1ec30f16.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ab631bea9cdc57dbdc97f11278d2bc1ec30f16.png 2x" data-dominant-color="A7A9AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">998×631 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I use the data probe, I see values around 30 and lower are background and the soft tissue that I don’t care. If I start a simple ramp from 30 to maximum, then the ‘internal structures’ are visible as intended.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c86cf84f708ef9ea2287a37bee3410163a6dfb25.png" data-download-href="/uploads/short-url/sB2XAGCzaMZFj9no4TNkmycrYcB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86cf84f708ef9ea2287a37bee3410163a6dfb25_2_690x436.png" alt="image" data-base62-sha1="sB2XAGCzaMZFj9no4TNkmycrYcB" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86cf84f708ef9ea2287a37bee3410163a6dfb25_2_690x436.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c86cf84f708ef9ea2287a37bee3410163a6dfb25.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c86cf84f708ef9ea2287a37bee3410163a6dfb25.png 2x" data-dominant-color="ABAEB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">998×631 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2021-04-03 03:06 UTC)

<p>If your object of interest is embedded in a medium that interferes with the visualization and you cannot easily remove it with a box-shaped ROI then you can use Mask volume effect in Segment Editor to remove it.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---
