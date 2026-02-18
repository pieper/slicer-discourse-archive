# 4D ITK image to vtkMRMLGridTransformNode

**Topic ID**: 741
**Date**: 2017-07-22
**URL**: https://discourse.slicer.org/t/4d-itk-image-to-vtkmrmlgridtransformnode/741

---

## Post #1 by @Fernando (2017-07-22 10:29 UTC)

<p>Hi all,</p>
<p>I have a displacement field “<code>field.nii</code>” that I need to convert from RAS to LPS so that I can use it in Slicer. What I’m doing now is:</p>
<ol>
<li>Read the file with SimpleITK</li>
<li>Modify the data</li>
<li>Save it</li>
<li>Load it with slicer.util.loadTransform()</li>
</ol>
<p>Is there a way to create a <code>vtkMRMLGridTransformNode</code> and set the vector data or to modify the data of the transform node directly?</p>
<p>My code:</p>
<pre><code class="lang-auto">def getRASFieldFromLPSField(self, displacementFieldPath):
    image = sitk.ReadImage(displacementFieldPath)
    arr = sitk.GetArrayFromImage(image)
    arr[..., :2] *= -1  # RAS to LPS

    # Create new image
    newImage = sitk.GetImageFromArray(arr)
    newImage.SetOrigin(image.GetOrigin())
    newImage.SetDirection(image.GetDirection())
    newImage.SetSpacing(image.GetSpacing())

    sitk.WriteImage(newImage, displacementFieldPath)
    transformNode = slicer.util.loadTransform(displacementFieldPath, returnNode=True)[1]
    return transformNode
</code></pre>
<p>Best,<br>
Fernando</p>

---

## Post #2 by @lassoan (2017-07-22 12:07 UTC)

<blockquote>
<p>I have a displacement field “field.nii”</p>
</blockquote>
<p>Where does that data come from? When Slicer saves transforms to file it is always converted to LPS. When you load a displacement field from nrrd or ITK transform file (hdf) then Slicer automatically converts to LPS. If you process data in CLI modules you typically do everything in LPS.</p>
<p>You can set displacement field in grid transform using SetDisplacementGridData method -<a href="http://www.vtk.org/doc/nightly/html/classvtkGridTransform.html" class="inline-onebox">VTK: vtkGridTransform Class Reference</a></p>
<p>Probably the easiest is to load transfrom from .nii and then modify the grid data image in place using numpy.</p>

---

## Post #3 by @Fernando (2017-07-22 12:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Where does that data come from?</p>
</blockquote>
</aside>
<p>It comes from a registration tool that saves displacement fields in RAS.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably the easiest is to load transfrom from .nii and then modify the grid data image in place using numpy.</p>
</blockquote>
</aside>
<p>What is the method to access the grid data image from the loaded <code>vtkMRMLGridTransformNode</code>?</p>

---

## Post #4 by @lassoan (2017-07-22 12:43 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>What is the method to access the grid data image from the loaded vtkMRMLGridTransformNode?</p>
</blockquote>
</aside>
<p>GetDisplacementGridData / SetDisplacementGridData</p>

---

## Post #5 by @lassoan (2017-07-22 12:49 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>It comes from a registration tool that saves displacement fields in RAS.</p>
</blockquote>
</aside>
<p>Nowadays the de facto standard in medical image computing research is to store images in LPS coordinate system when they are written to files. That registration tool should be updated accordingly. It may be difficult to update a software to change coordinate systems internally (that’s why Slicer still uses RAS internally), but it should be easy to change data export to write as LPS. Although nrrd, mha, and maybe nifty can store the used coordinate system reference as metadata, as far as I know, ITK only uses that metadata when it reads nrrd files. So, another option is to save as nrrd.</p>

---

## Post #6 by @Fernando (2017-07-22 13:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>GetDisplacementGridData / SetDisplacementGridData</p>
</blockquote>
</aside>
<p>I can’t access those methods from Python (Nightly):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; _, t = loadTransform('/tmp/transform.nii', returnNode=True)
&gt;&gt;&gt; t

