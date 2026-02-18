# MALPACA template selection

**Topic ID**: 27530
**Date**: 2023-01-29
**URL**: https://discourse.slicer.org/t/malpaca-template-selection/27530

---

## Post #1 by @Rachel_Fleming (2023-01-29 18:02 UTC)

<p>Hello!<br>
I would like to use the MALPACA template selection tool, but I am running into an error. I went through the MALPACA tutorial with the sample data (mouse skulls) and it worked fine. Now I am trying the same thing with my data, all of which are cervical vertebrae from the same species, but I am having trouble at Step 2: Generate point clouds matched to reference.</p>
<p>Here are the steps I used:<br>
• Placed my model data (.ply) in my Downloads folder (same one I used in the tutorial). The sample data used 61 models, I’m using 16 vertebrae from a pelican. These meshes were all cleaned/repaired in Meshmixer.<br>
• Started new 3D Slicer scene and opened ALPACA module.<br>
• Template selection: selected model directory and output directory. Did not enable reference selection box.<br>
• Used spacing factor of 0.03<br>
• Selected “Step 1”. This is the output:<br>
The reference is Pelican_C10_cleaned<br>
The number of points in the downsampled reference pointcloud is 653<br>
• Selected Step 2. There is no new output text.<br>
• The output folder has 5 matching point clouds: C10, C11, C12, C13, C14.<br>
• The next step is not enabled.</p>
<p>I tried this with a spacing factor of 0.02 as well, and I tried it with a different template (C5), and it still did not let me continue on to the next steps. Is there something I am overlooking?</p>
<p>Thanks!<br>
-Rachel</p>

---

## Post #2 by @Rachel_Fleming (2023-01-29 18:13 UTC)

<p>Here is my error log:</p>
<p>ReadDataInternal ((unknown)): File ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C10_cleaned.ply does not contain coordinate system information. Assuming LPS.<br>
“Model” Reader has successfully read the file “C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C10_cleaned.ply” “[0.10s]”<br>
:: Loading point clouds and downsampling…<br>
:: Point-to-plane ICP registration is applied on original point…<br>
ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C11_cleaned.ply does not contain coordinate system information. Assuming LPS.</p>

---

## Post #3 by @muratmaga (2023-01-29 21:44 UTC)

<p><a class="mention" href="/u/rachel_fleming">@Rachel_Fleming</a> This seems part of the log. There is really no error in here. (You can ignore the ply does not contain coordinate information message).</p>
<p>Can you share your datasets or provide the whole log?</p>

---

## Post #4 by @Rachel_Fleming (2023-01-30 16:00 UTC)

