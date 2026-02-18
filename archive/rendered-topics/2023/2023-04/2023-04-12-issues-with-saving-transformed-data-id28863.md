# Issues with saving transformed data

**Topic ID**: 28863
**Date**: 2023-04-12
**URL**: https://discourse.slicer.org/t/issues-with-saving-transformed-data/28863

---

## Post #1 by @jgrime (2023-04-12 11:34 UTC)

<p>Hi!</p>
<p>I’m trying to use Slicer 5.2.2 to align two 3D data sets, both of which feature data arranged on regular axis-aligned grid.</p>
<p>I first recentre the target data set volume on the world origin, and then tweak the orientation of that data to better align along the world axes. I then superpose the second data set onto the first (oriented) data set via the registration tools (Registration → Specialized → Fiducial Registration menu item).</p>
<p>I’ve got the alignment working via manual placement of three reference points on corresponding parts of the two data sets, and the alignment seems to work well. After hardening the transforms, the two (aligned) data sets look pretty good!</p>
<p>However, when trying to save the data I’m running into some problems.</p>
<p>I understand that slicer does not resample the data by default, and so after applying the appropriate transform(s) if I simply save the data I won’t necessarily get the output that I expect. I therefore tried to use the Legacy → Filtering → Resample Scalar Volume menu option to generate a new (resampled) data set from each of my two aligned data sets. Weirdly, this did actually seem to generate a resampled data set for the “fixed” target data (i.e., when I visualize the “old” and “new” versions of that data set in ParaView they are different), but the “moving” data set output is apparently identical to the input data set - just as if no transform(s) had been applied, or the data was not resampled.</p>
<p>I then tried the “Registration → Resample Image (BRAINS)” approach with “Image to Warp” as the second (i.e., moving) data set and “Reference Image” as the first (i.e., fixed) data set. This actually seems to work, as the resampled output file is properly aligned with the target/fixed data as per the visual display in Slicer. However: the very top of the resampled output file is chopped off!</p>
<p>I’m guessing this is because the image resampling crops the output to the bounding box of the “reference image” data, but I’m not sure about that. In any case, it’s really strange; I’m not sure why people would want the output data to be cropped in this manner by default. As an option, sure -but as the default behaviour? I don’t see how it’s at all helpful!</p>
<p>Can I turn off that cropping, or do something to adjust the output from the “Resample Image (BRAINS)” functionality so this cropping does not happen?</p>
<p>I’m frustratingly close to having what I want here!</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-04-12 12:12 UTC)

<p>What is your overall goal? Do you want the fixed image to have the same geometry as the fixed image? Then the resampled image may be clipped and some regions in the image may be blank.</p>
<p>ParaView is great software but not well suited for medical image computing. The most severe limitation is that ignores image orientation, so you cannot use it to verify alignment of images in physical space.</p>

---

## Post #3 by @jgrime (2023-04-12 12:21 UTC)

<p>Hi Andras,</p>
<p>I simply want to align the two data sets on top of one another in a common location/orientation, and then save the data sets such that I can load them into basically <em>anything</em>.</p>
<p>As such, it’s best if I can save resampled data - then I don’t need to worry about whether whatever transforms stored in file headers etc are compatible with $RANDOM_SOFTWARE_PACKAGE.</p>
<p>In this case I want to load them into is ParaView, as I wish to make use of the various movie making / user-defined rendering capabilities that ParaView has</p>
<p>My question regards the “clipping” issue in Slicer, not whether ParaView is suited to medical imaging.</p>
<p>Thanks for the help, Andras!</p>

---

## Post #4 by @jgrime (2023-04-12 17:39 UTC)

<p>If I use the scalar resampling function on an input .nrrd data set to create a new data set (having suitably translated/rotated the original data set and hardened the transform), the IJK to RAS direction matrix of the resampled data set appears to contain identical values to the original data set.</p>
<p>I am missing something important in my understanding of what resampling does? The Slicer documentation seems to indicate that resampling <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Resampling#What_we_mean_by_Resampling" rel="noopener nofollow ugc">will indeed modify the orientation</a> etc.</p>
<p>Guidance welcome!</p>

