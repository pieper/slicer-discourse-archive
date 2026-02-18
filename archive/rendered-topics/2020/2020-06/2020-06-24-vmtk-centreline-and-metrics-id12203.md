# VMTK centreline and metrics

**Topic ID**: 12203
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/vmtk-centreline-and-metrics/12203

---

## Post #1 by @chir.set (2020-06-24 15:40 UTC)

<p>This is a feature request concerning VMTK centerline and its metrics.</p>
<p>GLOBAL METRICS</p>
<p>The below image shows a sigle centerline of a pathological artery. It is not clear where is located the measured radius.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7159d7d21efdcd05ea6b697662736aa840e10ab3.jpeg" data-download-href="/uploads/short-url/gaKrp4LlV8obvaLcgE8Q67Tu9ij.jpeg?dl=1" title="SceneView" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7159d7d21efdcd05ea6b697662736aa840e10ab3_2_686x500.jpeg" alt="SceneView" data-base62-sha1="gaKrp4LlV8obvaLcgE8Q67Tu9ij" width="686" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7159d7d21efdcd05ea6b697662736aa840e10ab3_2_686x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7159d7d21efdcd05ea6b697662736aa840e10ab3_2_1029x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7159d7d21efdcd05ea6b697662736aa840e10ab3_2_1372x1000.jpeg 2x" data-dominant-color="262523"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView</span><span class="informations">1783×1299 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I wish the table data gives the minimum and the maximum radius too, between the two enpoints. At best, a graph of the measured radius at every millimeter would be helpful.</p>
<p>TARGETED METRICS</p>
<p>The image below shows a cross-section of a normal artery, where the radius is the same in every direction. In the pathological artery, the lumen morphology varies considerably.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b38f3cdb511fd5f855ae2ddd51d2973ac7207cae.png" data-download-href="/uploads/short-url/pCslRrDIxk77M7n2jzpW10ij03I.png?dl=1" title="ArteryLumen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b38f3cdb511fd5f855ae2ddd51d2973ac7207cae.png" alt="ArteryLumen" data-base62-sha1="pCslRrDIxk77M7n2jzpW10ij03I" width="666" height="500" data-dominant-color="FEFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ArteryLumen</span><span class="informations">800×600 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I wish that we can click on any point of the centreline, and get the minimum and maximum radius at the chosen point in some way. At best, a plane perpendicular to the centreline could be drawn in the segment, and remains visible with its metrics shown in the view, or in a separate table.</p>
<p>CLINICAL RELEVANCE</p>
<p>We usually care of vessel diameter, not radius. The conversion is straightforward, but has yet to be done. An additional column showing diameters would be welcome.</p>
<p>Hoping that these requests get considered.</p>
<p>Best regards.</p>

---

## Post #2 by @chir.set (2020-06-28 21:14 UTC)

<p>I pushed a <a href="https://github.com/chir-set/CenterLineMetrics" rel="nofollow noopener">module</a> that plots average diameters of a CMTK centerline. It’s templated over <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/LineProfile" rel="nofollow noopener">LineProfile</a> module.</p>
<p>Comments of Slicer’s gurus are welcome.</p>
<p>Regards.</p>

---

## Post #3 by @lassoan (2020-07-01 01:22 UTC)

<p>The module looks nice! It could be added to SlicerVMTK extension.</p>
<p>I would just recommend to fix/improve two things:</p>
<ol>
<li>
<p>The distance computation along the centerline. Currently, you project the centerline to a selected axis, but instead we should use distance along centerline. This distance should be fairly easy to compute (sum of Euclidean distances between points), but I am sure it can be already computed by VMTK (as far as I understand, this is called the “abscissa” and computed by filters like vmtkBranchMetrics).</p>
</li>
<li>
<p>Use the latest scripted module template in Extension Wizard module in latest Slicer Preview Release (that is downloaded July 1, 2020 or later), as it is greatly improved. Most importantly, the GUI is created in Qt Designer instead of manual scripting.</p>
</li>
</ol>
<p>Once these are addressed, it would be great if you could submit a pull request to <a href="https://github.com/vmtk/SlicerExtension-VMTK">SlicerVMTK extension</a> that adds this new module.</p>

