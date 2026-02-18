# Sometimes freehand drawing does not work in Segment editor

**Topic ID**: 2271
**Date**: 2018-03-08
**URL**: https://discourse.slicer.org/t/sometimes-freehand-drawing-does-not-work-in-segment-editor/2271

---

## Post #1 by @drusmanbashir (2018-03-08 18:20 UTC)

<p>Hi,<br>
While drawing annotation ROIs on a volume using freehand segmentation editor, sometimes the annotation does not draw altogether. If i delete the segmentation and create a new one , it will start working. I was able to save a mrml scene with the erratic segment map (named ‘HUM_PT1_LTlVL2’) with master volume (‘PT_20140501_123709’). Trying freehand draw on this volume produces no visible effect. If you can suggest, i would like to upload the zip folder containing the volumes segmaps and saved mrml scene.</p>
<p>Thanks<br>
Usman.</p>

---

## Post #2 by @lassoan (2018-03-08 19:22 UTC)

<aside class="quote no-group" data-username="drusmanbashir" data-post="1" data-topic="2271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drusmanbashir/48/1282_2.png" class="avatar"> drusmanbashir:</div>
<blockquote>
<p>While drawing annotation ROIs on a volume using freehand segmentation editor, sometimes the annotation does not draw altogether.</p>
</blockquote>
</aside>
<p>By “annotation does not draw” do you mean segment editor paint effect does not paint on the image? This can happen if the resolution of the binary labelmap in the segmentation node does not match resolution of the current master volume node.</p>
<p>Resolution of the binary labelmap is set to the <em>first selected</em> master volume node, so if you change a volume then the simplest is to create a new segmentation node and select the updated volume as master volume. If you had segments in an old segmentation node that you would like to keep using, you can copy those to the new segmentation (in Segmentations module’s Copy/Move section).</p>
<p>We are aware that this behavior is not intuitive and plan to add a simpler way of changing the binary labelmap geometry in the segmentation node. This task is tracked here: <a href="https://issues.slicer.org/view.php?id=4308" class="inline-onebox">Add convenient GUI for changing segmentation labelmap geometry · Issue #4308 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @drusmanbashir (2018-03-09 11:36 UTC)

<p>I realised that. But in the case I have mentioned (and in that particular scene) no matter how many times i create the segmentation and define the first master volume to be the intended one, it won’t draw on it (not using paint effect btw). I did work around it by loading the volumes one by one in the scene. So unless someone wants to look into it, the problem is not affecting my work for now.<br>
Thanks<br>
Usman.</p>

---

## Post #4 by @lassoan (2018-03-09 21:01 UTC)

<p>A post was split to a new topic: <a href="/t/surface-representation-of-segmentation-is-too-much-smoothed/2277">Surface representation of segmentation is too much smoothed</a></p>

---

## Post #5 by @lassoan (2018-03-09 21:06 UTC)

<p>It may be possible that there are non-axis aligned or tilted gantry acquisitions. Can you send the scene (upload to dropbox, onedrive, google drive, etc. and post the link here) so that I can have a look?</p>
<p>Only the draw tool has problems, or paint tool as well? If you enable sphere shape for the paintbrush, does it work then?</p>

---

## Post #6 by @drusmanbashir (2018-03-13 10:24 UTC)

<p>Hi Andras,<br>
Here is the link</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/1etf1mwe96cli8v/AACUtLDl6R4sur3e5TZWMfGEa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/1etf1mwe96cli8v/AACUtLDl6R4sur3e5TZWMfGEa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/1etf1mwe96cli8v/AACUtLDl6R4sur3e5TZWMfGEa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>A single segmentation map is saved in this folder. If i try to edit that on the master volume linked to it, I do not see anything</p>

---

## Post #7 by @drusmanbashir (2018-03-14 11:25 UTC)

<p>Hi,<br>
It seems the problem switches between contouring tools, at times I am able to use paint when freehand is not working and a few slices down it will alternate, i.e., freehand will start working and paint will stop. I hope this helps.</p>

---

## Post #8 by @lassoan (2018-03-14 17:57 UTC)

