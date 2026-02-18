# 3D rendering bug for models imported to segment?

**Topic ID**: 44892
**Date**: 2025-10-27
**URL**: https://discourse.slicer.org/t/3d-rendering-bug-for-models-imported-to-segment/44892

---

## Post #1 by @muratmaga (2025-10-27 19:18 UTC)

<p>There is something confusing going on when I try to import a model to segment (either via right-click in SH and choose convert to segmentation, or use SlicerMorph’s ImportSurfaceToSegment module).</p>
<p>Here is a screenshot displaying the 3D visualization of original model (yellow), SH method and ImportSurfaceToSegment (cyan);</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6fb61ffec681dd1861c44f39d1e6787941281dc.jpeg" data-download-href="/uploads/short-url/soh7HXhXkRm9yYJvTB06Nt20sDW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6fb61ffec681dd1861c44f39d1e6787941281dc_2_690x362.jpeg" alt="image" data-base62-sha1="soh7HXhXkRm9yYJvTB06Nt20sDW" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6fb61ffec681dd1861c44f39d1e6787941281dc_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6fb61ffec681dd1861c44f39d1e6787941281dc_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6fb61ffec681dd1861c44f39d1e6787941281dc_2_1380x724.jpeg 2x" data-dominant-color="ACABBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1009 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is no difference in detail. Visibilities are set through SH (drag and drop).</p>
<p>If I switch to Segment Editor, Show 3D button is pressed (enabled). If toggle it off and back on that’s what I get, a smoothened model (cyan):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ae249e7774efe754c675af30bd26f7af29a556.jpeg" data-download-href="/uploads/short-url/w3C3iefACDZ5D3NJmiFB6b72Mvk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ae249e7774efe754c675af30bd26f7af29a556_2_690x315.jpeg" alt="image" data-base62-sha1="w3C3iefACDZ5D3NJmiFB6b72Mvk" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ae249e7774efe754c675af30bd26f7af29a556_2_690x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ae249e7774efe754c675af30bd26f7af29a556_2_1035x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ae249e7774efe754c675af30bd26f7af29a556_2_1380x630.jpeg 2x" data-dominant-color="A6A4B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×879 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That’s because smoothing is enabled. So I turned it off, then instead of the original image, I get this more noisy looking surface:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39c1723af1dd92c258608e5a32f0ec6079200f8f.jpeg" data-download-href="/uploads/short-url/8eVFGKThYHF6XUye7HQsm5AArxB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39c1723af1dd92c258608e5a32f0ec6079200f8f_2_690x303.jpeg" alt="image" data-base62-sha1="8eVFGKThYHF6XUye7HQsm5AArxB" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39c1723af1dd92c258608e5a32f0ec6079200f8f_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39c1723af1dd92c258608e5a32f0ec6079200f8f_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39c1723af1dd92c258608e5a32f0ec6079200f8f_2_1380x606.jpeg 2x" data-dominant-color="A7A4B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×844 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Whatever level of smoothing I chose, I can’t seem to reproduce the original cyan model created after the conversion. The details seems to have been lost (specifically I am interested in suture boundaries). This also happens on the segmentation I derive from right-clicking in subject hierarchy.</p>
<p>Where is the loss of information is coming (or is the initial rendering is incorrect)?</p>

---

## Post #2 by @pieper (2025-10-27 19:26 UTC)

<p>That is “normal” if the source model is a triangulated surface and the operation you perform requires conversion to a binary labelmap representation, which is an inherently lossy operation.  You can in theory reduce the loss to an arbitrarily small level by sampling at a higher resolution (changing the labelmap resolution) at the cost of using more memory (potentially a lot more memory).  This could be a motivation to use one of the super-high memory JS2 instances.</p>

---

## Post #3 by @muratmaga (2025-10-27 19:27 UTC)

<p>So the initial model displayed after the conversion is not the real model?</p>

---

## Post #4 by @pieper (2025-10-27 19:34 UTC)

