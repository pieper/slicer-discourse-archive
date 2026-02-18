# AI Segmentation error with MOOSE (non zero exit status, check the FOV) and MONAIAuto3DSeg

**Topic ID**: 42761
**Date**: 2025-05-01
**URL**: https://discourse.slicer.org/t/ai-segmentation-error-with-moose-non-zero-exit-status-check-the-fov-and-monaiauto3dseg/42761

---

## Post #1 by @j_bu (2025-05-01 15:03 UTC)

<p>Hello all,<br>
I want to compare different segemantations but I always get exceptions. Please help, thank you very much in advance.<br>
Total Segmentator works. After opening my CT scan I get the output: “[VTK] There is more than one file, use the vtkITKArchetypeImageSeriesReader instead”. I am not sure if that is the cause of all the problems or not but I coundn´t find any good tips on how to fix my problems nor am I precisely sure what the real cause of all the trouble is.</p>
<ol>
<li>I tried to work with Moose but I get the following exceptions:</li>
</ol>
<pre><code class="lang-auto">[DEBUG][Qt] 01.05.2025 15:32:48 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-33216/PyTorch/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/NNUNet/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/SlicerPythonTestRunner/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/CleverSeg/lib/Slicer-5.8/qt-loadable-modules, slicer.org/Extensions-33216/CleverSeg/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/RegularizedFastMarching/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/TomoSAM/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/SlicerMOOSE/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/AirwaySegmentation/lib/Slicer-5.8/cli-modules, slicer.org/Extensions-33216/AirwaySegmentation/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/TorchIO/lib/Slicer-5.8/qt-scripted-modules, slicer.org/Extensions-33216/ImageAugmenter/lib/Slicer-5.8/qt-scripted-modules

[DEBUG][Python] 01.05.2025 15:32:55 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor

[DEBUG][Python] 01.05.2025 15:32:55 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics

[DEBUG][Qt] 01.05.2025 15:32:55 [] (unknown:0) - Switch to module: "Welcome"

[INFO][Python] 01.05.2025 15:32:55 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules

[ERROR][VTK] 01.05.2025 15:33:28 [vtkITKArchetypeDiffusionTensorImageReaderFile (00000246F437B110)] (vtkITKArchetypeDiffusionTensorImageReaderFile.cxx:165) - There is more than one file, use the vtkITKArchetypeImageSeriesReader instead

[DEBUG][Qt] 01.05.2025 15:33:29 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/johan/Documents/Slicer_Sets/Test_Sets/CT/3/DICOM_anon/i0000,0000b.dcm" "[1.38s]"

[DEBUG][Qt] 01.05.2025 15:33:33 [] (unknown:0) - Switch to module: "MOOSE"

[ERROR][Python] 01.05.2025 15:34:14 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\bin\Python\slicer\util.py:3057) - Error during MOOSE segmentation: Command '['C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\johan\\AppData\\Local\\slicer.org\\Slicer 5.8.0\\lib\\Python\\Scripts\\moosez.exe', '--main_directory', 'C:/Users/johan/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-01_15+33+34.473', '--model_names', 'clin_ct_body_composition']' returned non-zero exit status 1.

[ERROR][Python] 01.05.2025 15:34:41 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\bin\Python\slicer\util.py:3057) - Could not infer segmentation from provided dataset. Check the FOV.
</code></pre>
<ol start="2">
<li>I started using MONAI at it works if I use the Abdominal organs TS2 - quick but if I want to segment the whole body via any of the whole body segmentation T1 or T2 it just says “Processing faild with error code [1]”:</li>
</ol>
<pre><code class="lang-auto">[DEBUG][Python] 01.05.2025 15:35:57 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor

[DEBUG][Python] 01.05.2025 15:35:57 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics

[DEBUG][Qt] 01.05.2025 15:35:58 [] (unknown:0) - Switch to module: "Welcome"

[INFO][Python] 01.05.2025 15:35:58 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules

[ERROR][VTK] 01.05.2025 15:36:19 [vtkITKArchetypeDiffusionTensorImageReaderFile (00000249F5CD19B0)] (vtkITKArchetypeDiffusionTensorImageReaderFile.cxx:165) - There is more than one file, use the vtkITKArchetypeImageSeriesReader instead

[DEBUG][Qt] 01.05.2025 15:36:20 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/johan/Documents/Slicer_Sets/Test_Sets/CT/3/DICOM_anon/i0000,0000b.dcm" "[1.36s]"

[DEBUG][Qt] 01.05.2025 15:36:32 [] (unknown:0) - Switch to module: "MONAIAuto3DSeg"

[INFO][Python] 01.05.2025 15:36:48 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\dependency_handler.py:68) - Initializing PyTorch...

[INFO][Python] 01.05.2025 15:36:52 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/PyTorch/lib/Slicer-5.8/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...

[INFO][Python] 01.05.2025 15:36:52 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/PyTorch/lib/Slicer-5.8/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.5.1+cpu imported successfully

[INFO][Python] 01.05.2025 15:36:52 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/PyTorch/lib/Slicer-5.8/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: False