<p>Your red slice view was aligned right between two axial slices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d49888f0cee30850f093ade55f39dd71c39332c.png" data-download-href="/uploads/short-url/hSleaceVrg21xVzoCPFELaxKejW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d49888f0cee30850f093ade55f39dd71c39332c.png" alt="image" data-base62-sha1="hSleaceVrg21xVzoCPFELaxKejW" width="690" height="476" data-dominant-color="71707D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1331×919 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In these cases, due to rounding errors it may be possible that you see a different slice than you are drawing at.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7677860ee04a4e21df5c09385a14d909fedba7c1.png" data-download-href="/uploads/short-url/gU0q1E4Kkf5tKq13GPmDFkMzjKF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7677860ee04a4e21df5c09385a14d909fedba7c1.png" alt="image" data-base62-sha1="gU0q1E4Kkf5tKq13GPmDFkMzjKF" width="690" height="476" data-dominant-color="71717D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1331×919 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To fix this, use Shift+MouseMove to reposition your slice view in a sagittal or coronal view, to not be exactly at voxel boundary.</p>

---

## Post #9 by @pieper (2018-03-14 20:09 UTC)

<p>Yes, this can be an issue when there are an even number of slices in the view direction (the default fit exactly centers).</p>
<p>In the old Editor all labeling tools (draw, paint, etc) have this in the constructor for that very reason:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/EditorLib/LabelEffect.py#L193-L195" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/EditorLib/LabelEffect.py#L193-L195" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/EditorLib/LabelEffect.py#L193-L195</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="193" style="counter-reset: li-counter 192 ;">
<li># make sure the slice plane does not lie on an index boundary</li>
<li># - (to avoid rounding issues)</li>
<li>sliceLogic.SnapSliceOffsetToIJK()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It calls this code:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/f4ac8624e3ac55f4a5addfb68611639c370c353b/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L2165-L2182" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f4ac8624e3ac55f4a5addfb68611639c370c353b/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L2165-L2182" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/f4ac8624e3ac55f4a5addfb68611639c370c353b/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L2165-L2182</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="2165" style="counter-reset: li-counter 2164 ;">
<li>//----------------------------------------------------------------------------</li>
<li>void vtkMRMLSliceLogic::SnapSliceOffsetToIJK()</li>
<li>{</li>
<li>double offset, *spacing, bounds[6];</li>
<li>double oldOffset = this-&gt;GetSliceOffset();</li>
<li>spacing = this-&gt;GetLowestVolumeSliceSpacing();</li>
<li>this-&gt;GetLowestVolumeSliceBounds( bounds );</li>
<li>
</li>
<li>// number of slices along the offset dimension (depends on ijkToRAS and Transforms)</li>
<li>// - find the slice index corresponding to the current slice offset</li>
<li>// - move the offset to the middle of that slice</li>
<li>// - note that bounds[4] 'furthest' edge of the volume from the point of view of this slice</li>
<li>// - note also that spacing[2] may correspond to i, j, or k depending on ijkToRAS and sliceToRAS</li>
<li>double slice = (oldOffset - bounds[4]) / spacing[2];</li>
<li>int intSlice = static_cast&lt;int&gt; (slice);</li>
<li>offset = (intSlice + 0.5) * spacing[2] + bounds[4];</li>
<li>this-&gt;SetSliceOffset( offset );</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #10 by @drusmanbashir (2018-03-16 12:31 UTC)

<p>Slicer is proving quite a minefield of ‘gotchas’ . I think i understand the workaround. Thanks for the help</p>

---

## Post #11 by @lassoan (2018-03-16 13:26 UTC)

<p>Yes, in Slicer usually you are free to do whatever you want - but this can certainly make things more complicated and you may need to learn more than what you wanted to.</p>
<p>To make the slider behavior more clear, we planned to distinguish interpolated and slice-centered mode, but it hasn’t been implemented yet (see <a href="https://issues.slicer.org/view.php?id=3346">https://issues.slicer.org/view.php?id=3346</a>).</p>

---

## Post #12 by @drusmanbashir (2018-03-16 17:32 UTC)

<p>The only thing with this workaround is - if i have a different image-volume open in the saggital or cooronal view and i try pressing the shift key and (I see that they do some kind of alignment), does that still work or must i have the same volume open in the other window but in a different orientation?</p>

---

## Post #13 by @lassoan (2018-03-16 17:41 UTC)

<p>You don’t need to have same volume selected. The position is synchronized between all slice views that are in the same view group, regardless of what they show.</p>

---
