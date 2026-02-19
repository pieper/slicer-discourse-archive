---
topic_id: 23094
title: "Saved Dicom To Nii With Savenode Changes Range Of Intensitie"
date: 2022-04-23
url: https://discourse.slicer.org/t/23094
---

# Saved dicom to nii with saveNode, changes range of intensities and image volume

**Topic ID**: 23094
**Date**: 2022-04-23
**URL**: https://discourse.slicer.org/t/saved-dicom-to-nii-with-savenode-changes-range-of-intensities-and-image-volume/23094

---

## Post #1 by @S_Arbabi (2022-04-23 09:14 UTC)

<p>Hi,<br>
I load a dicom series and save it as nrrd like this:</p>
<pre><code class="lang-auto">img_node = DiskSimulator.load_image(img_dcm_dir, iid)
slicer.util.saveNode(img_node, os.path.join(self.imgs_nii_dir, iid, f"{iid}.nii.gz"))
</code></pre>
<p>where load_image method is defined as bellow:</p>
<pre><code class="lang-auto">def load_image(img_dicom_path, img_node_name):
      originalDicomPlugins = slicer.modules.dicomPlugins
      slicer.modules.dicomPlugins = {'DICOMScalarVolumePlugin': originalDicomPlugins['DICOMScalarVolumePlugin']}
      loadedNodeIDs = []
      with DICOMUtils.TemporaryDICOMDatabase() as db:
          DICOMUtils.importDicom(img_dicom_path, db)
          patientUIDs = db.patients()
          for patientUID in patientUIDs:
              loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
      volumeNode = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[0])
      volumeNode.SetName(img_node_name)
      slicer.modules.dicomPlugins = originalDicomPlugins
      slicer.app.applicationLogic().GetInteractionNode().SetCurrentInteractionMode(slicer.vtkMRMLInteractionNode.AdjustWindowLevel)
      return volumeNode
</code></pre>
<p>but when I open dicom image and nii image I see the intensity ranges and volume has some differences.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6c5c0c98bd12c3d0ed574022aa4692b7cf466b9.jpeg" data-download-href="/uploads/short-url/nNkWx8wSUQEWLwuhArDJZPZ5iqt.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6c5c0c98bd12c3d0ed574022aa4692b7cf466b9_2_690x322.jpeg" alt="Capture2" data-base62-sha1="nNkWx8wSUQEWLwuhArDJZPZ5iqt" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6c5c0c98bd12c3d0ed574022aa4692b7cf466b9_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6c5c0c98bd12c3d0ed574022aa4692b7cf466b9_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6c5c0c98bd12c3d0ed574022aa4692b7cf466b9_2_1380x644.jpeg 2x" data-dominant-color="4F4F4F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1920×897 78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here I attach a more detailed statistics of the two images loaded in MevisLab:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c89c00c19792f44d34cf1649d129ca60f23a20b.jpeg" data-download-href="/uploads/short-url/dcD3s4Fg6AgCCUWEPMgUZNO9TSz.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c89c00c19792f44d34cf1649d129ca60f23a20b_2_690x268.jpeg" alt="Capture" data-base62-sha1="dcD3s4Fg6AgCCUWEPMgUZNO9TSz" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c89c00c19792f44d34cf1649d129ca60f23a20b_2_690x268.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c89c00c19792f44d34cf1649d129ca60f23a20b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c89c00c19792f44d34cf1649d129ca60f23a20b.jpeg 2x" data-dominant-color="E6E6E6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">998×388 53.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I was wondering where the difference comes from? and how can I make them the same.</p>
<ul>
<li>I see the nii image is saved as integer data while dicom serie has been unsigned integer data</li>
<li>Especially in the side by side view it seems like even they are not registered, as they show different views in the same slice</li>
</ul>
<p>Best regards,<br>
Saeed</p>

---

## Post #2 by @lassoan (2022-04-25 04:20 UTC)

<p>You have only saved the first loaded node (<code>loadedNodeIDs[0]</code>) of the first patient in the database. Probably it was a different image than what you loaded manually. You can save all the loaded nodes (instead of just the first one) and then you’ll probably find the corresponding volumes.</p>

---

## Post #3 by @S_Arbabi (2022-04-28 12:45 UTC)

<p>Thanks Andras, I believe that’s not the case, since I printed the length of loadedNodeIDs, it just has one element in it, which is what I saved.<br>
So I checked with exporting the loaded DICOM node in slicer UI by right clicking and “export to DICOM”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c20c175788099b35ca426568e158fc3cbc4929.png" data-download-href="/uploads/short-url/l57VOgvEr2phhtL0LmYia8xSXi1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c20c175788099b35ca426568e158fc3cbc4929.png" alt="image" data-base62-sha1="l57VOgvEr2phhtL0LmYia8xSXi1" width="535" height="499" data-dominant-color="F1F2F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">663×619 23.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when I check the exported DICOM serie with the input DICOM serie, the image data is different. I think the reason should lie in “export type” (above screenshot)? that’s the only place I see can make difference.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca0fafbee5ab6d8f86ce813f761f356b7733685a.png" data-download-href="/uploads/short-url/sPw3xWcBSC7AJTpuF3fy3aFbtpw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca0fafbee5ab6d8f86ce813f761f356b7733685a.png" alt="image" data-base62-sha1="sPw3xWcBSC7AJTpuF3fy3aFbtpw" width="690" height="216" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">983×309 9.42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>these are statistics of loaded DICOM serie and exported DICOM serie. I’m wondering what’s makes the difference? how can I avoid it?</p>

---

## Post #4 by @lassoan (2022-04-28 17:11 UTC)

<p>You created a new topic for this, so let’s stop the discussion here and continue it there:</p>
<aside class="quote quote-modified" data-post="1" data-topic="23173">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/dfb087/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/saving-dicom-to-dicom-the-exported-and-input-do-not-match/23173">Saving dicom to dicom, the exported and input do not match</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I can’t understand this, can someone explain a bit? 
I open a dicom serie: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effb6222185706eb1d0a6fa8e7096c2cdad25488.jpeg" data-download-href="/uploads/short-url/yeYHvvcgzCjyIPqP4ADC2U02O9y.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
then I right click on it and choose export to DICOM: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734991ddc7a808a1917f777c28a195b451ab6779.jpeg" data-download-href="/uploads/short-url/grSwXFct84MkObHOY4l1wJmIN3r.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
and simply hitting export: 
[image] 
what I expect is that the input and exported DICOM should be the same in image voxel data at least (DICOM tags can differ, that’s fine). 
BUT, it’s not the case! here, some statistics of the two DICOMs: 
[image] 
Thanks in advance, 
Saeed
  </blockquote>
</aside>


---
