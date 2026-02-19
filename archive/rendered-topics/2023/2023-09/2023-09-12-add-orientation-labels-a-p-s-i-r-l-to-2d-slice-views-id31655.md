---
topic_id: 31655
title: "Add Orientation Labels A P S I R L To 2D Slice Views"
date: 2023-09-12
url: https://discourse.slicer.org/t/31655
---

# Add orientation labels (A, P, S, I, R, L) to 2D slice views

**Topic ID**: 31655
**Date**: 2023-09-12
**URL**: https://discourse.slicer.org/t/add-orientation-labels-a-p-s-i-r-l-to-2d-slice-views/31655

---

## Post #1 by @moraleda (2023-09-12 14:34 UTC)

<p>Hello everyone,</p>
<p>I  was wondering whether there is a nice way to add the orientation labels into the 2D slice view. In the 3D view, we see these labels (A, P, S, I, R, L) but in the 2D views, we can only use the little marker as orientation.</p>
<p>A naive way to show the orientation labels, that I thought of, would be some fiducials that would be recalculated every time the slice view changes. But that seems a bit complicated computationally.</p>
<p>I looked for “orientation” in the source code, but I did not find any useful code where to start from.</p>
<p>Does anyone have an idea on how to do it or a tip on where to look? Is there a nice way to draw on the slice views? (Something like, I draw in the lower right corner the orientation marker) I guess, that with python scripting one can draw only in “3D” coordinates (meaning, I set the fiducial’s position in the 3D space), so one has to do it in c++ source code?</p>
<p>Inspiration. The 2D view would then look like this. It would have the labels on the corresponding sides:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5419aeaf4bf9bea5133dd430ff6c06e7518e578b.jpeg" alt="image" data-base62-sha1="bZZ8alO24NZHhSZllp97hkQfnSj" width="505" height="434"></p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-09-12 17:11 UTC)

<p>We don’t have letters on the side of the images right now, but you can enable an orientation marker like axes or a human figure or a cube using the options illustrated below.  If that doesn’t suit your needs it would be possible to generalize by looking at how these markers are implemented and add a feature to put the letters on the side.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d2a592eef2e7e70a092e352b5b9c2b2411dea15.png" data-download-href="/uploads/short-url/8J5R71GZRXZFbJG4vCwbj6euaep.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d2a592eef2e7e70a092e352b5b9c2b2411dea15_2_690x117.png" alt="image" data-base62-sha1="8J5R71GZRXZFbJG4vCwbj6euaep" width="690" height="117" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d2a592eef2e7e70a092e352b5b9c2b2411dea15_2_690x117.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d2a592eef2e7e70a092e352b5b9c2b2411dea15_2_1035x175.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d2a592eef2e7e70a092e352b5b9c2b2411dea15_2_1380x234.png 2x" data-dominant-color="E5E6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1658×282 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e722d9ba97039cfced4070a7e07305491ef5365.png" data-download-href="/uploads/short-url/6CSAwVSs49nNqL5Fx3350FU5zWl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e722d9ba97039cfced4070a7e07305491ef5365_2_690x368.png" alt="image" data-base62-sha1="6CSAwVSs49nNqL5Fx3350FU5zWl" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e722d9ba97039cfced4070a7e07305491ef5365_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e722d9ba97039cfced4070a7e07305491ef5365.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e722d9ba97039cfced4070a7e07305491ef5365.png 2x" data-dominant-color="2F2827"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×384 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @moraleda (2023-09-18 12:45 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I know about the orientation marker. I looked at the source code, but wondering if for my purposes is not better to use the source code for the “3D view cube” (the pink cube in the image I posted). However, I cannot find where it is defined. Could you help me to find the right word to search the source code?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2023-09-18 13:22 UTC)

<p>The purple cube is designed for 3D views. It is much easier to display direction codes in 2D views. The only complication is that there are lots more corner and side annotations that we want to show in slice views, so we need to make sure that all the information fits. We have an issue that tracks this task, it would be great if you could work on it:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7184">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7184" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7184" target="_blank" rel="noopener">Refactor Slice View Annotations infrastructure</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-22" data-time="02:38:43" data-timezone="UTC">02:38AM - 22 Aug 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

Since its i<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nception started in 2014, the support for rendering slice annotations has been very useful.

It is ultimately done in the `SliceAnnotations`[^1] class instantiated based on the workflow described below.

Once the `SliceAnnotations` is instantiated, it is then responsible to add observation on slice logics (see `addSliceViewObserver()`[^6]) by systematically checking if new slice viewer have been instantiated within the function `updateViewAnnotations()`[^7] it self called when any of the slice logic is modified.

**Problem:** As outlined below by @lassoan, the current design is not extensible &amp; flexible as it requires to hard-code module specific behavior into a single script. It for example, prevent extension from registering new annotation that should take precedence.

