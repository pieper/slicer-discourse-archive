# How to adjust a subtly adjustable surface to cut both sides? (See the picture)

**Topic ID**: 36042
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/how-to-adjust-a-subtly-adjustable-surface-to-cut-both-sides-see-the-picture/36042

---

## Post #1 by @CheerfulMinions (2024-05-10 05:06 UTC)

<p>Hello, when I was using 3D slicer, there was one operation I didn’t know how to implement:<br>
In the following two pictures, in Figure 1, I can cut both sides of the surface after subtle adjustment (Figure 2). In 3D slicer, I know, such as the volume clip plugin, but every time you move a point, the entire surface will change greatly. Another plugin surface markup, its surface is very good, but I don’t know how to use it for effective segmentation?<br>
Thanks for answering!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b46b135956744938dc4190613a4a3e5567dcdf7.png" data-download-href="/uploads/short-url/fj0xTCS2lK6SbGbjsxrRQz4o79d.png?dl=1" title="pic1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b46b135956744938dc4190613a4a3e5567dcdf7_2_623x500.png" alt="pic1" data-base62-sha1="fj0xTCS2lK6SbGbjsxrRQz4o79d" width="623" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b46b135956744938dc4190613a4a3e5567dcdf7_2_623x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b46b135956744938dc4190613a4a3e5567dcdf7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b46b135956744938dc4190613a4a3e5567dcdf7.png 2x" data-dominant-color="918282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic1</span><span class="informations">876×703 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756.png" data-download-href="/uploads/short-url/cPkWRJ3vOnmjZluTvHeKqnmNHG6.png?dl=1" title="pic2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756_2_538x500.png" alt="pic2" data-base62-sha1="cPkWRJ3vOnmjZluTvHeKqnmNHG6" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756_2_538x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756.png 2x" data-dominant-color="898A85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic2</span><span class="informations">650×603 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-05-10 05:12 UTC)

<p>The surface moves a lot because the markup control point is snapped to the cutting surface. Make sure you disable this feature in Markups module → Display → Advanced → 3D Display → Placement mode: unconstrained.</p>
<p>If you want to use this for cutting segmentations then you may find <code>Surface cut</code> effect (provided by SegmentEditorExtraEffects extension) useful.</p>
<p>There is also a tool specifically developed for creating liver resections - see <a href="https://github.com/ALive-research/Slicer-Liver" class="inline-onebox">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</a></p>

---

## Post #3 by @CheerfulMinions (2024-05-11 13:37 UTC)

<p>Thank you very much! If you can see the short video attachment I uploaded (the video has been accelerated to save you time), it demonstrates the effects of a commercial software called MIMICS.<br>
This is cutting part of the lung lobe, so a more accurate plane is needed.</p>
<p>According to your method, I used the surface cut function, and it seems that the effect is not close to MIMICS, the surface I generated is very rough (even if the smooth is cancelled, the effect is still very stiff).</p>
<p>I would like to ask you, can the surface cut function or other tools achieve similar effects in the video? /_ \</p>
<p>Or is there no similar segmentation tool in the video?</p>
<p>Thank you very much again for your answer, and I apologize for my unclear description.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64a907dffb1181f9a0f1fe21ff828508c3a93f7f.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe73dceb229e9171ac81f022c2082c2d141e478a.png">
  </div><p></p>

---

## Post #4 by @chir.set (2024-05-11 20:36 UTC)

<p>Would <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/" rel="noopener nofollow ugc">this</a> module be helpful? It’s somehow close to your video’s content: use a warpable plane.</p>

---

## Post #5 by @lassoan (2024-05-11 21:20 UTC)

<p>In general, Slicer has much more and more powerful tools than MIMICS, but it is not always easy to find the most relevant tool and they are not always as simple and polished.</p>
<p>Surface cut effect works well for planning and guiding breast lumpectomy, but it is not well suited for liver resection planning, because it uses a closed surface.</p>
<p>As I wrote above, for liver resection planning, I would recommend the <a href="https://github.com/ALive-research/Slicer-Liver"><code>Liver</code> module</a> of <code>SlicerLiver</code> extension. It not just provides a way to specify a curved resection plane, but it can also visualizes distance from the tumor, subdivide the liver based on vasculature, measure volumes, etc. <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can help with any questions that you may have.</p>
<p>You can use TotalSegmentator, MONAI Auto3DSeg or <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation">RVX Liver</a> for liver, tumor, and vessel segmentation.</p>

---

## Post #6 by @CheerfulMinions (2024-05-12 05:26 UTC)

<p>Yes, I think it will help. After I have created the surface, how do I split the models on both sides of the surface?</p>
<p>I didn’t find a help manual in the instructions.</p>
<p>(For example, in the picture, I want to strictly follow the position of the surface, divided into two parts. Of course, this is just an example, I don’t apply it to cutting blood vessels)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490.png" data-download-href="/uploads/short-url/lcCo2eADfIAHiBcaHyb6gAISVFK.png?dl=1" title="pic3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490_2_523x500.png" alt="pic3" data-base62-sha1="lcCo2eADfIAHiBcaHyb6gAISVFK" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490.png 2x" data-dominant-color="918B97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic3</span><span class="informations">533×509 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @MikhayEeer (2024-05-12 05:34 UTC)

<p>I have the same problem. I have also seen this plug-in. I can use SurfaceMarkup to create an unclosed surface, but I have not found how to use the created surface for segmentation. <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @CheerfulMinions (2024-05-12 05:38 UTC)

