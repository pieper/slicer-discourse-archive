# Dog brain DTI problems

**Topic ID**: 1850
**Date**: 2018-01-16
**URL**: https://discourse.slicer.org/t/dog-brain-dti-problems/1850

---

## Post #1 by @opetne (2018-01-16 03:07 UTC)

<p>Dear Users,</p>
<p>My name is Ors Petnehazy and I’m interested in 3D veterinary anatomical reconstrucions. I know some features of the Slicer. I made some reconstructions already (air sacs, horse stifle CT, MR, etc.).<br>
For a research project I need to reconstruct a dog brain DTI series. I followed the instructions I found made by Sonja Pujol with my own dataset. After some step I only get a dark “image” as a result. I’d like to ask for your help for DTI reconstruction of a dog brain DTI dataset.</p>
<p>Best,</p>
<p>Ors Petnehazy</p>

---

## Post #2 by @ihnorton (2018-01-16 14:48 UTC)

<p>Hi Ors,</p>
<p>Welcome to the forum. Could you clarify your workflow please?</p>
<ul>
<li>What Slicer version? What operating system?</li>
<li>What scanner did you use to scan?</li>
<li>Do you have DICOM images, and are you converting with DWIConvert? or some other steps?</li>
<li>Which step is run before you get the dark image?</li>
</ul>
<p>It may also be helpful if you can share the data, either converted or raw DICOM, using dropbox/onedrive/etc. If you prefer to share privately please email the download link to me at <code>inorton -at- bwh dot harvard dot edu</code>. (hopefully there should not be any confidentiality issues <img src="https://emoji.discourse-cdn.com/twitter/dog.png?v=5" title=":dog:" class="emoji" alt=":dog:">).</p>

---

## Post #3 by @opetne (2018-01-18 10:19 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="1850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>inorton -at- bwh dot harvard dot</p>
</blockquote>
</aside>
<p>I followed the steps again, written in the DiffusionMRIanalysis PDF. I attach the screen savings I made during the procedure.<br>
First, I’m not familiar with the DTI procedure, I understood only the basics but I try to do my best to improve in it.<br>
The dataset comes from a 3T Biograph (Siemens). I tried to find any information about the resulting files of the DTI measurement but I was not sure what dataset I have to open for the reconstrucions. I tried all of these for doing the DICOM to NRRD transformation but there was only one where the transformation was successfull. So I worked with this dataset.<br>
It was interesting that after each step when I changed the view from trans (red) to sagittal (yellow) for example the blue brain mask was on the new orientation. After making the brain mask, I saw that it contains the temporal muscles and the whole head as well… I was sure after this stpe that there is something not working properly…</p>
<p>I send you the dataset and the screen captures via wetransfer.</p>
<p>Kind regards,</p>
<p>Ors</p>

---

## Post #4 by @opetne (2018-01-18 10:20 UTC)

<p>Dear Isaiah,</p>
<p>Thank you for your offer. I wrote my impressions in a separate message.</p>
<p>Best,</p>
<p>Ors</p>

---

## Post #5 by @ihnorton (2018-01-19 17:29 UTC)

<p><a class="mention" href="/u/opetne">@opetne</a> thanks for sharing the data. The first dataset <code>ep2d_diff_mddw_64_p2</code> seems quite distorted and I didn’t get good results from it.</p>
<p>The second dataset <code>ep2d_diff_mddw_64_p2_4100_tra</code> looks pretty good. I recognize the major structures anyway (I don’t know anything about canine neuroanatomy!). I followed these steps:</p>
<ul>
<li>DWIConvert</li>
<li>Diffusion Brain Masking</li>
<li>Diffusion Tensor Estimation</li>
<li>Tractography Seeding module (see the “Slicer Neurosurgical Planning Tutorial” linked <a href="http://dmri.slicer.org/docs/">here</a>).</li>
</ul>
<p>From your screenshots, I think you did the same except the last step.</p>
<p>The resulting tracts seem ok (again with no specific knowledge). Here is a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f823a9c2f8b8569cc2a9656e56da92a37919262.jpeg" data-download-href="/uploads/short-url/fUs0PHkabdwYSHKlmDd1gyt7Tfc.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f823a9c2f8b8569cc2a9656e56da92a37919262_2_690x380.jpg" alt="image" data-base62-sha1="fUs0PHkabdwYSHKlmDd1gyt7Tfc" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f823a9c2f8b8569cc2a9656e56da92a37919262_2_690x380.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f823a9c2f8b8569cc2a9656e56da92a37919262.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f823a9c2f8b8569cc2a9656e56da92a37919262.jpeg 2x" data-dominant-color="484847"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×441 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regarding</p>
<blockquote>
<p>It was interesting that after each step when I changed the view from trans (red) to sagittal (yellow) for example the blue brain mask was on the new orientation.</p>
</blockquote>
<p>I think you may have several datasets open? They have different image sizes, so it could lead to some confusion. Also, you should use the DWI volume <code>ep2d_diff_mddw_64_p2_4100_tra</code> in Slicer. The other ones with e.g. <code>_TR</code> or <code>_FA</code> in the name are calculated on the scanner, and there seems to be some change in the orientation/origin so the images are not directly comparable.</p>
<p>Your screenshots look good so far, except the mask overlay issue. So, I suggest to work with your dataset <code>ep2d_diff_mddw_64_p2_4100_tra</code>, and also try some of the example tutorial data from the link above to learn more processing steps. If you have any more questions, please let us know.</p>
<p>Best,<br>
Isaiah</p>

---

## Post #6 by @opetne (2018-01-19 18:19 UTC)

<p>Dear Isaiah,</p>
<p>Thank you so much for this explanation. You are right the images seem<br>
distorted for me too, at the beginning I was wondering if there will be any<br>
useable results from this dataset.<br>
For my trials i was using only one dataset, I have to check which one it<br>
was but I guess it could comprise more image orientation.<br>
I’ll go trough the steps again and hopefully I can have better results.</p>
<p>Best,</p>
<p>Ors</p>
<p>Isaiah Norton <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> (időpont: 2018. jan. 19., P,<br>
18:39) ezt írta:</p>

---
