---
topic_id: 23181
title: "Exporting Curvature Data"
date: 2022-04-28
url: https://discourse.slicer.org/t/23181
---

# Exporting Curvature Data

**Topic ID**: 23181
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/exporting-curvature-data/23181

---

## Post #1 by @heiko (2022-04-28 16:47 UTC)

<p>Hello everyone,</p>
<p>I am using the Slicer VMTK extension in order to extract centerlines from a vascular tree. In addition to radius, I would also like to have the curvature at every point of the centerline (like I would get from “vmtkcenterlinegeometry” command using VMTK alone).<br>
So far I found that the markups module internally calculates the curvature of an extracted centerline curve (which it uses to find the curvature  mean and max measurements and also to color the centerline when chosen as active scalar). Unfortunately I cannot find a way to export these values. Whichever way of saving I choose (e.g. as Markups JSON), it only contains curvature mean/curvature max and radius, but not a curvature value per point. Is there any way to export/save these values which slicer seemingly calculates internally already?</p>
<p>At the moment I am trying to look into the python interactor in order to try and get my hands on them, but as I am not familiar with the VTK framework I am having a hard time finding the measurement data.</p>
<p>Any help would be greatly appreciated!</p>

---

## Post #2 by @heiko (2022-08-24 16:23 UTC)

<p>No one has an idea for this?</p>
<p>I found out that I can access scalar data (the PedigreeIDs) of the markups curve using</p>
<pre><code class="lang-auto">res = slicer.util.arrayFromMarkupsCurveData(node, "PedigreeIDs")
</code></pre>
<p>but it does not work for curvature data:</p>
<pre><code class="lang-auto">res = slicer.util.arrayFromMarkupsCurveData(node, "Curvature")
</code></pre>
<p>always gives <em><strong>ValueError: Input markupsNode does not contain curve point data array ‘Curvature’. Available array names: ‘PedigreeIDs’</strong></em></p>
<p>I do know the curvature values must be stored somewhere though, as I can use them as active scalar on display:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745e1e32e70b142dabbad4cb457214f0eafc125e.png" data-download-href="/uploads/short-url/gBr24juoDjRJwru6iYXTZoQvb8W.png?dl=1" title="slicer_forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745e1e32e70b142dabbad4cb457214f0eafc125e_2_690x366.png" alt="slicer_forum" data-base62-sha1="gBr24juoDjRJwru6iYXTZoQvb8W" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745e1e32e70b142dabbad4cb457214f0eafc125e_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745e1e32e70b142dabbad4cb457214f0eafc125e_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745e1e32e70b142dabbad4cb457214f0eafc125e_2_1380x732.png 2x" data-dominant-color="B8BED6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_forum</span><span class="informations">1563×831 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could anyone give me a hint on what to look into?</p>

---

## Post #3 by @heiko (2022-08-24 16:28 UTC)

<p>I was almost there…<br>
Found out that I was missing one argument to get the Curvature data, which was setting the ‘world’ parameter to True:</p>
<pre><code class="lang-auto">res = slicer.util.arrayFromMarkupsCurveData(node, "Curvature", world=True)
</code></pre>
<p>Maybe someone else can profit from this knowledge. The question can be marked as solved.</p>

---

## Post #4 by @pieper (2022-08-24 17:10 UTC)

<p>Good to hear you were able to sort this out.  I hadn’t used the feature myself but I see the documentation mentioned that flag.  Maybe you didn’t have a chance to look or it wasn’t clear?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsCurveData" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsCurveData</a></p>

---

## Post #5 by @lassoan (2022-08-28 12:09 UTC)

