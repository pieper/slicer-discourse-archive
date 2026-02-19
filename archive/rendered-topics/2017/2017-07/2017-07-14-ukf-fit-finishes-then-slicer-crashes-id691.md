---
topic_id: 691
title: "Ukf Fit Finishes Then Slicer Crashes"
date: 2017-07-14
url: https://discourse.slicer.org/t/691
---

# UKF fit finishes then slicer crashes

**Topic ID**: 691
**Date**: 2017-07-14
**URL**: https://discourse.slicer.org/t/ukf-fit-finishes-then-slicer-crashes/691

---

## Post #1 by @mrjeffs (2017-07-14 22:16 UTC)

<p>i ran into this error both on Ubuntu 16.04 and 14.04. UKF inputs are a 64 direction 2 shell b=2000 and 800 dwi and a whole brain mask.<br>
here is the terminal output:</p>
<pre><code class="lang-auto">toddr@uhora:~/Software/Slicer-4.7.0-2017-06-03-linux-amd64$ "Volume" Reader has successfully read the file "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr" "[3.43s]" 
Loaded volume from file: /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/sub-nbwr144_ses-1_dwi-topup_6S0_1_topdn_concat_unwarped_mean_brain_mask.nii.gz. Dimensions: 144x144x70. Number of components: 1. Pixel type: short.


"Volume" Reader has successfully read the file "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/sub-nbwr144_ses-1_dwi-topup_6S0_1_topdn_concat_unwarped_mean_brain_mask.nii.gz" "[0.11s]" 
Switch to module:  "Volumes" 
no dataArray
Switch to module:  "UKFTractography" 
Found CommandLine Module, target is  /home/toddr/.config/NA-MIC/Extensions-26072/UKFTractography/lib/Slicer-4.7/cli-modules/UKFTractography 
ModuleType: CommandLineModule 
UKF Tractography command line: 

/home/toddr/.config/NA-MIC/Extensions-26072/UKFTractography/lib/Slicer-4.7/cli-modules/UKFTractography --dwiFile /tmp/Slicer/DADJG_vtkMRMLDiffusionWeightedVolumeNodeB.nhdr --seedsFile /tmp/Slicer/DADJG_vtkMRMLLabelMapVolumeNodeB.nhdr --labels 1 --maskFile /tmp/Slicer/DADJG_vtkMRMLLabelMapVolumeNodeB.nhdr --tracts /tmp/Slicer/DADJG_vtkMRMLFiberBundleNodeB.vtp --seedsPerVoxel 1 --seedFALimit 0.18 --minFA 0.15 --minGA 0.1 --numThreads -1 --numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 250 --recordNMSE --freeWater --recordFA --recordTrace --recordFreeWater --recordTensors --Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 --minBranchingAngle 0 
 
UKF Tractography standard output:


Found 24 cores on your system.
Running tractography with 24 thread(s).

Using the 2T simple model with free water estimation. Setting the default parameters accordingly:
"*": set by user
"-": default setting
- minFA: 0.15
* seedFALimit: 0.18
- Qm: 0.001
- Ql: 50
- Rs: 0.02
* stepLength: 0.3
* recordLength: 0.9
- Qw: 0.0015
* minGA: 0.1
- seedsPerVoxel: 1
Using 2-tensor simple model with free water estimation.
Using constrained filter

Branching disabled

Number of non-zero gradients: 64
Number of zero gradients: 1
Permuting the axis order to: 0 1 2 3
Resizing the data to: 64 144 144 70
Computing the baseline image
Dividing the signal by baseline image
Data normalization finished!


Estimating seed tensors:
Tracing 218956 primary fibers:
branch_seeds size: 0
fiber size after postprocessibers: 109126
nmse_avg=9.51002e+15
H count = 0
 
UKF Tractography completed without errors
 
