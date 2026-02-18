# Making new sequence

**Topic ID**: 6262
**Date**: 2019-03-24
**URL**: https://discourse.slicer.org/t/making-new-sequence/6262

---

## Post #1 by @Jainey (2019-03-24 14:33 UTC)

<p>Hi, This is actually a continuation of a previous question. I was trying to build a new sequence using segmented .stl files. But when I load them onto slicer as separate STL files, they get overlapped on one another on 3 D view. As this segments show motion of the same structure ultimately after loading 10 STL models I get a hugely distorted view of the original structure- combining all the possible positions of that.</p>
<p>Could ypu kindly advise please. I am planning to register these segmented models using elastix as a sequence.</p>

---

## Post #2 by @lassoan (2019-03-24 18:56 UTC)

<p>Load the models as individual nodes and create a sequence from them as explained here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes</a></p>
<p>You can then delete the individual nodes and just keep the sequence node.</p>
<p>Elastix is for image registration, so you cannot directly use it to register surface meshes.</p>
<p>One possible approach is to convert surface meshes to distance map images and use image registration on them. This is implemented in Segment Registration extension, so you can use that or take some ideas from that to implement your own module.</p>
<p>Another approach is to remain in the surface mesh domain and use SlicerSALT shape analysis modules.</p>
<p>What is your goal? Would you like to compute a transform sequence? What do you plan to use that for?</p>

---

## Post #3 by @Jainey (2019-03-25 02:58 UTC)

<p>Thanks, Prof Lasso, <a class="mention" href="/u/lassoan">@lassoan</a>. Yes I am trying to compute a transform sequence. And then use markers to compute the displacement of the points on he surface mesh.</p>
<p>Thanks for your input.</p>
<p>Will try the segment registration module.</p>

---

## Post #4 by @lassoan (2019-03-25 03:09 UTC)

<p>If you can identify corresponding landmark points then you don’t need to use Elastix or surface registration but you can go with simple landmark registration. There are a couple of modules available for that in Slicer but I would recommend SlicerIGT’s “Fiducial registration wizard” module for this use case.</p>
<p>You can either register each pair of markup point lists manually or write a short Python script. Once you have computed all the transforms, you can put them in a sequence and apply it to your model sequence.</p>

---

## Post #5 by @Jainey (2019-03-25 10:58 UTC)

<p>Thanks a lot Prof. Lasso <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Unfortunately there are no clearly identifiable landmarks. And the number of models is in the range of 10-20 that I want to register, each depict motion within a fraction of a second.</p>
<p>So I think the first solution will probably be the answer</p>
<p>Thanks</p>
<p>Jan</p>

---

## Post #6 by @Jainey (2019-03-25 17:57 UTC)

<p>I am afraid I cannot add more than one node as the proxy node. Prof lasso <a class="mention" href="/u/lassoan">@lassoan</a> could you kindly let me know whether I am doing something wrong. I ve attached a screenshot</p>

---

## Post #7 by @Jainey (2019-03-25 17:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f0d1d22842f7ca36ca6d9633cbc79f600f5b7f2.png" data-download-href="/uploads/short-url/8ZMaXMrIRDEbhGrnbv0iboVLCDg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0d1d22842f7ca36ca6d9633cbc79f600f5b7f2_2_690x388.png" alt="image" data-base62-sha1="8ZMaXMrIRDEbhGrnbv0iboVLCDg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0d1d22842f7ca36ca6d9633cbc79f600f5b7f2_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0d1d22842f7ca36ca6d9633cbc79f600f5b7f2_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0d1d22842f7ca36ca6d9633cbc79f600f5b7f2_2_1380x776.png 2x" data-dominant-color="AEACAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2019-03-26 03:35 UTC)

<p>You can ignore the warnings, a spacing difference of about 0.001mm should be negligible.</p>
<p>I would recommend to first just try the registration method between two timepoints, without involving sequences. Once you confirmed what processing steps are needed and everything works well, we can find the best way to automate it.</p>

---
