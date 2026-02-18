# Volume rendering appearance changes if ROI box is shown

**Topic ID**: 20575
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/volume-rendering-appearance-changes-if-roi-box-is-shown/20575

---

## Post #1 by @DIV (2021-11-09 12:34 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="17685">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"><a href="https://discourse.slicer.org/t/trying-to-diagnose-an-issue-with-virtualgl-and-slicer/17685/6">Trying to diagnose an issue with VirtualGL and Slicer</a></div>
<blockquote>
<p>When I hide the ROI, artifact disappears. Showing it brings it back.</p>
</blockquote>
</aside>
<p>Hello, all.<br>
I’m not sure whether this is related, but I am seeing an odd dependence of the 3D rendering when toggling the ROI visibility (specifically the ROI that is <em>always</em> enabled to crop the displayed 3D rendering).<br>
I realise that this issue is marked solved, but it may still be evident in the version of Slicer I’m using.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f38d64e038c47162370759f698454b07b2dcf8b.jpeg" data-download-href="/uploads/short-url/i9spwHfstHURkUcH3QwscV8Lzxp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f38d64e038c47162370759f698454b07b2dcf8b_2_690x367.jpeg" alt="image" data-base62-sha1="i9spwHfstHURkUcH3QwscV8Lzxp" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f38d64e038c47162370759f698454b07b2dcf8b_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f38d64e038c47162370759f698454b07b2dcf8b_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f38d64e038c47162370759f698454b07b2dcf8b.jpeg 2x" data-dominant-color="BEBDCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 74.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e59eacfb5af697cf513d9abc43b92f070a6efcd3.jpeg" data-download-href="/uploads/short-url/wLjiIp83USwhqQTcJ8IIdEjNsmD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e59eacfb5af697cf513d9abc43b92f070a6efcd3_2_690x367.jpeg" alt="image" data-base62-sha1="wLjiIp83USwhqQTcJ8IIdEjNsmD" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e59eacfb5af697cf513d9abc43b92f070a6efcd3_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e59eacfb5af697cf513d9abc43b92f070a6efcd3_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e59eacfb5af697cf513d9abc43b92f070a6efcd3.jpeg 2x" data-dominant-color="BEBECD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>FWIW, the green object was imported from an STL file.</p>
<p>Sorry if it’s duplication or redundant.  I wasn’t sure whether it’s quite the same issue or not.</p>
<p>—DIV</p>

---

## Post #2 by @lassoan (2021-11-09 13:00 UTC)

<p>The images above look correct to me. Enable cropping and displaying the ROI are controlled by two different checkboxes. Enabling cropping when you display the ROI <em>in the Volume rendering module</em> is a convenience feature, because this is what users expect most of the time. If you can show/hide the ROI elsewhere (such as in Data module) without re-enabling cropping.</p>

---

## Post #3 by @DIV (2021-11-09 13:35 UTC)

<p>I didn’t understand your point(s).</p>
<p>Are you saying that when I untick “Display ROI” in the <strong>Volume Rendering</strong> module that it <em>automatically</em> disables the cropping?  That is not my experience, and it’s not what I’m reporting above.  On top of that, I would not expect that hiding the ROI would disable the associated cropping unless the “Enable” tick-box became disabled (greyed out) whenever the ROI is hidden.  And finally, I don’t think I would want them to be linked like that:  it’s good to have two separate controls, so that I can view the cropped volume without being distracted by the white outlines (and coloured handles) of the ROI box.</p>
<p>In the case I presented, the cropping is (seemingly) unchanged, but the appearance of what’s within the ROI has changed.  Are you saying that that is expected/intended behaviour?  If so, could you clarify what the benefit of it would be?</p>
<p>—DIV</p>

---

## Post #4 by @lassoan (2021-11-09 14:09 UTC)

<p>ROI visibility and enabling a ROI to crop a volume are two independent properties. The only connection between them is a convenience feature in Volume Rendering module (enabling display will enable cropping).</p>

