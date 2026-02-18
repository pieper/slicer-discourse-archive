# Assessing accuracy of MR/CT registration 

**Topic ID**: 19471
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/assessing-accuracy-of-mr-ct-registration/19471

---

## Post #1 by @jdh (2021-09-01 19:34 UTC)

<p>Hello,</p>
<p>Does Slicer have any way of assessing the accuracy a registration between two images?</p>
<p>I have CTA and MRA image sets of the same patient (the timepoints for the two are only about a week apart) and I want to align the two images with an emphasis on aligning the arteries in the Circle of Willis. Ultimately, I will be segmenting the MR images and comparing the 3D CoW model to the CTA images to determine how well the model’s vessel diameters match CTA. Our hypothesis is that there are certain features that MR cannot well resolve (e.g., vessel stenosis) that will be more accurately captured by CTA. We have techniques using x-ray angiograms to adjust the features, but we want to know if we really are getting the model geometry closer to being correct.</p>
<p>For the comparison between the 3D model and the CTA images to have any meaning, we need the MR and CTA images (or at least the vessels in them that we care about) to be well aligned. I have tried several iterations of rigid alignment with various parameters and masking schemes using the BrainsFit module. I have a few registrations that visually look pretty good, but I am wondering if there is a metric or module in Slicer that will quantify how “good” each alignment is so that I can pick the best one and also gauge if my attempts at improving the registration by tweaking parameters are actually accomplishing anything.</p>
<p>I would appreciate any suggestions you might have. Thanks!</p>

---

## Post #2 by @pieper (2021-09-01 20:22 UTC)

<p>Unless you have “real” ground truth, which you wouldn’t in a real clinical case then visual inspection is typically your best approach.  If you see anything that is clearly incorrect then you can measure it with a ruler or you can put multiple paired landmarks and measure the average/min/max/std error.  But if the landmarks are that far off you probably can find a better registration method, like cropping the images, matching the spacing, or using a different tool like Elastix or ANTS extensions.</p>

---

## Post #3 by @mikebind (2021-09-01 21:57 UTC)

<p>Registration methods work by defining a cost metric, such as mutual information, and then trying to optimize that metric by moving one image relative to the other and trying to minimize the cost.  However, the metric is not as simple as “how far off is this registration from correct?”, because if we knew the correct registration, there would be no need to perform an optimization, we would just jump to the correct registration.  Once you’re pretty close, a transformation which produces a lower cost metric value is very likely better than one which produces a higher cost metric; in light of that, I think that when you are looking at the registration between two particular image volumes and tweaking parameter values, you can look at the final value of the cost metric in each registration to decide which parameter sets give you the best registration.  However, that information is specific to that pair of images and there is no guarantee that a different pair of images will have optimal results with the same parameter set, and no guarantee that a different pair of images will have the same (or even very similar) optimal cost metric values.  Ultimately, your eyes are the guide as to whether the registration is “good” or not.</p>
<p>If registration is generally pretty good (i.e. skull lines up very well), but not good enough (your arteries of interest don’t line up well enough), then I think <a class="mention" href="/u/pieper">@pieper</a> 's suggestion of cropping the images to your region of interest before registration is likely to be helpful.</p>
<p>Another possible approach would be to do the segmentation of the structures of interest in the CT and then separately in the MR, and then try to register or compare measurements on the segmented structures.  Perhaps it doesn’t matter if you can line them up perfectly if you can say that the narrowest point on the vessel on the CT is 40% less than the narrowest point on the MR.</p>

---

## Post #4 by @hotsen (2021-09-28 16:37 UTC)

<p>I have a similar question, so I just reply here instead of opening another topic. I am doing MR to CT registration using BRAINSfit module ( running CLI as slicer.cli.run(slicer.modules.brainsfit, parameters= parameters)  ). The same settings were applied to 40 registrations (same patient, same CT, different time points MR). Is there an easy way to evaluate all the registrations instead of looking through the images one by one? This project is going to apply the settings to hundreds more of registrations, so visual inspection is not feasible.</p>
<p>Is there a way to output the cost value or metric for each registration, so I can plot a curve for all registrations and determine which one is “bad” (with a high cost value compare to others)? I wish it could be this simple, but any suggestion would be appreciated. <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>There are “costFunctionConvergenceFactor: (a float)” and “costMetric: (‘MMI’ or ‘MSE’ or ‘NC’ or ‘MC’)” in BRAINSfit, but I am not sure this is what I want and how to output this.</p>
<p>Thank you.</p>
<p>Hotsen</p>

---

## Post #5 by @lassoan (2021-09-28 18:53 UTC)

<p>There is no reliable automatic metric for assessing registration quality.</p>
<aside class="quote no-group" data-username="hotsen" data-post="4" data-topic="19471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ba9def/48.png" class="avatar"> hotsen:</div>
<blockquote>
<p>Is there a way to output the cost value or metric for each registration, so I can plot a curve for all registrations and determine which one is “bad” (with a high cost value compare to others)?</p>
</blockquote>
</aside>
<p>It would not be hard to implement this, but similarity metrics that are used during registration would be very bad for assessing registration quality. One issue is that the similarity metric value is usually not clinically meaningful, so you cannot specify a threshold value for acceptable registration. But the bigger problem is that the similarity metric was used as the value that was minimized during registration, therefore even if the registration completely diverged to a very bad pose, you can get a nice low value. Finally, often registration is important in a specific part of the image, so quality is better reflected by a metric that measures misalignment in the clinical region of interest.</p>
<aside class="quote no-group" data-username="hotsen" data-post="4" data-topic="19471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ba9def/48.png" class="avatar"> hotsen:</div>
<blockquote>
<p>There are “costFunctionConvergenceFactor: (a float)” and “costMetric: (‘MMI’ or ‘MSE’ or ‘NC’ or ‘MC’)” in BRAINSfit, but I am not sure this is what I want and how to output this.</p>
</blockquote>
</aside>
<p>These are all similarity metrics used during registration and due to the above described regions, they are not suitable for assessing registration quality.</p>
<p>I’m not aware of any easy (“no effort”) solution for quantitative assessment of registration accuracy. Most common solutions are the followings:</p>
<ul>
<li>Specify matching anatomical landmark points (or artificial landmarks, such as gold seeds or other fiducial markers) in the moving and fixed images and measure the distance between the fixed landmark and the transformed moving landmark. Unfortunately, matching anatomical landmarks cannot be always identified, their position may not be always specified accurately (e.g., if you have large spacing between slices), or they may be farther from the clinical region of interest.</li>
<li>Segment structures in the fixed and moving image, then compare the difference between the fixed segment(s) and the transformed moving segment(s). The advantage of this method is that segmenting a structure may be done more reliably and may be easier to automate than accurate landmark point placement. Disadvantage is that you can only measure error on the surface of the structures, so you cannot get reliably 3D error value in a selected point.</li>
</ul>

---

## Post #6 by @hotsen (2021-09-29 16:50 UTC)

<p>Hi Andras,</p>
<p>Thank you for your reply, really helps a lot. If I want to use automated segmentation in both fixed and moving volume to assess the registration, should I assess the segmentation first? Looks like it will make things more complicated.</p>

---

## Post #7 by @lassoan (2021-09-29 16:53 UTC)

<p>Yes, if you want to use segmentation to evaluate registration error then you must make sure the segmentation is consistent between the two images. Segmentation indeed may be easier or harder than registration, depending on the image content.</p>

---
