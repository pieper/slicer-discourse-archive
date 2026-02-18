# Extract point data from label map in CLI module

**Topic ID**: 405
**Date**: 2017-05-30
**URL**: https://discourse.slicer.org/t/extract-point-data-from-label-map-in-cli-module/405

---

## Post #1 by @DanC (2017-05-30 21:27 UTC)

<p>Hi all.<br>
I would like to extract the point data from a 3d label map in a CLI module.<br>
Seems I could save to nrrd -&gt; open with itkreader -&gt; iterate over voxels and find filled voxels.<br>
Is there a way to directly get the data as an array?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-05-30 23:12 UTC)

<p>Image is read into an ITK image, so the cleanest and most reusable solution is to implement your processing as in ITK filter.</p>
<p>If for any reason you decide to work outside ITK, then you have to export the image to a raw buffer, process it, and import it back into an ITK image. Details are described in the <a href="https://itk.org/ItkSoftwareGuide.pdf">ITK Software Guide</a> and  <a href="https://stackoverflow.com/questions/26296870/writing-itk-insight-toolkit-results-to-local-buffer">here</a>.</p>

---

## Post #3 by @DanC (2017-05-31 22:13 UTC)

<p>Thanks Andras.<br>
I was able to save it into an ITK image.<br>
Now I am trying to apply filters and save it back to nrrd file format using the following but the saved file will load in slicer, but is a blank image. Is there an additional step I should take? Thanks!</p>
<pre><code>typedef  itk::ImageFileWriter&lt;OriginalImageType&gt; WriterType;
WriterType::Pointer writer = WriterType::New();
writer-&gt;SetImageIO(itk::NrrdImageIO::New());</code></pre>

---

## Post #4 by @lassoan (2017-06-02 14:22 UTC)

<p>You can check it out with other viewers (ITK Snap, ImageJ, etc), but most likely then the image is actually empty. For further help, you need to either share some sample images (make sure no patient-identifiable information is included) or part of the source code that generates and write the image.</p>

---

## Post #5 by @DanC (2017-06-02 21:21 UTC)

<pre><code>// declare the image class
typedef itk::Image&lt;float, 3&gt;                      OriginalImageType;

//// Do -Read in label map
typedef itk::ImageFileReader&lt;OriginalImageType&gt; itkReaderType;
itkReaderType::Pointer itkreader = itkReaderType::New();
itkreader-&gt;SetFileName("label.nrrd");
itkreader-&gt;Update();

OriginalImageType::Pointer outImage = itkreader-&gt;GetOutput();

typedef  itk::ImageFileWriter&lt;OriginalImageType&gt; WriterType;
WriterType::Pointer writer = WriterType::New();
writer-&gt;SetImageIO(itk::NrrdImageIO::New());
writer-&gt;SetFileName("output.nrrd");
writer-&gt;SetInput(outImage);
writer-&gt;Update();</code></pre>

---

## Post #6 by @lassoan (2017-06-02 21:42 UTC)

<p>I don’t see any obvious problem in the code. Can you send an example output image? (through dropbox or similar service)</p>

---

## Post #7 by @DanC (2017-06-02 21:53 UTC)

<p>My bad. I stripped down the code, and it seems that the IO part is working without a problem. This is the full code. Seems I am doing something wrong with the resample filter.</p>
<pre><code>//// Read in label map
typedef itk::ImageFileReader&lt;OriginalImageType&gt; itkReaderType;
itkReaderType::Pointer itkreader = itkReaderType::New();
itkreader-&gt;SetFileName("label.nrrd");
itkreader-&gt;Update();
// resample image to reduce number of points
OriginalImageType::SizeType outputSize = itkreader-&gt;GetOutput()-&gt;GetLargestPossibleRegion().GetSize();
outputSize[0] = (int) (outputSize[0]/10);
outputSize[1] = (int) (outputSize[1]/10);

OriginalImageType::SpacingType outputSpacing = itkreader-&gt;GetOutput()-&gt;GetSpacing();
outputSpacing[0] *= 10;
outputSpacing[1] *= 10;

typedef itk::IdentityTransform&lt;double, 3&gt; TransformType;
typedef itk::ResampleImageFilter&lt;OriginalImageType, OriginalImageType&gt; ResampleImageFilterType;
ResampleImageFilterType::Pointer resample = ResampleImageFilterType::New();
resample-&gt;SetInput(itkreader-&gt;GetOutput());
resample-&gt;SetSize(outputSize);
resample-&gt;SetTransform(TransformType::New());
resample-&gt;SetOutputSpacing(outputSpacing);
resample-&gt;SetOutputOrigin(itkreader-&gt;GetOutput()-&gt;GetOrigin());
resample-&gt;UpdateLargestPossibleRegion();

OriginalImageType::Pointer outImage = resample-&gt;GetOutput();

typedef  itk::ImageFileWriter&lt;OriginalImageType&gt; WriterType;
WriterType::Pointer writer = WriterType::New();
writer-&gt;SetImageIO(itk::NrrdImageIO::New());
writer-&gt;SetFileName("output.nrrd");
writer-&gt;SetInput(outImage);
writer-&gt;Update();</code></pre>

---

## Post #8 by @Saima (2018-09-13 05:35 UTC)

<p>How to extract data from the cli results. the cli module return this but I need to get the output volume node. how to get that output volume node?</p>
<p>vtkMRMLCommandLineModuleNode (00000178FF7638D0)<br>
ID: vtkMRMLCommandLineModuleNode1<br>
ClassName: vtkMRMLCommandLineModuleNode<br>
Name: Swiss Skull Stripper<br>
Debug: false<br>
MTime: 1380510<br>
Description: (none)<br>
SingletonTag: (none)<br>
HideFromEditors: true<br>
Selectable: true<br>
Selected: false<br>
Attributes:<br>
CommandLineModule:Swiss Skull Stripper<br>
UpdateDisplay:true<br>
Status: Completed<br>
AutoRun:0<br>
AutoRunMode:17<br>
Parameter values:<br>
patientVolume = vtkMRMLScalarVolumeNode1<br>
patientOutputVolume = vtkMRMLScalarVolumeNode4<br>
patientMaskLabel = vtkMRMLLabelMapVolumeNode2<br>
atlasMRIVolume = vtkMRMLScalarVolumeNode2<br>
atlasMaskVolume = vtkMRMLScalarVolumeNode3</p>
<p>I tried:<br>
cliResult.GetParameterValue(1,0)  this gives only value<br>
I thought of this then<br>
scene = cliResult.GetScene()<br>
n = scene.GetNodes()<br>
I was thinking of passing the parameter value to get the node by calling n.getnode because it has collection of vtk elements but this isnt working.</p>
<p>Dont know what to do to access the volume created by the module</p>

---

## Post #9 by @lassoan (2018-09-13 05:44 UTC)

<aside class="quote no-group" data-username="Saima" data-post="8" data-topic="405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I need to get the output volume node</p>
</blockquote>
</aside>
<p>You specify the patient output volume as an input for the CommandLineModule node, so you know which volume it is (in your example above, it is vtkMRMLScalarVolumeNode4).</p>

---

## Post #10 by @Saima (2018-09-13 05:46 UTC)

<p>Hi Andras,<br>
But it will not be always scalar volume node 4. how to do it dynamically?</p>

---

## Post #11 by @lassoan (2018-09-13 17:27 UTC)

<p>You create the output volume node, so you know which one it is.</p>

---

## Post #12 by @Saima (2018-09-15 09:28 UTC)

<p>Ohhhhhhhhhhh Yes, outVolume.</p>

---