---

## Post #5 by @muratmaga (2021-11-10 06:16 UTC)

<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="20575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>In the case I presented, the cropping is (seemingly) unchanged, but the appearance of what’s within the ROI has changed. Are you saying that that is expected/intended behaviour? If so, could you clarify what the benefit of it would be?</p>
</blockquote>
</aside>
<p>Primary benefit of hiding the ROI (once you setup your cropping) is that it doesn’t clutter your screenshot and distract from the features you are trying to visualize. Making the ROI visible/hidden will not impact the cropping extend, if you enabled the cropping (see <a class="mention" href="/u/lassoan">@lassoan</a>’s answer above).</p>

---

## Post #6 by @DIV (2021-11-10 23:34 UTC)

<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="20575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>the appearance of what’s within the ROI has changed</p>
</blockquote>
</aside>
<p>This discussion seems to be going around and around in circles.</p>
<p>The replies seem to be explaining the fact that hiding a ROI and enabling a ROI are two different things, and that it’s helpful that these two functions are separate.  Thank-you for confirming that.  I don’t dispute it;  I agree with it.  Unfortunately it doesn’t seem to have much to do with the issue I described above.</p>
<p>The issue I described is that hiding the ROI (while it is still enabled) caused a change in the appearance of the 3D rendering.  Please inspect the screenshots carefully, especially in the lower half of the reconstruction.  When the ROI is <em>hidden</em> the 3D rendering is <em><strong>less</strong></em> distinct.  Nothing so far explains that.  Hiding the ROI should either not affect the cropping (reconstruction should look identical) or else should potentially enlarge the reconstructed volume (reconstruction could look <em>darker</em> because of newly included voxels in the background or the foreground and/or could have larger extents);  there is no reason I can see for the observed behaviour in which the extents look essentially the same but the reconstruction is <em>lighter</em> when the ROI is <em>hidden</em>.</p>
<p>—DIV</p>

---

## Post #7 by @pieper (2021-11-10 23:41 UTC)

<p>Thanks for clarifying <a class="mention" href="/u/div">@DIV</a>.  I admit I looked at your images in your first post for a while and didn’t see obvious differences.  Now that you say it’s darker in the lower half your question makes sense.  Probably this is a difference with the zbuffer range or similar low level rendering issue.  We may or may not be able to resolve this in Slicer if it’s a VTK issue.  Best thing would be to make a reproducible example using public data.  Even then if it’s only a small difference in a rare case it may be hard to prioritize, but of course we want the program to provide consistent results if possible.</p>

---

## Post #8 by @DIV (2021-11-10 23:55 UTC)

<p>Thanks, Steve.<br>
This is the first time I noticed such a thing.  It was ‘obvious’ to me (because of where my attention was directed), but I realise it may not have been obvious to others.<br>
However, now that I have seen it this time I can look out for similar occurrences in future.</p>
<p>Going back to my original report (above), do you think this would be caused by the issue described by DRC at the start of this post, or does it seem like a separate thing?</p>
<p>—DIV</p>

---

## Post #9 by @pieper (2021-11-11 00:20 UTC)

<p>It might be related, since both seem to come from ROIs but it’s hard to say.  If you aren’t using VirtualGL it’s unlikely to be the exact same issue, but both may expose differences in the order of graphics commands leading to the driver being in slightly different states with or without the ROI visible.</p>

---

## Post #10 by @muratmaga (2021-11-11 00:23 UTC)

<aside class="quote no-group" data-username="DIV" data-post="8" data-topic="20575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Going back to my original report (above), do you think this would be caused by the issue described by DRC at the start of this post, or does it seem like a separate thing?</p>
</blockquote>
</aside>
<p>That was a specific bug in VirtualGL, not in Slicer. Unless you are using VGL to render these images (on a remote server) than this thread is relevant. And looks like you are not even using GPU rendering.</p>

---

