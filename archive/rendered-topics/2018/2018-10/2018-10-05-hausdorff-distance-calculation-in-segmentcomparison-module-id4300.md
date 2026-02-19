---
topic_id: 4300
title: "Hausdorff Distance Calculation In Segmentcomparison Module"
date: 2018-10-05
url: https://discourse.slicer.org/t/4300
---

# Hausdorff distance calculation in SegmentComparison module

**Topic ID**: 4300
**Date**: 2018-10-05
**URL**: https://discourse.slicer.org/t/hausdorff-distance-calculation-in-segmentcomparison-module/4300

---

## Post #1 by @fedorov (2018-10-05 14:56 UTC)

<p>Currently, Hausdorff distance calculation in Segment Comparison is unsigned - switching the order of segments used for comparison does not change the result of calculation. It is often critical to know the sign of the distance. For example, if I want to quantify the coverage of the tumor area given the defined ablation region, unsigned HD of 5 mm does not tell me whether tumor region is sticking out of the ablated zone by 5 mm, or there is a 5 mm safety margin that was ablated around the tumor.</p>
<p>I looked at the source code of SegmentComparison, which pointed me to the <a href="https://gitlab.com/plastimatch/plastimatch/blob/master/src/plastimatch/util/hausdorff_distance.cxx">plastimatch filter</a> implementing the calculation. If I understand correctly, the algorithm is to calculate <em>signed</em> distance map for the second label, identify boundary for the first label, and then iterate over the boundary pixels to calculate HD metrics. However, in <a href="https://gitlab.com/plastimatch/plastimatch/blob/master/src/plastimatch/util/hausdorff_distance.cxx#L177-183">this loop</a> effectively the absolute of the distances is taken, and so points inside and outside the label boundary are treated the same way.</p>
<p>I wonder if I am missing something in how the module should be used, since it is part of SlicerRT, and I would think that in radiation therapy this question of directionality should also be quite important.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/gcsharp">@gcsharp</a> can you share your thoughts on this, and the intent behind reporting HD in SegmentComparison and <code>plastimatch dice</code> as it is reported now? Is the use case I have in mind too distant from the RT applications?</p>
<p>cc: <a class="mention" href="/u/kmacneil0102">@Kmacneil0102</a></p>

---

## Post #2 by @fedorov (2018-10-05 15:32 UTC)

<p>To further illustrate my point, here’s an example <a href="https://www.dropbox.com/s/sa7rejcgcqr0ipm/tumor.nrrd?dl=0">“tumor”</a> and <a href="https://www.dropbox.com/s/aly83s8ojm260yq/ablation.nrrd?dl=0">“ablation”</a> datasets:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5eb6ef0c38adb6b7c0092af475da271192f1952d.png" alt="image" data-base62-sha1="dvSOAQTeNQyQP0DDYrndMNUnaIR" width="291" height="225"></p>
<p>Symmetric distance reported by plastimatch (same filter as used by SegmentComparison - no direction considered):</p>
<pre data-code-wrap="bash"><code class="lang-bash">$ plastimatch dice --hausdorff tumor.nrrd ablation.nrrd                                                        
Hausdorff distance = 12.079405
Avg average Hausdorff distance = 2.225087
Max average Hausdorff distance = 4.450174
Percent (0.95) Hausdorff distance = 5.149281
Hausdorff distance (boundary) = 12.079405
Avg average Hausdorff distance (boundary) = 2.441764
Max average Hausdorff distance (boundary) = 4.633363
Percent (0.95) Hausdorff distance (boundary) = 6.916576

