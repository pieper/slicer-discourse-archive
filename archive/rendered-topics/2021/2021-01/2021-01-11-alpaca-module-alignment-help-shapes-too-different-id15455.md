# ALPACA module alignment help - shapes too different?

**Topic ID**: 15455
**Date**: 2021-01-11
**URL**: https://discourse.slicer.org/t/alpaca-module-alignment-help-shapes-too-different/15455

---

## Post #1 by @bobkallal (2021-01-11 14:50 UTC)

<p>Hi,</p>
<p>I’m working some some sclerites that lack obvious landmarks that lend themselves to conventional landmarking and want to attempt to use the ALPACA module. I have surface meshes (.ply), with segmentations performed in a different program. I’ve used PseudoLMGenerator on my template specimen, using the ellipse geometry and the midline/sagittal plane. I’m not as concerned with the number of landmarks for now - I just want it working before making those decisions. I will note that, as it is bilaterally symmetrical, I am following a protocol for other sclerites where I perform a GPA on all points then use only half for downstream analyses to avoid midline artifacts. In the image, we are looking at the right side of the structure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd9b9d166ede30f5a4f136d2c7d86bab9ac9a9c6.png" data-download-href="/uploads/short-url/r3lDQ1oJeCcAp6c4hxXEiHsWIcu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd9b9d166ede30f5a4f136d2c7d86bab9ac9a9c6_2_498x500.png" alt="image" data-base62-sha1="r3lDQ1oJeCcAp6c4hxXEiHsWIcu" width="498" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd9b9d166ede30f5a4f136d2c7d86bab9ac9a9c6_2_498x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd9b9d166ede30f5a4f136d2c7d86bab9ac9a9c6_2_747x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd9b9d166ede30f5a4f136d2c7d86bab9ac9a9c6.png 2x" data-dominant-color="BE969F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">986×989 58.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I exported the SymmetricPseudoLandmarks file as a fiducial csv to be used in ALPACA. I have chosen a target mesh for a single alignment that is not too different from the template (but some differ considerably).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/104361354713d38a1de2da6600c038c3d107180e.jpeg" alt="alpaca_forum2" data-base62-sha1="2jRZZEv4nMsUaOWUwRkNzXn2iLA" width="367" height="267"></p>
<p>I see from the Porto et al preprint that the two meshes do not have to be oriented in the same way. In the tutorial, it notes the ‘Select Subsampling Voxel Size’ is important but I don’t have it on my interface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fea8b95be4bc98faf3061324cc693d3b5c41a49e.jpeg" data-download-href="/uploads/short-url/AkOLyOFCDuK0crvpZq9CciFQYgu.jpeg?dl=1" title="alpaca_forum3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fea8b95be4bc98faf3061324cc693d3b5c41a49e_2_690x491.jpeg" alt="alpaca_forum3" data-base62-sha1="AkOLyOFCDuK0crvpZq9CciFQYgu" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fea8b95be4bc98faf3061324cc693d3b5c41a49e_2_690x491.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fea8b95be4bc98faf3061324cc693d3b5c41a49e_2_1035x736.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fea8b95be4bc98faf3061324cc693d3b5c41a49e_2_1380x982.jpeg 2x" data-dominant-color="B2B2D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alpaca_forum3</span><span class="informations">1823×1299 97.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Anyway, I perform the subsampling and alignment, and the result is below. The two structures do not seem aligned to me. I also selected another target, with similar results (third image).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/958fc043c73bb3d80d53f7dc5a4b2da4e676551f.png" alt="image" data-base62-sha1="ll57X3GIZqJge6nD1N5vZlNCYhh" width="551" height="482"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f046ec03ee1376c0d659ab2f1114d4d3d0f59d4.jpeg" alt="alpaca_forum5" data-base62-sha1="bh1dsc2FVMjCTm52SqaEVuEt9U8" width="557" height="426"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e8258a489eabb8b7a02fae8d4cd05bd6463363b.jpeg" alt="alpaca_forum6" data-base62-sha1="bcwvvN6cR1gg2E2JuOFRR2r7dkT" width="443" height="359"></p>
<p>Am I missing some step, or need to change some options? Here are my questions to try to make this work:</p>
<p>1 - Do I need to manually change the registration for each sclerite such that they are oriented with anterior being anterior, dorsal being dorsal, etc for this to work? And if so, how do I do that?</p>
<p>2 - If that is not the case, do options do you recommend toggling in the ALPACA advanced parameter settings?</p>
<p>3 - Something else I’m not thinking of?</p>
<p>Thank you!<br>
Bob</p>

---