## Post #11 by @DIV (2021-11-11 01:04 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="20575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It might be related, since both seem to come from ROIs but it’s hard to say.</p>
</blockquote>
</aside>
<p>That’s more-or-less why I posted here, instead of opening up a new thread.</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="9" data-topic="20575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If you aren’t using VirtualGL […].</p>
</blockquote>
</aside>
<aside class="quote no-group quote-post-not-found" data-username="muratmaga" data-post="40" data-topic="17685">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"><a href="https://discourse.slicer.org/t/trying-to-diagnose-an-issue-with-virtualgl-and-slicer/17685/40">Trying to diagnose an issue with VirtualGL and Slicer</a></div>
<blockquote>
<p>Unless you are using VGL to render these images (on a remote server) […]. And looks like you are not even using GPU rendering.</p>
</blockquote>
</aside>
<p>Thanks for the explanations.  I wasn’t sure what VirtualGL was, and when it would be used (<em>e.g.</em> by default, or only in special circumstances) but you’re right:  I was doing everything on a local computer, and the setting shown in the <em>Display</em> panel of the <strong>Volume Rendering</strong> module  in the screenshots is <em>Rendering</em> = “VTK CPU Ray Casting”.<br>
In other instances I have also run with <em>Rendering</em> = “VTK GPU Ray Casting”, although I cannot comment on whether it makes any difference to the presently discussed issue.  (I can keep this distinction in mind for future.)</p>
<p>—DIV</p>

---

## Post #12 by @lassoan (2021-11-11 05:30 UTC)

<p>There are many small differences in features and limitations of VTK’s internal volume rendering pipelines. When you change a rendering option, such as enable/disable depth peeling, then internally VTK switches to a different pipeline, which produces slightly different rendering results.</p>
<p>Reason for the slight change in your use case: Depth peeling is enabled by default in recent Slicer versions, but depth peeling is not activated until a semi-transparent actor appears in the field of view. This is why showing the semi-transparent ROI changes the volume rendering appearance in the screenshots above.</p>
<p>The differences between the pipelines will not go away completely, because maintaining full consistency between all rendering pipelines would be expensive (would take lots of developer time to implement all features for all pipelines) and often also technically impossible (e.g., GPU volume rendering is much faster but you may have more restrictions in how you implement the compositing function). I would recommend you to experiment with different volume rendering options and for each application choose the one that is the most suitable. If any specific limitation causes a problem for a use case then you can hire a developer or set up a software development contract with Kitware to get the missing feature implemented or problem/limitation fixed in VTK.</p>

---

