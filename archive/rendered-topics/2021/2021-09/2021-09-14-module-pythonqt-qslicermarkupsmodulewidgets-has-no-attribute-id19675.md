# Module 'PythonQt.qSlicerMarkupsModuleWidgets' has no attribute 'qMRMLMarkupsROIWidget'?

**Topic ID**: 19675
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/module-pythonqt-qslicermarkupsmodulewidgets-has-no-attribute-qmrmlmarkupsroiwidget/19675

---

## Post #1 by @jumbojing (2021-09-14 21:14 UTC)

<p>Why?howto use qMRMLMarkupsROIWidget by python?</p>
<blockquote>
<p>[CRITICAL][Stream] 15.09.2021 04:43:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: module ‘PythonQt.qSlicerMarkupsModuleWidgets’ has no attribute ‘qMRMLMarkupsROIWidget’</p>
</blockquote>

---

## Post #2 by @jamesobutler (2021-09-14 21:17 UTC)

<p>If trying to instantiate a reference to a <code>qSlicerMarkupsROIWidget</code> object you should do the following from python. Things should not be accessed through the “PythonQt” namespace. Use “slicer” instead.</p>
<pre><code class="lang-python">roi_widget = slicer.qSlicerMarkupsROIWidget()
</code></pre>

---

## Post #3 by @jumbojing (2021-09-14 21:26 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="2" data-topic="19675">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40e8514d767dca90a817dddc39461c1a0344b23.png" data-download-href="/uploads/short-url/pGR3iWjBMN8p36vWobZJLDemxp1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b40e8514d767dca90a817dddc39461c1a0344b23_2_690x96.png" alt="image" data-base62-sha1="pGR3iWjBMN8p36vWobZJLDemxp1" width="690" height="96" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b40e8514d767dca90a817dddc39461c1a0344b23_2_690x96.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b40e8514d767dca90a817dddc39461c1a0344b23_2_1035x144.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b40e8514d767dca90a817dddc39461c1a0344b23_2_1380x192.png 2x" data-dominant-color="E3DFD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1686×236 36.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><code>roi_widget = slicer.qSlicerMarkupsROIWidget()</code></p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8391b9746ca5d6c92f67c0dd67ef6e6b6eb69502.png" data-download-href="/uploads/short-url/iLULeiWWYR5XcEC8uIjYrKbOiLU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8391b9746ca5d6c92f67c0dd67ef6e6b6eb69502.png" alt="image" data-base62-sha1="iLULeiWWYR5XcEC8uIjYrKbOiLU" width="690" height="69" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×100 3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Where is the ROIwidget?</p>

---

## Post #4 by @jamesobutler (2021-09-14 22:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Is there something wrong with <code>qSlicer</code> type widgets? <code>qSlicerMarkupsROIWidget</code> and <code>qSlicerVolumeRenderingModuleWidget</code> don’t appear to show anything?</p>
<p>When <code>qSlicerMarkupsROIWidget</code> was <code>qMRMLMarkupsROIWidget</code> prior to <a href="https://github.com/Slicer/Slicer/commit/13dc27c8dbc424ce6c0d14b90e9cbf4d213519e1" rel="noopener nofollow ugc">this commit</a> in Slicer 4.11.20210226 it can be shown successfully.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17d43256e3ab73dd83ccca6cc91ae00692d26c2e.png" alt="image" data-base62-sha1="3oNBSLsLwYC4MmIrD4Vys8mE87Y" width="384" height="234"></p>
<p>In latest Slicer Preview it is just blank<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb06b70543f87b44af774e79509de1537fa75f54.png" alt="image" data-base62-sha1="xx8AItbNKOWRbPyNc9n3IwA4oq8" width="402" height="333"></p>

---

## Post #5 by @jumbojing (2021-09-14 22:50 UTC)

<p>In latest Slicer Preview it is just blank？？？</p>

---

## Post #6 by @lassoan (2021-09-15 01:09 UTC)

<p>Good catch. We did not notice this design error during the recent markups module rework. There are several issues, I’ve summarized them in <a href="https://github.com/Slicer/Slicer/issues/5857">here</a>. <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is there a chance that you can work on this before finalizing Slicer5 (in the next 2 weeks or so)?</p>

---

## Post #7 by @RafaelPalomar (2021-09-21 08:06 UTC)

<p>Hello. Yes I will have a look at it.</p>

---

## Post #8 by @RafaelPalomar (2021-09-21 19:16 UTC)

<p>Thank you <a class="mention" href="/u/jumbojing">@jumbojing</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for reporting and giving insight on this issue. Here are my findings on this issue.</p>
<p>The idea behind <code>qSlicerMarkupsROIWidget</code> (as well as other qSlicerMarkups widgets) was to make it an “optional” widget that will show only when the relevant markup is selected. This avoids filling up the Markups module interface with widgets unusable in the context of the current markup (e.g., a ROI widget does not make sense for a line markup).</p>
<p>Much of this behavior is driven by the <code>qSlicerMarkupsROIWidget</code> itself (e.g., here the widget is set invisible by default <a href="https://github.com/Slicer/Slicer/blob/022a4f1a347ebb24509a50f6c8928ae26d3c5955/Modules/Loadable/Markups/Widgets/qSlicerMarkupsROIWidget.cxx#L72" class="inline-onebox" rel="noopener nofollow ugc">Slicer/qSlicerMarkupsROIWidget.cxx at 022a4f1a347ebb24509a50f6c8928ae26d3c5955 · Slicer/Slicer · GitHub</a>), which makes it less usable as an independent component. I think it is possible to translate the coordination of this behavior up to <code>qSlicerMarkupsModuleWidget</code> widget and leave <code>qSlicerMarkupsROIWidget</code> as a more independent component. <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, let me know your thoughts on this approach; I think I can handle this in the coming days, before the release of Slicer5.</p>

---

## Post #9 by @lassoan (2021-09-21 22:06 UTC)

<p>Adding markups option widgets is good. But these widgets should not replace the reusable high-level widgets, but they should show one or more of these high-level widgets.</p>

---

## Post #10 by @lassoan (2021-09-22 00:38 UTC)

<p>A post was split to a new topic: <a href="/t/get-oriented-bounding-boxes-for-each-segment/19796">Get oriented bounding boxes for each segment</a></p>

---

## Post #12 by @RafaelPalomar (2021-09-30 19:42 UTC)

<p>There is a PR (<a href="https://github.com/Slicer/Slicer/pull/5921" class="inline-onebox" rel="noopener nofollow ugc">Refactor markups qt widgets by RafaelPalomar · Pull Request #5921 · Slicer/Slicer · GitHub</a>) on this now.</p>

---
