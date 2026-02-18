# DTI Brain Mask Including Non-Brain Tissue

**Topic ID**: 6578
**Date**: 2019-04-23
**URL**: https://discourse.slicer.org/t/dti-brain-mask-including-non-brain-tissue/6578

---

## Post #1 by @MSpindler (2019-04-23 14:52 UTC)

<p>Dear Slicer community,</p>
<p>I’m using slicer 4.10.1.<br>
I first converted my nii.gz DWI file to .nrrd using DWIConvert. After that, I create a brain mask using “Diffusion Brain Masking”. But the resulting mask includes a lot of non-brain tissue (skull, soft tissue). My b-values are 0 and 1000, changing the b-value threshold doesnt help. How can I approach this?</p>
<p>Cheers<br>
Melanie</p>

---

## Post #2 by @ljod (2019-04-23 16:05 UTC)

<p>If you can share a screenshot that can help us see if the brain mask is as expected or not. Is your data working correctly otherwise? Can you estimate tensors and perform tractography? The main use of the brain mask is often for tractography such as UKF, which also uses thresholds to stop tractography. Is that how you plan to use the brain mask?</p>

---

## Post #3 by @MSpindler (2019-04-23 16:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/218677a4f4f3b9a5bf8b8f2825481bac86b06e7b.png" data-download-href="/uploads/short-url/4MzQNefUoKFuvnIOJxKCrl7SJRh.png?dl=1" title="3dslicer_brainmask" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/218677a4f4f3b9a5bf8b8f2825481bac86b06e7b_2_690x482.png" alt="3dslicer_brainmask" data-base62-sha1="4MzQNefUoKFuvnIOJxKCrl7SJRh" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/218677a4f4f3b9a5bf8b8f2825481bac86b06e7b_2_690x482.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/218677a4f4f3b9a5bf8b8f2825481bac86b06e7b_2_1035x723.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/218677a4f4f3b9a5bf8b8f2825481bac86b06e7b.png 2x" data-dominant-color="3F4F68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer_brainmask</span><span class="informations">1146×802 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks for the fast response <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
This is the brain mask. The tensor estimation works, the FA and V1 maps look also reasonable. It just calculates these parameters for non-brain voxels as well. (looks similar for many subjects)<br>
For now, I dont want to do tractography, but maybe later. At first, I want to register the DTI image to a T1 image, for which I need the brainmask. Then I want to do a segmentation using the T1 image with help of the diffusion directions.</p>

---

## Post #4 by @ljod (2019-04-23 17:41 UTC)

<p>I agree with you that this does not look as expected. Have you tried fiddling with any parameters in an “advanced” or similar section of the module?</p>

---

## Post #5 by @MSpindler (2019-04-24 06:30 UTC)

<p>Which advanced settings do you mean? This is what the module looks like to me: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43d967b51ceaca5c8b8c7cd2c4cdd2b03c6d99c8.png" alt="Unbenannt" data-base62-sha1="9GdMhLg072iOAkJDpHLYkgG97Cw" width="462" height="186"></p>

---

## Post #6 by @ljod (2019-04-24 09:38 UTC)

<p>Thanks. I had thought I remembered something else. One more question. How does the output baseline image look? The method is using this image to compute the mask. If it is very noisy or has some issue, that could lead a mask issue.</p>

---

## Post #7 by @MSpindler (2019-04-24 11:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f702651bbe6c3402c1ca65da3e56a067fa809da5.png" data-download-href="/uploads/short-url/zf9477dOlAHqMBhkvRwIVs2oFwx.png?dl=1" title="baselinevolume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f702651bbe6c3402c1ca65da3e56a067fa809da5_2_517x266.png" alt="baselinevolume" data-base62-sha1="zf9477dOlAHqMBhkvRwIVs2oFwx" width="517" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f702651bbe6c3402c1ca65da3e56a067fa809da5_2_517x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f702651bbe6c3402c1ca65da3e56a067fa809da5_2_775x399.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f702651bbe6c3402c1ca65da3e56a067fa809da5_2_1034x532.png 2x" data-dominant-color="44454F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">baselinevolume</span><span class="informations">1245×641 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the baseline volume. The surrounding tissue is displayed quite bright, the original data (b0) looks like this as well. I dont know if this might be the reason. I tried it once with motion and eddy current corrected dwi images from FSL, and once with the raw data, both create the same brainmask.</p>
<p>I also tried using the brain mask generated by FSL for the tensor estimation. But this results in an error due to a wrong coordinate space (the nii.gz dwi image is shifted when imported to .nrrd in DWIConvert, so that the transformation matrices dont match anymore).  If you know a way how I can use this other brainmask, that would be fine as well.</p>

---

## Post #8 by @ljod (2019-04-24 12:13 UTC)