error: [/home/toddr/Software/Slicer-4.7.0-2017-06-03-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.

[1]+  Exit 1                  ./Slicer
toddr@uhora:~/Software/Slicer-4.7.0-2017-06-03-linux-amd64$
</code></pre>

---

## Post #2 by @mrjeffs (2017-07-14 22:18 UTC)

<p>and here is the bug report log file:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Session start time .......: 2017-07-13 17:30:23
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Slicer version ...........: 4.7.0-2017-06-03 (revision 26072) linux-amd64 - installed
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Operating system .........: Linux / 4.4.0-81-generic / #104-Ubuntu SMP Wed Jun 14 08:17:06 UTC 2017 - 64-bit
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Memory ...................: 128810 MB physical, 130936 MB virtual
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Xeon(R) CPU E5-2643 v4 @ 3.40GHz, 12 cores, 24 logical processors
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 13.07.2017 17:30:23 [] (unknown:0) - Additional module paths ..: /home/toddr/.config/NA-MIC/Extensions-26072/UKFTractography/lib/Slicer-4.7/cli-modules, /home/toddr/.config/NA-MIC/Extensions-26072/SlicerDMRI/lib/Slicer-4.7/cli-modules, /home/toddr/.config/NA-MIC/Extensions-26072/SlicerDMRI/lib/Slicer-4.7/qt-loadable-modules, /home/toddr/.config/NA-MIC/Extensions-26072/SlicerDMRI/lib/Slicer-4.7/qt-scripted-modules, /home/toddr/.config/NA-MIC/Extensions-26072/DTIProcess/lib/Slicer-4.7/cli-modules, /home/toddr/.config/NA-MIC/Extensions-26072/ResampleDTIlogEuclidean/lib/Slicer-4.7/cli-modules
[DEBUG][Python] 13.07.2017 17:30:30 [Python] (/home/toddr/Software/Slicer-4.7.0-2017-06-03-linux-amd64/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 13.07.2017 17:30:30 [Python] (/home/toddr/Software/Slicer-4.7.0-2017-06-03-linux-amd64/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 13.07.2017 17:30:30 [Python] (/home/toddr/Software/Slicer-4.7.0-2017-06-03-linux-amd64/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 13.07.2017 17:30:24 [] (unknown:0) - Number of registered modules: 160
[DEBUG][Qt] 13.07.2017 17:30:26 [] (unknown:0) - Number of instantiated modules: 160
[INFO][Stream] 13.07.2017 17:30:30 [] (unknown:0) - Initializing terminology mapping for map file /home/toddr/Software/Slicer-4.7.0-2017-06-03-linux-amd64/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
[INFO][Stream] 13.07.2017 17:30:30 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors
[DEBUG][Qt] 13.07.2017 17:30:30 [] (unknown:0) - Number of loaded modules: 160
[DEBUG][Qt] 13.07.2017 17:30:30 [] (unknown:0) - Switch to module:  "Welcome"
[ERROR][VTK] 13.07.2017 17:31:21 [vtkITKArchetypeDiffusionTensorImageReaderFile (0x8032e90): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0x8044100)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:559) - ReadImageInformation: Error reading /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr:
[nrrd] nrrdLoad: trouble reading "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: couldn't open the first datafile
[nrrd] nrrdIoStateDataFileIterNext: couldn't open "/media/DiskArray/shared_data/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.raw.gz" (data file 1 of 1) for reading
[ERROR][VTK] 13.07.2017 17:31:21 [vtkCompositeDataPipeline (0x8034170)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv7/Common/ExecutionModel/vtkExecutive.cxx:784) - Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(0x8032e90) returned failure for request: vtkInformation (0x8037350)
  Debug: Off
  Modified Time: 1009677
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 13.07.2017 17:31:21 [vtkITKArchetypeImageSeriesVectorReaderSeries (0x802c370): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0x8013c40)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:559) - ReadImageInformation: Error reading /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr:
[nrrd] nrrdLoad: trouble reading "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: couldn't open the first datafile
[nrrd] nrrdIoStateDataFileIterNext: couldn't open "/media/DiskArray/shared_data/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.raw.gz" (data file 1 of 1) for reading
[ERROR][VTK] 13.07.2017 17:31:21 [vtkCompositeDataPipeline (0x8030f10)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv7/Common/ExecutionModel/vtkExecutive.cxx:784) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(0x802c370) returned failure for request: vtkInformation (0x812a4a0)
  Debug: Off
  Modified Time: 1011237
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 13.07.2017 17:31:21 [vtkITKArchetypeImageSeriesVectorReaderFile (0x80354e0): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0x8005370)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:559) - ReadImageInformation: Error reading /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr:
[nrrd] nrrdLoad: trouble reading "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: couldn't open the first datafile
[nrrd] nrrdIoStateDataFileIterNext: couldn't open "/media/DiskArray/shared_data/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.raw.gz" (data file 1 of 1) for reading
[ERROR][VTK] 13.07.2017 17:31:21 [vtkCompositeDataPipeline (0x800e0b0)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv7/Common/ExecutionModel/vtkExecutive.cxx:784) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile(0x80354e0) returned failure for request: vtkInformation (0x8035300)
  Debug: Off
  Modified Time: 1011338
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 13.07.2017 17:31:21 [vtkITKArchetypeImageSeriesScalarReader (0x8021fb0): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0x80312e0)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:559) - ReadImageInformation: Error reading /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr:
[nrrd] nrrdLoad: trouble reading "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: couldn't open the first datafile
[nrrd] nrrdIoStateDataFileIterNext: couldn't open "/media/DiskArray/shared_data/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.raw.gz" (data file 1 of 1) for reading
[ERROR][VTK] 13.07.2017 17:31:21 [vtkCompositeDataPipeline (0x80181d0)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv7/Common/ExecutionModel/vtkExecutive.cxx:784) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0x8021fb0) returned failure for request: vtkInformation (0x801d900)
  Debug: Off
  Modified Time: 1012148
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 13.07.2017 17:31:21 [vtkMRMLNRRDStorageNode (0x8018330)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkMRMLNRRDStorageNode.cxx:180) - ReadData: This is not a nrrd file
[ERROR][VTK] 13.07.2017 17:31:21 [vtkMRMLVolumeArchetypeStorageNode (0x8033620)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:381) - ReadData: Unable to read DiffusionTensorVolume data from file: /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr
[ERROR][VTK] 13.07.2017 17:31:21 [vtkMRMLNRRDStorageNode (0x802b090)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkMRMLNRRDStorageNode.cxx:180) - ReadData: This is not a nrrd file
[ERROR][VTK] 13.07.2017 17:31:21 [vtkMRMLVolumeArchetypeStorageNode (0x802bc70)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:314) - ReadData: Failed to instantiate a file reader
[ERROR][VTK] 13.07.2017 17:31:21 [vtkMRMLVolumeArchetypeStorageNode (0x800df70)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:389) - ReadData: Unable to read ScalarVolume data from file: /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr
[DEBUG][Qt] 13.07.2017 17:33:17 [] (unknown:0) - "Volume" Reader has successfully read the file "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/eddy_cuda_repol_v2/sub-nbwr144_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1_newvecs.nhdr" "[3.43s]"
[INFO][VTK] 13.07.2017 17:33:42 [vtkMRMLVolumeArchetypeStorageNode (0x9ad78a0)] (/home/kitware/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:452) - Loaded volume from file: /mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/sub-nbwr144_ses-1_dwi-topup_6S0_1_topdn_concat_unwarped_mean_brain_mask.nii.gz. Dimensions: 144x144x70. Number of components: 1. Pixel type: short.
[DEBUG][Qt] 13.07.2017 17:33:42 [] (unknown:0) - "Volume" Reader has successfully read the file "/mnt/users/js/nbwr/sub-nbwr144/ses-1/dwi/sub-nbwr144_ses-1_dwi-topup_6S0_1_topdn_concat_unwarped_mean_brain_mask.nii.gz" "[0.11s]"
[DEBUG][Qt] 13.07.2017 17:33:50 [] (unknown:0) - Switch to module:  "Volumes"
[WARNING][Qt] 13.07.2017 17:34:01 [] (unknown:0) - no dataArray
[DEBUG][Qt] 13.07.2017 17:35:40 [] (unknown:0) - Switch to module:  "UKFTractography"
[DEBUG][Qt] 13.07.2017 17:36:49 [] (unknown:0) - Found CommandLine Module, target is  /home/toddr/.config/NA-MIC/Extensions-26072/UKFTractography/lib/Slicer-4.7/cli-modules/UKFTractography
[DEBUG][Qt] 13.07.2017 17:36:49 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 13.07.2017 17:36:50 [] (unknown:0) - UKF Tractography command line: 

