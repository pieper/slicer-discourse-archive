# Creating ear model from image

**Topic ID**: 28599
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/creating-ear-model-from-image/28599

---

## Post #1 by @Mohan_R_ed21d021 (2023-03-27 14:03 UTC)

<p>i want to segment a ear model in the 3D Slicer. could anyone give some ideas to get the accurate ear model?</p>

---

## Post #2 by @mangotee (2023-03-27 14:52 UTC)

<p>Hi Mohan,<br>
not sure what you mean with “ear model”. In case you’re referring to the inner ear, we published a multimodal inner ear model, with templates in T1, T2 and CISS MRI, the paper can be found <a href="https://www.nature.com/articles/s41598-021-82716-0" rel="noopener nofollow ugc">here</a>. You can download all materials from our <a href="https://github.com/pydsgz/IEMap" rel="noopener nofollow ugc">repository on GitHub</a> using Git-LFS or using this <a href="https://www.dropbox.com/s/1f05i5gx8bkcyc9/IEMap_data_v_1_0.zip?dl=0" rel="noopener nofollow ugc">direct link</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa67dd951ec3e92fdcb2eb70cd8d0ec2cefb732a.jpeg" data-download-href="/uploads/short-url/zJbTHZuL2AkWgkSgF0AloZIG8Mq.jpeg?dl=1" title="IEMap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa67dd951ec3e92fdcb2eb70cd8d0ec2cefb732a_2_317x250.jpeg" alt="IEMap" data-base62-sha1="zJbTHZuL2AkWgkSgF0AloZIG8Mq" width="317" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa67dd951ec3e92fdcb2eb70cd8d0ec2cefb732a_2_317x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa67dd951ec3e92fdcb2eb70cd8d0ec2cefb732a_2_475x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa67dd951ec3e92fdcb2eb70cd8d0ec2cefb732a_2_634x500.jpeg 2x" data-dominant-color="9E9D9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IEMap</span><span class="informations">1084×854 90.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To segment the inner ear, you need to use deformable registration to register the template (single- or multi-contrast) to your subject’s inner ear. You can use Slicer tools like SlicerAnts or Elastix Toolbox to achieve this.</p>

---

## Post #4 by @Mohan_R_ed21d021 (2023-03-28 07:45 UTC)

<p>i want to create ear model with ear canal and outer ear (skin and cartilage ) from MRI data. could anyone guide me?</p>

---

## Post #5 by @Mohan_R_ed21d021 (2023-03-28 07:47 UTC)

<p>only i need external ear with canal part. is it possible from MRI data?. if you know , just give me the guidance.</p>

---

## Post #6 by @mangotee (2023-03-28 07:59 UTC)

<p>I think that’s possible, also for the external ear with canal part. The simplest way is to take one subject’s MRI and annotate that to create a single-subject atlas.</p>
<p>A more representative (i.e. less biased) model can be created by building an average ear template from a few subjects, and annotating that into a multi-subject atlas.<br>
To create that, you need high-quality (i.e. high-resolution) MRI images from a few subjects. The way I approached this is to create a custom template using <a href="https://stnava.github.io/ANTs/" rel="noopener nofollow ugc">ANTs</a> and their great template building tools. A concrete example is given <a href="https://ntustison.github.io/TemplateBuildingExample/" rel="noopener nofollow ugc">here</a>. It even works for multimodal MRI (as in our inner ear case)!<br>
You can either register the full heads and create a bilateral template, or you can create crops of left/right ear regions and horizontally flip all left ears onto the right ears and create a unilateral template. This way, you double your input data (left vs right anatomy is symmetric but not identical, there’s still small variation to learn from). For a full description of the unilateral procedure, you can check our publication for the inner ear, the workflow would be almost identical. The bilateral (full-head) procedure is much simpler even.</p>
<p>A heads-up though… the outer ear (incl. the full auricle) must be visible for all subjects, with a bit of air margin in the FOV to allow for registration, otherwise you can get partial registrations and noise in the template. This was the case for our data. The outer ear was not of interest to us, but I noticed that the template reconstruction was quite noisy for the auricle (i.e. ghost images overlaid onto each other), because there’s so much variation across subjects. It will need some tweaking to get all subjects’ ears aligned properly.</p>

---

## Post #7 by @Mohan_R_ed21d021 (2023-03-28 08:19 UTC)

<p>Thank you , I will try that.</p>

---

## Post #8 by @Mohan_R_ed21d021 (2023-04-04 17:36 UTC)

<p>i want to know about  what is single subject atlas. and  could give some detailed procedure to import data and segmentation?</p>

---
