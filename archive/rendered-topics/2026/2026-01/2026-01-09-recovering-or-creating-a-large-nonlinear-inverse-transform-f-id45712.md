# Recovering or creating a large nonlinear inverse transform from an ANTs registration

**Topic ID**: 45712
**Date**: 2026-01-09
**URL**: https://discourse.slicer.org/t/recovering-or-creating-a-large-nonlinear-inverse-transform-from-an-ants-registration/45712

---

## Post #1 by @sulli419 (2026-01-09 00:50 UTC)

<p>I need to invert a nonlinear transform generated with the standard 3D Slicer ANTs extension, so it can be applied back to the fixed image to make it more like the moving, but it is becoming clear I do not understand how it behaves.</p>
<p>I am essentially running the default Quick SyN preset for registration in slicer (steps from Rigid, to Affine, to SyN).  This generates an impressively accurate forward .h5 transform file that is on the order 15 GB.  However, when I click “invert” on my large transform it seems to compute the inverse too fast and it doesn’t behave the way I expected when applied to the fixed image (looks nothing like the moving).  Also, I’m curious if the steps (rigid, affine, SyN) need to be unraveled and applied in the reverse order (SyN, affine, rigid) to achieve my goal, or if the this presumed “displacement field” can be inverted in one step and applied.  Can the linear transforms be extracted?</p>
<p>It’s my beginner understanding that the main version of ANTs (linux) under the hood is moving both images to a “middle” common point and, as part of this process, both the forward and inverse transforms are iteratively written in tandem and that either can be called up (from RAM, temp file?).  Is there a way to retrieve this “default” inverse transform in Slicer?  If not, is there a way to properly invert this transform within slicer (I assume it should take some time!).</p>
<p>Also, possibly related, I am not understanding how exactly the “output displacement field” tick box is behaving (see circled area in image).  It seems to store the transform more as an image, but then I can’t apply it to any of my volumes.  Which works better for inverting?  It looks like there are tools for applying displacement fields, but on a first pass they didn’t work with my transform.<br>
Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4d8f4aadc236cdcf326e5e30e87197374c9c17f.png" data-download-href="/uploads/short-url/wEtGHEiev3H9L4K8jA49V4nWyNV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4d8f4aadc236cdcf326e5e30e87197374c9c17f_2_414x500.png" alt="image" data-base62-sha1="wEtGHEiev3H9L4K8jA49V4nWyNV" width="414" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4d8f4aadc236cdcf326e5e30e87197374c9c17f_2_414x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4d8f4aadc236cdcf326e5e30e87197374c9c17f_2_621x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4d8f4aadc236cdcf326e5e30e87197374c9c17f.png 2x" data-dominant-color="3B3D3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">747×902 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-01-09 02:39 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="1" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>It’s my beginner understanding that the main version of ANTs (linux) under the hood is moving both images to a “middle” common point and, as part of this process, both the forward and inverse transforms are iteratively written in tandem and that either can be called up (from RAM, temp file?). Is there a way to retrieve this “default” inverse transform in Slicer? If not, is there a way to properly invert this transform within slicer (I assume it should take some time!).</p>
</blockquote>
</aside>
<p>They are not moved to a middle point. Please read this: <a href="https://github.com/ANTsX/ANTs/wiki/Forward-and-inverse-warps-for-warping-images,-pointsets-and-Jacobians" class="inline-onebox" rel="noopener nofollow ugc">Forward and inverse warps for warping images, pointsets and Jacobians · ANTsX/ANTs Wiki · GitHub</a></p>
<p>Our SlicerANTsPy extension expose both the forward and inverse warps, if you need that. However, the registration call itself is not as customizable as the SlicerANTs extension. You want to use the antsRegistrationQuickSyN[s] for the equivalent of QuickSyN in SlicerANTs extension you are currently using.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6e54578e5084ae29827dfcf7c944bf9fdc215c8.png" data-download-href="/uploads/short-url/q5Y6TKXSt4Wtzy5KCv0pdNXyH3y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6e54578e5084ae29827dfcf7c944bf9fdc215c8_2_690x406.png" alt="image" data-base62-sha1="q5Y6TKXSt4Wtzy5KCv0pdNXyH3y" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6e54578e5084ae29827dfcf7c944bf9fdc215c8_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6e54578e5084ae29827dfcf7c944bf9fdc215c8_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6e54578e5084ae29827dfcf7c944bf9fdc215c8_2_1380x812.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1526×900 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mikebind (2026-01-09 20:30 UTC)

