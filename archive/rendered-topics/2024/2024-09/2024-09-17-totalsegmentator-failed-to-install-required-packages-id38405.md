# TotalSegmentator: Failed to install required packages 

**Topic ID**: 38405
**Date**: 2024-09-17
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-install-required-packages/38405

---

## Post #1 by @gsmattay (2024-09-17 01:46 UTC)

<p>Operating system: MacOS Big Sur 11.4<br>
Slicer version: 5.6.2<br>
Hello,</p>
<p>I have installed Slicer, installed Pytorch version 2.2.2 via the Pytorch utils module, installed the 3d segmentator module, and restarted Slicer. When attempting to run segmentation on test CT Chest data, I get the following error.</p>
<p>Failed to install required packages.</p>
<p>Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘rt-utils’]’ returned non-zero exit status 1.</p>
<p>Here are the more detailed logs:</p>
<p>TotalSegmentator Python package is required. Installing it from <a href="https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip</a>… (it may take several minutes)</p>
<ul>
<li>
<p>Installing numpy&lt;2…</p>
</li>
<li>
<p>Installing nibabel&gt;=2.3.0…</p>
</li>
<li>
<p>Installing tqdm&gt;=4.45.0…</p>
</li>
<li>
<p>Installing p-tqdm…</p>
</li>
<li>
<p>Installing xvfbwrapper…</p>
</li>
<li>
<p>Installing rt-utils…</p>
</li>
</ul>
<p>Failed to install Python dependencies:</p>
<p>Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘rt-utils’]’ returned non-zero exit status 1.</p>
<p>I have also attempted a force reinstall Total Segmentator Python package under advanced settings and this did not work. Would appreciate your help. Thank you.</p>

---

## Post #2 by @lassoan (2024-09-17 03:30 UTC)

<p>Please copy here the full application log (menu: Help / Report a bug).</p>

---

## Post #3 by @gsmattay (2024-09-18 22:53 UTC)

<p>Was not able to copy whole log due to character limit. Copied portions that may be relevant below:</p>
<pre><code class="lang-plaintext">[INFO][Stream] 15.09.2024 22:03:41 [] (unknown:0) - Successfully built TotalSegmentator

[INFO][Stream] 15.09.2024 22:03:41 [] (unknown:0) - Installing collected packages: TotalSegmentator

[INFO][Stream] 15.09.2024 22:03:41 [] (unknown:0) - WARNING: The scripts TotalSegmentator, crop_to_body, totalseg_combine_masks, totalseg_download_weights, totalseg_get_phase, totalseg_import_weights, totalseg_set_license and totalseg_setup_manually are installed in '/Applications/Slicer.app/Contents/lib/Python/bin' which is not on PATH.

[INFO][Stream] 15.09.2024 22:03:41 [] (unknown:0) - Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

[INFO][Stream] 15.09.2024 22:03:41 [] (unknown:0) - Successfully installed TotalSegmentator-2.4.0

[INFO][Python] 15.09.2024 22:03:41 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing numpy&lt;2...

[INFO][Stream] 15.09.2024 22:03:42 [] (unknown:0) - Requirement already satisfied: numpy&lt;2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (1.26.1)

[INFO][Python] 15.09.2024 22:03:43 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing nibabel&gt;=2.3.0...

[INFO][Stream] 15.09.2024 22:03:43 [] (unknown:0) - Collecting nibabel&gt;=2.3.0

[INFO][Stream] 15.09.2024 22:03:43 [] (unknown:0) - Obtaining dependency information for nibabel&gt;=2.3.0 from https://files.pythonhosted.org/packages/77/3f/ce43b8c2ccc4a7913a87c4d425aaf0080ea3abf947587e47dc2025981a17/nibabel-5.2.1-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:43 [] (unknown:0) - Using cached nibabel-5.2.1-py3-none-any.whl.metadata (8.8 kB)

[INFO][Stream] 15.09.2024 22:03:43 [] (unknown:0) - Requirement already satisfied: numpy&gt;=1.20 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nibabel&gt;=2.3.0) (1.26.1)

[INFO][Stream] 15.09.2024 22:03:43 [] (unknown:0) - Requirement already satisfied: packaging&gt;=17 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nibabel&gt;=2.3.0) (23.2)

[INFO][Stream] 15.09.2024 22:03:43 [] (unknown:0) - Using cached nibabel-5.2.1-py3-none-any.whl (3.3 MB)

