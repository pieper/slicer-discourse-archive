---
topic_id: 11981
title: "Centerline Computation Failed"
date: 2020-06-10
url: https://discourse.slicer.org/t/11981
---

# Centerline computation failed

**Topic ID**: 11981
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/centerline-computation-failed/11981

---

## Post #1 by @Deepa (2020-06-10 17:16 UTC)

<p>Hello Everyone,</p>
<p>I’ve been trying to compute centerlines for <a href="https://github.com/DeepaMahm/misc/blob/master/Segmentation4.seg.nrrd" rel="noopener nofollow ugc">this</a> geometry using VMTK extension.</p>
<p>However, I couldn’t successfully obtain centerlines. Even the networkExtraction failed when I tried<br>
to use the stl file of the same geometry</p>
<blockquote>
<p>reader = vmtkscripts.vmtkSurfaceReader()<br>
reader.InputFileName = ‘input.stl’<br>
reader.Execute()</p>
<pre><code># network extraction
networkExtraction = vmtkscripts.vmtkNetworkExtraction()
networkExtraction.Surface = reader.Surface
networkExtraction.Execute()
</code></pre>
</blockquote>
<p>Could someone kindly look into this?</p>

---

## Post #2 by @lassoan (2020-06-10 17:32 UTC)

<p>This model contain 2.8 million points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b90bfdaf7e5f54521bd28b378afbf4e9e2656e.png" data-download-href="/uploads/short-url/lmvBsfiE0tHux51yy1K2Vi6vIT4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95b90bfdaf7e5f54521bd28b378afbf4e9e2656e_2_690x267.png" alt="image" data-base62-sha1="lmvBsfiE0tHux51yy1K2Vi6vIT4" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95b90bfdaf7e5f54521bd28b378afbf4e9e2656e_2_690x267.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b90bfdaf7e5f54521bd28b378afbf4e9e2656e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b90bfdaf7e5f54521bd28b378afbf4e9e2656e.png 2x" data-dominant-color="9D938D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">976×378 360 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Centerline extraction may still work but it would take really long time. I would suggest to cut off unnecessary parts in Segment Editor and heavily decimate the exported model in Surface Toolbox.</p>
<p>You may ask for further suggestions for dealing with large models at the VMTK mailing list.</p>

---

## Post #3 by @Deepa (2020-06-11 07:54 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I wasn’t sure how to select a <code>Start point</code> for such geometry since there are many free ends.<br>
Could you please give some suggestions?</p>

---

## Post #4 by @lassoan (2020-06-11 14:21 UTC)

<p>If you don’t have any preferred root branch then just choose any larger branch that is connected to most others. Start with a cropped model and apply decimation to have no more than a few ten thousand points. You can then experiment with gradually increasing the region of interest size and tune decimation parameters to reach a good tradeoff between quality and amount of data you get, and computation time on your system.</p>
<p>There may be tricks that long-time VMTK users know about how to handle large networks, so please reach out to them and then report back here that you learned.</p>

---

## Post #5 by @Deepa (2020-06-11 15:21 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>decimation to have no more than a few ten thousand points</p>
</blockquote>
</aside>
<p>Thank you very much. I am working on these lines</p>
<p>May I ask a few doubts?</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Start with a cropped model</p>
</blockquote>
</aside>
<p>I couldn’t exactly understand how to obtain a cropped model. In the segment editor I try to use “Scissors” , select operation and shape (circle) required. How should I crop the volume after this step? In one of my previous post, you had mentioned Scissors will only blank the voxles. So I am not sure how to crop.</p>
<p>Could you please briefly explain how decimation works? I find a <code>Reduction</code>tab that shows (0.8) by default. Does this mean 0.8 percent of the original number of points are removed?</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>no more than a few ten thousand points</p>
</blockquote>
</aside>
<p>May I know which feature can be used to get an estimate of the number of points?</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There may be tricks that long-time VMTK users know about how to handle large networks, so please reach out to them and then report back here that you learned.</p>
</blockquote>
</aside>
<p>Definitely, I have reached out to them a week back and wrote to them for the second time today. I will wait for their response and share my learnings here.</p>

---