<p>It is, but it’s the surface model representation of the segmentation.</p>
<p>There are <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">specific instructions here</a>.</p>

---

## Post #5 by @muratmaga (2025-10-27 19:35 UTC)

<p>That I understand, what is confusing is that I can’t seem to recover that representation when I toggle the Show 3D switch on and off.</p>

---

## Post #6 by @pieper (2025-10-27 20:14 UTC)

<p>My guess would be that the “show 3d” operation is really the “build s surface model from the binary labelmap representaton” under the hood.  I agree that maybe it should be have like the “eye” icons in the subject hierarchy and not convert if not needed.</p>

---

## Post #7 by @muratmaga (2025-10-27 21:25 UTC)

<p>I don’t really have a preference, but the current behavior is confusing to say the least. If the conversion is lossy, then the first rendering (without going into the segment editor) should reflect that. if it is not, then I should be to recover that detail through the Show 3D button of segment editor.</p>

---

## Post #8 by @pieper (2025-10-27 22:12 UTC)

<p>I agree, if my theory of the show 3d button is correct then it is a bit misleading in this case.  Maybe <a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/cpinter">@cpinter</a> can comment.  I do think that showing the surface model at first makes sense, since you can do operations on segmentations without creating binary labelmaps but having the show 3D button change representations behind the scenes seems wrong.</p>

---

## Post #9 by @lassoan (2025-10-28 04:38 UTC)

<p>“Show 3D” button creates/deletes closed surface representation. The current button text is chosen because showing a segmentation in 3D is the primary use of the closed surface representation.</p>
<p>When you create a segmentation then the source representation is always binary labelmap, even if you import a model into it. The closed surface representation is generated from the labelmap representation when needed; for example when closed surface representation is removed/creaated; or when saving the scene to file and then loading from it; or when editing the segment.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>the current behavior is confusing to say the least. If the conversion is lossy, then the first rendering (without going into the segment editor) should reflect that</p>
</blockquote>
</aside>
<p>We preserve all the available representations as much as possible, because that allows moving segments between segmentations without losing any information (e.g., temporarily move a segment into another segmentation and later move it back).</p>

---

## Post #10 by @muratmaga (2025-10-28 04:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The closed surface representation is generated from the labelmap representation when needed; for example when closed surface representation is removed/creaated; or when saving the scene to file and then loading from it; or when editing the segment.</p>
</blockquote>
</aside>
<p>But that’s not what I am observing, I think. Unless I am missing out something, when I import the model as a segmentation by right-clicking and choosing “convert segmentation”, the final 3D rendering show is identical to the model one I just used. Then I toggle 3D view off and on again, I do see the new closed surface representation generated off the labelmap (which is noisier and some details are lost). From the explanation you have given, the first rendering after the conversion is an incorrect representation of the segmentation (it should have rendered using the labelmap generated).</p>
<p>This behavior is misleading, and the difference is noticeable enough to make people think they are doing something wrong, as suddenly the 3D view is less detailed than what it was before. Yet all of that was already lost during the conversion closed surface to labelmap representation, just the view didn’t get updated (at least this is how I interpret it).</p>

---

## Post #11 by @lassoan (2025-10-28 05:39 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>From the explanation you have given, the first rendering after the conversion is an incorrect representation of the segmentation (it should have rendered using the labelmap generated).</p>
</blockquote>
</aside>
<p>As I wrote above, it is important that we only update a representation if needed. If we already have a representation then we use it. This allows many useful features, for example organizing segments by moving them between segments is a lossless operation.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This behavior is misleading, and the difference is noticeable enough to make people think they are doing something wrong, as suddenly the 3D view is less detailed than what it was before. Yet all of that was already lost during the conversion closed surface to labelmap representation, just the view didn’t get updated (at least this is how I interpret it).</p>
</blockquote>
</aside>
<p>If we can find a way how to make segmentations easier to understand then that’s great, but segmentation is inherently complex, so I think it is unavoidable that time to time people are surprised to discover some new details.</p>

