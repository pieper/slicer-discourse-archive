# Drawing shapes in volume rendering

**Topic ID**: 2068
**Date**: 2018-02-12
**URL**: https://discourse.slicer.org/t/drawing-shapes-in-volume-rendering/2068

---

## Post #1 by @Jonas (2018-02-12 13:43 UTC)

<p>Hello,<br>
This is my first post on this forum, and I am new to Slicer. Hopefully you will be tolerant <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I want to create a shape, which would be visible in VR - the best approach would be to use Fiducials (as they are easy to move once placed) and possibly connect them by lines to draw a shape. I need to draw a triangle. I suppose. it could be a segment in 3D.<br>
Any ideas what would be the best and easiest approach?<br>
Thanks,<br>
Jonas</p>

---

## Post #2 by @timeanddoctor (2018-02-12 14:21 UTC)

<p>If you went to draw a point and a triangle line, the best method is “CurveMaker” module.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CurveMaker" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CurveMaker</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ea933478b30a5cf7d80be7334247324b5f9daf4.png" alt="" data-base62-sha1="mDzWV2QUW4BmpzFiG4BHnNbJRUE" role="presentation" width="300" height="363"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c975760da2c7f432a92b4f0f98a058c9f88ce4.png" alt="" data-base62-sha1="jEV2igskYKjfq8GgdhrRQCdwSuU" role="presentation" width="300" height="306"></p>

---

## Post #3 by @Jonas (2018-02-13 00:26 UTC)

<p>Thanks for your input. I have tested the functionality - it is on the right path to the destination <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
My intention is to have a plane/area (surface?) between the dots.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c51709d6b28ae3b81fc367b100492934d73b9ad.png" data-download-href="/uploads/short-url/miQY72Y3rfIN5jWCV5Jse0jxjjv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c51709d6b28ae3b81fc367b100492934d73b9ad_2_690x256.png" alt="image" data-base62-sha1="miQY72Y3rfIN5jWCV5Jse0jxjjv" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c51709d6b28ae3b81fc367b100492934d73b9ad_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c51709d6b28ae3b81fc367b100492934d73b9ad_2_1035x384.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c51709d6b28ae3b81fc367b100492934d73b9ad.png 2x" data-dominant-color="99929D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1367×508 556 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Curve is on the left, and I want to have an area like on the right.<br>
Any insights how this could be achieved?</p>

---

## Post #4 by @Jonas (2018-02-13 00:54 UTC)

<p>Ok, I managed to get it to work. I found a plugin markup to model and it had a function “closed surface”.<br>
Now I can generate such model:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/3/3046b4648242a34a9ce24e4f2db03db8866ad67d.jpg" data-download-href="/uploads/short-url/6T4oXEcDjOECcxcrvmQViYJ5aG1.jpg?dl=1" title="7dXdI9OZCn.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3046b4648242a34a9ce24e4f2db03db8866ad67d_2_690x416.jpg" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3046b4648242a34a9ce24e4f2db03db8866ad67d_2_690x416.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3046b4648242a34a9ce24e4f2db03db8866ad67d_2_1035x624.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3046b4648242a34a9ce24e4f2db03db8866ad67d_2_1380x832.jpg 2x" data-dominant-color="8F8D8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">7dXdI9OZCn.jpg</span><span class="informations">1920×1160 456 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Now I have additional question - if I try to make it transparent, it disappears - despite the skull having no visible voxels in the clipping ROI, it does not show model in it with transparency - any ideas how it could be solved?</p>

---

## Post #5 by @lassoan (2018-02-13 02:12 UTC)

<p>Note that there is already a Segment Editor effect (“Surface cut”), available in SegmentEditorExtraEffects extension, which uses MarkupsToModel module to create segments. I would recommend using this effect and tune it as needed, instead of redeveloping this effect from scratch.</p>
<p>To show semitransparent models correctly, you need to enable depth peeling in the 3D view:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d727d463d03b0bd763f843382532354c3f468d66.png" alt="image" data-base62-sha1="uHlZqx9YlHsMoYt4ERCHPv2AlMi" width="588" height="294"></p>

---

## Post #6 by @Jonas (2018-02-13 12:42 UTC)

<p>Ok, I followed your advice - I can easily segment a triangle shape surface (which is perfect), however, I still can’t achieve to have semi-transparency in 3D rending whatever I do. Any ideas?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/c/c6100e9d8ddab701c1d5afa0b67d84225f57ac7f.jpg" data-download-href="/uploads/short-url/sg8WmohEFGnWl7bWYgTzSYyY7f1.jpg?dl=1" title="CYEa4Dzbbb.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6100e9d8ddab701c1d5afa0b67d84225f57ac7f_2_690x416.jpg" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6100e9d8ddab701c1d5afa0b67d84225f57ac7f_2_690x416.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6100e9d8ddab701c1d5afa0b67d84225f57ac7f_2_1035x624.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c6100e9d8ddab701c1d5afa0b67d84225f57ac7f_2_1380x832.jpg 2x" data-dominant-color="898888"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CYEa4Dzbbb.jpg</span><span class="informations">1920×1160 603 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2018-02-13 13:00 UTC)

<p>It looks good. To adjust opacity, move the opacity  slider in Display section / 3D row.</p>

---

## Post #8 by @Jonas (2018-02-13 13:11 UTC)

