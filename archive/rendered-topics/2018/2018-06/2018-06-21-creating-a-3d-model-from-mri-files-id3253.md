---
topic_id: 3253
title: "Creating A 3D Model From Mri Files"
date: 2018-06-21
url: https://discourse.slicer.org/t/3253
---

# Creating a 3d model from MRI files

**Topic ID**: 3253
**Date**: 2018-06-21
**URL**: https://discourse.slicer.org/t/creating-a-3d-model-from-mri-files/3253

---

## Post #1 by @Sythic (2018-06-21 00:12 UTC)

<p>Hi all, a friend of mine was in an accident that caused her height loss in one of her vertebrae. Her birthday is coming up so I thought it’d be fun to giver her a 3D print of her broken spine. I have her MRIs and watched a few 3D Slicer tutorials but my files dont seem to be working right.</p>
<p>It looks like it imported everything to the DB correctly but the views look weird. Theres 1 view that looks fine and then the top and right side view are only thin blurry strips. (It said there were errors to see in advanced view?) Also most tutorials seem to be using CT files that have an obvious contrast for the bones but the MRI files I have dont seem to have the same thing. Is there anything I can do with this?</p>
            <div class="onebox imgur-album">
              <a href="https://imgur.com/a/ALscKVX" target="_blank" rel="noopener nofollow ugc">
                <span class="outer-box" style="width:600px">
                  <span class="inner-box">
                    <span class="album-title">[Album] imgur.com</span>
                  </span>
                </span>
                <img src="https://i.imgur.com/f0LNPJt.png?fb" title="imgur.com" height="315" width="600">
              </a>
            </div>

<p>Thanks for any help!</p>

---

## Post #2 by @pieper (2018-06-21 18:11 UTC)

<p>When MRs are acquired they often save time by acquiring anisotropic data.  There’s some more description and some suggestions here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>


---

## Post #3 by @mttctr (2018-06-21 18:38 UTC)

<p>Hey Sythic, what you have there looks like a 2mm slice CT scan. I’ve created spinal models from what you have before. Using mainly the sagittal view (yellow) that you have and the FastGrowCutEffect add-on. the DICOM has been generated from the sagittal view, so it has a high resolution, but every 2mm. This means you have voxels that are rectangular. Take you time with FastGrowCutEffect to teach it the anatomy you want. You could try just thresholding but I’ve found those models take longer to clean up. Once you have exposed your stl model, import to MeshMixer and remove all the geometry that looks undesirable, spikes and voids. Remove any internal geometry of the model that you don’t need, then smooth the entire model to remove the CT slice lines. For your gift purpose this will look great.</p>
<p>Regards, Matt</p>

---

## Post #4 by @lassoan (2018-06-21 18:54 UTC)

<p>Note that since Slicer-4.8, Segment editor module should be used for segmentation instead of the old Editor module. Segment editor module has fundamental changes, many improvements and fixes. It has a completely reworked, much faster and easier-to-use grow-cut effect: <em>Grow from seeds</em> effect. It also has <em>Smoothing</em> effect with several options to make surfaces smoother; and <em>Scissors</em> and <em>Islands</em> effect to remove irrelevant parts of the segmentation.</p>

---

## Post #5 by @Sythic (2018-06-22 02:08 UTC)

<p>Hey guys, thanks for the great tips. I actually got another disc of a much higher res MRI/CT she did which had like 500 layers and the bones were properly contrasted. It’s not perfect but pretty happy with how it came out without any tedious rotoscoping each layer.</p>
            <div class="onebox imgur-album">
              <a href="https://imgur.com/a/15G16fg" target="_blank" rel="noopener nofollow ugc">
                <span class="outer-box" style="width:600px">
                  <span class="inner-box">
                    <span class="album-title">[Album] imgur.com</span>
                  </span>
                </span>
                <img src="https://i.imgur.com/3HHKvCo.jpeg?fb" title="imgur.com" height="315" width="600">
              </a>
            </div>


---

## Post #6 by @jongress (2024-03-28 23:28 UTC)

<p>Hello everyone! Thank you all for a great forum and resource! It’s been amazingly helpful.</p>
<p>Does anyone know of any video tutorial examples of working with this type of “1 hi-res image + 2 strips” scenario?</p>

---

## Post #7 by @lassoan (2024-03-29 00:49 UTC)

<p>There is nothing special about segmenting a handful of slices that cover a narrow region. You can use the Segment Editor as usual.</p>
<p>What would you like to segment on what kind of images?</p>

---

## Post #8 by @jongress (2024-04-08 06:10 UTC)

<p>Thank you for the reply!  I’ve successfully reconstructed a small segment. But this MRI file contains just one good resolution transverse slice and then two long narrow strips that aren’t full regular slice images. I’m trying to isolate, then export a spine model as above. Do you know of any videos walking through this procedure?</p>

---
