---
topic_id: 3161
title: "Automated Spinal Cord Segmentation"
date: 2018-06-12
url: https://discourse.slicer.org/t/3161
---

# Automated Spinal Cord Segmentation

**Topic ID**: 3161
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/automated-spinal-cord-segmentation/3161

---

## Post #1 by @Hikmat (2018-06-12 22:05 UTC)

<p>Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>I am aiming to automate spinal cord segmentation from MR images. I have been using Spinal Cord Toolbox (SCT); a Linux-based open-source software dedicated specifically to the processing and analysis of the spinal cord. The documentation of the Spinal Cord Toolbox module <em>sct_propseg</em> which I have been using is listed here: <a href="https://sourceforge.net/p/spinalcordtoolbox/wiki/sct_propseg/" class="inline-onebox" rel="noopener nofollow ugc">Spinal Cord Toolbox / Documentation / sct_propseg</a></p>
<p>I have been testing SCT’s automated segmentation through Slicer and it works for this MR image of the cervical vertebrae:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e9553cd5aea20c0e868068ae533cb336c8547cb.jpeg" alt="image" data-base62-sha1="fMgs9EWBrEaE4W6R824yhMsXjhV" width="526" height="243"></p>
<p>However, the issue I am experiencing is poorly automated spinal cord segmentation for my lumbar vertebrae images. In fact, SCT seems to fail to segment my T1 image. Even stranger, my T2 image (spinal cord = dark, CSF = bright) is being segmented poorly when selected as a T2 image but adequately when selected as a T1 image (spinal cord = bright, CSF = dark).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14ff42c9c4b07b36fef5b0e5a55a4fbb0112589a.jpeg" alt="image" data-base62-sha1="2ZKrudODT8n5euMFCNfOzaCynii" width="688" height="371"></p>
<p>I believe that the lumbar vertebrae images are not being processed correctly due to the spinal cord not being well-defined as well as poor contrast between the spinal cord and the cerebrospinal fluid (CSF):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc09955b3194451e38acb92818f5505a052c1906.jpeg" alt="image" data-base62-sha1="zXCR0oy6DlUTmxmr6aXyWBr6Znw" width="682" height="300"></p>
<p>In fact, the recommendations listed here <a href="https://sourceforge.net/p/spinalcordtoolbox/wiki/correction_PropSeg/" class="inline-onebox" rel="noopener nofollow ugc">Spinal Cord Toolbox / Documentation / correction_PropSeg</a> suggest that the image should be edited to more clearly enhance these features. However, these editing procedures are complicated and my workflow would no longer consist of automated segmentation.</p>
<p>I have investigated equivalent Slicer semi-automated segmentation tools as an alternative and indeed, they work for the cervical vertebrae image. Some initialization (albeit very limited) is required by the user (which may impede its effectiveness); moreover, these tools do not perform as well as SCT but are satisfactory enough for my needs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f98082c530cf9dbf990c3af6224b180f94f8fa0.jpeg" data-download-href="/uploads/short-url/2dWT79gxoEAEDluGHOHGmRDSxiw.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f98082c530cf9dbf990c3af6224b180f94f8fa0_2_690x195.jpg" alt="image" data-base62-sha1="2dWT79gxoEAEDluGHOHGmRDSxiw" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f98082c530cf9dbf990c3af6224b180f94f8fa0_2_690x195.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f98082c530cf9dbf990c3af6224b180f94f8fa0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f98082c530cf9dbf990c3af6224b180f94f8fa0.jpeg 2x" data-dominant-color="5E5E5B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">761×216 70.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Unfortunately though, these tools are not adequate for the lumbar vertebrae images discussed above.</p>
<p>Thus, any suggestions on how I should proceed or advice concerning the appropriate tools or programs that can automate spinal cord segmentation would be greatly appreciated.</p>
<p>Thanks.</p>

---

## Post #2 by @Michael_Hardisty (2018-06-13 11:49 UTC)

<p>Hi Hikmat,</p>
<p>For help with SCT specifics of their algorithm, I would ask the SCT developers for help.  You could submit an issue on their github, <a href="https://github.com/neuropoly/spinalcordtoolbox/issues" rel="nofollow noopener">https://github.com/neuropoly/spinalcordtoolbox/issues</a> or write Julien an email.</p>
<p>Michael</p>

