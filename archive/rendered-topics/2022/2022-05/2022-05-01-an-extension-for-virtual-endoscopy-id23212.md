# An extension for virtual endoscopy

**Topic ID**: 23212
**Date**: 2022-05-01
**URL**: https://discourse.slicer.org/t/an-extension-for-virtual-endoscopy/23212

---

## Post #1 by @gaoyi.cn (2022-05-01 08:06 UTC)

<p>Dear All,</p>
<p>We already have an Endoscopy module in Slicer. However that requires the lumen being already segmented. I have been working on a module which performs the centerline extraction followed by lumen segmentation, for pancreatic duct (it can be used for other lumens too). This may be a useful module for lumen analysis.</p>
<p>I have not made a demonstration webpage yet, just have the repository at:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/gaoyi/VirtualEndoscopy">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/gaoyi/VirtualEndoscopy" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/00a42e0991ea7fba0b84e6dfdbd932d3cc2a8c4c369e9d6580683c16cc83a79d/gaoyi/VirtualEndoscopy" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/gaoyi/VirtualEndoscopy" target="_blank" rel="noopener nofollow ugc">GitHub - gaoyi/VirtualEndoscopy</a></h3>

  <p>Contribute to gaoyi/VirtualEndoscopy development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m hoping to add this through the extension management system and would like to hear about your suggestions/opinions.</p>
<p>Thanks!<br>
yi</p>

---

## Post #2 by @pieper (2022-05-02 16:53 UTC)

<p>You have all kinds of cool projects, thanks Yi!</p>
<p>If you haven’t already seen it should have a look at Delphine Naine’s master’s thesis, one of the original driving use cases for Slicer.  It would be great to see some of that functionality come back.</p>
<p><a href="https://dspace.mit.edu/handle/1721.1/87240" class="onebox" target="_blank" rel="noopener">https://dspace.mit.edu/handle/1721.1/87240</a></p>

---

## Post #3 by @Kedar_Hibare (2022-05-03 04:41 UTC)

<p>I am very interested in your work. Thank you for sharing</p>
<p>May I ask / suggest this would be very useful for us for the lung to map the airways … especially if there is a nodule to which we have to reach endoscopically. Often these nodules are peripheral (outer one third of the lung) as since the airways get narrow and branch it’s difficult to reach them with confidence. There is a ton of new equipment being pumped by many companies into this technology (Lung point, Electromagnetic navigation, Robotic bronchoscopy, Cone Beam CT etc etc ) but for a low cost setting / open source we have very little… it would be ideal if you could help design something which will help navigate the airways to a lesion of interest with your background work on Pancreas</p>
<p>Happy to hear from you</p>
<p>Warm Regards<br>
Dr Kedar Hibare<br>
<a href="mailto:kedarhibare@gmail.com">kedarhibare@gmail.com</a></p>

---

## Post #4 by @gaoyi.cn (2022-05-03 06:20 UTC)

<p>Hi Steve,</p>
<p>Of course I remember Delphine’s great work. I still remember using that module in the Tcl/Tk based Slicer 1.6 version. <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<p>Best,<br>
yi</p>

---

## Post #5 by @gaoyi.cn (2022-05-03 06:21 UTC)

<p>Hi Dr. Hibare,</p>
<p>Sure! I believe it should be straightforward to extend such a module to the airway endoscopy. I’ll work on that.</p>
<p>Thanks for your suggestion!</p>
<p>Best,<br>
yi</p>

---

## Post #6 by @whu (2022-05-11 14:17 UTC)

<p>Dear Professor Gao:</p>
<pre><code>   Can you share some pictures about the result  of the virtual endoscopy project?
 
    thanks</code></pre>

---

## Post #7 by @lassoan (2022-05-12 03:10 UTC)

<p>Thanks a lot for submitting these extensions!</p>
<p>There is some overlap with the VMTK extension, which offers an opportunity in reducing maintenance workload. For example, VMTK can compute vesselness, segment lumen automatically using a few simple methods, and create a centerline tree. The tree is compatible with curves module so that you can automatically find the shortest path between two points (maybe the tree that your modules extract could be used, too):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UpfDP6ejCjg" data-video-title="Finding shortest path between two points in the bronchial tree" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UpfDP6ejCjg/maxresdefault.jpg" title="Finding shortest path between two points in the bronchial tree" width="" height="">
  </a>
