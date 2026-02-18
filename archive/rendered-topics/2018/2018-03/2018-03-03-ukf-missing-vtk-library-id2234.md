# Ukf missing vtk library

**Topic ID**: 2234
**Date**: 2018-03-03
**URL**: https://discourse.slicer.org/t/ukf-missing-vtk-library/2234

---

## Post #1 by @mrjeffs (2018-03-03 22:28 UTC)

<p>hi all, fyi: noticed the linux dev release date is a month behind mac/win. known issue i presume…<br>
2. loaded ukf to process some diffusion data and got error below. any ideas on fixing vtk lib issue? jeff</p>
<p>[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Session start time …: 2018-03-03 14:00:12<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Slicer version …: 4.9.0-2018-02-08 (revision 26899) linux-amd64 - installed<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Operating system …: Linux / 4.4.0-112-generic / <span class="hashtag">#135-Ubuntu</span> SMP Fri Jan 19 11:48:36 UTC 2018 - 64-bit<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Memory …: 128906 MB physical, 131036 MB virtual<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - CPU …: GenuineIntel Intel® Xeon® CPU E5-2667 v2 @ 3.30GHz, 16 cores, 32 logical processors<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 03.03.2018 14:00:12 [] (unknown:0) - Additional module paths …: /home/toddr/.config/NA-MIC/Extensions-26899/SlicerDMRI/lib/Slicer-4.9/cli-modules, /home/toddr/.config/NA-MIC/Extensions-26899/SlicerDMRI/lib/Slicer-4.9/qt-loadable-modules, /home/toddr/.config/NA-MIC/Extensions-26899/SlicerDMRI/lib/Slicer-4.9/qt-scripted-modules, /home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/cli-modules, /home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/qt-loadable-modules, /home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/qt-scripted-modules, /home/toddr/.config/NA-MIC/Extensions-26899/DTIProcess/lib/Slicer-4.9/cli-modules, /home/toddr/.config/NA-MIC/Extensions-</p>
<p>skipping here…<br>
[DEBUG][Qt] 03.03.2018 14:02:14 [] (unknown:0) - “Volume” Reader has successfully read the file “/brainstudio/data/acdc/sub-acdc112/ses-1/dwi/eddy_cuda_repol_v1/sub-acdc112_ses-1_dwi-topup_64dir-3sh-800-2000_1_topdn_unwarped_ec_mf_clamp1.nhdr” “[4.69s]”<br>
[DEBUG][Qt] 03.03.2018 14:02:36 [] (unknown:0) - Switch to module:  “DiffusionWeightedVolumeMasking”<br>
[DEBUG][Qt] 03.03.2018 14:03:02 [] (unknown:0) - Found CommandLine Module, target is  /home/toddr/.config/NA-MIC/Extensions-26899/SlicerDMRI/lib/Slicer-4.9/cli-modules/DiffusionWeightedVolumeMasking<br>
[DEBUG][Qt] 03.03.2018 14:03:02 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 03.03.2018 14:03:03 [] (unknown:0) - Diffusion Brain Masking command line:</p>
<p>/home/toddr/.config/NA-MIC/Extensions-26899/SlicerDMRI/lib/Slicer-4.9/cli-modules/DiffusionWeightedVolumeMasking --baselineBValueThreshold 100 --removeislands /tmp/Slicer/CIJIC_vtkMRMLDiffusionWeightedVolumeNodeB.nrrd /tmp/Slicer/CIJIC_vtkMRMLScalarVolumeNodeB.nrrd /tmp/Slicer/CIJIC_vtkMRMLLabelMapVolumeNodeB.nrrd<br>
[DEBUG][Qt] 03.03.2018 14:03:08 [] (unknown:0) - Diffusion Brain Masking completed without errors<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:11 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:12 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:12 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:33 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:05:33 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:13 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:13 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:14 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:14 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:14 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:14 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:14 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:14 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:15 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:15 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:15 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:15 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:16 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:16 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:16 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:16 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:16 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:16 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:17 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:17 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:17 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:17 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:17 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:17 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:18 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[ERROR][VTK] 03.03.2018 14:06:18 [vtkCompositeDataPipeline (0x6438c70)] (/home/kitware/Dashboards/Nightly/Slicer-0-build/VTKv9/Common/ExecutionModel/vtkDemandDrivenPipeline.cxx:710) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(0x5d6b0f0) has 0 connections but is not optional.<br>
[DEBUG][Qt] 03.03.2018 14:06:49 [] (unknown:0) - Found CommandLine Module, target is  /home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/cli-modules/UKFTractography<br>
[DEBUG][Qt] 03.03.2018 14:06:49 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 03.03.2018 14:06:49 [] (unknown:0) - UKF Tractography command line:</p>
<p>/home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/cli-modules/UKFTractography --dwiFile /tmp/Slicer/CIJIC_vtkMRMLDiffusionWeightedVolumeNodeB.nhdr --seedsFile /tmp/Slicer/CIJIC_vtkMRMLLabelMapVolumeNodeC.nhdr --labels 1 --maskFile /tmp/Slicer/CIJIC_vtkMRMLLabelMapVolumeNodeC.nhdr --tracts /tmp/Slicer/CIJIC_vtkMRMLFiberBundleNodeB.vtp --seedsPerVoxel 1 --seedingThreshold 0.18 --stoppingFA 0.15 --stoppingThreshold 0.1 --numThreads -1 --numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 250 --freeWater --recordFA --recordTrace --recordFreeWater --recordTensors --Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 --minBranchingAngle 0 --minGA 10000<br>
[ERROR][VTK] 03.03.2018 14:06:49 [vtkSlicerCLIModuleLogic (0x30643d0)] (/home/kitware/Dashboards/Nightly/Slicer-0/Base/QTCLI/vtkSlicerCLIModuleLogic.cxx:2056) - UKF Tractography standard error:</p>
<p>/home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/cli-modules/UKFTractography: error while loading shared libraries: libUKFBase.so: cannot open shared object file: No such file or directory<br>
[ERROR][VTK] 03.03.2018 14:06:49 [vtkSlicerCLIModuleLogic (0x30643d0)] (/home/kitware/Dashboards/Nightly/Slicer-0/Base/QTCLI/vtkSlicerCLIModuleLogic.cxx:2087) - UKF Tractography completed with errors</p>

---

## Post #2 by @jcfr (2018-03-03 22:53 UTC)

<p>Slicer Linux build will be back shortly. Thanks for your patience.</p>

---

## Post #3 by @mrjeffs (2018-03-22 18:23 UTC)

<p>hi jean christophe, i am trying to get slicer’s UKF to run from the command line and it is still giving me the same error:</p>
<pre><code class="lang-auto">/home/toddr/.config/NA-MIC/Extensions-26899/UKFTractography/lib/Slicer-4.9/cli-modules/./UKFTractography: 
error while loading shared libraries: libUKFBase.so: cannot open shared object file:  No such file or directory.
</code></pre>
<p>it runs fine in the app, just not from the command line. here is the command i tried with mostly defaults, copied out of the log file from a successful run:</p>
<pre><code class="lang-nohighlight">/home/toddr/Software/Slicer-4.9.0-2018-02-08-linux-amd64/Slicer \
--launch UKFTractography --dwiFile dwi.nhdr --seedsFile mask.nii.gz \
--labels 1 --maskFile mask.nii.gz --tracts UKF_whbr.vtk --seedsPerVoxel 1 \
--seedingThreshold 0.18 --stoppingFA 0.15 --stoppingThreshold 0.1 --numThreads -1 \
--numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 250 \
--recordNMSE --freeWater --recordFA --recordTrace --recordFreeWater --recordTensors \
--Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 \
--minBranchingAngle 0 --minGA 10000
</code></pre>
<p>is the lib file truly required if app executes without errors?<br>
jeff</p>

---

## Post #4 by @mrjeffs (2018-03-22 20:41 UTC)

<p>works with stable linux version 4.8.1 revision 26813 built 2017-12-27. only dev version 4.9.0 revision 26899 built 2018-02-09 throws missing <code>libUKFBase.so</code> error. no latest linux version to test.<br>
jeff</p>

---

## Post #5 by @ihnorton (2018-05-03 17:45 UTC)

<p>This is fixed as of today’s SlicerPreview/nightly build (Slicer 4.9.0-2018-05-02).</p>

---

## Post #6 by @mrjeffs (2018-05-03 17:48 UTC)

<p>nice. thanks. will test again. jeff</p>

---

## Post #7 by @mrjeffs (2018-05-04 00:55 UTC)

<p>tried to load extentions to the new linux dev version and it crashes right off the bat.<br>
some qformbuilder was unable to create a custom widget.<br>
<img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #8 by @pieper (2018-05-04 11:59 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> found a fix for the extension manager crash yesterday - there’s a workaround here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4544">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4544" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4544" target="_blank" rel="noopener">Unable to launch Extension Manager in Slicer-4.9.0-2018-04-19</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:03:12" data-timezone="UTC">01:03AM - 13 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:03:12" data-timezone="UTC">01:03AM - 13 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=4544). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And a more permanent fix will be coming soon:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/944">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/944" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/944" target="_blank" rel="noopener">EM global priors of sibling tissues do not sum up to one</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:34:55" data-timezone="UTC">10:34PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:34:55" data-timezone="UTC">10:34PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=944). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @mrjeffs (2018-05-04 17:05 UTC)

<p>sorry guys, none of these fixes worked for me. even tried trashing the .config/NA-MIC folder to start with fresh .ini<br>
and no love. any other ideas?</p>

---

## Post #10 by @ihnorton (2018-05-04 17:37 UTC)

<p>What linux distribution/version? Unfortunately Linux ABI compatibility is really bad. The current nightlies are built on CentOS7, which <em>I think</em> should be compatible with Ubuntu &gt;= 14.04.</p>
<p>[edit: looks like there is a related, open issue: <a href="https://issues.slicer.org/view.php?id=4476">https://issues.slicer.org/view.php?id=4476</a>]</p>

---