[INFO][Stream] 15.09.2024 22:03:44 [] (unknown:0) - Installing collected packages: nibabel

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - WARNING: The scripts nib-conform, nib-convert, nib-dicomfs, nib-diff, nib-ls, nib-nifti-dx, nib-roi, nib-stats, nib-tck2trk, nib-trk2tck and parrec2nii are installed in '/Applications/Slicer.app/Contents/lib/Python/bin' which is not on PATH.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - totalsegmentator 2.4.0 requires dicom2nifti, which is not installed.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - totalsegmentator 2.4.0 requires p-tqdm, which is not installed.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - totalsegmentator 2.4.0 requires pyarrow, which is not installed.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - totalsegmentator 2.4.0 requires rt-utils, which is not installed.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - totalsegmentator 2.4.0 requires tqdm&gt;=4.45.0, which is not installed.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - totalsegmentator 2.4.0 requires xvfbwrapper, which is not installed.

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - Successfully installed nibabel-5.2.1

[INFO][Python] 15.09.2024 22:03:45 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing tqdm&gt;=4.45.0...

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - Collecting tqdm&gt;=4.45.0

[INFO][Stream] 15.09.2024 22:03:45 [] (unknown:0) - Obtaining dependency information for tqdm&gt;=4.45.0 from https://files.pythonhosted.org/packages/48/5d/acf5905c36149bbaec41ccf7f2b68814647347b72075ac0b1fe3022fdc73/tqdm-4.66.5-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - Using cached tqdm-4.66.5-py3-none-any.whl.metadata (57 kB)

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - Using cached tqdm-4.66.5-py3-none-any.whl (78 kB)

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - Installing collected packages: tqdm

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - WARNING: The script tqdm is installed in '/Applications/Slicer.app/Contents/lib/Python/bin' which is not on PATH.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - totalsegmentator 2.4.0 requires dicom2nifti, which is not installed.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - totalsegmentator 2.4.0 requires p-tqdm, which is not installed.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - totalsegmentator 2.4.0 requires pyarrow, which is not installed.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - totalsegmentator 2.4.0 requires rt-utils, which is not installed.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - totalsegmentator 2.4.0 requires xvfbwrapper, which is not installed.

[INFO][Stream] 15.09.2024 22:03:46 [] (unknown:0) - Successfully installed tqdm-4.66.5

[INFO][Python] 15.09.2024 22:03:46 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing p-tqdm...

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Collecting p-tqdm

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached p_tqdm-1.4.2-py3-none-any.whl

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Requirement already satisfied: tqdm&gt;=4.45.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from p-tqdm) (4.66.5)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Collecting pathos&gt;=0.2.5 (from p-tqdm)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Obtaining dependency information for pathos&gt;=0.2.5 from https://files.pythonhosted.org/packages/f4/7f/cea34872c000d17972dad998575d14656d7c6bcf1a08a8d66d73c1ef2cca/pathos-0.3.2-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached pathos-0.3.2-py3-none-any.whl.metadata (11 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Requirement already satisfied: six&gt;=1.13.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from p-tqdm) (1.16.0)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Collecting ppft&gt;=1.7.6.8 (from pathos&gt;=0.2.5-&gt;p-tqdm)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Obtaining dependency information for ppft&gt;=1.7.6.8 from https://files.pythonhosted.org/packages/ff/fa/5160c7d2fb1d4f2b83cba7a40f0eb4b015b78f6973b7ab6b2e73c233cfdc/ppft-1.7.6.8-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached ppft-1.7.6.8-py3-none-any.whl.metadata (12 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Collecting dill&gt;=0.3.8 (from pathos&gt;=0.2.5-&gt;p-tqdm)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Obtaining dependency information for dill&gt;=0.3.8 from https://files.pythonhosted.org/packages/c9/7a/cef76fd8438a42f96db64ddaa85280485a9c395e7df3db8158cfec1eee34/dill-0.3.8-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached dill-0.3.8-py3-none-any.whl.metadata (10 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Collecting pox&gt;=0.3.4 (from pathos&gt;=0.2.5-&gt;p-tqdm)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Obtaining dependency information for pox&gt;=0.3.4 from https://files.pythonhosted.org/packages/e1/d7/9e73c32f73da71e8224b4cb861b5db50ebdebcdff14d3e3fb47a63c578b2/pox-0.3.4-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached pox-0.3.4-py3-none-any.whl.metadata (8.0 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Collecting multiprocess&gt;=0.70.16 (from pathos&gt;=0.2.5-&gt;p-tqdm)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Obtaining dependency information for multiprocess&gt;=0.70.16 from https://files.pythonhosted.org/packages/da/d9/f7f9379981e39b8c2511c9e0326d212accacb82f12fbfdc1aa2ce2a7b2b6/multiprocess-0.70.16-py39-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached multiprocess-0.70.16-py39-none-any.whl.metadata (7.2 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached pathos-0.3.2-py3-none-any.whl (82 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached dill-0.3.8-py3-none-any.whl (116 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached multiprocess-0.70.16-py39-none-any.whl (133 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached pox-0.3.4-py3-none-any.whl (29 kB)