/home/toddr/.config/NA-MIC/Extensions-26072/UKFTractography/lib/Slicer-4.7/cli-modules/UKFTractography --dwiFile /tmp/Slicer/DADJG_vtkMRMLDiffusionWeightedVolumeNodeB.nhdr --seedsFile /tmp/Slicer/DADJG_vtkMRMLLabelMapVolumeNodeB.nhdr --labels 1 --maskFile /tmp/Slicer/DADJG_vtkMRMLLabelMapVolumeNodeB.nhdr --tracts /tmp/Slicer/DADJG_vtkMRMLFiberBundleNodeB.vtp --seedsPerVoxel 1 --seedFALimit 0.18 --minFA 0.15 --minGA 0.1 --numThreads -1 --numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 250 --recordNMSE --freeWater --recordFA --recordTrace --recordFreeWater --recordTensors --Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 --minBranchingAngle 0
[DEBUG][Qt] 13.07.2017 17:59:09 [] (unknown:0) - UKF Tractography standard output:


Found 24 cores on your system.
Running tractography with 24 thread(s).

Using the 2T simple model with free water estimation. Setting the default parameters accordingly:
"*": set by user
"-": default setting
- minFA: 0.15
* seedFALimit: 0.18
- Qm: 0.001
- Ql: 50
- Rs: 0.02
* stepLength: 0.3
* recordLength: 0.9
- Qw: 0.0015
* minGA: 0.1
- seedsPerVoxel: 1
Using 2-tensor simple model with free water estimation.
Using constrained filter