## Post #2 by @muratmaga (2021-01-11 20:15 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a> in general if geometries are too different then most automated alignment methods will not perform well. We don’t see the full picture and hard to tell the shapes, but snapshot 1 and 2 seems like a reasonable alignment from that angle.</p>
<p>It is correct that starting positions shouldn’t make difference in ALPACA, but we also didn’t test it with such different shapes. If you are worried that their orientation is making an impact in the alignment, you can manually transform one of the meshes to a closer orientation either by Transforms module or perhaps identifying 3-4 points on both meshes, and use that IGT Fiducial Registration (rigid option). After hardening the transform you can give another try with ALPACA with this new set.</p>
<p><a class="mention" href="/u/agporto">@agporto</a> can you comment on this?</p>

---

## Post #3 by @agporto (2021-01-11 21:06 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a>  First, just to answer your questions:</p>
<ol>
<li>
<p>There is no need to perform manual alignment for ALPACA. It should handle differences in orientation.</p>
</li>
<li>
<p>I would increase the point density (using advanced settings). Right now, you are sampling each mesh using around 1,500 points. I would aim to somewhere between 4,000 and 5,000 points.</p>
</li>
</ol>
<p>As <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned, I think the first alignment doesn’t look too bad. Increasing the point density will probably get you there. The last example, on the other hand, just seems to be a consequence that the two shapes are too different. Visually ,I can’t even tell how they should be aligned.</p>
<p>When you have shapes that are too dissimilar, one option would be to use more than one template. Since you are using pseudolandmarks, I am not sure whether that would be possible. But if it is, it might be worth considering.</p>

---

## Post #4 by @bobkallal (2021-01-11 21:22 UTC)

<p>Thank you both.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I will check out the Transforms module again. I was poking around this module over the weekend and I think for what I want - please correct me if I’m wrong - I want the ‘create new transform’ function in active transform? Specifically, if I want my surface to be oriented as in the first image such that the rightmost cylindrical part is anterior, the top is dorsal/superior, etc, would that be the way to go about it?</p>
<p><a class="mention" href="/u/agporto">@agporto</a> It can still ‘figure out’ differences when the shapes are so different but with different initial alignments? I see point density adjustment is 1.5 as default and goes up to 3. Am I looking at the wrong thing? I must me, as when I max it out to 3, the two pointclouds don’t even overlap, though they do seem more or less in a closer orientation. What do you advise to increase to 5,000 points?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e58629629b11aebe0d8182fa3e481be3ba3c983.png" data-download-href="/uploads/short-url/kjfaejLTPp6ZUWPinIIDXsdXwCn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e58629629b11aebe0d8182fa3e481be3ba3c983_2_690x318.png" alt="image" data-base62-sha1="kjfaejLTPp6ZUWPinIIDXsdXwCn" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e58629629b11aebe0d8182fa3e481be3ba3c983_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e58629629b11aebe0d8182fa3e481be3ba3c983_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e58629629b11aebe0d8182fa3e481be3ba3c983_2_1380x636.png 2x" data-dominant-color="A5A4CF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1040 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you both again!<br>
Bob</p>

---

## Post #5 by @agporto (2021-01-11 21:29 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a> Something is odd. You increased the point density, but the output box under ‘Run subsampling’ is still showing the same number of points. That should not happen. I suggest restarting Slicer. If the behavior continues, would you be willing to share the meshes with me? I can investigate it further to see what might be causing. But please try restarting Slicer first.</p>

---

## Post #6 by @agporto (2021-01-11 21:30 UTC)

<p>And just to be clear, when advanced parameters are changed, you have to rerun the entire pipeline again (including run subsampling)</p>

---

## Post #7 by @bobkallal (2021-01-11 21:37 UTC)

<p>Thank you. When I run at 1 for point density adjustment, I get the below image. Increasing from 1 to 3 only gains 200-300 points. How do you recommend I get to 5000 points? If you’d like me to share or have another idea, please let me know!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3df733c9548dc1c10d91c827a40ad91727884133.png" data-download-href="/uploads/short-url/8QaKL07ils8bk4grXzDd7mSkWoX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3df733c9548dc1c10d91c827a40ad91727884133_2_521x500.png" alt="image" data-base62-sha1="8QaKL07ils8bk4grXzDd7mSkWoX" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3df733c9548dc1c10d91c827a40ad91727884133_2_521x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3df733c9548dc1c10d91c827a40ad91727884133_2_781x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3df733c9548dc1c10d91c827a40ad91727884133_2_1042x1000.png 2x" data-dominant-color="BFBACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1254×1202 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @agporto (2021-01-11 21:46 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a> Very odd. Increasing the point density to 3 should increase the number of points to much more than 5,000. If you are willing to share two example meshes, you can contact me at [edited] . I can investigate it further and see if I can reason what might be happening.</p>