<p>It’s possible the mask process is challenged by the bright spots in the skull/scalp area. First try to read your mask using regular Slicer loading instead of dwiconvert. If that doesn’t help, in the slicer nightly version we have a new dcm2nii module available through the extension manager. If you are able to download the nightly and try this module (intended to replace dwiconvert) it may function better. Please keep us posted on your progress with this.</p>

---

## Post #9 by @MSpindler (2019-04-24 12:28 UTC)

<p>I loaded the FSL mask regularly anyway, DWIconvert only works for the “real” dwi image. For masks, eigenvectoror or fractional anisotropy maps, the import produces an error. So the dwi image is shifted during import, not the mask. (but I have to use the import for the data because the FSL data is otherwise not recognized as DTI format). I’ll try the nightly version, and will keep you posted, thank you!<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @ljod (2019-04-24 12:42 UTC)

<p>Great thank you for keeping us posted. Note that today’s nightly may not have all extensions available due to internal upload issues (we are migrating to a better server soon I think):<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview</a></p>

---

## Post #11 by @MSpindler (2019-04-26 11:20 UTC)

<p>I downloaded the nightly version from the website (18.04), but I cant find the extension dcm2nii. Is this the extension name or is it a module within an extension, or did I download the wrong nightly <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20">?</p>

---

## Post #12 by @ljod (2019-04-26 11:44 UTC)

<p>You did it right. This webpage shows the status of the nightly builds<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview</a></p>
<p>On Mac there is an upload error due to internal server problems the team is working on. On Windows there is a new build issue.  It seems Linux has not built yet, so later this morning. What operating system are you using?</p>

---

## Post #13 by @MSpindler (2019-04-26 12:21 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4de9525343fb2633e774de2b753cf515cbc93b5d.png" alt="grafik" data-base62-sha1="b7eEzypeRlyykyXKf0BP7RT5ME5" width="421" height="249"> I’m using Windows, but it says that the latest one is 18.04.</p>

---

## Post #14 by @ljod (2019-04-26 12:42 UTC)

<p>Most likely dcm2nii was not available then. We just fixed build issues but apparently there is a new one on Windows now.</p>
<p>If you’d just like to test the conversion you can try to run dcm2niix outside of slicer. The most recent version of this software can output nrrd/nhdr format.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rordenlab/dcm2niix">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/rordenlab/dcm2niix" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/46842b10e071e0ec8ffeccfaf92ef38c3a8653b3ef0d41dc6c3a1ae56d2b9274/rordenlab/dcm2niix" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rordenlab/dcm2niix" target="_blank" rel="noopener nofollow ugc">GitHub - rordenlab/dcm2niix: dcm2nii DICOM to NIfTI converter: compiled...</a></h3>

  <p>dcm2nii DICOM to NIfTI converter: compiled versions available from NITRC - GitHub - rordenlab/dcm2niix: dcm2nii DICOM to NIfTI converter: compiled versions available from NITRC</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or you can wait a few days and check back. Or you can try eroding and dilating the brain mask you have and some manual editing.</p>
<p>What is your use case/goal and time frame?</p>

---

## Post #15 by @MSpindler (2019-04-29 07:40 UTC)

<p>Hey!<br>
I converted the DICOMS to .nrrd format using dcm2niix. I used the flag -z with different n/3/y/i because I didnt know if slicer would be able to read zipped files. (if I convert to compressed files I get a .raw.gz, and a .nhdr file; if I convert to non-compressed file, I get a .nrrd, without .nhdr).<br>
Slicer does not recognize the .raw.gz file, so I used the un-compressed .nrrd.<br>
If I load that, it looks like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/569d0bb8eaa03fe0d5b2c5bc88feccb30016ce03.png" alt="grafik" data-base62-sha1="cmdwX8lMJXwC3emUxk1Siowf3ZF" width="320" height="232"><br>
The T1 image looks similar. Do you know what I did wrong here?<br>
command: dcm2niix -e y -z n dicompath</p>
<p>I’m a PhD student and want to work on segmentations of the hypothalamus in tumor patients, for which I also want to use the diffusion vectors. The goal at the moment is to align the T2 and diffusion image to the T1, then I can start with the segmentations (I would like to start the segmentations at some time during the next month).</p>

---

## Post #16 by @MSpindler (2019-04-29 11:44 UTC)

<p>Ohh, sorry. I found my mistake. I now used the raw.gz and .nhdr files converted with dcm2niix, which produce correct images. Still, the resulting brain mask looks like the one I had previously (including skull and eyes etc.).</p>

---

## Post #17 by @ljod (2019-04-29 13:18 UTC)

