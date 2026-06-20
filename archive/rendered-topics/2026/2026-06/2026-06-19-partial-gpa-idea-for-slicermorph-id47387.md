---
topic_id: 47387
title: "Partial GPA idea for slicermorph"
date: 2026-06-19
url: https://discourse.slicer.org/t/47387
last_bumped: 2026-06-19T17:24:27.266Z
---

# Partial GPA idea for slicermorph

**Topic ID**: 47387
**Date**: 2026-06-19
**URL**: https://discourse.slicer.org/t/partial-gpa-idea-for-slicermorph/47387

---

## Post #1 by @Stephan_Collins (2026-06-19 09:01 UTC)

<p>Dear all,</p>
<p>Dear all,</p>
<p>I am writing from a conference where I am learning a great deal about morphogeometry, which is quite far from my original background.</p>
<p>One issue that has come up, and that I have also encountered when using the SlicerMorph GPA module on my own data, concerns shape deformation when some landmarks remain relatively fixed while others move more substantially. One very celar example given at the conference is the case of an inner ear and the shape of the cochlea.</p>
<p>For example, if we assume that the cochlea grows, GPA will enforce alignment based on all landmarks. As a result, the base of the cochlea may be shifted inwards, even if it has not actually moved, while the tip of the cochlea shifts outwards. Consequently, the resulting model-to-model distance may highlight apparent changes at both extremities, even though the biological change may be concentrated mainly in one region.</p>
<p>I am still processing this, but I was wondering whether one possible way to address this would be to allow partial GPA, or to introduce a way to constrain or weight specific landmarks in the original space. This could perhaps help preserve relatively stable anatomical regions while still capturing true shape changes elsewhere.</p>
<p>I would be very interested to hear your thoughts on whether this makes sense, and whether such an approach would be feasible or already exists in some form..</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/455801ee5ccf0a84ed5f200057fec99aeb827e2d.png" data-download-href="/uploads/short-url/9Trv2TtonX693e09224F0dMYAYl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/455801ee5ccf0a84ed5f200057fec99aeb827e2d.png" alt="image" data-base62-sha1="9Trv2TtonX693e09224F0dMYAYl" width="204" height="192"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">204×192 52.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Stephan_Collins (2026-06-19 10:15 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="1" data-topic="47387">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>One issue that has come up, and that I have also encountered when using the SlicerMorph GPA module on my own data, concerns shape deformation when some landmarks remain relatively fixed while others move more substantially. One very celar example given at the conference is the case of an inner ear and the shape of the cochlea.</p>
<p>For example, if we assume that the cochlea grows, GPA will enforce alignment based on all landmarks. As a result, the base of the cochlea may be shifted inwards, even if it has not actually moved, while the tip of the cochlea shifts outwards. Consequently, the resulting model-to-model distance may highlight apparent changes at both extremities, even though the biological change may be concentrated mainly in one region.</p>
<p>I am still processing this, but I was wondering whether one possible way to address this would be to allow partial GPA, or to introduce a way to constrain or weight specific landmarks in the original space. This could perhaps help preserve relatively stable anatomical regions while still capturing true shape changes elsewhere.</p>
<p>I would be very interested to hear your thoughts on whether this makes sense, and whether such an approach would be feasible or already exists in some form..</p>
</blockquote>
</aside>
<p>Just to add to this after thinking about it a bit more: perhaps another way to frame the issue is that, in some cases, the models may already be aligned in a biologically meaningful coordinate system before entering the GPA workflow.</p>
<p>SlicerMorph already allows scaling to be skipped, which is very useful when absolute growth or size differences are biologically relevant. But in the example I am thinking about, the issue may also concern the registration/alignment step itself. If rotation and translation are still estimated from all landmarks, then regions that actually deform or grow will still influence the alignment.</p>
<p>So perhaps what would be useful is an option to bypass the GPA alignment step entirely when models have been pre-aligned, or alternatively to estimate the alignment only from a selected subset of stable landmarks and then apply that transformation to the full landmark set/model. This would allow distances or residual shape differences to be computed in a reference frame that has been defined anatomically beforehand, rather than one defined by all landmarks equally.</p>
<p>I am not sure whether this is already possible in the current workflow, but this may be closer to what I had in mind than “partial GPA” in the strict sense.</p>

---

## Post #3 by @ThomasVanParys (2026-06-19 10:52 UTC)

<p>You have the option to “subset” desired landmarks for GPA if you are interested in a particular biological region.. this can de done using the recently developed <a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis" rel="noopener nofollow ugc">DeCA</a> module in SlicerMorph or you can import landmark files into R Studio and code which landmarks are being subsetted, as long as all landmark files follow the same sequential pattern.</p>

---

## Post #4 by @muratmaga (2026-06-19 17:24 UTC)

<p>All registration methods, including GPA, that minimizes overall error will suffer if the difference between two shapes are heavily concentrated in one specific area.</p>
<aside class="quote no-group" data-username="Stephan_Collins" data-post="1" data-topic="47387">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>I am still processing this, but I was wondering whether one possible way to address this would be to allow partial GPA, or to introduce a way to constrain or weight specific landmarks in the original space. This could perhaps help preserve relatively stable anatomical regions while still capturing true shape changes elsewhere.</p>
</blockquote>
</aside>
<p>That is in theory possible and some people used it. In practice coming up these weights, particularly if the landmarks are more than a handful is challenging. You are sort of post-hoc trying to derive the alignment to give you what you think is the right alignment.</p>
<p>You may want to explore geomorph or shapes packages in R, which might be easier to do this kind of experimentation and post-hoc reprocessing. I just don’t recall which one supported the weights.  As <a class="mention" href="/u/thomasvanparys">@ThomasVanParys</a> eluded you can extract the indexes of landmarks using the <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor" rel="noopener nofollow ugc">MarkupEditor</a> then assign random weights to it, and see how it changes the alignment. As generic, UI driven tool it would be harder to do that in GPA.</p>

---
