# Can not load any DICOM file in SLicer 3D on notebook with

**Topic ID**: 34201
**Date**: 2024-02-08
**URL**: https://discourse.slicer.org/t/can-not-load-any-dicom-file-in-slicer-3d-on-notebook-with/34201

---

## Post #1 by @alexpos1989 (2024-02-08 00:57 UTC)

<pre><code class="lang-auto">[ERROR][VTK] 08.02.2024 02:53:28 [vtkXMLDataParser (0000025E65826F80)] (vtkXMLParser.cxx:380) - Error parsing XML in stream at line 1, column 0, byte index 0: not well-formed (invalid token)
[ERROR][VTK] 08.02.2024 02:53:28 [vtkXMLMultiBlockDataReader (0000025E61EAEC80)] (vtkXMLReader.cxx:522) - Error parsing input file.  ReadXMLInformation aborting.
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLSegmentationStorageNode (0000025E6DE985A0)] (vtkMRMLSegmentationStorageNode.cxx:987) - vtkMRMLSegmentationStorageNode::ReadPolyDataRepresentation: ReadPolyDataRepresentation: Failed to read file C:/Users/Я/Downloads/Teeth_0161.nii
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLSegmentationStorageNode (0000025E6DE985A0)] (vtkMRMLSegmentationStorageNode.cxx:308) - vtkMRMLSegmentationStorageNode::ReadDataInternal: File 'C:/Users/Я/Downloads/Teeth_0161.nii' could not be read neither as labelmap nor polydata while trying to read node (vtkMRMLSegmentationStorageNode5).
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLSegmentationStorageNode (0000025E6DE985A0)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_1 (vtkMRMLSegmentationNode5) from filename='C:/Users/Я/Downloads/Teeth_0161.nii'
[ERROR][VTK] 08.02.2024 02:53:28 [vtkSlicerSegmentationsModuleLogic (0000025E6265B940)] (vtkSlicerSegmentationsModuleLogic.cxx:297) - LoadSegmentationFromFile: Error reading C:/Users/Я/Downloads/Teeth_0161.nii
[ERROR][VTK] 08.02.2024 02:53:28 [vtkITKArchetypeDiffusionTensorImageReaderFile (0000025E5F3C0B70)] (vtkITKArchetypeImageSeriesReader.cxx:723) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/Я/Downloads/Teeth_0161_0000.nii. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/Я/Downloads/Teeth_0161_0000.nii
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.
[ERROR][VTK] 08.02.2024 02:53:28 [vtkCompositeDataPipeline (0000025E6540D310)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile (0000025E5F3C0B70) returned failure for request: vtkInformation (0000025E65A2C4B0)
  Debug: Off
  Modified Time: 270581
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 08.02.2024 02:53:28 [vtkITKArchetypeImageSeriesVectorReaderSeries (0000025E5F3C4370)] (vtkITKArchetypeImageSeriesReader.cxx:723) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/Я/Downloads/Teeth_0161_0000.nii. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/Я/Downloads/Teeth_0161_0000.nii
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.
[ERROR][VTK] 08.02.2024 02:53:28 [vtkCompositeDataPipeline (0000025E64EC1B40)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0000025E5F3C4370) returned failure for request: vtkInformation (0000025E65A452D0)
  Debug: Off
  Modified Time: 272099
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 08.02.2024 02:53:28 [vtkITKArchetypeImageSeriesVectorReaderFile (0000025E5F3C2770)] (vtkITKArchetypeImageSeriesReader.cxx:723) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/Я/Downloads/Teeth_0161_0000.nii. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/Я/Downloads/Teeth_0161_0000.nii
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.
[ERROR][VTK] 08.02.2024 02:53:28 [vtkCompositeDataPipeline (0000025E64EC0940)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (0000025E5F3C2770) returned failure for request: vtkInformation (0000025E65A43F90)
  Debug: Off
  Modified Time: 272206
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 08.02.2024 02:53:28 [vtkITKArchetypeImageSeriesScalarReader (0000025E5F3C2770)] (vtkITKArchetypeImageSeriesReader.cxx:723) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/Я/Downloads/Teeth_0161_0000.nii. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/Я/Downloads/Teeth_0161_0000.nii
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    ScancoImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.
[ERROR][VTK] 08.02.2024 02:53:28 [vtkCompositeDataPipeline (0000025E64EC1B40)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesScalarReader (0000025E5F3C2770) returned failure for request: vtkInformation (0000025E65A2C9F0)
  Debug: Off
  Modified Time: 273019
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLMultiVolumeStorageNode (0000025E6DE4CF30)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_0000 (vtkMRMLMultiVolumeNode1) from filename='C:/Users/Я/Downloads/Teeth_0161_0000.nii'
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLNRRDStorageNode (0000025E6DE4CF30)] (vtkMRMLNRRDStorageNode.cxx:187) - ReadData: This is not a nrrd file
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLNRRDStorageNode (0000025E6DE4CF30)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_0000 (vtkMRMLDiffusionWeightedVolumeNode1) from filename='C:/Users/Я/Downloads/Teeth_0161_0000.nii'
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLVolumeArchetypeStorageNode (0000025E6DE9E950)] (vtkMRMLVolumeArchetypeStorageNode.cxx:412) - vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type DiffusionTensorVolume [fullName = C:/Users/Я/Downloads/Teeth_0161_0000.nii]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of C:/Users/Я/Downloads/Teeth_0161_0000.nii [reader 0th file name = C:/Users/Я/Downloads/Teeth_0161_0000.nii].
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLVolumeArchetypeStorageNode (0000025E6DE9E950)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_0000 (vtkMRMLDiffusionTensorVolumeNode1) from filename='C:/Users/Я/Downloads/Teeth_0161_0000.nii'
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLNRRDStorageNode (0000025E65384AA0)] (vtkMRMLNRRDStorageNode.cxx:187) - ReadData: This is not a nrrd file
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLNRRDStorageNode (0000025E65384AA0)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_0000 (vtkMRMLVectorVolumeNode1) from filename='C:/Users/Я/Downloads/Teeth_0161_0000.nii'
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLVolumeArchetypeStorageNode (0000025E6DE9E950)] (vtkMRMLVolumeArchetypeStorageNode.cxx:352) - vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLVolumeArchetypeStorageNode (0000025E6DE9E950)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_0000 (vtkMRMLVectorVolumeNode2) from filename='C:/Users/Я/Downloads/Teeth_0161_0000.nii'
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLVolumeArchetypeStorageNode (0000025E6DE9E950)] (vtkMRMLVolumeArchetypeStorageNode.cxx:412) - vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type Volume [fullName = C:/Users/Я/Downloads/Teeth_0161_0000.nii]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of C:/Users/Я/Downloads/Teeth_0161_0000.nii [reader 0th file name = C:/Users/Я/Downloads/Teeth_0161_0000.nii].
[ERROR][VTK] 08.02.2024 02:53:28 [vtkMRMLVolumeArchetypeStorageNode (0000025E6DE9E950)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node Teeth_0161_0000 (vtkMRMLScalarVolumeNode1) from filename='C:/Users/Я/Downloads/Teeth_0161_0000.nii'
[WARNING][Qt] 08.02.2024 02:53:28 [] (unknown:0) - void __cdecl qSlicerIOManager::showLoadNodesResultDialog(bool,class vtkMRMLMessageCollection *) Errors occurred while loading nodes: "- Error: Loading C:/Users/Я/Downloads/Teeth_0161.nii -  load failed.\n\n--------\n\n- Error: Loading C:/Users/Я/Downloads/Teeth_0161_0000.nii -  load failed.\n"
</code></pre>

---

## Post #2 by @pieper (2024-02-08 14:53 UTC)

<p>Looks like your file claims to be a <code>.nii</code> but it’s not recognized.  Maybe it’s currupted.</p>

---

## Post #3 by @lassoan (2024-02-10 17:06 UTC)

<aside class="quote no-group" data-username="alexpos1989" data-post="1" data-topic="34201">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alexpos1989/48/69275_2.png" class="avatar"> alexpos1989:</div>
<blockquote>
<p><code>C:/Users/Я/Downloads/</code></p>
</blockquote>
</aside>
<p>Maybe also try to load the data from a folder that only have ASCII characters in its name.</p>

---
