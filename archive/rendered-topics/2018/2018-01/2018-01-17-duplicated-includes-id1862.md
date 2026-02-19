---
topic_id: 1862
title: "Duplicated Includes"
date: 2018-01-17
url: https://discourse.slicer.org/t/1862
---

# Duplicated includes?

**Topic ID**: 1862
**Date**: 2018-01-17
**URL**: https://discourse.slicer.org/t/duplicated-includes/1862

---

## Post #1 by @ihnorton (2018-01-17 14:55 UTC)

<p>Is there a reason we are setting the include path to both source <em>and the build directory</em> for VTK and ITK? This means I have nearly 500 include directories for a single compiler invocation (macOS 10.12, SDK 10.13; Qt 5.9.3 from Qt Company package, etc.)</p>
<pre><code class="lang-auto">cat /tmp/one-clang-invocation | sed $'s/ /\\\n/g' | grep "\-I" | wc -l
     493
</code></pre>
<p>where <code>/tmp/one-clang-invocation</code> is the first line in <code>Slicer-build/compile_commands.json</code> (with <code>CMAKE_EXPORT_COMPILE_COMMANDS</code> enabled, and <a href="https://github.com/Slicer/Slicer/pull/869">this PR</a>):</p>
<pre><code class="lang-auto">  "command": "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  -DITKFactoryRegistration_EXPORTS -DITK_IO_FACTORY_REGISTER_MANAGER -DPYTHONQT_USE_RELEASE_PYTHON_FALLBACK -DvtkRenderingContext2D_AUTOINIT=\"1(vtkRenderingContextOpenGL2)\" -DvtkRenderingCore_AUTOINIT=\"3(vtkInteractionStyle,vtkRenderingFreeType,vtkRenderingOpenGL2)\" -DvtkRenderingOpenGL2_AUTOINIT=\"1(vtkRenderingGL2PSOpenGL2)\" -DvtkRenderingVolume_AUTOINIT=\"1(vtkRenderingVolumeOpenGL2)\" -ILibs/ITKFactoryRegistration/ITKIOFactoryRegistration -I/opt/bld/s5nj/ITKv4/Modules/IO/DCMTK/include -I/opt/bld/s5nj/ITKv4/Modules/IO/MINC/include -I/opt/bld/s5nj/ITKv4/Modules/Remote/MGHIO/include -I/opt/bld/s5nj/ITKv4/Modules/IO/TransformMatlab/include -I/opt/bld/s5nj/ITKv4/Modules/IO/TransformInsightLegacy/include -I/opt/bld/s5nj/ITKv4/Modules/IO/TransformHDF5/include -I/opt/bld/s5nj/ITKv4/Modules/IO/GIPL/include -I/opt/bld/s5nj/ITKv4/Modules/IO/NRRD/include -I/opt/bld/s5nj/ITKv4/Modules/IO/NIFTI/include -I/opt/bld/s5nj/ITKv4/Modules/IO/MRC/include -I/opt/bld/s5nj/ITKv4/Modules/IO/Meta/include -I/opt/bld/s5nj/ITKv4/Modules/IO/BioRad/include -I/opt/bld/s5nj/ITKv4/Modules/IO/Stimulate/include -I/opt/bld/s5nj/ITKv4/Modules/IO/VTK/include -I/opt/bld/s5nj/ITKv4/Modules/IO/TIFF/include -I/opt/bld/s5nj/ITKv4/Modules/IO/PNG/include -I/opt/bld/s5nj/ITKv4/Modules/IO/LSM/include -I/opt/bld/s5nj/ITKv4/Modules/IO/BMP/include -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/Expat/src/expat -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/Expat/src/expat -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/DataStructureAndEncodingDefinition -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/MessageExchangeDefinition -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/InformationObjectDefinition -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/Common -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/DataDictionary -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/GDCM/src/gdcm/Source/Common -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/GDCM -I/opt/bld/s5nj/ITKv4/Modules/IO/GDCM/include -I/opt/bld/s5nj/ITKv4/Modules/IO/JPEG/include -I/opt/bld/s5nj/ITKv4/Modules/IO/TransformFactory/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Path/include -I/opt/bld/s5nj/zlib-install/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/ZLIB/src -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/MetaIO/src/MetaIO/src -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/MetaIO/src/MetaIO/src -I/opt/bld/s5nj/ITKv4/Modules/Core/SpatialObjects/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageCompose/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageStatistics/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageIntensity/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageFilterBase/include -I/opt/bld/s5nj/ITKv4/Modules/Core/Transform/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/Netlib -I/opt/bld/s5nj/ITKv4/Modules/Numerics/Statistics/include -I/opt/bld/s5nj/ITKv4/Modules/Core/ImageAdaptors/include -I/opt/bld/s5nj/ITKv4/Modules/Core/ImageFunction/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageGrid/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/DisplacementField/include -I/opt/bld/s5nj/ITKv4/Modules/IO/TransformBase/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/VNL/src/vxl/core -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/VNL/src/vxl/vcl -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/VNL/src/vxl/v3p/netlib -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/VNL/src/vxl/core -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/VNL/src/vxl/vcl -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/VNL/src/vxl/v3p/netlib -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/VNLInstantiation/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/KWSys/src -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/KWIML/src -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/KWIML/src -I/opt/bld/s5nj/ITKv4/Modules/Core/Common/include -I/opt/bld/s5nj/ITKv4-build/Modules/Core/Common -I/opt/bld/s5nj/ITKv4/Modules/IO/ImageBase/include -I/opt/bld/s5nj/ITKv4-build/Modules/IO/ImageBase -I/opt/bld/s5nj/VTKv9-build/Filters/Extraction -I/opt/bld/s5nj/VTKv9/Filters/Extraction -I/opt/bld/s5nj/VTKv9-build/Common/Core -I/opt/bld/s5nj/VTKv9/Common/Core -I/opt/bld/s5nj/VTKv9-build/Utilities/KWIML -I/opt/bld/s5nj/VTKv9/Utilities/KWIML -I/opt/bld/s5nj/VTKv9-build/Utilities/KWSys -I/opt/bld/s5nj/VTKv9/Utilities/KWSys -I/opt/bld/s5nj/VTKv9-build/ThirdParty/utf8 -I/opt/bld/s5nj/VTKv9/ThirdParty/utf8 -I/opt/bld/s5nj/VTKv9-build/Common/DataModel -I/opt/bld/s5nj/VTKv9/Common/DataModel -I/opt/bld/s5nj/VTKv9-build/Common/Math -I/opt/bld/s5nj/VTKv9/Common/Math -I/opt/bld/s5nj/VTKv9-build/Common/Misc -I/opt/bld/s5nj/VTKv9/Common/Misc -I/opt/bld/s5nj/VTKv9-build/Common/System -I/opt/bld/s5nj/VTKv9/Common/System -I/opt/bld/s5nj/VTKv9-build/Common/Transforms -I/opt/bld/s5nj/VTKv9/Common/Transforms -I/opt/bld/s5nj/VTKv9-build/Common/ExecutionModel -I/opt/bld/s5nj/VTKv9/Common/ExecutionModel -I/opt/bld/s5nj/VTKv9-build/Filters/Core -I/opt/bld/s5nj/VTKv9/Filters/Core -I/opt/bld/s5nj/VTKv9-build/Filters/General -I/opt/bld/s5nj/VTKv9/Filters/General -I/opt/bld/s5nj/VTKv9-build/Common/ComputationalGeometry -I/opt/bld/s5nj/VTKv9/Common/ComputationalGeometry -I/opt/bld/s5nj/VTKv9-build/Filters/Statistics -I/opt/bld/s5nj/VTKv9/Filters/Statistics -I/opt/bld/s5nj/VTKv9-build/Imaging/Fourier -I/opt/bld/s5nj/VTKv9/Imaging/Fourier -I/opt/bld/s5nj/VTKv9-build/Imaging/Core -I/opt/bld/s5nj/VTKv9/Imaging/Core -I/opt/bld/s5nj/VTKv9-build/ThirdParty/alglib -I/opt/bld/s5nj/VTKv9/ThirdParty/alglib -I/opt/bld/s5nj/VTKv9-build/Filters/FlowPaths -I/opt/bld/s5nj/VTKv9/Filters/FlowPaths -I/opt/bld/s5nj/VTKv9-build/Filters/Geometry -I/opt/bld/s5nj/VTKv9/Filters/Geometry -I/opt/bld/s5nj/VTKv9-build/Filters/Sources -I/opt/bld/s5nj/VTKv9/Filters/Sources -I/opt/bld/s5nj/VTKv9-build/IO/Core -I/opt/bld/s5nj/VTKv9/IO/Core -I/opt/bld/s5nj/VTKv9/ThirdParty/lz4/vtklz4/lib -I/opt/bld/s5nj/VTKv9-build/ThirdParty/lz4/vtklz4 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/lz4 -I/opt/bld/s5nj/VTKv9/ThirdParty/lz4 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/zlib -I/opt/bld/s5nj/VTKv9/ThirdParty/zlib -I/opt/bld/s5nj/VTKv9-build/GUISupport/QtOpenGL -I/opt/bld/s5nj/VTKv9/GUISupport/QtOpenGL -I/opt/bld/s5nj/VTKv9-build/GUISupport/Qt -I/opt/bld/s5nj/VTKv9/GUISupport/Qt -I/opt/bld/s5nj/VTKv9-build/Interaction/Style -I/opt/bld/s5nj/VTKv9/Interaction/Style -I/opt/bld/s5nj/VTKv9-build/Rendering/Core -I/opt/bld/s5nj/VTKv9/Rendering/Core -I/opt/bld/s5nj/VTKv9-build/Common/Color -I/opt/bld/s5nj/VTKv9/Common/Color -I/opt/bld/s5nj/VTKv9-build/Rendering/OpenGL2 -I/opt/bld/s5nj/VTKv9/Rendering/OpenGL2 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/glew -I/opt/bld/s5nj/VTKv9/ThirdParty/glew -I/opt/bld/s5nj/VTKv9-build/GUISupport/QtSQL -I/opt/bld/s5nj/VTKv9/GUISupport/QtSQL -I/opt/bld/s5nj/VTKv9-build/IO/SQL -I/opt/bld/s5nj/VTKv9/IO/SQL -I/opt/bld/s5nj/VTKv9-build/ThirdParty/sqlite -I/opt/bld/s5nj/VTKv9/ThirdParty/sqlite -I/opt/bld/s5nj/VTKv9-build/IO/Export -I/opt/bld/s5nj/VTKv9/IO/Export -I/opt/bld/s5nj/VTKv9-build/IO/Image -I/opt/bld/s5nj/VTKv9/IO/Image -I/opt/bld/s5nj/VTKv9-build/Utilities/DICOMParser -I/opt/bld/s5nj/VTKv9/Utilities/DICOMParser -I/opt/bld/s5nj/VTKv9-build/Utilities/MetaIO/vtkmetaio -I/opt/bld/s5nj/VTKv9-build/Utilities/MetaIO -I/opt/bld/s5nj/VTKv9/Utilities/MetaIO -I/opt/bld/s5nj/VTKv9-build/ThirdParty/jpeg -I/opt/bld/s5nj/VTKv9/ThirdParty/jpeg -I/opt/bld/s5nj/VTKv9-build/ThirdParty/png -I/opt/bld/s5nj/VTKv9/ThirdParty/png -I/opt/bld/s5nj/VTKv9-build/ThirdParty/tiff/vtktiff/libtiff -I/opt/bld/s5nj/VTKv9-build/ThirdParty/tiff -I/opt/bld/s5nj/VTKv9/ThirdParty/tiff -I/opt/bld/s5nj/VTKv9-build/Rendering/Context2D -I/opt/bld/s5nj/VTKv9/Rendering/Context2D -I/opt/bld/s5nj/VTKv9-build/Rendering/FreeType -I/opt/bld/s5nj/VTKv9/Rendering/FreeType -I/opt/bld/s5nj/VTKv9-build/ThirdParty/freetype -I/opt/bld/s5nj/VTKv9/ThirdParty/freetype -I/opt/bld/s5nj/VTKv9-build/Rendering/GL2PSOpenGL2 -I/opt/bld/s5nj/VTKv9/Rendering/GL2PSOpenGL2 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/gl2ps -I/opt/bld/s5nj/VTKv9/ThirdParty/gl2ps -I/opt/bld/s5nj/VTKv9/ThirdParty/libharu/vtklibharu/include -I/opt/bld/s5nj/VTKv9-build/ThirdParty/libharu/vtklibharu/include -I/opt/bld/s5nj/VTKv9-build/ThirdParty/libharu -I/opt/bld/s5nj/VTKv9/ThirdParty/libharu -I/opt/bld/s5nj/VTKv9-build/IO/Legacy -I/opt/bld/s5nj/VTKv9/IO/Legacy -I/opt/bld/s5nj/VTKv9-build/IO/PLY -I/opt/bld/s5nj/VTKv9/IO/PLY -I/opt/bld/s5nj/VTKv9-build/IO/XML -I/opt/bld/s5nj/VTKv9/IO/XML -I/opt/bld/s5nj/VTKv9-build/IO/XMLParser -I/opt/bld/s5nj/VTKv9/IO/XMLParser -I/opt/bld/s5nj/VTKv9-build/ThirdParty/expat -I/opt/bld/s5nj/VTKv9/ThirdParty/expat -I/opt/bld/s5nj/VTKv9-build/Imaging/Math -I/opt/bld/s5nj/VTKv9/Imaging/Math -I/opt/bld/s5nj/VTKv9-build/Imaging/Morphological -I/opt/bld/s5nj/VTKv9/Imaging/Morphological -I/opt/bld/s5nj/VTKv9-build/Imaging/General -I/opt/bld/s5nj/VTKv9/Imaging/General -I/opt/bld/s5nj/VTKv9-build/Imaging/Sources -I/opt/bld/s5nj/VTKv9/Imaging/Sources -I/opt/bld/s5nj/VTKv9-build/Imaging/Statistics -I/opt/bld/s5nj/VTKv9/Imaging/Statistics -I/opt/bld/s5nj/VTKv9-build/Imaging/Stencil -I/opt/bld/s5nj/VTKv9/Imaging/Stencil -I/opt/bld/s5nj/VTKv9-build/Interaction/Image -I/opt/bld/s5nj/VTKv9/Interaction/Image -I/opt/bld/s5nj/VTKv9-build/Imaging/Color -I/opt/bld/s5nj/VTKv9/Imaging/Color -I/opt/bld/s5nj/VTKv9-build/Interaction/Widgets -I/opt/bld/s5nj/VTKv9/Interaction/Widgets -I/opt/bld/s5nj/VTKv9-build/Filters/Hybrid -I/opt/bld/s5nj/VTKv9/Filters/Hybrid -I/opt/bld/s5nj/VTKv9-build/Filters/Modeling -I/opt/bld/s5nj/VTKv9/Filters/Modeling -I/opt/bld/s5nj/VTKv9-build/Imaging/Hybrid -I/opt/bld/s5nj/VTKv9/Imaging/Hybrid -I/opt/bld/s5nj/VTKv9-build/Rendering/Annotation -I/opt/bld/s5nj/VTKv9/Rendering/Annotation -I/opt/bld/s5nj/VTKv9-build/Rendering/Volume -I/opt/bld/s5nj/VTKv9/Rendering/Volume -I/opt/bld/s5nj/VTKv9-build/Rendering/ContextOpenGL2 -I/opt/bld/s5nj/VTKv9/Rendering/ContextOpenGL2 -I/opt/bld/s5nj/VTKv9-build/Rendering/Qt -I/opt/bld/s5nj/VTKv9/Rendering/Qt -I/opt/bld/s5nj/VTKv9-build/Filters/Texture -I/opt/bld/s5nj/VTKv9/Filters/Texture -I/opt/bld/s5nj/VTKv9-build/Rendering/Label -I/opt/bld/s5nj/VTKv9/Rendering/Label -I/opt/bld/s5nj/VTKv9-build/Rendering/VolumeOpenGL2 -I/opt/bld/s5nj/VTKv9/Rendering/VolumeOpenGL2 -I/opt/bld/s5nj/VTKv9-build/Testing/Rendering -I/opt/bld/s5nj/VTKv9/Testing/Rendering -I/opt/bld/s5nj/VTKv9-build/Testing/Core -I/opt/bld/s5nj/VTKv9/Testing/Core -I/opt/bld/s5nj/VTKv9-build/Views/Qt -I/opt/bld/s5nj/VTKv9/Views/Qt -I/opt/bld/s5nj/VTKv9-build/Infovis/Core -I/opt/bld/s5nj/VTKv9/Infovis/Core -I/opt/bld/s5nj/VTKv9-build/Views/Core -I/opt/bld/s5nj/VTKv9/Views/Core -I/opt/bld/s5nj/VTKv9-build/Views/Infovis -I/opt/bld/s5nj/VTKv9/Views/Infovis -I/opt/bld/s5nj/VTKv9-build/Charts/Core -I/opt/bld/s5nj/VTKv9/Charts/Core -I/opt/bld/s5nj/VTKv9-build/Filters/Imaging -I/opt/bld/s5nj/VTKv9/Filters/Imaging -I/opt/bld/s5nj/VTKv9-build/Infovis/Layout -I/opt/bld/s5nj/VTKv9/Infovis/Layout -I/opt/bld/s5nj/VTKv9-build/Wrapping/PythonCore -I/opt/bld/s5nj/VTKv9/Wrapping/PythonCore -I/opt/bld/s5nj/VTKv9-build/Utilities/Python -I/opt/bld/s5nj/VTKv9/Utilities/Python -I/opt/bld/s5nj/python-install/include/python2.7 -I/opt/bld/s5nj/VTKv9-build/Utilities/PythonInterpreter -I/opt/bld/s5nj/VTKv9/Utilities/PythonInterpreter -I/opt/bld/s5nj/VTKv9-build/Wrapping/Tools -I/opt/bld/s5nj/VTKv9/Wrapping/Tools -I/opt/bld/s5nj/CTK/Libs/Core -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Core -I/opt/bld/s5nj/CTK-build/CTK-build -I/opt/bld/s5nj/CTK/Libs/Widgets -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Widgets -I/opt/bld/s5nj/CTK/Libs/DICOM/Core -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/DICOM/Core -I/opt/bld/s5nj/DCMTK-build/config/include -I/opt/bld/s5nj/DCMTK/ofstd/include -I/opt/bld/s5nj/DCMTK/oflog/include -I/opt/bld/s5nj/DCMTK/dcmdata/include -I/opt/bld/s5nj/DCMTK/dcmimgle/include -I/opt/bld/s5nj/DCMTK/dcmimage/include -I/opt/bld/s5nj/DCMTK/dcmjpeg/include -I/opt/bld/s5nj/DCMTK/dcmjpls/include -I/opt/bld/s5nj/DCMTK/dcmtls/include -I/opt/bld/s5nj/DCMTK/dcmnet/include -I/opt/bld/s5nj/DCMTK/dcmsr/include -I/opt/bld/s5nj/DCMTK/dcmsign/include -I/opt/bld/s5nj/DCMTK/dcmwlm/include -I/opt/bld/s5nj/DCMTK/dcmqrdb/include -I/opt/bld/s5nj/DCMTK/dcmpstat/include -I/opt/bld/s5nj/DCMTK/dcmrt/include -I/opt/bld/s5nj/DCMTK/dcmiod/include -I/opt/bld/s5nj/DCMTK/dcmfg/include -I/opt/bld/s5nj/DCMTK/dcmseg/include -I/opt/bld/s5nj/DCMTK/dcmtract/include -I/opt/bld/s5nj/DCMTK/dcmpmap/include -I/opt/bld/s5nj/CTK/Libs/DICOM/Widgets -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/DICOM/Widgets -I/opt/bld/s5nj/CTK/Libs/ImageProcessing/ITK/Core -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/ImageProcessing/ITK/Core -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/DoubleConversion/src/double-conversion -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/DoubleConversion/src/double-conversion -I/opt/bld/s5nj/ITKv4/Modules/Core/FiniteDifference/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/CurvatureFlow/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/AnisotropicSmoothing/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/LabelMap/include -I/opt/bld/s5nj/ITKv4/Modules/Core/Mesh/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Thresholding/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/ConnectedComponents/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/MathematicalMorphology/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/BinaryMathematicalMorphology/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageLabel/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/NarrowBand/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/DistanceMap/include -I/opt/bld/s5nj/ITKv4/Modules/Core/QuadEdgeMesh/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/FastMarching/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageCompare/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Smoothing/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageGradient/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageSources/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageFeature/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/Optimizers/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/SignedDistanceFunction/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/LevelSets/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/AntiAlias/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/Polynomials/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/BiasCorrection/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/BioCell/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/Classifiers/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Colormap/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/FFT/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Convolution/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/DICOMParser/src/DICOMParser -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/DICOMParser/src/DICOMParser -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Deconvolution/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/DeformableMesh/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/Denoising/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/DiffusionTensorImage/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/Eigen/include -I/opt/bld/s5nj/ITKv4/Modules/IO/XML/include -I/opt/bld/s5nj/ITKv4/Modules/IO/SpatialObjects/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/Common/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/FEM/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/PDEDeformable/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/FEM/include -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/NIFTI/src/nifti/niftilib -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/NIFTI/src/nifti/znzlib -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/GIFTI/src/gifticlib -I/opt/bld/s5nj/ITKv4/Modules/Core/GPUCommon/include -I/opt/bld/s5nj/ITKv4/Modules/Core/GPUFiniteDifference/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/GPUAnisotropicSmoothing/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/GPUImageFilterBase/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/GPUCommon/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/GPUPDEDeformable/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/GPUSmoothing/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/GPUThresholding/include -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/HDF5/src -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/HDF5/src -I/opt/bld/s5nj/ITKv4/Modules/IO/CSV/include -I/opt/bld/s5nj/ITKv4/Modules/IO/IPL/include -I/opt/bld/s5nj/ITKv4/Modules/IO/GE/include -I/opt/bld/s5nj/ITKv4/Modules/IO/HDF5/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/JPEG/src -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/JPEG/src -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/TIFF/src -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/TIFF/src/itktiff -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/TIFF/src -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/MINC -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/MINC -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/MINC/src/libminc -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/MINC/src/libminc/libcommon -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/MINC/src/libminc/libsrc2 -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/MINC/src/libminc/volume_io/Include -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/HDF5/src/itkhdf5 -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/HDF5/src/itkhdf5 -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/HDF5/src/itkhdf5/src -I/opt/bld/s5nj/ITKv4/Modules/IO/Mesh/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/NrrdIO/src/NrrdIO -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/NrrdIO/src/NrrdIO -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/PNG/src -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/PNG/src -I/opt/bld/s5nj/ITKv4/Modules/IO/RAW/include -I/opt/bld/s5nj/ITKv4/Modules/IO/Siemens/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageFusion/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/ImageNoise/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/KLMRegionGrowing/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/LabelVoting/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/LevelSetsv4/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/MarkovRandomFieldsClassifiers/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/Optimizersv4/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/Metricsv4/include -I/opt/bld/s5nj/ITKv4/Modules/Numerics/NeuralNetworks/include -I/opt/bld/s5nj/ITKv4-build/Modules/ThirdParty/OpenJPEG/src/openjpeg -I/opt/bld/s5nj/ITKv4/Modules/ThirdParty/OpenJPEG/src/openjpeg -I/opt/bld/s5nj/ITKv4/Modules/Filtering/QuadEdgeMeshFiltering/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/RegionGrowing/include -I/opt/bld/s5nj/ITKv4/Modules/Registration/RegistrationMethodsv4/include -I/opt/bld/s5nj/ITKv4/Modules/Filtering/SpatialFunction/include -I/opt/bld/s5nj/ITKv4/Modules/Bridge/VTK/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/Voronoi/include -I/opt/bld/s5nj/ITKv4/Modules/Segmentation/Watersheds/include -I/opt/bld/s5nj/ITKv4/Modules/Nonunit/Review/include -I/opt/bld/s5nj/ITKv4/Modules/Core/TestKernel/include -I/opt/bld/s5nj/ITKv4/Modules/Video/Core/include -I/opt/bld/s5nj/ITKv4/Modules/Video/Filtering/include -I/opt/bld/s5nj/ITKv4/Modules/Video/IO/include -I/opt/bld/s5nj/ITKv4/Modules/Bridge/VtkGlue/include -I/opt/bld/s5nj/CTK/Libs/Scripting/Python/Core -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Scripting/Python/Core -I/opt/bld/s5nj/CTK-build/CMakeExternals/Install/include/PythonQt -I/opt/bld/s5nj/CTK/Libs/Scripting/Python/Widgets -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Scripting/Python/Widgets -I/opt/bld/s5nj/CTK/Libs/Visualization/VTK/Core -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Visualization/VTK/Core -I/opt/bld/s5nj/VTKv9-build/Domains/Chemistry -I/opt/bld/s5nj/VTKv9/Domains/Chemistry -I/opt/bld/s5nj/VTKv9-build/Domains/ChemistryOpenGL2 -I/opt/bld/s5nj/VTKv9/Domains/ChemistryOpenGL2 -I/opt/bld/s5nj/VTKv9-build/Parallel/Core -I/opt/bld/s5nj/VTKv9/Parallel/Core -I/opt/bld/s5nj/VTKv9-build/Filters/AMR -I/opt/bld/s5nj/VTKv9/Filters/AMR -I/opt/bld/s5nj/VTKv9-build/Filters/Generic -I/opt/bld/s5nj/VTKv9/Filters/Generic -I/opt/bld/s5nj/VTKv9-build/Filters/HyperTree -I/opt/bld/s5nj/VTKv9/Filters/HyperTree -I/opt/bld/s5nj/VTKv9-build/Filters/Parallel -I/opt/bld/s5nj/VTKv9/Filters/Parallel -I/opt/bld/s5nj/VTKv9-build/Filters/ParallelImaging -I/opt/bld/s5nj/VTKv9/Filters/ParallelImaging -I/opt/bld/s5nj/VTKv9-build/Filters/Points -I/opt/bld/s5nj/VTKv9/Filters/Points -I/opt/bld/s5nj/VTKv9-build/Filters/Programmable -I/opt/bld/s5nj/VTKv9/Filters/Programmable -I/opt/bld/s5nj/VTKv9-build/Filters/Python -I/opt/bld/s5nj/VTKv9/Filters/Python -I/opt/bld/s5nj/VTKv9-build/Filters/SMP -I/opt/bld/s5nj/VTKv9/Filters/SMP -I/opt/bld/s5nj/VTKv9-build/Filters/Selection -I/opt/bld/s5nj/VTKv9/Filters/Selection -I/opt/bld/s5nj/VTKv9-build/Filters/Topology -I/opt/bld/s5nj/VTKv9/Filters/Topology -I/opt/bld/s5nj/VTKv9-build/ThirdParty/verdict -I/opt/bld/s5nj/VTKv9/ThirdParty/verdict -I/opt/bld/s5nj/VTKv9-build/Filters/Verdict -I/opt/bld/s5nj/VTKv9/Filters/Verdict -I/opt/bld/s5nj/VTKv9/ThirdParty/libproj4/vtklibproj4 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/libproj4/vtklibproj4 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/libproj4 -I/opt/bld/s5nj/VTKv9/ThirdParty/libproj4 -I/opt/bld/s5nj/VTKv9-build/Geovis/Core -I/opt/bld/s5nj/VTKv9/Geovis/Core -I/opt/bld/s5nj/VTKv9-build/ThirdParty/hdf5/vtkhdf5 -I/opt/bld/s5nj/VTKv9/ThirdParty/hdf5/vtkhdf5/hl/src -I/opt/bld/s5nj/VTKv9/ThirdParty/hdf5/vtkhdf5/src -I/opt/bld/s5nj/VTKv9-build/ThirdParty/hdf5 -I/opt/bld/s5nj/VTKv9/ThirdParty/hdf5 -I/opt/bld/s5nj/VTKv9-build/IO/AMR -I/opt/bld/s5nj/VTKv9/IO/AMR -I/opt/bld/s5nj/VTKv9-build/IO/EnSight -I/opt/bld/s5nj/VTKv9/IO/EnSight -I/opt/bld/s5nj/VTKv9/ThirdParty/netcdf/vtknetcdf/include -I/opt/bld/s5nj/VTKv9-build/ThirdParty/netcdf/vtknetcdf -I/opt/bld/s5nj/VTKv9-build/ThirdParty/netcdf -I/opt/bld/s5nj/VTKv9/ThirdParty/netcdf -I/opt/bld/s5nj/VTKv9-build/ThirdParty/exodusII -I/opt/bld/s5nj/VTKv9/ThirdParty/exodusII -I/opt/bld/s5nj/VTKv9-build/IO/Exodus -I/opt/bld/s5nj/VTKv9/IO/Exodus -I/opt/bld/s5nj/VTKv9-build/IO/ExportOpenGL2 -I/opt/bld/s5nj/VTKv9/IO/ExportOpenGL2 -I/opt/bld/s5nj/VTKv9-build/IO/Geometry -I/opt/bld/s5nj/VTKv9/IO/Geometry -I/opt/bld/s5nj/VTKv9-build/IO/Import -I/opt/bld/s5nj/VTKv9/IO/Import -I/opt/bld/s5nj/VTKv9-build/ThirdParty/libxml2/vtklibxml2 -I/opt/bld/s5nj/VTKv9-build/ThirdParty/libxml2 -I/opt/bld/s5nj/VTKv9/ThirdParty/libxml2 -I/opt/bld/s5nj/VTKv9-build/IO/Infovis -I/opt/bld/s5nj/VTKv9/IO/Infovis -I/opt/bld/s5nj/VTKv9-build/IO/LSDyna -I/opt/bld/s5nj/VTKv9/IO/LSDyna -I/opt/bld/s5nj/VTKv9-build/IO/MINC -I/opt/bld/s5nj/VTKv9/IO/MINC -I/opt/bld/s5nj/VTKv9-build/ThirdParty/oggtheora -I/opt/bld/s5nj/VTKv9/ThirdParty/oggtheora -I/opt/bld/s5nj/VTKv9-build/IO/Movie -I/opt/bld/s5nj/VTKv9/IO/Movie -I/opt/bld/s5nj/VTKv9-build/ThirdParty/netcdfcpp -I/opt/bld/s5nj/VTKv9/ThirdParty/netcdfcpp -I/opt/bld/s5nj/VTKv9-build/IO/NetCDF -I/opt/bld/s5nj/VTKv9/IO/NetCDF -I/opt/bld/s5nj/VTKv9-build/ThirdParty/jsoncpp -I/opt/bld/s5nj/VTKv9/ThirdParty/jsoncpp -I/opt/bld/s5nj/VTKv9-build/IO/Parallel -I/opt/bld/s5nj/VTKv9/IO/Parallel -I/opt/bld/s5nj/VTKv9-build/IO/ParallelXML -I/opt/bld/s5nj/VTKv9/IO/ParallelXML -I/opt/bld/s5nj/VTKv9-build/IO/TecplotTable -I/opt/bld/s5nj/VTKv9/IO/TecplotTable -I/opt/bld/s5nj/VTKv9-build/IO/Video -I/opt/bld/s5nj/VTKv9/IO/Video -I/opt/bld/s5nj/VTKv9-build/Rendering/Image -I/opt/bld/s5nj/VTKv9/Rendering/Image -I/opt/bld/s5nj/VTKv9-build/Rendering/LOD -I/opt/bld/s5nj/VTKv9/Rendering/LOD -I/opt/bld/s5nj/VTKv9-build/Views/Context2D -I/opt/bld/s5nj/VTKv9/Views/Context2D -I/opt/bld/s5nj/CTK/Libs/Visualization/VTK/Widgets -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets -I/opt/bld/s5nj/CTK/Libs/QtTesting -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/QtTesting -I/opt/bld/s5nj/CTK-build/QtTesting -I/opt/bld/s5nj/CTK-build/QtTesting-build -I/opt/bld/s5nj/CTK/Libs/Testing -I/opt/bld/s5nj/CTK-build/CTK-build/Libs/Testing -I/opt/bld/s5nj/teem-build/include -I/Users/inorton/git/slcr/s5/CMake -I/Users/inorton/git/slcr/s5 -I. -I/Users/inorton/git/slcr/s5/Libs/ITKFactoryRegistration -ILibs/ITKFactoryRegistration        -g -arch x86_64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk -mmacosx-version-min=10.9 -fPIC   -std=c++11 -o Libs/ITKFactoryRegistration/CMakeFiles/ITKFactoryRegistration.dir/itkFactoryRegistration.cxx.o -c /Users/inorton/git/slcr/s5/Libs/ITKFactoryRegistration/itkFactoryRegistration.cxx",
</code></pre>

