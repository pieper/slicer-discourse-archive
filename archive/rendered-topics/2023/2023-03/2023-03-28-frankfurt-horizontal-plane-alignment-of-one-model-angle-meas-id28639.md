---
topic_id: 28639
title: "Frankfurt Horizontal Plane Alignment Of One Model Angle Meas"
date: 2023-03-28
url: https://discourse.slicer.org/t/28639
---

# Frankfurt Horizontal Plane alignment of one model, angle measurements

**Topic ID**: 28639
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/frankfurt-horizontal-plane-alignment-of-one-model-angle-measurements/28639

---

## Post #1 by @esomjai (2023-03-28 22:56 UTC)

<p>Hi there,<br>
I am currently starting a masters project in facial approximation with a landmark-heavy plan.<br>
I apologise if my questions are answered elsewhere, I truly am new to 3D Slicer.</p>
<ol>
<li>
<p>I would like to establish the Frankfort horizontal plane (anatomical plane based on 4 landmarks) as my midline for the models (see example pictures )  - they do not need to be aligned, their positions just need to be adjusted according to the plane. I established the plane before, having a hard time adjusting the view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7d481e6dcc35d11b994e769f3e8361799ee74d0.png" data-download-href="/uploads/short-url/x4RACNYRK7XHvXavXwgN7yMmy40.png?dl=1" title="fhn" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7d481e6dcc35d11b994e769f3e8361799ee74d0.png" alt="fhn" data-base62-sha1="x4RACNYRK7XHvXavXwgN7yMmy40" width="690" height="392" data-dominant-color="8C8D31"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fhn</span><span class="informations">850×483 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a33b095b9216673838abd84f008d5087cccfd4df.png" alt="fhn2" data-base62-sha1="ni0joQA8jSfF8LYBdX2icNqfgrd" width="320" height="456"></p>
</li>
<li>
<p>This plane is the basis of my angle measurements - I have lines in between landmarks crossing the plane and I will need the coordinates of these to be precise when measuring angles in relation to the plane. I am using this study: Guyomarc’h, P. and Stephan, C.N. (2012), The Validity of Ear Prediction Guidelines Used in Facial Approximation. Journal of Forensic Sciences, 57: 1427-1441. <a href="https://doi.org/10.1111/j.1556-4029.2012.02181.x" rel="noopener nofollow ugc">https://doi.org/10.1111/j.1556-4029.2012.02181.x</a></p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1c81932d8af559bbd8321a8decce1ef80eb0dc.png" alt="stephan et al" data-base62-sha1="8qVfbpPUJmNS5afAvmRoTMeDYqU" width="310" height="274"></p>
<p>Thank you in advance for your time and assistance!</p>

---

## Post #2 by @muratmaga (2023-03-29 04:56 UTC)

<p>We use this tutorial as an example of scripting in Slicer. It uses three points to define the Frankfort, but it should be trivial to adjust it to use your four points:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/W_2020/tree/master/Lab09_Slicer_Scripting#example-1-aligning-volumes-using-landmarks-frankfort-alignment-plane">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab09_Slicer_Scripting#example-1-aligning-volumes-using-landmarks-frankfort-alignment-plane" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab09_Slicer_Scripting#example-1-aligning-volumes-using-landmarks-frankfort-alignment-plane" target="_blank" rel="noopener">W_2020/Lab09_Slicer_Scripting at master · SlicerMorph/W_2020 - Example 1: Aligning volumes using landmarks (Frankfort alignment plane).</a></h3>

  <p><a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab09_Slicer_Scripting#example-1-aligning-volumes-using-landmarks-frankfort-alignment-plane" target="_blank" rel="noopener">master/Lab09_Slicer_Scripting</a></p>

  <p><span class="label1">Contents for the Winter 2020 SlicerMorph workshop. Contribute to SlicerMorph/W_2020 development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @esomjai (2023-03-30 17:47 UTC)

<p>Thank you so much for this! I have adjusted the code to suit version 5.2.2 and it works perfectly!<br>
I decided to do the 3-landmark approach anyway.</p>
<p>in case anyone reading these posts is interested in this version:</p>
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