<p>I was recently trying to understand what was happening under the hood in a similar situation, see this post for some potentially helpful information: <a href="https://discourse.slicer.org/t/interpreting-ants-registration-warp-field-directionality/45467/4" class="inline-onebox">Interpreting ANTs registration warp field directionality - #4 by mikebind</a></p>
<p>Note that I used the “General Registration (ANTs)” module rather than the “SlicerANTsPy” module (out of inertia rather than considered preference, and a namespace conflict has meant that it was not possible to have both extensions installed simultaneously).</p>
<p>In my experience, however, inverting a nonlinear transform calculated via ANTs has worked well for aligning a fixed volume to a moving volume, except sometimes near the edges of the image.  Transform inversion appears impossibly quick in Slicer because all that is done is change a flag on the component transforms which basically says “use the inverse of the stored transform”; the inverse is not actually calculated at that time.  Instead, when you want to look at a slice view transformed by this inverse transform, only the pixel points on that slice need to have their inverse transforms actually calculated, and this set of points is small enough that the inverse is quickly enough calculated that it appears instantaneous.  Slicer set up very cleverly in that way, so that the calculations are only actually performed when they are needed for display.</p>
<p>To answer a different question you asked, yes, Slicer automatically reverses the order of application of the inverses of the rigid, affine, and grid transforms when you invert a composite transform.</p>
<p>It is also possible that you are encountering a recently fixed bug where cloning of a composite transform did not preserve the order of application of component transforms, see here: <a href="https://discourse.slicer.org/t/cloning-a-composite-transform-yields-incorrect-result/44654" class="inline-onebox">Cloning a composite transform yields incorrect result</a></p>
<p>If that isn’t the problem, then I would suggest considering the domains over which your transforms are defined (see the pdf notes from the first link above).  If the moving image and fixed image have different spatial extents, then the grids over which the forward and reverse transforms make sense to be defined may differ.  Alternatively, if you just want a transform which works in each direction (and don’t need them to represent more or less exact inverses of each other), you can do the registration twice in General Registration (ANTs), or it looks like you could do it once in SlicerANTsPy but set it to generate both output directions.</p>

---

## Post #4 by @sulli419 (2026-01-12 22:50 UTC)

<p>Thanks for reminding me about SlicerANTsPy.  In the GUI you snapped, the inverse transform feature looks like exactly what I’m after, but unfortunately I will likely need more functionality.  Out of curiosity, can SlicerANTsPy: take fixed and moving masks, set a MeanSquares metric, add more convergence steps?  I need to keep the SlicerANTs extension but, to Mike’s later point, it sounds like they conflict with eachother.  I would hate to permanently lose the original extension’s function (sounds like maybe some users have run into this).  Maybe I can sandbox them within different slicer installs on different hard drives?</p>
<p>Another thing that has me curious, in the GUI it looks like there are some other useful tabs.  I’m most interested in the Template one.  Are there any good links that cover how to use these, and show what the menus look like?</p>
<p>Best,</p>
<p>Steve</p>

---

## Post #5 by @muratmaga (2026-01-12 23:25 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="4" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>but unfortunately I will likely need more functionality. Out of curiosity, can SlicerANTsPy:</p>
</blockquote>
</aside>
<p>These are not exposed at the GUI. ANTs have extreme number of parameters that can be tweaked and it is hard to do via GUI. When I need full control, I simply call it directly from python.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://antspy.readthedocs.io/en/latest/registration.html">
  <header class="source">

      <a href="https://antspy.readthedocs.io/en/latest/registration.html" target="_blank" rel="noopener nofollow ugc">antspy.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://antspy.readthedocs.io/en/latest/registration.html" target="_blank" rel="noopener nofollow ugc">Registration — ANTsPy dev (latest) documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The link I shared above is the best way to learn ANTsPy.</p>

---

## Post #6 by @sulli419 (2026-01-12 23:25 UTC)

<p>Not to get tangential, but understanding this might help me figure out how to best recover the inverse… Doesn’t this paper show that SyN works by warping to some middlespace?  See figure 2.  Hence why the inverse is computed by default.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/">
  <header class="source">
      <img src="https://pmc.ncbi.nlm.nih.gov/static/img/favicons/favicon-48x48.png" class="site-icon" alt="" width="48" height="48">

      <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/" target="_blank" rel="noopener nofollow ugc">PubMed Central (PMC)</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/360;"><img src="https://cdn.ncbi.nlm.nih.gov/pmc/cms/images/pmc-card-share.jpg?_=0" class="thumbnail" alt="" width="690" height="360"></div>