(vtkCommonCorePython.vtkMRMLGridTransformNode)0x12d39d3f8
&gt;&gt;&gt; t.GetDisplacementGridData

Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'vtkCommonCorePython.vtkMRMLGridTransformNode' object has no attribute 'GetDisplacementGridData'
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Nowadays the de facto standard in medical image computing research is to store images in LPS coordinate system when they are written to files. That registration tool should be updated accordingly. It may be difficult to update a software to change coordinate systems internally (that’s why Slicer still uses RAS internally), but it should be easy to change data export to write as LPS</p>
</blockquote>
</aside>
<p>I’ll let the developers know, thanks for the information.</p>

---

## Post #7 by @lassoan (2017-07-22 14:00 UTC)

<p>You need to get the VTK transform from the transform node: <code>t.GetTransformFromParent().GetDisplacementGrid()</code></p>
<p>I think the coordinate system situation is particularly bad in .nii files (I don’t know the details, because I avoid .nii as much as possible but see for example <a href="http://slicer-users-archive.65878.n3.nabble.com/Inconsistent-header-information-of-NIfTI-files-when-converted-to-nrrd-and-back-to-nifti-using-slicer-td4030959.html">this discussion thread</a>). So, it may not be possible to simply use LPS in nifty.</p>
<p>Option A. Everything works very reliably in nrrd, so you could use that file format.</p>
<p>Option B. Try to clean up the coordinate system mess in nifti. It should be started at the lowest level, making sure ITK can read/write nifti files consistently (e.g., make sure the data is converted to LPS upon loading, based on information stored in the header; make sure the used coordinate system is stored in the image header of the written files). Once that is cleaned up, Slicer would probably work correctly.</p>

---

## Post #8 by @emckenzi123 (2019-12-20 04:16 UTC)

<p>I was looking for how to load my own numpy-based transform into a Slicer Grid Transform, and found that this was the closest post on here.  After getting something to work, I thought I’d share my example code below.</p>
<ul>
<li>You may have to change your directionmatrix to account for differences in coordinates systems (as discussed in other posts on this topic).</li>
<li>The warpfile is a .npy file holding a numpy array with my transform.  This had shape (256, 256, 256, 3) for me.</li>
<li>All my volumes were 256x256x256, so its hardcoded in, but you should change it according to your needs.</li>
</ul>
<p>I hope this is helpful for others and will save them the time I spent figuring this out.  Also, please feel free to offer corrections if you notice something odd.  I’m just beginning to code in Slicer, so there is probably a better way to go about this.</p>
<p>Cheers</p>
<pre><code class="lang-python">import numpy as np
import vtk.util.numpy_support

def loadCustomTransform(warpfile):
    #create a blank Grid Transform to load into
    warpnode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLGridTransformNode')
    transformGrid = warpnode.GetTransformFromParent()
    displacementGrid = transformGrid.GetDisplacementGrid()
    displacementGrid.SetDimensions((256,256,256))
    directionmatrix = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
    directionVTKmatrix = createVTK4x4matrix(directionmatrix)
    transformGrid.SetGridDirectionMatrix(directionVTKmatrix)

    #load a numpy file holding your deformation vector field.  
    #This had shape (256, 256, 256, 3) for me
    warpdata = np.load(warpfile)
    
    #process your numpy file so that it works for Slicer
    warpdata_reshaped = warpdata.reshape((256*256*256, 3))
    vtkwarpdata = vtk.util.numpy_support.numpy_to_vtk(warpdata_reshaped)

    #Plug in your own deformation vector field and Voila!
    #The warpnode now has your custom data
    displacementGrid.GetPointData().SetScalars(vtkwarpdata)
    transformGrid.SetDisplacementGridData(displacementGrid)
    warpnode.SetAndObserveTransformFromParent(transformGrid)
    