<p>If I subtract any amount (ex 10%) it instantly disappears completely:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/e/e86e9cd0d0d922f2afa766c64f3b6ab720fa5999.jpg" data-download-href="/uploads/short-url/xabL5ntujdAJCxJ3gt1FI6IZffz.jpg?dl=1" title="FhitzO5iUW.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86e9cd0d0d922f2afa766c64f3b6ab720fa5999_2_690x416.jpg" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86e9cd0d0d922f2afa766c64f3b6ab720fa5999_2_690x416.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86e9cd0d0d922f2afa766c64f3b6ab720fa5999_2_1035x624.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86e9cd0d0d922f2afa766c64f3b6ab720fa5999_2_1380x832.jpg 2x" data-dominant-color="8B8A8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">FhitzO5iUW.jpg</span><span class="informations">1920×1160 601 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @Jonas (2018-02-13 13:15 UTC)

<p>If I make some other projection where are no structures behind the segmented region, it appears translucent. But if there is any structure behind it, it does not appear at all. It seems that the shape instantly goes to the background and only appears if are are no other structures in the same projection.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db27b073be43d2cc316a059d2349936d7b236805.png" data-download-href="/uploads/short-url/vgJBbYimJbgF0Rd7NWhO3X4b6vz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db27b073be43d2cc316a059d2349936d7b236805_2_670x500.png" alt="image" data-base62-sha1="vgJBbYimJbgF0Rd7NWhO3X4b6vz" width="670" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db27b073be43d2cc316a059d2349936d7b236805_2_670x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db27b073be43d2cc316a059d2349936d7b236805.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db27b073be43d2cc316a059d2349936d7b236805.png 2x" data-dominant-color="D0C6AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">679×506 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2018-02-13 14:33 UTC)

<p>On certain graphics cards, depth peeling does not work well in Slicer-4.8.1 and you need to use latest nightly version (not older than a couple of days).</p>

---

## Post #11 by @lassoan (2018-02-13 15:13 UTC)

<p>I’ve just noticed that you may use volume rendering. The title of the post was just “VR” instead of volume rendering, and I assumed that this is a project about virtual reality. Nowadays, it is better not to use the VR acronym.</p>
<p>Compositing of volume rendering and transparent surfaces may not be correct. However, these should work:</p>
<ul>
<li>Option A: show volume rendering and opaque surface models</li>
<li>Option B: segment your volume using Segment Editor and show transparent surfaces</li>
<li>Option C: edit your volume, for example, using Mask Volume effect in Segment Editor. Requires installation of SegmentEditorExtraEffects extension.</li>
<li>Option D: show volume rendering and show surface models as wireframe (Models module / Display / Representation)</li>
</ul>

---

## Post #12 by @Jonas (2018-02-13 15:41 UTC)

<p>yes, I am talking about volume rendering. I have into it deeper - I tried 4.9.0 nighly, but with it I have a problem, it does not save segmentations.</p>

---

## Post #13 by @lassoan (2018-02-13 16:17 UTC)

<aside class="quote no-group" data-username="Jonas" data-post="12" data-topic="2068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/aeb1de/48.png" class="avatar"> Jonas:</div>
<blockquote>
<p>it does not save segmentations</p>
</blockquote>
</aside>
<p>What do you do? What do you expect to happen? What happens instead? What operating system? Any related error in the log?</p>

---

## Post #14 by @Jonas (2018-02-13 19:01 UTC)

<p>Hello,<br>
I go to segmentations, create a segment (surface cut), mark the fiducials (as I did in 4.8.1), click “Apply”. When I click to return to Segmentations view the newly segmented triangle disappears.</p>
<p>I do have errors in error log:</p>
<pre><code class="lang-auto">void __cdecl qSlicerSegmentationsModuleWidget::onEditSelectedSegment(void) : MRMLNodeComboBox_Segmentation is not found in Segment Editor module
</code></pre>
<p>Traceback (most recent call last):</p>
<pre><code class="lang-auto">  File "C:/Users/Jonas/AppData/Roaming/NA-MIC/Extensions-26909/SegmentEditorExtraEffects/lib/Slicer-4.9/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py", line 255, in onApply
    self.logic.cutSurfaceWithModel(self.segmentMarkupNode, self.segmentModel)
  File "C:/Users/Jonas/AppData/Roaming/NA-MIC/Extensions-26909/SegmentEditorExtraEffects/lib/Slicer-4.9/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py", line 455, in cutSurfaceWithModel
    modMode = slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd
AttributeError: 'module' object has no attribute 'qSlicerSegmentEditorAbstractEffect'
</code></pre>
<p>In 4.8.1 I installed firstly Markups to Model and then SegmentEditorExtraEffects. In 4.9.0 nightly I installed instantly SegmentEditorExtraEffects and Markups to Model was installed together as a dependency.</p>
<p>Standard segmentations (draw, paint) works just fine.<br>
Operating system: Windows 10 64 bit.</p>
<p>P.S. Thanks for fixing the markup - I will get used to using them.</p>

---

## Post #15 by @lassoan (2018-02-13 21:43 UTC)

<p>I’ve pushed a fix, the surface cut effect should work correctly in tomorrow’s nightly version.</p>

---

## Post #16 by @lassoan (2018-02-14 04:42 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> did some investigation and it turned out that mixing transparent surfaces with volume rendering is supported in recent VTK versions; and <a href="https://github.com/commontk/CTK/pull/785#issuecomment-365480947">updated Slicer to take advantage of this option</a>. The feature will be available in the nightly builds from tomorrow. Thanks a lot Jc!</p>

---

## Post #17 by @Jonas (2018-02-14 10:36 UTC)

<p>Great. Thanks for guiding me all this way step by step. I will test the new<br>
Nighly.</p>
<p>Best regards<br>
Jonas</p>

---
