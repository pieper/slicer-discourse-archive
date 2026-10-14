---
topic_id: 48483
title: "Fast model align does not operate"
date: 2026-10-12
url: https://discourse.slicer.org/t/48483
last_bumped: 2026-10-14T03:38:39.706Z
---

# Fast model align does not operate

**Topic ID**: 48483
**Date**: 2026-10-12
**URL**: https://discourse.slicer.org/t/fast-model-align-does-not-operate/48483

---

## Post #1 by @philippepellerin (2026-10-12 15:30 UTC)

<p>Hi, in the last stable release, 3D Slicer 5.12.4, the SlicerMorph- FastModelAlign extension does not operate.I know from a previous issue that this extension runs only on the stable release, so when it failed with the 3.13.0 release, I downloaded the stable 5.12.4 release, installed the Python package, then tried to run the extension, which froze on the subsampling task, as you can see in the screenshot. Did I do something wrong? Is there any way to get fastmodelalign to work?</p>
<p>Thanks for any help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d8be77a4285171abb625d2d2260891ff09acfe.jpeg" data-download-href="/uploads/short-url/kX457tY3mLo1p8mN5Wzlwv9WiCy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d8be77a4285171abb625d2d2260891ff09acfe_2_637x500.jpeg" alt="image" data-base62-sha1="kX457tY3mLo1p8mN5Wzlwv9WiCy" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d8be77a4285171abb625d2d2260891ff09acfe_2_637x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d8be77a4285171abb625d2d2260891ff09acfe_2_955x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d8be77a4285171abb625d2d2260891ff09acfe_2_1274x1000.jpeg 2x" data-dominant-color="AFAFB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1505 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-10-12 15:44 UTC)

<p>Can you provide a log file?  (Use <strong>View → Error Log</strong>)</p>

---

## Post #3 by @philippepellerin (2026-10-12 15:57 UTC)