<p>Curvature measurement is a dynamic measurement, computed only in world space, so it is not stored in the markup file. However, you can easily get the curve measurements from the markup node using <code>arrayFromMarkupCurveData</code> after you enabled curvature computation:</p>
<pre data-code-wrap="python"><code class="lang-python">curveNode = getNode('OC')
curveNode.GetMeasurement('curvature mean').SetEnabled(True)
curvature = arrayFromMarkupsCurveData(curveNode, "Curvature", world=True)
plot(curvature)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee3fe80cb8d19cc6093a9c406e135b07911d5b50.png" data-download-href="/uploads/short-url/xZEywGWrCqAi2qqnrSmLIsX8F9e.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3fe80cb8d19cc6093a9c406e135b07911d5b50_2_690x351.png" alt="image" data-base62-sha1="xZEywGWrCqAi2qqnrSmLIsX8F9e" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3fe80cb8d19cc6093a9c406e135b07911d5b50_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3fe80cb8d19cc6093a9c406e135b07911d5b50_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee3fe80cb8d19cc6093a9c406e135b07911d5b50.png 2x" data-dominant-color="C0C1DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×560 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @smoudour (2023-05-09 14:26 UTC)

<p>Hi <a class="mention" href="/u/heiko">@heiko</a> . I am trying to do the same thing – extract curvature data out of a coronary artery centerline network. I have two problems:<br>
<del>1) While I’m setting world = True, I still get the error message below</del></p>
<pre><code class="lang-auto">ValueError: Input markupsNode does not contain curve point data array 'Curvature'. Available array names: 'PedigreeIDs', 'Radius'
</code></pre>
<p><del> I’m using one of the many centerlines extracted. Could somebody point to a solution direction?</del><br>
I followed Andras Lasso approach in the last post and it worked. However I only got 4-5 points of curvature. How can I control this, for example increase the points?</p>
<ol start="2">
<li>Relevant to the last info, is there anyway to acquire the centerline as a whole, since I’m interested in studying it both segmented and not. I cannot seem to find the node that describes the centerline as a whole, all along the arterial tree.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/002ed4907120a980998232b57a8f2852a5944a29.png" data-download-href="/uploads/short-url/1CkG2tJhJ58o1LcT7VsNZO7VA5.png?dl=1" title="rca_sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002ed4907120a980998232b57a8f2852a5944a29_2_690x455.png" alt="rca_sample" data-base62-sha1="1CkG2tJhJ58o1LcT7VsNZO7VA5" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002ed4907120a980998232b57a8f2852a5944a29_2_690x455.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002ed4907120a980998232b57a8f2852a5944a29_2_1035x682.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/002ed4907120a980998232b57a8f2852a5944a29.png 2x" data-dominant-color="9998CC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rca_sample</span><span class="informations">1377×909 66.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2023-05-10 02:31 UTC)

