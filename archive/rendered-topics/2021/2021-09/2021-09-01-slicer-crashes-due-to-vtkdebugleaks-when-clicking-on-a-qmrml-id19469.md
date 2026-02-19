---
topic_id: 19469
title: "Slicer Crashes Due To Vtkdebugleaks When Clicking On A Qmrml"
date: 2021-09-01
url: https://discourse.slicer.org/t/19469
---

# Slicer crashes due to vtkDebugLeaks when clicking on a qMRMLNodeComboBox

**Topic ID**: 19469
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/slicer-crashes-due-to-vtkdebugleaks-when-clicking-on-a-qmrmlnodecombobox/19469

---

## Post #1 by @Fernando (2021-09-01 18:40 UTC)

<p>Hi all,</p>
<p>I’m not sure whether this belongs here or on GitHub.</p>
<p>I just installed today’s preview (<code>4.13.0-2021-08-31 r30139 / 62817ae</code>) and then the TorchIO extension using the new, very nice Extensions Manager. I am on Ubuntu 18.04.</p>
<p>When I open the <code>TorchIO Transforms</code> module and I click on the <code>Input volume:</code> selector, Slicer crashes. It seems to be related to <code>vtkDebugLeaks</code>.</p>
<p>This is the output of the console I used to open Slicer:</p>
<pre><code class="lang-auto">Switch to module:  "Data"
Loading Slicer RC file [/home/fernando/.slicerrc.py]
Slicer RC file loaded [01/09/2021 18:36:14]
Requested file has been found: /tmp/BrainAnatomyLabelsV3_0.txt
"Color" Reader has successfully read the file "/tmp/BrainAnatomyLabelsV3_0.txt" "[0.01s]"
Loading /home/fernando/SlicerParcellation/InferenceUtils.py
Loading /home/fernando/SlicerParcellation/PyTorchUtils.py
Loading /home/fernando/SlicerParcellation/BrainParcellation.py
Loading /home/fernando/SlicerParcellation/TorchIOUtils.py
Loading /home/fernando/SlicerParcellation/BrainResectionCavitySegmentation.py
Loading .slicerrc.py
Fail to instantiate module  ".slicerrc"  (not registered)
Switch to module:  "TorchIOTransforms"
Importing torchio...
TorchIO 0.18.50 imported correctly
The X11 connection broke: Maximum allowed requested length exceeded (code 4)
XIO:  fatal IO error 0 (Success) on X server ":0"
      after 3061 requests (3056 known processed) with 0 events remaining.
The X11 connection broke: Maximum allowed requested length exceeded (code 4)
XIO:  fatal IO error 0 (Success) on X server ":0"
      after 3061 requests (3056 known processed) with 0 events remaining.