def createVTK4x4matrix(numpyarray):
    #a helper function to change numpy arrays into 4x4 VTK matrices
    vtkmatrix = vtk.vtkMatrix4x4()
    for i in np.arange(4):
        for j in np.arange(4):
            vtkmatrix.SetElement(i,j, numpyarray[i,j])
    return vtkmatrix
</code></pre>

---

## Post #9 by @bassam.abdallah (2023-11-07 16:50 UTC)

<p><a class="mention" href="/u/emckenzi123">@emckenzi123</a> I have the exact same use-case.<br>
An external program is providing a numpy_array (LPS coordinate system) that represents a dense vector field. My goal is to load this dense vector field in Slicer for vizualisation purposes (the corresponding 3D image is already loaded).</p>
<p>Best option for me would be to write a .nrrd file and load it using the simple AddData in the GUI:</p>
<pre><code class="lang-python">import nrrd
import numpy as np

# At first, a variable 'numpy_array' is created (LPS coordinate system). 
# It contains a numpy.ndarray with the following signature:
# &gt; numpy_array.shape
#   (512, 512, 256, 3)
# &gt; numpy_array.dtype
#   dtype('float32')
# &gt; numpy_array.flags
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False

header = {
		'type': numpy_array.dtype.__str__(),
		'sizes': np.array(numpy_array.shape), 
		'dimension': len(numpy_array.shape),
		'endian': 'little',
		'encoding': 'raw',
		'space': 'right-anterior-superior',
		'space directions': [[1, 0., 0.], [0., 1, 0.], [0., 0., 1], None],
		'space origin': np.array([0, 0., 0., 0.]),
		'kinds': ['domain', 'domain', 'domain', 'vector'],
		}
nrrd.write("my_file.nrrd", numpy_array, header)
</code></pre>
<p>Slicer is not reading this when I try AddData (GUI) and importing my file as a Transform // Volume (i tried both).<br>
Among the logs I get I can find this “ReadData: This is not a nrrd file”.</p>
<p>Anyone (<a class="mention" href="/u/lassoan">@lassoan</a> if you could take a look would be awesome) with an idea of what I’m doing wrong is more than welcome.<br>
Thanks <img src="https://emoji.discourse-cdn.com/twitter/sunny.png?v=12" title=":sunny:" class="emoji" alt=":sunny:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @lassoan (2023-11-07 17:51 UTC)

<p>The file cannot be loaded because the dimension of  <code>space origin</code> is incorrect. You have 3 spatial dimensions, so <code>space origin</code> has to be set to <code>[0., 0., 0.]</code>.</p>
<p>You don’t need to specify type and size (pynrrd sets these based on the input array).</p>
<p>DICOM and most medical image computing software store files in LPS (left-posterior-superior) coordinate system, so I would recommend to use <code>left-posterior-superior</code> in <code>space</code> field. Slicer converts the vector values and the axis orientations to RAS when loading the image, so keeping RAS could make sense, too, but then you risk incompatibility with other software (that ignore the <code>space</code> field and blindly assume LPS).</p>
<p>Complete working example:</p>
<pre><code class="lang-python">import nrrd
import numpy as np

# Use a random numpy array as displacement field
displacement_field = np.random.rand(50, 40, 30, 3)

header = {
    'endian': 'little',
    'encoding': 'raw',
    'space': 'left-posterior-superior',
    'space directions': [[1, 0., 0.], [0., 1, 0.], [0., 0., 1], None],
    'space origin': np.array([0., 0., 0.]),
    'kinds': ['domain', 'domain', 'domain', 'vector'],
    }
nrrd.write("c:/tmp/my_displacement_field.nrrd", displacement_field, header)
</code></pre>

---

## Post #11 by @bassam.abdallah (2023-11-13 08:59 UTC)

<p>Thank you for the clarification sir, your example works like a charm.<br>
You made my day.</p>

---