---

## Post #2 by @jcfr (2018-01-17 15:09 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="1" data-topic="1862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Is there a reason we are setting the include path to both source and the build directory for VTK and ITK?</p>
</blockquote>
</aside>
<p>Yes. This ensure that the generated header files associated with each project can be included. Example of generated file is the export header.</p>
<p>It is true we could generate all files in a common directory and reduce the number of includes.</p>

---

## Post #3 by @adamrankin (2018-01-17 15:25 UTC)

<p>Given the Windows path length issues, this would be a greatly appreciated undertaking. Maybe even installing to a build folder (VTKv9-install, etc…)?</p>
<p>Edit: the undertaking is reducing the number of includes</p>

---

## Post #4 by @jcfr (2018-01-17 16:01 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="3" data-topic="1862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>installing to a build folder</p>
</blockquote>
</aside>
<p>Few comments:</p>
<ul>
<li>
<p>I don’t think ITK (and VTK) support being used from an install tree (cc: <a class="mention" href="/u/thewtex">@thewtex</a> <a class="mention" href="/u/fbudin69500">@fbudin69500</a> )</p>
</li>
<li>
<p>installing the libraries would currently cause more headache to properly support macOS fixup (aka package generation)</p>
</li>
</ul>

---

## Post #5 by @thewtex (2018-01-17 16:24 UTC)