---

## Post #3 by @lassoan (2018-06-13 22:59 UTC)

<blockquote>
<p>Some initialization (albeit very limited) is required by the user (which may impede its effectiveness)</p>
</blockquote>
<p>You can usually automate seed placement and thus have a completely automatic method. For example you can register a generic “atlas” image and transferring seeds to the patient image. Or you may use simple global thresholding to get candidate regions and keep the most likely candidate (that meets minimum size and shape requirements). You may also use the segmentation that sct provides as seed: you shrink it by a few mm and use that as spinal cord segment, and expand by a centimeter and use that as background segment. The advantage is that you can add more seeds manually to fix segmentation in regions where sct registration failed.</p>
<aside class="quote no-group" data-username="Hikmat" data-post="1" data-topic="3161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>Unfortunately though, these tools are not adequate for the lumbar vertebrae images discussed above.</p>
</blockquote>
</aside>
<p>Grow from seeds and Watershed allows interactive seed editing, so they work on any images, they can even separate regions where there is no image contrast at all. The question is how much additional seed is needed. If you spend several minutes specifying additional seeds then you may just as well use more manual methods, such as interpolate between slices.</p>
<p>“Interpolate between slices” effect allows you to interpolate segmentation between slices. For example, you can segment on 20-30 slices and the effect computes segmentation between these. You can then review segmentation results and if you find that deviation on any interpolated slice is too much then you segment that single slice and the full segmentation is updated immediately.</p>
<p>We can give you more specific advice, if you provide example images and information on constraints (what should be segmented exactly, how accurate the segmentation has to be, how much time is available for segmentation, etc).</p>

---

## Post #4 by @Hikmat (2018-06-14 22:05 UTC)

<p>Thanks for the detailed response as always, Andras.</p>
<p>In terms of what exactly needs to get segmented, a correct interpretation of MR images of the spine is needed.</p>
<p>For T1 images, the spinal cord (the R.O.I) is identified as follows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2a0da4fbb7839e87697342bfd0c66b9e1faa83.jpeg" alt="image" data-base62-sha1="diavdyZ1QNwuydPl9bnMHhVrTdF" width="670" height="331"></p>
<p>For T2 images, the spinal cord is interpreted differently:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37902d83f9d3ba54407b9b2bd3eff6e38af031e2.jpeg" alt="image" data-base62-sha1="7Vx9Wu4SbW5LZH5GiyZdRWc4Ixk" width="670" height="332"></p>
<p>As for how accurate the segmentation needs to be, the contrast between the spinal cord and the CSF needs to be recognized. More specifically, the spinal cord is typically well-defined in MR images (a definite outline) and so the segmentation should define the spinal cord according to this feature.</p>
<p>Finally, the segmentation technique should be as automated as possible. There are many Slicer tools that are quite powerful but the manual nature of these tools may be overwhelming to the user. Moreover, I think the issue is that most Slicer tools work on the principles of intensity-based definition: ie. the <em>Threshold</em> effect. This poses an issue though, since the interior of the spinal cord is either not of a consistent intensity or it is of an intensity equal to that of other components of the spine - thus rendering <em>Threshold</em> ineffective.</p>
<p>In addition, while <em>Grow from seeds</em> and <em>Watershed</em> are powerful tools, the many seeds required to yield an accurate segmentation detracts from the automation of the tool. Furthermore, <em>Interpolate between slices</em> is too manual for my needs. SCT’s <em>sct_propseg</em> thus seems like the most promising tool; but there are issues with its performance and their developers are looking into the matter.</p>
<p>The structure of the spinal cord is evident by its outline; which is defined by the contrast of the CSF surrounding it. Perhaps there is a tool / script that can recognize a "<em>boundary change"</em> between different components in an image?</p>
<p>Hopefully I have broken things down more clearly and that a solution may present itself - preferably Slicer-based but I am open to outside tools too (i.e. SCT).</p>
<p>Thanks in advance.</p>

---

## Post #5 by @lassoan (2018-06-15 04:33 UTC)