vtkDebugLeaks has detected LEAKS!
Class "vtkPVScalarBarActor" has 3 instances still around.
Class "vtkExtractStructuredGridHelper" has 1 instance still around.
Class "vtkInformationStringVectorValue" has 5 instances still around.
Class "vtkOpenGLBufferObject" has 3 instances still around.
Class "vtkInformationIntegerVectorValue" has 36 instances still around.
Class "vtkPixel" has 15 instances still around.
Class "vtkShaderProgram" has 22 instances still around.
Class "vtkShader" has 66 instances still around.
Class "vtkMRMLMultiVolumeRenderingDisplayNode" has 1 instance still around.
Class "vtkMRMLShaderPropertyStorageNode" has 1 instance still around.
Class "vtkMRMLShaderPropertyNode" has 1 instance still around.
Class "vtkOpenGLShaderProperty" has 26 instances still around.
Class "vtkOpenGLUniforms" has 78 instances still around.
Class "vtkTextureObject" has 40 instances still around.
Class "vtkPiecewiseFunction" has 2 instances still around.
Class "vtkVolumeProperty" has 1 instance still around.
Class "vtkMRMLVolumeRenderingDisplayableManager" has 1 instance still around.
Class "vtkVolumePicker" has 1 instance still around.
Class "vtkRectilinearSynchronizedTemplates" has 1 instance still around.
Class "vtkSynchronizedTemplates3D" has 1 instance still around.
Class "vtkUniformInternals" has 78 instances still around.
Class "vtkMultiVolume" has 1 instance still around.
Class "vtkCenteredAxesActor" has 3 instances still around.
Class "vtkSlicerTransformLogic" has 1 instance still around.
Class "vtkSlicerTextsLogic" has 1 instance still around.
Class "vtkSlicerSceneViewsModuleLogic" has 1 instance still around.
Class "vtkSlicerReformatLogic" has 1 instance still around.
Class "vtkSlicerPlotsLogic" has 1 instance still around.
Class "vtkClosedSurfaceToBinaryLabelmapConversionRule" has 1 instance still around.
Class "vtkBinaryLabelmapToClosedSurfaceConversionRule" has 1 instance still around.
Class "vtkMRMLSegmentEditorNode" has 1 instance still around.
Class "vtkMRMLSegmentationsDisplayableManager3D" has 1 instance still around.
Class "vtkSlicerTerminologiesModuleLogic" has 1 instance still around.
Class "vtkMRMLMultiVolumeStorageNode" has 1 instance still around.
Class "vtkSlicerMultiVolumeExplorerLogic" has 1 instance still around.
Class "vtkSlicerModelsLogic" has 1 instance still around.
Class "vtkMRMLMarkupsPlaneJsonStorageNode" has 1 instance still around.
Class "vtkMRMLMarkupsROIJsonStorageNode" has 1 instance still around.
Class "vtkMRMLMarkupsStorageNode" has 1 instance still around.
Class "vtkMRMLMarkupsDisplayNode" has 2 instances still around.
Class "vtkMRMLMarkupsNode" has 1 instance still around.
Class "vtkMRMLMarkupsDisplayableManager" has 4 instances still around.
Class "vtkMRMLMarkupsROINode" has 2 instances still around.
Class "vtkMRMLMarkupsFiducialDisplayNode" has 1 instance still around.
Class "vtkMRMLMeasurementVolume" has 2 instances still around.
Class "vtkSlicerPlaneWidget" has 1 instance still around.
Class "vtkSlicerCurveWidget" has 2 instances still around.
Class "vtkCurveMeasurementsCalculator" has 4 instances still around.
Class "vtkPassThroughFilter" has 4 instances still around.
Class "vtkSlicerAngleWidget" has 1 instance still around.
Class "vtkMRMLMeasurementAngle" has 2 instances still around.
Class "vtkSlicerLineWidget" has 1 instance still around.
Class "vtkMRMLMarkupsLineNode" has 2 instances still around.
Class "vtkMRMLMeasurementLength" has 6 instances still around.
Class "vtkMRMLSceneViewNode" has 1 instance still around.
Class "vtkSlicerPointsWidget" has 1 instance still around.
Class "vtkMRMLMarkupsFiducialNode" has 2 instances still around.
Class "vtkFractionalLabelmapToClosedSurfaceConversionRule" has 1 instance still around.
Class "vtkParallelTransportFrame" has 15 instances still around.
Class "vtkSlicerMarkupsLogic" has 1 instance still around.
Class "vtkMRMLDynamicModelerNode" has 1 instance still around.
Class "vtkMRMLMarkupsROIDisplayNode" has 1 instance still around.
Class "vtkSlicerDynamicModelerLogic" has 1 instance still around.
Class "vtkSlicerDoubleArraysLogic" has 1 instance still around.
Class "vtkSlicerDataStoreLogic" has 1 instance still around.
Class "vtkSlicerDataModuleLogic" has 1 instance still around.
Class "vtkMRMLCropVolumeParametersNode" has 1 instance still around.
Class "vtkSlicerCropVolumeLogic" has 1 instance still around.
Class "vtkSlicerUnitsLogic" has 1 instance still around.
Class "vtkMRMLUnitNode" has 42 instances still around.
Class "vtkSlicerCamerasModuleLogic" has 1 instance still around.
Class "vtkMRMLLinearTransformsDisplayableManager3D" has 1 instance still around.
Class "vtkMRMLAnnotationHierarchyNode" has 1 instance still around.
Class "vtkMRMLAnnotationFiducialsStorageNode" has 1 instance still around.
Class "vtkMRMLAnnotationFiducialNode" has 1 instance still around.
Class "vtkMRMLVolumePropertyNode" has 1 instance still around.
Class "vtkMRMLAnnotationROINode" has 1 instance still around.
Class "vtkMRMLAnnotationRulerStorageNode" has 1 instance still around.
Class "vtkMRMLAnnotationRulerNode" has 1 instance still around.
Class "vtkMRMLAnnotationTextNode" has 1 instance still around.
Class "vtkBitArray" has 6 instances still around.
Class "vtkMRMLAnnotationSnapshotStorageNode" has 1 instance still around.
Class "vtkMRMLAnnotationSnapshotNode" has 1 instance still around.
Class "vtkMRMLAnnotationLinesStorageNode" has 1 instance still around.
Class "vtkMRMLAnnotationPointDisplayNode" has 1 instance still around.
Class "vtkMRMLAnnotationControlPointsStorageNode" has 1 instance still around.
Class "vtkMRMLAnnotationControlPointsNode" has 1 instance still around.
Class "vtkMRMLChartViewNode" has 2 instances still around.
Class "vtkBSplineTransformConnectionHolder" has 2 instances still around.
Class "vtkActorCollection" has 22 instances still around.
Class "vtkMRMLGridTransformNode" has 2 instances still around.
Class "vtkPickingManager" has 4 instances still around.
Class "vtkStreamingDemandDrivenPipeline" has 488 instances still around.
Class "vtkGridTransformConnectionHolder" has 2 instances still around.
Class "vtkPoints" has 644 instances still around.
Class "vtkMRMLdGEMRICProceduralColorNode" has 2 instances still around.
Class "vtkOrientationMarkerWidget" has 1 instance still around.
Class "vtkInformationIntegerPointerValue" has 210 instances still around.
Class "vtkPointData" has 503 instances still around.
Class "vtkMRMLBSplineTransformNode" has 2 instances still around.
Class "vtkTrivialProducer" has 488 instances still around.
Class "vtkMRMLTransformStorageNode" has 2 instances still around.
Class "vtkImageMathematics" has 8 instances still around.
Class "vtkMRMLTransformDisplayNode" has 2 instances still around.
Class "vtkColorTransferFunction" has 13 instances still around.
Class "vtkVolumeCollection" has 16 instances still around.
Class "vtkMRMLTableViewNode" has 2 instances still around.
Class "vtkSlicerScriptedLoadableModuleLogic" has 72 instances still around.
Class "vtkPerspectiveTransform" has 36 instances still around.
Class "vtkArrayCalculator" has 4 instances still around.
Class "vtkPropPicker" has 9 instances still around.
Class "vtkMRMLGPURayCastVolumeRenderingDisplayNode" has 1 instance still around.
Class "vtkSlicerVolumeRenderingLogic" has 1 instance still around.
Class "vtkMRMLVectorVolumeNode" has 2 instances still around.
Class "vtkMRMLSnapshotClipNode" has 2 instances still around.
Class "vtkMRMLAnnotationTextDisplayNode" has 1 instance still around.
Class "vtkMRMLNRRDStorageNode" has 2 instances still around.
Class "vtkMRMLDiffusionTensorVolumeSliceDisplayNode" has 2 instances still around.
Class "vtkMRMLDiffusionTensorVolumeDisplayNode" has 2 instances still around.
Class "vtkContourFilter" has 1 instance still around.
Class "vtkMRMLProceduralColorStorageNode" has 2 instances still around.
Class "vtkSphereSource" has 6 instances still around.
Class "vtkDiffusionTensorGlyph" has 4 instances still around.
Class "vtkImageData" has 187 instances still around.
Class "vtkExtractVOI" has 1 instance still around.
Class "vtkEmptyCell" has 321 instances still around.
Class "vtkMRMLHierarchyStorageNode" has 2 instances still around.
Class "vtkMRMLMultiVolumeNode" has 1 instance still around.
Class "vtkMRMLDoubleArrayNode" has 2 instances still around.
Class "vtkMRMLScalarVolumeDisplayNode" has 2 instances still around.
Class "vtkMRMLSliceCompositeNode" has 6 instances still around.
Class "vtkMRMLMeasurementArea" has 4 instances still around.
Class "vtkMRMLDiffusionWeightedVolumeNode" has 2 instances still around.
Class "vtkMRMLRulerDisplayableManager" has 4 instances still around.
Class "vtkMRMLColorTableNode" has 60 instances still around.
Class "vtkLookupTable" has 101 instances still around.
Class "vtkOrientedGridTransform" has 2 instances still around.
Class "vtkObservation" has 2496 instances still around.
Class "vtkMRMLColorTableStorageNode" has 24 instances still around.
Class "vtkLine" has 15 instances still around.
Class "vtkMRMLStaticMeasurement" has 8 instances still around.
Class "vtkMRMLTextStorageNode" has 2 instances still around.
Class "vtkImplicitFunctionCollection" has 1 instance still around.
Class "vtkPolyDataToImageStencil" has 1 instance still around.
Class "vtkMRMLLabelMapVolumeDisplayNode" has 2 instances still around.
Class "vtkMRMLCrosshairDisplayableManager3D" has 1 instance still around.
Class "vtkUnsignedCharArray" has 125 instances still around.
Class "vtkImageStencil" has 9 instances still around.
Class "vtkDataSetSurfaceFilter" has 9 instances still around.
Class "vtkImageExtractComponents" has 35 instances still around.
Class "vtkMRMLMarkupsCurveNode" has 2 instances still around.
Class "vtkCompositeDataPipeline" has 876 instances still around.
Class "vtkImageThreshold" has 9 instances still around.
Class "vtkImageAppendComponents" has 15 instances still around.
Class "vtkSlicerVolumesLogic" has 1 instance still around.
Class "vtkMRMLFolderDisplayNode" has 2 instances still around.
Class "vtkImageLogic" has 9 instances still around.
Class "vtkOpenGLActor" has 49 instances still around.
Class "vtkContourValues" has 6 instances still around.
Class "vtkMRMLSelectionNode" has 3 instances still around.
Class "9vtkBufferIfE" has 495 instances still around.
Class "vtkCursor3D" has 1 instance still around.
Class "vtkMRMLPETProceduralColorNode" has 6 instances still around.
Class "vtkTimerLog" has 477 instances still around.
Class "vtkMRMLTransformsDisplayableManager2D" has 3 instances still around.
Class "vtkMRMLSliceViewInteractorStyle" has 3 instances still around.
Class "vtkDoubleArray" has 391 instances still around.
Class "vtkSlicerColorLogic" has 1 instance still around.
Class "vtkXMLDataElement" has 44 instances still around.
Class "vtkMRMLMarkupsAngleNode" has 2 instances still around.
Class "vtkCommand or subclass" has 6086 instances still around.
Class "vtkMultiThreader" has 182 instances still around.
Class "vtkSegmentationConverter" has 3 instances still around.
Class "vtkMRMLTableStorageNode" has 2 instances still around.
Class "vtkMRMLMessageCollection" has 101 instances still around.
Class "vtkFloatArray" has 495 instances still around.
Class "vtkMRMLSegmentationNode" has 3 instances still around.
Class "vtkCellPicker" has 4 instances still around.
Class "vtkAssignAttribute" has 42 instances still around.
Class "vtkSubjectHierarchyItem" has 6 instances still around.
Class "vtkImageRGBToHSI" has 2 instances still around.
Class "vtkDataIOManagerLogic" has 1 instance still around.
Class "vtkSlicerAnnotationModuleLogic" has 1 instance still around.
Class "vtkMRMLTransformsDisplayableManager3D" has 1 instance still around.
Class "vtkSlicerApplicationLogic" has 1 instance still around.
Class "vtkConeSource" has 4 instances still around.
Class "vtkImageReslice" has 22 instances still around.
Class "vtkEventBroker" has 1 instance still around.
Class "vtkMRMLCameraNode" has 3 instances still around.
Class "vtkMRMLThreeDViewInteractorStyle" has 1 instance still around.
Class "vtkMRMLMarkupsDisplayableManagerHelper" has 4 instances still around.
Class "vtkMRMLSliceNode" has 6 instances still around.
Class "vtkOutputWindow" has 1 instance still around.
Class "vtkMatrix3x3" has 301 instances still around.
Class "vtkPlane" has 12 instances still around.
Class "vtkTexturedActor2D" has 6 instances still around.
Class "vtkPointHandleRepresentation3D" has 1 instance still around.
Class "vtkMRMLDiffusionTensorVolumeNode" has 2 instances still around.
Class "vtkImageMapToWindowLevelColors" has 9 instances still around.
Class "vtkMRMLModelStorageNode" has 2 instances still around.
Class "vtkMRMLStreamingVolumeNode" has 2 instances still around.
Class "vtkMRMLDisplayableHierarchyNode" has 2 instances still around.
Class "vtkMRMLInteractionNode" has 3 instances still around.
Class "vtkMRMLSliceLinkLogic" has 1 instance still around.
Class "vtkMRMLDisplayableManagerGroup" has 4 instances still around.
Class "vtkInformationIntegerValue" has 10003 instances still around.
Class "vtkIdList" has 1107 instances still around.
Class "vtkMRMLTransformNode" has 2 instances still around.
Class "vtkMatrix4x4" has 1782 instances still around.
Class "vtkInformationDoubleVectorValue" has 75 instances still around.
Class "vtkMRMLAnnotationLineDisplayNode" has 1 instance still around.
Class "vtkMRMLDoubleArrayStorageNode" has 2 instances still around.
Class "vtkMRMLAnnotationFiducialDisplayableManager" has 4 instances still around.
Class "vtkFunctionParser" has 4 instances still around.
Class "vtkIntArray" has 797 instances still around.
Class "vtkImageShiftScale" has 4 instances still around.
Class "vtkMRMLSegmentationsDisplayableManager2D" has 3 instances still around.
Class "vtkMRMLAnnotationClickCounter" has 12 instances still around.
Class "vtkOpenGLPolyDataMapper" has 40 instances still around.
Class "vtkMRMLSliceViewDisplayableManagerFactory" has 1 instance still around.
Class "vtkInformationExecutivePortValue" has 995 instances still around.
Class "vtkClosedSurfaceToFractionalLabelmapConversionRule" has 1 instance still around.
Class "vtkMRMLCPURayCastVolumeRenderingDisplayNode" has 1 instance still around.
Class "vtkSimpleTransform" has 160 instances still around.
Class "vtkMRMLChartNode" has 2 instances still around.
Class "vtkMRMLVolumeArchetypeStorageNode" has 2 instances still around.
Class "vtkInformationIterator" has 1364 instances still around.
Class "vtkOpenGLImageMapper" has 3 instances still around.
Class "vtkAxesActor" has 1 instance still around.
Class "vtkMRMLFiducialListNode" has 2 instances still around.
Class "vtkVertex" has 3 instances still around.
Class "vtkMRMLVolumeSequenceStorageNode" has 2 instances still around.
Class "9vtkBufferIiE" has 797 instances still around.
Class "vtkOpenGLCamera" has 18 instances still around.
Class "vtkMRMLAnnotationDisplayableManagerHelper" has 12 instances still around.
Class "vtkTransformPolyDataFilter" has 36 instances still around.
Class "vtkOpenGLShaderCache" has 4 instances still around.
Class "vtkMRMLLayoutNode" has 3 instances still around.
Class "vtkCellArray" has 415 instances still around.
Class "vtkMRMLCommandLineModuleNode" has 1 instance still around.
Class "vtkOpenGLState" has 4 instances still around.
Class "vtkInformationVector" has 5945 instances still around.
Class "vtkTagTable" has 151 instances still around.
Class "vtkCoordinate" has 636 instances still around.
Class "9vtkBufferIhE" has 125 instances still around.
Class "vtkSlicerTablesLogic" has 1 instance still around.
Class "vtkMRMLSegmentationStorageNode" has 2 instances still around.
Class "vtkGeometryFilter" has 11 instances still around.
Class "vtkCacheManager" has 1 instance still around.
Class "vtkMRMLDiffusionWeightedVolumeDisplayNode" has 2 instances still around.
Class "vtkImageStencilData" has 23 instances still around.
Class "vtkSlicerViewControllersLogic" has 1 instance still around.
Class "vtkFocalPlanePointPlacer" has 1 instance still around.
Class "vtkOpenGLRenderer" has 16 instances still around.
Class "vtkProp3DCollection" has 6 instances still around.
Class "vtkLineSource" has 12 instances still around.
Class "vtkImageBlend" has 6 instances still around.
Class "vtkMRMLLinearTransformNode" has 5 instances still around.
Class "vtkMRMLSegmentationDisplayNode" has 2 instances still around.
Class "vtkPersonInformation" has 1 instance still around.
Class "vtkStringArray" has 179 instances still around.
Class "vtkThreshold" has 11 instances still around.
Class "vtkWidgetEventTranslator" has 109 instances still around.
Class "vtkVariantArray" has 2 instances still around.
Class "9vtkBufferIdE" has 391 instances still around.
Class "vtkMRMLSceneViewStorageNode" has 1 instance still around.
Class "vtkCollection" has 39 instances still around.
Class "vtkDiffusionTensorMathematics" has 5 instances still around.
Class "vtkSegmentation" has 3 instances still around.
Class "9vtkBufferIxE" has 1245 instances still around.
Class "vtkDataIOManager" has 1 instance still around.
Class "vtkPassThrough" has 11 instances still around.
Class "vtkOpenGLVertexBufferObjectGroup" has 308 instances still around.
Class "vtkFieldData" has 530 instances still around.
Class "vtkFrustumCoverageCuller" has 16 instances still around.
Class "9vtkBufferImE" has 360 instances still around.
Class "vtkDataSetAttributes" has 2 instances still around.
Class "vtkFXAAOptions" has 16 instances still around.
Class "vtkUnsignedLongArray" has 360 instances still around.
Class "vtkMRMLCrosshairDisplayableManager" has 3 instances still around.
Class "vtkMRMLScalarVolumeNode" has 2 instances still around.
Class "vtkGridSynchronizedTemplates3D" has 1 instance still around.
Class "vtkCaptionActor2D" has 12 instances still around.
Class "vtkMRMLModelNode" has 5 instances still around.
Class "vtkMRMLColorNode" has 2 instances still around.
Class "vtkIdTypeArray" has 415 instances still around.
Class "vtkPropCollection" has 42 instances still around.
Class "vtkMRMLROIListNode" has 2 instances still around.
Class "vtkImageCast" has 20 instances still around.
Class "vtkGeneralTransform" has 46 instances still around.
Class "vtkPointLocator" has 30 instances still around.
Class "vtkMRMLAnnotationLinesNode" has 1 instance still around.
Class "vtkAlgorithmOutput" has 769 instances still around.
Class "vtkOpenGLTextMapper" has 160 instances still around.
Class "vtkMRMLSequenceBrowserNode" has 1 instance still around.
Class "vtkMRMLModelDisplayNode" has 5 instances still around.
Class "vtkVectorText" has 6 instances still around.
Class "vtkMRMLSliceLogic" has 3 instances still around.
Class "vtkMRMLFiducialListStorageNode" has 2 instances still around.
Class "vtkMRMLVectorVolumeDisplayNode" has 2 instances still around.
Class "vtkMRMLMarkupsPlaneNode" has 2 instances still around.
Class "vtkHandleWidget" has 1 instance still around.
Class "vtkOpenGLLight" has 15 instances still around.
Class "vtkSynchronizedTemplates2D" has 1 instance still around.
Class "vtkTypeInt64Array" has 830 instances still around.
Class "vtkCurveGenerator" has 15 instances still around.
Class "vtkMRMLModelSliceDisplayableManager" has 3 instances still around.
Class "vtkMRMLROINode" has 2 instances still around.
Class "vtkMRMLDiffusionTensorDisplayPropertiesNode" has 2 instances still around.
Class "vtkVoxel" has 2 instances still around.
Class "vtkMRMLScriptedModuleNode" has 3 instances still around.
Class "vtkMRMLAnnotationBidimensionalNode" has 1 instance still around.
Class "vtkMRMLScene" has 2 instances still around.
Class "vtkMRMLViewNode" has 4 instances still around.
Class "vtkMRMLTextNode" has 2 instances still around.
Class "vtkMRMLPlotSeriesNode" has 2 instances still around.
Class "vtkMRMLPlotChartNode" has 2 instances still around.
Class "vtkMRMLPlotViewNode" has 3 instances still around.
Class "vtkMRMLSubjectHierarchyNode" has 3 instances still around.
Class "vtkSlicerDijkstraGraphGeodesicPath" has 15 instances still around.
Class "vtkMRMLProceduralColorNode" has 4 instances still around.
Class "vtkMRMLSequenceNode" has 2 instances still around.
Class "vtkMRMLSequenceStorageNode" has 2 instances still around.
Class "vtkMRMLMarkupsFiducialStorageNode" has 1 instance still around.
Class "vtkMRMLClipModelsNode" has 3 instances still around.
Class "vtkHTTPHandler" has 1 instance still around.
Class "ctkVTKOutputWindow" has 1 instance still around.
Class "vtkMRMLLabelMapVolumeNode" has 2 instances still around.
Class "vtkPolyData" has 316 instances still around.
Class "vtkMRMLMultiVolumeDisplayNode" has 1 instance still around.
Class "vtkTriangleFilter" has 4 instances still around.
Class "vtkSlicerSubjectHierarchyModuleLogic" has 1 instance still around.
Class "vtkOpenGLGPUVolumeRayCastMapper" has 1 instance still around.
Class "vtkTable" has 2 instances still around.
Class "vtkGenericCell" has 5 instances still around.
Class "vtkCleanPolyData" has 4 instances still around.
Class "vtkOpenGLFramebufferObject" has 12 instances still around.
Class "vtkOpenGLVertexArrayObject" has 1475 instances still around.
Class "vtkMRMLCameraWidget" has 1 instance still around.
Class "vtkImageAccumulate" has 1 instance still around.
Class "vtkObserverManager" has 1069 instances still around.
Class "vtkOpenGLTexture" has 188 instances still around.
Class "CellMap" has 4 instances still around.
Class "vtkMRMLVolumePropertyStorageNode" has 1 instance still around.
Class "vtkMRMLMarkupsJsonStorageNode" has 1 instance still around.
Class "vtkMRMLViewLinkLogic" has 1 instance still around.
Class "vtkAppendPolyData" has 12 instances still around.
Class "vtkMRMLLayoutLogic" has 1 instance still around.
Class "vtkMRMLModelHierarchyNode" has 2 instances still around.
Class "vtkInformationExecutivePortVectorValue" has 750 instances still around.
Class "vtkOpenGLRenderTimerLog" has 4 instances still around.
Class "vtkStereoCompositor" has 4 instances still around.
Class "vtkMRMLTableNode" has 2 instances still around.
Class "vtkRendererCollection" has 4 instances still around.
Class "vtkOpenGLVertexBufferObjectCache" has 4 instances still around.
Class "vtkTextureUnitManager" has 4 instances still around.
Class "vtkTransform" has 527 instances still around.
Class "vtkGenericOpenGLRenderWindow" has 4 instances still around.
Class "vtkOpenGLIndexBufferObject" has 1472 instances still around.
Class "vtkOpenGLCellToVTKCellMap" has 308 instances still around.
Class "vtkWidgetCallbackMapper" has 1 instance still around.
Class "vtkOpenGLPolyDataMapper2D" has 268 instances still around.
Class "vtkMRMLLinearTransformSequenceStorageNode" has 2 instances still around.
Class "vtkMRMLVolumeGlyphSliceDisplayableManager" has 3 instances still around.
Class "vtkActor2D" has 246 instances still around.
Class "vtkCullerCollection" has 16 instances still around.
Class "vtkActor2DCollection" has 16 instances still around.
Class "vtkImageMapToColors" has 11 instances still around.
Class "vtkOutlineSource" has 5 instances still around.
Class "vtkCornerAnnotation" has 7 instances still around.
Class "vtkMRMLMarkupsClosedCurveNode" has 2 instances still around.
Class "vtkMRMLModelDisplayableManager" has 1 instance still around.
Class "vtkLightBoxRendererManager" has 3 instances still around.
Class "vtkLightCollection" has 16 instances still around.
Class "vtkProperty2D" has 110 instances still around.
Class "vtkTDxInteractorStyleSettings" has 4 instances still around.
Class "vtkTDxInteractorStyleCamera" has 4 instances still around.
Class "vtkWorldPointPicker" has 11 instances still around.
Class "QVTKInteractor" has 4 instances still around.
Class "vtkInternalLightBoxRendererManagerProxy" has 3 instances still around.
Class "vtkEvent" has 233 instances still around.
Class "vtkMRMLCrosshairNode" has 3 instances still around.
Class "vtkGlyph3D" has 12 instances still around.
Class "vtkMRMLInteractionEventData" has 531 instances still around.
Class "vtkMRMLSliceIntersectionWidget" has 3 instances still around.
Class "vtkAxisActor2D" has 4 instances still around.
Class "vtkMRMLWindowLevelWidget" has 3 instances still around.
Class "vtkCellData" has 503 instances still around.
Class "vtkMRMLScalarBarDisplayableManager" has 3 instances still around.
Class "vtkImageLabelOutline" has 18 instances still around.
Class "vtkOpenGLProperty" has 49 instances still around.
Class "vtkMRMLSliceLayerLogic" has 9 instances still around.
Class "vtkPlaneSource" has 3 instances still around.
Class "vtkMRMLHierarchyNode" has 2 instances still around.
Class "vtkInformationStringValue" has 71 instances still around.
Class "vtkMRMLNodeReference" has 35 instances still around.
Class "vtkPlaneCutter" has 9 instances still around.
Class "vtkOrientedBSplineTransform" has 2 instances still around.
Class "vtkCompositeDataGeometryFilter" has 9 instances still around.
Class "vtkSlicerSequencesLogic" has 1 instance still around.
Class "vtkITKImageThresholdCalculator" has 1 instance still around.
Class "vtkSlicerROIWidget" has 1 instance still around.
Class "vtkSampleImplicitFunctionFilter" has 9 instances still around.
Class "vtkSlicerSegmentationsModuleLogic" has 1 instance still around.
Class "vtkTextProperty" has 226 instances still around.
Class "vtkTransformFilter" has 9 instances still around.
Class "vtkSlicerCLIModuleLogic" has 49 instances still around.
Class "vtkMRMLSliceIntersectionRepresentation2D" has 3 instances still around.
Class "vtkMRMLRubberBandWidgetRepresentation" has 3 instances still around.
Class "vtkMRMLViewLogic" has 1 instance still around.
Class "vtkMRMLAnnotationStorageNode" has 1 instance still around.
Class "vtkOpenGLTextActor" has 19 instances still around.
Class "vtkCylinderSource" has 4 instances still around.
Class "vtkOpenGLVertexBufferObject" has 53 instances still around.
Class "vtkCaptionActor2DConnection" has 12 instances still around.
Class "vtkMRMLCameraDisplayableManager" has 1 instance still around.
Class "vtkMRMLOrientationMarkerDisplayableManager" has 4 instances still around.
Class "vtkFollower" has 6 instances still around.
Class "vtkMRMLViewDisplayableManager" has 1 instance still around.
Class "vtkMRMLThreeDViewDisplayableManagerFactory" has 1 instance still around.
Class "vtkPointPicker" has 1 instance still around.
Class "vtkImplicitBoolean" has 1 instance still around.
Class "vtkMRMLThreeDReformatDisplayableManager" has 1 instance still around.
Class "vtkEventDataButton3D" has 2 instances still around.
Class "vtkMRMLAnnotationNode" has 1 instance still around.
Class "vtkEventDataMove3D" has 1 instance still around.
Class "vtkInformation" has 10794 instances still around.
Class "vtkMatrixToLinearTransform" has 8 instances still around.
Class "vtkMRMLAnnotationRulerDisplayableManager" has 4 instances still around.
Class "vtkMRMLAnnotationROIDisplayableManager" has 4 instances still around.
Class "vtkMRMLRemoteIOLogic" has 1 instance still around.
Class "vtkMRMLAnnotationDisplayNode" has 1 instance still around.
</code></pre>

