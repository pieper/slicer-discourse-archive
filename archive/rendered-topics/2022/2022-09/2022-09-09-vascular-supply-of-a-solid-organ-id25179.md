# Vascular supply of a solid organ

**Topic ID**: 25179
**Date**: 2022-09-09
**URL**: https://discourse.slicer.org/t/vascular-supply-of-a-solid-organ/25179

---

## Post #1 by @Celina_Hallal (2022-09-09 16:06 UTC)

<p>Hello!<br>
Is there anyway I can estimate the area supplied by a specific branch? I would like to see a preview of an ischemic area if one branch is ligated or embolized, and estimate the drainage area of some vein…</p>
<p>Thanks a lot!</p>

---

## Post #2 by @Celina_Hallal (2022-09-09 16:11 UTC)

<p>I’m not sure I was clear in my request, but I would like to do something like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fe31cf9edce7c467e17ef9c9bed64072585a233.jpeg" data-download-href="/uploads/short-url/97aFrkCqD0OwiTPQLJvNEJQ4VGz.jpeg?dl=1" title="Captura de Tela 2022-09-09 às 13.08.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe31cf9edce7c467e17ef9c9bed64072585a233_2_432x500.jpeg" alt="Captura de Tela 2022-09-09 às 13.08.58" data-base62-sha1="97aFrkCqD0OwiTPQLJvNEJQ4VGz" width="432" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe31cf9edce7c467e17ef9c9bed64072585a233_2_432x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe31cf9edce7c467e17ef9c9bed64072585a233_2_648x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe31cf9edce7c467e17ef9c9bed64072585a233_2_864x1000.jpeg 2x" data-dominant-color="CDC4D1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2022-09-09 às 13.08.58</span><span class="informations">1124×1298 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
doi: 10.21037/atm-20-7920</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c81d06d3de6745bff242ccb5eb8e2dfb11da4081.jpeg" data-download-href="/uploads/short-url/syhGn9TN2oQszDyFDKwNIlJGhVf.jpeg?dl=1" title="Captura de Tela 2022-09-09 às 13.08.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c81d06d3de6745bff242ccb5eb8e2dfb11da4081_2_494x500.jpeg" alt="Captura de Tela 2022-09-09 às 13.08.09" data-base62-sha1="syhGn9TN2oQszDyFDKwNIlJGhVf" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c81d06d3de6745bff242ccb5eb8e2dfb11da4081_2_494x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c81d06d3de6745bff242ccb5eb8e2dfb11da4081_2_741x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c81d06d3de6745bff242ccb5eb8e2dfb11da4081_2_988x1000.jpeg 2x" data-dominant-color="615F5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2022-09-09 às 13.08.09</span><span class="informations">1112×1124 70.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
doi: 10.1016/j.cmpb.2017.12.008</p>

---

## Post #3 by @rbumm (2022-09-10 01:30 UTC)

<p>Hi Celina,<br>
I know that <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is working on a very similar project - Slicer-Liver.<br>
Maybe he can comment.<br>
Kind regards<br>
Rudolf</p>

---

## Post #4 by @lassoan (2022-09-10 12:31 UTC)

<p>I haven’t looked at the paper but most likely you can reproduce the same workflow in Slicer.</p>
<p>If I had to implement vessel-based segmentation of the liver in Slicer, I would do the following:</p>
<ul>
<li>segment the whole liver and the arteries in Segment Editor module</li>
<li>partition the vessel tree (into separate segments): for example, you can make a few scribbles in the vessel tree and use Grow from seeds (choose the vessel segment as editable region)</li>
<li>partition the liver segment: use the vessel segments as seeds to segment the liver (using a full liver segment as editable region, hide the liver segment so that it is not used for region growing, and set a high seed locality value to do the region growing mostly based on distance from vessels and not so much based on image intensity)</li>
</ul>
<p>It is a complex workflow if you don’t know all the tools yet, but if you complete a couple of segmentations then it becomes much easier. It can be also fully automated, using MONAILabel for liver and vessel segmentation, VMTK for centerline analysis, and some Python scripting to go through all the steps.</p>
<p>However, as <a class="mention" href="/u/rbumm">@rbumm</a> suggested, before diving into reimplementing these steps from scratch I would recommend to check out extensions that are already developed for liver segmentation and surgical planning, such as:</p>
<ul>
<li>
<a href="https://github.com/ALive-research/Slicer-LiverAnalysis" class="inline-onebox">GitHub - ALive-research/Slicer-LiverAnalysis: 3D Slicer extension for liver analysis</a> by group of <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>
</li>
<li><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" class="inline-onebox">GitHub - R-Vessel-X/SlicerRVXLiverSegmentation: 3D Slicer plugin for Liver Anatomy Annotation by R-Vessel-X</a></li>
<li>
<a href="https://github.com/Project-MONAI/MONAILabel" class="inline-onebox">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a> general-purpose volumetric image segmentation</li>
</ul>