---

## Post #12 by @cpinter (2025-10-28 09:29 UTC)

<p>When you import a model node to a segmentation, it will do three things:</p>
<ol>
<li>Create a new segmentation with the default binary labelmap segmentation</li>
<li>Set the imported model as closed surface representation</li>
<li>Convert it into binary labelmap so that we have a valid source representation (lossy)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e010abf163cb169dcdbb259f4424f647748ab73e.jpeg" data-download-href="/uploads/short-url/vYaFG3klURsKQDt85go1joJislU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e010abf163cb169dcdbb259f4424f647748ab73e_2_690x258.jpeg" alt="image" data-base62-sha1="vYaFG3klURsKQDt85go1joJislU" width="690" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e010abf163cb169dcdbb259f4424f647748ab73e_2_690x258.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e010abf163cb169dcdbb259f4424f647748ab73e_2_1035x387.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e010abf163cb169dcdbb259f4424f647748ab73e_2_1380x516.jpeg 2x" data-dominant-color="A4A691"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1790×671 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At this point, the shown closed surface is the original one you imported.</p>
<p>Then, when you turn off Show 3D, the closed surface gets removed. When you turn it on again, the closed surface is converted from the source representation (lossy).</p>
<p>As I remember we remove the closed surface instead of just hiding it, because if you edit the labelmap in Segment Editor, we don’t want to continually re-convert the surface if we don’t even see it (we always need to keep valid representations). As Andras says this infrastructure is inherently complex. <a class="mention" href="/u/muratmaga">@muratmaga</a> If you’re interested you can read about motivations, design, etc <a href="https://qspace.library.queensu.ca/handle/1974/26422">here</a> or <a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf">here</a>. Or feel free to keep asking of course <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @pieper (2025-10-28 13:06 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for the extra explanation and details.  To me the difference is that <a class="mention" href="/u/muratmaga">@muratmaga</a> expects the “show 3D” to operate just like the visibility eye icons in other parts of the application, while what it really does is to tell Slicer to update the surface representation to match the labelmap representation and keep it updated as long as that mode is active.  Although it’s an edge case, I could see this being a bit of a trap if instead of loading a file, the user created the surface representation in a way that’s hard to recreate leading to data loss.  Also once this happens you have no way to go back and adjust the resampling geometry.</p>
<p>It seems easy to detect this situation (existing surface representation but no labelmap) and ask the user if they really want to replace their current surface.  I think this case happens anytime you do a Segment Editor operation that requires a labelmap and people may not know that or have any other easy way to learn.</p>

---

## Post #14 by @cpinter (2025-10-28 15:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="13" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>if instead of loading a file, the user created the surface representation in a way that’s hard to recreate leading to data loss</p>
</blockquote>
</aside>
<p>I don’t really see this happening. The only way you can get to this point is to convert an existing model node to a segmentation node. You’ll still have the model node unless you explicitly delete it.</p>
<aside class="quote no-group" data-username="pieper" data-post="13" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>“show 3D” to operate just like the visibility eye icons</p>
</blockquote>
</aside>
<p>That button was called something else but users did not understand it so we had to simplify the message. I’m open to renaming it again…</p>
<aside class="quote no-group" data-username="pieper" data-post="13" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I think this case happens anytime you do a Segment Editor operation that requires a labelmap and people may not know that or have any other easy way to learn.</p>
</blockquote>
</aside>
<p>Yes any time the labelmap is modified, the closed surface is reconverted. I have to think a bit more, but I don’t see an elegant way for deciding if a surface is the “actual source”, unless with a new flag, which is an idea I don’t like.</p>
<p>As I remember there was also a discussion about the source representation when people import a model to an empty segmentation. To me the most reasonable solution would be to set the source representation as closed surface (because that is what is happening), and then when the user wants to edit, a warning already pops up about changing the source. But I also remember that the outcome of that discussion was the current way (not sure anymore why).</p>

