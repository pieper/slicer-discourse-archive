---
topic_id: 21114
title: "Fix Size In Cropped Volume"
date: 2021-12-17
url: https://discourse.slicer.org/t/21114
---

# Fix size in cropped volume

**Topic ID**: 21114
**Date**: 2021-12-17
**URL**: https://discourse.slicer.org/t/fix-size-in-cropped-volume/21114

---

## Post #1 by @bserrano (2021-12-17 13:00 UTC)

<p>Hi,</p>
<p>I want to crop a volume with a fixed size, let’s say 400x400. As far as I know, there is no way to set the dimension of the AnnotationROI in Crop Volume module. (I can do it manually but it’s quite frustrating).</p>
<p>Is there any way to do it automatically?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @Juicy (2021-12-19 03:36 UTC)

<p>Yes, you can do this using python code. Can you describe in more detail what you want to achieve and I may be able to write you some code for you to do what you need.</p>

---

## Post #3 by @bserrano (2021-12-20 07:52 UTC)

<p>What I’m trying to do is cropping a volume with a desired size:</p>
<ul>
<li>I open my dcm volume that is 512(H)x512(W)x256(depth)</li>
<li>I want to crop it so I have a volume of (for example) 400x400x200 → I want to choose the size in advance, so I don’t need to struggle with the mouse to obtain exactly 400 pixels.</li>
</ul>
<p>It would be nice if I can place the center of the square (annotation ROI with desired size) whenever I want and then crop the volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf0b4878bee2af08fe6ab475e93a62fb2bcfe31f.jpeg" alt="imagen" data-base62-sha1="rg3mZePo18dLXb762GDGmMKt7LF" width="385" height="334"></p>
<p>If you could recommend me any type of tutorial for writing python code for slicer I would appreciate it.</p>
<p>Thanks,</p>

---

## Post #4 by @Juicy (2021-12-20 08:46 UTC)

<p>Some very quick and simple code to get you going:</p>
<p>First drop an ROI around the heart like you have shown in the picture above. Make sure the ROI is called ‘R’ (this is usually what it is called by default when you drop and ROI in) if it is called something else rename it ‘R’ in the data module. Then open the python interactor (the little blue and yellow symbol on the far right on the top toolbar). Copy and paste this code into the interactor:</p>
<pre><code class="lang-auto"># this gets the ROI node and assigns it to a variable
roiNode = slicer.util.getNode('R')
# Set the sizes you want the ROI here. Change the numbers to suit your application
radius = [400,400,200]
# This sets the ROI size to the dimensions specified above
roiNode.SetRadiusXYZ(radius)
</code></pre>
<p>This will quickly size the ROI to the exact sizes specified in the ‘radius’ list. You can also automate the cropping etc. Let me know if there is anything you would like to add to the code to make life easier.</p>
<p>In terms of learning to code in slicer (I’m still pretty noob but can do basic things). I would recommend learning some basic python to get the hang of the structure. The code is quite specific to slicer but there are heaps of examples which will give you a good start in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">script repository</a> to get the hang of the slicer commands.</p>

---

## Post #5 by @bserrano (2021-12-20 09:20 UTC)

<p>Hi, thank you so much.</p>
<p>It works but this is not the size I expected. What I did is:</p>
<ul>
<li>Open Crop Volume → input ROI → create new as ‘R’</li>
<li>Then run your code<br>
The ROI box is bigger tan expected:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31622053d0b34e8b7a514f88e1022b2199e40163.jpeg" data-download-href="/uploads/short-url/72RD69YAUijxfzpytLPxPVs81rR.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31622053d0b34e8b7a514f88e1022b2199e40163_2_690x224.jpeg" alt="imagen" data-base62-sha1="72RD69YAUijxfzpytLPxPVs81rR" width="690" height="224" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31622053d0b34e8b7a514f88e1022b2199e40163_2_690x224.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31622053d0b34e8b7a514f88e1022b2199e40163_2_1035x336.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31622053d0b34e8b7a514f88e1022b2199e40163.jpeg 2x" data-dominant-color="61627A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1364×444 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0fcc547579ea19757a8884c770e86aed1f3eb40.png" alt="imagen" data-base62-sha1="w6kvJSFS1zl2BOHTDPUFuLn7aw0" width="525" height="205"></p>

---

## Post #6 by @Juicy (2021-12-20 09:25 UTC)

<p>Actually, I just realised that the ‘radius’ is specified in millimeters (RAS coordinates) and not pixels (IJK coordinates). It may need a conversion between RAS and IJK coordinates. This just picks up the first volume in the scene. Also, I forgot that the radius measurement needs to be halved to make the size of the ROI correct. This may not be the most elegant way of doing this but this worked for me in a quick test:</p>
<pre><code class="lang-auto"># specify desired dimensions in voxels
radiusIJK = [400, 400, 200]
# assign the first volume node in the data module to a variable
volumeNode = slicer.util.getNode('vtkMRMLScalarVolumeNode1')
# assign roi node to a variable
roiNode = slicer.util.getNode('R')
# get the size of the volume voxels
spacing = volumeNode.GetSpacing()
# convert the number of pixels to measurements in mm
radiusRAS = [(radiusIJK[0]*spacing[0])/2, (radiusIJK[1]*spacing[1])/2, (radiusIJK[2]*spacing[2])/2]
# change the size of the ROI
roiNode.SetRadiusXYZ(radiusRAS)

</code></pre>

---

## Post #7 by @bserrano (2021-12-20 09:33 UTC)

<p>Now it’s perfect!</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/orange_heart.png?v=10" title=":orange_heart:" class="emoji" alt=":orange_heart:"></p>

---

## Post #8 by @Juicy (2021-12-20 21:37 UTC)

<p>Great, this should work as long as the DICOM images are true axial images, that is they are in the same plane as the CT gantry plane. If you look in the volume information area of the Volumes module, the IJK to RAS direction matrix should have only 1s and 0s in it. This means the volume is aligned with the primary axes in Slicer. Sometimes the CT operator makes reformatted reconstructions that are not quite true axial images if, for example, the patient is not sitting straight in the CT machine. If you encounter volumes generated from reformatted images that are not quite aligned with the primary axes in Slicer then we will have to make some additions to the code. Perhaps align the ROI to the volume prior to resizing it or something.</p>

---