---

## Post #2 by @pieper (2021-09-01 18:48 UTC)

<p>thanks for the report.</p>
<p>I’m not sure what causes it, but this part is the real error, and it leads the application to exit without cleaning up and that’s what causes the leak report.</p>
<pre><code class="lang-auto">The X11 connection broke: Maximum allowed requested length exceeded (code 4)
XIO:  fatal IO error 0 (Success) on X server ":0"
      after 3061 requests (3056 known processed) with 0 events remaining.
The X11 connection broke: Maximum allowed requested length exceeded (code 4)
XIO:  fatal IO error 0 (Success) on X server ":0"
      after 3061 requests (3056 known processed) with 0 events remaining.
</code></pre>
<p>Dot it happen repeatably? Is it just this button press or have you seen it with other buttons?</p>

---

## Post #3 by @Fernando (2021-09-01 18:52 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="19469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Dot it happen repeatably? Is it just this button press or have you seen it with other buttons?</p>
</blockquote>
</aside>
<p>It happens with all the selectors in that module. The push button is ok. Selectors in other modules are ok.</p>
<p>Is this maybe Qt related? I just found this: <a href="https://github.com/bitcoin-core/gui/issues/47" class="inline-onebox" rel="noopener nofollow ugc">Maximum allowed requested length exceeded · Issue #47 · bitcoin-core/gui · GitHub</a></p>