# The vector between two porions that we will align to LR axis by calculating the yaw angle
po =[po1[0] - po2[0], po1[1] -po2[1], po1[2]-po2[2]]
vTransform = vtk.vtkTransform()
vTransform.RotateZ(-numpy.arctan2(po[1], po[0])*180/numpy.pi)
transform = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode')
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
<p>Now that part 1 of my loaded question is solved, the second part remains - How do I get the coordinates of the intersection point where my measurement line crosses the plane? I could do this with approximation but that would be imprecise…</p>
<p>Thank you again for your time and assistance!</p>

---

## Post #5 by @lili-yu22 (2024-10-25 05:41 UTC)

<p>can you help me?<br>
I don’t know pathon please give me script to produce a sagittal plane through N point and vertical to FHplane.</p>

---

## Post #6 by @esomjai (2024-10-25 07:52 UTC)

<p>Dear lili-yu22,</p>
<p>I think you’d need a different approach for that…</p>
<p>I would not do this by python scripting if you already have your FHPlane in the environment - I’d do the following:<br>
1.</p>
<ol>
<li>Duplicate the FHP ONCE (right click on Markups list &gt; Clone)</li>
</ol>
<ul>
<li>Rename it to Sag</li>
</ul>
<p>Time to rotate the new planes</p>
<ul>
<li>
<p>Open Transforms</p>
</li>
<li>
<p>Click Sag, then the &gt;○ arrow</p>
</li>
</ul>
<ol>
<li>
<p>Adjust Rotation LR to 90 degrees</p>
</li>
<li>
<p>Click again on Sag and on ‘Harden Transform’</p>
</li>
<li>
<p>Adjust the planes to meet the dots described</p>
</li>
<li>
<p>Toggle the visibility of the point you need the plane to meet (N)</p>
</li>
<li>
<p>Then enable under <code>Display¬ </code>Interaction<code> Visibility</code> <code>enable translation</code> for all and manually toggle until they cross the landmarks described above</p>
</li>
<li>
<p>If they don’t move, unlock their control points!1. I hope this helps <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>
</li>
</ol>
<p>Best wishes,<br>
Eszter</p>

---

## Post #7 by @lili-yu22 (2024-11-05 04:41 UTC)

<p>I copy  the script ，but  I also  want  the segment of the skull adjust as the volume 。so I modify the script as the picture ， but after I usethe modified scipt， the volume and the segment of the skullnot overlap，please help me​:rose:<img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a537b4e865cf404d37408649323a6fa6e9293a6.jpeg" data-download-href="/uploads/short-url/1tlDgBhDVSPfR5kA49QdSH08eFw.jpeg?dl=1" title="IMG_20241105_123848_edit_64463091217767" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a537b4e865cf404d37408649323a6fa6e9293a6_2_375x500.jpeg" alt="IMG_20241105_123848_edit_64463091217767" data-base62-sha1="1tlDgBhDVSPfR5kA49QdSH08eFw" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a537b4e865cf404d37408649323a6fa6e9293a6_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a537b4e865cf404d37408649323a6fa6e9293a6_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a537b4e865cf404d37408649323a6fa6e9293a6_2_750x1000.jpeg 2x" data-dominant-color="7B7874"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20241105_123848_edit_64463091217767</span><span class="informations">1920×2560 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @esomjai (2024-11-15 13:01 UTC)

<p>Hi,<br>
I believe the issue is in the order in which you execute the steps.<br>
I re-orientate my scan (script) BEFORE any segmentation takes place - this way, they will be oriented the same.<br>
I hope this helps.</p>
<p>so</p>
<ol>
<li>Open the DICOM file,</li>
<li>Put the orientating landmarks for FHP on the image</li>
<li>Run the script</li>
<li>Create an segmentations needed</li>
</ol>

---

## Post #9 by @lili-yu22 (2024-11-16 09:14 UTC)

<p>thank you very much <img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"></p>

---