$ plastimatch dice --hausdorff ablation.nrrd tumor.nrrd                                                        
Hausdorff distance = 12.079405
Avg average Hausdorff distance = 2.225087
Max average Hausdorff distance = 4.450174
Percent (0.95) Hausdorff distance = 5.149281
Hausdorff distance (boundary) = 12.079405
Avg average Hausdorff distance (boundary) = 2.441764
Max average Hausdorff distance (boundary) = 4.633363
Percent (0.95) Hausdorff distance (boundary) = 6.916576
</code></pre>
<p>Signed distance calculated with <code>itk.DirectedHausdorffDistanceImageFilter</code> - I think this is the one that often is needed for volume coverage applications:</p>
<pre data-code-wrap="bash"><code class="lang-bash">$ python itk_hd.py                                                                                             
Ablation to tumor: 12.079405
Tumor to ablation: 0.000000
</code></pre>
<p><code>itk_hd.py</code> script:</p>
<pre data-code-wrap="python"><code class="lang-python">import itk

tumor=itk.imread('tumor.nrrd')
ablation=itk.imread('ablation.nrrd')

a2t = itk.DirectedHausdorffDistanceImageFilter.New(ablation,tumor)
t2a = itk.DirectedHausdorffDistanceImageFilter.New(tumor,ablation)

a2t.Update()
t2a.Update()

print('Ablation to tumor: %f' % (a2t.GetDirectedHausdorffDistance()))
print('Tumor to ablation: %f' % (t2a.GetDirectedHausdorffDistance()))
</code></pre>

---

## Post #3 by @cpinter (2018-10-05 15:52 UTC)

<p>Interesting question. I’ll let <a class="mention" href="/u/gcsharp">@gcsharp</a> answer the original question, as I’m not familiar with the depths of all the RT applications enough to be able to answer this. I haven’t had the need for a signed distance yet, so this has been fine for our use cases.</p>
<p>Do you need the signed distance for a specific use case? If yes, can you describe it?</p>
<p>Based on the <a href="https://en.wikipedia.org/wiki/Hausdorff_distance">definition</a> of Hausdorff distance, it seems to me that it is unsigned by definition (and probably that’s why you get a 0 from ITK too). If you want a signed Hausdorff, then I think that if I’m right in this, then instead of tweaking the current Hausdorff class, a new SignedHausdorff class should be created if needed.</p>

---

## Post #4 by @fedorov (2018-10-05 16:04 UTC)

<p>The one calculated by ITK is directed, see definition here: <a href="https://itk.org/Doxygen/html/classitk_1_1DirectedHausdorffDistanceImageFilter.html">https://itk.org/Doxygen/html/classitk_1_1DirectedHausdorffDistanceImageFilter.html</a>.</p>
<p>The specific use case is evaluation of the coverage of the planned ablation zone with the actual ablated region. I need to be able to differentiate between the tumor edge being at the distance inside or outside the ablation zone (like in the example I showed in my previous post). I had a student working on a project, and I realized he was using SegmentComparison and reporting HDs, but interpretation of the distance between segments inside and outside is very important in that particular use case, and it was not provided by the module.</p>
<p>Did you intend SegmentComparison to be used for the evaluation of agreement between segmentations done by different readers/tools? Is there any other tool in SlicerRT to help with the task of evaluating quality of coverage of the planned treatment region by a certain dose contour?</p>

---

## Post #5 by @cpinter (2018-10-05 16:17 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>The one calculated by ITK is directed</p>
</blockquote>
</aside>
<p>Directed, yes. Signed, no. As I understood you wanted a signed distance.</p>
<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>help with the task of evaluating quality of coverage of the planned treatment region by a certain dose contour</p>
</blockquote>
</aside>
<p>DVH is the usual way to evaluate coverage.</p>

---

## Post #6 by @fedorov (2018-10-05 16:30 UTC)

<p>Yes, ideally I want to have something that differentiates and quantifies the distance inside from the distance outside. But I believe directed is already more useful than symmetric in the use case I described.</p>

---

## Post #7 by @lassoan (2018-10-05 18:05 UTC)