<p>Hi try converting your good mask using dcm2nii. I think that was the goal, to import both using the same pipeline, to see if they align. However it’s possible you need to use image registration (for example T2 to baseline from dMRI) then apply that transform to the mask, then resample. I don’t know if the mask started out aligned to the dMRI or not. So whether it’s a conversion or registration issue is not yet clear to me. Let us know how this goes.</p>

---

## Post #18 by @MSpindler (2019-04-30 08:55 UTC)

<p>Hmm, I’m not sure what you mean. The “good” mask was created with FSL, is therefore in .nii.gz format.<br>
I dont think I can convert .nii.gz files to .nrrd with dcm2nii, but only DICOM to .nrrd. The .nii.gz files are aligned, but after converting the data to .nrrd, the mask doesnt fit anymore. I now checked whether registration of DTI and T1 works with the baseline image that I got, and this seems alright. So I can do the segmentation anyways <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>But to get rid of signal outside the brain for tractography, maybe I could use my T1 image (it’s skullstripped) as mask? I would have to mask the DTI tensor image (cant use the Diffusion Brain Masking-Module because the DWI data is not registered to the T1, only to the DTI data and the DWI baseline image).<br>
Is something like this possible?</p>

---

## Post #19 by @ljod (2019-04-30 11:56 UTC)

<p>You can use any mask if it’s exactly registered to the baseline and has the exact same voxel dimensions.  This requires registration then resampling. Try googling resample 3DSlicer and searching this forum/tutorials for more information on exact steps. For resampling you want nearest neighbor since it’s a mask volume (don’t want to average neighboring voxels).</p>

---

## Post #20 by @MSpindler (2019-04-30 13:38 UTC)

<p>Sorry, I think I’m confused now…<img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<ol>
<li>I created a baseline volume using Diffusion Brain Masking</li>
<li>I created the tensor data using the baseline volume (over the whole image, not restricted to the brain)</li>
<li>I registered the DTI image and Baseline image to the structural (T1) image using General Registration and Resample DTI Volume.</li>
<li>I created a mask from the T1 image (after registration, because only then it matches the baseline image)</li>
</ol>
<p>Now I want to apply this mask to the DTI.</p>
<p>What I tried:<br>
I cannot use a mask created with the baseline image (neither in Diffusion Brain Masking, nor in Segment Editor), since this includes nonbrain tissue (probably brightness issue).<br>
What I could do is to manually edit the baseline-mask in the segment editor slice by slice until only brain is left, to put that into Diffusion Brain Masking before Tensor estimation. But I would have to do this for 70 subjects, and I wont do that because it’s incredibly time consuming.</p>
<p>I can also not register the DWI data to the T1 image before tensor estimation to be able to use the T1 mask “regularly” within Diffusion Brain Masking.<br>
(at least not using General Registration + Resample DTI volume/Resample Scalar/Vector/DWI, because the Registration step does not allow DWI).</p>
<p>So my questions are:<br>
Is there either<br>
a way to delete values in the <strong>DTI volume</strong> outside of a mask <strong>after tensor estimation</strong>?<br>
or<br>
a module for registering the <strong>DWI volume</strong> to the T1 image <strong>before Diffusion Brain Masking</strong>?</p>
<p>I couldnt find anything about that in the forum or on the website. Maybe it’s obvious and I just dont get it.<img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #21 by @ljod (2019-04-30 13:56 UTC)

<p>Hi. For best tractography, do not register or resample the DWI/DTI. Instead do tractography first in the original data and then you can apply a registration matrix to the tractography if you want it in T1 space.</p>
<p>So for masking, 1) register T1 to baseline. Then 2) apply this transform to the mask that was in T1 space. Then 3) resample the mask to be the same as the baseline.</p>
<p>You don’t ever need to register DWI. baseline image is in DWI coordinate system. So register T1 and mask to baseline and they are registered to DWI as well.</p>

---

## Post #22 by @MSpindler (2019-04-30 14:10 UTC)

<p>I dont want to register T1 to DWI, but DWI to T1. The T1 is in AC-PC orientation, and I want to keep that for the segmentation.<br>
But for tractography that is not necessary I guess.</p>
<p>Basically I need two “pipelines” then?:<br>
Use the procedure I have for the segmentation (processed with “ugly” mask, resampled, AC-PC orientation), and for tractography: reorient the segmentations to DWI space for use as seeds (good mask, original data)?</p>

---

## Post #23 by @ljod (2019-04-30 14:38 UTC)

<p>sure. just do tractography in DWI space then afterwards you can transform it into any space you prefer. it’s best to avoid interpolation of DWI before tractography if at all possible. No need to modify the data before tractography unless you want to average multiple subjects DWIs or something like that.</p>
<p>you can transform any other data into DWI space for doing tractography. Though the preferred most robust way is to seed in the whole brain mask, then later select the tracts you are interested in. So you could transform the tractography into the space where your segmentations are and use them to select tracts, if that is your goal.</p>
<p>If your goal is to do manual segmentation of the hypothalamus in a standard coordinate system, then yes you would want to register the DWI into that coordinate system and resample. That makes sense for that use case.</p>
<p>Furthermore, if in the paper you will explain this logical reason for resampling the DWI, the reviewers may not complain that you performed tractography after resampling. Just in general this is not something ideal to do.</p>