<p>Sure! Here is the full log (I had to copy and paste since I couldn’t upload a .txt file):</p>
<p>[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-01-30 10:48:19<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.2.1 (revision 31317 / 77da381) win-amd64 - installed release<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 22621, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16068 MB physical, 52932 MB virtual<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 20 cores, 20 logical processors<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/rache/AppData/Local/NA-MIC/Slicer 5.2.1/bin<br>
[DEBUG][Qt] 30.01.2023 10:48:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-31317/SegmentEditorExtraEffects/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31317/SegmentEditorExtraEffects/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31317/MarkupsToModel/lib/Slicer-5.2/qt-loadable-modules<br>
[WARNING][Qt] 30.01.2023 10:48:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[WARNING][Qt] 30.01.2023 10:48:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 30.01.2023 10:48:24 [Python] (C:\Users\rache\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 30.01.2023 10:48:25 [Python] (C:\Users\rache\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 30.01.2023 10:48:25 [Python] (C:\Users\rache\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 30.01.2023 10:48:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Python] 30.01.2023 10:48:26 [Python] (C:\Users\rache\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: FormatMarkups<br>
[DEBUG][Qt] 30.01.2023 10:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “ALPACA”<br>
[INFO][VTK] 30.01.2023 10:51:32 [vtkMRMLModelStorageNode (000001AC6DC6CB20)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C10_cleaned.ply does not contain coordinate system information. Assuming LPS.<br>
[DEBUG][Qt] 30.01.2023 10:51:32 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Model” Reader has successfully read the file “C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C10_cleaned.ply” “[0.15s]”<br>
[INFO][VTK] 30.01.2023 10:51:41 [vtkMRMLModelStorageNode (000001AC6DC6C170)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C10_cleaned.ply does not contain coordinate system information. Assuming LPS.<br>
[DEBUG][Qt] 30.01.2023 10:51:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Model” Reader has successfully read the file “C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C10_cleaned.ply” “[0.14s]”<br>
[INFO][Stream] 30.01.2023 10:51:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Loading point clouds and downsampling<br>
[INFO][Stream] 30.01.2023 10:51:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:41 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: RANSAC registration on downsampled point clouds.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    Since the downsampling voxel size is 1.240,<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    we use a liberal distance threshold 3.721.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Point-to-plane ICP registration is applied on original point<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    clouds to refine the alignment. This time we use a strict<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    distance threshold 1.861.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 653<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 34880<br>
[INFO][VTK] 30.01.2023 10:51:42 [vtkMRMLModelStorageNode (000001AC6DC74530)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C11_cleaned.ply does not contain coordinate system information. Assuming LPS.<br>
[DEBUG][Qt] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Model” Reader has successfully read the file “C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C11_cleaned.ply” “[0.14s]”<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Loading point clouds and downsampling<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: RANSAC registration on downsampled point clouds.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    Since the downsampling voxel size is 1.240,<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    we use a liberal distance threshold 3.721.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Point-to-plane ICP registration is applied on original point<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    clouds to refine the alignment. This time we use a strict<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    distance threshold 1.861.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 653<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 33598<br>
[INFO][VTK] 30.01.2023 10:51:43 [vtkMRMLModelStorageNode (000001AC6DC6E260)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C12_cleaned.ply does not contain coordinate system information. Assuming LPS.<br>
[DEBUG][Qt] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Model” Reader has successfully read the file “C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C12_cleaned.ply” “[0.14s]”<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Loading point clouds and downsampling<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: RANSAC registration on downsampled point clouds.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    Since the downsampling voxel size is 1.240,<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    we use a liberal distance threshold 3.721.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Point-to-plane ICP registration is applied on original point<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    clouds to refine the alignment. This time we use a strict<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    distance threshold 1.861.<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 653<br>
[INFO][Stream] 30.01.2023 10:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 44791<br>
[INFO][VTK] 30.01.2023 10:51:44 [vtkMRMLModelStorageNode (000001AC6DC76430)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C13_cleaned.ply does not contain coordinate system information. Assuming LPS.<br>
[DEBUG][Qt] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Model” Reader has successfully read the file “C:/Users/rache/Downloads/MALPACA_test_vertebrae/CV_test_Models\Pelican_C13_cleaned.ply” “[0.17s]”<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Loading point clouds and downsampling<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Downsample with a voxel size 1.240.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Estimate normal with search radius 2.481.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: Compute FPFH feature with search radius 6.202.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - :: RANSAC registration on downsampled point clouds.<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    Since the downsampling voxel size is 1.240,<br>
[INFO][Stream] 30.01.2023 10:51:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    we use a liberal distance threshold 3.721.<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/rache/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 756, in onMatchingPointsButton<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     template_density, matchedPoints, indices, files = logic.matchingPCD(self.ui.modelsMultiSelector.currentPath, self.sparseTemplate, self.referenceNode, self.pcdOutputFolder, self.ui.spacingFactorSlider.value,<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/rache/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 1652, in matchingPCD<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ICPTransform = self.estimateTransform(sourcePoints, targetPoints, sourceFeatures, targetFeatures, voxelSize, skipScalingOption, parameterDictionary)<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/rache/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 1325, in estimateTransform<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ransac = self.execute_global_registration(sourcePoints, targetPoints, sourceFeatures, targetFeatures, voxelSize,<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/rache/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 1445, in execute_global_registration<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     evaluation = registration.evaluate_registration(target_down, source_down, distance_threshold, np.linalg.inv(result.transformation))<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “&lt;<strong>array_function</strong> internals&gt;”, line 180, in inv<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\rache\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\numpy\linalg\linalg.py”, line 552, in inv<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\rache\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\numpy\linalg\linalg.py”, line 89, in _raise_linalgerror_singular<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     raise LinAlgError(“Singular matrix”)<br>
[CRITICAL][Stream] 30.01.2023 10:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - numpy.linalg.LinAlgError: Singular matrix</p>

---

## Post #5 by @Rachel_Fleming (2023-01-30 16:10 UTC)

<p>I can also share my dataset, let me know if you still need it and I can email them to you.</p>

---

## Post #6 by @muratmaga (2023-01-30 16:20 UTC)

<p>Yes, sharing the data would be great.</p>

---

## Post #7 by @Rachel_Fleming (2023-01-30 16:21 UTC)

<p><a href="https://drive.google.com/file/d/1b0hgf4pJeTMnCDfw5VWezM1Z-srQNg92/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C2_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1OWtXWf0b4qTitaaGnLPdLfKsDWJQY_M9/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C3_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/10M_sHBViMpjMT_ynQ7dvbsQpD31TDKts/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C4_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1e2tv6puqNugFw00ZsvEC6RlKyiTxhHYY/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C5_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1IoV2n8jnq9S4aOkBFSINRw5YaBtnm82y/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C6_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1f9uJsaV88Ix346ubbuUq9SBwJTWrqPDr/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C7_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/10HbvK7qtknd7xjBIJqcGJEjrdHdf6-H5/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C8_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1YUNvrgEGlJgxtzEZ5haIIDarTwGTfEWm/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C9_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1bTOhxDvYmP3LIYVJMm55QB3D-bJyMM0x/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C10_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/14v9Fz3xlmIWJbY4QDEs6mtM1JQFqMbjp/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C11_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/16tBrX6kgURrtZy8PsqkllkkRBPKQDcn-/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C12_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1MRTUzPIMTsixIu-tiWxokdgpjE8L6Rms/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C13_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1FwTR3N9U26Qeh94ghW2t4jHOm0hmoLC6/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C14_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1PNA1d-J1utRqaydzJHwbEqKSaguUv_1J/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C15_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1WeC1_kjYbFvTRKS-K9AnIwYJULlXzd-F/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C16_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"><br>
<a href="https://drive.google.com/file/d/1gYUApSUpUyViT8zIa-_Qo4yRrsgXqB2u/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">Pelican_C17_cleaned.ply</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"></p>

---

## Post #8 by @Rachel_Fleming (2023-01-30 16:23 UTC)

<p>Alternatively, here’s a zipped folder:<br>
<a href="https://drive.google.com/file/d/1-VG0do30gLcuhG06jIvTwDkkeVxinVaX/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="16" height="16">CV_test_Models.zip</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="21" height="21"></p>

---

## Post #9 by @muratmaga (2023-01-30 17:13 UTC)

<p>Says I need permission, can you share publicly?</p>

---

## Post #10 by @Rachel_Fleming (2023-01-30 17:25 UTC)

<p>I made the link general access, did that work?</p>

---

## Post #11 by @muratmaga (2023-01-30 17:39 UTC)

<p>So, I donwloaded the data and replicate the error. We will take a look.<br>
Meanwhile, can you tell me a bit about the project? All I have a is a vertebral column. Do you have more samples (lots more)?</p>
<p>ALPACA/MALPACA will probably not going to work well if your goal is to use one or two of the vertebra to landmark the rest, given how drastically their shape changes from proximal to distal. However, if you do have a lots of specimen with the same structures, you might be able to pool the data and select a proximal vertebra to landmakr similar looking ones, a middle one in the series for similar range, and finally distal one to do the remaining ones (basically three templates).</p>
<p>Is it sort of the analysis you are looking into doing it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f355a401bb5d4070e828a1d876a0c959a87457c3.jpeg" data-download-href="/uploads/short-url/yIDvAMszcBSl3BWMsw3eml54eXN.jpeg?dl=1" title="Screen Shot 2023-01-30 at 9.34.05 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f355a401bb5d4070e828a1d876a0c959a87457c3_2_618x500.jpeg" alt="Screen Shot 2023-01-30 at 9.34.05 AM" data-base62-sha1="yIDvAMszcBSl3BWMsw3eml54eXN" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f355a401bb5d4070e828a1d876a0c959a87457c3_2_618x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f355a401bb5d4070e828a1d876a0c959a87457c3_2_927x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f355a401bb5d4070e828a1d876a0c959a87457c3_2_1236x1000.jpeg 2x" data-dominant-color="A2A4CE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-01-30 at 9.34.05 AM</span><span class="informations">1712×1384 85.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Rachel_Fleming (2023-01-30 17:49 UTC)

<p>Hi Murat,<br>
Ok! Yes I have cervical vertebrae models from a dozen species in the Pelicanimorphoae clade. I’m interested in knowing whether there is GPA clustering associated with feeding strategy (strikers, plunge divers, tactile probers, etc). In total I have around 200 models. I could choose a representative vertebra from each neck region. Though I do suspect there may be a lot of variability in shape between species.</p>

---

## Post #14 by @chz31 (2023-01-30 18:32 UTC)

<p>Hi Rachel,</p>
<p>Thanks for trying our method and posting the issue! I also looked at your dataset. Like what Murat suggested, I think the issue is that some vertebrae from one specimen are a bit too different. The generating matching pointcloud function stopped in the middle (in my case, it stopped at C3), that’s why the next step is not enabled automatically. You can check the generated matching pointclouds in the specified output folder.</p>
<p>ALPACA can still generate a reasonable registration among them, but the difference is too much for matching downsampled pointclouds in the templates selection module. For example, here is a registered C2 (red) and C3 (blue) pointclouds in ALPACA. You can use ALPACA (“single alignment” tab) to test the registration when in doubt.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab8a17903d50054f4dcf0a91f29db917ea40aec0.jpeg" data-download-href="/uploads/short-url/otvvvRgfjw2hgnSpcR51cULdqyk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab8a17903d50054f4dcf0a91f29db917ea40aec0_2_287x250.jpeg" alt="image" data-base62-sha1="otvvvRgfjw2hgnSpcR51cULdqyk" width="287" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab8a17903d50054f4dcf0a91f29db917ea40aec0_2_287x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab8a17903d50054f4dcf0a91f29db917ea40aec0_2_430x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab8a17903d50054f4dcf0a91f29db917ea40aec0_2_574x500.jpeg 2x" data-dominant-color="8F83BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">861×750 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Anyway, we’ll add a catch for this error to remind users to check for the original models. Thanks!</p>

---

## Post #15 by @muratmaga (2023-01-30 19:10 UTC)

<aside class="quote no-group" data-username="Rachel_Fleming" data-post="12" data-topic="27530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rachel_fleming/48/18113_2.png" class="avatar"> Rachel_Fleming:</div>
<blockquote>
<p>Ok! Yes I have cervical vertebrae models from a dozen species in the Pelicanimorphoae clade. I’m interested in knowing whether there is GPA clustering associated with feeding strategy (strikers, plunge divers, tactile probers, etc). In total I have around 200 models. I could choose a representative vertebra from each neck region. Though I do suspect there may be a lot of variability in shape between species.</p>
</blockquote>
</aside>
<p>To give a deeper insight, templates modules are there to help you choose what samples you can use as source to landmark the rest of the sample via ALPACA/MALPACA. For that, we do a pseudo-GPA in which we use the geometry of the samples to create a fixed number of points across samples. If the shapes of the reference specimen (selected randomly, or you can specify explicitly) and targets are too different, then that finding the corresponding points step fail. And we can’t do out pseudoGPA and kmeans clustering.</p>
<p>If you can split your samples by the region of the vertebrate (proximal cervical, middle cervicals, and distal cervicals), and pool the models that way, and rerun the templates separately for each region, you might be able to run the templates module.</p>
<p>Are you planning to use manual LMs or semiLM to digitize the shape of the vertebra?</p>

---

## Post #16 by @Rachel_Fleming (2023-01-30 20:06 UTC)

<p>Thanks for your quick responses! I am planning on using semiLMs.<br>
Later today or tomorrow I will try template selection separately on those different regions, then use PseudoLMGenerator on the selected templates, then run MALPACA. If that sounds good, I’ll get back to you soon to let you know how it went.</p>

---

## Post #17 by @muratmaga (2023-01-30 20:26 UTC)

<aside class="quote no-group" data-username="Rachel_Fleming" data-post="16" data-topic="27530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rachel_fleming/48/18113_2.png" class="avatar"> Rachel_Fleming:</div>
<blockquote>
<p>Later today or tomorrow I will try template selection separately on those different regions, then use PseudoLMGenerator on the selected templates, then run MALPACA. If that sounds good, I’ll get back to you soon to let you know how it went.</p>
</blockquote>
</aside>
<p>One more clarification. You can’t use PseudoLM generator in context of multiple template landmarking. PseudoLM generator uses the geometry of the selected to create the LMs. So if you switch to another template, a different number of point will be generated hence multi-template pipeline won’t work.</p>
<p>You can still do all of these in ALPACA though. (Run templates tool to select the template separately for each anatomical region, just choose template as 1. Generate the point cloud for that template in PseudoLMs module and then run ALPACA on the rest of the samples.) .</p>

---

## Post #18 by @Rachel_Fleming (2023-01-30 20:53 UTC)

<p>Ah that makes sense, I’ll do the separate ALPACA runs on the different regions. Thanks!! I’ll follow up after trying that out.</p>

---