[INFO][Stream] 15.09.2024 22:03:47 [] (unknown:0) - Using cached ppft-1.7.6.8-py3-none-any.whl (56 kB)

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - Installing collected packages: ppft, pox, dill, multiprocess, pathos, p-tqdm

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - totalsegmentator 2.4.0 requires dicom2nifti, which is not installed.

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - totalsegmentator 2.4.0 requires pyarrow, which is not installed.

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - totalsegmentator 2.4.0 requires rt-utils, which is not installed.

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - totalsegmentator 2.4.0 requires xvfbwrapper, which is not installed.

[INFO][Stream] 15.09.2024 22:03:48 [] (unknown:0) - Successfully installed dill-0.3.8 multiprocess-0.70.16 p-tqdm-1.4.2 pathos-0.3.2 pox-0.3.4 ppft-1.7.6.8

[INFO][Python] 15.09.2024 22:03:48 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing xvfbwrapper...

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - Collecting xvfbwrapper

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - Using cached xvfbwrapper-0.2.9-py3-none-any.whl

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - Installing collected packages: xvfbwrapper

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - totalsegmentator 2.4.0 requires dicom2nifti, which is not installed.

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - totalsegmentator 2.4.0 requires pyarrow, which is not installed.

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - totalsegmentator 2.4.0 requires rt-utils, which is not installed.

[INFO][Stream] 15.09.2024 22:03:49 [] (unknown:0) - Successfully installed xvfbwrapper-0.2.9

[INFO][Python] 15.09.2024 22:03:50 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing rt-utils...

[INFO][Stream] 15.09.2024 22:03:50 [] (unknown:0) - Collecting rt-utils

[INFO][Stream] 15.09.2024 22:03:50 [] (unknown:0) - Obtaining dependency information for rt-utils from https://files.pythonhosted.org/packages/84/f7/4212ac81d23733a79415dc0cc8c7d0d795ca025d5cdb34d1887a0402a6cb/rt_utils-1.2.7-py2.py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:03:50 [] (unknown:0) - Using cached rt_utils-1.2.7-py2.py3-none-any.whl.metadata (7.5 kB)

[INFO][Stream] 15.09.2024 22:03:50 [] (unknown:0) - Requirement already satisfied: pydicom in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from rt-utils) (2.4.3)

[INFO][Stream] 15.09.2024 22:03:50 [] (unknown:0) - Requirement already satisfied: numpy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from rt-utils) (1.26.1)

[INFO][Stream] 15.09.2024 22:03:51 [] (unknown:0) - Collecting opencv-python (from rt-utils)

[INFO][Stream] 15.09.2024 22:03:51 [] (unknown:0) - Using cached opencv-python-4.10.0.84.tar.gz (95.1 MB)

[INFO][Stream] 15.09.2024 22:03:58 [] (unknown:0) - Installing build dependencies: started

[INFO][Stream] 15.09.2024 22:04:09 [] (unknown:0) - Installing build dependencies: finished with status 'done'

[INFO][Stream] 15.09.2024 22:04:09 [] (unknown:0) - Getting requirements to build wheel: started

[INFO][Stream] 15.09.2024 22:04:10 [] (unknown:0) - Getting requirements to build wheel: finished with status 'done'

[INFO][Stream] 15.09.2024 22:04:10 [] (unknown:0) - Preparing metadata (pyproject.toml): started

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Preparing metadata (pyproject.toml): finished with status 'done'

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Collecting dataclasses (from rt-utils)

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Obtaining dependency information for dataclasses from https://files.pythonhosted.org/packages/26/2f/1095cdc2868052dd1e64520f7c0d5c8c550ad297e944e641dbf1ffbb9a5d/dataclasses-0.6-py3-none-any.whl.metadata

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Using cached dataclasses-0.6-py3-none-any.whl.metadata (3.0 kB)

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Using cached rt_utils-1.2.7-py2.py3-none-any.whl (18 kB)

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Using cached dataclasses-0.6-py3-none-any.whl (14 kB)

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Building wheels for collected packages: opencv-python

[INFO][Stream] 15.09.2024 22:04:11 [] (unknown:0) - Building wheel for opencv-python (pyproject.toml): started

[INFO][Stream] 15.09.2024 22:05:12 [] (unknown:0) - Building wheel for opencv-python (pyproject.toml): still running...

...

INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       #include &lt;Python.h&gt;
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -                ^~~~~~~~~~
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       1 error generated.
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       make[2]: *** [modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o] Error 1
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       make[1]: *** [modules/python3/CMakeFiles/opencv_python3.dir/all] Error 2
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       make: *** [all] Error 2
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       Traceback (most recent call last):
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         File "/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-mom19h7d/overlay/lib/python3.9/site-packages/skbuild/setuptools_wrap.py", line 668, in setup
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           cmkr.make(make_args, install_target=cmake_install_target, env=env)
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         File "/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-mom19h7d/overlay/lib/python3.9/site-packages/skbuild/cmaker.py", line 696, in make
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           self.make_impl(clargs=clargs, config=config, source_dir=source_dir, install_target=install_target, env=env)
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         File "/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-mom19h7d/overlay/lib/python3.9/site-packages/skbuild/cmaker.py", line 741, in make_impl
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           raise SKBuildError(msg)
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       An error occurred while building with CMake.
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         Command:
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-mom19h7d/overlay/lib/python3.9/site-packages/cmake/data/bin/cmake --build . --target install --config Release --
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         Install target:
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           install
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         Source directory:
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-install-rs3opx14/opencv-python_3ac362bd7bcc47caa112dc6c55c41cf0
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -         Working directory:
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -           /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-install-rs3opx14/opencv-python_3ac362bd7bcc47caa112dc6c55c41cf0/_skbuild/macosx-11.0-x86_64-3.9/cmake-build
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       Please check the install target is valid and see CMake's output for more information.
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -       [end of output]
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -   note: This error originates from a subprocess, and is likely not a problem with pip.
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) -   ERROR: Failed building wheel for opencv-python
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) - Failed to build opencv-python
[INFO][Stream] 15.09.2024 22:35:57 [] (unknown:0) - ERROR: Could not build wheels for opencv-python, which is required to install pyproject.toml-based projects
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 274, in onApplyButton
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -     self.logic.setupPythonRequirements()
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 788, in setupPythonRequirements
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -     skippedRequirements = self.pipInstallSelective(
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 706, in pipInstallSelective
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -     slicer.util.pip_install(requirement)
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3887, in pip_install
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -     _executePythonModule("pip", args)
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3848, in _executePythonModule
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -     logProcessOutput(proc)
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3814, in logProcessOutput
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 15.09.2024 22:36:00 [] (unknown:0) - subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'rt-utils']' returned non-zero exit status 1.
[ERROR][Python] 15.09.2024 22:36:00 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3009) - Failed to install required packages.
</code></pre>

---

## Post #4 by @lassoan (2024-09-19 19:36 UTC)

<p>A post was split to a new topic: <a href="/t/problem-with-ai-lung-segmentation-in-lungctanalyzer/38447">Problem with AI lung segmentation in LungCTAnalyzer</a></p>

---

## Post #5 by @lassoan (2024-09-19 19:40 UTC)

<blockquote>
<p>Failed to build opencv-python</p>
</blockquote>
<p>TotalSegmentator listed <code>rt_utils</code> in its dependency list, which is an unnecessary package (it is only needed for RTSTRUCT export, but Slicer can do that already) and it is a problematic package, because it depends on <code>opencv-python</code>, which is a complex, messy package that often fails to build.</p>
<p>I’ve updated TotalSegmentator extension to skip <code>rt_utils</code> package. If you use latest Slicer Stable Release then all you need is to update the TotalSegmentator extension tomorrow and reinstall the Python packages.</p>

---

## Post #6 by @gsmattay (2024-09-20 15:33 UTC)

