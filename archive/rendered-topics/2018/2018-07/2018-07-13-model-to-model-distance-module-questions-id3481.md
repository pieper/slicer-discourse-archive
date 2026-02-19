---
topic_id: 3481
title: "Model To Model Distance Module Questions"
date: 2018-07-13
url: https://discourse.slicer.org/t/3481
---

# Model-to-model distance module questions

**Topic ID**: 3481
**Date**: 2018-07-13
**URL**: https://discourse.slicer.org/t/model-to-model-distance-module-questions/3481

---

## Post #1 by @aseman (2018-07-13 20:01 UTC)

<p>Operating system:<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
hello 3D slicer experts, I made two models and calculated the distance between them with the model to model distance module , then I  ran it’s vtk output file in shapepopulationviewer module.it gives me a colour bar.<br>
1)what is the scale of this colour bar?<br>
2) how to calibrate the colour bar, so that the scale of this colour bar shows the actual distance between the points of two models?<br>
thank you</p>

---

## Post #2 by @lassoan (2018-07-14 17:08 UTC)

<p>You can edit color map range and show it in 3D view in Colors module.</p>

---

## Post #3 by @bjoern (2019-06-07 20:10 UTC)

<p>Hello everyone,</p>
<p>I am trying to calculate distances between two and also between more than two models in Slicer 4.10.2 .</p>
<p>The segment comparison module does not help me.</p>
<p>When use the Model To Model Distance module, I get an error. Please find the error message below.</p>
<p>Does anyone have an idea, why this doesn’t work?</p>
<p>Or does anyone know a better and working way to calculate distances?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59bf7dcfbdeef77101d4b69c0f559094640ed5d3.png" data-download-href="/uploads/short-url/cNWLkyqFNffWjfpIn5fFvWDtuV5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bf7dcfbdeef77101d4b69c0f559094640ed5d3_2_690x339.png" alt="image" data-base62-sha1="cNWLkyqFNffWjfpIn5fFvWDtuV5" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bf7dcfbdeef77101d4b69c0f559094640ed5d3_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59bf7dcfbdeef77101d4b69c0f559094640ed5d3_2_1035x508.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59bf7dcfbdeef77101d4b69c0f559094640ed5d3.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1068×526 23.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Model To Model Distance standard error:</p>
<p>dyld: Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtSql.framework/Versions/5/QtSql</p>
<p>Referenced from: /Applications/Slicer.app/Contents/Extensions-28257/ModelToModelDistance/lib/Slicer-4.10/cli-modules/libModelToModelDistanceLib.dylib</p>
<p>Reason: image not found</p>

---

## Post #4 by @lassoan (2019-06-07 20:26 UTC)

<aside class="quote no-group" data-username="bjoern" data-post="3" data-topic="3481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/46a35a/48.png" class="avatar"> bjoern:</div>
<blockquote>
<p>The segment comparison module does not help me.</p>
</blockquote>
</aside>
<p>What do you mean? What do you do, what do you expect to happen, and what happens instead?</p>
<aside class="quote no-group" data-username="bjoern" data-post="3" data-topic="3481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/46a35a/48.png" class="avatar"> bjoern:</div>
<blockquote>
<p>When use the Model To Model Distance module, I get an error. Please find the error message below.</p>
</blockquote>
</aside>
<p>I’ve just tried it and it works fine on Windows. Try uninstalling and installing the extension again (make sure to wait for the “Restart” button to appear, then press it to restart Slicer).</p>

---

## Post #5 by @fedorov (2019-06-13 21:43 UTC)

<p>It does not work on mac - the error is below.</p>
<p>cc:<a class="mention" href="/u/fbudin69500">@fbudin69500</a></p>
<pre><code class="lang-auto">Model To Model Distance standard error:

dyld: Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtSql.framework/Versions/5/QtSql
  Referenced from: /Applications/Slicer-4.10.2.app/Contents/Extensions-28257/ModelToModelDistance/lib/Slicer-4.10/cli-modules/libModelToModelDistanceLib.dylib
  Reason: image not found
</code></pre>

---

## Post #6 by @fedorov (2019-06-18 18:56 UTC)

<p>I was going to submit an issue about this so it is documented somewhere other than this forum, but then I got confused about the source code location.</p>
<p>ExtensionIndex points to the fork of the code under <a class="mention" href="/u/jcfr">@jcfr</a> account: <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/ModelToModelDistance.s4ext#L9" rel="nofollow noopener">https://github.com/Slicer/ExtensionsIndex/blob/master/ModelToModelDistance.s4ext#L9</a></p>
<p>However, the <a class="mention" href="/u/jcfr">@jcfr</a> version does not allow submission of issues: <a href="https://github.com/jcfr/3dmetrictools" rel="nofollow noopener">https://github.com/jcfr/3dmetrictools</a>. Also, the one from which <a class="mention" href="/u/jcfr">@jcfr</a> forked the repo is 18 commits behind the one under GitHub NIRALUser: <a href="https://github.com/NIRALUser/3DMetricTools" rel="nofollow noopener">https://github.com/NIRALUser/3DMetricTools</a>.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> do you know what is going on with this extension?</p>
<p>It sounds like a basic functionality, but for clinical researchers this functionality can actually be quite useful (if it works).</p>

---

## Post #7 by @lassoan (2019-06-18 19:09 UTC)

<p>We need to fix the module (or add another one that works) but in the meantime, you can get model to model distance by typing 5 lines of code:</p>
<pre><code class="lang-python"># Get two model nodes that we want to compute distances of
m1=getNode('Segment_1')
m2=getNode('Segment_2')

# Compute distance
distanceFilter = vtk.vtkDistancePolyDataFilter()
distanceFilter.SetInputData(0, m1.GetPolyData())
distanceFilter.SetInputData(1, m2.GetPolyData())
distanceFilter.Update()
m1.SetAndObservePolyData(distanceFilter.GetOutput())

# Use the computed distance to color the node
m1.GetDisplayNode().SetActiveScalarName('Distance')
m1.GetDisplayNode().SetScalarVisibility(True)
</code></pre>

---

## Post #8 by @fedorov (2019-06-18 19:30 UTC)

<p>Hope this helps <a class="mention" href="/u/bjoern">@bjoern</a></p>

---

## Post #9 by @lassoan (2021-06-27 03:05 UTC)

<p>5 posts were merged into an existing topic: <a href="/t/combining-module-functionalities/18347/2">Combining Module Functionalities</a></p>

---
