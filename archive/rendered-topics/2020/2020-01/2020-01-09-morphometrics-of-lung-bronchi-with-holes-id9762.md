---
topic_id: 9762
title: "Morphometrics Of Lung Bronchi With Holes"
date: 2020-01-09
url: https://discourse.slicer.org/t/9762
---

# Morphometrics of lung bronchi with holes

**Topic ID**: 9762
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/morphometrics-of-lung-bronchi-with-holes/9762

---

## Post #1 by @bobcieri (2020-01-09 19:54 UTC)

<p>Hi,</p>
<p>I am interested in using geometric morphometrics through the SlicerMorph to analyze shape differences in varanid lizard lungs. The lungs are complex but the main intrapulmonary airways are at the heart of the diversity of the structures and share some similarities. Attached here is a screenshot of an STL of these structures. I’ve done some geometric morphometrics on bones before, but how should I approach this strucuture? The size, shape, and position of the holes in the long tube is important and I’d like to capture the variation in these as they lead to secondary bronchi that carry unique airflow patterns. Would it be best to try and fill the holes and then measure the resulting filled flat surfaces that are where the holes used to be, or try and arrange the landmarks around the holes but not in them?</p>
<p>Thanks for your suggestions!</p>
<p>Bob<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27aa771b9b1da578d68906f4c2ee72eb4251a414.jpeg" data-download-href="/uploads/short-url/5ETQaHqEBAAZahUEX2nE22JRxBO.jpeg?dl=1" title="primary bronchus sreenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/27aa771b9b1da578d68906f4c2ee72eb4251a414_2_690x407.jpeg" alt="primary bronchus sreenshot" data-base62-sha1="5ETQaHqEBAAZahUEX2nE22JRxBO" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/27aa771b9b1da578d68906f4c2ee72eb4251a414_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/27aa771b9b1da578d68906f4c2ee72eb4251a414_2_1035x610.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/27aa771b9b1da578d68906f4c2ee72eb4251a414_2_1380x814.jpeg 2x" data-dominant-color="474584"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">primary bronchus sreenshot</span><span class="informations">1852×1094 52.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-01-09 20:15 UTC)

<p>This kind of data representation of the bronchial tree is highly unusual and very limited. I would recommend to segment the bronchial tree using “Segment Editor” module then extract centerline model using SlicerVMTK extension’s “Centerline computation” module. It creates a centerline tree, which you can interrogate by a bit of Python scripting (get statistics on number and positions of branching points, radius values, etc).</p>

---

## Post #3 by @muratmaga (2020-01-09 20:41 UTC)

<p>This type of structure is going to be quite difficult to analyze with landmark based geometric methods. As <a class="mention" href="/u/lassoan">@lassoan</a> indicated, one option is to see if there are metrics you can get out of VMTK that might be useful for your particular question. I have not done that type of analysis, but I assume will need to extract a more complete bronchial tree with the secondary branches attached to it (as oppose to pruned).</p>
<p>I was going to suggest you can turn it into a solid model (or a segmentation), and use something like SlicerSALT or Shapeworks to look at shape variability, but you seem to be interested in the position and distribution of the secondary structures, so I don’t think that will work…</p>

---

## Post #4 by @bobcieri (2020-01-10 18:58 UTC)

<p>Thanks for these suggestions - I am going to try and give VMTK a go. Will it be able to handle a non-bifurcating tree? Here is a screenshot of a more complete segmentation of the lung structure - obviously this is negative space that has been segmented. Would this sort of structure work better for morphometrics? Is it possible to put landmarks on the inside of a surface file? that would probably allow for reasonable capture of the bronchial tree structure.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eff0aa228749d64feb59302a63816cebcab6727.jpeg" data-download-href="/uploads/short-url/i7sAhHgnfu2mM2tEvKPyLWCmffp.jpeg?dl=1" title="full segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eff0aa228749d64feb59302a63816cebcab6727_2_690x377.jpeg" alt="full segmentation" data-base62-sha1="i7sAhHgnfu2mM2tEvKPyLWCmffp" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eff0aa228749d64feb59302a63816cebcab6727_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eff0aa228749d64feb59302a63816cebcab6727_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eff0aa228749d64feb59302a63816cebcab6727_2_1380x754.jpeg 2x" data-dominant-color="313030"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">full segmentation</span><span class="informations">2250×1230 777 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-01-10 22:33 UTC)

