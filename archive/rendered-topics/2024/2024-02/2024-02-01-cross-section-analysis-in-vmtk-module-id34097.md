# Cross section analysis in VMTK module

**Topic ID**: 34097
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/cross-section-analysis-in-vmtk-module/34097

---

## Post #1 by @michaelli (2024-02-01 20:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0510361618b1a688ccbdb35b9c1178c8040cac4.png" data-download-href="/uploads/short-url/mSdXQt2OGIDnIFwDpJr7UyEN0LG.png?dl=1" title="Screenshot_20240113_152913" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0510361618b1a688ccbdb35b9c1178c8040cac4_2_690x450.png" alt="Screenshot_20240113_152913" data-base62-sha1="mSdXQt2OGIDnIFwDpJr7UyEN0LG" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0510361618b1a688ccbdb35b9c1178c8040cac4_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0510361618b1a688ccbdb35b9c1178c8040cac4_2_1035x675.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0510361618b1a688ccbdb35b9c1178c8040cac4_2_1380x900.png 2x" data-dominant-color="B2B5D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20240113_152913</span><span class="informations">1804×1178 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I can convert a cross section and convert to a segmentation and then convert it back to a model; then go to the next cross section by browsing in the cross sectional analysis module. Finally, I can save them to STL. This is tedious. Is there is way to export multiple cross sections at a time? Say, I want to resample the centerline to have 20 control points, then export all the cross sections at these control points.</p>
<p>Also, how to get the center (coordinates) of a cross section?</p>

---

## Post #2 by @chir.set (2024-02-01 21:01 UTC)

<aside class="quote no-group" data-username="michaelli" data-post="1" data-topic="34097">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michaelli/48/67910_2.png" class="avatar"> michaelli:</div>
<blockquote>
<p>Is there is way to export multiple cross sections at a time?</p>
</blockquote>
</aside>
<p>If I have fully understood your requirements, this step can be done through scripting. A good start is as follows:</p>
<pre><code class="lang-auto">import CrossSectionAnalysis
logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()
centerline = getNode("Centerline curve (0)")
segmentation = getNode("Segmentation")
logic.setInputCenterlineNode(centerline)
logic.setLumenSurface(segmentation, "Segment_1")
logic.run()
for i in range(20):
    crossSectionPolyData = logic.computeCrossSectionPolydata(i)
    # Add your export code to STL here
</code></pre>
<p>You must add more code to export the crossSectionPolyData to STL.</p>
<aside class="quote no-group" data-username="michaelli" data-post="1" data-topic="34097">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michaelli/48/67910_2.png" class="avatar"> michaelli:</div>
<blockquote>
<p>how to get the center (coordinates) of a cross section?</p>
</blockquote>
</aside>
<p>For me, ‘centre’ refers to a regular geometry, like circle, rectangle, cube… Do you mean the control point coordinates of your resampled curve? They are available in the ‘Markups’ module.</p>

---

## Post #3 by @michaelli (2024-02-01 22:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5cedbcbc0ee38343ece42f08abda8c24e0c5623.png" data-download-href="/uploads/short-url/z4waHVL3JIpMyNujuldKmg0RAQz.png?dl=1" title="Screenshot_20240201_165426" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5cedbcbc0ee38343ece42f08abda8c24e0c5623_2_480x500.png" alt="Screenshot_20240201_165426" data-base62-sha1="z4waHVL3JIpMyNujuldKmg0RAQz" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5cedbcbc0ee38343ece42f08abda8c24e0c5623_2_480x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5cedbcbc0ee38343ece42f08abda8c24e0c5623_2_720x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5cedbcbc0ee38343ece42f08abda8c24e0c5623_2_960x1000.png 2x" data-dominant-color="C8CBE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20240201_165426</span><span class="informations">1180×1228 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/chir.set">@chir.set</a>, thank you so much! Your method seems promising. I’m not familiar with script, but I get your code run in the python console and it seems working. Can you tell me how to export crossSectionPolyData to STL, how to convert them to models so that I can view them in Slicer?</p>
<p>For the second question about the center, if the sections are exactly extracted at the centerline control points, then I can get the coordinates from the centerline table.</p>

---

