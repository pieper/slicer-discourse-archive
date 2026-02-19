---
topic_id: 34825
title: "Converting A 2D Numpy Array To A Vtk Image"
date: 2024-03-11
url: https://discourse.slicer.org/t/34825
---

# Converting a 2D numpy array to a VTK image

**Topic ID**: 34825
**Date**: 2024-03-11
**URL**: https://discourse.slicer.org/t/converting-a-2d-numpy-array-to-a-vtk-image/34825

---

## Post #1 by @yaraabdelazim (2024-03-11 16:57 UTC)

<p>Hello,</p>
<p>I am trying to detect edges in a volume and therefore, I use OpenCV. After converting my slice to a numpy array and detecting the edges, I am able to display it in my Jupyter notebook. Here is the result I get:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/385e869fd7e1bfea315d95e3c745c136a3e8140c.png" alt="image" data-base62-sha1="82Fg3Z9MerBcBwGLFlQx0mTAgbi" width="544" height="246"></p>
<p>However, when I try to display this in 3D slicer, the image gets displayed on 2 different slices and the orientation isn’t right. Here’s what I mean:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f27c52df5afdb33ff3faa032c01632c69c0d589.png" alt="image" data-base62-sha1="fRkcNYFvWh3NSuNg3trcZFmt0AV" width="602" height="325"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/483efa6bba1caee322975120db4acf74aa672efa.png" alt="image" data-base62-sha1="aj7j6aBMB8PD0qgvkAiKLHfLl7s" width="609" height="326"><br>
I’m not really sure where I went wrong as I have tried to change the dimensions in multiple different ways but nothing seems to be working. Is there something that I missed to be able to fix this issue?</p>
<p>Here is my code:</p>
<pre data-code-wrap="python"><code class="lang-python">data_type = vtk.VTK_UNSIGNED_CHAR
imageSpacing = [0.1, 0.1, 0.1]
imageDirections = [[1,0,0], [0,1,0], [0,0,1]]
shape = edges.shape
print("tableau contours:", shape)
dims = volume.GetImageData().GetDimensions()
print("tableau dimensions volume:", dims)

### edges = edges[:,np.newaxis,:]
flat_data_array = edges.flatten()
vtk_data = numpy_support.numpy_to_vtk(num_array=flat_data_array, deep=True, array_type=data_type)

plt.figure()
plt.title("Résultat détection de contours")
plt.imshow(edges, cmap='gray')
plt.show()

result = vtk.vtkImageData()
result.GetPointData().SetScalars(vtk_data)
result.SetDimensions(60, 1, 512)

result.Modified()
result_volume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
result_volume.SetSpacing(imageSpacing)
result_volume.SetIJKToRASDirections(imageDirections)
result_volume.SetAndObserveImageData(result)
result_volume.CreateDefaultDisplayNodes()

slicer.util.updateVolumeFromArray(result_volume, edges)

### result_volume.SetIJKToRASDirections(imageDirections)


slicer.util.updateVolumeFromArray(result_volume, edges)
</code></pre>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2024-03-12 04:27 UTC)

<p>OpenCV is for computer vision. It is very good for image processing for computer vision but not well suited for medical image processing. For example, most OpenCV functions operate in pixel space (instead of physical space), cannot deal with arbitrarily oriented images (ignores IJKtoRAS), many functions don’t work on 3D images, and in general its developers did not think about medical image processing needs when they implemented the library.</p>
<p>Most likely you will have much simpler life and get better results if you use ITK instead. You can either use SimpleITK or ITK-Python. There is a simple example of using SimpleITK in Slicer <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk">here</a>.</p>

---

## Post #3 by @yaraabdelazim (2024-03-12 09:03 UTC)

<p>My issue with SimpleITK is tha whenever I try to execute the CannyEdgeDetectionImageFilter(), I get an error that I don’t quite understand and I don’t know where it’s coming from. Here is my error:</p>
<p>RuntimeError: Exception thrown in SimpleITK CannyEdgeDetectionImageFilter_Execute: sitk::ERROR: Pixel type: 16-bit unsigned integer is not supported in 3D by class slicer_itk::simple::CannyEdgeDetectionImageFilter.</p>

---

## Post #4 by @cpinter (2024-03-12 11:02 UTC)

<p>It seems that the scalar type of your image is not supported byu the Canny filter. You can cast it to 8 bits if it does not mean too much data loss for you.</p>
<p>The other option is to make sure the geometry of the image is preserved after the OpenCV processing. Here is some background about this<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a><br>
But basically what you’ll need is to set the numpy output to a volume that has the same geometry as the input. What I’d do is I’d clone the input volume using subject hierarchy and then use that cloned node with the <code>updateVolumeFromArray</code> method.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-node" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-node</a></p>

---

## Post #5 by @yaraabdelazim (2024-03-12 13:51 UTC)

<p>Thank you very much, that was very helpful !</p>

---
