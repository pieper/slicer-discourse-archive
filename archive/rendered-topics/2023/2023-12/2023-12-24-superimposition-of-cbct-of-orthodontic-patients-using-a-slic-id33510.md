# Superimposition of CBCT of orthodontic patients using a slicer, diagnocat, blender

**Topic ID**: 33510
**Date**: 2023-12-24
**URL**: https://discourse.slicer.org/t/superimposition-of-cbct-of-orthodontic-patients-using-a-slicer-diagnocat-blender/33510

---

## Post #1 by @danik (2023-12-24 21:36 UTC)

<p>Good afternoon, dear colleagues. My name is Daniil, I am a dentist, orthodontist. For 4 years I have been doing superimposition before and after orthodontic treatment. I use stl files from Diagnocat and overlay them. I encountered inaccuracy in segmentation and, therefore, inaccuracy in overlay. I switched to slicer and studied the forum for a long time, I want to thank <a class="mention" href="/u/finetjul">@finetjul</a><br>
Julien Finet, <a class="mention" href="/u/lassoan">@lassoan</a><br>
Andras Lasso, <a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Murat Maga. Thanks to your answers, things are starting to work out.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f653f78ba32f9d5bd96952bf32afbf96925ae95.mp4">
  </div><p></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b5cb292dde1dc39b1d30afcd5c350dcd56ac80e.png" data-download-href="/uploads/short-url/d2e3jhvbE9p4sMmmL4fmz3CYPCK.png?dl=1" title="image_2023-12-25_00-19-57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b5cb292dde1dc39b1d30afcd5c350dcd56ac80e.png" alt="image_2023-12-25_00-19-57" data-base62-sha1="d2e3jhvbE9p4sMmmL4fmz3CYPCK" width="393" height="500" data-dominant-color="EDEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2023-12-25_00-19-57</span><span class="informations">428×544 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