## Post #4 by @michaelli (2024-02-01 22:01 UTC)

<p>As you can see in the snapshot, I have the centerline extracted and resampled.</p>

---

## Post #5 by @chir.set (2024-02-01 22:33 UTC)

<aside class="quote no-group" data-username="michaelli" data-post="3" data-topic="34097">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michaelli/48/67910_2.png" class="avatar"> michaelli:</div>
<blockquote>
<p>convert them to models</p>
</blockquote>
</aside>
<p>To create a model from polydata:</p>
<p><code>model = slicer.modules.models.logic().AddModel(crossSectionPolyData)</code></p>
<p>As for the STL thing, I’m not familiar with it. May be someone else could kick in.</p>

---

## Post #6 by @michaelli (2024-02-01 22:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ead32637a5d3d3ea4277ab2636a3848cfeca450.png" data-download-href="/uploads/short-url/mDIvNjrP5WNt5E8uO9zDXFe1eJW.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ead32637a5d3d3ea4277ab2636a3848cfeca450_2_690x454.png" alt="1" data-base62-sha1="mDIvNjrP5WNt5E8uO9zDXFe1eJW" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ead32637a5d3d3ea4277ab2636a3848cfeca450_2_690x454.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ead32637a5d3d3ea4277ab2636a3848cfeca450_2_1035x681.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ead32637a5d3d3ea4277ab2636a3848cfeca450_2_1380x908.png 2x" data-dominant-color="B6BBCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1866×1228 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Cool. I got 20 cross sections in a second. Unfortunately, they are not at the control points. Did I miss something with my centerline curve? I just resampled it to have 20 control points.</p>

---

## Post #7 by @chir.set (2024-02-02 07:49 UTC)

<aside class="quote no-group" data-username="michaelli" data-post="6" data-topic="34097">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michaelli/48/67910_2.png" class="avatar"> michaelli:</div>
<blockquote>
<p>Did I miss something with my centerline curve?</p>
</blockquote>
</aside>
<p>Not really, the code works on curve points while you are expecting a result at control points. The update below should do:</p>
<pre><code class="lang-auto">import CrossSectionAnalysis
logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()
centerline = getNode("Centerline curve (0)")
segmentation = getNode("Segmentation")
logic.setInputCenterlineNode(centerline)
logic.setLumenSurface(segmentation, "Segment_1")
logic.run()
numberOfControlPoints = centerline.GetNumberOfControlPoints()
controlPointCoordinates = [0.0, 0.0, 0.0]
for i in range(numberOfControlPoints):
    centerline.GetNthControlPointPositionWorld(i, controlPointCoordinates)
    pointId = centerline.GetCurveWorld().FindPoint(controlPointCoordinates)
    crossSectionPolyData = logic.computeCrossSectionPolydata(pointId)
    model = slicer.modules.models.logic().AddModel(crossSectionPolyData)
</code></pre>

---

## Post #8 by @michaelli (2024-02-02 13:40 UTC)

<p>I really appreciate your great help. It works perfectly. I got the cross sections at the desired positions.</p>
<p>I would like to share the complete code with renaming and saving the models here in case it is of interest to other people.</p>
<pre><code class="lang-auto">import CrossSectionAnalysis
logic = CrossSectionAnalysis.CrossSectionAnalysisLogic()
centerline = getNode("Centerline curve (0)")
segmentation = getNode("Segmentation")
logic.setInputCenterlineNode(centerline)
logic.setLumenSurface(segmentation, "Segment_1")
logic.run()
numberOfControlPoints = centerline.GetNumberOfControlPoints()
controlPointCoordinates = [0.0, 0.0, 0.0]
for i in range(numberOfControlPoints):
    centerline.GetNthControlPointPositionWorld(i, controlPointCoordinates)
    pointId = centerline.GetCurveWorld().FindPoint(controlPointCoordinates)
    crossSectionPolyData = logic.computeCrossSectionPolydata(pointId)
    model = slicer.modules.models.logic().AddModel(crossSectionPolyData)
    
    model.SetName(f"Secion{i}")
    
    filename = os.path.basename(model.GetName())
    filepath =  filename + ".stl"
    slicer.util.exportNode(model, filepath)    
</code></pre>

---
