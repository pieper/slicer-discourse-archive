# My dental segmentator on the mac does not work please help

**Topic ID**: 45874
**Date**: 2026-01-23
**URL**: https://discourse.slicer.org/t/my-dental-segmentator-on-the-mac-does-not-work-please-help/45874

---

## Post #1 by @Sankalpa_Gamage (2026-01-23 05:34 UTC)

<p>[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Session start time …: 20260123_104632<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) macosx-amd64 - installed release<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Operating system …: macOS / 26.2 / 25C56 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Memory …: 16384 MB physical, 3072 MB virtual<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - CPU …:  Apple M3, 8 cores, 8 logical processors<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Qt configuration …: version 5.15.18, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Additional module paths ..: Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules, Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules, Extensions-34045/DentalSegmentator/lib/Slicer-5.10/qt-scripted-modules, Extensions-34045/SlicerPythonTestRunner/lib/Slicer-5.10/qt-scripted-modules<br>
[INFO][Stream] 23.01.2026 10:46:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[DEBUG][Python] 23.01.2026 10:46:35 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 23.01.2026 10:46:35 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 23.01.2026 10:46:35 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 23.01.2026 10:46:38 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Populating font family aliases took 155 ms. Replace uses of missing font family “Courier” with one that exists to avoid this cost.<br>
[DEBUG][Qt] 23.01.2026 10:46:40 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Python console user input: slicer.util.pip_install(“acvl_utils==0.2”)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Collecting acvl_utils==0.2<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   Using cached acvl_utils-0.2-py3-none-any.whl<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: numpy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from acvl_utils==0.2) (2.0.2)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: batchgenerators in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from acvl_utils==0.2) (0.25.1)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: torch in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from acvl_utils==0.2) (2.2.2)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: SimpleITK in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from acvl_utils==0.2) (2.5.2rc2.dev6)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: scikit-image in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from acvl_utils==0.2) (0.26.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: connected-components-3d in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from acvl_utils==0.2) (3.26.1)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: pillow&gt;=7.1.2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (11.2.1)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: scipy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.13.1)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: scikit-learn in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.8.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: future in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.0.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: pandas in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (3.0.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: unittest2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.1.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: threadpoolctl in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from batchgenerators-&gt;acvl_utils==0.2) (3.6.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: networkx&gt;=3.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-image-&gt;acvl_utils==0.2) (3.6.1)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: imageio!=2.35.0,&gt;=2.33 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-image-&gt;acvl_utils==0.2) (2.37.2)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: tifffile&gt;=2022.8.12 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-image-&gt;acvl_utils==0.2) (2026.1.14)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: packaging&gt;=21 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-image-&gt;acvl_utils==0.2) (25.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: lazy-loader&gt;=0.4 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-image-&gt;acvl_utils==0.2) (0.4)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: filelock in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from torch-&gt;acvl_utils==0.2) (3.20.3)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: typing-extensions&gt;=4.8.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from torch-&gt;acvl_utils==0.2) (4.14.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: sympy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from torch-&gt;acvl_utils==0.2) (1.14.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: jinja2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from torch-&gt;acvl_utils==0.2) (3.1.6)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: fsspec in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from torch-&gt;acvl_utils==0.2) (2026.1.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: MarkupSafe&gt;=2.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from jinja2-&gt;torch-&gt;acvl_utils==0.2) (3.0.3)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: python-dateutil&gt;=2.8.2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2.9.0.post0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: joblib&gt;=1.3.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from scikit-learn-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.5.3)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from sympy-&gt;torch-&gt;acvl_utils==0.2) (1.3.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Collecting argparse (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: six&gt;=1.4 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.17.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: traceback2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.4.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Requirement already satisfied: linecache2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages (from traceback2-&gt;unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.0.0)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Installing collected packages: argparse, acvl_utils<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   Attempting uninstall: acvl_utils<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     Found existing installation: acvl_utils 0.2.5<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     Uninstalling acvl_utils-0.2.5:<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -       Successfully uninstalled acvl_utils-0.2.5<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ERROR: pip’s dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - nnunetv2 2.6.2 requires acvl-utils&lt;0.3,&gt;=0.2.3, but you have acvl-utils 0.2 which is incompatible.<br>
[INFO][Stream] 23.01.2026 10:46:41 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Successfully installed acvl_utils-0.2 argparse-1.4.0<br>
[DEBUG][Qt] 23.01.2026 10:47:30 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[INFO][Python] 23.01.2026 10:47:32 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 23.01.2026 10:47:32 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (1048.0/4096.0) set to volume ‘11: Axial’ from SOP instance 1.76.380.18.11.1240614171306551.5272.92.170.<br>
[DEBUG][Qt] 23.01.2026 10:47:38 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “DentalSegmentator”<br>
[ERROR][VTK] 23.01.2026 10:47:38 [vtkSlicerSegmentEditorLogic (0x600003ca41a0)] (vtkSlicerSegmentEditorLogic.cxx:846) - SetSourceVolumeNode: need to set segment editor and segmentation nodes first<br>
[INFO][Python] 23.01.2026 10:47:43 [Python] (/Applications/Slicer.app/Contents/Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules/SlicerNNUNetLib/InstallLogic.py:57) - nnUNet is already installed (2.6.2) and compatible with requested version (nnunetv2).<br>
[DEBUG][Python] 23.01.2026 10:47:43 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): <a href="http://www.google.com:443" rel="noopener nofollow ugc">www.google.com:443</a><br>
[DEBUG][Python] 23.01.2026 10:47:44 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="https://www.google.com:443" rel="noopener nofollow ugc">https://www.google.com:443</a> “GET / HTTP/1.1” 200 None<br>
[DEBUG][Python] 23.01.2026 10:47:44 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): <a href="http://api.github.com:443" rel="noopener nofollow ugc">api.github.com:443</a><br>
[DEBUG][Python] 23.01.2026 10:47:44 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="https://api.github.com:443" rel="noopener nofollow ugc">https://api.github.com:443</a> “GET /repos/gaudot/SlicerDentalSegmentator HTTP/1.1” 200 1480<br>
[DEBUG][Python] 23.01.2026 10:47:45 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): <a href="http://api.github.com:443" rel="noopener nofollow ugc">api.github.com:443</a><br>
[DEBUG][Python] 23.01.2026 10:47:45 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="https://api.github.com:443" rel="noopener nofollow ugc">https://api.github.com:443</a> “GET /repos/gaudot/SlicerDentalSegmentator/releases HTTP/1.1” 200 828<br>
[DEBUG][Python] 23.01.2026 10:47:45 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): <a href="http://api.github.com:443" rel="noopener nofollow ugc">api.github.com:443</a><br>
[DEBUG][Python] 23.01.2026 10:47:46 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="https://api.github.com:443" rel="noopener nofollow ugc">https://api.github.com:443</a> “GET /repos/gaudot/SlicerDentalSegmentator/releases/147040025/assets HTTP/1.1” 200 602<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - A module that was compiled using NumPy 1.x cannot be run in<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - NumPy 2.0.2 as it may crash. To support both 1.x and 2.x<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - versions of NumPy, modules must be compiled with NumPy 2.0.<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Some module may need to rebuild instead e.g. with ‘pybind11&gt;=2.12’.<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - If you are a user of the module, the easiest solution will be to<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - downgrade to ‘numpy&lt;2’ or try to upgrade the affected module.<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - We expect that some modules will need time to support NumPy 2.<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Traceback (most recent call last):  File “/Applications/Slicer.app/Contents/Extensions-34045/DentalSegmentator/lib/Slicer-5.10/qt-scripted-modules/DentalSegmentatorLib/SegmentationWidget.py”, line 238, in onApplyClicked<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     self._runSegmentation()<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-34045/DentalSegmentator/lib/Slicer-5.10/qt-scripted-modules/DentalSegmentatorLib/SegmentationWidget.py”, line 257, in _runSegmentation<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     if not parameter.isSelectedDeviceAvailable():<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules/SlicerNNUNetLib/Parameter.py”, line 66, in isSelectedDeviceAvailable<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     import torch<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/<strong>init</strong>.py”, line 1477, in<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     from .functional import *  # noqa: F403<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/functional.py”, line 9, in<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     import torch.nn.functional as F<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/<strong>init</strong>.py”, line 1, in<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     from .modules import *  # noqa: F403<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/modules/<strong>init</strong>.py”, line 35, in<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     from .transformer import TransformerEncoder, TransformerDecoder,<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/modules/transformer.py”, line 20, in<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device(‘cpu’),<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - /Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)<br>
[CRITICAL][Stream] 23.01.2026 10:47:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device(‘cpu’),<br>
[ERROR][Python] 23.01.2026 10:47:56 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3146) - Failed to load the segmentation.<br>
Something went wrong during the nnUNet processing.<br>
Please check the logs for potential errors and contact the library maintainers.</p>

---