---

## Post #5 by @rbumm (2022-09-13 17:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> like your idea and, as we need to do the same for lung segments, I tried the grow from seeds technique from AI-generated vessels but the borders of the segmentation were very fuzzy and did not appear line-cut.</p>
<p>So in this upper lung lobe with three segments <a class="mention" href="/u/eserval">@Eserval</a> and I current would:</p>
<ul>
<li>create S1, S2 and S3 segments</li>
<li>use arithmetic copy of right upper lobe on each segment</li>
<li>use a vessel-orientated scissor cut to isolate S1</li>
<li>subtract S1 from S2 and S3</li>
<li>do a vessel-orientated scissor cut to isolate S2</li>
<li>finally, subtract S2 from S3.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc483f0211b7477fdfca86f423923e5f7a7228be.png" data-download-href="/uploads/short-url/qRCyafBW2u47Oad8r85oPJmTK58.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc483f0211b7477fdfca86f423923e5f7a7228be_2_690x301.png" alt="image" data-base62-sha1="qRCyafBW2u47Oad8r85oPJmTK58" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc483f0211b7477fdfca86f423923e5f7a7228be_2_690x301.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc483f0211b7477fdfca86f423923e5f7a7228be_2_1035x451.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc483f0211b7477fdfca86f423923e5f7a7228be_2_1380x602.png 2x" data-dominant-color="B5B5D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×838 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But this is a bit like cheating and a grow from seeds or watershed method would be better.<br>
As we need to perform this in 20+ cases and all lung lobes for training a model any ideas on how to do this effectively and anatomically correct are very welcome.</p>

---

## Post #6 by @pieper (2022-09-13 18:45 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> what about doing a distance transform from each branch of the vessels and then create a segmentation where each voxel is labeled by the vessel it is closest to (min of the distance transforms).   Basically a <a href="https://en.wikipedia.org/wiki/Voronoi_diagram">Voronoi method</a>.</p>

---

## Post #7 by @Eserval (2022-09-14 12:25 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/celina_hallal">@Celina_Hallal</a> I do not know how is the definition of edge segment in liver but for the lungs, it is a key point. For lungs, we have the artery in the center of the segment running together with the bronchus, but the border of segment is defined by an intersegmental vein.<br>
Look at the example of that lower lobe surgery planning with a nodule in the S8 segment (Veins in red and artery in blue since is lung circulation):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93d71f875935dcc28ff98fba54b59681dc4bc78a.jpeg" data-download-href="/uploads/short-url/l5R5pXw4I30AQMI0CZU5GDVAoeS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d71f875935dcc28ff98fba54b59681dc4bc78a_2_689x384.jpeg" alt="image" data-base62-sha1="l5R5pXw4I30AQMI0CZU5GDVAoeS" width="689" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d71f875935dcc28ff98fba54b59681dc4bc78a_2_689x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d71f875935dcc28ff98fba54b59681dc4bc78a_2_1033x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93d71f875935dcc28ff98fba54b59681dc4bc78a.jpeg 2x" data-dominant-color="D1C0B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1293×720 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8020083ae15c6d851e8e71e268b3cf8c6f91f2.jpeg" data-download-href="/uploads/short-url/d3rXjgRde15qx4jBCc4GHgRHH6q.jpeg?dl=1" title="Right lung with lower lobe segmented, in yellow, the segment of interest with the lesion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8020083ae15c6d851e8e71e268b3cf8c6f91f2_2_690x411.jpeg" alt="Right lung with lower lobe segmented, in yellow, the segment of interest with the lesion" data-base62-sha1="d3rXjgRde15qx4jBCc4GHgRHH6q" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8020083ae15c6d851e8e71e268b3cf8c6f91f2_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8020083ae15c6d851e8e71e268b3cf8c6f91f2_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8020083ae15c6d851e8e71e268b3cf8c6f91f2.jpeg 2x" data-dominant-color="C5BDB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Right lung with lower lobe segmented, in yellow, the segment of interest with the lesion</span><span class="informations">1226×732 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d218aa756d9006b604fb97f3b9747fb4fa6a48.jpeg" data-download-href="/uploads/short-url/udQShSWQc8ajVydZw9P92cWULK8.jpeg?dl=1" title="Rigth lung (front and R view)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d218aa756d9006b604fb97f3b9747fb4fa6a48_2_690x415.jpeg" alt="Rigth lung (front and R view)" data-base62-sha1="udQShSWQc8ajVydZw9P92cWULK8" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d218aa756d9006b604fb97f3b9747fb4fa6a48_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d218aa756d9006b604fb97f3b9747fb4fa6a48_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d218aa756d9006b604fb97f3b9747fb4fa6a48.jpeg 2x" data-dominant-color="DBD0D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Rigth lung (front and R view)</span><span class="informations">1216×732 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d65bbc2bb90752008f443c4ab7c6ad0722461f6d.jpeg" data-download-href="/uploads/short-url/uAiIE3oi6ouqyCjeR7i8AK8OiRv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d65bbc2bb90752008f443c4ab7c6ad0722461f6d.jpeg" alt="image" data-base62-sha1="uAiIE3oi6ouqyCjeR7i8AK8OiRv" width="668" height="500" data-dominant-color="BCA99D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1007×753 78.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ad96bd9a76c4a2547f831a1321cae6dcbca7d61.jpeg" data-download-href="/uploads/short-url/ffeqXuPYSP0B95Cn5k7CKokw2Yh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ad96bd9a76c4a2547f831a1321cae6dcbca7d61.jpeg" alt="image" data-base62-sha1="ffeqXuPYSP0B95Cn5k7CKokw2Yh" width="553" height="500" data-dominant-color="B0A196"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">828×748 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d306dbe6aecff4da77369dfc15fa284866ebcb9d.jpeg" data-download-href="/uploads/short-url/u6PrnqW62ZQxKH70R128NeZ72Hj.jpeg?dl=1" title="Note that the limit between segments are defined by veins" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d306dbe6aecff4da77369dfc15fa284866ebcb9d.jpeg" alt="Note that the limit between segments are defined by veins" data-base62-sha1="u6PrnqW62ZQxKH70R128NeZ72Hj" width="624" height="500" data-dominant-color="BBA79D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Note that the limit between segments are defined by veins</span><span class="informations">935×749 60.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So… for the lung I think we have two major challenges: make the segment grow from the main artery and stop in the intersegmental vein. Thinking about the final user, most of the time is hard to define the intersegmental vein before having the 3D segmentation of the vessels and airway. So, maybe the automatic workflow should have steps where the first should be the vessels and airway segmentation and next the user would mark the intersegmental vein and artery… I don’t know it’s an idea. <a class="mention" href="/u/rbumm">@rbumm</a><br>
<a class="mention" href="/u/celina_hallal">@Celina_Hallal</a> I don’t know if in the liver you have the same issues.</p>
<p>I also work with the Synapse Vincent by Fuji… The AI is awesome in dividing the intersegmental plane between lung segments. It works through center lines. After the lobes, airway, and vessel’s automatic extraction, the user selects the centerline of the segmental artery, and the software automatically extracts the segment.</p>