<p>Thank you, however I followed your advice and am still coming up with a similar error. I updated the TotalSegmentator extension and selected force reinstall TotalSegmentator python package. Error log as below:</p>
<pre><code class="lang-auto">Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator', '-i', '/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/Slicer-govindmattay/__SlicerTemp__2024-09-20_09+26+03.691/total-segmentator-input.nii', '-o', '/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/Slicer-govindmattay/__SlicerTemp__2024-09-20_09+26+03.691/segmentation', '--fast']' returned non-zero exit status 1.
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1002, in process
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1042, in processVolume
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 848, in logProcessOutput
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 20.09.2024 09:26:40 [] (unknown:0) - subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator', '-i', '/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/Slicer-govindmattay/__SlicerTemp__2024-09-20_09+26+03.691/total-segmentator-input.nii', '-o', '/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/Slicer-govindmattay/__SlicerTemp__2024-09-20_09+26+03.691/segmentation', '--fast']' returned non-zero exit status 1.
[INFO][Python] 20.09.2024 09:27:34 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...
[INFO][Python] 20.09.2024 09:27:34 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.2.2 imported successfully
[INFO][Python] 20.09.2024 09:27:34 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: False
[INFO][Python] 20.09.2024 09:27:34 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - TotalSegmentator Python package is required. Installing it from https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip... (it may take several minutes)
[INFO][Stream] 20.09.2024 09:27:36 [] (unknown:0) - Found existing installation: TotalSegmentator 2.4.0
[INFO][Stream] 20.09.2024 09:27:36 [] (unknown:0) - Uninstalling TotalSegmentator-2.4.0:
[INFO][Stream] 20.09.2024 09:27:36 [] (unknown:0) -   Successfully uninstalled TotalSegmentator-2.4.0
[INFO][Stream] 20.09.2024 09:27:36 [] (unknown:0) - Collecting https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip
[INFO][Stream] 20.09.2024 09:27:37 [] (unknown:0) -   Using cached https://github.com/wasserth/TotalSegmentator/archive/7274faac4673298d17b63a5a8335006f02e6d426.zip
[INFO][Stream] 20.09.2024 09:27:37 [] (unknown:0) -   Installing build dependencies: started
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) -   Installing build dependencies: finished with status 'done'
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) -   Getting requirements to build wheel: started
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) -   Getting requirements to build wheel: finished with status 'done'
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) -   Preparing metadata (pyproject.toml): started
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) -   Preparing metadata (pyproject.toml): finished with status 'done'
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) - Building wheels for collected packages: TotalSegmentator
[INFO][Stream] 20.09.2024 09:27:41 [] (unknown:0) -   Building wheel for TotalSegmentator (pyproject.toml): started
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) -   Building wheel for TotalSegmentator (pyproject.toml): finished with status 'done'
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) -   Created wheel for TotalSegmentator: filename=TotalSegmentator-2.4.0-py3-none-any.whl size=348308 sha256=261f5e08838790ecd65fe568dff3be1b1fd1d87354b3c5231be3adfc1b40a280
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) -   Stored in directory: /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-ephem-wheel-cache-yucaapnd/wheels/d8/41/ce/20b3efb2dd6cebf94e551445b85bf8412c77d640fe7bd41cbb
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) - Successfully built TotalSegmentator
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) - Installing collected packages: TotalSegmentator
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) -   WARNING: The scripts TotalSegmentator, crop_to_body, totalseg_combine_masks, totalseg_download_weights, totalseg_get_phase, totalseg_import_weights, totalseg_set_license and totalseg_setup_manually are installed in '/Applications/Slicer.app/Contents/lib/Python/bin' which is not on PATH.
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) -   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) - Successfully installed TotalSegmentator-2.4.0
[INFO][Python] 20.09.2024 09:27:42 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing numpy&lt;2...
[INFO][Stream] 20.09.2024 09:27:42 [] (unknown:0) - Requirement already satisfied: numpy&lt;2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (1.26.1)
[INFO][Python] 20.09.2024 09:27:43 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing nibabel&gt;=2.3.0...
[INFO][Stream] 20.09.2024 09:27:44 [] (unknown:0) - Requirement already satisfied: nibabel&gt;=2.3.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (5.2.1)
[INFO][Stream] 20.09.2024 09:27:44 [] (unknown:0) - Requirement already satisfied: numpy&gt;=1.20 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nibabel&gt;=2.3.0) (1.26.1)
[INFO][Stream] 20.09.2024 09:27:44 [] (unknown:0) - Requirement already satisfied: packaging&gt;=17 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nibabel&gt;=2.3.0) (23.2)
[INFO][Python] 20.09.2024 09:27:44 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing tqdm&gt;=4.45.0...
[INFO][Stream] 20.09.2024 09:27:45 [] (unknown:0) - Requirement already satisfied: tqdm&gt;=4.45.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (4.66.5)
[INFO][Python] 20.09.2024 09:27:45 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing p-tqdm...
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: p-tqdm in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (1.4.2)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: tqdm&gt;=4.45.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from p-tqdm) (4.66.5)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: pathos&gt;=0.2.5 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from p-tqdm) (0.3.2)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: six&gt;=1.13.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from p-tqdm) (1.16.0)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: ppft&gt;=1.7.6.8 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from pathos&gt;=0.2.5-&gt;p-tqdm) (1.7.6.8)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: dill&gt;=0.3.8 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from pathos&gt;=0.2.5-&gt;p-tqdm) (0.3.8)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: pox&gt;=0.3.4 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from pathos&gt;=0.2.5-&gt;p-tqdm) (0.3.4)
[INFO][Stream] 20.09.2024 09:27:46 [] (unknown:0) - Requirement already satisfied: multiprocess&gt;=0.70.16 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from pathos&gt;=0.2.5-&gt;p-tqdm) (0.70.16)
[INFO][Python] 20.09.2024 09:27:46 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing xvfbwrapper...
[INFO][Stream] 20.09.2024 09:27:47 [] (unknown:0) - Requirement already satisfied: xvfbwrapper in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (0.2.9)
[INFO][Python] 20.09.2024 09:27:48 [Python] (/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - - Installing rt-utils...
[INFO][Stream] 20.09.2024 09:27:48 [] (unknown:0) - Collecting rt-utils
[INFO][Stream] 20.09.2024 09:27:48 [] (unknown:0) -   Obtaining dependency information for rt-utils from https://files.pythonhosted.org/packages/84/f7/4212ac81d23733a79415dc0cc8c7d0d795ca025d5cdb34d1887a0402a6cb/rt_utils-1.2.7-py2.py3-none-any.whl.metadata
[INFO][Stream] 20.09.2024 09:27:48 [] (unknown:0) -   Using cached rt_utils-1.2.7-py2.py3-none-any.whl.metadata (7.5 kB)
[INFO][Stream] 20.09.2024 09:27:48 [] (unknown:0) - Requirement already satisfied: pydicom in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from rt-utils) (2.4.3)
[INFO][Stream] 20.09.2024 09:27:48 [] (unknown:0) - Requirement already satisfied: numpy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from rt-utils) (1.26.1)
[INFO][Stream] 20.09.2024 09:27:49 [] (unknown:0) - Collecting opencv-python (from rt-utils)
[INFO][Stream] 20.09.2024 09:27:49 [] (unknown:0) -   Using cached opencv-python-4.10.0.84.tar.gz (95.1 MB)
[INFO][Stream] 20.09.2024 09:27:55 [] (unknown:0) -   Installing build dependencies: started
[INFO][Stream] 20.09.2024 09:28:06 [] (unknown:0) -   Installing build dependencies: finished with status 'done'
[INFO][Stream] 20.09.2024 09:28:07 [] (unknown:0) -   Getting requirements to build wheel: started
[INFO][Stream] 20.09.2024 09:28:07 [] (unknown:0) -   Getting requirements to build wheel: finished with status 'done'
[INFO][Stream] 20.09.2024 09:28:07 [] (unknown:0) -   Preparing metadata (pyproject.toml): started
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) -   Preparing metadata (pyproject.toml): finished with status 'done'
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) - Collecting dataclasses (from rt-utils)
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) -   Obtaining dependency information for dataclasses from https://files.pythonhosted.org/packages/26/2f/1095cdc2868052dd1e64520f7c0d5c8c550ad297e944e641dbf1ffbb9a5d/dataclasses-0.6-py3-none-any.whl.metadata
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) -   Using cached dataclasses-0.6-py3-none-any.whl.metadata (3.0 kB)
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) - Using cached rt_utils-1.2.7-py2.py3-none-any.whl (18 kB)
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) - Using cached dataclasses-0.6-py3-none-any.whl (14 kB)
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) - Building wheels for collected packages: opencv-python
[INFO][Stream] 20.09.2024 09:28:08 [] (unknown:0) -   Building wheel for opencv-python (pyproject.toml): started
...
...
...
[INFO][Stream] 20.09.2024 10:00:41 [] (unknown:0) -       [  0%] Built target opencv_dnn_plugins
[INFO][Stream] 20.09.2024 10:00:41 [] (unknown:0) -       [  0%] Built target opencv_highgui_plugins
...
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       [ 99%] Linking CXX static library ../../lib/libopencv_gapi.a
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       /Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../../lib/libopencv_gapi.a(gtbbexecutor.cpp.o) has no symbols
...
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       [ 99%] Built target opencv_gapi
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       [ 99%] Generate files for Python bindings and documentation
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       Note: Class cv::Feature2D has more than 1 base class (not supported by Python C extensions)
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -             Bases:  cv::Algorithm, cv::class, cv::Feature2D, cv::Algorithm
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -             Only the first base class will be used
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       Note: Class cv::detail::GraphCutSeamFinder has more than 1 base class (not supported by Python C extensions)
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -             Bases:  cv::detail::GraphCutSeamFinderBase, cv::detail::SeamFinder
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -             Only the first base class will be used
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       [ 99%] Built target gen_opencv_python_source
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       [ 99%] Building CXX object modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       In file included from /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-install-fhss2s9r/opencv-python_b944e47b429d46758eda51e823b82402/opencv/modules/python/src2/cv2.cpp:5:
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-install-fhss2s9r/opencv-python_b944e47b429d46758eda51e823b82402/opencv/modules/python/src2/cv2.hpp:23:10: fatal error: 'Python.h' file not found
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       #include &lt;Python.h&gt;
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -                ^~~~~~~~~~
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       1 error generated.
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       make[2]: *** [modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o] Error 1
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       make[1]: *** [modules/python3/CMakeFiles/opencv_python3.dir/all] Error 2
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       make: *** [all] Error 2
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       Traceback (most recent call last):
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         File "/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-6_j_vbk0/overlay/lib/python3.9/site-packages/skbuild/setuptools_wrap.py", line 668, in setup
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           cmkr.make(make_args, install_target=cmake_install_target, env=env)
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         File "/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-6_j_vbk0/overlay/lib/python3.9/site-packages/skbuild/cmaker.py", line 696, in make
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           self.make_impl(clargs=clargs, config=config, source_dir=source_dir, install_target=install_target, env=env)
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         File "/private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-6_j_vbk0/overlay/lib/python3.9/site-packages/skbuild/cmaker.py", line 741, in make_impl
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           raise SKBuildError(msg)
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       An error occurred while building with CMake.
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         Command:
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-build-env-6_j_vbk0/overlay/lib/python3.9/site-packages/cmake/data/bin/cmake --build . --target install --config Release --
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         Install target:
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           install
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         Source directory:
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-install-fhss2s9r/opencv-python_b944e47b429d46758eda51e823b82402
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -         Working directory:
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -           /private/var/folders/5y/nyrtn1qx1pq81bdg8l9tzck80000gn/T/pip-install-fhss2s9r/opencv-python_b944e47b429d46758eda51e823b82402/_skbuild/macosx-11.0-x86_64-3.9/cmake-build
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       Please check the install target is valid and see CMake's output for more information.
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -       [end of output]
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -   note: This error originates from a subprocess, and is likely not a problem with pip.
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) -   ERROR: Failed building wheel for opencv-python
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) - Failed to build opencv-python
[INFO][Stream] 20.09.2024 10:00:42 [] (unknown:0) - ERROR: Could not build wheels for opencv-python, which is required to install pyproject.toml-based projects
[ERROR][Python] 20.09.2024 10:00:46 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3009) - Failed to upgrade TotalSegmentator

Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'rt-utils']' returned non-zero exit status 1.
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 319, in onPackageUpgrade
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -     self.logic.setupPythonRequirements(upgrade=True)
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 789, in setupPythonRequirements
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -     skippedRequirements = self.pipInstallSelective(
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 706, in pipInstallSelective
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -     slicer.util.pip_install(requirement)
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3887, in pip_install
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -     _executePythonModule("pip", args)
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3848, in _executePythonModule
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -     logProcessOutput(proc)
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3814, in logProcessOutput
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 20.09.2024 10:12:54 [] (unknown:0) - subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'rt-utils']' returned non-zero exit status 1.
</code></pre>