<p>Dose volume histogram (DVH) is a much richer and clinically more meaningful metric than Hausdorff distance could be, because it takes into account dose distribution and provides a histogram and not just a single value. DVH tells how large part of a region of interest is under/overtreated and this metric is used ubiquitously in clinical practice.</p>
<p>Hausdorff distance characterizes segmentation error and typically it does not matter which contour is more outside or inside, because the difference is expected to be small (if the difference is significant then segmentation is failed and it is not very important how). I don’t remember anybody using “signed” Hausdorff distance.</p>

---

## Post #8 by @fedorov (2018-10-05 18:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Dose volume histogram (DVH) is a much richer and clinically more meaningful metric than Hausdorff distance could be, because it takes into account dose distribution and provides a histogram and not just a single value. DVH tells how large part of a region of interest is under/overtreated and this metric is used ubiquitously in clinical practice.</p>
</blockquote>
</aside>
<p>Yes, I agree it is more meaningful, but it is specific to radiotherapy. Can you apply that tool in a situation outside radiation therapy evaluation, where you have two binary contours - one corresponding to the tumor, and one corresponding to the ablation margin?</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Hausdorff distance characterizes segmentation error and typically it does not matter which contour is more outside or inside, because the difference is expected to be small (if the difference is significant then segmentation is failed and it is not very important how). I don’t remember anybody using “signed” Hausdorff distance.</p>
</blockquote>
</aside>
<p>Yes, I again agree, but as I tried to explain earlier - the use case is not to compare two segmentations of the same thing, but to use HD to evaluate tumor target coverage. In the example below, situation on the left can be considered as failure of the procedure, but the HD reported by SegmentComparison module will be identical between the two. Do you agree it is important to distinguish between the two situations?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6837b86603507aa536cfb2ed0c8662e98753f6e2.png" data-download-href="/uploads/short-url/eRX2iJPJLpu5rXFqRHvEJkVyhma.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6837b86603507aa536cfb2ed0c8662e98753f6e2.png" alt="image" data-base62-sha1="eRX2iJPJLpu5rXFqRHvEJkVyhma" width="690" height="307" data-dominant-color="D1D0E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×324 2.97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Signed distance would give an idea about directionality. But even directed distance, as already implemented in ITK, would be more informative, as it will not treat distances equally.</p>
<p>This kind of difference will not always be as obvious visually, and I am afraid the users of the module will not notice this difference, and will just use the numbers produced by the module to come to a conclusion (as happened in the situation I had with the student). Addition of the <s>signed</s> directed distance to the SegmentComparison interface would in my opinion will be very helpful, and it is already implemented in ITK.</p>
<p>HD was used in this kind of applications before, for example see <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2952665/" class="inline-onebox">Multimodality Non-Rigid Image Registration for Planning, Targeting and Monitoring during CT-guided Percutaneous Liver Tumor Cryoablation - PMC</a>. I have not done a thorough review of the literature to see how commonly it is used, but it makes sense to me.</p>
<p>I promise if I again failed to make my point clear, I will not bother this thread again - enough is enough!</p>

---

## Post #9 by @cpinter (2018-10-05 19:02 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>HD reported by SegmentComparison module will be identical between the two</p>
</blockquote>
</aside>
<p>Max HD will be the same. But if you get the minimum, it will be 0 instead of non-zero, which means there is intersection. Maybe you should check the minimum too. Unfortunately Plastimatch HD does not provide that, but there is this class also in SegmentComparison logic that can get you that number (after conversions but with segmentations it’s nothing really)</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.h#L78">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.h#L78" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.h#L78" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.h#L78</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="68" style="counter-reset: li-counter 67 ;">
          <li>
</li>
          <li>/// Get standard deviation of the absolute of the minimum distances \sa GetOutputDistances from the compare mesh to the reference mesh.
</li>
          <li>double GetStandardDeviationHausdorffDistance();
</li>
          <li>
</li>
          <li>/// Get 95th percentile of the absolute of the minimum distances \sa GetOutputDistances from the compare mesh to the reference mesh.
</li>
          <li>/// (this corresponds to the 'percent Hausdorff distance' in plastimatch: http://plastimatch.org/doxygen/classHausdorff__distance.html )
