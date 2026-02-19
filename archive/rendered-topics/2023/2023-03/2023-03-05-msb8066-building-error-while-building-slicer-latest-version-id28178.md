---
topic_id: 28178
title: "Msb8066 Building Error While Building Slicer Latest Version"
date: 2023-03-05
url: https://discourse.slicer.org/t/28178
---

# MSB8066 Building Error while building slicer latest version in Win11 22h2

**Topic ID**: 28178
**Date**: 2023-03-05
**URL**: https://discourse.slicer.org/t/msb8066-building-error-while-building-slicer-latest-version-in-win11-22h2/28178

---

## Post #1 by @f1oNae (2023-03-05 07:46 UTC)

<p>I am building slicer latest version with:<br>
CMake = 3.24.3<br>
Visual studio = 2022 , toolset v143<br>
QT = 5.15.2<br>
OS = WIindows 11 22H2<br>
git version 2.39.2.windows.1<br>
however,I meet MSB8066 error at the end of slicer building.Here it is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30c29e095d695d2b8adab705f6ea374f018a5f09.png" data-download-href="/uploads/short-url/6XlSPcNYuy1VDMirbEEOfqODHsJ.png?dl=1" title="Quicker_20230305_153552" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30c29e095d695d2b8adab705f6ea374f018a5f09_2_690x31.png" alt="Quicker_20230305_153552" data-base62-sha1="6XlSPcNYuy1VDMirbEEOfqODHsJ" width="690" height="31" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30c29e095d695d2b8adab705f6ea374f018a5f09_2_690x31.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30c29e095d695d2b8adab705f6ea374f018a5f09_2_1035x46.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30c29e095d695d2b8adab705f6ea374f018a5f09_2_1380x62.png 2x" data-dominant-color="5D9FD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Quicker_20230305_153552</span><span class="informations">2092×96 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3504e4f07d0b96b61ca27d6f955fcb1eb60a4b6.png" data-download-href="/uploads/short-url/wqUriNHPZOfXnrFQabT1cpwaTZ4.png?dl=1" title="Quicker_20230305_153410" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504e4f07d0b96b61ca27d6f955fcb1eb60a4b6_2_690x195.png" alt="Quicker_20230305_153410" data-base62-sha1="wqUriNHPZOfXnrFQabT1cpwaTZ4" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504e4f07d0b96b61ca27d6f955fcb1eb60a4b6_2_690x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504e4f07d0b96b61ca27d6f955fcb1eb60a4b6_2_1035x292.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504e4f07d0b96b61ca27d6f955fcb1eb60a4b6_2_1380x390.png 2x" data-dominant-color="F8F7FB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Quicker_20230305_153410</span><span class="informations">2100×596 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<details>
<summary>
Here is the output message </summary>
<pre><code class="lang-auto">46&gt;------ Build started: Project: Slicer, Configuration: Debug x64 ------
46&gt;Performing configure step for 'Slicer'
46&gt;loading initial cache file C:/D/S4D/Slicer-prefix/tmp/Slicer-cache-Debug.cmake
46&gt;-- Setting C++ standard
46&gt;-- Setting C++ standard - C++17
46&gt;-- Configuring Slicer organization domain [www.na-mic.org]
46&gt;-- Configuring Slicer organization name [NA-MIC]
46&gt;-- Configuring Slicer default home module [Welcome]
46&gt;-- Configuring Slicer default favorite modules [Data, Volumes, Models, Transforms, Markups, SegmentEditor]
46&gt;-- Configuring Slicer text of disclaimer at startup [Thank you for using %1!&lt;br&gt;&lt;br&gt;This software is not intended for clinical use.]
46&gt;-- Configuring Slicer requires admin account [OFF]
46&gt;-- Configuring Slicer install root [$LOCALAPPDATA/NA-MIC]
46&gt;-- Configuring Slicer release type [Experimental]
46&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:87 (message):
46&gt;  Skipping repository info extraction: directory [C:/D/S4] is not a GIT
46&gt;  checkout
46&gt;Call Stack (most recent call first):
46&gt;  CMake/SlicerVersion.cmake:55 (SlicerMacroExtractRepositoryInfo)
46&gt;  CMakeLists.txt:341 (include)
46&gt;This warning is for project developers.  Use -Wno-dev to suppress it.
46&gt;
46&gt;-- Configuring Slicer version [5.3.0-]
46&gt;-- Configuring Slicer revision [3237]
46&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:87 (message):
46&gt;  Skipping repository info extraction: directory [C:/D/S4] is not a GIT
46&gt;  checkout
46&gt;Call Stack (most recent call first):
46&gt;  CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)
46&gt;  CMakeLists.txt:341 (include)
46&gt;This warning is for project developers.  Use -Wno-dev to suppress it.
46&gt;
46&gt;-- Configuring VTK
46&gt;--   Slicer_VTK_RENDERING_BACKEND is OpenGL2
46&gt;--   Slicer_VTK_SMP_IMPLEMENTATION_TYPE is TBB
46&gt;--   Slicer_VTK_VERSION_MAJOR is 9
46&gt;-- Configuring Slicer with Qt 5.15.2 (using modules: Core, Widgets, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, Multimedia, MultimediaWidgets, WebEngine, WebEngineWidgets, WebChannel, Script, LinguistTools, )
46&gt;-- Setting QT_PLUGINS_DIR: C:/Qt/5.15.2/msvc2019_64/plugins
46&gt;-- Setting QT_BINARY_DIR: C:/Qt/5.15.2/msvc2019_64/bin
46&gt;-- Setting QT_LIBRARY_DIR: C:/Qt/5.15.2/msvc2019_64/lib
46&gt;-- Setting ExternalData_OBJECT_STORES to 'C:/D/S4D/ExternalData/Objects'
46&gt;-- Configuring Slicer for [win-amd64]
46&gt;-- Found OpenGL: opengl32  found components: OpenGL
46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
46&gt;-- Found PythonLibs: C:/D/S4D/python-install/libs/python39.lib (found suitable version "3.9.10", minimum required is "3.9")
46&gt;Traceback (most recent call last):
46&gt;  File "&lt;string&gt;", line 1, in &lt;module&gt;
46&gt;AttributeError: module 'sys' has no attribute 'abiflags'
46&gt;-- Configuring Slicer with python 3.9
46&gt;-- Configuring MRML
46&gt;--   MRML_APPLICATION_NAME is Slicer
46&gt;--   MRML_APPLICATION_VERSION is 0x050300
46&gt;--   MRML_APPLICATION_REVISION is 3237
46&gt;--   MRML_APPLICATION_SUPPORT_VERSION is 0x030000
46&gt;-- Configuring library: ITKFactoryRegistration
46&gt;-- ITK is setting ITKFactoryRegistration's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring library: vtkAddon [vtkAddon_SOURCE_DIR: C:/D/S4D/vtkAddon]
46&gt;-- Found OpenGL: opengl32
46&gt;-- Found PythonLibs: C:/D/S4D/python-install/libs/python39.lib (found version "3.9.10")
46&gt;-- Configuring library: vtkTeem
46&gt;-- Configuring library: vtkITK
46&gt;-- ITK is setting vtkITK's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring library: vtkSegmentationCore
46&gt;-- Configuring library: MRML/Core
46&gt;-- ITK is setting MRMLCore's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring library: MRML/CLI
46&gt;-- Configuring library: RemoteIO
46&gt;-- Configuring library: MRML/Logic
46&gt;-- Configuring library: MRML/DisplayableManager
46&gt;-- Configuring library: MRML/IDImageIO
46&gt;-- ITK is setting MRMLIDImageIO's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring library: MRML/Widgets
46&gt;-- Looking for decorator header qMRMLWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qMRMLWidgetsPythonQtDecorators.h - Not found
46&gt;-- ITK is setting SlicerBaseLogic's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
46&gt;-- ITK is setting qSlicerBaseQTCore's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTCore
46&gt;-- Looking for decorator header qSlicerBaseQTCorePythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerBaseQTCorePythonQtDecorators.h - Found
46&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTGUI
46&gt;-- Looking for decorator header qSlicerBaseQTGUIPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerBaseQTGUIPythonQtDecorators.h - Found
46&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTCLI
46&gt;-- Looking for decorator header qSlicerBaseQTCLIPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerBaseQTCLIPythonQtDecorators.h - Not found
46&gt;-- Configuring Slicer Qt base library: qSlicerModulesCore
46&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTApp
46&gt;-- Looking for decorator header qSlicerBaseQTAppPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerBaseQTAppPythonQtDecorators.h - Found
46&gt;-- Configuring Loadable module: Cameras [qSlicerCamerasModuleExport.h]
46&gt;-- Looking for decorator header qSlicerUnitsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerUnitsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Units [qSlicerUnitsModuleExport.h]
46&gt;-- RapidJSON found. Headers: ./include/Slicer-5.3
46&gt;-- Looking for decorator header qSlicerTerminologiesModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTerminologiesModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Terminologies [qSlicerTerminologiesModuleExport.h]
46&gt;-- Looking for decorator header qSlicerSubjectHierarchyModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerSubjectHierarchyModuleWidgetsPythonQtDecorators.h - Found
46&gt;-- Configuring Loadable module: SubjectHierarchy [qSlicerSubjectHierarchyModuleExport.h]
46&gt;-- Looking for decorator header qSlicerColorsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerColorsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerColorsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerColorsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Colors [qSlicerColorsModuleExport.h]
46&gt;-- Configuring Loadable module: Annotations [qSlicerAnnotationsModuleExport.h]
46&gt;-- Looking for decorator header qSlicerSceneViewsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerSceneViewsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: SceneViews [qSlicerSceneViewsModuleExport.h]
46&gt;-- RapidJSON found. Headers: ./include/Slicer-5.3
46&gt;-- Looking for decorator header qSlicerMarkupsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerMarkupsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerMarkupsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerMarkupsModuleWidgetsPythonQtDecorators.h - Found
46&gt;-- Configuring Loadable module: Markups [qSlicerMarkupsModuleExport.h]
46&gt;-- Looking for decorator header qSlicerTransformsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTransformsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerTransformsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTransformsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Transforms [qSlicerTransformsModuleExport.h]
46&gt;-- Configuring Loadable module: Data [qSlicerDataModuleExport.h]
46&gt;-- Looking for decorator header qSlicerModelsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerModelsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerModelsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerModelsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Models [qSlicerModelsModuleExport.h]
46&gt;-- Looking for decorator header qSlicerPlotsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerPlotsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerPlotsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerPlotsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Plots [qSlicerPlotsModuleExport.h]
46&gt;-- Looking for decorator header qSlicerSegmentationsEditorEffectsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerSegmentationsEditorEffectsPythonQtDecorators.h - Found
46&gt;-- Looking for decorator header qSlicerSegmentationsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerSegmentationsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerSegmentationsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerSegmentationsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Segmentations [qSlicerSegmentationsModuleExport.h]
46&gt;-- Looking for decorator header qSlicerSequencesModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerSequencesModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Sequences [qSlicerSequencesModuleExport.h]
46&gt;-- Configuring Loadable module: Welcome [qSlicerWelcomeModuleExport.h]
46&gt;-- Looking for decorator header qSlicerTablesSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTablesSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerTablesModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTablesModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Tables [qSlicerTablesModuleExport.h]
46&gt;-- Looking for decorator header qSlicerTextsModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTextsModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerTextsSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTextsSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Texts [qSlicerTextsModuleExport.h]
46&gt;-- Configuring Loadable module: Reformat [qSlicerReformatModuleExport.h]
46&gt;-- Configuring Loadable module: ViewControllers [qSlicerViewControllersModuleExport.h]
46&gt;-- Looking for decorator header qSlicerVolumesSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerVolumesSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerVolumesModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerVolumesModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: Volumes [qSlicerVolumesModuleExport.h]
46&gt;-- Looking for decorator header qSlicerVolumeRenderingModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerVolumeRenderingModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: VolumeRendering [qSlicerVolumeRenderingModuleExport.h]
46&gt;-- Configuring Loadable module: CropVolume [qSlicerCropVolumeModuleExport.h]
46&gt;-- Configuring Scripted module: CropVolumeSequence
46&gt;-- Configuring Scripted module: DataProbe
46&gt;-- Configuring Scripted module: ImportItkSnapLabel
46&gt;-- Configuring Scripted module: PerformanceTests
46&gt;-- Configuring Scripted module: SampleData
46&gt;-- Configuring Scripted module: ScreenCapture
46&gt;-- Configuring Scripted module: SegmentEditor
46&gt;-- Configuring Scripted module: SegmentStatistics
46&gt;-- Configuring Scripted module: SelfTests
46&gt;-- Configuring Scripted module: VectorToScalarVolume
46&gt;-- Configuring Scripted module: WebServer
46&gt;-- Configuring Scripted module: DMRIInstall
46&gt;-- Configuring Scripted module: ExtensionWizard
46&gt;-- Configuring Scripted module: Endoscopy
46&gt;-- Configuring Scripted module: DICOM
46&gt;-- Looking for decorator header qSlicerDICOMLibModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerDICOMLibModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Looking for decorator header qSlicerDICOMLibSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerDICOMLibSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Scripted module: DICOMLib
46&gt;-- Configuring Scripted module: DICOMPlugins
46&gt;-- Configuring Scripted module: DICOMPatcher
46&gt;-- Configuring SEM CLI module: ACPCTransform
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: AddScalarVolumes
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: CastScalarVolume
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: CheckerBoardFilter
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: CurvatureAnisotropicDiffusion
46&gt;-- Configuring SEM CLI module: ExecutionModelTour
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ExtractSkeleton
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: GaussianBlurImageFilter
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: GradientAnisotropicDiffusion
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: GrayscaleFillHoleImageFilter
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: GrayscaleGrindPeakImageFilter
46&gt;-- Configuring SEM CLI module: GrayscaleModelMaker
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: HistogramMatching
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ImageLabelCombine
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: LabelMapSmoothing
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: MaskScalarVolume
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: MedianImageFilter
46&gt;-- Configuring SEM CLI module: MergeModels
46&gt;-- Configuring SEM CLI module: ModelMaker
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ModelToLabelMap
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: MultiplyScalarVolumes
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: N4ITKBiasFieldCorrection
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: OrientScalarVolume
46&gt;-- Configuring SEM CLI module: ProbeVolumeWithModel
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ResampleDTIVolume
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ResampleScalarVectorDWIVolume
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: RobustStatisticsSegmenter
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: SimpleRegionGrowingSegmentation
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: SubtractScalarVolumes
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ThresholdScalarVolume
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: VotingBinaryHoleFillingImageFilter
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: CreateDICOMSeries
46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: PETStandardUptakeValueComputation
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: FiducialRegistration
46&gt;-- ITK is setting Slicer's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: ResampleScalarVolume
46&gt;-- --------------------------------------------------
46&gt;-- Configuring Slicer application library: qSlicerApp
46&gt;-- --------------------------------------------------
46&gt;-- Setting Slicer DESCRIPTION_SUMMARY to 'Medical Visualization and Processing Environment for Research'
46&gt;-- Setting Slicer DESCRIPTION_FILE to 'C:/D/S4/README.txt'
46&gt;-- --------------------------------------------------
46&gt;-- Configuring Slicer application: SlicerApp
46&gt;-- --------------------------------------------------
46&gt;-- Setting Slicer APPLICATION_NAME to 'Slicer'
46&gt;-- Setting Slicer LAUNCHER_SPLASHSCREEN_FILE to 'C:/D/S4/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png'
46&gt;-- Setting Slicer APPLE_ICON_FILE to 'C:/D/S4/Applications/SlicerApp/Resources/Slicer.icns'
46&gt;-- Setting Slicer WIN_ICON_FILE to 'C:/D/S4/Applications/SlicerApp/Resources/Slicer.ico'
46&gt;-- Setting Slicer LICENSE_FILE to 'C:/D/S4/License.txt'
46&gt;-- Setting Slicer executable name to 'SlicerApp-real.exe'
46&gt;-- Setting Slicer EXECUTABLE to 'C:/D/S4D/Slicer-build/bin/SlicerApp-real.exe'
46&gt;-- Enabling Slicer build tree launcher option: --VisualStudio
46&gt;-- Enabling Slicer build tree launcher option: --VisualStudioProject
46&gt;-- Enabling Slicer build tree launcher option: --cmd
46&gt;-- Enabling Slicer install tree launcher option: --cmd
46&gt;-- Looking for decorator header qSlicerTemplateKeyModuleWidgetsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerTemplateKeyModuleWidgetsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: TemplateKey [qSlicerTemplateKeyModuleExport.h]
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: MultiVolumeExplorer
46&gt;-- Configuring Loadable module: MultiVolumeExplorer [qSlicerMultiVolumeExplorerModuleExport.h]
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: MultiVolumeImporter
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: SimpleFilters
46&gt;-- Checking EXTENSION_NAME variable
46&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED
46&gt;-- Checking MODULE_NAME variable
46&gt;-- Checking MODULE_NAME variable - NOTDEFINED
46&gt;-- Checking PROJECT_NAME variable
46&gt;-- Checking PROJECT_NAME variable - SimpleFilters
46&gt;-- Setting EXTENSION_NAME ......................: SimpleFilters
46&gt;-- Configuring Scripted module: SimpleFilters
46&gt;-- Skipping extension packaging: SimpleFilters - Slicer_SOURCE_DIR is defined.
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: BRAINSTools
46&gt;-- BUILD_FOR_DASHBOARD: OFF
46&gt;-- BRAINSTools_BUILD_DICOM_SUPPORT: ON
46&gt;-- BRAINSTools_VERSION_MAJOR 5
46&gt;-- BRAINSTools_VERSION_MINOR 7
46&gt;-- BRAINSTools_VERSION_PATCH 0
46&gt;-- BRAINSTools_VERSION_TWEAK
46&gt;-- BRAINSTools_VERSION_RC
46&gt;-- BRAINSTools_VERSION_HASH  37b0a
46&gt;-- BRAINSTools_VERSION_POST
46&gt;-- BRAINSTools_VERSION_DEV   22
46&gt;-- Building BRAINSTools version "5.7.0..dev22-g37b0a"
46&gt;-- ITK is setting BRAINSCommonLib's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSFit
46&gt;-- Configuring SEM CLI module: PerformMetricTest
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSResample
46&gt;-- Configuring SEM CLI module: BRAINSResize
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSROIAuto
46&gt;-- ITK is setting DWIConvert's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: DWIConvert
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSDWICleanup
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSTransformConvert
46&gt;-- ITK is setting BRAINSStripRotation's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSStripRotation
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSDeface
46&gt;-- ITK is setting BRAINSTools's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: BRAINSIntensityNormalize
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: CompareVolumes
46&gt;-- Configuring Scripted module: CompareVolumes
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: LandmarkRegistration
46&gt;-- Configuring Scripted module: LandmarkRegistration
46&gt;-- --------------------------------------------------
46&gt;-- Configuring remote module: SurfaceToolbox
46&gt;-- Checking EXTENSION_NAME variable
46&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED
46&gt;-- Checking MODULE_NAME variable
46&gt;-- Checking MODULE_NAME variable - NOTDEFINED
46&gt;-- Checking PROJECT_NAME variable
46&gt;-- Checking PROJECT_NAME variable - SurfaceToolbox
46&gt;-- Setting EXTENSION_NAME ......................: SurfaceToolbox
46&gt;-- ITK is setting SurfaceToolbox's MSVC_RUNTIME_LIBRARY to dynamic
46&gt;-- Configuring SEM CLI module: Decimation
46&gt;-- Configuring Scripted module: SurfaceToolbox
46&gt;-- Looking for decorator header qSlicerDynamicModelerSubjectHierarchyPluginsPythonQtDecorators.h
46&gt;-- Looking for decorator header qSlicerDynamicModelerSubjectHierarchyPluginsPythonQtDecorators.h - Not found
46&gt;-- Configuring Loadable module: DynamicModeler [qSlicerDynamicModelerModuleExport.h]
46&gt;-- Skipping extension packaging: SurfaceToolbox - Slicer_SOURCE_DIR is defined.
46&gt;CMake Warning at Utilities/Scripts/SlicerWizard/doc/CMakeLists.txt:41 (message):
46&gt;CUSTOMBUILD : warning : sphinx-build not found: Python documentation will not be created
46&gt;
46&gt;
46&gt;-- Setting 'CTEST_MODEL' variable with default value 'Experimental'
46&gt;-- Setting 'SLICER_PACKAGE_MANAGER_CLIENT_EXECUTABLE' variable with default value 'SLICER_PACKAGE_MANAGER_CLIENT_EXECUTABLE-NOTDEFINED'
46&gt;-- Setting 'SLICER_PACKAGE_MANAGER_URL' variable with default value 'SLICER_PACKAGE_MANAGER_URL-NOTDEFINED'
46&gt;-- Setting 'SLICER_PACKAGE_MANAGER_API_KEY' variable with default value 'OBFUSCATED'
46&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:87 (message):
46&gt;  Skipping repository info extraction: directory [C:/D/S4] is not a GIT
46&gt;  checkout
46&gt;Call Stack (most recent call first):
46&gt;  CMake/SlicerPackageAndUploadTarget.cmake:105 (SlicerMacroExtractRepositoryInfo)
46&gt;  CMake/LastConfigureStep/CMakeLists.txt:41 (include)
46&gt;This warning is for project developers.  Use -Wno-dev to suppress it.
46&gt;
46&gt;CMake Error at CMake/SlicerPackageAndUploadTarget.cmake:118 (message):
46&gt;  Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined.
46&gt;Call Stack (most recent call first):
46&gt;  CMake/LastConfigureStep/CMakeLists.txt:41 (include)
46&gt;
46&gt;
46&gt;-- Configuring incomplete, errors occurred!
46&gt;See also "C:/D/S4D/Slicer-build/CMakeFiles/CMakeOutput.log".
46&gt;See also "C:/D/S4D/Slicer-build/CMakeFiles/CMakeError.log".
46&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5): error MSB8066: Custom build for 'C:\D\S4D\CMakeFiles\2842409b95e95d33933c6c3501e382b4\Slicer-configure.rule;C:\D\S4D\CMakeFiles\2842409b95e95d33933c6c3501e382b4\Slicer-build.rule;C:\D\S4D\CMakeFiles\2842409b95e95d33933c6c3501e382b4\Slicer-forceconfigure.rule;C:\D\S4D\CMakeFiles\2842409b95e95d33933c6c3501e382b4\Slicer-install.rule;C:\D\S4D\CMakeFiles\48bccb291ecb400233c5d25d04671af3\Slicer-complete.rule;C:\D\S4D\CMakeFiles\f5993a3ec64cf58c5707908b20f354e5\Slicer.rule' exited with code 1.
46&gt;Done building project "Slicer.vcxproj" -- FAILED.
</code></pre>
</details>
<p>And here is the CmakeError.log:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/f1oNae/CmakeError.log/blob/af69a5c5e99a32245a70b3739929868b74a541ad/CmakeError.log">
  <header class="source">

      <a href="https://github.com/f1oNae/CmakeError.log/blob/af69a5c5e99a32245a70b3739929868b74a541ad/CmakeError.log" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/f1oNae/CmakeError.log/blob/af69a5c5e99a32245a70b3739929868b74a541ad/CmakeError.log" target="_blank" rel="noopener nofollow ugc">f1oNae/CmakeError.log/blob/af69a5c5e99a32245a70b3739929868b74a541ad/CmakeError.log</a></h4>


      <pre><code class="lang-log">Performing C SOURCE FILE Test CMAKE_HAVE_LIBC_PTHREAD failed with the following output:
Change Dir: C:/D/S4D/Slicer-build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/amd64/MSBuild.exe cmTC_d3496.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=17.0 /v:m &amp;&amp; MSBuild version 17.5.0+6f08c67f3 for .NET Framework

  用于 x64 的 Microsoft (R) C/C++ 优化编译器 19.35.32215 版
  src.c
  版权所有(C) Microsoft Corporation。保留所有权利。
  cl /c /Zi /W1 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D CMAKE_HAVE_LIBC_PTHREAD /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_d3496.dir\Debug\\" /Fd"cmTC_d3496.dir\Debug\vc143.pdb" /external:W1 /Gd /TC /errorReport:queue "C:\D\S4D\Slicer-build\CMakeFiles\CMakeTmp\src.c"
C:\D\S4D\Slicer-build\CMakeFiles\CMakeTmp\src.c(1,10): fatal  error C1083: 无法打开包括文件: “pthread.h”: No such file or directory [C:\D\S4D\Slicer-build\CMakeFiles\CMakeTmp\cmTC_d3496.vcxproj]


Source file was:
#include &lt;pthread.h&gt;

static void* test_func(void* data)
{
  return data;
}

</code></pre>



  This file has been truncated. <a href="https://github.com/f1oNae/CmakeError.log/blob/af69a5c5e99a32245a70b3739929868b74a541ad/CmakeError.log" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2023-03-06 04:20 UTC)

<aside class="quote no-group" data-username="f1oNae" data-post="1" data-topic="28178">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/f1onae/48/17418_2.png" class="avatar"> f1oNae:</div>
<blockquote>
<p>Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined</p>
</blockquote>
</aside>
<p>This is the error.</p>
<p>Do you store Slicer source code in a git repository, or it is just a plain local folder?</p>
<p>If it is a plain local folder then you need to specify the working copy information (the build system needs that to make some decisions), but the proper solution is to use a revision-controlled folder for the source code.</p>
<p>If you store Slicer in a git repository then the data extraction may fail due to regional settings in your computer (how dates are formatted). See more details (what additional information we would need for the investigation) <a href="https://discourse.slicer.org/t/3d-slicer-release-build-error-variable-slicer-wc-last-changed-date-is-expected-to-be-defined-in-slicerpackageanduploadtarget/20984/21">here</a>.</p>

---