---

## Post #9 by @lassoan (2021-01-11 21:59 UTC)

<aside class="quote no-group" data-username="agporto" data-post="8" data-topic="15455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/agporto/48/8319_2.png" class="avatar"> agporto:</div>
<blockquote>
<p>you can contact me at</p>
</blockquote>
</aside>
<p>FYI, you don’t need to disclose your email address publicly here but people can send you private messages via the forum (by clicking on your name then on the “Message” button).</p>

---

## Post #10 by @agporto (2021-01-11 22:00 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a> One thing that occurred to me is that your meshes might only have 1,800 vertices total, in which case you won’t be sample more than that.</p>

---

## Post #11 by @agporto (2021-01-11 22:00 UTC)

<p>That is good to know. Thanks, Andras!</p>

---

## Post #12 by @bobkallal (2021-01-11 22:37 UTC)

<p>Thank you. That might also be the case as these are very small structures that have been simplified. Still, I will send you the information and see what you think. I really appreciate any insight you may have!<br>
Bob</p>

---

## Post #13 by @bobkallal (2021-01-20 17:16 UTC)

<p>Hi everyone - thank you all again and especially Arthur. It seems like the surfaces are pretty different and ALPACA might not be the best tool, so I’m looking to auto3Dgm now. I definitely used it over the summer workshop session. I have a folder with the 5 example .ply surfaces and an output directory designated, but nothing happens when I try to load the data. I know the mosek license is required, and that should still be in the same (right?) place. What am I missing? Thank you for your continued help and patience.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d2849a4357bf9c028baaa4ce93894102d6834e.png" data-download-href="/uploads/short-url/sNp0gkR6rcVBLBgmcVroiF2Bc3c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d2849a4357bf9c028baaa4ce93894102d6834e.png" alt="image" data-base62-sha1="sNp0gkR6rcVBLBgmcVroiF2Bc3c" width="690" height="91" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1151×152 6.26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @muratmaga (2021-01-20 17:22 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a> you do need to acknowledge that none of these method work well if structures are very different.</p>
<p>As for the auto3Dgm, nothing has changed since the summer workshop. Probably the best thing for troubleshoot is to see if the summer example works, and if it does see where the issue arises with your data.</p>
<p>In the summer workshop, we followed the instructions provided by auto3Dgm team. <a href="https://toothandclaw.github.io/how-to-use/" class="inline-onebox" rel="noopener nofollow ugc">How to use - Slicer Auto3dgm</a>. There is also a <a href="https://www.dropbox.com/sh/sv8328dvpczezkk/AAAfNHWUL5HThQHG1wGNUdNua?dl=0&amp;preview=Auto3dgm_tutorial.mp4" rel="noopener nofollow ugc">video tutorial</a></p>

---

## Post #15 by @bobkallal (2021-01-20 17:40 UTC)

<p>Thank you, Murat. I acknowledge that different shapes are a challenge indeed.</p>
<p>As you suggested, I was trying to do the 5 example ply surfaces following the linked tutorial prior to trying my own data (as screenshot below). Those 5 example surfaces from the summer example are the ones not loading. I’ll review the tutorial video to see if that sheds any light on why it is not loading the surfaces.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/816ad8e661a0080b55a9567c1279c659e9fa8817.png" data-download-href="/uploads/short-url/isSvNzZtLJCH3zAvFBAAr7EDeE7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/816ad8e661a0080b55a9567c1279c659e9fa8817.png" alt="image" data-base62-sha1="isSvNzZtLJCH3zAvFBAAr7EDeE7" width="690" height="205" data-dominant-color="F1F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">774×231 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @muratmaga (2021-01-20 18:00 UTC)

<p>can you open the python terminal and type<br>
import mosek<br>
and see if it turns an error.<br>
Also can you post an error log (CTRL +0) after you completed these steps, perhaps there is an error/warning that might be helpful. I don’t think auto3Dgm team actively monitors the forum, so I will get in touch with them offline.</p>

---

## Post #17 by @muratmaga (2021-01-20 18:32 UTC)

<p>FYI, I ran auto3Dgm successful with the latest stable, once I installed the mosek license. This was on windows.</p>

---

## Post #18 by @lassoan (2021-01-20 18:33 UTC)