---

## Post #4 by @pieper (2021-09-01 19:00 UTC)

<p>Definitely Qt related, but odd that other combo boxes don’t crash.  Maybe it’s a library mismatch somehow?  Perhaps the new extension manager is not fetching the right package.  There was some mention of a similar version issue recently.</p>

---

## Post #5 by @Fernando (2021-09-01 19:02 UTC)

<p>Let me know if you need any more info from my machine. Just to clarify, it’s my laptop, not a remote connection.</p>

---

## Post #6 by @dzenanz (2021-09-01 19:14 UTC)

<p>The error looks somewhat similar to <a href="https://unix.stackexchange.com/questions/629281/gitk-crashes-when-viewing-commit-containing-emoji-x-error-of-failed-request-ba" rel="noopener nofollow ugc">this <code>gitk</code> crash</a> I ran into a few days ago. <code>sudo apt install unifont</code> was the solution for me on Ubuntu 20.04.</p>

---

## Post #7 by @Fernando (2021-09-01 19:18 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="6" data-topic="19469">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>sudo apt install unifont</p>
</blockquote>
</aside>
<p>Thanks, <a class="mention" href="/u/dzenanz">@dzenanz</a>. I just tried that but it didn’t help in my case.</p>

---

## Post #8 by @lassoan (2021-09-01 19:44 UTC)