</li>
          <li>double GetPercent95HausdorffDistance();
</li>
          <li>
</li>
          <li>// Get the Nth percentile of the absolute of the minimum distances \sa GetOutputDistances from the compare mesh to the reference mesh.
</li>
          <li>/// (this corresponds to the 'percent Hausdorff distance' in plastimatch: http://plastimatch.org/doxygen/classHausdorff__distance.html )
</li>
          <li class="selected">double GetNthPercentileHausdorffDistance(double n);
</li>
          <li>
</li>
          <li>/// Set whether the filter should sample on the vertices of the input vtkPolyData objects.
</li>
          <li>vtkSetMacro(SamplePolyDataVertices, int);
</li>
          <li>/// Get whether the filter should sample on the vertices of the input vtkPolyData objects.
</li>
          <li>vtkGetMacro(SamplePolyDataVertices, int);
</li>
          <li>/// Set whether the filter should sample on the vertices of the input vtkPolyData objects.
</li>
          <li>vtkBooleanMacro(SamplePolyDataVertices,int);
</li>
          <li>  
</li>
          <li>/// Set whether the filter should sample on the edges of the input vtkPolyData objects.
</li>
          <li>vtkSetMacro(SamplePolyDataEdges, int);
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I understand your point about the directed HD. I think it’s time to just wait until <a class="mention" href="/u/gcsharp">@gcsharp</a> has time to chime in about that.</p>

---

## Post #10 by @lassoan (2018-10-05 19:20 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I promise if I again failed to make my point clear, I will not bother this thread again - enough is enough!</p>
</blockquote>
</aside>
<p>It’s a good discussion that I think is worth the time. Doing one-sided HD is an interesting proposition it is just not yet clear for me if it is a good solution for your needs (or there are any other good use cases).</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>the use case is not to compare two segmentations of the same thing, but to use HD to evaluate tumor target coverage</p>
</blockquote>
</aside>
<p>HD is good for verifying that two segmentations are the same. However, for volumetric analysis, such as evaluating coverage, DSC and related metrics (TP, TN, FP, FN percentages) are probably more appropriate.</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Can you apply that tool in a situation outside radiation therapy evaluation, where you have two binary contours - one corresponding to the tumor, and one corresponding to the ablation margin?</p>
</blockquote>
</aside>
<p>This is exactly the kind of treatment that you can evaluate with DVH. To compute DVH, you need to create a dose volume from your ablation region (export to scalar volume and optionally rescale the intensity to 0-100 range and apply a Gaussian to make it a bit more realistic) and use that to compute DVH for the tumor segment. You can segment multiple regions (target volume, maybe subregions where you want to have higher dose, organs at risk, etc.) to get an even better idea of how good the treatment was. You can also use DVH comparison module to compare the actual DVH to the ideal DVH curves.</p>

---

## Post #11 by @cpinter (2018-10-05 19:37 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Definitely give using DVH a thought, because as Andras says ablation and RT are very similar in this sense. For example the ablation margin you use is analogous with the CTV/PTV (clinical/planning target volume) concept of RT. DVH is the main vehicle of evaluating plans and calculated doses.</p>

---

## Post #12 by @gcsharp (2018-10-05 19:42 UTC)

<p>Yes, I agree.  It is an interesting discussion.  There are many potentially useful metrics.</p>
<p>One quick hack would be to evaluate Hausdorff distance between Tumor \union Ablation and Ablation.  This would give you maximum miss.</p>
<p>For signed distance, you would start with a histogram of distances, some negative, some positive.  How would you propose to condense them?</p>

---

## Post #13 by @fedorov (2018-10-05 20:59 UTC)