</div>

<p>The resulting tree in the Slicer core Endoscopy module (if your modules create a curve node as output then that can be used there, too).</p>
<p>We should review what is common between existing and new modules and how to consolidate them, so that they combine all the good properties and features.</p>
<p>What is in the <code>gth818n</code> folder?<br>
What does <code>SegmentLumenFromAxis</code> module do?<br>
How the VIrtualEndoscopy module differs from the Endoscopy module in Slicer core? Could they be merged into a single module?<br>
Could we make some segmentation features available in the Segment Editor as effects?</p>
<p>These could be all great projects for the upcoming project week.</p>

---

## Post #8 by @whu (2022-05-16 16:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/692bdd8fbf4e059cffd3618418d5246122845ad6.png" data-download-href="/uploads/short-url/f0o7aUPZcMApN1mItkzTAjCAMrI.png?dl=1" title="ss" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/692bdd8fbf4e059cffd3618418d5246122845ad6_2_690x163.png" alt="ss" data-base62-sha1="f0o7aUPZcMApN1mItkzTAjCAMrI" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/692bdd8fbf4e059cffd3618418d5246122845ad6_2_690x163.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/692bdd8fbf4e059cffd3618418d5246122845ad6_2_1035x244.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/692bdd8fbf4e059cffd3618418d5246122845ad6.png 2x" data-dominant-color="E8E7DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss</span><span class="informations">1188×282 50.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="23212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a href="https://dspace.mit.edu/handle/1721.1/87240" rel="noopener nofollow ugc">https://dspace.mit.edu/handle/1721.1/87240</a></p>
</blockquote>
</aside>
<p>And this paper for short:   Nain D. An interactive virtual endoscopy tool with automotive path generation[D]. Massachusetts Institute of Technology, 2002.<br>
Shows the centerline idea.<br>
This does not affect the innovation of the project。</p>

---

## Post #9 by @gaoyi.cn (2022-06-24 14:08 UTC)

<p>I agree. there might be some overlapping the the VMTK package.</p>
<p>I recall that I had some discussion with Luca back in the old days that VMTK is computing the vessel lumen surface using level set evolution, then computing the center line from from the lumen segmentation. I thought that such level set evolution that perfectly grabbing the vessel without leaking is particularly hard except some high contrast cases such as the big air way wall.</p>
<p>In contrast, the Virtual Endoscopy module is computing the center line first and the “grow out” from the center line. This is what the “SegmentLumenFromAxis” dose.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20">  gth818n was my student ID back in Georgia Tech and I used it as a namespace storing my tools/functions…</p>
<p>The current Endoscopy assumes an already extracted surface. But both VMTK and the Virtual Endoscopy proposed here starts from volumetric image. They could be combined.</p>
<p>Also i agree that making an effect for centerline computation in Segment Editor would be a good idea. I’ll look into that.</p>
<p>I’ll check the wiki for the upcoming project week. Project week has always been so much fun!</p>
<p>Best,<br>
yi</p>

---

## Post #10 by @lassoan (2022-06-24 14:18 UTC)

<aside class="quote no-group" data-username="gaoyi.cn" data-post="9" data-topic="23212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>I thought that such level set evolution that perfectly grabbing the vessel without leaking is particularly hard except some high contrast cases such as the big air way wall.</p>
</blockquote>
</aside>
<p>Agreed. It only works for a single, very well contrasted vessel branch, but you can segment that using simple thresholding or grow from seeds, so I did not find the levelset method useful (other than it creates smoother surface). A few more segmentation tools were added to VMTK, but I did not have much luck using them either.</p>
<aside class="quote no-group" data-username="gaoyi.cn" data-post="9" data-topic="23212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>In contrast, the Virtual Endoscopy module is computing the center line first and the “grow out” from the center line. This is what the “SegmentLumenFromAxis” dose.</p>
</blockquote>
</aside>
<p>Growing segmentation from a manually defined curve could be a good approach for challenging cases. I would be interested to see if it can be used for segmentation of intestines.</p>
<aside class="quote no-group" data-username="gaoyi.cn" data-post="9" data-topic="23212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>The current Endoscopy assumes an already extracted surface. But both VMTK and the Virtual Endoscopy proposed here starts from volumetric image. They could be combined</p>
</blockquote>
</aside>
<p>I agree. We should split the functionalities so that we can pick any of the segmentation and centerline extraction methods and then use the created centerline for visualization (travel along the centerline).</p>
<p>The current Endoscopy module does not deal with centerline extraction and segmentation, so probably it could be left as is (or some features added from your endoscopy module, if anything is missing). For the segmentation from centerline we could add a Segment Editor effect, as you suggested. If you have time next week, then we could make this a project for the project week.</p>