---

## Post #15 by @pieper (2025-10-28 15:33 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="14" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The only way you can get to this point is to convert an existing model node to a segmentation node.</p>
</blockquote>
</aside>
<p>Okay, that’s fair.  I was thinking that you could load a surface model as a segmentation but I checked and I see that’s not possible.</p>

---

## Post #16 by @muratmaga (2025-10-28 20:15 UTC)

<aside class="quote no-group" data-username="pieper" data-post="15" data-topic="44892">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I was thinking that you could load a surface model as a segmentation but I checked and I see that’s not possible.</p>
</blockquote>
</aside>
<p>It is possible but I think it is restricted for OBJ format for some reason. Not sure why format matters?</p>

---

## Post #17 by @pieper (2025-10-28 20:25 UTC)

<p>Good question.  I used vtk and it was not an option.</p>

---

## Post #18 by @cpinter (2025-10-29 11:50 UTC)

<p>I just loaded an STL as segmentation, and the source representation is Closed surface. So the issue this topic is about (show-hide 3D and the model deteriorates) does not exist in this use case.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e0531ca894026fe5d4efd8874457d543dccd292.png" data-download-href="/uploads/short-url/b8cn3oXgZxuQoFpAvpUg26PFbrQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e0531ca894026fe5d4efd8874457d543dccd292.png" alt="image" data-base62-sha1="b8cn3oXgZxuQoFpAvpUg26PFbrQ" width="501" height="132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">501×132 2.88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @pieper (2025-10-29 12:47 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> can you replicate the issue without the SlicerMorph modules?  They might be side-stepping the Slicer native behavior.</p>
<p>I just tried loading and stl file as a segmentation.  It works fine and when I try to paint I need to select a source volume and then it warns that details may be lost due to the labelmap.  This seems quite reasonable to me, but something different must be going on in the ImportSurfaceToSegment process that bypasses the warning.</p>

---

## Post #20 by @cpinter (2025-10-29 14:49 UTC)

<p>The import feature is quite simple:</p>
<ol>
<li>The <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/SubjectHierarchyPlugins/qSlicerSubjectHierarchySegmentationsPlugin.cxx#L1215">SH plugin creates a new segmentation</a> with default options (binary labelmap source)</li>
<li>Calls the segmentations logic (<code>ImportModelToSegmentationNode</code>), which simply <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L1342">creates a segment</a> from the model’s polydata and adds it to the segmentation</li>
</ol>
<p>I found a thread that is about the same thing. It’s from five years ago and I said the same thing; it seems odd that the source representation is labelmap when we import a model to segmentation.</p>
<aside class="quote quote-modified" data-post="1" data-topic="8062">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/andrew_kanawati/48/3983_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/convert-stl-model-to-segmentation-node/8062">Convert STL model to segmentation node</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    I am having trouble creating a segmentation node from an STL of a 3d scan. The imported transform looks like this: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bed4a8ac13ee850a879e75c1d171942d17f6070.jpeg" data-download-href="/uploads/short-url/foLtXYRW6vqJCH7O5ArsTSLoH2o.jpeg?dl=1" title="04%20PM" rel="noopener nofollow ugc">[04%20PM]</a> 
The segmentation has characteristics that are not present on the STL: <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf25a42c883d23ac8828a7e0db2cbda788b259ca.jpeg" data-download-href="/uploads/short-url/rgXQgpr6dIN25X10FKREqj6iQVY.jpeg?dl=1" title="08%20PM" rel="noopener nofollow ugc">[08%20PM]</a> 
Help would be much appreciated.
  </blockquote>
</aside>

<p>I think it would be more correct adding a line in the SH plugin that sets closed surface as source representation. But again I’m not sure why this was kept like this. <a class="mention" href="/u/lassoan">@lassoan</a> if you remember please let us know. You see way more use cases than I and there must have been a good reason. Thanks!</p>

---
