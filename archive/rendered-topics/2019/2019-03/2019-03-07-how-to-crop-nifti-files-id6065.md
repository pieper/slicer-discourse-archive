# How to crop nifti files

**Topic ID**: 6065
**Date**: 2019-03-07
**URL**: https://discourse.slicer.org/t/how-to-crop-nifti-files/6065

---

## Post #1 by @rjortiz2 (2019-03-07 20:59 UTC)

<p>I know this may be a simple solution, but how does one crop a nifti file of a brain? I am trying to remove the skull and I’ve been stuck at this issue for quite some time. I have used segmentation wizard (or segmentation) module to highlight the regions I don’t want cropped, but cannot seem to figure out what module to use to actually cropt the rest out. I really appreciate all of the help!</p>

---

## Post #2 by @muratmaga (2019-03-07 21:49 UTC)

<p>If you already done the segmentations of the regions that you want to remove, install the Segment Editor Extra Effects extension and use mask volume function to save a version of your volume with just the brain. Then you can use the Crop Volume if you still want to remove the empty background.</p>

---

## Post #3 by @lassoan (2019-03-07 21:51 UTC)

<p>If you need to remove the skull from MRI images, then you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper" rel="nofollow noopener">SwissSkullStripper</a> extension. It removes the skull from the image completely automatically.</p>

---

## Post #4 by @rjortiz2 (2019-03-07 21:56 UTC)

<p>I forgot to mention that I am using rodent images, and SwissSkullStripper is probably human-based, correct?</p>

---

## Post #5 by @rjortiz2 (2019-03-07 22:11 UTC)

<p>Will the outcome of this process still be in nifti? Your method was great for cropping out the desired stuff, but I cannot seem to save it back as a nifti file again.</p>

---

## Post #6 by @lassoan (2019-03-07 23:06 UTC)

<p>The skull stripper should work for any species, just provide your own template (a single image volume and a corresponding brain segmentation).</p>
<p>The result can be save in many formats, including nifti (you can choose file format in the save dialog).</p>

---

## Post #7 by @muratmaga (2019-03-07 23:08 UTC)

<p>You can save the masked volume in any format slicer supports (including Nifti). Just use the save as dialog box.</p>

---

## Post #8 by @rjortiz2 (2019-03-12 19:25 UTC)

<p>Update:</p>
<p>These files are multi-volume nifti and I am attaching a dropbox link of an example of my data.</p>
<p>So far, my steps include</p>
<p>1- MultiVolume Importer–&gt;Select folder where .nii file in–&gt;output node–&gt;create new MRML MultiVolume–&gt;click Import (Output node becomes a 200 frames NIfTI MultiVolume)<br>
2. MultiVolume Explorer Module–&gt;select input multivolume as 200 frames NIfTI MultiVolume (can click play)<br>
3. Segment editor module w/ segment editor extra effects add-on installed–&gt;segment portion I want<br>
4. Mask Volume (within segment editor)–&gt;save new dataset with only segmented region<br>
5. Crop volume module–&gt;apply (I am able to visualize the masked, cropped image exclusively.</p>
<p><strong>The problem occurs because I cannot save the masked cropped image into a .nii file, as the only options are .nrrd or .nhdr format.</strong></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/6hhoo3u3bvlx9lx/KSIL_17_litter_20_male_1_1_Scan26_Reco1.nii?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/6hhoo3u3bvlx9lx/KSIL_17_litter_20_male_1_1_Scan26_Reco1.nii?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/6hhoo3u3bvlx9lx/KSIL_17_litter_20_male_1_1_Scan26_Reco1.nii?dl=0" target="_blank" rel="noopener nofollow ugc">KSIL_17_litter_20_male_1_1_Scan26_Reco1.nii</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @fedorov (2019-03-12 20:48 UTC)

<p>If you need to export multivolume as a .nii file, that functionality is not available. You can only save multivolumes as .nhdr/.nrrd.</p>

---

## Post #10 by @Tim_othy (2021-11-17 15:00 UTC)

<p>Try the brain extraction tool in FSL?</p>
<p>Or FreeSurfer?</p>

---