<p>Thank you for all the responses. This is helpful and interesting.</p>
<p>I think there are two aspects to my question:</p>
<ol>
<li>how to calculate the various measures for the specific use case, and what is the “best” (for the lack of a better word!) one - I had my own ideas, and I learned a lot more here, thank you for that!</li>
<li>how to improve SegmentComparison module so that it provides more information and hopefully reduces possibility of error for a future user. For this one, my suggestion remains to add directed HD to the list of metrics provided by the module, and discuss the difference between the various HD flavors in the documentation. I am still worried there is a real danger (I witnessed that) that a user can read a paper like the one I referenced, take the module, and proceed with HD calculations, which may end up invalid for a specific situation.</li>
</ol>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>for volumetric analysis, such as evaluating coverage, DSC and related metrics (TP, TN, FP, FN percentages) are probably more appropriate.</p>
</blockquote>
</aside>
<p>I don’t agree with this. Distances are more intuitive to interpret, as they provide value that is meaningful clinically, and they are more actionable.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To compute DVH, you need to create a dose volume from your ablation region (export to scalar volume and optionally rescale the intensity to 0-100 range and apply a Gaussian to make it a bit more realistic) and use that to compute DVH for the tumor segment. You can segment multiple regions (target volume, maybe subregions where you want to have higher dose, organs at risk, etc.) to get an even better idea of how good the treatment was. You can also use DVH comparison module to compare the actual DVH to the ideal DVH curves.</p>
</blockquote>
</aside>
<p>That sounds like a lot of work to “fake” DVH, and I don’t quite understand the benefit yet. I can see how this potentially could be quite interesting to explore, if one has spatial distribution of some meaningful value over the ablation region, such as maximum/minimum temperature at each voxel, but for the simple case we have, we only have the segmentation of a single region. I probably need to read and think more about DVN.</p>
<p>I did give it a quick try, and failed to select a regular scalar volume as “Dose volume” in “Dose Volume Histogram” module, since those need to be “dose volumes”: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/qSlicerDoseVolumeHistogramModuleWidget.cxx#L289-L290" class="inline-onebox">SlicerRT/DoseVolumeHistogram/qSlicerDoseVolumeHistogramModuleWidget.cxx at master · SlicerRt/SlicerRT · GitHub</a> (not sure what this means in terms of attributes that have to be populated).</p>
<aside class="quote no-group" data-username="gcsharp" data-post="12" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>For signed distance, you would start with a histogram of distances, some negative, some positive. How would you propose to condense them?</p>
</blockquote>
</aside>
<p>Maybe report stats for negative and positive values separately?</p>

---

## Post #14 by @lassoan (2018-10-05 21:35 UTC)

<p>Tissue ablation is RT, regardless of the energy source, and so the same basic methods are applicable as for other RT procedures.</p>
<p>Generating a dose volume is not faking anything. It allows much more realistic representation of the dose distribution than a closed surface. You can have a very sharp gradient at the edge of the treated volume, but if you want to be a bit more realistic then you can add a transition zone at the edge.</p>
<p>To make a scalar volume usable as dose volume in Slicer, you need to set a few node attributes (dose unit, etc). <a class="mention" href="/u/cpinter">@cpinter</a> do you have a list of required attributes?</p>

---

## Post #15 by @gcsharp (2018-10-05 21:36 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="13" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Maybe report stats for negative and positive values separately?</p>
</blockquote>
</aside>
<p>We could also simply produce a histogram of distances and let the user crunch the numbers as they see fit.</p>

---

## Post #16 by @gcsharp (2018-10-05 21:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Tissue ablation is RT, regardless of the energy source, and so the same basic methods are applicable as for other RT procedures.</p>
</blockquote>
</aside>
<p>In general, I agree a DVH approach would be a reasonable evaluation method.  But I can imagine cases where there is not enough information to estimate tissue damage, and distance is a reasonable surrogate.</p>

---