Branching disabled

Number of non-zero gradients: 64
Number of zero gradients: 1
Permuting the axis order to: 0 1 2 3
Resizing the data to: 64 144 144 70
Computing the baseline image
Dividing the signal by baseline image
Data normalization finished!


Estimating seed tensors:
Tracing 218956 primary fibers:
branch_seeds size: 0
fiber size after postprocessibers: 109126
nmse_avg=9.51002e+15
H count = 0
[DEBUG][Qt] 13.07.2017 17:59:09 [] (unknown:0) - UKF Tractography completed without errors
</code></pre>

---

## Post #3 by @lassoan (2017-07-15 04:26 UTC)

<p>Could you please try enabling “Prefer executable CLIs” option in Application settings / Modules?</p>
<p>Can you reproduce this with one of the sample data sets or other publicly available data sets or can you share anonymized data?</p>

---

## Post #4 by @mrjeffs (2017-07-17 22:17 UTC)

<p>hi andras, Prefer executable CLIs was enabled for the crash dump reported. here is a dropbox link to the data run:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/l2mayfnk13pifsh/slicer_UKF_err.tar.gz?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-zip-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/l2mayfnk13pifsh/slicer_UKF_err.tar.gz?dl=0" target="_blank" rel="nofollow noopener">slicer_UKF_err.tar.gz</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>jeff</p>

---

## Post #5 by @lassoan (2017-07-18 12:47 UTC)

<p>Thanks for the data. I’ve run UKFTractography on Windows and after running for 2 hours, it had problems with writing its output (maybe I have run out of disk space). I’ll run it again on a different computer and let you know how it went.</p>
<p>I’ve noticed one potential issue: origin and spacing of the two volumes are slightly different (after 3 decimal digits). I don’t know if this is a problem for this particular module, but it may worth trying to change spacing and origin information manually to the same values (in Volumes module) and see if it makes any difference.</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Do you have any comments on this? Do you know who maintains UKFTractography? A small, unrelated issue: SlicerDMRI extension should be added as a dependency to UKFTractography.</p>

---

## Post #6 by @ljod (2017-07-18 13:04 UTC)

<p>Hi Andras thanks for looking into this. UKF is maintained by Yogesh Rathi’s group at the PNL and by the SlicerDMRI group. For testing, seeding from a small region (ROI input) can work better than seeding from the entire brain mask. This would help check if the input data is the issue, or if it is output file writing issues. It really looks like UKF worked, so the output may be an issue. For large datasets and many seeds per voxel, with many output attributes saved, the output can reach 5GB per subject.</p>

---

