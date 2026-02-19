---
topic_id: 17590
title: "Convert Mri Image Saved In Dicom File To Nrrd Format"
date: 2021-05-12
url: https://discourse.slicer.org/t/17590
---

# Convert MRI image saved in dicom file to nrrd format

**Topic ID**: 17590
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/convert-mri-image-saved-in-dicom-file-to-nrrd-format/17590

---

## Post #1 by @EddardaaBL (2021-05-12 12:28 UTC)

<p>Hi everyone</p>
<p>I appreciate you help if you could reply to my following requests:</p>
<p>1.I trying to install stable release of 3D slider on Ubuntu 16.04 but i couldn’t and when i checked the tutorial i found that it require Ubuntu 18.04 or late, so how I can do to install it?</p>
<ol start="2">
<li>
<p>I wanted to use 3D slider to convert the ProstateX dataset to nrrd format them use pyradiomics tools to extract the features, it’s possible to convert the whole dataset and also the true mask using 3D slider ?</p>
</li>
<li>
<p>my last question is about the dataset itself, I couldn’t visualize which file represents the segmented label in dataset for each patient, anyone have an idea, it would be a huge help for me.</p>
</li>
</ol>
<p>sorry if I asked a lot, I never work before on medical image and I am getting confused between the concepts and the modalities.</p>
<p>waiting for your response soon.</p>
<p>Kind regards,</p>

---

## Post #2 by @lassoan (2021-05-13 05:31 UTC)