<h3><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2276735/" target="_blank" rel="noopener nofollow ugc">Symmetric Diffeomorphic Image Registration with Cross-Correlation: Evaluating...</a></h3>

  <p>One of the most challenging problems in modern neuroimaging is detailed characterization of neurodegeneration. Quantifying spatial and longitudinal atrophy patterns is an important component of this process. These spatiotemporal signals will aid in...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @sulli419 (2026-01-12 23:42 UTC)

<p>Really appreciate all this detail.  I printed your explanation and might have a few questions later.</p>
<p>It’s useful to know AntsPy Slicer and the Ants extension conflict.  Have you found any way to safely tinker with each?  Does this come with some risk of permanently rendering the extension unusable (I’ve seen a fairly related issue come up in forums)?</p>
<p>It looks like there are few methods for inverting transforms in slicer.  Can you point me to the best one (that you think would work for a large non-linear warp .h5 file?</p>
<p>For your inverse to work, is your initial transform created with the “output displacement field” option ticked?</p>
<p>Are you sure quick SyN is outputting a composite transform or are the rigid and affine steps cooked into the “displacement field”?  It looks like there are Slicer options for breaking a composite transform into its components but this wasn’t working for me.</p>
<p>Good point about the cloning. This could be a source of my problem (since the forward took so long to compute, I didn’t want to lose it).  Which version of Slicer was this bug fixed in?</p>
<p>As you suggested, my fallback plan is to compute the forward and inverse separately, but the registration for my files takes a non-trivial amount of time, so hope I can do it “the right way”.</p>
<p>You’ve inspired me to try a couple more things.  Will likely get back.</p>
<p>Cheers</p>

---

## Post #8 by @muratmaga (2026-01-13 00:48 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="6" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Doesn’t this paper show that SyN works by warping to some middlespace?</p>
</blockquote>
</aside>
<p>As it is written in the paper, the middle point is used to calculate the map from both sides (at least my reading of it). There is nothing in the paper that the calculated warps are to the middle point.</p>

---

## Post #9 by @muratmaga (2026-01-13 00:49 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="7" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Does this come with some risk of permanently rendering the extension unusable (I’ve seen a fairly related issue come up in forums)?</p>
</blockquote>
</aside>
<p>You can uninstall one or the other, and the remaining one works fine.</p>

---

## Post #10 by @muratmaga (2026-01-13 00:51 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="7" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>As you suggested, my fallback plan is to compute the forward and inverse separately, but the registration for my files takes a non-trivial amount of time, so hope I can do it “the right way”.</p>
</blockquote>
</aside>
<p>As you are learning, I would suggest using the ANTs (or any of its ecosystem components like ANTsPy) stand alone. That way you will remove the complexity of “am I doing this wrong, or loading it into Slicer incorrectly”.</p>

---

## Post #11 by @mikebind (2026-01-13 20:29 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="7" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Are you sure quick SyN is outputting a composite transform or are the rigid and affine steps cooked into the “displacement field”? It looks like there are Slicer options for breaking a composite transform into its components but this wasn’t working for me.</p>
</blockquote>
</aside>
<p>Yes, I’m sure the output is a composite transform. If you hover your mouse over the transform node entry in the Data module (or look in the Information section of the Transforms module), the components are listed separately in the hover text.   The linear steps (Rigid+Affine) are combined into one matrix, and the other component is a grid transform. I have found that splitting into components using the Transforms module works fine; if you clone before splitting, however, the cloning bug would mean that the clone was already wrong before splitting.</p>
<aside class="quote no-group" data-username="sulli419" data-post="7" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Good point about the cloning. This could be a source of my problem (since the forward took so long to compute, I didn’t want to lose it). Which version of Slicer was this bug fixed in?</p>
</blockquote>
</aside>
<p>The fix was incorporated into nightly builds as of Oct 6 2025, so anything older than that has the bug, and anything newer should have it fixed. It looks like 5.8.1 would have the bug, but 5.9, 5.10, or 5.11 should be fixed. If you want to continue to use an earlier version of Slicer, the code in <a href="https://gist.github.com/mikebind/d902b2410c339e9d9575eca77085b219" rel="noopener nofollow ugc">this gist</a> provides a workaround</p>
<aside class="quote no-group" data-username="sulli419" data-post="7" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>As you suggested, my fallback plan is to compute the forward and inverse separately, but the registration for my files takes a non-trivial amount of time, so hope I can do it “the right way”.</p>
</blockquote>
</aside>
<p>A demonstration of calculating the inverse of a displacement field is <a href="https://gist.github.com/mikebind/a6b5b4c9ba088615fdb5d896b32a7654" rel="noopener nofollow ugc">in this gist</a>.  Please note that this example constructs the inverse displacement field on the same grid points as the forward displacement field.  To modify this to allow sampling on an arbitrary grid, there would need to be more interpolation and index bookkeeping.</p>

---

## Post #12 by @sulli419 (2026-01-13 23:35 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="11" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>if you clone before splitting, however, the cloning bug would mean that the clone was already wrong before splitting.</p>
</blockquote>
</aside>
<p>Thanks for your replies.  I think maybe I will start here—<span class="bbcode-u">split first, then clone</span>—since I don’t want to risk losing functionality of many extensions with a Slicer update (even if it’s a very low risk).<br>
So say I have a Quick SyN .h5 transform, and I split before cloning.  Would I then invert both transforms (Affine and SyN) all within slicer?  Would inverting the isolated SyN field do as you said in an earlier message (i.e., ~call up the ANTs prestored inverse transform)?  And then in which steps/order would I apply these to the fixed image to make it “moving”?  Will the end volume effectively be resampled to the moving?</p>

---

## Post #13 by @mikebind (2026-01-15 18:12 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="12" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Would I then invert both transforms (Affine and SyN) all within slicer?</p>
</blockquote>
</aside>
<p>Yes, and reverse the order of application.</p>
<aside class="quote no-group" data-username="sulli419" data-post="12" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Would inverting the isolated SyN field do as you said in an earlier message (i.e., ~call up the ANTs prestored inverse transform)?</p>
</blockquote>
</aside>
<p>My understanding is that there is no stored inverse transform.  Instead, Slicer dynamically computes the inverse where it is requested for viewing. If you apply the chain of inverse transforms to the fixed volume, what you see should be registered to the moving volume.</p>
<aside class="quote no-group" data-username="sulli419" data-post="12" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Will the end volume effectively be resampled to the moving?</p>
</blockquote>
</aside>
<p>Effectively yes, but it is a dynamically applied soft transformation.  If you want to save the resampled image in the new geometry, you can harden the parent transform on the fixed image (note that this step is a resampling, so it is not lossless and cannot be perfectly inverted).  Also note that the grid it is resampled onto may not exactly match the geometry of the moving volume, I think the exact grid is constructed by Slicer such that it includes the bounding box of the transformed voxels and has the same voxel size as the fixed volume, but I’m not sure of the details of that.  If you want the fixed volume transformed to the moving volume and resampled onto the voxel grid of the moving volume, you can achieve that with the “Resample Image (BRAINS)” module by setting the fixed image as the “Image To Warp”, the moving image as the “Reference Image”, the composite transform from the registration as the “Transform file”, and checking the “Compute inverse transform of given transformation?” checkbox.</p>

---

## Post #14 by @sulli419 (2026-01-20 22:01 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="13" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>If you want the fixed volume transformed to the moving volume and resampled onto the voxel grid of the moving volume, you can achieve that with the “Resample Image (BRAINS)” module by setting the fixed image as the “Image To Warp”, the moving image as the “Reference Image”, the composite transform from the registration as the “Transform file”, and checking the “Compute inverse transform of given transformation?” checkbox.</p>
</blockquote>
</aside>
<p>Thanks.  I started with this approach you outlined above because it didn’t require cloning composite transforms which, as you said, has a bug in my version of Slicer (5.9.0).  It’s also a plus that this approach doesn’t require splitting.  However, when I run this as stated, the outputted resampled volume changes some, but it doesn’t not match the moving.  Also, the output will look the same irrespective of if I tick the “compute inverse transform of given transformation?” box.   Could it not be working because of the same bug?  Also the CPU usage is rather minimal (10% for ~10sec) considering that it is supposedly applying the non-linear transform to create the new output volume (contrast with below).</p>
<p>As an alternative, I spilt the composite transform.  I then cloned the displacement component, and inverted that (bottom most transform and image) and applied it to my fixed image, and hardened this transform; this hardening took a more expected CPU usage (100% for ~30 sec).  Next, to this hardened output, I then applied the inverted affine transform as highlighted in blue.  This fairly convincingly warped my fixed image to look more like the moving, but there are still a lot of things I don’t understand.  Why is that after I “split” the transforms, it seems like they are still tethered to eachother?  Notice how the blue highlighting toggles the yellow link.  Also, the little grid symbol on the right side seems to be the opposite of what I’d expect.  It shows a warped grid next to what I understand to be the affine component.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a534ea1d6dd9e8a5d552f874f0f40911b3dc89c.png" data-download-href="/uploads/short-url/hs8JDMs2FZPpO71kpyvkiuKavAo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a534ea1d6dd9e8a5d552f874f0f40911b3dc89c_2_690x93.png" alt="image" data-base62-sha1="hs8JDMs2FZPpO71kpyvkiuKavAo" width="690" height="93" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a534ea1d6dd9e8a5d552f874f0f40911b3dc89c_2_690x93.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a534ea1d6dd9e8a5d552f874f0f40911b3dc89c_2_1035x139.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a534ea1d6dd9e8a5d552f874f0f40911b3dc89c.png 2x" data-dominant-color="485D5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1124×152 40.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @mikebind (2026-01-26 23:34 UTC)

<p>The curved grid indicates that the item is currently being soft-transformed by a nonlinear transform, not that it is, itself, a nonlinear transform.  The highlighting also has to do with the transform hierarchy: different colors of highlighting show parent/child relationships, with fainter versions showing two-step removed relationships.</p>

---

## Post #16 by @sulli419 (2026-01-26 23:53 UTC)

<p>Thanks for clarifying.</p>
<p>How you ever come across the issue where ticking the “compute inverse transform of given transformation?” does not change the resampled volume in BRAINS?</p>

---

## Post #17 by @mikebind (2026-01-27 00:14 UTC)

<p>I haven’t ever tried using that checkbox, I just took it at face value that that it did what it said.  If you get the same result whether it is checked or not, that sounds like a bug!</p>

---

## Post #18 by @muratmaga (2026-01-27 03:38 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="14" data-topic="45712">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Thanks. I started with this approach you outlined above because it didn’t require cloning composite transforms which, as you said, has a bug in my version of Slicer (5.9.0).</p>
</blockquote>
</aside>
<p>That bug is fixed, you should really use something newer than 5.9. Also I think you will benefit directly interfacing with ANTs and loading data into Slicer. If you are using SlicerANTsPy, here is an example of registering volume B (moving) to A (fixed) and loading all the transforms along with the warped image into Slicer as appropriate data objects.</p>
<pre data-code-wrap="python"><code class="lang-python"># In Slicer Python console:
import ants
from ANTsRegistration import antsImageFromNode, nodeFromANTSImage, nodeFromANTSTransform

# Get your volumes
volumeA = slicer.util.getNode('A')
volumeB = slicer.util.getNode('B')

# Convert to ANTs
fixedImg = antsImageFromNode(volumeA)
movingImg = antsImageFromNode(volumeB)

# Run standard ANTsPy registration
result = ants.registration(
    fixed=fixedImg, 
    moving=movingImg, 
    type_of_transform='antsRegistrationSyNQuick[s]',
    write_composite_transform=False
)

# Check what transforms were created
print("Forward transforms:", result['fwdtransforms'])
print("Inverse transforms:", result['invtransforms'])

# Load transforms back to Slicer
# Forward transforms: [0] = warp field, [1] = affine
if len(result['fwdtransforms']) &gt; 0:
    forwardWarp = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
    forwardWarp.SetName('Forward_Warp')
    nodeFromANTSTransform(result['fwdtransforms'][0], forwardWarp)

if len(result['fwdtransforms']) &gt; 1:
    forwardAffine = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
    forwardAffine.SetName('Forward_Affine')
    nodeFromANTSTransform(result['fwdtransforms'][1], forwardAffine)

# Inverse transforms: [0] = affine, [1] = warp field
if len(result['invtransforms']) &gt; 0:
    inverseAffine = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
    inverseAffine.SetName('Inverse_Affine')
    nodeFromANTSTransform(result['invtransforms'][0], inverseAffine)

if len(result['invtransforms']) &gt; 1:
    inverseWarp = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
    inverseWarp.SetName('Inverse_Warp')
    nodeFromANTSTransform(result['invtransforms'][1], inverseWarp)

# Load warped image
warpedVolume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
warpedVolume.SetName('Warped_Moving_Volume')
nodeFromANTSImage(result['warpedmovout'], warpedVolume)
</code></pre>
<p>Note that forward and inverse affine matrices are actually the same (they also point out to the same file on disk). Because that’s the convention in ANTs if you pass the inverse transform, it will automatically calculate the inverse of the affine transform on the fly. You can use the invert option in Slicer, if you do need the invert it.</p>

---