[^6]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L346-L357
[^7]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L363-L380

## Describe the solution you'd like

* Re-implemented in C++
* Organize the content to display in `vtkMRMLTextNode` nodes with associated displayable manager
* Allow customization of displayed fields
* Support displaying
  * Slice position
  * Anatomical direction codes
  * Image display parameters (window, level, slice thickness, etc)
  * Patient/study/series metadata

## Describe alternatives you've considered

NA

## Additional context

### Related posts &amp; issues

* https://discourse.slicer.org/t/how-to-show-orientation-marker-label-left-right-anterior-posterior/20231
* https://github.com/Slicer/Slicer/issues/4854

### Excerpt copied from the prior comments and emails

_Originally shared by @lassoan over email on August 19th, 2023_

&gt; We want to display a lot of things around image sides and corners:
&gt; - Patient/study/series metadata (with much more flexibility than now) 
&gt; - Anatomical direction codes (L, R, A, P, LA, LPI,... similarly to slice offset sliders) 
&gt; - Image display parameters (window, level, slice thickness, etc)
&gt; - Slice position, maybe some data probe content
&gt; - Any text node content (that would allow a flexible way for modules to display custom content; which corner, color, etc. could be specified in display node)
&gt; 
&gt; The current design is very limited, inflexible, non-extensible in any way. The implementation is also very fragile, low quality.
&gt; 
&gt; The best would be to reimplement it in C++, using MRML nodes to store data, displayable manager to render, etc.
&gt; 
&gt; Maybe all the corner text could be specified using HTML-like description using placeholders, for example:
&gt; 
&gt; ```html
&gt; &lt;b&gt;&lt;PatientName/&gt; &lt;PatientAge/&gt; &lt;PatientSex format="short" /&gt;&lt;/b&gt;&lt;br&gt;
&gt; &lt;StudyDate/&gt;&lt;br&gt;
&gt; &lt;WindowWidthLevel/&gt;&lt;br&gt;
&gt; &lt;TextNode id="vtkMRMLTextNode1" color="red" /&gt;
&gt; ```

_Originally posted by @lassoan in https://github.com/Slicer/Slicer/issues/7176#issuecomment-1684865471_

&gt; Slice view annotations is a mess. It was a quick prototype that got integrated to have this important feature in Slicer, but the design is really fragile and limited. We would need to rebuild it from scratch, using proper MRML-based design and flexibility and extensibility in mind, as overlay on image corners is very important space for displaying information.

_Originally posted by @pieper in https://github.com/Slicer/Slicer/issues/7176#issuecomment-1685033306_