---

## Post #7 by @jamesobutler (2024-09-20 15:50 UTC)

<aside class="quote no-group" data-username="gsmattay" data-post="6" data-topic="38405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gsmattay/48/77944_2.png" class="avatar"> gsmattay:</div>
<blockquote>
<p>Using cached opencv-python-4.10.0.84.tar.gz (95.1 MB)</p>
</blockquote>
</aside>
<p>It’s unclear why it picked opencv-python’s source file.  PyPI hosts a whl file that could be used:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f23bc1467bf83661ebfced9c9db99f7f3f47e89b.png" alt="image" data-base62-sha1="yyTztWHaeWXIEdCwgNjix9h7RML" width="547" height="65"></p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/opencv-python/#files">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.35549fe8.ico" class="site-icon" width="32" height="30">

      <a href="https://pypi.org/project/opencv-python/#files" target="_blank" rel="noopener nofollow ugc">PyPI</a>
  </header>

  <article class="onebox-body">
    <img width="300" height="300" src="https://pypi.org/static/images/twitter.abaf4b19.webp" class="thumbnail onebox-avatar">

<h3><a href="https://pypi.org/project/opencv-python/#files" target="_blank" rel="noopener nofollow ugc">opencv-python</a></h3>

  <p>Wrapper package for OpenCV python bindings.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Clearing the pip cache could potentially force it to try and pull the whl file. Alternatively you can download the whl file manually and tell pip to install the path to the whl.</p>