About working in the slicer, first I upload two CT scans, before the start of treatment and after, then I select transform, orient the CT scan after, with my hands, then I use the General registration elastix tool, it completes the job, I confirm all the actions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12e8cb97547062a2d8b509d1504e98bcb9e2fcd2.jpeg" data-download-href="/uploads/short-url/2Hhm4EPO76WYurUxC1znYbnDjd8.jpeg?dl=1" title="photo_2023-12-25_00-17-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12e8cb97547062a2d8b509d1504e98bcb9e2fcd2_2_690x369.jpeg" alt="photo_2023-12-25_00-17-46" data-base62-sha1="2Hhm4EPO76WYurUxC1znYbnDjd8" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12e8cb97547062a2d8b509d1504e98bcb9e2fcd2_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12e8cb97547062a2d8b509d1504e98bcb9e2fcd2_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12e8cb97547062a2d8b509d1504e98bcb9e2fcd2.jpeg 2x" data-dominant-color="6C6B72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">photo_2023-12-25_00-17-46</span><span class="informations">1280×686 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I convert the images into dicom, after treatment and upload them to the diagnocat .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e627cc39bedb24e137cd63f201084f355a3bcf5.jpeg" data-download-href="/uploads/short-url/kjAO9N5nUi37mMa3F6rqezpGj1b.jpeg?dl=1" title="photo_2023-12-25_00-18-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e627cc39bedb24e137cd63f201084f355a3bcf5_2_690x245.jpeg" alt="photo_2023-12-25_00-18-13" data-base62-sha1="kjAO9N5nUi37mMa3F6rqezpGj1b" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e627cc39bedb24e137cd63f201084f355a3bcf5_2_690x245.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e627cc39bedb24e137cd63f201084f355a3bcf5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e627cc39bedb24e137cd63f201084f355a3bcf5.jpeg 2x" data-dominant-color="100D0F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">photo_2023-12-25_00-18-13</span><span class="informations">808×288 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then, in a blender, I orient the CT scan along the Frankfurt and the median cranial plane, grind the teeth and take measurements. the application turns out to be acceptable, but the teeth move in the process, as does the lower jaw, and the General registration elastix tool, as I understand it, pays attention to all structures, questions arise<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f8a8c837263074da33e818b6e7c8484db06ada4.png" data-download-href="/uploads/short-url/dDccm6Uvs8Eod4kwh13lpjUnUaM.png?dl=1" title="image_2023-12-25_00-15-36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f8a8c837263074da33e818b6e7c8484db06ada4_2_461x500.png" alt="image_2023-12-25_00-15-36" data-base62-sha1="dDccm6Uvs8Eod4kwh13lpjUnUaM" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f8a8c837263074da33e818b6e7c8484db06ada4_2_461x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f8a8c837263074da33e818b6e7c8484db06ada4_2_691x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f8a8c837263074da33e818b6e7c8484db06ada4.png 2x" data-dominant-color="8C888B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2023-12-25_00-15-36</span><span class="informations">705×764 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef00e6a5c34cdc4b7a2ba494b7dc699d8c8066f3.png" data-download-href="/uploads/short-url/y6k2PRtzgdxsNX00AS1K2EbG3Jx.png?dl=1" title="image_2023-12-25_00-15-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef00e6a5c34cdc4b7a2ba494b7dc699d8c8066f3_2_461x500.png" alt="image_2023-12-25_00-15-54" data-base62-sha1="y6k2PRtzgdxsNX00AS1K2EbG3Jx" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef00e6a5c34cdc4b7a2ba494b7dc699d8c8066f3_2_461x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef00e6a5c34cdc4b7a2ba494b7dc699d8c8066f3_2_691x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef00e6a5c34cdc4b7a2ba494b7dc699d8c8066f3.png 2x" data-dominant-color="878B8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2023-12-25_00-15-54</span><span class="informations">705×764 383 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d44b6219acb7d4a375fafff39d60a89b7899c6ab.png" data-download-href="/uploads/short-url/ui2JlUeBXmPyo5WZU2wlySgpdkD.png?dl=1" title="image_2023-12-25_00-16-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d44b6219acb7d4a375fafff39d60a89b7899c6ab_2_461x500.png" alt="image_2023-12-25_00-16-13" data-base62-sha1="ui2JlUeBXmPyo5WZU2wlySgpdkD" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d44b6219acb7d4a375fafff39d60a89b7899c6ab_2_461x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d44b6219acb7d4a375fafff39d60a89b7899c6ab_2_691x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d44b6219acb7d4a375fafff39d60a89b7899c6ab.png 2x" data-dominant-color="8A8B8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2023-12-25_00-16-13</span><span class="informations">705×764 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
1 Is it possible to make comparisons for certain areas, for example, sphenoethmoidal synchondrosis (it is fully formed by the age of 8)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1000ac2db1961ea7b05626afe5745b161c2dfcf3.png" data-download-href="/uploads/short-url/2hz4ZsXJapznkrysZ1kOeaBhSW7.png?dl=1" title="image_2023-12-25_00-35-52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1000ac2db1961ea7b05626afe5745b161c2dfcf3_2_690x469.png" alt="image_2023-12-25_00-35-52" data-base62-sha1="2hz4ZsXJapznkrysZ1kOeaBhSW7" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1000ac2db1961ea7b05626afe5745b161c2dfcf3_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1000ac2db1961ea7b05626afe5745b161c2dfcf3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1000ac2db1961ea7b05626afe5745b161c2dfcf3.png 2x" data-dominant-color="4B4956"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2023-12-25_00-35-52</span><span class="informations">841×572 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
, to analyze work with growing patients, adults after teeth have been moved. 2 how to compare the lower jaw, 3 how to isolate it from the total volume, 1 select comparison zones. I hope for your detailed help, thank you</p>

---

## Post #2 by @muratmaga (2023-12-25 07:10 UTC)