---

## Post #11 by @gaoyi.cn (2022-06-24 14:27 UTC)

<p>Sounds great! I’ve just registered for the Project week. I’ll populate the project i’m planning to work on on the wiki.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="23212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but you can segment that using simple thresholding or grow from seeds</p>
</blockquote>
</aside>
<p>Yes I used the same algorithm in the “Grow From Seed” for lumen segmentation in SegmentLumenFromAxis.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="23212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would be interested to see if it can be used for segmentation of intestines.</p>
</blockquote>
</aside>
<p>I’ve tried that but found little luck… The intestine is very hard because the touching outer surfaces and the collapsed lumen make the recognition of the topology very hard even for human. So it’s even very hard to draw the seed.  It relatively easy for the inflated colon. It’s even hard to prepared colon (without inflation).</p>

---

## Post #12 by @pieper (2022-06-24 17:38 UTC)

<p>Great that you can join Project Week <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">  I really like the idea of a custom editor effect for vessels.  It would be great to have something interactive that traces tubular structures.</p>

---

## Post #13 by @lassoan (2022-06-25 04:57 UTC)

<p>We have “Draw tube effect” (in SegmentEditorExtraEffects extension), which can draw a uniform-radius tube in the selected segment. Maybe we could add a feature to this effect: snap the tube walls to the image content.</p>

---

## Post #14 by @gaoyi.cn (2022-11-07 07:01 UTC)

<p>I tried the “Draw tube effect” and it’s really nice. It seems to be purely determined by the fiducial points place, the image content is not affecting the tube trajectory.</p>
<p>The proposed extension has four possible “contact points” with the other modules:</p>
<ol>
<li>For tracing a curve in the image, you place n (&gt;=2) fiducial points along a tubular structure. Then the algorithm will trace from the n-th back to the 1st points, passing the most-vessel-like regions in the image. Comparing to the “Draw tube effect”, this module takes the image content into consideration. This module is useful when you want to trace out a single un-branched vessel/tube whose contrast with surrounding is poor, such as the pancreatic duct.</li>
</ol>
<p>For example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de3ee97279465ea621f925b0a6504618bf0c1306.jpeg" data-download-href="/uploads/short-url/vI4MLzHp3MNCUesMHEcJRo9rBci.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de3ee97279465ea621f925b0a6504618bf0c1306_2_690x415.jpeg" alt="image" data-base62-sha1="vI4MLzHp3MNCUesMHEcJRo9rBci" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de3ee97279465ea621f925b0a6504618bf0c1306_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de3ee97279465ea621f925b0a6504618bf0c1306_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de3ee97279465ea621f925b0a6504618bf0c1306_2_1380x830.jpeg 2x" data-dominant-color="989694"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1157 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>
<p>Once you have a major vessel traced out as a curve, the second module allows you to place m fiducial points, and then it will find a curve from each of the m points back to the curve, along the most-vessel-like regions. This is useful when you want to trace a “fish bone” type structure, such as the SMA, or the lower-limb vessels.</p>
</li>
<li>
<p>If you want trace a tree-type structure, such as coronary artery, where there is no long-running main thread with side branches like a fish-bone. You may want to try the 3rd module. Here you give n fiducial points and the algorithm will trace back from each point (from 2nd to n-th) back to the 1st point, independently.</p>
</li>
</ol>
<p>For example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0424f836126657df621437ab430db3a1c002120.jpeg" data-download-href="/uploads/short-url/tIlnMLOiDwO0qOoENIbYzJvajNS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0424f836126657df621437ab430db3a1c002120_2_690x378.jpeg" alt="image" data-base62-sha1="tIlnMLOiDwO0qOoENIbYzJvajNS" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0424f836126657df621437ab430db3a1c002120_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0424f836126657df621437ab430db3a1c002120_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0424f836126657df621437ab430db3a1c002120_2_1380x756.jpeg 2x" data-dominant-color="AA9C95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1053 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="4">
<li>Once you have the center-line/curve traced out, you want to extract the lumen from the center-curve. You run this 4th module. Essentially it runs a “grow from seed” growing out from the center-curve.</li>
</ol>
<p>In vmtk, the lumen is firstly segmented using level-set. This requires the image to have good contrast and relatively large diameter to allow the contour/surface to grow in. Then the center-curve is computed from the lumen.</p>
<p>Here the order is reversed and my experience is that sometimes it’s easier to find the center-curve first and then the lumen.</p>

