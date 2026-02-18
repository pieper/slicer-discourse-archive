# More efficient resampling

**Topic ID**: 19661
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/more-efficient-resampling/19661

---

## Post #1 by @park (2021-09-14 10:35 UTC)

<p>Hi all,</p>
<p>I would like to make some function which perform real-time resampling depending on the transform matrix</p>
<p>I used simple itk resample function, however, this one quite slow (e.g, 1~2 s for one interpolation)</p>
<p>Is there more effcieint way to perform the resample ?<br>
Below, this is my cord</p>
<pre><code class="lang-auto"> # Create a new transform
    transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", "MyTransform")
    transNode.SetAndObserveTransformNodeID(transformNode.GetID())

    # Callback function that will be called each time the transform is modified

    def onMyTransformModified(caller, event):
      transformMatrix = vtk.vtkMatrix4x4()
      caller.GetMatrixTransformToWorld(transformMatrix)
      transformMatrix.Invert()
      matrix_arr = []
      translate_arr = []
      for i in range(0, 3):
        for j in range(0, 3):
          matrix_arr.append(transformMatrix.GetElement(i, j))
        translate_arr.append(transformMatrix.GetElement(i, 3))

      rigid_euler = sitk.Euler3DTransform()
      rigid_euler.SetMatrix(matrix_arr)  # rotate 
      rigid_euler.SetTranslation(translate_arr)  # move to 
      interpolator = sitk.sitkCosineWindowedSinc

      default_value = 0
      resampler = sitk.ResampleImageFilter()
      resampler.SetInterpolator(interpolator)
      resampler.SetReferenceImage(reference_image)
      resampler.SetOutputPixelType(sitk.sitkFloat32)
      resampler.SetDefaultPixelValue(default_value)
      resampler.SetTransform(rigid_euler)
      resampler.SetNumberOfThreads(10)
      resample_image = resampler.Execute(excute_image)

      sitkUtils.PushVolumeToSlicer(resample_image, targetNode=transNode)

    # Add an observer that will make the callback function called each time the transform is modified
    observationTag = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, onMyTransformModified)

</code></pre>

---

## Post #2 by @lassoan (2021-09-14 16:36 UTC)

<p>A sophisticated filter, such as ITK’s windowed sinc implementation is quite slow, while you can get visually indistinguishable results with a much faster linear or cubic interpolation implemented in VTK. Transferring image between ITK and VTK (if you deep-copy the image and the image is large) and instantiating a filter each time the callback function is executed are also unnecessarily slow down things.</p>
<p>All these problems are solved if you simply use Volume Reslice Driver module (in SlicerIGT extension). It uses a fast interpolator and there is no overhead in recreating filters, unnecessary copies, etc. The resampling usually does not take more than a few ten milliseconds. Your code will be much simpler, too, as you can set up a parameter node and set the input image and transform nodes in a few lines of Python code.</p>

---