<aside class="quote no-group" data-username="danik" data-post="1" data-topic="33510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/49beb7/48.png" class="avatar"> danik:</div>
<blockquote>
<p>Then, in a blender, I orient the CT scan along the Frankfurt and the median cranial plane, grind the</p>
</blockquote>
</aside>
<p>You should be able to do everything you want in Slicer, without any other program.</p>
<ol>
<li>Use DICOM module to import your DICOMs directly into Slicer.</li>
<li>Use this simple script to align any volume with three points that define Frankfort horizontal (<a href="https://github.com/SlicerMorph/S_2019/tree/master/Lab08#example-1-aligning-volumes-using-landmarks-frankfort-alignment-plane" class="inline-onebox">S_2019/Lab08 at master · SlicerMorph/S_2019 · GitHub</a>)</li>
<li>If you want to restrict your registration to a specific region, you can either crop them with ROI and only use them to register. Or define a mask using segment editor and specify masks during registration process.</li>
</ol>
<aside class="quote no-group" data-username="danik" data-post="1" data-topic="33510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/49beb7/48.png" class="avatar"> danik:</div>
<blockquote>
<p>1 Is it possible to make comparisons for certain areas, for example, sphenoethmoidal synchondrosis (it is fully formed by the age of 8)</p>
</blockquote>
</aside>
<p>Not sure what and how you would like to compare things? I couldn’t quite follow what you want to do.</p>

---

## Post #3 by @danik (2023-12-25 12:04 UTC)

<p>good afternoon, thank you very much for your answer <a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Murat Maga. I’m very glad that I can do everything in the slicer, it’s important to me.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28a4bfdc98c7e0ff785d0680a07e216610c4712c.jpeg" data-download-href="/uploads/short-url/5Ny4wfW7ZPSzDSPycwAYayR78Qs.jpeg?dl=1" title="image_2023-12-25_14-49-41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28a4bfdc98c7e0ff785d0680a07e216610c4712c_2_690x431.jpeg" alt="image_2023-12-25_14-49-41" data-base62-sha1="5Ny4wfW7ZPSzDSPycwAYayR78Qs" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28a4bfdc98c7e0ff785d0680a07e216610c4712c_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28a4bfdc98c7e0ff785d0680a07e216610c4712c_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28a4bfdc98c7e0ff785d0680a07e216610c4712c_2_1380x862.jpeg 2x" data-dominant-color="414049"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2023-12-25_14-49-41</span><span class="informations">1449×907 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to make an overlay over a selected area to look at how jaw growth has changed in children or how the position of teeth has changed in an orthodontic patient after treatment.I imagine it like this, I need 1.0 - load two CT scans, 1.1 segment the selection zone of the CT scan before (so that the comparison is based on bone landmarks) 1.2 compare the CT scan after, with the CT scan before, according to the segmentation zone, 1.3 save. Could you tell me 2 whether I present the algorithm correctly, 3 whether it is possible, if so, 1 it would be useful for me to describe in detail how and what tools should be used, maybe. I have little experience with slicers, thanks</p>

---

## Post #4 by @muratmaga (2023-12-26 16:52 UTC)

<p>If you have 6-7 landmarks, you don’t even need to segment anything or define an ROI.  Place the same set of landmarks on both volumes. Then use the Fiducial Registration Wizard from the SlicerIGT extenstion to create a Rigid Transform. Finally put the volume which you define as the source landmark under this transform. The volumes will be aligned using those landmarks as constraints.</p>

---

## Post #5 by @danik (2023-12-26 18:30 UTC)

<p>good afternoon, <a class="mention" href="/u/muratmaga">@muratmaga</a> ,everything worked out, thank you very much. Did I understand correctly that ROI can be used like points?<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/940151920385039b4e0525b2a82d2b76c52938da.mp4">
  </div><p></p>

---

## Post #6 by @muratmaga (2023-12-26 20:16 UTC)

<p>I am glad things worked out. ROIs come into play if you are going to do image registration. Then the contents of the ROIs is used as the constraint for the registration. Otherwise, if you are going to stick to landmarks, no need for ROI.</p>

