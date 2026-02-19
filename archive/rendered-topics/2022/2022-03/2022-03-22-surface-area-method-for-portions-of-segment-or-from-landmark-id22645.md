---
topic_id: 22645
title: "Surface Area Method For Portions Of Segment Or From Landmark"
date: 2022-03-22
url: https://discourse.slicer.org/t/22645
---

# Surface Area method for portions of segment or from landmarks

**Topic ID**: 22645
**Date**: 2022-03-22
**URL**: https://discourse.slicer.org/t/surface-area-method-for-portions-of-segment-or-from-landmarks/22645

---

## Post #1 by @Rosalee_Elting (2022-03-22 20:41 UTC)

<p><strong>Surface Area method for portions of segment or from landmarks</strong></p>
<p>OS: Windows 10Pro<br>
Slicer version: 4.11.20210226<br>
Data file location: <a href="https://drive.google.com/file/d/1dxBYAEgEPDulDVuz_X3BaTYmzNbk6roQ/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">For Forum Upload.zip - Google Drive</a></p>
<p>I am trying to get surface area of a portion of a segment, or model. I am working with hummingbird bills and hoping to create a workflow to determine surface area of the bill. The problem is some of these CT scans are of museum birds, and the inside of the maxilla has packing material, distorting the SA. I am hoping to find a way to get just the dorsal surface area of the bill, not the intraoral space.</p>
<ol>
<li>
<p>Imported CT scans, segmented out upper mandible.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f83b0be37cd18d66d4ea9d1f81369168436a1d0.png" data-download-href="/uploads/short-url/blpRFbb0ceZo6ifZytZaDVqt6KY.png?dl=1" title="Segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f83b0be37cd18d66d4ea9d1f81369168436a1d0_2_677x500.png" alt="Segment" data-base62-sha1="blpRFbb0ceZo6ifZytZaDVqt6KY" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f83b0be37cd18d66d4ea9d1f81369168436a1d0_2_677x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f83b0be37cd18d66d4ea9d1f81369168436a1d0_2_1015x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f83b0be37cd18d66d4ea9d1f81369168436a1d0.png 2x" data-dominant-color="9397C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment</span><span class="informations">1250×922 67.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c2e4dd0e8aa4bd44ef8e4f7f38cac38ac21d7c.png" data-download-href="/uploads/short-url/jEGYg2WhVyZ3Zpi0luoWb80oHMM.png?dl=1" title="segment 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89c2e4dd0e8aa4bd44ef8e4f7f38cac38ac21d7c_2_690x311.png" alt="segment 2" data-base62-sha1="jEGYg2WhVyZ3Zpi0luoWb80oHMM" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89c2e4dd0e8aa4bd44ef8e4f7f38cac38ac21d7c_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c2e4dd0e8aa4bd44ef8e4f7f38cac38ac21d7c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c2e4dd0e8aa4bd44ef8e4f7f38cac38ac21d7c.png 2x" data-dominant-color="9299C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment 2</span><span class="informations">1031×466 69.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I was able to get SA from the <strong>Segment Statistics Module</strong>, but again, I’m missing the ability to only get the upper surface of the bill.</p>
</li>
<li>
<p>Made a model out of the segment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/535b03226744f0d448df1040fc8fb911fa4e292c.png" data-download-href="/uploads/short-url/bToCClLNoTXrYiNwsTxH4E1ppoM.png?dl=1" title="model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/535b03226744f0d448df1040fc8fb911fa4e292c_2_690x415.png" alt="model" data-base62-sha1="bToCClLNoTXrYiNwsTxH4E1ppoM" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/535b03226744f0d448df1040fc8fb911fa4e292c_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/535b03226744f0d448df1040fc8fb911fa4e292c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/535b03226744f0d448df1040fc8fb911fa4e292c.png 2x" data-dominant-color="9898CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model</span><span class="informations">716×431 43.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Again, could get SA here, but for the whole model.</p>
</li>
<li>
<p>Used <strong>PseudoLM Module</strong> to create landmarks using a template.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8f176032944b25568f1bae5a778eacd58e092e9.png" data-download-href="/uploads/short-url/uXasBASF0hy6Smwd8pR4SHUWs6R.png?dl=1" title="pseudo lm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8f176032944b25568f1bae5a778eacd58e092e9_2_600x500.png" alt="pseudo lm" data-base62-sha1="uXasBASF0hy6Smwd8pR4SHUWs6R" width="600" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8f176032944b25568f1bae5a778eacd58e092e9_2_600x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8f176032944b25568f1bae5a778eacd58e092e9_2_900x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8f176032944b25568f1bae5a778eacd58e092e9.png 2x" data-dominant-color="9999CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pseudo lm</span><span class="informations">913×760 97.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Created a open curve using <strong>Markups Module</strong> to make a border of the bill so landmark vertices included area of interest. Added those points to my landmark control point list.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23bcbe8990c757d50efeacc77fa24b402a8a850f.png" data-download-href="/uploads/short-url/5695QeM11yixRtDvBOJXdHGWeaX.png?dl=1" title="landmarks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23bcbe8990c757d50efeacc77fa24b402a8a850f_2_644x500.png" alt="landmarks" data-base62-sha1="5695QeM11yixRtDvBOJXdHGWeaX" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23bcbe8990c757d50efeacc77fa24b402a8a850f_2_644x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23bcbe8990c757d50efeacc77fa24b402a8a850f_2_966x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23bcbe8990c757d50efeacc77fa24b402a8a850f.png 2x" data-dominant-color="9899CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">landmarks</span><span class="informations">1041×808 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Get Surface area from these landmarks? This is where I’m hoping for some input. Perhaps it can even be done back in segment editor. I also considered “filling” the bill with a plane, getting the SA of that and then merging with the model, subtract ting that SA and getting the bill SA, but not sure how I’d execute that.</p>
</li>
</ol>
<p>Thank you for any input!</p>

