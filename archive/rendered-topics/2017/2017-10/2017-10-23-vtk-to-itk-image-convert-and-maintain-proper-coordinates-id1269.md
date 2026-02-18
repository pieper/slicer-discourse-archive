# VTK to ITK Image convert and maintain proper coordinates

**Topic ID**: 1269
**Date**: 2017-10-23
**URL**: https://discourse.slicer.org/t/vtk-to-itk-image-convert-and-maintain-proper-coordinates/1269

---

## Post #1 by @danielbr (2017-10-23 18:59 UTC)

<p>Working on writing a command line module for 3D slicer in C++.  I am trying to convert a VTK image to an ITK image and maintain the proper coordinate systems so the images line up in 3D space.  Having a slight issue that I was hoping someone could help me with.  Let me outline it below:</p>
<p>First I read in a DICOM set using vtkDICOMImageReader as follows:</p>
<pre><code>std::string dicomFolder = "D:/images";
vtkSmartPointer&lt;vtkImageData&gt; imageVTK = vtkSmartPointer&lt;vtkImageData&gt;::New();
vtkSmartPointer&lt;vtkDICOMImageReader&gt; DICOMreader = vtkSmartPointer&lt;vtkDICOMImageReader&gt;::New();
DICOMreader-&gt;SetDirectoryName(dicomFolder.c_str());
DICOMreader-&gt;Update();
imageVTK = DICOMreader-&gt;GetOutput();
</code></pre>
<p>Now that I have the VTK imagedata I use VTKImageToImageFilter to flip it to ITK as follows:</p>
<pre><code>typedef itk::VTKImageToImageFilter&lt; ImageType &gt; itkToVTKFilterType;
itkToVTKFilterType::Pointer itkToVtkFilter = itkToVTKFilterType::New();
itkToVtkFilter-&gt;SetInput(imageVTK);
itkToVtkFilter-&gt;Update();
ImageType::Pointer imageITK = itkToVtkFilter-&gt;GetOutput();
</code></pre>
<p>Now I have the image as an itk::image.  If I look at the image data, the image is flipped along Y and Z.  I believe this is because of the difference between what VTK and ITK define as the origin. But I am not 100% certain.  Regardless, if I flip the itkImage as follows the image data is no longer flipped:</p>
<pre><code>itk::FixedArray&lt;bool, 3&gt; flipAxes;
flipAxes[0] = false;
flipAxes[1] = true;
flipAxes[2] = true;
typedef itk::FlipImageFilter &lt;ImageType&gt; FlipImageFilterType;
FlipImageFilterType::Pointer flipFilter = FlipImageFilterType::New();
flipFilter-&gt;SetInput(imageITK);
flipFilter-&gt;SetFlipAxes(flipAxes);
imageITK = flipFilter-&gt;GetOutput();
</code></pre>
<p>At this point I realize that the spacing information has been lost during the flip.  Furthermore the origin and direction cosines need to be set from the original vtkImage.</p>
<pre><code>//set image spacing
imageITK-&gt;SetSpacing(imageVTK-&gt;GetSpacing());

//set image origin
imageITK-&gt;SetOrigin(DICOMreader-&gt;GetImagePositionPatient());

//Set the direction cosines.....
float* imageOrientationPatient;
imageOrientationPatient = DICOMreader-&gt;GetImageOrientationPatient();
VectorType xVector;
xVector[0] = imageOrientationPatient[0];
xVector[1] = imageOrientationPatient[1];
xVector[2] = imageOrientationPatient[2];
VectorType yVector;
yVector[0] = imageOrientationPatient[3];
yVector[1] = imageOrientationPatient[4];
yVector[2] = imageOrientationPatient[5];
//The Z vector needs to be calculated.  It is the cross product of the X and Y vectors.
VectorType zVector;
zVector[0] = (xVector[1] * yVector[2]) - (xVector[2] * yVector[1]);
zVector[1] = (xVector[2] * yVector[0]) - (xVector[0] * yVector[2]);
zVector[2] = (xVector[0] * yVector[1]) - (xVector[1] * yVector[0]);

InputImageType::DirectionType imageDirection;
imageDirection[0][0] = xVector[0];
imageDirection[0][1] = xVector[1];
imageDirection[0][2] = xVector[2];
imageDirection[1][0] = yVector[0];
imageDirection[1][1] = yVector[1];
imageDirection[1][2] = yVector[2];
imageDirection[2][0] = zVector[0];
imageDirection[2][1] = zVector[1];
imageDirection[2][2] = zVector[2];