---

## Post #8 by @lassoan (2024-09-20 16:24 UTC)

<p>Maybe opencv-python does not have wheel for this specific linux distribution. Anyway, OpenCV is messy and it is not needed, so the best is to just not install it.</p>
<p>The TotalSegmentator extension that you download today will no longer attempt to install opencv-python, so it should be all good. To get this updated version:</p>
<ul>
<li>use the latest Slicer Stable Release (or download the latest Slicer Preview Release today - the preview release that you may have downloaded yesterday or earlier will not have the latest extension updates)</li>
<li>reinstall the TotalSegmentator extension.</li>
</ul>

---

## Post #9 by @jamesobutler (2024-09-20 16:40 UTC)

<aside class="quote no-group" data-username="gsmattay" data-post="1" data-topic="38405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gsmattay/48/77944_2.png" class="avatar"> gsmattay:</div>
<blockquote>
<p>MacOS Big Sur 11.4</p>
</blockquote>
</aside>
<p>Apologies, the user appears to be on macOS 11 where that latest opencv-python version has a macOS 11+ whl but only on Apple Silicon. If this was an Intel mac, then it needs macOS 12+.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68d8ea1ec536f51a5f3d5327f5071042e1a4440e.png" alt="{EDE3F05C-9B07-4F93-8B07-008F70B7673D}" data-base62-sha1="eXworbjQZjTdrszM4vElPFJu1oW" width="623" height="130"></p>