<p>Session start time …: 20261012_170630</p>
<p>Slicer version …: 5.12.4 (revision 34645 / 4e21c19) macosx-amd64 - installed release</p>
<p>Operating system …: macOS / 26.6.2 / 25G83 / UTF-8 - 64-bit</p>
<p>Memory …: 16384 MB physical, 5120 MB virtual</p>
<p>CPU …:  Apple M2 Pro, 10 cores, 10 logical processors</p>
<p>VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>Qt configuration …: version 5.15.18, with SSL, requested OpenGL 3.2 (core profile)</p>
<p>DCMTK configuration …: version 3.7.0, no SSL</p>
<p>Internationalization …: disabled, language=</p>
<p>Developer mode …: disabled</p>
<p>Application path …: /Applications/Slicer.app/Contents/MacOS</p>
<p>Additional module paths ..: Extensions-34645/SegmentEditorExtraEffects/lib/Slicer-5.12/qt-loadable-modules, Extensions-34645/SegmentEditorExtraEffects/lib/Slicer-5.12/qt-scripted-modules, Extensions-34645/MarkupsToModel/lib/Slicer-5.12/qt-loadable-modules, Extensions-34645/SurfaceMarkup/lib/Slicer-5.12/qt-loadable-modules, Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules, Extensions-34645/Sandbox/lib/Slicer-5.12/qt-loadable-modules, Extensions-34645/Sandbox/lib/Slicer-5.12/qt-scripted-modules</p>
<p>libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>libpng warning: iCCP: known incorrect sRGB profile</p>
<p>DeserializeTerminologyEntry: Invalid type component</p>
<p>Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>Switch to module:  “Data”</p>
<p>Scripted subject hierarchy plugin registered: FormatMarkups</p>
<p>Adding SlicerMorph Volume Rendering Presets</p>
<p>GetSliceOrientationPreset: invalid orientation preset name: Reformat</p>
<p>GetSliceOrientationPreset: invalid orientation preset name: Reformat</p>
<p>GetSliceOrientationPreset: invalid orientation preset name: Reformat</p>
<p>“MRB Slicer Data Bundle” Reader has successfully read the file “/Users/philippe/Dropbox/dossier livre craniofaciale/Illustration livre craniofaciale/untitled folder 2/superposition fente 6.mrb” “[1.68s]”</p>
<p>Switch to module:  “FastModelAlign”</p>
<p>5 Python packages need to be installed.</p>
<p>This will modify Slicer’s Python environment. Continue?</p>
<p>Populating font family aliases took 169 ms. Replace uses of missing font family “Monospace” with one that exists to avoid this cost.</p>
<p>Collecting itk~=5.4.0</p>
<p>Using cached itk-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Collecting scikit-learn</p>
<p>Using cached scikit_learn-1.9.1-cp312-cp312-macosx_10_13_x86_64.whl.metadata (9.3 kB)</p>
<p>Collecting itk-fpfh~=0.2.0</p>
<p>Using cached itk_fpfh-0.2.0-cp311-abi3-macosx_10_9_x86_64.whl.metadata (16 kB)</p>
<p>Collecting itk-ransac~=0.2.1</p>
<p>Using cached itk_ransac-0.2.1-cp311-abi3-macosx_10_9_x86_64.whl.metadata (17 kB)</p>
<p>Collecting cpdalp</p>
<p>Using cached cpdalp-1.2.0-py3-none-any.whl.metadata (2.8 kB)</p>
<p>Collecting itk-core==5.4.7 (from itk~=5.4.0)</p>
<p>Using cached itk_core-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Collecting itk-numerics==5.4.7 (from itk~=5.4.0)</p>
<p>Using cached itk_numerics-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Collecting itk-io==5.4.7 (from itk~=5.4.0)</p>
<p>Using cached itk_io-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Collecting itk-filtering==5.4.7 (from itk~=5.4.0)</p>
<p>Using cached itk_filtering-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Collecting itk-registration==5.4.7 (from itk~=5.4.0)</p>
<p>Using cached itk_registration-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Collecting itk-segmentation==5.4.7 (from itk~=5.4.0)</p>
<p>Using cached itk_segmentation-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)</p>
<p>Requirement already satisfied: numpy in ./Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from itk~=5.4.0) (2.4.6)</p>
<p>Requirement already satisfied: scipy&gt;=1.10.0 in ./Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-learn) (1.17.1)</p>
<p>Collecting joblib&gt;=1.4.0 (from scikit-learn)</p>
<p>Using cached joblib-1.6.0-py3-none-any.whl.metadata (6.5 kB)</p>
<p>Collecting narwhals&gt;=2.0.1 (from scikit-learn)</p>
<p>Downloading narwhals-2.27.1-py3-none-any.whl.metadata (15 kB)</p>
<p>Collecting threadpoolctl&gt;=3.5.0 (from scikit-learn)</p>
<p>Using cached threadpoolctl-3.7.0-py3-none-any.whl.metadata (24 kB)</p>
<p>Collecting cloudpickle&gt;=3.0 (from joblib&gt;=1.4.0-&gt;scikit-learn)</p>
<p>Using cached cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)</p>
<p>Using cached itk-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (16 kB)</p>
<p>Using cached itk_core-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (71.1 MB)</p>
<p>Using cached itk_filtering-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (46.8 MB)</p>
<p>Using cached itk_io-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (22.4 MB)</p>
<p>Using cached itk_numerics-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (35.8 MB)</p>
<p>Using cached itk_registration-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (22.0 MB)</p>
<p>Using cached itk_segmentation-5.4.7-cp311-abi3-macosx_10_9_x86_64.whl (13.1 MB)</p>
<p>Using cached itk_fpfh-0.2.0-cp311-abi3-macosx_10_9_x86_64.whl (357 kB)</p>
<p>Using cached itk_ransac-0.2.1-cp311-abi3-macosx_10_9_x86_64.whl (1.6 MB)</p>
<p>Using cached scikit_learn-1.9.1-cp312-cp312-macosx_10_13_x86_64.whl (8.8 MB)</p>
<p>Using cached cpdalp-1.2.0-py3-none-any.whl (18 kB)</p>
<p>Using cached joblib-1.6.0-py3-none-any.whl (306 kB)</p>
<p>Using cached cloudpickle-3.1.2-py3-none-any.whl (22 kB)</p>
<p>Downloading narwhals-2.27.1-py3-none-any.whl (483 kB)</p>
<p>Using cached threadpoolctl-3.7.0-py3-none-any.whl (26 kB)</p>
<p>Installing collected packages: threadpoolctl, narwhals, itk-core, cpdalp, cloudpickle, joblib, itk-numerics, itk-io, scikit-learn, itk-filtering, itk-segmentation, itk-registration, itk, itk-ransac, itk-fpfh</p>
<p>Successfully installed cloudpickle-3.1.2 cpdalp-1.2.0 itk-5.4.7 itk-core-5.4.7 itk-filtering-5.4.7 itk-fpfh-0.2.0 itk-io-5.4.7 itk-numerics-5.4.7 itk-ransac-0.2.1 itk-registration-5.4.7 itk-segmentation-5.4.7 joblib-1.6.0 narwhals-2.27.1 scikit-learn-1.9.1 threadpoolctl-3.7.0</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 473, in onRunRegistrationButton</p>
<pre><code>self.sourcePoints, self.targetPoints, self.scalingTransformNode, self.ICPTransformNode, self.voxelSize = logic.ITKRegistration(

                                                                                                         ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 757, in ITKRegistration</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x600002707b40): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 473, in onRunRegistrationButton</p>