<aside class="quote no-group" data-username="Hikmat" data-post="4" data-topic="3161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>most Slicer tools work on the principles of intensity-based definition: ie. the <em>Threshold</em> effect</p>
</blockquote>
</aside>
<p>Some effects use global threshold, but most semi-automatic methods use gradient (intensity change) instead. You can segment structures that have varying intensity, as long as there is some intensity difference at its boundary. For example, Grow from seeds, Watershed, and Fast marching all put segment boundaries at where image intensity suddenly changes.</p>
<p>I had a look at the images that you’ve shared and indeed it is not easy to segment the spinal cord from them.</p>
<p>One problem is that the resolution of the volumes are highly anisotropic (spacing between sagittal image planes is 6x more than in-plane spacing). Resampling the volume before segmentation to have isotropic spacing improves the result (using Crop volume module, isotropic spacing option), but of course it would be better to acquire images that have less spacing between slices.</p>
<p>VMTK did not work very well, as it relies on a pre-processing filter that detects tubular structures and this filter does not enhance the the spinal cord.</p>
<p>Grow from seeds and Watershed seems to require too much tuning of the seeds, so it is not worth the time if you only need the cord. If you want to segment cord, CSF, fat, etc. then it could be a good approach.</p>
<p>For me, the most effective method was to contour on 8 slices using Draw effect and then get full 3D segmentation using Fill between slices. The whole process takes 2 minutes. The accuracy is as good as the operator’s best judgement, and it is very easy to make manual adjustments if needed.</p>
<p>If some toolkits offer acceptable automatic registration then of course use that; but if they do not work (because image quality is not good enough, uncommon patient anatomy, etc.) then Draw+Fill between slices could be a good choice.</p>

---

## Post #6 by @lassoan (2018-06-15 04:37 UTC)

<p>Can I add these findings and your sample images to <a href="https://lassoan.github.io/SlicerSegmentationRecipes/">segmentation recipes</a>?</p>

---

## Post #7 by @Hikmat (2018-06-15 19:13 UTC)

<p>I think this will be a valuable contribution to the Slicer learning community; I may have to check with the lab though.</p>
<p>EDIT: Posting the images for access and download would be a problem.</p>

---

## Post #8 by @Hikmat (2018-06-15 20:25 UTC)

<p>I appreciate your valuable insight into this matter. I have also tested these tools in detail and it is reassuring to know that I am reaching the same conclusions. I did not consider the Draw + Fill as I deemed it too manual but it is indeed giving me the best results.</p>
<p>I was given these images for testing purposes to use for my simulator and perhaps the quality is simply not good enough. Interestingly enough, the SCT developers also commented about the anisotropic property of the images and its effect on performance. They now have a better understanding of my constraints / objectives and are looking into the matter. If some useful findings are made, I can report them here.</p>

---

## Post #9 by @jcohenadad (2019-01-08 19:49 UTC)

<p>Hi,</p>
<p>Thank you for your feedback. Please note that SCT now has another method for spinal cord segmentation based on deep learning called <code>sct_deepseg_sc</code>, which in some cases is more robust than <code>sct_propseg</code>. More information <a href="https://www.slideshare.net/neuropoly/sct-course-20190121#35" rel="nofollow noopener">here</a>.</p>
<p>Best,<br>
Julien</p>

---

## Post #10 by @chancock (2020-07-03 12:42 UTC)

<p>Has there been further progress in semi &amp; auto-segmentation of MRI studies of spine?</p>

---

## Post #11 by @lassoan (2020-07-03 19:14 UTC)

<p>I don’t know if anything significant happened on the algorithms side, but there have been lots of enhancements in Slicer that may be relevant for you.</p>
<ol>
<li>
<p>Now you can run deep-learning based segmentation methods directly in Slicer. If there is any spine segmentation methods that you know that works well then you can create a small plugin that makes it available in the Segment Editor with a convenient user interface.</p>
</li>
<li>
<p>New segmentation tools have been added. If the image is sufficiently good quality then you can segment the spinal cord by a few clicks. If you describe your requirements and main challenges and share an anonymized image (at least screenshots) then we can give more specific advice.</p>
</li>
</ol>

---