<p>If you have trouble with matching very different shapes, you might try <a href="https://github.com/SlicerRt/SegmentRegistration">SegmentRegistration extension</a>, which computes a warping transform between distance map of the two shapes. The module requires segmentation as input, so you need to right-click on the model node in Data modue to convert it to segmentation node. This transform provides full spatial mapping between the two shapes, so you can use it to transform landmarks from one model to the other. It is a pairwise registration only, but it may be used to register all shapes to some template or maybe combined with other groupwise methods.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Do you know groupwise shape registration and analysis tools in <a href="http://salt.slicer.org/">SlicerSALT extension</a>? Could they be useful here?</p>

---

## Post #19 by @bobkallal (2021-01-20 20:03 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Hi - I think I found out what it was and - of course - it was something wrong on my end. When I tried ALPACA last week, I had to change Slicer from version 4.11.0 that I used over the summer to 4.11.2 because 4.11.0 didn’t have the PseudoLMGenerator module as an option. It seems to be working now. Thank you.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you, I will see about the SegmentRegistration extension if auto3Dgm has trouble. I do have only ply for my files, but if you can convert then I’ll give it a go.</p>
<p>I wonder, though, given the disparity of the structures, is it even wise to continue to try to do morphometric analyses of them? Would I be inherently inviting issues and criticisms?</p>

---

## Post #20 by @muratmaga (2021-01-20 20:27 UTC)

<aside class="quote no-group" data-username="bobkallal" data-post="19" data-topic="15455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/838e76/48.png" class="avatar"> bobkallal:</div>
<blockquote>
<p>I wonder, though, given the disparity of the structures, is it even wise to continue to try to do morphometric analyses of them? Would I be inherently inviting issues and criticisms?</p>
</blockquote>
</aside>
<p>This is something you as an expert have to convince yourself (and potentially your reviewers). Keep in mind most automated analyses are designed in context of single species. For example in clinical imaging, corpus callosum is a corpus callosum, however deformed it might be due to genetic or environmental factors. As long as algorithms align those structures in reasonable orientations, there is a biological basis of that comparison.</p>
<p>Things get complicated in multi-species context, particularly when someone uses a structure like ‘skull’ which is actually derived from many independent bones and growth centers. Continuing this example, if you align a point cloud of pseudolandmarks derived from a mouse skull to a cat skull (e.g., using ALPACA, or with SegmentRegistration), you will get <code>a result</code>. Because there are no inherent constrains on this warping, then some points that were originally on the nasal bone in the template (because mice have elongated nasals compared to cats), may end up on the frontal in the cat skull. While this is a naive example, it tries to highlight using fully automated shape analyses in multi-species, evolutionary context. We develop and continue to use ALPACA for population level problems in model organisms or in single species. I haven’t used SlicerSALT for a while, but it used to have the same kind of issue.</p>
<p>At this point if you, as an expert, cannot identify corresponding structures in your samples (however few they might be) visually or from developmental biology or literature, I wouldn’t expect the automated procedures to do a very good job. And particularly for shape analysis as you wouldn’t have any means to evaluate whether that results make sense or not.</p>

---

## Post #21 by @bobkallal (2021-01-20 20:52 UTC)

<p>Thank you. You put more eloquently the fragments of the thoughts I’m having myself. Luckily my issue now involves a single sclerite that is self-contained and not touching another sclerite (that is, has no subdivisions like a skull), but it doesn’t seem like that will save me. I suppose even a 2D analysis using elliptical Fourier transform would need at least one homologous point too.</p>

---

## Post #22 by @muratmaga (2021-01-20 21:06 UTC)

<p><a class="mention" href="/u/bobkallal">@bobkallal</a> sorry don’t know the first thing about arthropods, so take everything with a good grain of salt.</p>
<p>I think you should experiment some and see how it works. It is part of the exploring the data. The point I am trying to make is be always aware of the issues and be critical of results. A combination of using your expert knowledge and some automated process might actually work. Perhaps at some point we might consider taking a set of landmarks as constrains on the mesh alignment in ALPACA (<a class="mention" href="/u/agporto">@agporto</a>), but at this point it is not possible.</p>

---

## Post #23 by @lassoan (2021-01-20 22:41 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="22" data-topic="15455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>we might consider taking a set of landmarks as constrains on the mesh alignment</p>
</blockquote>
</aside>
<p>Some of the SlicerSALT tools support this. For example, we rely on landmarks for shape analysis of heart valve leaflets (which all look like slightly bent somewhat circular disks).</p>

---

## Post #24 by @muratmaga (2021-01-20 22:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="15455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Some of the SlicerSALT tools support this.</p>
</blockquote>
</aside>
<p>Thanks Andras. We might get some clues from there. <a class="mention" href="/u/agporto">@agporto</a> <a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---