<p>ITK and VTK support being used from an install tree with the caveat that ITK can only be extended with additional external modules from a build tree. Since I use this feature from Slicer extensions, it would be nice to keep it :-).</p>

---

## Post #6 by @thewtex (2018-01-17 16:29 UTC)

<aside class="quote no-group" data-username="thewtex" data-post="5" data-topic="1862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thewtex/48/32_2.png" class="avatar"> thewtex:</div>
<blockquote>
<p>Since I use this feature from Slicer extensions, it would be nice to keep it :-).</p>
</blockquote>
</aside>
<p>Then again, if the ITK build directory is also provided, with some the external module could still be built again ITK’s build tree and installed into the common install prefix. That assumes that there are not any packaging issues – <a class="mention" href="/u/jcfr">@jcfr</a> has the best perspective on how extensions are packaged.</p>

---

## Post #7 by @ihnorton (2018-01-17 18:36 UTC)

<p>Inspired by this discussion, here is a related change that I’ve wanted for a long time:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/870">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/870" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/870" target="_blank" rel="noopener">Add ability to specify only the Initialization transform.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:33" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:33" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
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
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=870). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It needs some build system fixes, so I haven’t tried to build it yet <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> but spot-checks look correct, and it is completely scripted (runs on in ~1s) so it’s very easy to make tweaks and re-run.</p>
<p>The idea is that we would then need to pass only a single path, e.g. <code>/path/to/SuperBuild/VTKv9/</code> containing VTK source checked out in the subdirectory <code>vtk</code>.</p>

