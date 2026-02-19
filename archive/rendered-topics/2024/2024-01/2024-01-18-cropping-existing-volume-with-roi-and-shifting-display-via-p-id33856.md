---
topic_id: 33856
title: "Cropping Existing Volume With Roi And Shifting Display Via P"
date: 2024-01-18
url: https://discourse.slicer.org/t/33856
---

# Cropping existing volume with ROI and shifting display via Python scripting

**Topic ID**: 33856
**Date**: 2024-01-18
**URL**: https://discourse.slicer.org/t/cropping-existing-volume-with-roi-and-shifting-display-via-python-scripting/33856

---

## Post #1 by @paleomariomm (2024-01-18 15:51 UTC)

<p>Hi community. I am writing a Python script to automate a pipeline that will be used in around 1000 CT scans.</p>
<p>Now I am able to load 1 DICOM folder and to display Volume rendering with Python</p>
<pre><code class="lang-auto"># Load DICOM files
  # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom
dicomDataDir = "C:/Users/mario.modesto/Desktop/DICOM/W111"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

# Display volume rendering
# https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering
logic = slicer.modules.volumerendering.logic()
volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(logic)
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
</code></pre>
<p>However, I would like to know, in my progress, two things I am struggling right now. When volume rendering is shown, it is almost all black.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65b56a7a43af2e5eed27b07fbfdce5733ab6be86.jpeg" data-download-href="/uploads/short-url/evKUc0hx7GjuldpeXiWrSwtAuCG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65b56a7a43af2e5eed27b07fbfdce5733ab6be86_2_690x319.jpeg" alt="image" data-base62-sha1="evKUc0hx7GjuldpeXiWrSwtAuCG" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65b56a7a43af2e5eed27b07fbfdce5733ab6be86_2_690x319.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65b56a7a43af2e5eed27b07fbfdce5733ab6be86_2_1035x478.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65b56a7a43af2e5eed27b07fbfdce5733ab6be86_2_1380x638.jpeg 2x" data-dominant-color="818296"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×888 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Therefore, I need to move to right the Shift option in Display to show the skull.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb90cda2883b759ad7acc34952f212552a9dbdb4.jpeg" data-download-href="/uploads/short-url/xBUrB0F3SJZHtMpEDH1FimhvtAM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb90cda2883b759ad7acc34952f212552a9dbdb4_2_690x307.jpeg" alt="image" data-base62-sha1="xBUrB0F3SJZHtMpEDH1FimhvtAM" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb90cda2883b759ad7acc34952f212552a9dbdb4_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb90cda2883b759ad7acc34952f212552a9dbdb4_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb90cda2883b759ad7acc34952f212552a9dbdb4_2_1380x614.jpeg 2x" data-dominant-color="ABADD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2375×1057 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How han I introduce in the Python code a different shift value?</p>
<p>Next, as you can see in the CT, there is a platform below the skull, of approximate 2-3 cm. In all my scans this platform exists. So I would like to remove it by cropping this volume (and generating another _cropped) by using ROI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3069d1f8564c33bdc014768c63c56e78f1f3034e.jpeg" data-download-href="/uploads/short-url/6UhDvNC9li7hEESOsU8wILtFZb8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d1f8564c33bdc014768c63c56e78f1f3034e_2_690x290.jpeg" alt="image" data-base62-sha1="6UhDvNC9li7hEESOsU8wILtFZb8" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d1f8564c33bdc014768c63c56e78f1f3034e_2_690x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d1f8564c33bdc014768c63c56e78f1f3034e_2_1035x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d1f8564c33bdc014768c63c56e78f1f3034e_2_1380x580.jpeg 2x" data-dominant-color="ACADD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2522×1063 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried cropping in empty volume, which is a script in the Slicer documentation. But I do not know how can I apply to an existing volume and creating another.</p>
<p>How can it be done?</p>
<p>Best</p>

---

## Post #2 by @muratmaga (2024-01-18 16:51 UTC)