<aside class="quote no-group" data-username="bobcieri" data-post="4" data-topic="9762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bobcieri/48/5633_2.png" class="avatar"> bobcieri:</div>
<blockquote>
<p>Will it be able to handle a non-bifurcating tree?</p>
</blockquote>
</aside>
<p>VMTK (and all tree segmentation methods) require a tree.</p>
<p>How did you create this trimmed model? Normally you would segment the bronchial tree on the volumetric image and compute metrics from that.</p>
<p>If you have hundreds of trimmed models like this already then you can write a script that processes them as they are: there are VTK filters for getting boundary edges and the rest of the processing should be fairly straightforward. Otherwise, I would start all processing with manual/semi-automatic 3D segmentation and automatically compute everything else from this segmentation.</p>

---

## Post #6 by @bobcieri (2020-01-10 23:09 UTC)

<p>Both the trimmed models I’ve shown are generated from a segmentation of an image stack volume (CT scan). I’d like to try and make comparisons betwen 7 species (not hundreds of trees!). I’ll work to compute from the segmentations. Segmentation was done in Avizo but I can export to Slicer or re-segment.</p>

---

## Post #7 by @muratmaga (2020-01-11 06:47 UTC)

<p>That segmentation looks like a lot of work. I am not sure what formats Avizo export but if it does NRRD or Nifti (nii), you should be able to import your volume and your segmentation to continue working in Slicer.</p>
<p>I guess I am not sure why these bronchii doesn’t look like a tree. I am not sure about this species, but doesn’t supposed to look like something more or less like this?<br>
          <iframe src="https://sketchfab.com/models/3379f97524aa412c8736f65e2ae609cc/embed?" width="695" height="521" scrolling="no" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>

---

## Post #8 by @bobcieri (2020-01-11 14:33 UTC)

<p>The bronchi of reptiles and birds don’t look at all like mammals which is why they are interesting - the air doesn’t take a tidal path through the lung.  In mammals, the air goes down the bronchi to alveoli and takes the same path out. In these animals, the air takes a different path in and out of the lung and some sections of the lung contain unidirectional flow. See our work here.</p>
<p><a href="https://anatomypubs.onlinelibrary.wiley.com/doi/abs/10.1002/ar.24293" rel="nofollow noopener">https://anatomypubs.onlinelibrary.wiley.com/doi/abs/10.1002/ar.24293</a></p>
<p>We are studying how the airflow patterns work and are generated and that’s one of the reasons I’d like to compare the bronchi. I’ll try importing the segmentation as a Nifti - I think Avizo has that option.</p>

---

## Post #9 by @manjula (2020-01-11 15:24 UTC)

<p><a class="mention" href="/u/bobcieri">@bobcieri</a></p>
<p>This is not related to your problem but for a segmentation problem I wanted to look at Avizo but i don’t have access to it. It seems that you are familiar with Avizo.</p>
<p>Can I please know your experience with Avizo in segmentation?</p>
<p>Does it do a better job in segmenting complex structures than 3D Slicer and ITK-SNAP ?<br>
in terms of accuracy and ease of use ?</p>

---

## Post #10 by @muratmaga (2020-01-11 22:30 UTC)