[INFO][Python] 01.05.2025 15:36:52 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\dependency_handler.py:84) - Initializing MONAI...

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: monai&gt;=1.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.4.0)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: numpy&lt;2.0,&gt;=1.24 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.26.4)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: torch&gt;=1.9 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (2.5.1)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk&gt;=5.2 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: pyyaml in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (6.0.2)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: tensorboard in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (2.19.0)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: psutil in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (7.0.0)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: nibabel in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.3.2)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: tqdm&gt;=4.47.0 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (4.67.1)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: fire in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (0.7.0)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: scikit-image&gt;=0.14.2 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (0.24.0)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: pynrrd in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.1.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk-core==5.4.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from itk&gt;=5.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk-numerics==5.4.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from itk&gt;=5.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk-io==5.4.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from itk&gt;=5.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk-filtering==5.4.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from itk&gt;=5.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk-registration==5.4.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from itk&gt;=5.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: itk-segmentation==5.4.3 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from itk&gt;=5.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (5.4.3)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: scipy&gt;=1.9 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.13.1)

[INFO][Stream] 01.05.2025 15:36:55 [] (unknown:0) - Requirement already satisfied: networkx&gt;=2.8 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.2.1)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: pillow&gt;=9.1 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (10.3.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: imageio&gt;=2.33 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (2.37.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: tifffile&gt;=2022.8.12 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (2024.8.30)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: packaging&gt;=21 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (24.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: lazy-loader&gt;=0.4 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from scikit-image&gt;=0.14.2-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (0.4)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: filelock in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from torch&gt;=1.9-&gt;monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.13.1)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: typing-extensions&gt;=4.8.0 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from torch&gt;=1.9-&gt;monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (4.12.1)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: jinja2 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from torch&gt;=1.9-&gt;monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.1.6)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: fsspec in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from torch&gt;=1.9-&gt;monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (2024.6.1)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: sympy==1.13.1 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from torch&gt;=1.9-&gt;monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.13.1)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from sympy==1.13.1-&gt;torch&gt;=1.9-&gt;monai&gt;=1.3-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.3.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: colorama in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tqdm&gt;=4.47.0-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (0.4.6)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: termcolor in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from fire-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.0.1)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: importlib-resources&gt;=5.12 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from nibabel-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (6.5.2)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: absl-py&gt;=0.4 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (2.2.2)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: grpcio&gt;=1.48.2 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.71.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: markdown&gt;=2.6.8 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.8)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: protobuf!=4.24.0,&gt;=3.19.6 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (6.30.2)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: setuptools&gt;=41.0.0 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (70.0.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: six&gt;1.9 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (1.16.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (0.7.2)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: werkzeug&gt;=1.0.1 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.1.3)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: zipp&gt;=3.1.0 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from importlib-resources&gt;=5.12-&gt;nibabel-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.21.0)

[INFO][Stream] 01.05.2025 15:36:56 [] (unknown:0) - Requirement already satisfied: importlib-metadata&gt;=4.4 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from markdown&gt;=2.6.8-&gt;tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (8.6.1)

[INFO][Stream] 01.05.2025 15:36:57 [] (unknown:0) - Requirement already satisfied: MarkupSafe&gt;=2.1.1 in c:\users\johan\appdata\local\slicer.org\slicer 5.8.0\lib\python\lib\site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard-&gt;monai[fire,itk,nibabel,psutil,pynrrd,pyyaml,skimage,tensorboard,tqdm]&gt;=1.3) (3.0.2)

[INFO][Python] 01.05.2025 15:36:58 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\dependency_handler.py:95) - Dependencies are set up successfully.

[INFO][Python] 01.05.2025 15:36:58 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1270) - Processing started

[INFO][Python] 01.05.2025 15:36:58 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1291) - Writing input file to C:/Users/johan/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-01_15+36+58.596/input-volume0.nrrd

[INFO][Python] 01.05.2025 15:36:59 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1312) - Creating segmentations with MONAIAuto3DSeg AI...

[INFO][Python] 01.05.2025 15:36:59 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1313) - Auto3DSeg command: ['C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\johan\\AppData\\Local\\slicer.org\\Slicer 5.8.0\\slicer.org\\Extensions-33216\\MONAIAuto3DSeg\\lib\\Slicer-5.8\\qt-scripted-modules\\Scripts\\auto3dseg_segresnet_inference.py', '--model-file', 'C:\\Users\\johan\\.MONAIAuto3DSeg\\models\\whole-body-3mm-v2.0.0\\model.pt', '--image-file', 'C:/Users/johan/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-01_15+36+58.596/input-volume0.nrrd', '--result-file', 'C:/Users/johan/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-01_15+36+58.596/output-segmentation.nrrd']