<p>You need to figure out what is “special” about your module. You can do that by simplifying the module until the point it no longer behaves incorrectly, then gradually add back the features to see what makes it break. For example, you can start with removing all the Qt connections (so that selecting a node has no effect), if it fixes the issue then add back the connection, but comment out all the lines in the callback function, and add back the lines one by one.</p>

---

## Post #9 by @Fernando (2021-09-01 20:02 UTC)

<p>Hi, <a class="mention" href="/u/lassoan">@lassoan</a>. I’ve performed the ablation study, as requested:</p>
<ol>
<li>Reinstall Slicer</li>
<li>Install PyTorch extension</li>
<li>Add module directory in settings</li>
<li>Start removing things</li>
</ol>
<p>Unfortunately, the module is now tiny and it still crashes when I click on the selector. This is the whole code:</p>
<pre><code class="lang-python">import slicer
from slicer.ScriptedLoadableModule import (
  ScriptedLoadableModule,
  ScriptedLoadableModuleWidget,
)


class TorchIOTransforms(ScriptedLoadableModule):

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = 'TorchIO Transforms'
    self.parent.categories = ['Utilities']


class TorchIOTransformsWidget(ScriptedLoadableModuleWidget):

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    self.layout.addWidget(self.inputSelector)
</code></pre>