<p>Yes! I also think that 3D slicer is more powerful than Mimics and can combine more operations.</p>
<p>But the Liver module can’t be applied directly to some free segmentation: removing part of the lung, for example, or dividing the sides of a curved surface strictly according to the surface. (I’m not using it to cut livers.)</p>
<p>For this kind of cutting, I don’t think AI can directly help me at the moment</p>
<p>Thank you very much for your answer!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756.png" data-download-href="/uploads/short-url/cPkWRJ3vOnmjZluTvHeKqnmNHG6.png?dl=1" title="pic2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756_2_538x500.png" alt="pic2" data-base62-sha1="cPkWRJ3vOnmjZluTvHeKqnmNHG6" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756_2_538x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e7b7ef6f219e9349ce2288e7ebb9ce47514756.png 2x" data-dominant-color="898A85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic2</span><span class="informations">650×603 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490.png" data-download-href="/uploads/short-url/lcCo2eADfIAHiBcaHyb6gAISVFK.png?dl=1" title="pic3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490_2_523x500.png" alt="pic3" data-base62-sha1="lcCo2eADfIAHiBcaHyb6gAISVFK" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949ad484430ce5bab8cc733b60621301c8f29490.png 2x" data-dominant-color="918B97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic3</span><span class="informations">533×509 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2024-05-12 11:35 UTC)

<aside class="quote no-group" data-username="CheerfulMinions" data-post="6" data-topic="36042">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cheerfulminions/48/70361_2.png" class="avatar"> CheerfulMinions:</div>
<blockquote>
<p>how do I split the models on both sides of the surface?</p>
</blockquote>
</aside>
<p>The Liver extension can compute volumes, distances, etc. based on this surface.</p>
<p>What is your overall goal and what are some specific steps that you are considering to do to achieve these goals?</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> has done a lot of lung surgery planning with Slicer, so he may also have suggestions if you describe what you want to do.</p>

---

## Post #10 by @dalbenzioG (2024-05-13 09:16 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>, for mentioning our Slicer-Liver extension.</p>
<p>Hi <a class="mention" href="/u/cheerfulminions">@CheerfulMinions</a>!</p>
<p>Currently, it is not possible to split the segmentation of the resected and remaining lobes using a cutting surface. However, you can utilize our Liver Segment section to segment the lobes and plan a resection. This process involves placing control points on the vessels (1), generating the centerlines (2), and computing the vascular territories(3) - please see the figure below and you can also find more information in this <a href="https://www.researchsquare.com/article/rs-3574517/v1" rel="noopener nofollow ugc">preprint</a>. We have successfully applied this strategy to lung resection, as demonstrated <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/#lung-surgery-planning-with-rudolf-bumm" rel="noopener nofollow ugc">here</a>.</p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>, please feel free to add any additional insights if I’ve missed something.<br>
I’m currently updating the tutorial for our extension and integrating new functionalities, so stay tuned! If you’d like to try it out and need assistance, don’t hesitate to reach out to either me or Rafael.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7598029ee771f3c675a8c5d15f40b183cba843d3.png" data-download-href="/uploads/short-url/gMhxKXk5InoSJ9t4cD9nkFLITBh.png?dl=1" title="centerline" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7598029ee771f3c675a8c5d15f40b183cba843d3_2_690x388.png" alt="centerline" data-base62-sha1="gMhxKXk5InoSJ9t4cD9nkFLITBh" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7598029ee771f3c675a8c5d15f40b183cba843d3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7598029ee771f3c675a8c5d15f40b183cba843d3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7598029ee771f3c675a8c5d15f40b183cba843d3.png 2x" data-dominant-color="BDBED6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centerline</span><span class="informations">960×540 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @RafaelPalomar (2024-05-13 09:49 UTC)

<p><a class="mention" href="/u/cheerfulminions">@CheerfulMinions</a>, <a class="mention" href="/u/chir.set">@chir.set</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/dalbenziog">@dalbenzioG</a>, this is a very interesting discussion.</p>
<p>Slicer-Liver has functionality to plan resections, perform liver classification based on liver vasculature and do volumetry analysis of resections, liver segments, etc. The way it works  may not resemble workflows of other applications. For instance, our resection plans are based on visualization of resection surfaces with the possibility to do volumetry, but we don’t explicitly cut the mesh on resected/remnant sub-meshes to visualize them in different colors. Reasons: (1) we think it unnecessarily complicates the visualization (having resection surfaces and different colored areas is redundant; transparent colors are perceived differently depending on the background they have); (2) volumetric calculations are more precise in image-space than in possibly simplified meshes and that’s what we use for volumetry analysis.</p>
<p>If you strictly adhere to anatomical resections, the approach <a class="mention" href="/u/dalbenziog">@dalbenzioG</a>, illustrated is valid and you don’t need to set any resection surface, you just need to use the segments classification tool in Slicer-Liver.</p>
<p>If you would like non-anatomical resections it may be possible already to get the remnant/resected segmentations from the volumetry analysis in Slicer-Liver. <a class="mention" href="/u/ruoyanmeng">@RuoyanMeng</a>, do we expose the subvolumes of the liver as Slicer Segmentations during the volumetry analysis? If not, would it be difficult to save and expose them for this type of analysis?</p>
<p>Project week is around the corner, it may be a good avenue to joint efforts for refining/adding this functionality.</p>

---

## Post #12 by @RuoyanMeng (2024-05-13 10:52 UTC)

<p>Currently, we don’t expose the subvolumes to the user. We can add this as an optional output in the LiverVolumetry, so when the user places ROI points on resected and remaining lobes we can generate a new segmentation image that labels the resected and remaining lobes. I opened an <a href="https://github.com/ALive-research/Slicer-Liver/issues/266" rel="noopener nofollow ugc">issue</a>, <a class="mention" href="/u/cheerfulminions">@CheerfulMinions</a> you are welcome to add more description of the functionality you would like.</p>

---