---

## Post #7 by @anasmh101 (2023-12-30 02:42 UTC)

<p>Hello, thank you for your answer, I have a  problem with orienting DICOM according to Frankfort plane , I did all the steps that you have mentioned at the GitHub, I copied and pasted the script but nothing happened,<br>
this is what shown on the python console</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/eca488dae5d352a3e975ee2562a723dbdc1ade86.png" data-download-href="/uploads/short-url/xLrccliNsBqaLoGUXcLVRufh1NY.png?dl=1" title="python" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/eca488dae5d352a3e975ee2562a723dbdc1ade86.png" alt="python" data-base62-sha1="xLrccliNsBqaLoGUXcLVRufh1NY" width="690" height="362" data-dominant-color="FDF1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">python</span><span class="informations">691×363 5.09 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2023-12-30 19:06 UTC)

<p>Sorry there has been an API change since this snippet was written. Try this, seems to work for me using the sample data provided in Slicer 5.6.1</p>
<pre data-code-wrap="Python"><code class="lang-Python">import numpy
scene = slicer.mrmlScene
F = getNodesByClass('vtkMRMLMarkupsFiducialNode')
F = F[0]

# Get the fiducial IDs of porions and zygomatico - orbitale  suture from the fiducial list by name
po1_id = -1; po2_id = -1; zyo_id = -1;

for i in range(0, F.GetNumberOfControlPoints()):
	if F.GetNthControlPointLabel(i) == 'poR' :
		po1_id = i
	if F.GetNthControlPointLabel(i) == 'poL' :
		po2_id = i
	if F.GetNthControlPointLabel(i) == 'zyoL' :
		zyo_id = i


# Get the coordinates of landmarks
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# The vector between two porions that we will align to LR axis by calculating the yaw angle
po =[po1[0] - po2[0], po1[1] -po2[1], po1[2]-po2[2]]
vTransform = vtk.vtkTransform()
vTransform.RotateZ(-numpy.arctan2(po[1], po[0])*180/numpy.pi)
transform.SetMatrixTransformToParent(vTransform.GetMatrix())

# Apply the transform to the fiducials and the volume
transform = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform) 
transform.SetMatrixTransformToParent(vTransform.GetMatrix())
V = getNodesByClass('vtkMRMLScalarVolumeNode')
V = V[0]
V.SetAndObserveTransformNodeID(transform.GetID())
F.SetAndObserveTransformNodeID(transform.GetID())

# Get the updated (transformed) coordinates from the list
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# Apply the transform to the coordinates
po1 = vTransform.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])
po =[po1[0]-po2[0], po1[1]-po2[1], po1[2]-po2[2]]

# Calculate the rotation for the roll 
vTransform2 = vtk.vtkTransform()
vTransform2.RotateY(numpy.arctan2(po[2], po[0])*180/numpy.pi)

# Apply the transform to previous transform hierarchy
transform2 = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform2) 
transform2.SetMatrixTransformToParent(vTransform2.GetMatrix())
transform.SetAndObserveTransformNodeID(transform2.GetID())

# Get the coordinates again
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# Apply transforms to points to get updated coordinates
po1 = vTransform.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])
po1 = vTransform2.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform2.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform2.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])

# The vector for pitch angle
po_zyo = [zyo[0]-(po1[0]+po2[0])/2, zyo[1]-(po1[1]+po2[1])/2, zyo[2]-(po1[2]+po2[2])/2]

# Calculate the transform for aligning pitch
vTransform3 = vtk.vtkTransform()
vTransform3.RotateX(-numpy.arctan2(po_zyo[2], po_zyo[1])*180/numpy.pi)

# Apply the transform to both fiducial list and the volume
transform3 = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform3) 
transform3.SetMatrixTransformToParent(vTransform3.GetMatrix())
transform2.SetAndObserveTransformNodeID(transform3.GetID())