<pre><code>self.sourcePoints, self.targetPoints, self.scalingTransformNode, self.ICPTransformNode, self.voxelSize = logic.ITKRegistration(

                                                                                                         ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 757, in ITKRegistration</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x60000270bb40): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 393, in onSubsampleButton</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x60000270b3c0): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 393, in onSubsampleButton</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x600002740e40): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 393, in onSubsampleButton</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x600002737780): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 393, in onSubsampleButton</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x6000027e4780): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 393, in onSubsampleButton</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x60000276c600): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 393, in onSubsampleButton</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x600002737780): Point id doesn’t exist: 18446744073709551615</p>
<p>parameters are  {‘pointDensity’: 1.0, ‘normalSearchRadius’: 2.0, ‘FPFHNeighbors’: 100, ‘FPFHSearchRadius’: 5.0, ‘distanceThreshold’: 2.0, ‘maxRANSAC’: 1000000, ‘ICPDistanceThreshold’: 1.5, ‘alpha’: 2.0, ‘beta’: 2.0, ‘CPDIterations’: 100, ‘CPDTolerance’: 0.001, ‘gridSpacing’: 1.0, ‘gridSpacingAuto’: False, ‘Acceleration’: False, ‘GeodesicKernel’: False, ‘GeodesicTau’: 0.2, ‘BCPDFolder’: ‘’}</p>
<p>:: Loading point clouds and downsampling</p>
<p>Scale length are   286.6114269804389 260.31233478037495</p>
<p>Voxel Size is  5.2111168541897985</p>
<p>Scaling factor is  1</p>
<p>Generic Warning: In vtkMath.cxx, line 778</p>
<p>vtkMath::Jacobi: Error extracting eigenfunctions</p>
<p>------------------------------------------------------------</p>
<p>movingMeshPoints.shape  (4321, 3)</p>
<p>movingMeshPointNormals.shape  (4321, 3)</p>
<p>fixedMeshPoints.shape  (6465, 3)</p>
<p>fixedMeshPointNormals.shape  (6465, 3)</p>
<p>------------------------------------------------------------</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 473, in onRunRegistrationButton</p>
<pre><code>self.sourcePoints, self.targetPoints, self.scalingTransformNode, self.ICPTransformNode, self.voxelSize = logic.ITKRegistration(

                                                                                                         ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/FastModelAlign.py”, line 757, in ITKRegistration</p>
<pre><code>) = logic.runSubsample(

    ^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2827, in runSubsample</p>
<pre><code>source_fpfh = self.get_fpfh_feature(

              ^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34645/SlicerMorph/lib/Slicer-5.12/qt-scripted-modules/ALPACA.py”, line 2727, in get_fpfh_feature</p>
<pre><code>fpfh.ComputeFPFHFeature(pointset, normalset, float(radius), int(neighbors))
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/itk/itkPointFeaturePython.py”, line 632, in ComputeFPFHFeature</p>
<pre><code>return \_itkPointFeaturePython.itkPointFeatureMF3MF3_ComputeFPFHFeature(self, input, input_normals, radius, neighbors)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>RuntimeError: /Users/svc-dashboard/D/P/ITKPythonPackage/ITK-source/ITK/Modules/Core/Common/include/itkPointSet.hxx:190:</p>
<p>ITK ERROR: PointSet(0x6000027ee340): Point id doesn’t exist: 18446744073709551615</p>

---

## Post #4 by @pieper (2026-10-12 16:07 UTC)

<p>I’m not familiar with the internals of that module, but this looks very wrong:</p>
<blockquote>
<p>ITK ERROR: PointSet(0x600002707b40): Point id doesn’t exist: 18446744073709551615</p>
</blockquote>
<p>Probably someone who know’s the code could check if there’s a datatype issue.  Or if someone points their Claude at this I’ll bet it’s an easy fix.</p>

---

## Post #5 by @muratmaga (2026-10-12 16:21 UTC)

<p>Looks like one of your models has at least one vertex marked as NaN, and functions are failing because that.</p>
<p>Try this in your python window, and then rerun the FastModelAlign.</p>
<p><code>import numpy as np, vtk</code><br>
<code>m = getNode('MovingModel')</code><br>
<code>pts = slicer.util.arrayFromModelPoints(m)</code><br>
<code>bad = np.where(~np.isfinite(pts).all(axis=1))[0]</code><br>
<code>print(len(bad), "invalid vertices")</code><br>
<code>poly = m.GetPolyData(); poly.BuildLinks()</code><br>
<code>for i in bad:</code><br>
<code>ids = vtk.vtkIdList(); poly.GetPointCells(int(i), ids)</code><br>
<code>for k in range(ids.GetNumberOfIds()): poly.DeleteCell(ids.GetId(k))</code><br>
<code>poly.RemoveDeletedCells()</code><br>
<code>c = vtk.vtkCleanPolyData(); c.SetInputData(poly); c.Update()</code><br>
<code>m.SetAndObservePolyData(c.GetOutput())</code></p>
<p>ALPACA already detects and offers to fix these, I opened an issue to implement that for FastModelAlign too. Thanks for reporting.</p>

---

## Post #6 by @philippepellerin (2026-10-13 07:56 UTC)

<p>Thanks both of you for your help</p>

---

## Post #7 by @philippepellerin (2026-10-13 08:03 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="48483">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>import numpy as np, vtk</code><br>
<code>m = getNode('MovingModel')</code><br>
<code>pts = slicer.util.arrayFromModelPoints(m)</code><br>
<code>bad = np.where(~np.isfinite(pts).all(axis=1))[0]</code><br>
<code>print(len(bad), "invalid vertices")</code><br>
<code>poly = m.GetPolyData(); poly.BuildLinks()</code><br>
<code>for i in bad:</code><br>
<code>ids = vtk.vtkIdList(); poly.GetPointCells(int(i), ids)</code><br>
<code>for k in range(ids.GetNumberOfIds()): poly.DeleteCell(ids.GetId(k))</code><br>
<code>poly.RemoveDeletedCells()</code><br>
<code>c = vtk.vtkCleanPolyData(); c.SetInputData(poly); c.Update()</code><br>
<code>m.SetAndObservePolyData(c.GetOutput())</code></p>
</blockquote>
</aside>
<p><em>I tried your lines oc code and got this:</em></p>
<p>import numpy as np, vtk</p>
<p>m = getNode(‘MovingModel’)</p>
<p>pts = slicer.util.arrayFromModelPoints(m)</p>
<p>bad = np.where(~np.isfinite(pts).all(axis=1))[0]</p>
<p>print(len(bad), “invalid vertices”)</p>
<p>poly = m.GetPolyData(); poly.BuildLinks()</p>
<p>for i in bad:</p>
<p>ids = vtk.vtkIdList(); poly.GetPointCells(int(i), ids)</p>
<p>for k in range(ids.GetNumberOfIds()): poly.DeleteCell(ids.GetId(k))</p>
<p>poly.RemoveDeletedCells()</p>
<p>c = vtk.vtkCleanPolyData(); c.SetInputData(poly); c.Update()</p>
<p>m.SetAndObservePolyData(c.GetOutput())</p>
<p>File “”, line 8</p>
<pre><code>ids = vtk.vtkIdList(); poly.GetPointCells(int(i), ids)

^^^
</code></pre>
<p>IndentationError: expected an indented block after ‘for’ statement on line 7</p>
<p>&gt;&gt;&gt;</p>

---

## Post #8 by @muratmaga (2026-10-14 03:38 UTC)

<p>Looks like paste messed up indentations. Try this:</p>
<pre><code class="lang-auto">import numpy as np, vtk
m = getNode('MovingModel')
pts = slicer.util.arrayFromModelPoints(m)
bad = np.where(~np.isfinite(pts).all(axis=1))[0]
print(len(bad), "invalid vertices")
poly = m.GetPolyData(); poly.BuildLinks()
for i in bad:
    ids = vtk.vtkIdList(); poly.GetPointCells(int(i), ids)
    for k in range(ids.GetNumberOfIds()): poly.DeleteCell(ids.GetId(k))
poly.RemoveDeletedCells()
c = vtk.vtkCleanPolyData(); c.SetInputData(poly); c.Update()
m.SetAndObservePolyData(c.GetOutput())
</code></pre>
<p>Also make sure to replace the MovingModel with the actual name of the model failed in your tries.</p>

---
