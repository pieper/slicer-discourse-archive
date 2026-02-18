# Fill between slices

**Topic ID**: 6276
**Date**: 2019-03-25
**URL**: https://discourse.slicer.org/t/fill-between-slices/6276

---

## Post #1 by @PaoloZaffino (2019-03-25 13:54 UTC)

<p>Hi all,<br>
I have a question about the function “Fill between slices” in the segment editor.</p>
<p>How are the slices interpolated?<br>
Linear, Spline? Any intensity information used or just contours geometry?</p>
<p>Thanks a lot.<br>
Paolo</p>

---

## Post #2 by @cpinter (2019-03-25 15:28 UTC)

<p>Hi Paolo,</p>
<p>I hope you’re doing great <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>The interpolation algorithm under the hood is ultimately this one:<br>
<a href="https://itk.org/Doxygen/html/classitk_1_1MorphologicalContourInterpolator.html" class="onebox" target="_blank" rel="nofollow noopener">https://itk.org/Doxygen/html/classitk_1_1MorphologicalContourInterpolator.html</a><br>
It is used with the default parameters.</p>
<p>It does not take intensity information into account (see the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorFillBetweenSlicesEffect.py#L41-L46" rel="nofollow noopener">code</a>, where the only input of the filter is the labelmap).</p>

---

## Post #3 by @PaoloZaffino (2019-03-25 15:53 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a>!<br>
I’m doing fine <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Thanks for helping, I think I found the article as well.<br>
It should be:</p>
<blockquote>
<p>Blockquote Albu, A.B., Beugeling, T. and Laurendeau, D., 2008. A morphology-based approach for interslice interpolation of anatomical slices from volumetric images.  <em>IEEE Transactions on Biomedical Engineering</em> ,  <em>55</em> (8), pp.2022-2038.</p>
</blockquote>
<p>Thanks a lot!<br>
Paolo</p>

---

## Post #4 by @Leon (2019-06-27 20:32 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The interpolation algorithm under the hood is ultimately this one:<br>
<a href="https://itk.org/Doxygen/html/classitk_1_1MorphologicalContourInterpolator.html" rel="noopener nofollow ugc">https://itk.org/Doxygen/html/classitk_1_1MorphologicalContourInterpolator.html </a><br>
It is used with the default parameters.</p>
<p>It does not take intensity information into account (see the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorFillBetweenSlicesEffect.py#L41-L46" rel="noopener nofollow ugc">code</a>, where the only input of the filter is the labelmap).</p>
</blockquote>
</aside>
<p><span class="mention">@Csaba</span>.<br>
I have experience with a more or less similar tool in Mimics, called ‘Multiple slice Edit’. For me it has been very usefull when segmenting for instance a vessel, or a tibia in a MRI.<br>
The way I always use the tool is in combination with a threshold setting.</p>
<p>In short it works like this:<br>
– I start by choosing the correct threshold for the part I want to segment (or remove from a mask).<br>
– With the “Multiple slice edit’ I then draw a region around that particular part on multiple, non adjacent slices, just like it is done with the ‘Fill between slices’ in Slicer.<br>
– Then I let the tool interpolate a temporary mask. This temporary masks then includes the part.<br>
– Finally I can choose whether I want to add or remove the part and hit apply.<br>
The resulting mask then shows a nice, continuous mask.</p>
<p>I would love to see this feature in Slicer’s ‘Fill between slices’ tool. Do you think it’s possible to include it?</p>
<p>For some more information on how the ‘Multiple slice edit’ works, I’ve attached a link to a pdf (page 33).<br>
<a href="https://www.researchgate.net/file.PostFileLoader.html?id=5686aa597dfbf9d5458b458b&amp;assetKey=AS%3A313124089991168%401451666008906" rel="noopener nofollow ugc">https://www.researchgate.net/file.PostFileLoader.html?id=5686aa597dfbf9d5458b458b&amp;assetKey=AS%3A313124089991168%401451666008906</a>).</p>

---

## Post #5 by @cpinter (2019-06-27 21:07 UTC)

<p>I don’t quite understand neither how the threshold is used nor why you’d remove.</p>
<p>In case this information is useful</p>
<ul>
<li>You can define a threshold for edited region in the masking options on the bottom. Only those voxels are affected by any editing operation that are within the threshold</li>
<li>The logical operator allows subtracting a segment from another (or you can specify editable area as outside segment in the masking options)</li>
</ul>

---

## Post #6 by @Amine (2019-06-28 00:30 UTC)

<p>Could be done on slicer, just make a first segment with a threshold then another with with “fill between slices” then do a logical operations&gt; intersect</p>

---

## Post #7 by @cpinter (2019-06-28 01:39 UTC)

<aside class="quote no-group" data-username="Amine" data-post="6" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>threshold then another with with “fill between slices” then do a logical operations&gt; intersect</p>
</blockquote>
</aside>
<p>If this is the goal then it’s easier to do a single Fill between slices with threshold set for Editable intensity range within Masking options. No second segment, no logical operators.</p>

---

## Post #8 by @Leon (2019-06-28 08:30 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I don’t quite understand neither how the threshold is used nor why you’d remove.</p>
</blockquote>
</aside>
<p>To give you an example. Recently I was asked to segment a MRI of a pelvis from a patient with a tumor. The surgeon needed the segmentation for his orientation during the operation. Close to this tumor there was a large blood vessel, so for his convenience I also segmented that.<br>
In MRI the gray values are much harder to handle then in a CT. For this the ‘Multiple slice edit’ (or the ‘Fill between slices’) can be very helpfull.</p>
<p>Doing this in Mimics with the ‘Multiple slice edit’ is very simple.<br>
Let’s say I only want to segment a length of 10 cm. I start by determining which gray values represent the blood vessel. Then with the ‘Multiple slice edit’ I first draw my top slice well around the blood vessel and then my bottom slice, 10 cm lower. Next I let the algorithm calculate/interpolate a temporary 3D-mask. This is also done with some sort of morphing. The temporary mask then includes the part of the blood vessel I want to segment. Within this 3D-mask the tool then decides which voxel gray values (the vessel) correspond to my threshold settings and then it’s up to me to decide whether I want to add or remove these voxels to my final 3D-mask.</p>
<p>I’ve tried this also with the Editable intensity range of ‘Fill between slices’ and it does work, but still it uses it’s contour interpolation which leads to a less accurate, jaggy mask (when smoothing is off, of course) and that’s not what I want.<br>
Also if there is a large change in morphology of the object in between the selected slice (for instance because it changes direction), Mimics does the job well, as long as the object stays within the temporary 3D-mask. With Slicer you have to select extra slices to correct for this, but still the result is less accurate.</p>
<p>If you or someone else knows another easy way or workaround for this, please let me know.</p>

---

## Post #9 by @Leon (2019-06-28 08:56 UTC)

<p>Well, I’ve just discovered my own solution! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>
<p>When I read through my post I came to this workflow:</p>
<ul>
<li>First I start with a segment in which I use the  ‘Fill between slices’ tool to define a 3D-mask that includes my object of interest.</li>
<li>Then I start a second segment, choose the threshold tool to define the correct thresholds for this object, select the first mask as my ‘Editable area’ and hit apply.<br>
Viola! Done!</li>
</ul>
<p>Thanks!</p>

---

## Post #10 by @pieper (2019-06-28 10:21 UTC)

<p>This sounds great <a class="mention" href="/u/leon">@Leon</a>, would it be possible to add a couple screenshots?</p>

---

## Post #11 by @cpinter (2019-06-28 12:37 UTC)

<p>To further simplify this workflow:</p>
<ul>
<li>Set threshold values in Threshold tool but don’t apply, instead select Use for masking</li>
<li>Use Fill between slices (or any other tool)</li>
</ul>
<p>You’ll notice that this will yield equivalent results.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4db4b9fd2d5745f5250688ecd76d508ef261fec.png" data-download-href="/uploads/short-url/un13QfhSfp2QzBsf9kCyCFOQjfu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4db4b9fd2d5745f5250688ecd76d508ef261fec.png" alt="image" data-base62-sha1="un13QfhSfp2QzBsf9kCyCFOQjfu" width="690" height="205" data-dominant-color="EFEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1133×337 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Leon (2019-06-28 13:21 UTC)

<p><a class="mention" href="/u/steve">@Steve</a>.<br>
Here you see the procedure for making the temporary mask + unsmoothed result in 3D-viewer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f00b1b2c8962a5cb1e0f1e747de364cae90f44f.png" data-download-href="/uploads/short-url/mGBp6JpoIXhxU1O0G5v49Cb9qFh.png?dl=1" title="Temporary%20segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f00b1b2c8962a5cb1e0f1e747de364cae90f44f_2_690x177.png" alt="Temporary%20segment" data-base62-sha1="mGBp6JpoIXhxU1O0G5v49Cb9qFh" width="690" height="177" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f00b1b2c8962a5cb1e0f1e747de364cae90f44f_2_690x177.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f00b1b2c8962a5cb1e0f1e747de364cae90f44f_2_1035x265.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f00b1b2c8962a5cb1e0f1e747de364cae90f44f.png 2x" data-dominant-color="A7AAAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Temporary%20segment</span><span class="informations">1280×329 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then the thresholding for the second segment (I removed the non-connected area’s with the island tool).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/891365cde09b4ffa3b58c2b3e6b5a85421844ded.png" data-download-href="/uploads/short-url/jyCYjlbnKTZZ1LqpwZDPwijE2rH.png?dl=1" title="Final%20segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/891365cde09b4ffa3b58c2b3e6b5a85421844ded_2_690x349.png" alt="Final%20segment" data-base62-sha1="jyCYjlbnKTZZ1LqpwZDPwijE2rH" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/891365cde09b4ffa3b58c2b3e6b5a85421844ded_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/891365cde09b4ffa3b58c2b3e6b5a85421844ded.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/891365cde09b4ffa3b58c2b3e6b5a85421844ded.png 2x" data-dominant-color="C4C3CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Final%20segment</span><span class="informations">693×351 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><span class="mention">@Csaba</span>.<br>
This is the result that comes out of your method. I’ve used the same slices as in my one method.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83fe530f871e17049ea06ea6832e557fca6a34b5.png" alt="Csaba's%20method" data-base62-sha1="iPFr2ZtVhW1sKrg6KUPxup0gNaB" width="263" height="342"></p>
<p>So it’s up to you guys to tell which one is the best. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @lassoan (2019-06-28 15:28 UTC)

<p>You may further improve segmentation result if you use Crop volume module to resample the input volume to have isotropic resolution before segmenting it.</p>

---

## Post #14 by @aiNeander (2019-07-26 13:40 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="2" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><a href="https://itk.org/Doxygen/html/classitk_1_1MorphologicalContourInterpolator.html" class="inline-onebox" rel="noopener nofollow ugc">ITK: itk::MorphologicalContourInterpolator&lt; TImage &gt; Class Template Reference</a></p>
</blockquote>
</aside>
<p>I use Mimics primarily at work and use the Multislice Edit tool All The Time. The work around you say here is what I’ve been doing for my micro-CT scans on my personal project at home. It’s clunky, and I wish the Fill between slices was less jagged, but it works… slowly. What I would give for a smoother Fill between slices!</p>
<p>I’m trying to separate bones of the skull, so the suture lines are sometimes almost non-existant, so more automated tools don’t work for me.</p>
<p>Good to know there is another Mimics user out here facing the same challenges.</p>

---

## Post #15 by @cpinter (2019-07-26 14:13 UTC)

<aside class="quote no-group" data-username="aiNeander" data-post="14" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/48db29/48.png" class="avatar"> aiNeander:</div>
<blockquote>
<p>What I would give for a smoother Fill between slices!</p>
</blockquote>
</aside>
<p>You can change the resolution of the segment labelmaps to make the raw segmentation smoother using the box icon next to the master volume selector.</p>
<p>Also you can use the Smooth effect to perform additional smoothing if needed.</p>

---

## Post #16 by @lassoan (2019-07-26 16:16 UTC)

<p>Thanks for the feedback. Our goal is to make Slicer’s image segmentation tools work better than Mimics. I think we are already achieved this in many aspects, but if there is anything that you cannot find in Slicer or feel that could be improved then let us know.</p>

---

## Post #17 by @aiNeander (2019-07-26 16:58 UTC)

<p>Thanks for the tips, cpinter. I didn’t know about the ability to break the segmenting voxels into smaller units. I’m assuming that this would take up more RAM and make things slower, though? However, this may make all the difference because I can see the sutures between skull bones, but it is only one voxel wide in places and therefore not enough to really register with the automated tools. I’ve been looking into getting a computer with more RAM anyways.</p>
<p>Also, I’ll try smoothing what I think of as my ‘temporary selection layer’ after I apply Fill between slices. It’s another step, but likely faster than cleaning up that selection by hand.</p>
<p>lassoan, one other thing that would make a big difference for me is how Fast Marching works. The way the tool works now, you limit it to a percentage of the whole volume. I’d like to use the tool for very local regions, but I can’t go smaller than 0.01%. It would be much more useful to be able to limit it to n voxel radius (eg look only within a 10 voxel radius). What I have in mind is a little closer to how VG Studio works in that regard.</p>
<p>Thanks both for the suggestions!</p>

---

## Post #18 by @pieper (2019-07-27 12:27 UTC)

<p>Hi <a class="mention" href="/u/aineander">@aiNeander</a> - we don’t typically use the commercial tools, so if you can provide illustrative examples, either with Slicer’s SampleData or with data you can share, where you find Slicer’s tools could be improved please share as much detail as you can (e.g. screenshots of the level of segmentation detail you need to achieve).</p>
<p>Regarding the Fast Marching min size, that’s a good suggestion (knowing Andras he’s probably already fixed that while I’ve been typing!).</p>

---

## Post #19 by @lassoan (2019-07-27 13:55 UTC)

<aside class="quote no-group" data-username="aiNeander" data-post="17" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/48db29/48.png" class="avatar"> aiNeander:</div>
<blockquote>
<p>this may make all the difference because I can see the sutures between skull bones, but it is only one voxel wide in places</p>
</blockquote>
</aside>
<p>Due to discretization of distances, image noise, and partial volume effect, you cannot reliably work with structures with thickness of a single voxel. Probably you need to at least double or triple the resolution, which would make the total volume size 8x or 27x larger. To keep memory size and computation time under control, crop the volume to the region that contains the region of interest. It is also advisable to resample your volume to have isotropic spacing. You can do all these operations in one step, using Crop volume module. If your region of interest is large and you need high resolution then you may need a strong computer (lots of RAM and CPU with high clock speed).</p>
<aside class="quote no-group" data-username="aiNeander" data-post="17" data-topic="6276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/48db29/48.png" class="avatar"> aiNeander:</div>
<blockquote>
<p>I’d like to use the tool for very local regions, but I can’t go smaller than 0.01%.</p>
</blockquote>
</aside>
<p>If you reduce the maximum volume then initialization will be faster and for example by setting 0.01% for maximum volume then 0.01% for segment volume, the total is 0.0001%, which should be small enough for most cases. If not, then press <code>Ctrl</code> - <code>+</code> to show more decimals and enter values smaller than 0.01.</p>
<p>How do you use Fast marching for segmenting very local regions? We normally use Fast marching for segmenting an entire region, as you can specify many seeds.</p>
<ul>
<li>If you want to just click a point and add similar regions around it: Then “Flood filling” effect may be more suitable. Than fast marching.</li>
<li>If you specify many seed points and want to constrain fast marching around it then we could enable masking for this effect to constraint growing to be within a specific mask segment. We haven’t enabled masking for Fast marching yet because for such cases the much more versatile “Grow from seeds” effect can be used instead, which already supports masking and multiple input segments. Grow from seeds allows you to work within a predefined masked region (that you can create using any other effects) and then use seeds to grow and split segments within the masked region, with interactive updates, with real-time 3D preview.</li>
</ul>
<p>There are so many very powerful tools in Slicer that can be used in combination to solve very challenging segmentation tasks, but it is not trivial to come up with a good segmentation workflow. If you provide more information as <a class="mention" href="/u/pieper">@pieper</a> suggested above then we can give more specific advice.</p>

---