[DEBUG][Python] 01.05.2025 15:36:59 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\process.py:225) - Launching process: ['C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\johan\\AppData\\Local\\slicer.org\\Slicer 5.8.0\\slicer.org\\Extensions-33216\\MONAIAuto3DSeg\\lib\\Slicer-5.8\\qt-scripted-modules\\Scripts\\auto3dseg_segresnet_inference.py', '--model-file', 'C:\\Users\\johan\\.MONAIAuto3DSeg\\models\\whole-body-3mm-v2.0.0\\model.pt', '--image-file', 'C:/Users/johan/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-01_15+36+58.596/input-volume0.nrrd', '--result-file', 'C:/Users/johan/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-01_15+36+58.596/output-segmentation.nrrd']

[INFO][Python] 01.05.2025 15:36:59 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1073) - Process Started

[INFO][Python] 01.05.2025 15:37:13 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1073) - You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.

[INFO][Python] 01.05.2025 15:37:13 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\process.py:239) - You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.

[INFO][Python] 01.05.2025 15:37:14 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1073) - `apex.normalization.InstanceNorm3dNVFuser` is not installed properly, use nn.InstanceNorm3d instead.

[INFO][Python] 01.05.2025 15:37:14 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\process.py:239) - `apex.normalization.InstanceNorm3dNVFuser` is not installed properly, use nn.InstanceNorm3d instead.

[INFO][Python] 01.05.2025 15:37:16 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1073) - Model epoch 299 metric 0.8636216521263123

[INFO][Python] 01.05.2025 15:37:16 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\process.py:239) - Model epoch 299 metric 0.8636216521263123

[INFO][Python] 01.05.2025 15:37:21 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1073) - error: [C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/bin/./python-real.exe] exit abnormally - Report the problem.

[INFO][Python] 01.05.2025 15:37:21 [Python] (C:\Users\johan\AppData\Local\slicer.org\Slicer 5.8.0\slicer.org\Extensions-33216\MONAIAuto3DSeg\lib\Slicer-5.8\qt-scripted-modules\MONAIAuto3DSegLib\process.py:239) - error: [C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/bin/./python-real.exe] exit abnormally - Report the problem.

[INFO][Python] 01.05.2025 15:37:21 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1382) - Processing failed with return code 1

[INFO][Python] 01.05.2025 15:37:21 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1386) - Cleaning up temporary folder.

[INFO][Python] 01.05.2025 15:37:21 [Python] (C:/Users/johan/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules/MONAIAuto3DSeg.py:1401) - Processing failed after 22.36 seconds.
</code></pre>

---

## Post #2 by @lassoan (2025-05-01 15:14 UTC)

<aside class="quote no-group" data-username="j_bu" data-post="1" data-topic="42761">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/838e76/48.png" class="avatar"> j_bu:</div>
<blockquote>
<p>Total Segmentator works. After opening my CT scan I get the output: “[VTK] There is more than one file, use the vtkITKArchetypeImageSeriesReader instead”. I am not sure if that is the cause of all the problems or not but I coundn´t find any good tips on how to fix my problems nor am I precisely sure what the real cause of all the trouble is.</p>
</blockquote>
</aside>
<p>If TotalSegmentator works then you don’t need to worry about loading of your CT.</p>
<aside class="quote no-group" data-username="j_bu" data-post="1" data-topic="42761">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/838e76/48.png" class="avatar"> j_bu:</div>
<blockquote>
<p>I tried to work with Moose but I get the following exceptions:</p>
</blockquote>
</aside>
<p>Please ask MOOSE developers by submitting an issue to their issue tracker - <a href="https://github.com/mprires/SlicerMOOSE" class="inline-onebox">GitHub - mprires/SlicerMOOSE: Slicer extension for MOOSE</a>. Post a link here for reference for others who come across similar issue in the future.</p>
<aside class="quote no-group" data-username="j_bu" data-post="1" data-topic="42761">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/838e76/48.png" class="avatar"> j_bu:</div>
<blockquote>
<p>I started using MONAI at it works if I use the Abdominal organs TS2 - quick but if I want to segment the whole body via any of the whole body segmentation T1 or T2 it just says “Processing faild with error code [1]”</p>
</blockquote>
</aside>
<p>It seems that it actually provides some messages that indicate that processing is started but then there is a failure, probably due to running out of resources.</p>
<p>It seems that you don’t use a GPU (<code>PyTorch 2.5.1+cpu imported successfully</code>). Does your computer have a GPU? What model? How much RAM do you have in your computer? Does segmentation complete successfully if you use crop your volume (using “Crop volumes” module) to half or quarter size? Does it work with the default test data (you can get it by a single click in the module)? Do other models in MONAIAuto3DSeg model work well on your computer?</p>

---

## Post #3 by @j_bu (2025-05-01 16:06 UTC)

<p>Thank you very much for your help.<br>
I have an old Surface with 8GB RAM installed, no GPU.<br>
Don´t ask me why but after reloading, empting the trash and taking another CT I got the whole body segmentation (but still not sure how long it will work).<br>
MOOSE is still not working even after croping. I will get in touch with the developer.<br>
Thank you</p>

---

## Post #4 by @j_bu (2025-05-01 18:29 UTC)

<p>Think the problem is the laptop. Just tried on a different laptop and MONAI worked. I still have to get in touch with the developers of MOOSE. Thanks</p>

---