---

## Post #10 by @gsmattay (2024-09-30 03:49 UTC)

<p>Thank you all for your help. After updating to macOS Ventura 13.7, it worked.</p>

---

## Post #11 by @eNable_Polska (2025-10-10 11:31 UTC)

<p>I have a similar problem that I can’t solve.<br>
I can’t install the pyarrow package in Slicer, which is necessary for TotalSegmentator to work. When I try to force a reinstall, I get the following message:</p>
<pre><code class="lang-auto">Failed to build pyarrow
ERROR: Could not build wheels for pyarrow, which is required to install pyproject.toml-based projects
[Python] Failed to upgrade TotalSegmentator
[Python] Command '['/home/zop/Slicer-5.8.1-linux-amd64/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'pyarrow']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/home/zop/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 321, in onPackageUpgrade
    self.logic.setupPythonRequirements(upgrade=True)
  File "/home/zop/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 860, in setupPythonRequirements
    self.pipInstallSelective(
  File "/home/zop/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 741, in pipInstallSelective
    slicer.util.pip_install(requirement)
  File "/home/zop/Slicer-5.8.1-linux-amd64/bin/Python/slicer/util.py", line 3942, in pip_install
    _executePythonModule("pip", args)
  File "/home/zop/Slicer-5.8.1-linux-amd64/bin/Python/slicer/util.py", line 3896, in _executePythonModule
    logProcessOutput(proc)
  File "/home/zop/Slicer-5.8.1-linux-amd64/bin/Python/slicer/util.py", line 3862, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/home/zop/Slicer-5.8.1-linux-amd64/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'pyarrow']' returned non-zero exit status 1.

</code></pre>
<p>I tried installing pyarrow from the Slicer python console (pip-install(“pyarrow”)) but without success.<br>
How can I resolve this issue?</p>
<p>Slicer 5.8.1 ArchLinux up-to-date</p>

---

## Post #12 by @lassoan (2025-10-10 12:44 UTC)

<p>Normally commonly used packages don’t need to be built but binary wheels are downloaded from PyPI. Probably you had internet connectivity issues or some firewalls or proxy server interfered with the operation. I cannot tell because you did not include that part of the error message, only the last small part of the output.</p>
<blockquote>
<p>I tried installing pyarrow from the Slicer python console (pip-install(“pyarrow”)) but without success.</p>
</blockquote>
<p><code>pip-install</code> does not exist. Did you run <code>pip_install</code>? Did you get the same error?</p>

---

## Post #13 by @eNable_Polska (2025-10-10 14:52 UTC)

<p>Sorry, my mistake, of course I used pip_install but the error is as above</p>
<p>I installed the night version and the necessary elements were added without any problems. Therefore, it is probably not a firewall issue.</p>

---

## Post #14 by @jamesobutler (2025-10-10 16:11 UTC)

<p>This was likely due to latest pyarrow only having manylinux 2_28 whls for Python 3.9 and Slicer’s 5.8.1 linux environment doesn’t support those whl versions, but it could have done a manylinux 2_17 whl. Latest Slicer Preview has an updated linux environment that support manylinux 2_28 whls which is why pyarrow installation likely worked for you when using that newer version.</p>
<aside class="quote quote-modified" data-post="1" data-topic="43802">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-build-environment-upgraded-to-qt5-almalinux8-gcc14/43802">Slicer Build Environment Upgraded to `qt5-almalinux8-gcc14`</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    The build environment used for generating Slicer Preview and its extensions has been upgraded from qt5-centos7-gcc7 to qt5-almalinux8-gcc14. 
This update brings improved C++ standards support, better compatibility with modern systems, and eliminates complications related to the Dual ABI issue previously discussed <a href="https://discourse.slicer.org/t/temporary-disabling-of-stable-extension-builds-in-preparation-for-slicer-5-8-release-visual-studio-update/41207/7">here</a>. 
<a name="p-126953-comparison-of-build-environments-1" class="anchor" href="#p-126953-comparison-of-build-environments-1"></a>Comparison of Build Environments




Build Environment
Minimum Required glibc
Manylinux Policy
GCC Version
Compatible Systems




qt5-centos7-gcc7
2.17
manylinux2014, manylinux_2…
  </blockquote>
</aside>


---

## Post #15 by @hina-shah (2025-10-27 20:22 UTC)

<p>I’m getting a similar error with Slicer 5.8.1. This is happening even with idc-index and batchgenerator. The installation worked fine a few months ago. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I’ll try with the nightly version.</p>

---