slicer.vtkSlicerTransformLogic().hardenTransform(V)
</code></pre>

---

## Post #9 by @danik (2023-12-30 19:14 UTC)

<aside class="quote no-group" data-username="danik" data-post="5" data-topic="33510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/49beb7/48.png" class="avatar"> danik:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a></p>
</blockquote>
</aside>
<p>good afternoon, <a class="mention" href="/u/muratmaga">@muratmaga</a>. I want to ask, I succeeded in matching, but now the question for me is how to save the new CT orientation after, how to export this new orientation from the slicer?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30a55cc05e35b8f9676a0de4a80a977f249fabcd.jpeg" data-download-href="/uploads/short-url/6WlcKHsflpvHAjizS2tpVgb8DBb.jpeg?dl=1" title="22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a55cc05e35b8f9676a0de4a80a977f249fabcd_2_690x372.jpeg" alt="22" data-base62-sha1="6WlcKHsflpvHAjizS2tpVgb8DBb" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a55cc05e35b8f9676a0de4a80a977f249fabcd_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a55cc05e35b8f9676a0de4a80a977f249fabcd_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a55cc05e35b8f9676a0de4a80a977f249fabcd_2_1380x744.jpeg 2x" data-dominant-color="767579"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">22</span><span class="informations">1914×1032 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2023-12-30 23:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="33510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>slicer.vtkSlicerTransformLogic().hardenTransform(V)</code></p>
</blockquote>
</aside>
<p>The last line of the code<br>
<code>slicer.vtkSlicerTransformLogic().hardenTransform(V)</code></p>
<p>is applying the transformation to the image. If you save it, and reload only the save image, you should see that it is preserved.</p>

---

## Post #11 by @anasmh101 (2023-12-31 03:02 UTC)

<p>thank you so much for your reply<br>
I still get this note on the python console,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195a00f05d6b7e1330365499fdc1bc4d1bbdae30.png" alt="python 2" data-base62-sha1="3CgLEZRcYDH6GFnGwA16CjZUK1a" width="647" height="202"></p>

---

## Post #12 by @muratmaga (2023-12-31 21:38 UTC)

<p>I must have copied and pasted the code incompete somehow.</p>
<pre data-code-wrap="Python"><code class="lang-Python">import numpy
scene = slicer.mrmlScene
F = getNodesByClass('vtkMRMLMarkupsFiducialNode')
F = F[0]

# Get the fiducial IDs of porions and zygomatico - orbitale  suture from the fiducial list by name
po1_id = -1; po2_id = -1; zyo_id = -1;

for i in range(0, F.GetNumberOfControlPoints()):
	if F.GetNthControlPointLabel(i) == 'poR' :
		po1_id = i
	if F.GetNthControlPointLabel(i) == 'poL' :
		po2_id = i
	if F.GetNthControlPointLabel(i) == 'zyoL' :
		zyo_id = i


# Get the coordinates of landmarks
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

transform = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform) 

# The vector between two porions that we will align to LR axis by calculating the yaw angle
po =[po1[0] - po2[0], po1[1] -po2[1], po1[2]-po2[2]]
vTransform = vtk.vtkTransform()
vTransform.RotateZ(-numpy.arctan2(po[1], po[0])*180/numpy.pi)
transform.SetMatrixTransformToParent(vTransform.GetMatrix())

# Apply the transform to the fiducials and the volume
transform.SetMatrixTransformToParent(vTransform.GetMatrix())
V = getNodesByClass('vtkMRMLScalarVolumeNode')
V = V[0]
V.SetAndObserveTransformNodeID(transform.GetID())
F.SetAndObserveTransformNodeID(transform.GetID())

# Get the updated (transformed) coordinates from the list
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# Apply the transform to the coordinates
po1 = vTransform.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])
po =[po1[0]-po2[0], po1[1]-po2[1], po1[2]-po2[2]]

