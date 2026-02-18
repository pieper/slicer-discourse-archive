# MakeModelEffect Error. The file cannot be saved.

**Topic ID**: 7957
**Date**: 2019-08-09
**URL**: https://discourse.slicer.org/t/makemodeleffect-error-the-file-cannot-be-saved/7957

---

## Post #1 by @11127 (2019-08-09 02:39 UTC)

<p>Operating system: window10<br>
Slicer version:4.10.2<br>
Expected behavior: Save the cropped as a STL file.<br>
Actual behavior: Fail in the last step.(Model Maker)</p>
<p>Hello.<br>
I want to use this program to extract the ears from the CT as a STL file.<br>
But I keep getting errors in the last step.<br>
Here’s what I did.</p>
<p>1.Load Dicom data<br>
2.Select Modules -&gt; Volume Rendering<br>
3.Select Modules -&gt;Crop Volume(Crop only necessary)<br>
4.Select Modules -&gt;Editor<br>
ThresholdEffect(Select right external ear)<br>
MakeModelEffect</p>
<p>But, failed to apply last step continuously.<br>
This is error massage.</p>

Model Maker standard error:
<p>Model scene file doesn’t exist yet: C:/Users/??/AppData/Local/Temp/Slicer/DEGI_AAAAACDCEECDBBHA.mrml<br>
Error: no model hierarchy node at ID “vtkMRMLModelHierarchyNode1”, creating one<br>
ERROR: cannot open input volume file C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLLabelMapVolumeNodeB.nrrd</p>
<p>Model Maker completed with errors</p>

Model Maker command line: 
<p>C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/cli-modules/ModelMaker.exe --color C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLColorTableNodeFileGenericAnatomyColors.txt.ctbl --modelSceneFile C:/Users/??/AppData/Local/Temp/Slicer/DEGI_AAAAACDCEECDDDHA.mrml#vtkMRMLModelHierarchyNode1 --name right middle ear test --labels 136 --start -1 --end -1 --skipUnNamed --smooth 10 --filtertype Sinc --decimate 0.25 --splitnormals --pointnormals --pad C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLLabelMapVolumeNodeB.nrrd</p>

ERROR writing file C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLLabelMapVolumeNodeB.nrrd
<p>Write: Could not open file C:/Users/??/AppData/Local/Temp/Slicer/DEGI_AAAAACDCEECDBBHA.mrml</p>

itk::ExceptionObject (00000062F26FB830)
Location: "unknown" 
File: D:\D\S\Slicer-4102-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx
Line: 1123
Description: itk::ERROR: NrrdImageIO(0000023C29B78800): Write: Error writing C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLLabelMapVolumeNodeB.nrrd:
[nrrd] nrrdSave: couldn't fopen("C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLLabelMapVolumeNodeB.nrrd","wb"): Invalid argument

WriteData: unable to open file C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLColorTableNodeFileGenericAnatomyColors.txt.ctbl for writing
<p>ERROR writing file C:/Users/??/AppData/Local/Temp/Slicer/DEGI_vtkMRMLColorTableNodeFileGenericAnatomyColors.txt.ctbl</p>
<p>UpdateFileList: Failed to create directoryC:/Users/??/AppData/Local/Temp/Slicer/TempWriteDEGI_vtkMRMLLabelMapVolumeNodeB</p>

Found CommandLine Module, target is  C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/cli-modules/ModelMaker.exe
ModuleType: CommandLineModule
<p>What should i do? Please help me.</p>

---

## Post #2 by @pieper (2019-08-09 20:55 UTC)

<p>Hi <a class="mention" href="/u/11127">@11127</a> -</p>
<p>It looks like your login name is not ascii (and <a href="https://discourse.slicer.org/t/special-characters/5398">alas Slicer can’t handle that</a>).  You should be able to manually change the temp directory in the Edit-&gt;Application Settings dialog to someplace with only English characters.</p>
<p>Also, you can update to using the <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Segmentation" rel="nofollow noopener">Segment Editor</a> and you’ll have a better set of tools and more STL export options.</p>
<p>Best,<br>
Steve</p>

---