<p><a class="mention" href="/u/bobcieri">@bobcieri</a> got it. If all your seven species have corresponding structures (i.e., the label structures exists in all your samples), you might be able to analyze shape of those secondary structures independently with geometric methods (probably with SlicerSALT), but I am not sure what that might tell you about the general variability of the whole airway across species.</p>
<p><a class="mention" href="/u/manjula">@manjula</a> most of the tools found in biomedical visualization software are general purpose image tools. I haven’t used Avizo for a while now, but I don’t recall seeing anything very different than the tools available in Slicer. If you need a very specific tool in Slicer that gives you exactly what you want, you may want to talk to some independent developers that might be following the forum. You might be surprised that a custom implementation of a tool (or a workflow) you miss in Slicer may only cost a license or two of Avizo (or other commercial tools), and if you choose to share it then everybody benefits from it. Just a thought.</p>

---

## Post #11 by @lassoan (2020-01-11 23:36 UTC)

<aside class="quote no-group quote-modified" data-username="manjula" data-post="9" data-topic="9762">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Can I please know your experience with Avizo in segmentation?<br>
Does it do a better job in segmenting complex structures than 3D Slicer and ITK-SNAP in terms of accuracy and ease of use ?</p>
</blockquote>
</aside>
<p>I had a chance to try Mimics InPrint, a commercial medical image segmentation software a month ago. It was quite shocking that it was at least as complicated as Slicer, yet it had so much less features and many limitations compared to Slicer.</p>
<p>I hear people have similar experience with Avizo (not much easier to use and very limited compared to Slicer) but it would be interesting to get more information. Also, if there is any segmentation feature in any other software that you miss in Slicer then let us know. It may be easy to add it (or it may already exist just not easy to find).</p>

---

## Post #12 by @manjula (2020-01-12 00:03 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you for sharing your experiences and   very much appreciate it.  The commercial software I have used for medical imaging are Geomagic and materialize. I think 3D slicer is much more versatile and powerful than the both.  However i have no experience with segmentation with commercial software.  i have used only 3DSlicer and ITK-SNAP.</p>
<p>If you did see the link i shared on the other post from the ITK-SNAP,  is there a way to interactively visualize the seeds growing and stop it when we want to in 3D Slicer like the one i have recorded ? because it would be very good to have that control when to stop the growth.</p>
<div class="lazyYT" data-youtube-id="IlFBkkJIIr0" data-youtube-title="dental" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #13 by @bobcieri (2020-01-12 00:13 UTC)

<p>Great ideas - I only used Avizo beacuse I had institutional access to the software and the folks that trained me in CFD used it to generate their surfaces. I am activly trying (and mostly succeeding!) in moving totally to open source tools. If I had the money to buy an Avizo license I would certainly rather push it towards developing open source tools.</p>
<p>As far as Avizo, I don’t think it does segmentation better than Slicer, but it may allow the user to handle larger datasets on smaller machines because it doesn’t require the entire dataset to be loaded into RAM. In addition, a few years ago I found its surface smoothing algorithms superior to Slicer but I doubt this is true any longer.</p>

---

## Post #14 by @bobcieri (2020-01-12 00:16 UTC)

<p>Also, thanks for your advice regarding the corresponding structures. All of the species will have a central intrapulmonary bronchus with secondary bronchi radiating off in similar directions but they will vary in terms of relative thickness/volume and branching angle. I was hoping to compare these shapes rigorously but it may be best to simply statistically compare traditional morphometric measurements in each species. I will give the SlicerSALT a try.</p>

---

## Post #15 by @muratmaga (2020-01-12 01:38 UTC)

<p>Yes, when you are in exploration and discovery phase starting basic morphometrics is probably the best way to go. Some of the automated shape analyses require massaging the data quite a bit (in terms of preprocessing), sometimes it doesn’t pay off (in terms of time investment) unless you have very large datasets…</p>
<p>Let us know if you cannot get your data into Slicer from Avizo. We distribute <a class="mention" href="/u/lassoan">@lassoan</a> tool RawImageGuess with SlicerMorph, which may help with some of the issues.</p>

---
