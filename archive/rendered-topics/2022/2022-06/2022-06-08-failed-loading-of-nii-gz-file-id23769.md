# Failed loading of nii.gz file

**Topic ID**: 23769
**Date**: 2022-06-08
**URL**: https://discourse.slicer.org/t/failed-loading-of-nii-gz-file/23769

---

## Post #1 by @James_Goldfarb (2022-06-08 14:43 UTC)

<p>Having trouble loading a CT series after conversion from dicom to nii.gz . with dicom2nifti.convert_directory()</p>
<p>ITKsnap loads the nii.gz file without error.<br>
Original dicom files are read by 3dslicer without error.<br>
Other series (calcium score, peripheral angio, etc) load ok in 3dslicer.</p>
<p>This is a multiphase coronary CTA .  The phases are stored separately and convert to multiple nii.gz files.  Trying to load one phase in s3dlicer at a time.</p>
<p>Any suggestions?</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz. ITK exception info: error in unknown: Could not create IO object for reading file C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz</p>
<p>Tried to create one of the following:</p>
<p>BMPImageIO</p>
<p>BioRadImageIO</p>
<p>DCMTKImageIO</p>
<p>GDCMImageIO</p>
<p>GiplImageIO</p>
<p>JPEGImageIO</p>
<p>LSMImageIO</p>
<p>MGHImageIO</p>
<p>MINCImageIO</p>
<p>MRCImageIO</p>
<p>MetaImageIO</p>
<p>NiftiImageIO</p>
<p>NrrdImageIO</p>
<p>PNGImageIO</p>
<p>ScancoImageIO</p>
<p>StimulateImageIO</p>
<p>TIFFImageIO</p>
<p>VTKImageIO</p>
<p>MRMLIDImageIO</p>
<p>Bruker2dseqImageIO</p>
<p>GE4ImageIO</p>
<p>GE5ImageIO</p>
<p>HDF5ImageIO</p>
<p>JPEG2000ImageIO</p>
<p>You probably failed to set a file suffix, or</p>
<p>set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(000002979E13F090) returned failure for request: vtkInformation (000002979F7A1390)</p>
<p>Debug: Off</p>
<p>Modified Time: 261172</p>
<p>Reference Count: 1</p>
<p>Registered Events: (none)</p>
<p>Request: REQUEST_INFORMATION</p>
<p>FORWARD_DIRECTION: 0</p>
<p>ALGORITHM_AFTER_FORWARD: 1</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz. ITK exception info: error in unknown: Could not create IO object for reading file C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz</p>
<p>Tried to create one of the following:</p>
<p>BMPImageIO</p>
<p>BioRadImageIO</p>
<p>DCMTKImageIO</p>
<p>GDCMImageIO</p>
<p>GiplImageIO</p>
<p>JPEGImageIO</p>
<p>LSMImageIO</p>
<p>MGHImageIO</p>
<p>MINCImageIO</p>
<p>MRCImageIO</p>
<p>MetaImageIO</p>
<p>NiftiImageIO</p>
<p>NrrdImageIO</p>
<p>PNGImageIO</p>
<p>ScancoImageIO</p>
<p>StimulateImageIO</p>
<p>TIFFImageIO</p>
<p>VTKImageIO</p>
<p>MRMLIDImageIO</p>
<p>Bruker2dseqImageIO</p>
<p>GE4ImageIO</p>
<p>GE5ImageIO</p>
<p>HDF5ImageIO</p>
<p>JPEG2000ImageIO</p>
<p>You probably failed to set a file suffix, or</p>
<p>set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(000002979E140710) returned failure for request: vtkInformation (000002979F7A19D0)</p>
<p>Debug: Off</p>
<p>Modified Time: 262686</p>
<p>Reference Count: 1</p>
<p>Registered Events: (none)</p>
<p>Request: REQUEST_INFORMATION</p>
<p>FORWARD_DIRECTION: 0</p>
<p>ALGORITHM_AFTER_FORWARD: 1</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz. ITK exception info: error in unknown: Could not create IO object for reading file C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz</p>
<p>Tried to create one of the following:</p>
<p>BMPImageIO</p>
<p>BioRadImageIO</p>
<p>DCMTKImageIO</p>
<p>GDCMImageIO</p>
<p>GiplImageIO</p>
<p>JPEGImageIO</p>
<p>LSMImageIO</p>
<p>MGHImageIO</p>
<p>MINCImageIO</p>
<p>MRCImageIO</p>
<p>MetaImageIO</p>
<p>NiftiImageIO</p>
<p>NrrdImageIO</p>
<p>PNGImageIO</p>
<p>ScancoImageIO</p>
<p>StimulateImageIO</p>
<p>TIFFImageIO</p>
<p>VTKImageIO</p>
<p>MRMLIDImageIO</p>
<p>Bruker2dseqImageIO</p>
<p>GE4ImageIO</p>
<p>GE5ImageIO</p>
<p>HDF5ImageIO</p>
<p>JPEG2000ImageIO</p>
<p>You probably failed to set a file suffix, or</p>
<p>set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeImageSeriesVectorReaderFile(000002979E143B90) returned failure for request: vtkInformation (000002979F7A27E0)</p>
<p>Debug: Off</p>
<p>Modified Time: 262793</p>
<p>Reference Count: 1</p>
<p>Registered Events: (none)</p>
<p>Request: REQUEST_INFORMATION</p>
<p>FORWARD_DIRECTION: 0</p>
<p>ALGORITHM_AFTER_FORWARD: 1</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz. ITK exception info: error in unknown: Could not create IO object for reading file C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz</p>
<p>Tried to create one of the following:</p>
<p>BMPImageIO</p>
<p>BioRadImageIO</p>
<p>DCMTKImageIO</p>
<p>GDCMImageIO</p>
<p>GiplImageIO</p>
<p>JPEGImageIO</p>
<p>LSMImageIO</p>
<p>MGHImageIO</p>
<p>MINCImageIO</p>
<p>MRCImageIO</p>
<p>MetaImageIO</p>
<p>NiftiImageIO</p>
<p>NrrdImageIO</p>
<p>PNGImageIO</p>
<p>ScancoImageIO</p>
<p>StimulateImageIO</p>
<p>TIFFImageIO</p>
<p>VTKImageIO</p>
<p>MRMLIDImageIO</p>
<p>Bruker2dseqImageIO</p>
<p>GE4ImageIO</p>
<p>GE5ImageIO</p>
<p>HDF5ImageIO</p>
<p>JPEG2000ImageIO</p>
<p>You probably failed to set a file suffix, or</p>
<p>set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(000002979E140710) returned failure for request: vtkInformation (000002979F7A5CB0)</p>
<p>Debug: Off</p>
<p>Modified Time: 263602</p>
<p>Reference Count: 1</p>
<p>Registered Events: (none)</p>
<p>Request: REQUEST_INFORMATION</p>
<p>FORWARD_DIRECTION: 0</p>
<p>ALGORITHM_AFTER_FORWARD: 1</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node 22_half_10_073s_cardiac_05_ce (vtkMRMLMultiVolumeNode1) from filename=‘C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz’</p>
<p>ReadData: This is not a nrrd file</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node 22_half_10_073s_cardiac_05_ce (vtkMRMLDiffusionWeightedVolumeNode1) from filename=‘C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz’</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type DiffusionTensorVolume [fullName = C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz [reader 0th file name = C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz].</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node 22_half_10_073s_cardiac_05_ce (vtkMRMLDiffusionTensorVolumeNode1) from filename=‘C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz’</p>
<p>ReadData: This is not a nrrd file</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node 22_half_10_073s_cardiac_05_ce (vtkMRMLVectorVolumeNode1) from filename=‘C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz’</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node 22_half_10_073s_cardiac_05_ce (vtkMRMLVectorVolumeNode2) from filename=‘C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz’</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type Volume [fullName = C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz [reader 0th file name = C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz].</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node 22_half_10_073s_cardiac_05_ce (vtkMRMLScalarVolumeNode1) from filename=‘C:/Users/dir/patient_nii_interop/22_half_10_073s_cardiac_05_ce.nii.gz’</p>

---

## Post #2 by @lassoan (2022-06-10 14:52 UTC)

<p>Loading of 4D images from NIFTI file format is not supported. You can load 4D images directly from DICOM or from NRRD. You can create 4D NRRD images by saving in Slicer or by using recent versions of dcm2niix.</p>
<p>NIFTI is not a general-purpose file format. It is developed for brain imaging and it is good for that, but there are many issues and limitations for using it for other type of images. I would not recommend using it for storing cardiac images.</p>

---