---

## Post #8 by @ihnorton (2018-01-17 18:44 UTC)

<p>Here is an example:</p>
<pre><code class="lang-auto">-#include &lt;vtkAlgorithm.h&gt;
</code></pre>
<p>becomes</p>
<pre><code class="lang-auto">+#include &lt;vtk/Common/ExecutionModel/vtkAlgorithm.h&gt;
</code></pre>
<p>And we would then use a single include specifier: <code>-I/path/to/SuperBuild/VTKv9/</code>, assuming VTK source is in <code>/path/to/SuperBuild/VTKv9/vtk</code> as noted above.</p>

---

## Post #9 by @jcfr (2018-01-17 18:55 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="7" data-topic="1862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>The idea is that we would then need to pass only a single path, e.g. /path/to/SuperBuild/VTKv9/ containing VTK source checked out in the subdirectory vtk.</p>
</blockquote>
</aside>
<p>I like where this is going.</p>
<p>The challenge is that we still need to pass the same number of build directory for VTK. Currently the export header are generated in each sub directory.</p>
<p>To obtain the same reduction in number include directories, we could instead generate all export header in a single directory.</p>
<p>The following files would have be updated:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L759">
  <header class="source">

      <a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L759" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L759" target="_blank" rel="noopener">Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L759</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="749" style="counter-reset: li-counter 748 ;">
          <li># include \"vtkAutoInit.h\"</li>
          <li>VTK_AUTOINIT(${vtk-module})</li>
          <li>#endif")</li>
          <li>  endif()</li>
          <li></li>
          <li>  # Generate the export macro header for symbol visibility/Windows DLL declspec</li>
          <li>  if(target_suffix)</li>
          <li>    set(${vtk-module}${target_suffix}_EXPORT_CODE</li>
          <li>      ${${vtk-module}_EXPORT_CODE})</li>
          <li>  endif()</li>
          <li class="selected">  vtk_generate_export_header(${vtk-module}${export_symbol_object} EXPORT_FILE_NAME ${vtk-module}Module.h)</li>
          <li>  if (BUILD_SHARED_LIBS)</li>
          <li>    # export flags are only added when building shared libs, they cause</li>
          <li>    # mismatched visibility warnings when building statically since not all</li>
          <li>    # libraries that VTK builds don't set visibility flags. Until we get a</li>
          <li>    # time to do that, we skip visibility flags for static libraries.</li>
          <li>    set_property(TARGET ${vtk-module}${target_suffix}</li>
          <li>                 PROPERTY CXX_VISIBILITY_PRESET "hidden")</li>
          <li>  endif()</li>
          <li></li>
          <li>  if(BUILD_TESTING AND PYTHON_EXECUTABLE AND NOT ${vtk-module}_NO_HeaderTest AND VTK_SOURCE_DIR)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L195">
  <header class="source">

      <a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L195" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L195" target="_blank" rel="noopener">Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkModuleMacros.cmake#L195</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="185" style="counter-reset: li-counter 184 ;">
          <li></li>
          <li></li>
          <li># vtk_module_impl()</li>
          <li>#</li>
          <li># This macro provides module implementation, setting up important variables</li>
          <li># necessary to build a module. It assumes we are in the directory of the module.</li>
          <li>macro(vtk_module_impl)</li>
          <li>  include(module.cmake OPTIONAL) # Load module meta-data</li>
          <li></li>
          <li>  list(APPEND ${vtk-module}_INCLUDE_DIRS</li>
          <li class="selected">    ${${vtk-module}_BINARY_DIR}</li>
          <li>    ${${vtk-module}_SOURCE_DIR})</li>
          <li>  list(REMOVE_DUPLICATES ${vtk-module}_INCLUDE_DIRS)</li>
          <li>  if(${vtk-module}_INCLUDE_DIRS)</li>
          <li>    include_directories(${${vtk-module}_INCLUDE_DIRS})</li>
          <li>  endif()</li>
          <li></li>
          <li>  vtk_module_config(_dep ${${vtk-module}_DEPENDS})</li>
          <li>  if(_dep_INCLUDE_DIRS)</li>
          <li>    include_directories(${_dep_INCLUDE_DIRS})</li>
          <li>    # This variable is used in vtkWrapping.cmake</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Similar changes could also be applied to Slicer and CTK libraries</p>