imageITK-&gt;SetDirection(imageDirection);
</code></pre>
<p>Now that everything is set.  I write this image out to the disk in NRRD format.  Load it into slicer.  My origin does not match my original image.  If I call imageITK-&gt;GetOrigin() the origin is correct, but when I write it out as an NRRD file the origin gets changed.  I believe there is something I am not fully grasping with the differences between VTK and ITK, how they handle image data, how they handle coordinate systems, and how they define the origin.  I really want to make sure I fully understand these nuances.  Can anyone help me out?</p>
<p>I do realize that I could just load the images in ITK and never have the images in VTK format, but for this specific module there is a reason why I need to do it this way…</p>

---

## Post #2 by @danielbr (2017-10-23 19:28 UTC)

<p>Ok figured out the problem, but I don’t quite understand yet why.  So hopefully someone can help explain it to me.  So basically the problem is if I don’t call imageITK-&gt;UpdateOutputInformation() before I set the origin, then the origin changes.  When should I be calling imageITK-&gt;UpdateOutputInformation()?  Also, if anyone has a more straightforward way to convert from VTK to ITK and maintain the coordinate systems I would love to hear it.  It seems like there must be a better way…</p>

---

## Post #3 by @pieper (2017-10-23 19:56 UTC)

<p>If you need an itk image with orientation, wouldn’t it be simpler to use an itkImageReader?</p>

---

## Post #4 by @danielbr (2017-10-23 20:11 UTC)

<p>As I said in the end of my post…for this module, there is a reason I need to accept vtkImageData.  Its too much to get into and explain, but I need to be able to take vtkImageData as the input and perform a lot of image analysis using ITK.  Trust me, if I could just read the image data using ITK I would have done it!  Would have made it much more simple.</p>

---

## Post #6 by @jcfr (2017-10-23 21:22 UTC)

<p><a class="mention" href="/u/danielbr">@danielbr</a> Considering that VTK does <em>NOT</em> have support for direction cosines, the  <code>VTKImageToImageFilter</code> provided by <a href="https://itk.org/ITKExamples/src/Bridge/VtkGlue/index.html">ITKVtkGlue</a> can not use that information.</p>
<p>The obtained ITK images data needs to be transformed by considering the direction information from the original DICOM.</p>
<p>Other approach would be to:</p>
<ul>
<li>use <a href="https://itk.org/Doxygen/html/classitk_1_1DCMTKImageIO.html">DCMTKImageIO</a>
</li>
<li>resample the data associated with the <code>vtkImageData</code> and then use <code>VTKImageToImageFilter</code> filter</li>
</ul>
<p><strong>Bonus:</strong></p>
<p>Also as a spoiler, conversion ITK &lt;-&gt; (aka <a href="https://kitware.github.io/vtk-js/">VTK.js</a>) using the web version of these toolkits is also <a href="https://github.com/Kitware/itk-vtk-image-viewer/blob/master/src/convertItkImageToVtkImage.js">available</a> in <code>itk-vtk-image-viewer</code> and it supports VTK direction cosine.</p>
<p>Cc: <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #7 by @lassoan (2017-10-23 21:33 UTC)

<p>Slicer normally imports images and other objects (structure sets, transforms, segmentation objects, etc) from DICOM and creates ITK images in simple NRRD format, meshes, ITK transforms, … - with proper coordinate system axis directions, handling variable spacing, tilted gantry acquisitions, etc. Reimplementing these DICOM import features from scratch in a CLI does not sound like a good idea. If you describe what you would like to achieve then we can give advice the takes you closer to an optimal solution.</p>

---

## Post #8 by @siaeleni (2020-03-05 20:48 UTC)

<p>Hello,<br>
I would like to ask if you have any update on this question.<br>
The aim is to use VTKImageToImageFilter in Python in order to convert vtkImageData to vtkImage or vtkPolyData to vtkData in order to use ConstantPadImageFilter.<br>
Thanks</p>

---

## Post #9 by @lassoan (2020-03-05 23:13 UTC)

<p>In Slicer, we normally use <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK">sitkUtils</a> to convert between VTK and ITK image. We did not really have any other option because until very recently vtkImageData could not store axis directions, so we could only do lossless conversion between (ITK image) &lt;-&gt; (VTK image in a volume node).</p>
<p>You can use ConstantPadImageFilter directly on vtkImageData.</p>
<p>There is no such class as vtkImage or vtkData.</p>
<p>What is the problem that you are trying to solve? (go at least one level above “use ConstantPadImageFilter”)</p>

---