---

## Post #10 by @lassoan (2021-09-01 20:04 UTC)

<p>You can then clone another module (that does not crash) and start adding your features to it.</p>

---

## Post #11 by @Fernando (2021-09-01 20:10 UTC)

<p>Ok, I used the same code in an empty folder and it didn’t crash.</p>
<p>Some people from the links above mentioned some images being too large for Qt, so I deleted the <code>Resources</code> folder from the problematic repo and it didn’t crash! So we’re getting closer, I guess.</p>
<p>Edit: the <code>Resources</code> folder:</p>
<pre><code class="lang-auto">Resources
└── Icons
    └── TorchIOTransforms.png
</code></pre>

---

## Post #12 by @Fernando (2021-09-01 20:13 UTC)

<p>Update: when I resize the icon from 2048x2048 to 128x128, there’s no crash.</p>
<p>1024x1024 is fine too.</p>

---

## Post #13 by @Greydon_Gilmore (2021-10-14 22:37 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> you are a life saver! I have been trying to fix this bug for the past week… I thought I was initializing the parameter node or the <code>qMRMLNodeComboBox</code> incorrectly. I even tried re-installing Pop!_OS…</p>
<p>Turns out the icon I generated for my module was too large, compressing the image solved my issue.</p>
<p>For reference, the behaviour I was experiencing was the Slicer app crashing when interacting with the <code>qMRMLNodeComboBox</code>. The displayed error message (when running --launcher-verbose):</p>
<pre><code class="lang-auto">The X11 connection broke: Maximum allowed requested length exceeded (code 4)
XIO:  fatal IO error 0 (Success) on X server ":1"
      after 3234 requests (3229 known processed) with 0 events remaining.
error: [/opt/Slicer-4.11.20210226/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>Thank you!</p>

---