## Post #6 by @lassoan (2020-06-11 18:44 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="5" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I couldn’t exactly understand how to obtain a cropped model. In the segment editor I try to use “Scissors” , select operation and shape (circle) required. How should I crop the volume after this step? In one of my previous post, you had mentioned Scissors will only blank the voxles. So I am not sure how to crop.</p>
</blockquote>
</aside>
<p>If you crop to reduce memory usage then you need to crop the input volume (before you start segmentation) using Crop volume module. If you crop so that you have a network that VMTK can process faster, you can further cut off parts of the image using Scissors tool.</p>
<aside class="quote no-group" data-username="Deepa" data-post="5" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>Could you please briefly explain how decimation works? I find a <code>Reduction</code> tab that shows (0.8) by default. Does this mean 0.8 percent of the original number of points are removed?</p>
</blockquote>
</aside>
<p>Reduction refers to the requested fraction of points to be removed. 0.8 means that you request removal of 80% of points. Probably you want to use values in the 0.9-0.99 range.</p>
<aside class="quote no-group" data-username="Deepa" data-post="5" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>May I know which feature can be used to get an estimate of the number of points?</p>
</blockquote>
</aside>
<p>Number of points are shown in the tooltip when you hover over your model in Data module. Some more information is shown in Models module / Information section.</p>
<aside class="quote no-group" data-username="Deepa" data-post="5" data-topic="11981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>Definitely, I have reached out to them a week back and wrote to them for the second time today. I will wait for their response and share my learnings here</p>
</blockquote>
</aside>
<p>Explain them in 2-3 sentences who you are, what your project is about, and why it is important. Also attach a screenshot link to example labelmap and segmented model files. Then you have a better chance to get an answer. You may also keep asking 1-2x a week for a couple of weeks, telling what you have tried, and how well those worked.</p>

---

## Post #7 by @Deepa (2020-06-12 14:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks a lot for the clarifications.</p>
<p>I’ve used the segment editor to extract a really small segment this time (available <a href="https://github.com/DeepaMahm/misc/blob/master/Segmentation5.seg.nrrd" rel="noopener nofollow ugc">here</a>).  The initial number of points is 188394.</p>
<p>I have reduced by 80 %( started with 95 % initially). The decimated model now has 37602 points.</p>
<p>I get the following output while trying to run Compute centerlines:</p>
<blockquote>
<p>No data to smooth<br>
No data to decimate<br>
No points to subdivide</p>
</blockquote>
<p>When I try for the original model, the centerline computation doesn’t complete even after 30 min.</p>

---

## Post #8 by @lassoan (2020-06-12 16:00 UTC)

<p>Can you share a download link to a model before and after decimation?</p>

---

## Post #9 by @Deepa (2020-06-13 02:18 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Please find the model files <a href="https://github.com/DeepaMahm/misc/blob/master/Segment5.vtk" rel="nofollow noopener">before</a> and <a href="https://github.com/DeepaMahm/misc/blob/master/Segment5_80deci.vtk" rel="nofollow noopener">after</a> decimation.</p>

---

## Post #10 by @Deepa (2020-06-13 04:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I now have the ouput ,<a href="https://github.com/DeepaMahm/misc/blob/master/CenterlineComputationModel.vtk" rel="noopener nofollow ugc">CenterlineComputationModel</a>, created after centerline computation using the original model (before decimation).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a43914c677ac440624857d83c270cb8469a3cb0.png" data-download-href="/uploads/short-url/8jqshpjxEechlrXZoxgnwPv96o0.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a43914c677ac440624857d83c270cb8469a3cb0_2_345x198.png" alt="Untitled" data-base62-sha1="8jqshpjxEechlrXZoxgnwPv96o0" width="345" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a43914c677ac440624857d83c270cb8469a3cb0_2_345x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a43914c677ac440624857d83c270cb8469a3cb0_2_517x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a43914c677ac440624857d83c270cb8469a3cb0_2_690x396.png 2x" data-dominant-color="8F91BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1367×785 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I see a problem with holes (created during segmentation).</p>

---

## Post #11 by @lassoan (2020-06-20 21:51 UTC)

<p>The <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">new Extract centerline module</a> has now built-in decimation tuned to work well for vessel centerline model preprocessing.</p>

---
