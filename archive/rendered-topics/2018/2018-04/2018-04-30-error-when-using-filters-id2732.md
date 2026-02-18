# Error when using filters

**Topic ID**: 2732
**Date**: 2018-04-30
**URL**: https://discourse.slicer.org/t/error-when-using-filters/2732

---

## Post #1 by @FungalSlicer (2018-04-30 08:27 UTC)

<p>Hey guys,</p>
<p>maybe someone has an idea about this sort or error, which I get when using some basic image filters:</p>
<p>Median Image Filter standard error:</p>
<p>Median Image Filter standard error:</p>
<p>C:/Program Files/Slicer3D/Slicer 4.9.0-2018-04-29/lib/Slicer-4.9/cli-modules/MedianImageFilter.exe: exception caught !</p>
<p>itk::ImageFileReaderException (0000000158CFEC38)<br>
Location: “unknown”<br>
File: d:\d\p\slicer-0-build\itkv4\modules\io\imagebase\include\itkImageFileReader.hxx<br>
Line: 143<br>
Description:  Could not create IO object for reading file C:/Users/User/AppData/Local/Temp/Slicer/GGEJG_vtkMRMLScalarVolumeNodeB.nrrd<br>
The file doesn’t exist.<br>
Filename = C:/Users/User/AppData/Local/Temp/Slicer/GGEJG_vtkMRMLScalarVolumeNodeB.nrrd</p>
<p>Thank you in advance,</p>
<p>FungalSlicer</p>

---

## Post #2 by @pieper (2018-04-30 13:18 UTC)

<p>Do filters work with SampleData (e.g. MRHead) or is this specific to your data?</p>
<p>(Note: median filter and others work fine for me with a recent windows nightly).</p>

---

## Post #3 by @lassoan (2018-04-30 18:27 UTC)

<p>Make sure your temporary folder is writeable - menu: Application settings / Modules / Temporary directory.</p>
<p>Something is odd about how Slicer is installed, as the path in the error message refers to C:/Program Files/<strong>Slicer3D</strong>/Slicer 4.9.0-2018-04-29/lib/Slicer-4.9/cli-modules/MedianImageFilter.exe - while it is normally “c:\Program Files\Slicer 4.9.0-2018-04-29\lib\Slicer-4.9\cli-modules\MedianImageFilter.exe”.</p>

---

## Post #4 by @FungalSlicer (2018-05-03 11:45 UTC)

<p>thank you, that solved it  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