---

## Post #15 by @rkikinis (2022-11-07 12:18 UTC)

<p>Hi Yi,<br>
Vessel segmentation is still a challenge. You are proposing an interesting approach.<br>
In your third proposed bullet item: How do you handle something like the pulmonary veins and arteries?<br>
Best<br>
Ron</p>

---

## Post #16 by @pieper (2022-11-07 13:19 UTC)

<p>I really like your approach <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a>.  Accurate vessel segmentation is important and hard with current tools.  What can we do to help?</p>

---

## Post #17 by @gaoyi.cn (2022-11-08 00:24 UTC)

<p>Hi Ron,</p>
<p>Thank you very much! Yes, pulmonary veins and arteries are tough. But not in the tracing step, instead, they are challenging in the vessleness characterization step. My understanding is that the Hessian based vesselness computation (such as the Frangi filter) relies on the implicit assumption that the diameter of the vessel being relatively constant, but that’s not the case the pulmonary vessels, whose diameters change dramatically in a very short distance.</p>
<p>We are facing this difficulty coz we are working on a pulmonary embolism detection and measurement project currently and doctors want to extract the vessels first. But I took the liberty of postponing that and detect the embolism regions first. <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=12" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:" loading="lazy" width="20" height="20"></p>
<p>The current form of this extension wouldn’t handle pulmonary vessels well. We are trying combining some deep learning segmentation with shape prior to see if that helps… Now knowing that you are interested in this, i’ll definitely keep you updated and asking for your advice on this project.</p>
<p>Best,<br>
yi</p>

---

## Post #18 by @gaoyi.cn (2022-11-08 00:32 UTC)

<p>Thank you Steve!</p>
<p>Since this extension contains several components that may potentially be interacting with several different parts in Slicer (tube segmentation in segmentation editor, vmtk, endoscopy), the path and integration approach of each may not be very clear right now. How about we first integrate these as a SlicerVesselAnalysisAndVirtualEndoscopy extension. We people are using them (hopefully), we can gather more information and hands-on experience on how to integrate it with the other modules?</p>
<p>Thank you for your advice!</p>
<p>Best,<br>
yi</p>

---

## Post #19 by @rkikinis (2022-11-08 13:32 UTC)

<p>Hi Yi,<br>
sounds good. Vessels have been one of my interests for a long time. But they are still a challenge.</p>
<p>Kikinis R, Jolesz FA, Gerig G, Sandor T, Cline HE, Lorensen WE, Halle M, Benton SA. 3D morphometric and morphologic information derived from clinical brain MR images. In: Proceedings of the NATO Advanced Workshop; June 1990; Travemuende, Germany. NATO ASI Series. 1990. p. 441-54.</p>
<p>Best</p>
<p>Ron</p>

---

## Post #20 by @pieper (2022-11-08 13:47 UTC)

<p>Yes, I like the plan of a high-level tool that builds on utilities from existing core Slicer code and extensions.</p>
<p>I’d be happy to look for a time to discuss this.   It could be a good topic for the upcoming <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/">Project Week</a> but it may also be practical to meet electronically as needed.</p>

---