<p>Few general comments:</p>
<ol>
<li>
<p>When you are converting/processing 1000s of files, you do not want to interactively do anything, including visualization. So for your purposes visualization step is probably not necessary and will add additional time to your pipeline (but it is total fine, if you are using as a way to learn scripting).</p>
</li>
<li>
<p>First thing I would do is to interactively create a ROI box from that will crop most of the foam out in one sample, save it to disk, and reload and test it interactively with few other samples to get a sense of how consistent the sample placement, and whether you can use this fixed size ROI for most (if not all) of your samples. If the answer is no (samples have different orientation, origins etc), you will have to find a heuristic that will get you to crop box automatically. This might involve fitting an ROI to the volume, and then reducing in the  I plane a few centimeters (again if all your samples are consistently oriented).</p>
</li>
</ol>
<p>this example here shows how to load NRRD file and fit a ROI and resample it to a lower resolution. You can modify it to fit your needs (namely modify the dimensions of the ROI box).</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/Scripts#5-read-an-nrrd-volume-from-the-disk-and-resample-it-to-a-specified-voxel-size">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Scripts#5-read-an-nrrd-volume-from-the-disk-and-resample-it-to-a-specified-voxel-size" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/86b9de2c26925ed33403bfebd5558d6c498595e2621c86ed6ac7b93cc5ac64a3/SlicerMorph/Scripts" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/Scripts#5-read-an-nrrd-volume-from-the-disk-and-resample-it-to-a-specified-voxel-size" target="_blank" rel="noopener">GitHub - SlicerMorph/Scripts</a></h3>

  <p>Contribute to SlicerMorph/Scripts development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @paleomariomm (2024-01-19 13:15 UTC)

<p>Thanks for the link Murat,</p>
<p>I adapted the code up to here:</p>
<pre><code class="lang-auto"># find the files NodeID
volumeNode = getNode('2: Facial Bones  0.75  H70h')

#create a blank Markup ROI
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")

#set the new markup ROI to the dimensions of the volume
cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolumeParameters.SetInputVolumeNodeID(volumeNode.GetID())
cropVolumeParameters.SetROINodeID(roiNode.GetID())
slicer.modules.cropvolume.logic().SnapROIToVoxelGrid(cropVolumeParameters)  # optional (rotates the ROI to match the volume axis directions)
slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
slicer.mrmlScene.RemoveNode(cropVolumeParameters)

#set the cropping parameters
cropVolumeLogic = slicer.modules.cropvolume.logic()
cropVolumeParameterNode = slicer.vtkMRMLCropVolumeParametersNode()
cropVolumeParameterNode.SetIsotropicResampling(True)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e3c63e0cec17e963d509aa9818f41c5c493f18.jpeg" data-download-href="/uploads/short-url/tNVjJf0zSp4No7LUQpxD1iRGs4M.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e3c63e0cec17e963d509aa9818f41c5c493f18_2_690x453.jpeg" alt="image" data-base62-sha1="tNVjJf0zSp4No7LUQpxD1iRGs4M" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e3c63e0cec17e963d509aa9818f41c5c493f18_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e3c63e0cec17e963d509aa9818f41c5c493f18_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0e3c63e0cec17e963d509aa9818f41c5c493f18_2_1380x906.jpeg 2x" data-dominant-color="CBC6D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1262 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I am struggling on how to insert cropping bounds in here. How do I specify to crop only lower bound up to 2 cm?</p>
<p>Answering your question, all 1000 skulls were scanned keeping the same orientation.</p>

---

## Post #4 by @muratmaga (2024-01-19 16:12 UTC)

<p>You have to look up the API, I don’t actually know the python call to set the ROI bounds <a class="mention" href="/u/lassoan">@lassoan</a>?</p>
<p>But if you are certain that orientation is consistent, then you don’t have to recreate the ROI every time and fit to the volume. I would adjust one manually, save it, and write the script in a way that will use it (load from the disk).</p>

---

## Post #5 by @chir.set (2024-01-19 17:37 UTC)

<p>As <a class="mention" href="/u/muratmaga">@muratmaga</a> said, a saved ROI might be the best approach.</p>
<p>I had a more or less similar workflow with CT angiograms and came up with a custom script. You may find some insight <a href="https://gitlab.com/chir-set/Tools7/-/blame/master/TemplateROICrop/TemplateROICrop.py#L166" rel="noopener nofollow ugc">here</a> to set Window/Level, load a known ROI from disk and apply cropping. Full automation should be possible the way you laid out the problem.</p>

---
