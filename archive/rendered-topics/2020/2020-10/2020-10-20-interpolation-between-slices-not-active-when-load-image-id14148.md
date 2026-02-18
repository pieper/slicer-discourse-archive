# Interpolation between slices not active when load image

**Topic ID**: 14148
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/interpolation-between-slices-not-active-when-load-image/14148

---

## Post #1 by @rayan (2020-10-20 00:10 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.1120200930<br>
Expected behavior:In previous versions, when I load an image, it was automatically interpolating the slices i.e. “Interpolate” option in Volume module was checked.<br>
Actual behavior:In the latest version, this option is not active by default, and I have to check every time I load image. Is there a way to have it always activated w/o actually activating all the time?</p>
<p>Thanks,<br>
Rayan</p>

---

## Post #2 by @lassoan (2020-10-20 00:21 UTC)

<p>It is due to SlicerMorph overriding some default settings - see <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918" class="inline-onebox">Volume display - Interpolate turned off by default in newest stable?</a>.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Please change SlicerMorph so that it does not silently override application settings (disabling interpolation is particularly undesirable, but other settings may be unexpected, too), If you want to expose additional application settings to users then you can do that by a few short Python code snippets, for example:</p>
<ul>
<li>Create new settings panel: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L295-L350">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L295-L350</a>
</li>
<li>Add it to application settings: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L77-L82">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L77-L82</a>
</li>
</ul>

---

## Post #3 by @muratmaga (2020-10-20 00:38 UTC)

<p>There is already a SlicerMorph panel that all of this can be disabled. (Application Settings-&gt;SlicerMorph uncheck use SlicerMorph specific customizations ).</p>
<p><a class="mention" href="/u/pieper">@pieper</a> can we make this opt-in instead of opt-out? It is automatically enabled when SlicerMorph is installed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/756d3ec5d5d6205d140381eb107b835220ddfa53.png" data-download-href="/uploads/short-url/gKNV5CzCZLKUyDsxzFk53SNWVnt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/756d3ec5d5d6205d140381eb107b835220ddfa53_2_690x398.png" alt="image" data-base62-sha1="gKNV5CzCZLKUyDsxzFk53SNWVnt" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/756d3ec5d5d6205d140381eb107b835220ddfa53_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/756d3ec5d5d6205d140381eb107b835220ddfa53_2_1035x597.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/756d3ec5d5d6205d140381eb107b835220ddfa53_2_1380x796.png 2x" data-dominant-color="3A3D3D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2188×1264 54.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-10-20 01:36 UTC)

<p>It would be better to show the actual settings, one by one, each with its own checkbox, instead of a single all-or-nothing “SlicerMorph customization” option.</p>

---

## Post #5 by @pieper (2020-10-20 13:41 UTC)

<p>Yes, we have full control over the customization options and can choose what to expose with a UI and what to leave as code for advanced use cases.</p>

---

## Post #6 by @lassoan (2020-10-20 16:35 UTC)

<p>I’ve checked <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/.slicerrc.py">SlicerMorph customizations</a> and they should be mostly moved to Slicer core:</p>
<ul>
<li>Use compression in saved files by default =&gt; we should add to Slicer core application settings</li>
<li>Default file format for models: this can cause data loss, as it changes file format used in mrb files to ply, which means that you lose all scalar data associated with cells and points when you save the scene as mrb =&gt; this should be disabled by default until we implement at least a warning reporting mechanism from inside mrb file saving (that we want to implement anyway)</li>
<li>Interpolated image display - we have already discussed this =&gt; we should show the image grid instead of introducing artifacts (voxel edge boundaries) in the displayed image</li>
<li>Hiding Slicer logo =&gt; we should fix this in Slicer core (move it where it does not take extra space)</li>
<li>additional menu shortcuts: OK to do it for SlicerMorph (you don’t change any core behavior, just add SlicerMorph specific content)</li>
<li>Data probe collapsed by default =&gt; should be an application option (or just remember the last state in application settings)</li>
<li>Cycle segment editor effects =&gt; we cshuld add it to default segment editor shortcuts (useful for digitizer boards and wheels)</li>
</ul>

---

## Post #7 by @muratmaga (2020-10-20 16:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="14148">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Use compression in saved files by default =&gt; we should add to Slicer core application settings</p>
</blockquote>
</aside>
<p>Actually we disable compression by default.</p>

---

## Post #8 by @muratmaga (2020-10-20 16:42 UTC)

<p>Also that file slightly out date and is now replaced with <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/MorphPreferences/Resources/SlicerMorphRC.py" rel="noopener nofollow ugc">this</a> that has few additional customizations.</p>

---