## Post #7 by @ihnorton (2017-07-18 13:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A small, unrelated issue: SlicerDMRI extension should be added as a dependency to UKFTractography.</p>
</blockquote>
</aside>
<p>SlicerDMRI lists UKF as a dependency. Are mutual dependencies allowed? If so, I can add the other way too.</p>

---

## Post #8 by @lassoan (2017-07-18 13:42 UTC)

<p>I don’t think mutual dependency is possible. If there is circular dependency then the common part should be extracted into a separate extension, or UKFTractography extension should be hidden from the extension manager (or clearly displayed as a utility extension that should not be installed by itself).</p>

---

## Post #9 by @ihnorton (2017-07-18 13:58 UTC)

<p>I did some basic tests on small ROIs with your data and everything works as expected. So we may be hitting a de-facto size limit in some code path. I don’t know if anyone regularly runs UKF with every option checked like that so we may have avoided this by luck so far.</p>
<aside class="quote no-group quote-modified" data-username="mrjeffs" data-post="1" data-topic="691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrjeffs/48/1185_2.png" class="avatar"> mrjeffs:</div>
<blockquote>
<p>–tracts /tmp/Slicer/DADJG_vtkMRMLFiberBundleNodeB.vtp</p>
</blockquote>
</aside>
<p>Since Slicer crashed, if you have not restarted yet, then the file above may still exist – could you please check? If it exists, copy somewhere semi-permanent (<code>/tmp/</code> is wiped on reboot by most linuxes). Please let us know the file size, and try to load directly. If it is not outrageously large (say less than ~1GB), please share it and I will investigate.</p>
<p>I’ll try some tests with larger regions, but that may take a while.</p>

---

## Post #10 by @ljod (2017-07-18 15:56 UTC)

<p>Hi definitely increase the output step length to 1.8 or 2mm, so that data are only saved every 2mm along the tracts. This should decrease file size by half and improve performance for every analysis.</p>

---

## Post #11 by @mrjeffs (2017-07-18 18:11 UTC)

<p>unfortunately our lab is working at 1mm3. any chance the display bottleneck will be resolved?</p>
<p>here are the contents of /tmp/Slicer:</p>
<p>toddr@uhora:/tmp/Slicer$ ls<br>
DADJG_vtkMRMLDiffusionWeightedVolumeNodeB.raw<br>
RemoteIO<br>
Slicer_26072_20170714_151708.log<br>
DADJG_vtkMRMLLabelMapVolumeNodeB.raw<br>
Slicer_26072_20170713_173023.log<br>
Slicer_26072_20170717_150245.log</p>
<p>no sign of the DADJG_vtkMRMLFiberBundleNodeB.vtp being saved.</p>

---

## Post #12 by @ljod (2017-07-18 18:28 UTC)

<p>Hi do you mean voxels are 1mm^3? That is independent of how the tractography is saved. Tractography computation always happens at much higher than 1mm (step size is 0.2mm in UKF but that is an internal default, not changed by user). Visualization and quantitation will not appreciably change if you save points every 2mm along the tract.</p>
<p>It would be good for you to test with a smaller seed ROI to verify if the pipeline works on your computer. Next try seeding without saving any values along the tract, to see if the whole brain tractography is working. If so then check the disk space available at /tmp/Slicer. If this is limited, it could prevent saving the high res tractography with so much data stored. Note that most of the values (FA, MD) can and will be recomputed from the tensors if you measure with Slicer. The free water must be saved if that will be studied later. This all depends on your use case.</p>

---

## Post #13 by @mrjeffs (2017-07-18 20:50 UTC)

<p>understood. will do. j</p>

---

## Post #14 by @mrjeffs (2017-07-18 22:25 UTC)

<p>works at 1.8mm. file size 1.8GB compressed. thanks for your help.</p>

---

## Post #15 by @ljod (2017-07-19 00:12 UTC)

<p>You’re welcome. I’m glad it is working. FYI If you happen to be running studies with multiple subjects you can do quality control of many output tractography vtks rapidly using our whitematteranalysis tool: <a href="https://github.com/SlicerDMRI/whitematteranalysis" rel="nofollow noopener">https://github.com/SlicerDMRI/whitematteranalysis</a></p>

---