<aside class="quote no-group" data-username="smoudour" data-post="6" data-topic="23181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smoudour/48/18451_2.png" class="avatar"> smoudour:</div>
<blockquote>
<p>I followed Andras Lasso approach in the last post and it worked. However I only got 4-5 points of curvature. How can I control this, for example increase the points?</p>
</blockquote>
</aside>
<p>You get as many points as points in the curve segment. If it is a very short segment then it may contain only 4-5 points. You can adjust sampling distance in Extract Centerline module / Advanced / Sampling distance.</p>
<aside class="quote no-group" data-username="smoudour" data-post="6" data-topic="23181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smoudour/48/18451_2.png" class="avatar"> smoudour:</div>
<blockquote>
<p>Relevant to the last info, is there anyway to acquire the centerline as a whole</p>
</blockquote>
</aside>
<p>You can get the entire centerline tree as a model (choose Extract Centerline module / Outputs / Centerline model) and compute the curvature using vtkvmtkCenterlineGeometry filter (see example <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/9f54874daff66aa68758113007045d1d84a084d1/ExtractCenterline/ExtractCenterline.py#L619C38-L633">here</a>).</p>

---

## Post #8 by @smoudour (2023-05-10 12:44 UTC)

<p>Hi Andras, thanks for the quick reply.</p>
<ol>
<li>
<p>I managed to increase the points, but I do get a weird result. One of my curves has curvature values of over 100, even reaches 2000+ on a point. All other curves seem to have normal values. Is there any explanation/intuition for this? I am not very familiar with the curvature measurement procedure in general.</p>
</li>
<li>
<p>I don’t exactly understand how to do this. Is there any tutorial to help get a hang of these python scripts on github describing the clasess and how can someone use them to construct code? For example, what I understand here is that I need to extract the centerline geometry from the model, but I cannot access the  ExtractCenterlineLogic class to set compute geometry into “True”.</p>
</li>
</ol>

---

## Post #9 by @lassoan (2023-05-12 04:40 UTC)

<aside class="quote no-group" data-username="smoudour" data-post="8" data-topic="23181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smoudour/48/18451_2.png" class="avatar"> smoudour:</div>
<blockquote>
<p>One of my curves has curvature values of over 100, even reaches 2000+ on a point</p>
</blockquote>
</aside>
<p>You need to use a smooth interpolation (e.g., spline) when resampling the curve. Otherwise you can have large values due to noise.</p>
<aside class="quote no-group" data-username="smoudour" data-post="8" data-topic="23181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smoudour/48/18451_2.png" class="avatar"> smoudour:</div>
<blockquote>
<p>I don’t exactly understand how to do this. Is there any tutorial to help get a hang of these python scripts on github describing the clasess</p>
</blockquote>
</aside>
<p>There are lots of tutorials online, but to get started, I would recommend the PerkLab Bootcamp <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">Slicer programming tutorial</a>.</p>

---

## Post #10 by @smoudour (2023-05-12 11:08 UTC)

<p>Thanks a bunch for the tutorial, will definitely look into.</p>
<blockquote>
<p>You need to use a smooth interpolation (e.g., spline) when resampling the curve. Otherwise you can have large values due to noise.</p>
</blockquote>
<p>That means I need to resample to even more points than at the beginning right? I can find the option of distance in resampling (Centerline module : curve sampling distance <em>mm</em>) but not an option to select interpolator. Do I need to do this programmatically? Can you suggest the python method I should use to do it? I found that by using</p>
<pre><code class="lang-auto">getNode('curveNode').ResampleCurveWorld(n)
</code></pre>
<p>n describes the number of points of resampling.</p>

---

## Post #11 by @lassoan (2023-05-12 15:28 UTC)

<p>For a smoother curve you need have less control points. If you less control points (or want more curve points sampled more densely along the curve) then you can call <code>curveNode.SetNumberOfPointsPerInterpolatingSegment(20)</code>. This value specifies how many curve points are added between each pair of control points. Default value is 10, the higher the number the more dense the sampling is.</p>

---

## Post #12 by @bserrano (2023-10-27 10:34 UTC)

<p>Hi,</p>
<p>I’m facing the same problem, so I tried this solution. The issue is that I want to calculate the curvature only at the centerline control points. How can I achieve that?</p>

---

## Post #13 by @smoudour (2023-10-27 12:24 UTC)

<p>Hi <a class="mention" href="/u/bserrano">@bserrano</a><br>
If you set the number of points per interpolating segment to 1, then you basically get a curvature measurement for n=control points.<br>
You can set the number of points per interpolating segment to 1 using:<br>
<code>curve_node.SetNumberOfPointsPerInterpolatingSegment(1)</code></p>
<p>To get number of control points per curve_node use:<br>
<code>curve_node.GetNumberOfControlPoints()</code></p>
<p>To get number of curvature points just measure length of curvature array:</p>
<pre><code class="lang-auto">curvature = arrayFromMarkupsCurveData(curve_node, "Curvature", world=True)
len(curvature)
</code></pre>
<p>I don’t know why you would want to do this though, because to get better curvature measurements you need a small number of control points and a large number of points per interpolating segment, at least that works for my case.<br>
In general, I found it very useful to visualize the curvature values as mentioned in this post <a href="https://discourse.slicer.org/t/separating-centerline-metrics/19173/9" class="inline-onebox">Separating centerline metrics - #9 by som1197</a></p>

---

## Post #15 by @bserrano (2023-10-27 13:06 UTC)

<p>Thank you so much.</p>
<p>I think you are right because I’m getting a quite erratic curve<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f924a3a6a0a5be6d4e8bafca7d4576de43543fd7.png" data-download-href="/uploads/short-url/zy1o8Qe6I4JKSfikkPF7bULYcdN.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f924a3a6a0a5be6d4e8bafca7d4576de43543fd7_2_689x165.png" alt="imagen" data-base62-sha1="zy1o8Qe6I4JKSfikkPF7bULYcdN" width="689" height="165" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f924a3a6a0a5be6d4e8bafca7d4576de43543fd7_2_689x165.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f924a3a6a0a5be6d4e8bafca7d4576de43543fd7_2_1033x247.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f924a3a6a0a5be6d4e8bafca7d4576de43543fd7.png 2x" data-dominant-color="F6F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1283×307 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @smoudour (2023-10-27 13:26 UTC)

<p>I see. To be honest, values are kind of ok - I sometimes get values of the thousands or something, which really don’t make sense! Maybe try and lower the number of control points &amp; increase number of points per interpolating segment.</p>
<p>By the way, is that the centerline of a coronary artery? Curious because I’m working on such a project.</p>

---

## Post #17 by @bserrano (2023-10-30 07:35 UTC)

<p>I’ll try. Many thanks.</p>
<p>Yes, it’s a coronary vessel.</p>

---

## Post #18 by @smoudour (2023-10-30 10:14 UTC)

<p>Could you describe the process which you followed to get the centerline curve? Because I’m only able to get network curve on the coronary vessels I’m studying. I’m using CCTA scans as an input. My curvature centerlines produced are full of artifacts and straight lines.</p>

---

## Post #19 by @bserrano (2023-10-30 11:03 UTC)

<p>Are you using the extract centerlines module? You can try the option “tree” instead of “network”. You need to be careful placing the control points and avoid sharpening geometries</p>

---

## Post #20 by @smoudour (2023-10-30 13:23 UTC)

<p>Yes, I’m using both options. What happens is, while I’m getting an adequate representation on the network option, centerlines are completely off.<br>
See: <a href="https://discourse.slicer.org/t/centerline-computation-problem-straight-lines/32397" class="inline-onebox">Centerline computation problem - straight lines</a></p>
<p>If you do have any suggestions it would be great!</p>

---

## Post #21 by @bserrano (2023-10-31 08:45 UTC)

<p>Uhm, I think that the coronary segments are “too” smooth and too thin in some cases.<br>
Which version of slicer are you using?</p>

---

## Post #22 by @smoudour (2023-10-31 08:52 UTC)

<p>I’m using version 5.4.0. Considering vessel thickness, I think this is the best I can do after processing the CCTA scans with Vesselness Filtering and Segment Editor to isolate the vessels. If I decrease the threshold (to capture more detail) I get a lot of artifacts.</p>

---

## Post #23 by @bserrano (2023-10-31 08:59 UTC)

<p>Have you tried local threshold in segment editor? It requires a bit of manual post processing anyway but depending on the image you can achieve good results</p>

---

## Post #24 by @smoudour (2023-10-31 09:00 UTC)

<p>I used generic threshold functionality and then isolated segmnes using the islands tool. Do you think local threshold does a better job? I will give it a try, thanks!</p>

---

## Post #25 by @bserrano (2023-10-31 09:26 UTC)

<p>Maybe it’s just a visualization thing but try to turn off smoothing<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4e625086b24af69e4ce9f6c22019c1620e6d3f6.png" alt="imagen" data-base62-sha1="unoiZMoMFoTV7U6FhLM0dFBBORg" width="364" height="105"></p>

---

## Post #26 by @mssm (2024-08-06 06:03 UTC)

<p>Thanks everyone.</p>
<p>This thread was very helpful to me.<br>
Thanks to you, I was able to print the list of curvature values ​​in the Python console.<br>
But it would have been nice to be able to export it as a CSV or xlxs file. It’s kind of tedious to copy the listed numbers from the Python console and put carriage returns between the numbers.<br>
Does anyone have a good idea to export the curvature list in an Excel compatible format?</p>
<p>Regards,</p>

---