# Calculate the rotation for the roll 
vTransform2 = vtk.vtkTransform()
vTransform2.RotateY(numpy.arctan2(po[2], po[0])*180/numpy.pi)

# Apply the transform to previous transform hierarchy
transform2 = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform2) 
transform2.SetMatrixTransformToParent(vTransform2.GetMatrix())
transform.SetAndObserveTransformNodeID(transform2.GetID())

# Get the coordinates again
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# Apply transforms to points to get updated coordinates
po1 = vTransform.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])
po1 = vTransform2.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform2.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform2.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])

# The vector for pitch angle
po_zyo = [zyo[0]-(po1[0]+po2[0])/2, zyo[1]-(po1[1]+po2[1])/2, zyo[2]-(po1[2]+po2[2])/2]

# Calculate the transform for aligning pitch
vTransform3 = vtk.vtkTransform()
vTransform3.RotateX(-numpy.arctan2(po_zyo[2], po_zyo[1])*180/numpy.pi)

# Apply the transform to both fiducial list and the volume
transform3 = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform3) 
transform3.SetMatrixTransformToParent(vTransform3.GetMatrix())
transform2.SetAndObserveTransformNodeID(transform3.GetID())


slicer.vtkSlicerTransformLogic().hardenTransform(V)
</code></pre>
<p>should work <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @anasmh101 (2024-01-02 06:53 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="33510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<pre><code class="lang-auto">import numpy
scene = slicer.mrmlScene
F = getNodesByClass('vtkMRMLMarkupsFiducialNode')
F = F[0]

# Get the fiducial IDs of porions and zygomatico - orbitale  suture from the fiducial list by name
po1_id = -1; po2_id = -1; zyo_id = -1;

for i in range(0, F.GetNumberOfControlPoints()):
	if F.GetNthControlPointLabel(i) == 'poR' :
		po1_id = i
	if F.GetNthControlPointLabel(i) == 'poL' :
		po2_id = i
	if F.GetNthControlPointLabel(i) == 'zyoL' :
		zyo_id = i


# Get the coordinates of landmarks
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

transform = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform) 

# The vector between two porions that we will align to LR axis by calculating the yaw angle
po =[po1[0] - po2[0], po1[1] -po2[1], po1[2]-po2[2]]
vTransform = vtk.vtkTransform()
vTransform.RotateZ(-numpy.arctan2(po[1], po[0])*180/numpy.pi)
transform.SetMatrixTransformToParent(vTransform.GetMatrix())

# Apply the transform to the fiducials and the volume
transform.SetMatrixTransformToParent(vTransform.GetMatrix())
V = getNodesByClass('vtkMRMLScalarVolumeNode')
V = V[0]
V.SetAndObserveTransformNodeID(transform.GetID())
F.SetAndObserveTransformNodeID(transform.GetID())

# Get the updated (transformed) coordinates from the list
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# Apply the transform to the coordinates
po1 = vTransform.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])
po =[po1[0]-po2[0], po1[1]-po2[1], po1[2]-po2[2]]

# Calculate the rotation for the roll 
vTransform2 = vtk.vtkTransform()
vTransform2.RotateY(numpy.arctan2(po[2], po[0])*180/numpy.pi)

# Apply the transform to previous transform hierarchy
transform2 = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform2) 
transform2.SetMatrixTransformToParent(vTransform2.GetMatrix())
transform.SetAndObserveTransformNodeID(transform2.GetID())

# Get the coordinates again
po1 = [0, 0, 0]
po2 = [0, 0, 0]
zyo = [0, 0, 0]

F.GetNthControlPointPosition(po1_id,po1)
F.GetNthControlPointPosition(po2_id,po2)
F.GetNthControlPointPosition(zyo_id,zyo)

# Apply transforms to points to get updated coordinates
po1 = vTransform.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])
po1 = vTransform2.GetMatrix().MultiplyPoint([po1[0], po1[1], po1[2], 0])
po2 = vTransform2.GetMatrix().MultiplyPoint([po2[0], po2[1], po2[2], 0])
zyo = vTransform2.GetMatrix().MultiplyPoint([zyo[0], zyo[1], zyo[2], 0])

