# Paint segmentation not filling slice after ROI and rotate to volume plane

**Topic ID**: 1915
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/paint-segmentation-not-filling-slice-after-roi-and-rotate-to-volume-plane/1915

---

## Post #1 by @JohnK (2018-01-23 18:39 UTC)

<p>Hi, I am using slicer 4.9.0-2017-11-23 on Windows.<br>
I was getting the segmentation errors previously discussed (I am segmenting an older T1+c image at 4 mm thickness) so I did this:</p>
<ol>
<li>
<p>I used the crop volume and b-spline resampled at isotropic dimensions.</p>
</li>
<li>
<p>I followed this suggestion to  rotate all sections to volume plane:<br>
<a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459" class="inline-onebox">Segmentation Editor - How to disable painting on adjacent slices?</a></p>
</li>
<li>
<p>Of note, I had already done some segmentation before 1 and 2 were performed.</p>
</li>
</ol>
<p>When I use the ‘Draw’ tool (axial slice) I still get incomplete filling of the draw outline:<br>
first image is outline:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0eaa0714c64ad8222d04322c044e72ef866ce3f.jpeg" data-download-href="/uploads/short-url/rwCmiYi0laS3BOgZPDQULx736BV.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0eaa0714c64ad8222d04322c044e72ef866ce3f_2_283x500.jpg" alt="image" data-base62-sha1="rwCmiYi0laS3BOgZPDQULx736BV" width="283" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0eaa0714c64ad8222d04322c044e72ef866ce3f_2_283x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0eaa0714c64ad8222d04322c044e72ef866ce3f_2_424x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0eaa0714c64ad8222d04322c044e72ef866ce3f.jpeg 2x" data-dominant-color="70756D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">444×784 67.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This image is what is filled<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a2b2c2e853694331c47de5e97d5c22fc079dad7.jpeg" data-download-href="/uploads/short-url/1rXgPNO0aC0DDC8W6fQbDSs4n1t.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a2b2c2e853694331c47de5e97d5c22fc079dad7_2_274x500.jpg" alt="image" data-base62-sha1="1rXgPNO0aC0DDC8W6fQbDSs4n1t" width="274" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a2b2c2e853694331c47de5e97d5c22fc079dad7_2_274x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a2b2c2e853694331c47de5e97d5c22fc079dad7_2_411x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a2b2c2e853694331c47de5e97d5c22fc079dad7.jpeg 2x" data-dominant-color="7A7E75"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">420×766 58.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I confess I am no wizard at 3dSlicer so am I doing something wrong? Thanks</p>

---

## Post #2 by @cpinter (2018-01-23 19:09 UTC)

<p>The voxels are not aligning with your view, so you get a staircase effect. You can align the view to your slices and draw like that if you want, but probably your current segmentation is fine. What does it look like in 3D?</p>

---

## Post #3 by @JohnK (2018-01-23 20:32 UTC)

<p>Yes, strange the 3d (with 0.5 smoothing) looks fine and filled in so the program does what it should. So align the view is different from ‘rotate to volume plane’ ? Is there a way to align to view?</p>
<p>Also since the purpose is to measure volumes I will want to make sure I get the segmentation correct.<br>
Thanks,<br>
John</p>

---

## Post #4 by @Ahmed_Soufane (2018-01-23 21:00 UTC)

<p>Dear John,</p>
<p>Would you please tell me how to access/edit/modify the rotation and zoom<br>
in/out of an image on 3dslicer using python console.??</p>
<p>Thank you,<br>
Sincerely,<br>
Ahmed Soufane</p>

---

## Post #5 by @cpinter (2018-01-23 21:06 UTC)

<p><a class="mention" href="/u/ahmed_soufane">@Ahmed_Soufane</a>  You’ve answered to an email related to another thread, where it’s off-topic. Please keep using the thread you started</p><aside class="quote" data-post="1" data-topic="1912">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotation-zooming/1912">Rotation&amp;zooming </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
How can I modify or call the rotation of an image on the python interactor  on 3dslicer ? 
Is it possible to modify or edit zooming in and out of the image on python console ?
  </blockquote>
</aside>
<p>
Looking into Steve’s suggestion will solve your problem</p>

---

## Post #6 by @cpinter (2018-01-23 21:08 UTC)

<p>Yes, the function you want is “Rotate to volume plane” in the slice view controller’s toolbar.</p>

---

## Post #7 by @JohnK (2018-01-23 21:22 UTC)

<p>Hi Csaba, yes I had already rotated to volume plane (see my first post), and after that I was still getting the problem. Maybe that all has to happen at the very beginning prior to any segmentation?</p>
<p>I might add that using the ‘Paint’ tool worked different from the ‘Draw’ tool. The images above occur with the ‘draw’ tool.</p>
<p>[Edit] OK, If I set up <strong>all views prior to segmentation</strong>, now it appears to work fine.</p>

---

## Post #8 by @lassoan (2018-01-23 23:08 UTC)

<aside class="quote no-group" data-username="JohnK" data-post="1" data-topic="1915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/59ef9b/48.png" class="avatar"> JohnK:</div>
<blockquote>
<p>Of note, I had already done some segmentation before 1 and 2 were performed.</p>
</blockquote>
</aside>
<p>If you create a segmentation and set a master volume then it determines the geometry of the internal binary labelmap. If you later switch master volume it does not matter, it won’t change the internal geometry. You can to create a new Segmentation node, set the new volume (result of resampling) and work with that segmentation. You can copy segments from your old segmentation node using Segmentations module’s Import/export section.</p>
<p>Note that most effects work well on oblique slices (only level tracing and Fill between slices do not). The sampling artifacts (incomplete filling, striping) appearing at segment boundaries are not nice to look at, but they don’t affect the quality of segmentation, the segmentation is still correct and there are no holes in 3D.</p>

