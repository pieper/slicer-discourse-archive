# Newbie question on using filters and access imagedata

**Topic ID**: 3978
**Date**: 2018-09-03
**URL**: https://discourse.slicer.org/t/newbie-question-on-using-filters-and-access-imagedata/3978

---

## Post #1 by @Niels (2018-09-03 19:49 UTC)

<p>Hi all,</p>
<p>I am working on a module for exporting image data from slicer to a format for our medical simulation systems. I have started with a simple python module for thresholding, scaling and normalizing the data (0 – 1) and writing them to a file format our simulation system can read. Getting the image data and writing them to file seems straight forward.</p>
<p>But for me it is not clear how to change the actual image data and get the values for writing them to an output file. I see people using vtk filters to change the displayed views, but they do not change the actual image data.</p>
<p>My code looks somewhat like this:</p>
<pre>
# getimage dimentions and spacing
imageData = inVolumeData.GetImageData()
imageDimention = imageData.GetDimensions()
scalarRange = imageData.GetScalarRange();
imageSpaceing = inVolumeData.GetSpacing()

# filter, let use existing filters and not make my own
shiftScale = vtk.vtkImageShiftScale()
shiftScale.SetInputData( imageData )
shiftScale.SetShift(3000)
shiftScale.SetScale(0.07)
shiftScale.SetOutputScalarTypeToUnsignedChar()
### how to get the raw data values for output the file?
### and update the slicer views?
</pre>

---

## Post #2 by @lassoan (2018-09-03 20:18 UTC)

<p>You can do it quite easily using numpy: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume</a></p>
<p>However, I would strongly suggest <em>not</em> to rescale actual voxel values only for display: voxel values may have physical meaning (Hounsfield unit, etc) that you would lose by “normalizing” them; it may also increase  storage requirements by a factor of 4-8x if you rescale to 0-1 range, because you need to use float or double data type; you may need to implement rescaling in the end-user software anyway, as window/level often need to be adjusted depending on the specific task and user preference. There are several more reasons.</p>

---

## Post #3 by @Niels (2018-09-25 13:41 UTC)

<p>Hi lassoan,</p>
<p>Thanks for your answer, I got it to work!</p>

---