---

## Post #24 by @MSpindler (2019-05-01 09:18 UTC)

<p>Thank you very much, that helps a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #25 by @MSpindler (2019-05-20 08:55 UTC)

<p>Hey!</p>
<p>I found that during “Resample DTI”, the voxel size of the output volume is changed to the voxel size of the “Reference Volume”.<br>
Of course I want to have the same orientation as the reference volume, but not the same voxel size, since my reference volume (T1) has a voxel size of 1x1x1, and the DTI a voxel size of 2.2x2.2x2.3.<br>
If I put no reference volume, the initial orientation is of course no longer approriate and a posterior part of the brain is cut off.<br>
The same happens in “General Registration (BRAINS)”. The output baseline image volume is no longer 2x…, but 1x… Otherwise I would use the registered baseline image as reference volume.<br>
(I followed the steps of the tutorial slides for this procedure).</p>
<p>Why would you want to change the dimensions of the image during registration, and is there a way I can prevent that?</p>

---

## Post #26 by @ljod (2019-05-20 10:02 UTC)

<p>Hi the goal of resampling is always to put an image into the exact coordinate system of another.</p>
<p>If you want a different reference coordinate system you can use a different reference image.</p>
<p>Or, depending on your use case or goal, you can just view the data after registration but without resampling. In Slicer the registration is applied only for visualization without changing the data in this way.</p>
<p>What is your goal here??</p>

---

## Post #27 by @MSpindler (2019-05-20 10:12 UTC)

<p>Thanks for the answer!<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I now used the option “Manual Output Parameters” in “Resample DTI Volume” with:<br>
Spacing: of DTI<br>
Size: of DTI<br>
Origin: None<br>
Direction Matrix: of T1<br>
For registering the DTI to the T1, I used the procedure from the Wiki. Create Baseline → General Registration → Resampling DTI.  As far as I understood, there is no way in 3DSlicer to register the DTI to the T1 without “Resample DTI”, even though I dont want to resample. Or what do you mean by “view the data after registration without resampling”?</p>

---

## Post #28 by @MSpindler (2019-05-20 10:22 UTC)

<p>I think I dont understand the general purpose of changing e.g. the voxel size to the voxel size of another image, and I dont think that it should be done in most cases (for example when coregistering functional to structural MRIs, you dont want to change the voxel size of the functionals). The coordinate system should be correct, yes, in order to get the correct positions, but why the voxel sizes?</p>

---

## Post #29 by @ljod (2019-05-20 13:58 UTC)

<p>Hi that is just the definition of resampling.</p>
<p>You don’t need to resample. Why did you choose to resample?</p>
<p>The images should have been already registered before you resampled, right?</p>

---

## Post #30 by @MSpindler (2019-05-20 14:11 UTC)

<p>This is what I did:<br>
<a href="https://www.slicer.org/wiki/Documentation:Nightly:Registration:RegistrationLibrary:RegLib_C03" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation:Nightly:Registration:RegistrationLibrary:RegLib_C03</a></p>
<p>“<strong>Resample DTI:</strong> We have now computed the registration transform, but the output volume produced above is a registered version of the baseline, which we need for validation only. To get the actual DTI registered we now apply this transform to the tensor image.”<br>
This module is needed for registering DTI to T1. In no other module, I can use the DTI as input for registration.</p>
<p>My overall goal is to coregister/align multiple images with the T1 image, without changing all properties of these images to the properties of the T1, only the alignment. If not necessary, I dont want to resample at all. For example in SPM, you just use the “Coregistration”-Tab for that. You can either reslice or not reslice that (write a new image).</p>

---

## Post #31 by @ljod (2019-05-20 14:49 UTC)

<p>Definitely don’t resample. You should be able to apply the transform to the DWI or DTI in the Transforms module.</p>

---

## Post #32 by @MSpindler (2019-05-22 10:26 UTC)

<p>Ahh, i did not try that with the DWI… For the DTI, it crashes the program, that’s why I didnt do it.<br>
But with the DWI it works totally fine, thanks!</p>

---

## Post #33 by @ljod (2019-05-22 11:17 UTC)

<p>Please give exact details of how the crash can be reproduced. What exactly did you do and exactly what happened?</p>
<p>Thanks!</p>

---

## Post #34 by @ljod (2019-05-27 10:58 UTC)

<p>More information for you: the masking works correctly in the release version (4.10.2).</p>

---