---

## Post #8 by @lassoan (2022-09-15 13:05 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="25179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I tried the grow from seeds technique from AI-generated vessels but the borders of the segmentation were very fuzzy and did not appear line-cut</p>
</blockquote>
</aside>
<p>This is expected if the region growing is done based on image intensity. If you set  set a high “Seed locality” value in Grow from seeds then region growing will be based on a distance transform (doing essentially the same that <a class="mention" href="/u/pieper">@pieper</a> suggested, too), that takes into account the lung mask (while computing the distance map, the area outside the lung is excluded).</p>
<p>Joint smoothing can be applied to further smooth the boundary as much as needed. If that is still not sufficient then it is possible to fit a spline surface to the boundary, which can be used for smoothing (enforce a slightly curved cutting surfaces) and to allow convenient manual adjustment.</p>

---

## Post #9 by @Celina_Hallal (2022-09-15 14:10 UTC)

<p>Lots of things! I will take some time to read it and try some workflows. Did I said I really like the Slicer community? <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @rbumm (2022-09-15 19:29 UTC)

<aside class="quote no-group" data-username="Celina_Hallal" data-post="9" data-topic="25179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/celina_hallal/48/12339_2.png" class="avatar"> Celina_Hallal:</div>
<blockquote>
<p>like the Slicer community? <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>Me too <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Thanks all for the thoughtful comments, will try the grow from seeds with the different settings again as soon as possible. We should look into this Synapse workflow during our next meeting <a class="mention" href="/u/eserval">@Eserval</a>. The segmentations you show above are top-notch.</p>

---

## Post #11 by @RafaelPalomar (2022-10-06 06:49 UTC)

<p>Hello <a class="mention" href="/u/celina_hallal">@Celina_Hallal</a>. Have you tried the Slicer-Liver extension as <a class="mention" href="/u/rbumm">@rbumm</a> suggested? It should be available through the extension manager in the Slicer Preview release. You can find more information at <a href="https://github.com/ALive-research/Slicer-Liver" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</a>. Don’t hesitate to contact me if you have questions about Slicer-Liver</p>
<p>-Rafael.</p>

---