# The vector for pitch angle
po_zyo = [zyo[0]-(po1[0]+po2[0])/2, zyo[1]-(po1[1]+po2[1])/2, zyo[2]-(po1[2]+po2[2])/2]

# Calculate the transform for aligning pitch
vTransform3 = vtk.vtkTransform()
vTransform3.RotateX(-numpy.arctan2(po_zyo[2], po_zyo[1])*180/numpy.pi)

# Apply the transform to both fiducial list and the volume
transform3 = slicer.vtkMRMLLinearTransformNode()
scene.AddNode(transform3) 
transform3.SetMatrixTransformToParent(vTransform3.GetMatrix())
transform2.SetAndObserveTransformNodeID(transform3.GetID())


slicer.vtkSlicerTransformLogic().hardenTransform(V)
</code></pre>
</blockquote>
</aside>
<p>thank you so much, it worked perfectly</p>

---

## Post #14 by @danik (2024-01-06 19:24 UTC)

<p>After fiducial reg. I go to transform, there I move ct after and dots after in transformed, then apply Harden transform. I will convert the field nrrd to dicom. When I open before and after pictures in the slicer, the orientation is saved, but when I upload it to diagnocat for segmentation, the original orientation is there. I tried using confert, but I still couldn’t figure out what was what.</p>

---

## Post #15 by @danik (2024-01-06 19:25 UTC)

<p><span class="mention">@maratmega</span> answered - The fault is probably on the other software that you are using to import those modified dicoms. My guess it doesn’t read the orientation matrix Slicer saved. Try resampling the data and exporting one more time. Instead of hardening, keep it under the transform and then use the crop volume to resample the data.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolumesequence.html#overview" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolumesequence.html#overview</a></p>

---

## Post #16 by @danik (2024-01-06 19:26 UTC)

<p>I sent him a private message <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #17 by @danik (2024-01-06 20:28 UTC)

<p>Good afternoon, the slicer works great for comparison, but when I load the new CT orientation into diagnocat, it’s not saved. I tried saving the new CT orientation after hard transformation and crop volume sequence, what other options are there to export the CT scan so that the orientation changes to the new one?<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0540cf118da7d5a398d5479a0de2f23e998dd4b7.mp4">
  </div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56b2858fbef05e48106b19c542364be6d6d1dbf8.jpeg" data-download-href="/uploads/short-url/cmXxHaNZDxyYFoBCwM78uAquEaY.jpeg?dl=1" title="photo_2024-01-06_23-14-34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56b2858fbef05e48106b19c542364be6d6d1dbf8_2_690x369.jpeg" alt="photo_2024-01-06_23-14-34" data-base62-sha1="cmXxHaNZDxyYFoBCwM78uAquEaY" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56b2858fbef05e48106b19c542364be6d6d1dbf8_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56b2858fbef05e48106b19c542364be6d6d1dbf8_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56b2858fbef05e48106b19c542364be6d6d1dbf8.jpeg 2x" data-dominant-color="464646"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">photo_2024-01-06_23-14-34</span><span class="informations">1280×685 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
maybe I’m not working correctly with the Crop volume sequence, I placed the desired CT AFTER in the input and created a new one in the output<p></p>

---

## Post #18 by @danik (2024-01-07 09:33 UTC)

<p>good afternoon, today I tried to use general registration (elastics), then I loaded the CT scan into the diagnocat and the orientation was changed, but the comparison itself did not suit me, maybe you know another registration method with a similar operating algorithm?<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b13aa83d63d990422a53a415b2293ad68955d23.mp4">
  </div><p></p>

---

## Post #19 by @danik (2024-01-07 18:18 UTC)

<p>Good afternoon, today I tried ct segmentation after in blueskyplan. Everything is the same as with Diagnocad, the CT orientation remains the same</p>

---