---

## Post #4 by @chir.set (2020-07-01 06:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but instead we should use distance along centerline</p>
</blockquote>
</aside>
<p>True; would be closer to interventional reality. I’ll have a closer look as to what VMTK offers… within my technical limits. Thanks for the hints.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>a selected axis</p>
</blockquote>
</aside>
<p>This has just been adressed, any of the RAS axis can be selected.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Use the latest scripted module template</p>
</blockquote>
</aside>
<p>Does it mean ‘do rewrite the GUI’ ?</p>

---

## Post #5 by @lassoan (2020-07-01 13:00 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Does it mean ‘do rewrite the GUI’ ?</p>
</blockquote>
</aside>
<p>It means that you don’t need any code for creating the GUI, but use QtDesigner. It allows you to create your user interface by drag-and-dropping widgets and setting its properties.</p>

---

## Post #6 by @chir.set (2020-07-02 19:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we should use distance along centerline</p>
</blockquote>
</aside>
<p>Fixed.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the GUI is created in Qt Designer</p>
</blockquote>
</aside>
<p>But there’s only a QVTKWidget if system VTK is installed, not the like of qMRMLNodeComboBox.</p>

---

## Post #7 by @lassoan (2020-07-02 19:37 UTC)

<p>To see all the Slicer and CTK widgets, launch Qt designer by clicking on “Edit UI” button in the module’s “Reload &amp; Test section”.</p>

---

## Post #8 by @chir.set (2020-07-03 06:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>launch Qt designer by clicking on “Edit UI” button</p>
</blockquote>
</aside>
<p>I get ‘designer-real missing’ message. This is home built Slicer, and designer-real is missing in the SuperBuild tree. This file does exist in factory packages. What config switch do I have to use to get it built ? Thanks.</p>

---

## Post #9 by @lassoan (2020-07-03 19:01 UTC)

<p>Qt designer can be launched correctly in the build tree on Windows, but maybe there are issues on Linux or Mac. You can also try launching it using <code>./Slicer --designer</code>. It would be great if you could investigate the issue and maybe even come up with a fix.</p>
<p>In the meantime, you can download and use an official Slicer build to run Qt Designer.</p>

---

## Post #10 by @chir.set (2020-07-03 19:50 UTC)

<p>I’m using as a workaround :</p>
<blockquote>
<p>./Slicer --launch konsole<br>
"# In the new terminal<br>
designer-qt5</p>
</blockquote>
<p>Then I have all CTK, VTK, MRML widgets.</p>
<p>Will investigate when possible. First, I’ll rebase the module on a .ui file.</p>

---

## Post #11 by @chir.set (2020-07-07 14:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the GUI is created in Qt Designer instead of manual scripting.</p>
</blockquote>
</aside>
<p>I updated the GUI part of the module on Qt Designer. If you deem it worthwhile, I’ll delve into the pull request.</p>

---

## Post #12 by @chir.set (2020-07-14 14:25 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>a plane perpendicular to the centreline</p>
</blockquote>
</aside>
<p>Not exactly what I thought of but quite near, this <a href="https://github.com/chir-set/PathReformat" rel="noopener nofollow ugc">module</a> can move a 2D view perpendicular to a centerline. What puzzles me is the amount of rotation in the 2D view when the path is convoluted. We won’t have these rotations with Curve Planar Reformat.</p>
<p>Just saying, might be useful.</p>
<p>N.B : it has nothing to do with metrics.</p>

---

## Post #13 by @lassoan (2022-05-09 13:52 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="12" data-topic="12203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>this <a href="https://github.com/chir-set/PathReformat">module </a> can move a 2D view perpendicular to a centerline</p>
</blockquote>
</aside>
<p>The module is available in VMTK extension now, it is called <code>Cross-Section Analysis</code>. See its <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md">documentation</a>) for some more information.</p>

---
