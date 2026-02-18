# Issue during loading sequence of jpg files

**Topic ID**: 5969
**Date**: 2019-02-28
**URL**: https://discourse.slicer.org/t/issue-during-loading-sequence-of-jpg-files/5969

---

## Post #1 by @fhk (2019-02-28 15:10 UTC)

<p>Hi, I’m trying to load sequence of jpg files using this guide: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>
<p>Unfortunately nothing shows up in data module. Naming convention is: Transverse_00001.jpg (number of leading 0’s decreases as image index increases eg. Transverse_00001.jpg, Transverse_00010.jpg and so on.)</p>
<p>I launched slicer in verbose mode. Here is log:</p>
<pre><code class="lang-auto">Exception from vtkITK MegaMacro: 
itk::InvalidRequestedRegionError (0x51bf4d0)
Location: "unknown" 
File: /work/Preview/Slicer-0-build/ITKv4/Modules/IO/ImageBase/include/itkImageFileReader.hxx
Line: 350
Description: ImageIO returns IO region that does not fully contain the requested regionRequested region: ImageRegion (0x7ffc70063b40)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [708, 759, 1]
StreamableRegion region: ImageRegion (0x7ffc70063b00)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [623, 708, 1]






Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(0x47ffd40) returned failure for request: vtkInformation (0x53523e0)
  Debug: Off
  Modified Time: 420830
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_DATA
  FROM_OUTPUT_PORT: 0
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




UpdateFromSeries: Unsupported number of components: 1 != 3


ReadData: This is not a nrrd file


ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = /home/maciek/VHP2/Transverse_00000.jpg]
	Number of files listed in the node = 0.
	File reader says it was able to read 768 files.
	File reader used the archetype file name of /home/maciek/VHP2/Transverse_00000.jpg [reader 0th file name = /home/maciek/VHP2/Transverse_00000.jpg]
FileFormatError



ReadData: This is not a nrrd file


ReadData: Cannot read file as a volume of type VectorVolume[fullName = /home/maciek/VHP2/Transverse_00000.jpg]
	Number of files listed in the node = 0.
	File reader says it was able to read 768 files.
	File reader used the archetype file name of /home/maciek/VHP2/Transverse_00000.jpg [reader 0th file name = /home/maciek/VHP2/Transverse_00000.jpg]
FileFormatError



ReadData: Cannot read file as a volume of type Volume[fullName = /home/maciek/VHP2/Transverse_00000.jpg]
	Number of files listed in the node = 0.
	File reader says it was able to read 768 files.
	File reader used the archetype file name of /home/maciek/VHP2/Transverse_00000.jpg [reader 0th file name = /home/maciek/VHP2/Transverse_00000.jpg]
FileFormatError</code></pre>

---

## Post #2 by @lassoan (2019-02-28 15:11 UTC)

<p>All the images must have the same size (number of rows and columns).</p>

---

## Post #3 by @fhk (2019-02-28 15:31 UTC)

<p>Thank you so much. It was the case.</p>

---