&gt; Many viewers also use these as UI controls/widgets too (e.g. control reslice rotation or window/level tools by clicking on the corresponding corner annotation can be logical and 

### Workflow: Instantiation of `DataProbeLib.SliceAnnotations`

1. `DataProbe` module constructor, `slicer.app.startupCompleted()` is connected to `DataProbe.DataProbe.addView()`[^2]
3. `DataProbe.DataProbe.addView()` instantiates[^3] `DataProbeInfoWidget.DataProbeInfoWidget`[^4] class 
4. In `DataProbeInfoWidget` constructor, the function `DataProbeInfoWidget._createSmall()` which intern instantiates `DataProbeLib.SliceAnnotations()`[^5]

[^1]: https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py
[^2]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L40-L41
[^3]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L59-L60
[^4]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L68-L106
[^5]: https://github.com/Slicer/Slicer/blob/8c92a12d6acecde092439981af70b1a27b6d2cf1/Modules/Scripted/DataProbe/DataProbe.py#L401-L406</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note that direction codes are not always just simple axis directions (L, R, A, P, I, S) but in case of oblique slices they can be a combination of 2 or 3 directions (LP, AR, LPI, SLP, …). You can see these direction codes next to the slice selector slider after you rotated slice views.</p>

---

## Post #5 by @moraleda (2023-09-19 07:46 UTC)

<p>Is there a reason why not just “rotate” the L,R,A,P,I,S labels around the slice? For me it seems complicated to display the combination of the of the directions.<br>
I have seen this “rotation” in another software that is widely used by clinicians.</p>
<p>“Rotation” would be like in this image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84ed503c71549d8aacbe47238443168eb6bfc2a4.png" data-download-href="/uploads/short-url/iXVt04GFSzmP6iFGL7METZg2G3O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84ed503c71549d8aacbe47238443168eb6bfc2a4_2_690x332.png" alt="image" data-base62-sha1="iXVt04GFSzmP6iFGL7METZg2G3O" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84ed503c71549d8aacbe47238443168eb6bfc2a4_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84ed503c71549d8aacbe47238443168eb6bfc2a4_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84ed503c71549d8aacbe47238443168eb6bfc2a4_2_1380x664.png 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2187×1055 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2023-09-19 11:13 UTC)

<p>In most cases direction codes displayed on the sides or rotated should work similarly well. Even very experienced radiologist have a lot of trouble interpreting oblique images, so most of the time the images would be aligned with anatomical axes or slightly rotated along one axis. Direction codes should be fairly straightforward to interpret either displayed at image sides or rotated around. Directions are only needed for the clinicians to distinguish sides of symmetric structures anyway, as they are getting the general sense of orientation by recognizing patient anatomy in the images.</p>
<p>However, when you display oblique slices, labeling direction becomes much harder, because neither slice intersection lines nor any axes that lie within the slice plane will concide with any of the anatomical axis directions.</p>
<p>For example, what direction codes would you draw an these image slices and where?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfb583183855ae8f25bd6f0cf166f9cdd1f78dd2.jpeg" data-download-href="/uploads/short-url/vV1myjA8awDL42kuVGkl5kHZQB4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb583183855ae8f25bd6f0cf166f9cdd1f78dd2_2_690x473.jpeg" alt="image" data-base62-sha1="vV1myjA8awDL42kuVGkl5kHZQB4" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb583183855ae8f25bd6f0cf166f9cdd1f78dd2_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb583183855ae8f25bd6f0cf166f9cdd1f78dd2_2_1035x709.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb583183855ae8f25bd6f0cf166f9cdd1f78dd2_2_1380x946.jpeg 2x" data-dominant-color="646264"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1505×1033 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Rotating the labels can reduce the direction codes from 3-letter-code to 2, or from 2-letter-code to just 1 in some special cases, which I agree could be somewhat useful, as it could potentially make some directions easier to interpret. However, it would raise several new problems:</p>
<ul>
<li>In general, you would not be able to show single-letter codes anywhere anyway. You could choose to show only the dominant direction (i.e., the first letter of the direction code), but that may be misleading.</li>
<li>It would make the already difficult corner text annotation layout problem even harder to solve: where would you show those labels to avoid overlap with corner annotations?</li>
<li>Users could have trouble finding those direction codes, because they move around.</li>
<li>Direction labels may be mistaken for other image annotations if the labels do not appear in a standard location.</li>
<li>Orientation codes are displayed at image sides in most if not all other radiology software. Users would have harder time getting used to the labels showing up in different location.</li>
</ul>
<p>Considering that rotating the labels around would not make the directions much easier to interpret in complex cases and it would raise several new problems, overall it seems better to display labels in standard locations (at center of image sides).</p>

---

## Post #7 by @moraleda (2023-11-02 15:30 UTC)

<p>I got back to the problem after a while, considering what you said. I thought of a solution (probably not general) utilizing <code>vtk.CornerAnnotations</code> to write on the sides of the viewers. I need to write only to the edge centers, as my views are always perpendicular to each other.</p>
<p>(However, it could be later extended to show the letters after reorienting your views such that one view would be horizontal and we would write at the right edge.)</p>
<p>During this, I found out, that one is not able to write to lower right corner. When you run</p>
<pre><code class="lang-auto">view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.LowerRight,'note')
</code></pre>
<p>the <code>note</code> is visible for a moment, and then disapears again. Is it because the place is reserved for the orientation marker?</p>
<p>Another question I have is how do you get the orientation programatically?<br>
In the image below, I have just hardcoded <code>LIA</code> into the code. I cannot find the right command to get this orientation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e980c6ef77d49ee6a959b763e20ec9cdaab8218.jpeg" data-download-href="/uploads/short-url/i3TVhcVWEMqVBHjhfyXzuSdYJ4Y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e980c6ef77d49ee6a959b763e20ec9cdaab8218_2_320x250.jpeg" alt="image" data-base62-sha1="i3TVhcVWEMqVBHjhfyXzuSdYJ4Y" width="320" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e980c6ef77d49ee6a959b763e20ec9cdaab8218_2_320x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e980c6ef77d49ee6a959b763e20ec9cdaab8218_2_480x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e980c6ef77d49ee6a959b763e20ec9cdaab8218_2_640x500.jpeg 2x" data-dominant-color="74685C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">890×694 48.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>

---

## Post #8 by @lassoan (2023-11-02 15:40 UTC)

<p>Corner annotations are alredy used by DataProbe module. All corners are already used for displaying some content. Only the centers remain available for direction codes, and actually that is the position where you want to display the codes anyway.</p>
<p>Note that VTK corner annotations very limited. It can only do a small fraction of what we need (see <a href="https://github.com/Slicer/Slicer/issues/7184">here</a> for some details), so if you implement direction code display using corner annotations, it’ll probably have to remain just prototype/test code and needs to be redesigned before it can be integrated into Slicer core.</p>

---