<p>I don’t think there is anything that would prevent Slicer running on Ubuntu 16.04 (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">Linux install instructions</a>). We just don’t test with this Ubuntu version anymore. We haven’t heard other users complaining about this, so either not many people use Ubuntu 16 anymore or Slicer works for most of them.</p>
<aside class="quote no-group" data-username="EddardaaBL" data-post="1" data-topic="17590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ed8c4c/48.png" class="avatar"> EddardaaBL:</div>
<blockquote>
<p>it’s possible to convert the whole dataset and also the true mask using 3D slider ?</p>
</blockquote>
</aside>
<p>Yes, you can everything either using the GUI or using Python scripting. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>
<aside class="quote no-group" data-username="EddardaaBL" data-post="1" data-topic="17590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ed8c4c/48.png" class="avatar"> EddardaaBL:</div>
<blockquote>
<p>I couldn’t visualize which file represents the segmented label in dataset for each patient, anyone have an idea, it would be a huge help for me.</p>
</blockquote>
</aside>
<p>This works well (I’ve just tested with a recent Slicer Preview Release on PROSTATEx-0141). What you have probably missed is to <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#images">install Quantitative Reporting extension to be able to load DICOM segmentation objects</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cbb85a2f84653295e2874b602f5572d9822db2c.jpeg" data-download-href="/uploads/short-url/46b8gbzK5D3l7ZHytxH5UECspIw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cbb85a2f84653295e2874b602f5572d9822db2c_2_690x419.jpeg" alt="image" data-base62-sha1="46b8gbzK5D3l7ZHytxH5UECspIw" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cbb85a2f84653295e2874b602f5572d9822db2c_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cbb85a2f84653295e2874b602f5572d9822db2c_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cbb85a2f84653295e2874b602f5572d9822db2c_2_1380x838.jpeg 2x" data-dominant-color="959390"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1372 494 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @EddardaaBL (2021-05-14 23:07 UTC)

<p>Hi<br>
Thank <a class="mention" href="/u/lassoan">@lassoan</a>  I appreciate your help<br>
finally i successfully installed 3Dslider and i could upload a sample from the dataset but about the segmented image, i mean the true label how you did it?<br>
for example in the ISBI 2013 dataset, the raw image saved in dicom files however the true mask saved in nrrd files and i could visualize both the original slice and it segmentation. but for prostatex, what’s the true mask? and how i can load it into 3d slicer and then save the both in nrrd files?<br>
another question please, how can I transfer the whole dataset from dicom to nrrd in the same instruction?<br>
looking hearing from you.</p>
<p>kind regards,</p>

---

## Post #4 by @lassoan (2021-05-15 00:26 UTC)

<p>Slicer can load images and segmentations in many formats (nrrd, nifti, DICOM segmentation object, DICOM RT structure set, …) and save in nrrd or other formats.</p>
<p>Any operation that you can do by the user interface, you can also do using Python scripting. For example: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">import from DICOM</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">save volume as nrrd</a>.</p>
<aside class="quote no-group" data-username="EddardaaBL" data-post="3" data-topic="17590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ed8c4c/48.png" class="avatar"> EddardaaBL:</div>
<blockquote>
<p>for prostatex, what’s the true mask?</p>
</blockquote>
</aside>
<p>There are 346 series in PROSTATEx but only 98 segmentations. On the TCIA website you can search for segmentations (image modality: SEG) then download all the subjects that have segmentations.</p>

---

## Post #5 by @EddardaaBL (2021-05-19 15:02 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I was looking for the segmentation mask as you said but the prostateX (or prostateX-2) data consisted of a total of 204 mpMRIs dicom images(one per patient) including the following sequences: T2-weighted (T2), diffusion-weighted (DW)<br>
with b-values b50, b400, and b800 s/mm2<br>
, apparent diffusion coefficient (ADC) map (calculated from<br>
the b-values),  with ktrans images and lession information which consists on csv files.<br>
when i convert the dicom images to nrrd using 3D slicer, i obtained 10 nrrd refers to the mpMRI. however in my task just i need the t2-MRI transversal.<br>
should i take  just the t2-tra.nrrd file ?<br>
about the masks, I took them from this repository <strong><a href="https://github.com/rcuocolo/PROSTATEx_masks" class="inline-onebox" rel="noopener nofollow ugc">GitHub - rcuocolo/PROSTATEx_masks: Lesion and prostate masks for the PROSTATEx training dataset, after a lesion-by-lesion quality check.</a></strong><br>
I will attach you image to show you what contains each dicom image, also what obtained after converting.<br>
please let me know.<br>
I appreciate your time and your help.<br>
regards,</p>

---

## Post #6 by @EddardaaBL (2021-05-19 15:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/406d9f38654f5c10b305599d85cd987f74dfebca.png" data-download-href="/uploads/short-url/9bXqapkRwVq9opRPVKq1rq4ntZ8.png?dl=1" title="Screenshot from 2021-05-19 01-15-37" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/406d9f38654f5c10b305599d85cd987f74dfebca_2_690x243.png" alt="Screenshot from 2021-05-19 01-15-37" data-base62-sha1="9bXqapkRwVq9opRPVKq1rq4ntZ8" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/406d9f38654f5c10b305599d85cd987f74dfebca_2_690x243.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/406d9f38654f5c10b305599d85cd987f74dfebca_2_1035x364.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/406d9f38654f5c10b305599d85cd987f74dfebca.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-05-19 01-15-37</span><span class="informations">1123×396 28.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c456a564e42a5d2cd4a55a254e763dc59fac483.png" data-download-href="/uploads/short-url/8BbmWfk2O2hRUSXsz02GzAgo5gf.png?dl=1" title="prostatex" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c456a564e42a5d2cd4a55a254e763dc59fac483_2_690x223.png" alt="prostatex" data-base62-sha1="8BbmWfk2O2hRUSXsz02GzAgo5gf" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c456a564e42a5d2cd4a55a254e763dc59fac483_2_690x223.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c456a564e42a5d2cd4a55a254e763dc59fac483_2_1035x334.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c456a564e42a5d2cd4a55a254e763dc59fac483.png 2x" data-dominant-color="EDEAE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">prostatex</span><span class="informations">1168×378 35.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-05-19 15:25 UTC)

<p>You are free to choose whichever sequences you find useful and ignore the rest. For example, localizers are rarely usable for anything.</p>

---

## Post #8 by @EddardaaBL (2021-05-21 14:44 UTC)

<p>I loaded the dicom images also the true mask in 3D slicer and i wanted to save the slices for each patient with the correspondent ground truth into png images, however i obtained just single png file for dicom images and a single png for the label but for dicom image the slice is blurry and for the true mask, the image is totally black, the gland does not appear there. you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51a5212a84111d33d080f1af839ee19028b16a32.png" data-download-href="/uploads/short-url/bEgsJS3Giz0GnCO8esCh5nlsFWO.png?dl=1" title="2021-05-21-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51a5212a84111d33d080f1af839ee19028b16a32_2_566x500.png" alt="2021-05-21-Scene" data-base62-sha1="bEgsJS3Giz0GnCO8esCh5nlsFWO" width="566" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51a5212a84111d33d080f1af839ee19028b16a32_2_566x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51a5212a84111d33d080f1af839ee19028b16a32.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51a5212a84111d33d080f1af839ee19028b16a32.png 2x" data-dominant-color="7E7D80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-05-21-Scene</span><span class="informations">726×641 14.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97842c7f98e3faed2b691593bc783d30db311f65.png" alt="ProstateX-0002" data-base62-sha1="lCnhj29VFjwd664kOQznmgy6uVL" width="384" height="384"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303e13fcabe95041aa5b8f0de50cc75e0fe30179.png" alt="4 t2_tse_tra" data-base62-sha1="6SLV3ptifMHyte7rq4JYjRL6LEJ" width="384" height="384"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/396007b44553b5a3ba8011efe6ae6bb6579c39c2.png" data-download-href="/uploads/short-url/8byXtIyRjB6rmPyjMOItZUYuSyu.png?dl=1" title="2021-05-21-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/396007b44553b5a3ba8011efe6ae6bb6579c39c2_2_566x500.png" alt="2021-05-21-Scene" data-base62-sha1="8byXtIyRjB6rmPyjMOItZUYuSyu" width="566" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/396007b44553b5a3ba8011efe6ae6bb6579c39c2_2_566x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/396007b44553b5a3ba8011efe6ae6bb6579c39c2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/396007b44553b5a3ba8011efe6ae6bb6579c39c2.png 2x" data-dominant-color="848386"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-05-21-Scene</span><span class="informations">726×641 89.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
can check the attached files.<br>
please let me know why?<br>
I appreciate your time. Thank you.</p>

---

## Post #9 by @EddardaaBL (2021-05-21 14:45 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303e13fcabe95041aa5b8f0de50cc75e0fe30179.png" alt="4 t2_tse_tra" data-base62-sha1="6SLV3ptifMHyte7rq4JYjRL6LEJ" width="384" height="384"></p>

---

## Post #10 by @lassoan (2021-05-21 17:18 UTC)

<p>I would not recommend to use PNG file format for storing medical images. PNG is not suitable for storing high-bit-depth 3D medical images and with essential metadata (image position, spacing, and axis directions). The deep learning tutorials that you find on the web use PNG format because they are developed for computer vision tasks (where native images are stored as PNG) or they were copied from computer vision tutorials.</p>
<p>Instead, follow <a href="https://torchio.readthedocs.io/">torchio</a> and <a href="https://monai.io/">monai</a> tutorials for learning about how to use medical images for deep learning.</p>

---

## Post #11 by @EddardaaBL (2021-05-21 18:10 UTC)

<p>Thank you again for your quick reply.<br>
I am not working with png format, i work with simpleitk, pynrrd and pydicom libraries.<br>
just i wanted to get sample of slice as png. however i tried with python script and i got the same result for label black image but the raw images are clear.</p>

---

## Post #12 by @lassoan (2021-05-21 19:03 UTC)

<blockquote>
<p>I am not working with png format,</p>
</blockquote>
<p>Great!</p>
<blockquote>
<p>just i wanted to get sample of slice as png</p>
</blockquote>
<p>If you save a 3D volume into a png file then only the very first slice is saved (you can get the slice axis from the image direction matrix).</p>
<p>The easiest way to access volume voxels in a Python script is to get the volume as a numpy array and use indexing. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates">examples in the script repository</a>.</p>
<p>You can also save the displayed slice as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-a-series-of-images-from-a-slice-view">here</a>.</p>

---