## Post #17 by @fedorov (2018-10-05 22:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Tissue ablation is RT, regardless of the energy source, and so the same basic methods are applicable as for other RT procedures.</p>
<p>Generating a dose volume is not faking anything. It allows much more realistic representation of the dose distribution than a closed surface. You can have a very sharp gradient at the edge of the treated volume, but if you want to be a bit more realistic then you can add a transition zone at the edge.</p>
</blockquote>
</aside>
<p>Good point in general. But I have to say I do not know off-hand how I would populate those. All I have really is the segmentation of the volume intended to be treated, and segmentation of the region that is interpreted as the ablated region by the domain expert. <em>De facto</em> I will be faking the dose volume, since the semantics I have in hand for those region is different from what one would need for dose volume.</p>
<aside class="quote no-group" data-username="gcsharp" data-post="15" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>We could also simply produce a histogram of distances and let the user crunch the numbers as they see fit.</p>
</blockquote>
</aside>
<p>We could, and that would be helpful for a more sophisticated user, but I am not so sure about users coming from clinical or clinical research background.</p>

---

## Post #18 by @lassoan (2018-10-06 03:59 UTC)

<p>I’ve checked the Dose Volume Histogram module and it can actually use any scalar volume as “dose volume”, you just need to uncheck <code>Show dose volumes only</code> checkbox.</p>
<p>If you want to make a scalar volume a full-fledged dose volume then execute this script:</p>
<pre><code>import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()

# Create patient and study and put the volume under the study
shNode = slicer.modules.subjecthierarchy.logic().GetSubjectHierarchyNode()
patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), "Patient 1")
studyItemID = shNode.CreateStudyItem(patientItemID, "Study 1")
volumeShItemID = shNode.GetItemByDataNode(volumeNode)
shNode.SetItemParent(volumeShItemID, studyItemID)

# Set volume node appear as dose volume
volumeNode.SetAttribute("DicomRtImport.DoseVolume","1")
volumeNode.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeFilePlasma.txt")
shNode.SetItemAttribute(studyItemID, "DicomRtImport.DoseUnitName", "GY")
shNode.SetItemAttribute(studyItemID, "DicomRtImport.DoseUnitValue", "1e-6")
shNode.RequestOwnerPluginSearch(volumeShItemID)
</code></pre>
<p>The DVH module can also compute metrics of the dose distribution. V and D metric allow you to specify a dose value or a volume (absolute or percentage) and give you the corresponding volume or dose value, respectively. It can be used to quickly evaluate the quality of the treatment, for example it can tell you what percentage of the volume received sufficient dose; or how much dose was delivered to 95% of the volume.</p>
<p>These all are very expressive and clinically widely used metrics. I would strongly recommend to use these instead of trying to invent something new.</p>
<p>You may also find DVH comparison module useful. It can determine how well a dose distribution matches the planned distribution. This is used for example to assess effect of patient motion.</p>

---

## Post #19 by @cpinter (2018-10-09 15:07 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="13" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I did give it a quick try, and failed to select a regular scalar volume as “Dose volume” in “Dose Volume Histogram” module, since those need to be “dose volumes”</p>
</blockquote>
</aside>
<ol>
<li>There is a checkbox under the selector “Show dose volumes only”. If you uncheck it then you can select non-dose volumes, and then the histogram becomes an “Intensity Volume Histogram”</li>
<li>You can convert any volume to a dose volume in subject hierarchy in the right-click menu. In your case it will be a fake dose volume, but you can specify any unit, not just GY</li>
</ol>
<aside class="quote no-group" data-username="gcsharp" data-post="15" data-topic="4300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>We could also simply produce a histogram of distances and let the user crunch the numbers as they see fit.</p>
</blockquote>
</aside>
<p>+1</p>

---

## Post #20 by @fedorov (2018-10-09 15:18 UTC)

<p>Thanks for the pointers! I have not made time yet to try it out and respond, but I will.</p>

---

## Post #21 by @fedorov (2018-10-10 19:58 UTC)

<p>Thinking more about this - <a class="mention" href="/u/kmacneil0102">@Kmacneil0102</a> I think this kind of evaluation (applicability of DVH to this use case, comparison with HD-based metrics, analysis of the literature) fits very nicely into the scope of your thesis. Would be great if you investigated this topic.</p>

---
