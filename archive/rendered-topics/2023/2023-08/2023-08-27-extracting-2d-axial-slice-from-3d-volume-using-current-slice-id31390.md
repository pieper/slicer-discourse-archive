# Extracting 2D axial slice from 3D volume using current slice view

**Topic ID**: 31390
**Date**: 2023-08-27
**URL**: https://discourse.slicer.org/t/extracting-2d-axial-slice-from-3d-volume-using-current-slice-view/31390

---

## Post #1 by @calici (2023-08-27 20:01 UTC)

<p>Hi!</p>
<p>Currently I am working on developing a custom extension.</p>
<p>One of the functionalities that I want to implement is a user can scroll in axial view and select the axial slice as the slice-of-interest. Then I want to use this slice a 2D nrrd/mha file in my algorithm.</p>
<p>I looked at the similar topics and implemented  suggested ways. The problem is that my original volume has size (512, 512 ,225) but extracted slice has size (932, 548, 1). I want it to be (512, 512, 1). How can I extract with correct shape?</p>
<p>Below you may find the code  I used  and images [1].</p>
<p>Thank you!</p>
<pre><code class="lang-auto">sliceNodeID = "vtkMRMLSliceNodeRed"

# Get image data from slice view
sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sliceLayerLogic = sliceLogic.GetBackgroundLayer()
reslice = sliceLayerLogic.GetReslice()
reslicedImage = vtk.vtkImageData()
reslicedImage.DeepCopy(reslice.GetOutput())

# Create new volume node using resliced image
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
volumeNode.SetIJKToRASMatrix(sliceNode.GetXYToRAS())
volumeNode.SetAndObserveImageData(reslicedImage)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()
slicer.util.exportNode(volumeNode, &lt;SAVE_PATH&gt;)

</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/267c6eece00da04c80f082206d1cab0a7c830199.jpeg" data-download-href="/uploads/short-url/5usJWojn9n49UihvhFftETzYEcx.jpeg?dl=1" title="Screenshot 2023-08-27 155125" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/267c6eece00da04c80f082206d1cab0a7c830199_2_690x296.jpeg" alt="Screenshot 2023-08-27 155125" data-base62-sha1="5usJWojn9n49UihvhFftETzYEcx" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/267c6eece00da04c80f082206d1cab0a7c830199_2_690x296.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/267c6eece00da04c80f082206d1cab0a7c830199_2_1035x444.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/267c6eece00da04c80f082206d1cab0a7c830199_2_1380x592.jpeg 2x" data-dominant-color="5B5A5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-27 155125</span><span class="informations">1920×826 61.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li><em>Soler, L., A. Hostettler, V. Agnus, A. Charnoz, J. Fasquel, J. Moreau, A. Osswald, M. Bouhadjar, and J. Marescaux. “<strong>3D image reconstruction for comparison of algorithm database: A patient specific anatomical and medical image database.</strong>” <em>IRCAD, Strasbourg, France, Tech. Rep</em> (2010)</em></li>
</ol>

---

## Post #2 by @pieper (2023-08-27 21:27 UTC)

<p>Assuming the data was axial (like this CT) you can just access the volume node as an array and get <code>array[k]</code> where k is the slice offset transformed to IJK space.  I f you look in the script repository you can find all the pieces pretty easily.</p>

---

## Post #3 by @calici (2023-08-28 01:42 UTC)

<p>Hi Steve,</p>
<p>Thank you very much for your answer!</p>
<p>Previously I got slice offset but could not find a way to obtain the slice itself by using that value. With your hint I got the idea.</p>
<p>I am not sure if it is an elegant solution but I am leaving my code as a reference:</p>
<pre><code class="lang-auto"># Get image data from  current axial (red) slice view
sliceNodeID = "vtkMRMLSliceNodeRed"
sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sourceVolumeNode = sliceLogic.GetBackgroundLayer().GetVolumeNode()

# Get current axial slice in RAS:
sliceOffset = sliceLogic.GetSliceOffset()

# Convert RAS to IJK:
volumeRasToIjk = vtk.vtkMatrix4x4()
sourceVolumeNode.GetRASToIJKMatrix(volumeRasToIjk)
point_VolumeRas = [0, 0, sliceOffset, 1]
point_Ijk = [0, 0, 0, 1]
volumeRasToIjk.MultiplyPoint(point_VolumeRas, point_Ijk)
point_Ijk = [ int(round(c)) for c in point_Ijk[0:3] ]

# Get slice of interest as a volume:
imageArray = slicer.util.arrayFromVolume(sourceVolumeNode)
sliceOfInterest = imageArray[point_Ijk[-1], :, :]
volumeOfInterestNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
slicer.util.updateVolumeFromArray(volumeOfInterestNode, sliceOfInterest)

#  Copy image origin, spacing and direction:
ijkToRas = vtk.vtkMatrix4x4()
sourceVolumeNode.GetIJKToRASMatrix(ijkToRas)
volumeOfInterestNode.SetIJKToRASMatrix(ijkToRas)

# Export:
slicer.util.saveNode(volumeOfInterestNode,  r"C:\extracted_slice.nrrd")
</code></pre>
<p>Best regards!</p>

---

## Post #4 by @calici (2023-08-31 03:54 UTC)

<p>New edit</p>
<p>Much shorter version if anyone is interested:</p>
<pre><code class="lang-auto">sliceNodeID = "vtkMRMLSliceNodeRed"
sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sliceOffset = sliceLogic.GetSliceOffset()

k = sliceLogic.GetSliceIndexFromOffset(sliceOffset) - 1 # -1 since 1-based
</code></pre>

---