---

## Post #10 by @ihnorton (2018-01-17 19:26 UTC)

<p>Hmm, thinking about this a little bit more, the PR870 idea may be problematic because VTK itself doesn’t specify relative include paths internally. I guess we pass all subdirectory permutations to work around this (does every VTK client really do this?).</p>
<p>Assuming VTK doesn’t want to apply the same library-style path fix in PR870 <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:">…</p>
<p>…an alternative is that we copy all of the headers for VTK (and ITK) into a single directory in our build system. This requires no <code>#include</code> changes, just build system changes, and has the same effect of reducing the path specification to 1-2 (assuming we retarget the Export headers as <a class="mention" href="/u/jcfr">@jcfr</a> mentioned).</p>
<p>(side note: in this scenario the copy script would need to exclude <code>VTKv9/Examples/</code> because there are about 20 duplicate-named headers)</p>

---

## Post #11 by @jcfr (2018-01-17 19:54 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="10" data-topic="1862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>we copy all of the headers for VTK (and ITK) into a single directory in our build system</p>
</blockquote>
</aside>
<p>Since VTK build system is being improved to fully leverage “modern CMake” and target properties, it will be difficult (if not already the case) to exclude the build directories from the target exported in <code>VTKConfig</code>.</p>
<p>Instead, it should be possible to add an option to VTK named asking the build system to copy all headers of enabled modules into a single directory at build time.</p>

---

## Post #12 by @jcfr (2019-06-21 07:00 UTC)

<p>To conclude, the associated pull request <a href="https://github.com/Slicer/Slicer/pull/870" rel="nofollow noopener">PR#870</a> has been abandoned.</p>

---