---

## Post #5 by @lassoan (2023-04-16 19:03 UTC)

<aside class="quote no-group" data-username="jgrime" data-post="3" data-topic="28863">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/47e85d/48.png" class="avatar"> jgrime:</div>
<blockquote>
<p>such that I can load them into basically <em>anything</em></p>
</blockquote>
</aside>
<p>If you want to use software that ignores all image geometry information (origin, spacing, axis directions) then the only option is to resample one image to the other image’s geometry. In Slicer you can do that with most of the resampling modules. The resampled image may be clipped and/or contain blank voxels.</p>
<p>You can expand the extent of the reference image to prevent clippin. In Slicer you can do that using <code>Crop Volume</code> module.</p>
<aside class="quote no-group" data-username="jgrime" data-post="3" data-topic="28863">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/47e85d/48.png" class="avatar"> jgrime:</div>
<blockquote>
<p>I don’t need to worry about whether whatever transforms stored in file headers etc</p>
</blockquote>
</aside>
<p>You need to pay attention to preserve correct image geometry for many reasons. Most processing algorithms work incorrectly inconsistently if you ignore the image geometry. Also, if you discard or change some components of the image geometry (e.g., you ignore axis directions) then you lose the ability to cross-reference positions between the original image and your modified images.</p>
<aside class="quote no-group" data-username="jgrime" data-post="3" data-topic="28863">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/47e85d/48.png" class="avatar"> jgrime:</div>
<blockquote>
<p>I want to load them into is ParaView, as I wish to make use of the various movie making / user-defined rendering capabilities that ParaView has</p>
</blockquote>
</aside>
<p>Both Slicer and ParaView use VTK toolkit for visualization, so the same rendering capabilities are available in both software. ParaView is tuned for general-purpose engineering visualization, while Slicer is specifically targets medical imaging, therefore some rendering options may not be exposed in one software or the other. Slicer and ParaView uses different animation tools. As a result, it may not be always trivial to find how to do the same thing in these two applications. If you let us know what kind of vísualization you want then we can give advice about how to achieve it in Slicer.</p>

---

## Post #6 by @jgrime (2023-04-16 19:36 UTC)

<p>Thanks, Andras!</p>
<p>The output data is purely for visualization purposes, and so provided everything is consistent in the output files I can easily tweak the spacing etc in something like ParaView. Cross-referencing with the original data is not required at that stage, fortunately!</p>
<p>The animations are fairly simply, and essentially involve moving clipping planes “revealing” certain aspects of multiple data sets in the same animation, likely with some additional rotations etc applied to move around the data sets during the animation(s). This is fairly standard stuff I’d imagine, but it also ties into some work we have in evaluating ParaView as a viable option for dealing with the visualization of large (i.e., multl-terabyte) data sets.</p>
<p>I could not find a simple way to do this with Slicer; it seems that applying a clipping plane required me going through the segmentation editor, re-threshold the data to create a new segment, and then export segments as models to which I can finally apply a clipping plane. It’s not as intuitive as adding a clipping plane in Paraview, but there might well be more direct ways to accomplish this task that I’ve not been able to find as I’m pretty new to Slicer.</p>
<p>Thanks again!</p>

---

## Post #7 by @lassoan (2023-04-16 20:30 UTC)

<p>If you can “segment” by just thresholding then you don’t need to go through segmentation, etc. but you may use volume rendering directly.</p>
<p>You can animate coming rendering properties, clipping, etc. using Animation module in SlicerMorph extension.</p>
<p>You can also record and replay any node property changes (camera, slice views, display nodes, etc.) using Sequences module - but since keyframe animation is not available, this may not be an easy way to create animations.</p>
<p>If you want to visualize multi-terabyte images in Slicer then you can try the BigImage extension. It is still experimental, but already shows how easy it is to visualize very large data sets by leveraging Python packages that can provide any image region at any resolution. If you work with very large 3D medical images then it might be an avenue worth exploring. That said, ParaView is developed from the beginning for processing of very large data set on distributed systems, so if you need to perform not just visualization but complex interactive processing then ParaView is a very strong candidate.</p>