---

## Post #2 by @muratmaga (2022-03-22 21:04 UTC)

<p>As I understand you only want the SA of the dorsal (top) of the bill? Is that correct?</p>
<p>Probably the simplest solution is to use the Surface Cut effect in Segment editor, cut out the portion you want to retain via using closed curve markup, and then use the Segment Statistics module to calculate the SA.</p>
<p>Alternatively, there is a new markup type called patchMarkup available as a separate extension. I have not tried that, but that might give you an option of placing a patch over the region you want to measure.</p>

---

## Post #3 by @Rosalee_Elting (2022-03-22 22:54 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>, thanks for the prompt reply.</p>
<p>So I would:</p>
<ol>
<li>Isolate the upper bill with Surface cut (directly from CT scan?) &gt;</li>
<li>Use closed curve to choose the area on the segment I’d like to keep (line along the edge of the bill to circle around the dorsal side of the bill). Btw can I constrain a resampled closed curve to the surface of a segment, or only a model?&gt;</li>
<li>Measure the SA of that segment that falls within the closed curve? (I don’t see an option in segment statistics to use a closed curve as the source for the SA.</li>
</ol>
<p>Maybe I’m missing something here and the closed curve is to portion out a new segment from the entire bill segment, in which case, which module would I use?</p>
<p>Thank you!</p>

---

## Post #4 by @Rosalee_Elting (2022-03-22 23:20 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I did find a potential solution to my own question for <strong>3</strong> using the second code chunk that Andras gave in <a href="https://discourse.slicer.org/t/how-can-i-calculate-an-area-on-a-ct-image-i-can-calculate-volumes-mm-3-but-not-areas-mm-2/1549/4">this link</a>.</p>
<p>Attached is what it looks like it’s measuring, which is within the closed curve, but is unfortunately the under side of the bill.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/301b03e0661f8c4b5c7fbc611d817214bbf16f8c.png" data-download-href="/uploads/short-url/6RyNuvfznRr4XmADjy3qxNzuEva.png?dl=1" title="measured area" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/301b03e0661f8c4b5c7fbc611d817214bbf16f8c_2_679x500.png" alt="measured area" data-base62-sha1="6RyNuvfznRr4XmADjy3qxNzuEva" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/301b03e0661f8c4b5c7fbc611d817214bbf16f8c_2_679x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/301b03e0661f8c4b5c7fbc611d817214bbf16f8c_2_1018x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/301b03e0661f8c4b5c7fbc611d817214bbf16f8c.png 2x" data-dominant-color="9497C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">measured area</span><span class="informations">1102×811 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It also seems like it’s adding a “cap” here, to the end of the bill, which might resolve when we’re measuring the dorsal area<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8fa72547cd5a69e852d2a22f0e1481e5895131.jpeg" data-download-href="/uploads/short-url/1N7vhEd8NjFfaeEdbRdBfQUHwMF.jpeg?dl=1" title="included edge.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8fa72547cd5a69e852d2a22f0e1481e5895131.jpeg" alt="included edge.PNG" data-base62-sha1="1N7vhEd8NjFfaeEdbRdBfQUHwMF" width="689" height="460" data-dominant-color="5E607D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">included edge.PNG</span><span class="informations">1181×789 38.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a way to change which surface of the segment it is measuring. Has there has been an updated method to do this beyond the Python console?</p>
<p>Thanks!</p>

---

## Post #5 by @chir.set (2022-03-23 07:48 UTC)

<aside class="quote no-group" data-username="Rosalee_Elting" data-post="4" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>a potential solution to my own question for <strong>3</strong> using the second code chunk</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Rosalee_Elting" data-post="4" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>Has there has been an updated method to do this beyond the Python console?</p>
</blockquote>
</aside>
<p>If you use a Closed Curve, the surface area is <a href="https://discourse.slicer.org/t/how-can-i-calculate-an-area-on-a-ct-image-i-can-calculate-volumes-mm-3-but-not-areas-mm-2/1549/24">available</a> right away in the Markups module. It seems that’s what you are looking for, right ?</p>

---

## Post #6 by @muratmaga (2022-03-23 15:38 UTC)

<aside class="quote no-group" data-username="Rosalee_Elting" data-post="4" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>It also seems like it’s adding a “cap” here, to the end of the bill, which might resolve when we’re measuring the dorsal area</p>
</blockquote>
</aside>
<p>I am not sure why it is recapping only a portion of the closed surface. As I recall it should visualize entire area that’s encompassed by the curve, and that’s where the SA comes from.</p>
<p>Your issue is you want the outer surface of the bill, but all your points on the curve is roughly coplanar, and only covers the inner side. You won’t be able to do that with this approach. That’s why I think new surfaceMarkup type (which allows you draw a surface patch, as opposed to a curve) will be more flexible and usable.  Here is an example. The gray is the surface patch generated by this 3x3 grid, and it follows the curvature of the skull roof closely.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/506bd2af42273c22043e87c975b8a4e3274dae65.jpeg" data-download-href="/uploads/short-url/btrcQW3Vwix0UI3AJ8wLFT5EWPP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506bd2af42273c22043e87c975b8a4e3274dae65_2_408x500.jpeg" alt="image" data-base62-sha1="btrcQW3Vwix0UI3AJ8wLFT5EWPP" width="408" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506bd2af42273c22043e87c975b8a4e3274dae65_2_408x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/506bd2af42273c22043e87c975b8a4e3274dae65.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/506bd2af42273c22043e87c975b8a4e3274dae65.jpeg 2x" data-dominant-color="A2A0B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">537×657 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The issue is it looks like measurement calculations are not enabled for this markup type. <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is that correct, or do I have an old version?</p>
<p>If you search for surfaceMarkup extension in a recent preview version, you can experiment with it.</p>
<p>Otherwise, I think the surface cut in segment editor would work too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e8f29df6d198f2d6b1c443d40d557bbbcfff3f5.png" data-download-href="/uploads/short-url/fM3fomAYv0b1je4gir1hMcwS1Uh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e8f29df6d198f2d6b1c443d40d557bbbcfff3f5_2_690x379.png" alt="image" data-base62-sha1="fM3fomAYv0b1je4gir1hMcwS1Uh" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e8f29df6d198f2d6b1c443d40d557bbbcfff3f5_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e8f29df6d198f2d6b1c443d40d557bbbcfff3f5_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e8f29df6d198f2d6b1c443d40d557bbbcfff3f5.png 2x" data-dominant-color="D9D6E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1043×574 82.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @mau_igna_06 (2022-03-23 16:13 UTC)

<p>More or less I think until step 3 you are on your way.</p>
<p>You could use this tool <a href="https://discourse.slicer.org/t/new-dynamic-modeler-tool-select-by-points/22165" class="inline-onebox">New Dynamic Modeler Tool: Select by Points</a> to extract the surface</p>
<p>Then use the this filter <a href="https://vtk.org/doc/nightly/html/classvtkMassProperties.html#a02ff978e03cdb233de1851e7d011917b" class="inline-onebox">VTK: vtkMassProperties Class Reference</a> to calculate the surface area.</p>
<p>Also try to take a look at how the surface area calculation is implemented on the Models module of Slicer as I think you may need to preprocess your input with the triangle filter with some non-default option</p>
<p>Or you could just simply check the surface area of the (cropped) selectByPointsModel on the information panel of the Models module. I think that would be enough</p>
<p>Hope it helps</p>

---

## Post #9 by @Rosalee_Elting (2022-03-23 18:11 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> I didn’t know I could get this data from a closed curve in markups— thank you!</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Otherwise, I think the surface cut in segment editor would work too.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> This worked pretty well too. Here is my original segment, with a new segment of the surface, whose points I modified in both 3D and 3D views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/626f67db150f9ca371370ca676984003533a6b67.png" data-download-href="/uploads/short-url/e2NtCeakFF2AuKiC2eNDtd5frVR.png?dl=1" title="bill with cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/626f67db150f9ca371370ca676984003533a6b67_2_689x500.png" alt="bill with cut" data-base62-sha1="e2NtCeakFF2AuKiC2eNDtd5frVR" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/626f67db150f9ca371370ca676984003533a6b67_2_689x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/626f67db150f9ca371370ca676984003533a6b67_2_1033x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/626f67db150f9ca371370ca676984003533a6b67.png 2x" data-dominant-color="9899CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bill with cut</span><span class="informations">1236×896 89.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is what the segment looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97ff65c05d14f5a3fa3d92eb5dd018ebf28aee3d.png" data-download-href="/uploads/short-url/lGDhDWQEfaGxbjBG2bBBRqCWBU9.png?dl=1" title="segment I cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ff65c05d14f5a3fa3d92eb5dd018ebf28aee3d_2_678x500.png" alt="segment I cut" data-base62-sha1="lGDhDWQEfaGxbjBG2bBBRqCWBU9" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ff65c05d14f5a3fa3d92eb5dd018ebf28aee3d_2_678x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ff65c05d14f5a3fa3d92eb5dd018ebf28aee3d_2_1017x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97ff65c05d14f5a3fa3d92eb5dd018ebf28aee3d.png 2x" data-dominant-color="999CCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment I cut</span><span class="informations">1230×906 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am curious when I measure in Segment Statistics, it looks like this segment is more of a modified cylinder than planar.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a789cc9ff9d6ce6330bad24780744c9ec276e04c.png" data-download-href="/uploads/short-url/nU6Ydrd3Ep8laaw1LX3bypsP2hu.png?dl=1" title="segment measurement" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a789cc9ff9d6ce6330bad24780744c9ec276e04c_2_674x500.png" alt="segment measurement" data-base62-sha1="nU6Ydrd3Ep8laaw1LX3bypsP2hu" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a789cc9ff9d6ce6330bad24780744c9ec276e04c_2_674x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a789cc9ff9d6ce6330bad24780744c9ec276e04c_2_1011x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a789cc9ff9d6ce6330bad24780744c9ec276e04c.png 2x" data-dominant-color="5D5E76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment measurement</span><span class="informations">1251×928 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That makes me wonder if it measuring the SA of this whole column. Is there a setting I can use to make this more planar and only measure the SA of the dorsal side of the bill from this segment cut? Perhaps this is just what happens when I’m measuring a curved surface where the points do not exist on one consistent plane longitudinally.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>surfaceMarkup type (which allows you draw a surface patch, as opposed to a curve) will be more flexible and usable. Here is an example. The gray is the surface patch generated by this 3x3 grid, and it follows the curvature of the skull roof closely.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I was able to replicate your point locations, more or less, with the surfaceMarkup method.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9318ebaa3809fc2886bcc5e7d89f3e4dc400965d.png" data-download-href="/uploads/short-url/kZhzYniabK5qVy4tpsiTqg1IB4x.png?dl=1" title="unconstrained" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9318ebaa3809fc2886bcc5e7d89f3e4dc400965d_2_690x350.png" alt="unconstrained" data-base62-sha1="kZhzYniabK5qVy4tpsiTqg1IB4x" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9318ebaa3809fc2886bcc5e7d89f3e4dc400965d_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9318ebaa3809fc2886bcc5e7d89f3e4dc400965d_2_1035x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9318ebaa3809fc2886bcc5e7d89f3e4dc400965d_2_1380x700.png 2x" data-dominant-color="77798F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unconstrained</span><span class="informations">1918×973 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am having trouble constraining the points to the model. I have attached a screen shot of what my settings are. I’m wondering if it is something with my projection distance, or something limiting it from “snapping” to my model. Would love any input on this with the sample data, then I’ll try it on the bill.</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
I tried the method you outlined. From a model, I was able to use the dynamic modeler to create a new model from selected points<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c93511b5b864c250b051cd9b59f18b35190ced2d.png" data-download-href="/uploads/short-url/sHXFEdkb6uTwAgtIhW25vmoR1bD.png?dl=1" title="on bill" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c93511b5b864c250b051cd9b59f18b35190ced2d_2_689x466.png" alt="on bill" data-base62-sha1="sHXFEdkb6uTwAgtIhW25vmoR1bD" width="689" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c93511b5b864c250b051cd9b59f18b35190ced2d_2_689x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c93511b5b864c250b051cd9b59f18b35190ced2d_2_1033x699.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c93511b5b864c250b051cd9b59f18b35190ced2d.png 2x" data-dominant-color="9491C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">on bill</span><span class="informations">1212×820 67.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The issue is, because there are other surfaces within my sphere size (0.5), I am getting multiple surfaces from this method<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b894c0862096740ffaaee864a2d2a56bc6f90e5a.png" data-download-href="/uploads/short-url/qkSymVLuaXkONsJ1vYTdrdMh5xM.png?dl=1" title="model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b894c0862096740ffaaee864a2d2a56bc6f90e5a_2_667x500.png" alt="model" data-base62-sha1="qkSymVLuaXkONsJ1vYTdrdMh5xM" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b894c0862096740ffaaee864a2d2a56bc6f90e5a_2_667x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b894c0862096740ffaaee864a2d2a56bc6f90e5a_2_1000x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b894c0862096740ffaaee864a2d2a56bc6f90e5a.png 2x" data-dominant-color="9A9CD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model</span><span class="informations">1076×806 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Model SA measurements work great, but having trouble with this as it is likely giving me SA of all these surfaces.<br>
Let me know if you have any thoughts to pursue this method. I think Murat has some other ideas too, I’m trying them all right now to create a helpful workflow.</p>
<p>I really appreciate the help!</p>

---

## Post #11 by @mau_igna_06 (2022-03-23 18:51 UTC)

<p>I think you could change the algorithm to ‘geodesic’ on the selectByPoints tool options to avoid the problem you show.</p>
<p>Let me know if you achieve it</p>

---

## Post #12 by @muratmaga (2022-03-23 19:34 UTC)

<aside class="quote no-group" data-username="Rosalee_Elting" data-post="9" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>I was able to replicate your point locations, more or less, with the surfaceMarkup method.</p>
</blockquote>
</aside>
<p>Points will snap to the surface once they are close enough. Most of your points are currently inside the model. Turn the model so that you are seeing lateral view approximately, Turn off the model, and drag the points that are inside the skull such that they are way outside, then reposition them. Particularly the ones that are in the middle of the patch.</p>

---

## Post #13 by @Rosalee_Elting (2022-03-24 00:11 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> This helped with getting the points on the surface, thank you! It looks like I can start with a small grid, then “resample” with a larger grid to get more points and adjust them to the surface. I assume when this is a stable release the SA measurements might be available?</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> Geodesic did help! Thank you. The only small barrier I still have is getting the circles around the points to go to the edge of the bill, but not spill into the intraoral space (currently looks “scalloped” on the edge. Still multitudes better than the other methods I’ve been trying, but let me know if you have any thoughts there.</p>

---

## Post #14 by @mau_igna_06 (2022-03-24 00:39 UTC)

<p>The dynamic modeler tool is based on a vtk geodesic filter.</p>
<p><a href="https://www.vtkjournal.org/browse/publication/891" class="onebox" target="_blank" rel="noopener">https://www.vtkjournal.org/browse/publication/891</a></p>
<p>There is the option “exclusion region” that you could use around your area of interest drawn with a markups closed curve. You just need to put a seed point inside it using a fiducial.<br>
You just need to use the filter inside Slicer on python by <code>slicer.vtkFastMarchingGeodesicFilter</code> and set the proper inputs by converting the data. You should be able to get your surface of interest extracted and then assing it to a model, after that you can check on the Models module the surface area.</p>
<p>If you need more help you can contact me privately and I think I could work on a reusable script for this</p>

---

## Post #15 by @muratmaga (2022-03-24 01:21 UTC)

<aside class="quote no-group" data-username="Rosalee_Elting" data-post="13" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>I assume when this is a stable release the SA measurements might be available?</p>
</blockquote>
</aside>
<p>I don’t know the answer to that. Maybe <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can tell if and when that would be available.</p>

---

## Post #16 by @lassoan (2022-03-24 05:05 UTC)

<p>Use the latest Slicer Preview Release, as it contains many fixes and improvements that you’ll need.</p>
<p>I would recommend the following steps:</p>
<ul>
<li>Make your segment solid (get rid of internal holes due to air and packing material) to make all subsequent processing steps faster and more robust. You can use <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSolidify extension</a> for this.</li>
<li>Export the segmentation to a model. Segmentation is always a closed surface, so segment statistics would provide the surface area as the sum of the upper beak + lower beak + capping, which would not be useful. If you export the segmentation to a model then you can trim the surface model to the surface region that you want to measure.</li>
<li>Separate the lower and upper beak and remove the capping using Dynamic modeler module. The best is to use the <code>Curve cut</code> tool as it allows you to draw the boundary using a couple of control points, so the edge will be clean and straight. You can constrain the cutting curve to the model (in Markups module → Curve settings → Constrain to model → select the model exported from the segmentation) to make editing easier. For fine-tuning the curve you may resample the control points at equal distances along the curve (Markups module → Resample).</li>
<li>Go to Models module → Information section to get the surface area.</li>
</ul>

---

## Post #17 by @Rosalee_Elting (2022-03-25 22:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> This workflow is fantastic for my project, thank you! I just successfully created a model of the dorsal surface of this bill. Thanks to you all for the catered help, I really appreciate this forum and learning some new tools.</p>

---

## Post #18 by @KaiWei_Han (2023-11-24 01:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="22645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend the following steps:</p>
<ul>
<li>Make your segment solid (get rid of internal holes due to air and packing material) to make all subsequent processing steps faster and more robust. You can use <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify" rel="noopener nofollow ugc">SurfaceWrapSolidify extension </a> for this.</li>
<li>Export the segmentation to a model. Segmentation is always a closed surface, so segment statistics would provide the surface area as the sum of the upper beak + lower beak + capping, which would not be useful. If you export the segmentation to a model then you can trim the surface model to the surface region that you want to measure.</li>
<li>Separate the lower and upper beak and remove the capping using Dynamic modeler module. The best is to use the <code>Curve cut</code> tool as it allows you to draw the boundary using a couple of control points, so the edge will be clean and straight. You can constrain the cutting curve to the model (in Markups module → Curve settings → Constrain to model → select the model exported from the segmentation) to make editing easier. For fine-tuning the curve you may resample the control points at equal distances along the curve (Markups module → Resample).</li>
<li>Go to Models module → Information section to get the surface area.</li>
</ul>
</blockquote>
</aside>
<p>Fantastic method！ I just want to appreciate my thanks to you. This method solved a long disturbing problem for me. Than you very much.</p>

---