## Post #13 by @DIV (2021-11-16 05:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="20575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Depth peeling is enabled by default in recent Slicer versions, but depth peeling is not activated until a semi-transparent actor appears in the field of view.</p>
</blockquote>
</aside>
<p>I am curious as to why the depth peeling is not configured to be ‘active’ all of the time, for (more) consistent rendering.  Is it too computationally expensive (and/or disruptive to the user experience due to lags in video updating)?</p>
<p>As the previous screenshots didn’t seem to illustrate the effect so clearly, here are another pair.  (Which also demonstrates that it’s not a one-off quirk of one particular CT scan.)</p>
<p><strong>VTK <em>CPU</em> Ray Casting (cropping enabled; with and without displayed ROI)</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f9d32731452e3c384fa026faa5401095200f6b6.jpeg" data-download-href="/uploads/short-url/94KSaU0Jhawy8QD6lST2kZY25aC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9d32731452e3c384fa026faa5401095200f6b6_2_690x367.jpeg" alt="image" data-base62-sha1="94KSaU0Jhawy8QD6lST2kZY25aC" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9d32731452e3c384fa026faa5401095200f6b6_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f9d32731452e3c384fa026faa5401095200f6b6_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f9d32731452e3c384fa026faa5401095200f6b6.jpeg 2x" data-dominant-color="B4ABB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c64d334fca3f35b9a6e5279bb126cdb4316e529.jpeg" data-download-href="/uploads/short-url/k1YRtoVtG5fBEjAqlVhb2P8WQxb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c64d334fca3f35b9a6e5279bb126cdb4316e529_2_690x367.jpeg" alt="image" data-base62-sha1="k1YRtoVtG5fBEjAqlVhb2P8WQxb" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c64d334fca3f35b9a6e5279bb126cdb4316e529_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c64d334fca3f35b9a6e5279bb126cdb4316e529_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c64d334fca3f35b9a6e5279bb126cdb4316e529.jpeg 2x" data-dominant-color="B5AEBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 90.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I got curious about what happens with GPU selected…<br>
<strong>VTK <em>GPU</em> Ray Casting (cropping enabled; with and without displayed ROI)</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123a829c169a34becd94b20b89ca220188eeeca7.jpeg" data-download-href="/uploads/short-url/2BfX1pJU6FK5y5rPve4HtFldfZt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123a829c169a34becd94b20b89ca220188eeeca7_2_690x367.jpeg" alt="image" data-base62-sha1="2BfX1pJU6FK5y5rPve4HtFldfZt" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123a829c169a34becd94b20b89ca220188eeeca7_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/123a829c169a34becd94b20b89ca220188eeeca7_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123a829c169a34becd94b20b89ca220188eeeca7.jpeg 2x" data-dominant-color="BDAFB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c5e7855e2dfaaac18a38585bddff7b682cc304f.jpeg" data-download-href="/uploads/short-url/k1LfjB8ni5uRlQuPRPsqMACz1Hp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c5e7855e2dfaaac18a38585bddff7b682cc304f_2_690x367.jpeg" alt="image" data-base62-sha1="k1LfjB8ni5uRlQuPRPsqMACz1Hp" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c5e7855e2dfaaac18a38585bddff7b682cc304f_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c5e7855e2dfaaac18a38585bddff7b682cc304f_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c5e7855e2dfaaac18a38585bddff7b682cc304f.jpeg 2x" data-dominant-color="BDAFB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When rendering with the GPU the display of the ROI does not seem to have any effect at all on the 3D appearance.<br>
Maybe depth peeling is always active (or always inactive) for the GPU pipelines?</p>
<p>In summary, the rendering in the two GPU screenshots is identical, albeit different to the two rendering results seen in the two CPU screenshots.</p>
<p>—DIV</p>

---

## Post #14 by @DIV (2021-11-16 05:39 UTC)

<p>Correction:   there are some minor differences when <code>VTK GPU Ray Casting</code> is selected too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9d4544bc558e5a40265de83f4d496675c4475ba.jpeg" data-download-href="/uploads/short-url/xmyaaq9iJYK1TeZVxsRUGdqwU9I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9d4544bc558e5a40265de83f4d496675c4475ba_2_690x367.jpeg" alt="image" data-base62-sha1="xmyaaq9iJYK1TeZVxsRUGdqwU9I" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9d4544bc558e5a40265de83f4d496675c4475ba_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9d4544bc558e5a40265de83f4d496675c4475ba_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9d4544bc558e5a40265de83f4d496675c4475ba.jpeg 2x" data-dominant-color="CEC1B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 83.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b48da4c46b07af6138a6b5b9c14881cdc56cb2bb.jpeg" data-download-href="/uploads/short-url/pLfpIgx9twZO92qCHAWLXEUoH8v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b48da4c46b07af6138a6b5b9c14881cdc56cb2bb_2_690x367.jpeg" alt="image" data-base62-sha1="pLfpIgx9twZO92qCHAWLXEUoH8v" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b48da4c46b07af6138a6b5b9c14881cdc56cb2bb_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b48da4c46b07af6138a6b5b9c14881cdc56cb2bb_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b48da4c46b07af6138a6b5b9c14881cdc56cb2bb.jpeg 2x" data-dominant-color="CDC1BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>—DIV</p>

---