---

## Post #8 by @jgrime (2023-04-17 15:38 UTC)

<p>Hi Andras,</p>
<p>I’ve checked the documentation and I can’t see how to “use volume rendering directly” to get a clipping plane without going through the generation of a model. Are you talking about using a region-of-interest or something?</p>
<p>I’m taking a look at the SlicerMorph extension now - thanks for the suggestion!</p>
<p>Thanks.</p>

---

## Post #9 by @lassoan (2023-04-17 15:58 UTC)

<p>Yes, you can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html">Volume rendering</a> module and crop using an ROI box.</p>

---

## Post #10 by @jgrime (2023-04-17 17:11 UTC)

<p>That’s what I’ve been trying so far to avoid the whole “generate a model” dance, yes!</p>
<p>SlicerMorph’s animation functionality is quite interesting so far, but there’s an issue with changing the ffmpeg path in the Utilities → Screen Capture module so SlicerMorph’s animation tools can export to a video file: The modified ffmpeg file path (via Screen Capture’s “Advanced” tab) won’t actually be used unless I also e.g. click on the “Capture” button in the Screen Capture module and generate a dummy screenshot before trying to export a video in SlicerMorph.</p>
<p>Without that button click after updating the ffmpeg path, the new path does not seem to register with SlicerMorph. I’ll file a bug report on GitHub.</p>

---

## Post #11 by @jgrime (2023-04-17 17:31 UTC)

<p>Okay, I may struggle to use the SlicerMorph animation tools for our purposes; only one ROI modification is allowed for each animation, so I’d need to create a bunch of separate animations and splice them together afterwards.</p>
<p>Also, it would be really nice to be able to <em>precisely</em> specify the start/end times for each element in the animation rather than having to basically guess when trying to synchronize the start/end times of different parts of the animation via the slider control (which doesn’t seem to let you enter actual values, you’re limited to “this looks about the same”).</p>
<p>Other than these sorts of limitations, I like the SlicerMorph animation stuff - it’s pretty intuitive!</p>

---

## Post #12 by @pieper (2023-04-17 19:22 UTC)

<p>Thanks for the feedback on the Animator tool.  We had only limited resources to pull this together understanding it would have limitations but haven’t had a chance to go back and do a second pass on it.  The Animator leverages the Sequences and Screen Capture functionality but adds some high level python classes to implement the various actions, so if you have something specific in mind like sequencing a set of behaviors you can’t do with the GUI you could probably write a small python script to do it.</p>

---

## Post #13 by @jgrime (2023-04-17 20:36 UTC)

<p>Thanks, Steve!</p>
<p>I took a quick look at the source code for the Animator tool (specifically, “Animator.py”) to see why only one ROI modification might be supported in each animation, but multiple volume modifications can be used. I’m definitely not an expert on VTK, so this was out of curiosity more than an intent to modify anything for my own purposes!</p>
<p>Having said that, there’s nothing jumping out at me to indicate the reason only one ROI can be modified - so I tried creating two ROIs for the same source data in the Slicer GUI for volumetric rendering, and it seems only one of them can be displayed at a time; does this mean I’d need to load a duplicate copy of the same data set into Slicer and set that as the source data for a second ROI if I wanted to display e.g. disjoint regions of the same data set using ROIs in Slicer?</p>

---

## Post #14 by @pieper (2023-04-17 20:46 UTC)

<p>Right - the Volume Rendering module only supports a single ROI per volume.  But yes, you could use the multiple volume renderer to have multiple copies, and each could have their own ROIs that could be animated.</p>
<p>There are other options of course if you aren’t looking for real-time you could make a lot of interesting animation effects by scripting various slicer modules, like Crop Volume and Add Scalar Volumes.  I guess it’s all a function of how much effort you are able to devote to it.</p>

---