---

## Post #10 by @JohnK (2018-01-30 20:32 UTC)

<p>Not sure if this is relevant… bug or just my new user brain.</p>
<p>I was getting an error again after (what i thought was) proper setup for manual segmentation with the paint tool, and made sure of the align to volume was set. (BTW, I am also segmenting longitudinal volumes that are registered that may have different slice thickness). Then the circle cursor only appears during 'sphere" and I get a different ‘tool’ cursor. Then I noticed these critical errors appeared:</p>
<p>class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushSphere”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushSphere”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “ColorSmudge”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “ColorSmudge”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushMaximumAbsoluteDiameter”  cannot be found for effect  "Erase"<br>
double __cdecl qSlicerSegmentEditorAbstractEffect::doubleParameter(class QString) : Parameter named  “BrushMaximumAbsoluteDiameter”  cannot be converted to floating point number!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushAbsoluteDiameter”  cannot be found for effect  "Erase"<br>
double __cdecl qSlicerSegmentEditorAbstractEffect::doubleParameter(class QString) : Parameter named  “BrushAbsoluteDiameter”  cannot be converted to floating point number!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushSphere”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushSphere”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “ColorSmudge”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “ColorSmudge”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushAbsoluteDiameter”  cannot be found for effect  "Erase"<br>
double __cdecl qSlicerSegmentEditorAbstractEffect::doubleParameter(class QString) : Parameter named  “BrushAbsoluteDiameter”  cannot be converted to floating point number!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushSphere”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushSphere”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “ColorSmudge”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “ColorSmudge”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushSphere”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushSphere”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “ColorSmudge”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “ColorSmudge”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushDiameterIsRelative”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushSphere”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushSphere”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “ColorSmudge”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “ColorSmudge”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “ColorSmudge”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “ColorSmudge”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!<br>
class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  “BrushPixelMode”  cannot be found for effect  "Erase"<br>
int __cdecl qSlicerSegmentEditorAbstractEffect::integerParameter(class QString) : Parameter named  “BrushPixelMode”  cannot be converted to integer!</p>

---

## Post #11 by @lassoan (2018-01-30 23:10 UTC)

<p>Can you provide step-by-step description of what you do so that we can reproduce the problem?</p>

---

## Post #12 by @JohnK (2018-01-30 23:43 UTC)

<p>Thanks, here are the steps<br>
Windows 7, 64-bit, slicer ver. 4.9.0-2017-11-23 (from nightly build)</p>
<ol>
<li>load 2 different T1+c MRIs taken at 2 time points</li>
<li>register the older MRI to the newer one since the older has thicker cuts (1 vs 4 mm), in plane resolution is nearly the same. Registration looks great.</li>
<li>Create a single segmentation.</li>
<li>set the active volume, then click the “rotate volume to plane” button, when all slice views are locked together (all rotate slightly after this). This is done for each master volume.</li>
<li>Manually ‘paint’ the location of the tumor - this gives me the above problems.</li>
<li>potential issues – segmentation may not all have been done on the same session. Also it seems intermittent – that is I cannot isolate a specific thing I am doing.</li>
<li>Checked memory via Task manager to ensure I have some head-room.</li>
</ol>
<p>Thanks for your help!</p>

---

## Post #13 by @lassoan (2018-01-31 04:40 UTC)

<p>At the beginning of Step 3, is the master volume the same as the background volume in the slice viewers?</p>
<p>Note that the brush thickness is always the same as the slice spacing that is set in the slice viewer. If the brush size is much thinner than the slice thickness of the segmentation’s labelmap then it might not be large enough to include any voxels. This should not happen if the master volume is the background volume and slice views are rotated to volume’s plane.</p>

---

## Post #14 by @JohnK (2018-01-31 18:05 UTC)

<p>Ok, good to know.</p>
<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="1915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>At the beginning of Step 3, is the master volume the same as the background volume in the slice viewers?</p>
</blockquote>
</aside>
<p>I believe so. To be honest, I just make sure the volume in the viewer was the same as that listed in “Master volume.” I never actually checked but I am pretty sure none was in the Foreground.  I have been consistently doing segmentations in  single axial slice only. I will be sure to check this in the future.</p>
<p>Currently, I really can’t seem to isolate a factor that leads to this error but I can keep these issues in mind.</p>

---

## Post #15 by @lassoan (2018-01-31 18:24 UTC)

<aside class="quote no-group" data-username="JohnK" data-post="14" data-topic="1915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/59ef9b/48.png" class="avatar"> JohnK:</div>
<blockquote>
<p>I just make sure the volume in the viewer was the same as that listed in “Master volume.”</p>
</blockquote>
</aside>
<p>Geometry of internal labelmap in segmentation node is determined by the <strong>first selected master volume</strong>. If you later change the master volume, it does not affect the geometry (slice thickness, orientation, etc). We plan to give the user some more controls over this, so that users could force changing of the labelmap geometry for an existing segmentation, but for now, if you want to change labelmap geometry in the segmentation, then you need to create a new segmentation and make sure you that the master volume you select first is the correct one.</p>

---
