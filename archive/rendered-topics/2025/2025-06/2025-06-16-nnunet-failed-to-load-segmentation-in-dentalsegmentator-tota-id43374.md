---
topic_id: 43374
title: "Nnunet Failed To Load Segmentation In Dentalsegmentator Tota"
date: 2025-06-16
url: https://discourse.slicer.org/t/43374
---

# nnUNET failed to load segmentation in DentalSegmentator & totalSegmentator

**Topic ID**: 43374
**Date**: 2025-06-16
**URL**: https://discourse.slicer.org/t/nnunet-failed-to-load-segmentation-in-dentalsegmentator-totalsegmentator/43374

---

## Post #1 by @chz31 (2025-06-16 20:22 UTC)

<p>I am using Ubuntu 22.04 and Slicer 5.9.0. The DentalSegmentator showed “failed to load segmentation; something is wrong with nnUnet processing”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fae17fd992165dbf8dc1cdc7d12585d07692202.png" data-download-href="/uploads/short-url/6NNqYNBH7utHyx1zeb93QtrZPr4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fae17fd992165dbf8dc1cdc7d12585d07692202.png" alt="image" data-base62-sha1="6NNqYNBH7utHyx1zeb93QtrZPr4" width="414" height="111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×149 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the error log:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Session start time .......: 20250616_150812
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Slicer version ...........: 5.9.0-2025-06-14 (revision 33686 / 7a97a67) linux-amd64 - installed release
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Operating system .........: Linux / 6.8.0-60-generic / #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Apr 22 19:00:15 UTC 2 / UTF-8 - 64-bit
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Memory ...................: 256950 MB physical, 2047 MB virtual
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Xeon(R) w9-3575X, 44 cores, 88 logical processors
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - DCMTK configuration ......: version 3.6.8, no SSL
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Application path .........: /home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin
[DEBUG][Qt] 16.06.2025 15:08:12 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-33686/NNUNet/lib/Slicer-5.9/qt-scripted-modules, slicer.org/Extensions-33686/PyTorch/lib/Slicer-5.9/qt-scripted-modules, slicer.org/Extensions-33686/DentalSegmentator/lib/Slicer-5.9/qt-scripted-modules, slicer.org/Extensions-33686/SlicerPythonTestRunner/lib/Slicer-5.9/qt-scripted-modules
[DEBUG][Python] 16.06.2025 15:08:15 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 16.06.2025 15:08:15 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 16.06.2025 15:08:15 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 16.06.2025 15:08:24 [] (unknown:0) - Switch to module:  "PyTorchUtils"
[DEBUG][Qt] 16.06.2025 15:08:33 [] (unknown:0) - Switch to module:  "DentalSegmentator"
[DEBUG][Qt] 16.06.2025 15:08:39 [] (unknown:0) - Switch to module:  "SampleData"
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Verifying checksum
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - File already exists and checksum is OK - reusing it.
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Requesting load PreDentalSurgery from /home/zhang/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz ...
[DEBUG][Qt] 16.06.2025 15:08:41 [] (unknown:0) - "Volume" Reader has successfully read the file "/home/zhang/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz" "[0.34s]"
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Load finished
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Verifying checksum
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - File already exists and checksum is OK - reusing it.
[DEBUG][Python] 16.06.2025 15:08:41 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Requesting load PostDentalSurgery from /home/zhang/.cache/slicer.org/Slicer/SlicerIO/PostDentalSurgery.gipl.gz ...
[DEBUG][Qt] 16.06.2025 15:08:42 [] (unknown:0) - "Volume" Reader has successfully read the file "/home/zhang/.cache/slicer.org/Slicer/SlicerIO/PostDentalSurgery.gipl.gz" "[0.35s]"
[DEBUG][Python] 16.06.2025 15:08:42 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Load finished
[DEBUG][Qt] 16.06.2025 15:08:46 [] (unknown:0) - Switch to module:  "DentalSegmentator"
[INFO][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/slicer.org/Extensions-33686/NNUNet/lib/Slicer-5.9/qt-scripted-modules/SlicerNNUNetLib/InstallLogic.py:56) - nnUNet is already installed (2.6.2) and compatible with requested version (nnunetv2).
[DEBUG][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): www.google.com:443
[DEBUG][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - https://www.google.com:443 "GET / HTTP/1.1" 200 None
[DEBUG][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): api.github.com:443
[DEBUG][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - https://api.github.com:443 "GET /repos/gaudot/SlicerDentalSegmentator HTTP/1.1" 200 1477
[DEBUG][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): api.github.com:443
[DEBUG][Python] 16.06.2025 15:08:50 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - https://api.github.com:443 "GET /repos/gaudot/SlicerDentalSegmentator/releases HTTP/1.1" 200 817
[DEBUG][Python] 16.06.2025 15:08:51 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:1049) - Starting new HTTPS connection (1): api.github.com:443
[DEBUG][Python] 16.06.2025 15:08:51 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - https://api.github.com:443 "GET /repos/gaudot/SlicerDentalSegmentator/releases/147040025/assets HTTP/1.1" 200 603
[ERROR][Python] 16.06.2025 15:08:54 [Python] (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/Python/slicer/util.py:3146) - Failed to load the segmentation.
Something went wrong during the nnUNet processing.
Please check the logs for potential errors and contact the library maintainers.
</code></pre>
<p>The pytorch util showed pytorch properly installed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37224130725a9fcbc3f37cfffb69d8e4296ade76.png" data-download-href="/uploads/short-url/7RJEmSJWY2yxgqPmdKAOKDOhRuC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37224130725a9fcbc3f37cfffb69d8e4296ade76.png" alt="image" data-base62-sha1="7RJEmSJWY2yxgqPmdKAOKDOhRuC" width="414" height="111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×149 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also tried totalSegmentator, which showed below errors:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/Python/slicer/util.py", line 3392, in tryWithErrorDisplay
    yield
  File "/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 1046, in process
    self.processVolume(inputFile, inputVolume,
  File "/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 1113, in processVolume
    self.logProcessOutput(proc)
  File "/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 892, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/../bin/PythonSlicer', '/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/lib/Python/bin/TotalSegmentator', '-i', '/tmp/Slicer-zhang/__SlicerTemp__2025-06-16_15+19+33.235/total-segmentator-input.nii', '-o', '/tmp/Slicer-zhang/__SlicerTemp__2025-06-16_15+19+33.235/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @chz31 (2025-06-16 20:36 UTC)

<p>I am not sure if it is my Ubuntu system’s problem. I used PythonSlicer -m pip install to install pytorch. If I used DentalSegmentator to install pytorch within a freshly installed Slicer 5.9.0, it reported below error when installing numexpr:</p>
<pre><code class="lang-auto">Collecting numexpr
  Using cached numexpr-2.11.0.tar.gz (108 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'error'
  error: subprocess-exited-with-error

  × pip subprocess to install build dependencies did not run successfully.
  │ exit code: 1
  ╰─&gt; [51 lines of output]
      Collecting setuptools
        Using cached setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
      Collecting wheel
        Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
      Collecting numpy&gt;=2.0.0
        Using cached numpy-2.3.0.tar.gz (20.4 MB)
        Installing build dependencies: started
        Installing build dependencies: finished with status 'done'
        Getting requirements to build wheel: started
        Getting requirements to build wheel: finished with status 'done'
        Installing backend dependencies: started
        Installing backend dependencies: finished with status 'done'
        Preparing metadata (pyproject.toml): started
        Preparing metadata (pyproject.toml): finished with status 'error'
        error: subprocess-exited-with-error

        × Preparing metadata (pyproject.toml) did not run successfully.
        │ exit code: 1
        ╰─&gt; [22 lines of output]
            + /home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/python-real /tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1/vendored-meson/meson/meson.py setup /tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1 /tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1/.mesonpy-kqkrx0ha -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --native-file=/tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1/.mesonpy-kqkrx0ha/meson-python-native-file.ini
            The Meson build system
            Version: 1.6.1
            Source dir: /tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1
            Build dir: /tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1/.mesonpy-kqkrx0ha
            Build type: native build
            Project name: NumPy
            Project version: 2.3.0
            C compiler for the host machine: cc (gcc 11.4.0 "cc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0")
            C linker for the host machine: cc ld.bfd 2.38
            C++ compiler for the host machine: c++ (gcc 11.4.0 "c++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0")
            C++ linker for the host machine: c++ ld.bfd 2.38
            Cython compiler for the host machine: cython (cython 3.1.2)
            Host machine cpu family: x86_64
            Host machine cpu: x86_64
            Program python found: YES (/home/zhang/Slicer-5.9.0-2025-06-14-linux-amd64/bin/python-real)
            Found pkg-config: YES (/usr/bin/pkg-config) 0.29.2
            Run-time dependency python found: NO (tried pkgconfig, pkgconfig and sysconfig)

            ../meson.build:41:12: ERROR: Python dependency not found

            A full log can be found at /tmp/pip-install-y22nmtxm/numpy_51d4d08f7ec641d1a235f64003b012f1/.mesonpy-kqkrx0ha/meson-logs/meson-log.txt
            [end of output]

        note: This error originates from a subprocess, and is likely not a problem with pip.
      error: metadata-generation-failed

      × Encountered error while generating package metadata.
      ╰─&gt; See above for output.

      note: This is an issue with the package mentioned above, not pip.
      hint: See above for details.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× pip subprocess to install build dependencies did not run successfully.
│ exit code: 1
╰─&gt; See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
</code></pre>
<p>The Pytorch Util also showed nothing, including not recognizing nvidia driver:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfcccb6ad47f8e8ac61adc895efea1e69e217046.png" data-download-href="/uploads/short-url/tEhBCuqsMhbPM3LtmZeRWtALLyC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfcccb6ad47f8e8ac61adc895efea1e69e217046.png" alt="image" data-base62-sha1="tEhBCuqsMhbPM3LtmZeRWtALLyC" width="552" height="149"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×149 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I reinstall Pytorch via Pytorch Util, it recognized Nvidia driver and showed torch corrupted, which shouldn’t be a big probalem:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da0e2efbba7f9d0987f7427a9a4f6a4a60cf756a.png" data-download-href="/uploads/short-url/v70ty9JcV6ER0XumdvwntrsjEy6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da0e2efbba7f9d0987f7427a9a4f6a4a60cf756a.png" alt="image" data-base62-sha1="v70ty9JcV6ER0XumdvwntrsjEy6" width="552" height="149"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×149 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, Dental Segmentator showed the same error as in the original post.</p>
<p>Reinstall pytorch using PythonSlicer -m pip install will fix the torch corruption issue but still showed  the same error as the original post.</p>
<p>CPU mode in DentalSegmentator and TotalSegmentator also showed the same error as the original post.</p>

---

## Post #3 by @chz31 (2025-06-16 20:57 UTC)

<p>I think it is probably the version issue of the newest Slicer 5.9.0. Both Dental- and TotalSegmentator still worked with Pytorch-gpu in the most recent stable Slicer 5.8.1</p>

---

## Post #4 by @jamesobutler (2025-06-16 21:44 UTC)

<aside class="quote no-group" data-username="chz31" data-post="2" data-topic="43374">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<pre><code class="lang-auto">Collecting numexpr
  Using cached numexpr-2.11.0.tar.gz
</code></pre>
</blockquote>
</aside>
<p>It appears to be trying to build the <code>numexpr</code> package from source because the whl available is <code>numexpr-2.11.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl</code> which is too new of a glibc for what the Slicer Linux package is based off.</p>
<p>See the following about upcoming work to allow install of whls that are of newer manylinux_2_28 types:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8468#issuecomment-2946745251">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8468#issuecomment-2946745251" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8468#issuecomment-2946745251" target="_blank" rel="noopener nofollow ugc">Request for PyTorch 2.7 Support in 3D Slicer for NVIDIA Blackwell GPUs</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-05" data-time="17:00:16" data-timezone="UTC">05:00PM - 05 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/rodrigoteixeira7" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/215039333?v=4" class="onebox-avatar-inline" width="20" height="20">
          rodrigoteixeira7
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Request for PyTorch 2.7 Support in 3D Slicer for NVIDIA Blackwell GPUs

System I<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nformation:
- GPU: NVIDIA GeForce RTX 5070 Ti
- Architecture: NVIDIA Blackwell
- OS: Linux Unbutu 24.04.2 LTS

PyTorch version 2.7 introduces support for the Blackwell architecture, which is required for compatibility with this GPU. Earlier versions of PyTorch (≤2.6) do not support it, resulting in the following error:
- “The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90.”

Unfortunately, the PyTorch version currently available in 3D Slicer is&nbsp;limited&nbsp;to&nbsp;2.6

xref https://discourse.slicer.org/t/pytorch-cuda-incompatibility-with-nvidia-rtx-5070-ti/43233</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For now I would suggest trying these Slicer extensions on Windows or macOS.</p>

---

## Post #5 by @chz31 (2025-06-17 14:20 UTC)

<p>Thanks for the clarification. On Windows, I got the same errors for the newest Slicer 5.9.0.</p>

---

## Post #6 by @jamesobutler (2025-06-17 14:48 UTC)

<p>Can you post the error you observed on Windows? It was the same issue building the <code>numexpr</code> package? Or was it a different issue?</p>

---

## Post #7 by @chz31 (2025-06-17 18:41 UTC)

<p>No, it did not report the numexpr installation error. The auto pytorch installation via DentalSegmentator in a freshly install Slicer 5.9.0 was OK. I suspected it might be related to nnUnet. In Linux, after I manually installed pytorch, I got the same errors when running Dental- and TotalSegmentator.</p>
<p>In Dental Segmentator, the same error reported for loading the segmentations when I run auto-segmentation:</p>
<pre><code class="lang-auto">[Python] Failed to load the segmentation.
[Python] Something went wrong during the nnUNet processing.
[Python] Please check the logs for potential errors and contact the library maintainers.
</code></pre>
<p>Here is the full log:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 17.06.2025 13:26:34 [] (unknown:0) - Session start time .......: 20250617_132634
[DEBUG][Qt] 17.06.2025 13:26:34 [] (unknown:0) - Slicer version ...........: 5.9.0-2025-06-14 (revision 33686 / 7a97a67) win-amd64 - installed release
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 22631, Code Page 65001) - 64-bit
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Memory ...................: 64980 MB physical, 74708 MB virtual
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - CPU ......................: GenuineIntel , 22 cores, 22 logical processors
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - DCMTK configuration ......: version 3.6.8, no SSL
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Application path .........: C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin
[DEBUG][Qt] 17.06.2025 13:26:35 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-33686/NNUNet/lib/Slicer-5.9/qt-scripted-modules, slicer.org/Extensions-33686/PyTorch/lib/Slicer-5.9/qt-scripted-modules, slicer.org/Extensions-33686/DentalSegmentator/lib/Slicer-5.9/qt-scripted-modules, slicer.org/Extensions-33686/SlicerPythonTestRunner/lib/Slicer-5.9/qt-scripted-modules
[DEBUG][Python] 17.06.2025 13:26:37 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 17.06.2025 13:26:37 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 17.06.2025 13:26:37 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 17.06.2025 13:26:50 [] (unknown:0) - Switch to module:  "SampleData"
[DEBUG][Python] 17.06.2025 13:26:54 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Verifying checksum
[DEBUG][Python] 17.06.2025 13:26:54 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - File already exists and checksum is OK - reusing it.
[DEBUG][Python] 17.06.2025 13:26:54 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Requesting load PreDentalSurgery from C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PreDentalSurgery.gipl.gz ...
[DEBUG][Qt] 17.06.2025 13:26:55 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PreDentalSurgery.gipl.gz" "[0.30s]"
[DEBUG][Python] 17.06.2025 13:26:55 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Load finished
[DEBUG][Python] 17.06.2025 13:26:55 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Verifying checksum
[DEBUG][Python] 17.06.2025 13:26:55 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - File already exists and checksum is OK - reusing it.
[DEBUG][Python] 17.06.2025 13:26:55 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Requesting load PostDentalSurgery from C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PostDentalSurgery.gipl.gz ...
[DEBUG][Qt] 17.06.2025 13:26:55 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PostDentalSurgery.gipl.gz" "[0.32s]"
[DEBUG][Python] 17.06.2025 13:26:55 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py:408) - Load finished
[DEBUG][Qt] 17.06.2025 13:26:57 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 17.06.2025 13:27:05 [] (unknown:0) - Switch to module:  "DentalSegmentator"
[CRITICAL][Qt] 17.06.2025 13:27:05 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::setSourceVolumeNode(class vtkMRMLNode *)  failed: need to set segment editor and segmentation nodes first
[INFO][Python] 17.06.2025 13:27:11 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - Start nnUNet install with requirements : nnunetv2
[INFO][Python] 17.06.2025 13:27:11 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing nnunetv2 --no-deps...
[INFO][Stream] 17.06.2025 13:27:13 [] (unknown:0) - Collecting nnunetv2
[INFO][Stream] 17.06.2025 13:27:13 [] (unknown:0) -   Using cached nnunetv2-2.6.2-py3-none-any.whl
[INFO][Stream] 17.06.2025 13:27:13 [] (unknown:0) - Installing collected packages: nnunetv2
[INFO][Stream] 17.06.2025 13:27:14 [] (unknown:0) - Successfully installed nnunetv2-2.6.2
[INFO][Python] 17.06.2025 13:27:14 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing dynamic-network-architectures&lt;0.5,&gt;=0.4.1 --no-deps...
[INFO][Stream] 17.06.2025 13:27:15 [] (unknown:0) - Collecting dynamic-network-architectures&lt;0.5,&gt;=0.4.1
[INFO][Stream] 17.06.2025 13:27:15 [] (unknown:0) -   Using cached dynamic_network_architectures-0.4.2-py3-none-any.whl
[INFO][Stream] 17.06.2025 13:27:15 [] (unknown:0) - Installing collected packages: dynamic-network-architectures
[INFO][Stream] 17.06.2025 13:27:15 [] (unknown:0) - Successfully installed dynamic-network-architectures-0.4.2
[INFO][Python] 17.06.2025 13:27:15 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing timm --no-deps...
[INFO][Stream] 17.06.2025 13:27:16 [] (unknown:0) - Collecting timm
[INFO][Stream] 17.06.2025 13:27:16 [] (unknown:0) -   Using cached timm-1.0.15-py3-none-any.whl.metadata (52 kB)
[INFO][Stream] 17.06.2025 13:27:16 [] (unknown:0) - Using cached timm-1.0.15-py3-none-any.whl (2.4 MB)
[INFO][Stream] 17.06.2025 13:27:16 [] (unknown:0) - Installing collected packages: timm
[INFO][Stream] 17.06.2025 13:27:17 [] (unknown:0) - Successfully installed timm-1.0.15
[INFO][Python] 17.06.2025 13:27:17 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing pyyaml --no-deps...
[INFO][Stream] 17.06.2025 13:27:18 [] (unknown:0) - Collecting pyyaml
[INFO][Stream] 17.06.2025 13:27:18 [] (unknown:0) -   Using cached PyYAML-6.0.2-cp312-cp312-win_amd64.whl.metadata (2.1 kB)
[INFO][Stream] 17.06.2025 13:27:18 [] (unknown:0) - Using cached PyYAML-6.0.2-cp312-cp312-win_amd64.whl (156 kB)
[INFO][Stream] 17.06.2025 13:27:18 [] (unknown:0) - Installing collected packages: pyyaml
[INFO][Stream] 17.06.2025 13:27:18 [] (unknown:0) - Successfully installed pyyaml-6.0.2
[INFO][Python] 17.06.2025 13:27:18 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing huggingface_hub --no-deps...
[INFO][Stream] 17.06.2025 13:27:19 [] (unknown:0) - Collecting huggingface_hub
[INFO][Stream] 17.06.2025 13:27:19 [] (unknown:0) -   Using cached huggingface_hub-0.33.0-py3-none-any.whl.metadata (14 kB)
[INFO][Stream] 17.06.2025 13:27:19 [] (unknown:0) - Using cached huggingface_hub-0.33.0-py3-none-any.whl (514 kB)
[INFO][Stream] 17.06.2025 13:27:19 [] (unknown:0) - Installing collected packages: huggingface_hub
[INFO][Stream] 17.06.2025 13:27:20 [] (unknown:0) - Successfully installed huggingface_hub-0.33.0
[INFO][Python] 17.06.2025 13:27:20 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing filelock --no-deps...
[INFO][Stream] 17.06.2025 13:27:21 [] (unknown:0) - Collecting filelock
[INFO][Stream] 17.06.2025 13:27:21 [] (unknown:0) -   Using cached filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
[INFO][Stream] 17.06.2025 13:27:21 [] (unknown:0) - Using cached filelock-3.18.0-py3-none-any.whl (16 kB)
[INFO][Stream] 17.06.2025 13:27:21 [] (unknown:0) - Installing collected packages: filelock
[INFO][Stream] 17.06.2025 13:27:21 [] (unknown:0) - Successfully installed filelock-3.18.0
[INFO][Python] 17.06.2025 13:27:21 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing fsspec&gt;=2023.5.0 --no-deps...
[INFO][Stream] 17.06.2025 13:27:22 [] (unknown:0) - Collecting fsspec&gt;=2023.5.0
[INFO][Stream] 17.06.2025 13:27:22 [] (unknown:0) -   Using cached fsspec-2025.5.1-py3-none-any.whl.metadata (11 kB)
[INFO][Stream] 17.06.2025 13:27:22 [] (unknown:0) - Using cached fsspec-2025.5.1-py3-none-any.whl (199 kB)
[INFO][Stream] 17.06.2025 13:27:22 [] (unknown:0) - Installing collected packages: fsspec
[INFO][Stream] 17.06.2025 13:27:22 [] (unknown:0) - Successfully installed fsspec-2025.5.1
[INFO][Python] 17.06.2025 13:27:22 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing tqdm&gt;=4.42.1 --no-deps...
[INFO][Stream] 17.06.2025 13:27:23 [] (unknown:0) - Collecting tqdm&gt;=4.42.1
[INFO][Stream] 17.06.2025 13:27:23 [] (unknown:0) -   Using cached tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
[INFO][Stream] 17.06.2025 13:27:23 [] (unknown:0) - Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
[INFO][Stream] 17.06.2025 13:27:23 [] (unknown:0) - Installing collected packages: tqdm
[INFO][Stream] 17.06.2025 13:27:23 [] (unknown:0) - Successfully installed tqdm-4.67.1
[INFO][Python] 17.06.2025 13:27:23 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing colorama --no-deps...
[INFO][Stream] 17.06.2025 13:27:24 [] (unknown:0) - Collecting colorama
[INFO][Stream] 17.06.2025 13:27:24 [] (unknown:0) -   Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
[INFO][Stream] 17.06.2025 13:27:24 [] (unknown:0) - Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
[INFO][Stream] 17.06.2025 13:27:24 [] (unknown:0) - Installing collected packages: colorama
[INFO][Stream] 17.06.2025 13:27:24 [] (unknown:0) - Successfully installed colorama-0.4.6
[INFO][Python] 17.06.2025 13:27:24 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing safetensors --no-deps...
[INFO][Stream] 17.06.2025 13:27:25 [] (unknown:0) - Collecting safetensors
[INFO][Stream] 17.06.2025 13:27:25 [] (unknown:0) -   Using cached safetensors-0.5.3-cp38-abi3-win_amd64.whl.metadata (3.9 kB)
[INFO][Stream] 17.06.2025 13:27:25 [] (unknown:0) - Using cached safetensors-0.5.3-cp38-abi3-win_amd64.whl (308 kB)
[INFO][Stream] 17.06.2025 13:27:25 [] (unknown:0) - Installing collected packages: safetensors
[INFO][Stream] 17.06.2025 13:27:25 [] (unknown:0) - Successfully installed safetensors-0.5.3
[INFO][Python] 17.06.2025 13:27:25 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing einops --no-deps...
[INFO][Stream] 17.06.2025 13:27:26 [] (unknown:0) - Collecting einops
[INFO][Stream] 17.06.2025 13:27:26 [] (unknown:0) -   Using cached einops-0.8.1-py3-none-any.whl.metadata (13 kB)
[INFO][Stream] 17.06.2025 13:27:26 [] (unknown:0) - Using cached einops-0.8.1-py3-none-any.whl (64 kB)
[INFO][Stream] 17.06.2025 13:27:26 [] (unknown:0) - Installing collected packages: einops
[INFO][Stream] 17.06.2025 13:27:26 [] (unknown:0) - Successfully installed einops-0.8.1
[INFO][Python] 17.06.2025 13:27:26 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing batchgenerators&gt;=0.25.1 --no-deps...
[INFO][Stream] 17.06.2025 13:27:27 [] (unknown:0) - Collecting batchgenerators&gt;=0.25.1
[INFO][Stream] 17.06.2025 13:27:27 [] (unknown:0) -   Using cached batchgenerators-0.25.1-py3-none-any.whl
[INFO][Stream] 17.06.2025 13:27:27 [] (unknown:0) - Installing collected packages: batchgenerators
[INFO][Stream] 17.06.2025 13:27:28 [] (unknown:0) - Successfully installed batchgenerators-0.25.1
[INFO][Python] 17.06.2025 13:27:28 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing scikit-image --no-deps...
[INFO][Stream] 17.06.2025 13:27:28 [] (unknown:0) - Collecting scikit-image
[INFO][Stream] 17.06.2025 13:27:28 [] (unknown:0) -   Using cached scikit_image-0.25.2-cp312-cp312-win_amd64.whl.metadata (14 kB)
[INFO][Stream] 17.06.2025 13:27:28 [] (unknown:0) - Using cached scikit_image-0.25.2-cp312-cp312-win_amd64.whl (12.9 MB)
[INFO][Stream] 17.06.2025 13:27:29 [] (unknown:0) - Installing collected packages: scikit-image
[INFO][Stream] 17.06.2025 13:27:30 [] (unknown:0) - Successfully installed scikit-image-0.25.2
[INFO][Python] 17.06.2025 13:27:30 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing networkx&gt;=3.0 --no-deps...
[INFO][Stream] 17.06.2025 13:27:31 [] (unknown:0) - Collecting networkx&gt;=3.0
[INFO][Stream] 17.06.2025 13:27:31 [] (unknown:0) -   Using cached networkx-3.5-py3-none-any.whl.metadata (6.3 kB)
[INFO][Stream] 17.06.2025 13:27:31 [] (unknown:0) - Using cached networkx-3.5-py3-none-any.whl (2.0 MB)
[INFO][Stream] 17.06.2025 13:27:31 [] (unknown:0) - Installing collected packages: networkx
[INFO][Stream] 17.06.2025 13:27:34 [] (unknown:0) - Successfully installed networkx-3.5
[INFO][Python] 17.06.2025 13:27:34 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing imageio!=2.35.0,&gt;=2.33 --no-deps...
[INFO][Stream] 17.06.2025 13:27:35 [] (unknown:0) - Collecting imageio!=2.35.0,&gt;=2.33
[INFO][Stream] 17.06.2025 13:27:35 [] (unknown:0) -   Using cached imageio-2.37.0-py3-none-any.whl.metadata (5.2 kB)
[INFO][Stream] 17.06.2025 13:27:35 [] (unknown:0) - Using cached imageio-2.37.0-py3-none-any.whl (315 kB)
[INFO][Stream] 17.06.2025 13:27:35 [] (unknown:0) - Installing collected packages: imageio
[INFO][Stream] 17.06.2025 13:27:35 [] (unknown:0) - Successfully installed imageio-2.37.0
[INFO][Python] 17.06.2025 13:27:35 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing tifffile&gt;=2022.8.12 --no-deps...
[INFO][Stream] 17.06.2025 13:27:36 [] (unknown:0) - Collecting tifffile&gt;=2022.8.12
[INFO][Stream] 17.06.2025 13:27:36 [] (unknown:0) -   Using cached tifffile-2025.6.11-py3-none-any.whl.metadata (32 kB)
[INFO][Stream] 17.06.2025 13:27:36 [] (unknown:0) - Using cached tifffile-2025.6.11-py3-none-any.whl (230 kB)
[INFO][Stream] 17.06.2025 13:27:36 [] (unknown:0) - Installing collected packages: tifffile
[INFO][Stream] 17.06.2025 13:27:36 [] (unknown:0) - Successfully installed tifffile-2025.6.11
[INFO][Python] 17.06.2025 13:27:37 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing lazy-loader&gt;=0.4 --no-deps...
[INFO][Stream] 17.06.2025 13:27:37 [] (unknown:0) - Collecting lazy-loader&gt;=0.4
[INFO][Stream] 17.06.2025 13:27:37 [] (unknown:0) -   Using cached lazy_loader-0.4-py3-none-any.whl.metadata (7.6 kB)
[INFO][Stream] 17.06.2025 13:27:37 [] (unknown:0) - Using cached lazy_loader-0.4-py3-none-any.whl (12 kB)
[INFO][Stream] 17.06.2025 13:27:37 [] (unknown:0) - Installing collected packages: lazy-loader
[INFO][Stream] 17.06.2025 13:27:37 [] (unknown:0) - Successfully installed lazy-loader-0.4
[INFO][Python] 17.06.2025 13:27:38 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing scikit-learn --no-deps...
[INFO][Stream] 17.06.2025 13:27:39 [] (unknown:0) - Collecting scikit-learn
[INFO][Stream] 17.06.2025 13:27:39 [] (unknown:0) -   Using cached scikit_learn-1.7.0-cp312-cp312-win_amd64.whl.metadata (14 kB)
[INFO][Stream] 17.06.2025 13:27:39 [] (unknown:0) - Using cached scikit_learn-1.7.0-cp312-cp312-win_amd64.whl (10.7 MB)
[INFO][Stream] 17.06.2025 13:27:39 [] (unknown:0) - Installing collected packages: scikit-learn
[INFO][Stream] 17.06.2025 13:27:42 [] (unknown:0) - Successfully installed scikit-learn-1.7.0
[INFO][Python] 17.06.2025 13:27:43 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing joblib&gt;=1.2.0 --no-deps...
[INFO][Stream] 17.06.2025 13:27:43 [] (unknown:0) - Collecting joblib&gt;=1.2.0
[INFO][Stream] 17.06.2025 13:27:43 [] (unknown:0) -   Using cached joblib-1.5.1-py3-none-any.whl.metadata (5.6 kB)
[INFO][Stream] 17.06.2025 13:27:43 [] (unknown:0) - Using cached joblib-1.5.1-py3-none-any.whl (307 kB)
[INFO][Stream] 17.06.2025 13:27:44 [] (unknown:0) - Installing collected packages: joblib
[INFO][Stream] 17.06.2025 13:27:44 [] (unknown:0) - Successfully installed joblib-1.5.1
[INFO][Python] 17.06.2025 13:27:44 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing threadpoolctl&gt;=3.1.0 --no-deps...
[INFO][Stream] 17.06.2025 13:27:45 [] (unknown:0) - Collecting threadpoolctl&gt;=3.1.0
[INFO][Stream] 17.06.2025 13:27:45 [] (unknown:0) -   Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
[INFO][Stream] 17.06.2025 13:27:45 [] (unknown:0) - Using cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
[INFO][Stream] 17.06.2025 13:27:45 [] (unknown:0) - Installing collected packages: threadpoolctl
[INFO][Stream] 17.06.2025 13:27:45 [] (unknown:0) - Successfully installed threadpoolctl-3.6.0
[INFO][Python] 17.06.2025 13:27:45 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing future --no-deps...
[INFO][Stream] 17.06.2025 13:27:46 [] (unknown:0) - Collecting future
[INFO][Stream] 17.06.2025 13:27:46 [] (unknown:0) -   Using cached future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
[INFO][Stream] 17.06.2025 13:27:46 [] (unknown:0) - Using cached future-1.0.0-py3-none-any.whl (491 kB)
[INFO][Stream] 17.06.2025 13:27:46 [] (unknown:0) - Installing collected packages: future
[INFO][Stream] 17.06.2025 13:27:47 [] (unknown:0) - Successfully installed future-1.0.0
[INFO][Python] 17.06.2025 13:27:47 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing pandas --no-deps...
[INFO][Stream] 17.06.2025 13:27:48 [] (unknown:0) - Collecting pandas
[INFO][Stream] 17.06.2025 13:27:48 [] (unknown:0) -   Using cached pandas-2.3.0-cp312-cp312-win_amd64.whl.metadata (19 kB)
[INFO][Stream] 17.06.2025 13:27:48 [] (unknown:0) - Using cached pandas-2.3.0-cp312-cp312-win_amd64.whl (11.0 MB)
[INFO][Stream] 17.06.2025 13:27:48 [] (unknown:0) - Installing collected packages: pandas
[INFO][Stream] 17.06.2025 13:27:55 [] (unknown:0) - Successfully installed pandas-2.3.0
[INFO][Python] 17.06.2025 13:27:56 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing pytz&gt;=2020.1 --no-deps...
[INFO][Stream] 17.06.2025 13:27:56 [] (unknown:0) - Collecting pytz&gt;=2020.1
[INFO][Stream] 17.06.2025 13:27:56 [] (unknown:0) -   Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
[INFO][Stream] 17.06.2025 13:27:56 [] (unknown:0) - Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
[INFO][Stream] 17.06.2025 13:27:56 [] (unknown:0) - Installing collected packages: pytz
[INFO][Stream] 17.06.2025 13:27:57 [] (unknown:0) - Successfully installed pytz-2025.2
[INFO][Python] 17.06.2025 13:27:57 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing tzdata&gt;=2022.7 --no-deps...
[INFO][Stream] 17.06.2025 13:27:58 [] (unknown:0) - Collecting tzdata&gt;=2022.7
[INFO][Stream] 17.06.2025 13:27:58 [] (unknown:0) -   Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
[INFO][Stream] 17.06.2025 13:27:58 [] (unknown:0) - Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
[INFO][Stream] 17.06.2025 13:27:58 [] (unknown:0) - Installing collected packages: tzdata
[INFO][Stream] 17.06.2025 13:27:58 [] (unknown:0) - Successfully installed tzdata-2025.2
[INFO][Python] 17.06.2025 13:27:58 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing unittest2 --no-deps...
[INFO][Stream] 17.06.2025 13:27:59 [] (unknown:0) - Collecting unittest2
[INFO][Stream] 17.06.2025 13:27:59 [] (unknown:0) -   Using cached unittest2-1.1.0-py2.py3-none-any.whl.metadata (15 kB)
[INFO][Stream] 17.06.2025 13:27:59 [] (unknown:0) - Using cached unittest2-1.1.0-py2.py3-none-any.whl (96 kB)
[INFO][Stream] 17.06.2025 13:27:59 [] (unknown:0) - Installing collected packages: unittest2
[INFO][Stream] 17.06.2025 13:27:59 [] (unknown:0) - Successfully installed unittest2-1.1.0
[INFO][Python] 17.06.2025 13:28:00 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing argparse --no-deps...
[INFO][Stream] 17.06.2025 13:28:00 [] (unknown:0) - Collecting argparse
[INFO][Stream] 17.06.2025 13:28:00 [] (unknown:0) -   Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
[INFO][Stream] 17.06.2025 13:28:00 [] (unknown:0) - Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
[INFO][Stream] 17.06.2025 13:28:00 [] (unknown:0) - Installing collected packages: argparse
[INFO][Stream] 17.06.2025 13:28:00 [] (unknown:0) - Successfully installed argparse-1.4.0
[INFO][Python] 17.06.2025 13:28:01 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing traceback2 --no-deps...
[INFO][Stream] 17.06.2025 13:28:01 [] (unknown:0) - Collecting traceback2
[INFO][Stream] 17.06.2025 13:28:01 [] (unknown:0) -   Using cached traceback2-1.4.0-py2.py3-none-any.whl.metadata (1.5 kB)
[INFO][Stream] 17.06.2025 13:28:01 [] (unknown:0) - Using cached traceback2-1.4.0-py2.py3-none-any.whl (16 kB)
[INFO][Stream] 17.06.2025 13:28:01 [] (unknown:0) - Installing collected packages: traceback2
[INFO][Stream] 17.06.2025 13:28:01 [] (unknown:0) - Successfully installed traceback2-1.4.0
[INFO][Python] 17.06.2025 13:28:02 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing linecache2 --no-deps...
[INFO][Stream] 17.06.2025 13:28:02 [] (unknown:0) - Collecting linecache2
[INFO][Stream] 17.06.2025 13:28:02 [] (unknown:0) -   Using cached linecache2-1.0.0-py2.py3-none-any.whl.metadata (1000 bytes)
[INFO][Stream] 17.06.2025 13:28:02 [] (unknown:0) - Using cached linecache2-1.0.0-py2.py3-none-any.whl (12 kB)
[INFO][Stream] 17.06.2025 13:28:02 [] (unknown:0) - Installing collected packages: linecache2
[INFO][Stream] 17.06.2025 13:28:02 [] (unknown:0) - Successfully installed linecache2-1.0.0
[INFO][Python] 17.06.2025 13:28:03 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing graphviz --no-deps...
[INFO][Stream] 17.06.2025 13:28:03 [] (unknown:0) - Collecting graphviz
[INFO][Stream] 17.06.2025 13:28:03 [] (unknown:0) -   Using cached graphviz-0.21-py3-none-any.whl.metadata (12 kB)
[INFO][Stream] 17.06.2025 13:28:03 [] (unknown:0) - Using cached graphviz-0.21-py3-none-any.whl (47 kB)
[INFO][Stream] 17.06.2025 13:28:03 [] (unknown:0) - Installing collected packages: graphviz
[INFO][Stream] 17.06.2025 13:28:04 [] (unknown:0) - Successfully installed graphviz-0.21
[INFO][Python] 17.06.2025 13:28:04 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing nibabel --no-deps...
[INFO][Stream] 17.06.2025 13:28:04 [] (unknown:0) - Collecting nibabel
[INFO][Stream] 17.06.2025 13:28:04 [] (unknown:0) -   Using cached nibabel-5.3.2-py3-none-any.whl.metadata (9.1 kB)
[INFO][Stream] 17.06.2025 13:28:05 [] (unknown:0) - Using cached nibabel-5.3.2-py3-none-any.whl (3.3 MB)
[INFO][Stream] 17.06.2025 13:28:05 [] (unknown:0) - Installing collected packages: nibabel
[INFO][Stream] 17.06.2025 13:28:06 [] (unknown:0) - Successfully installed nibabel-5.3.2
[INFO][Python] 17.06.2025 13:28:06 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing matplotlib --no-deps...
[INFO][Stream] 17.06.2025 13:28:07 [] (unknown:0) - Collecting matplotlib
[INFO][Stream] 17.06.2025 13:28:07 [] (unknown:0) -   Using cached matplotlib-3.10.3-cp312-cp312-win_amd64.whl.metadata (11 kB)
[INFO][Stream] 17.06.2025 13:28:07 [] (unknown:0) - Using cached matplotlib-3.10.3-cp312-cp312-win_amd64.whl (8.1 MB)
[INFO][Stream] 17.06.2025 13:28:07 [] (unknown:0) - Installing collected packages: matplotlib
[INFO][Stream] 17.06.2025 13:28:09 [] (unknown:0) - Successfully installed matplotlib-3.10.3
[INFO][Python] 17.06.2025 13:28:09 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing contourpy&gt;=1.0.1 --no-deps...
[INFO][Stream] 17.06.2025 13:28:10 [] (unknown:0) - Collecting contourpy&gt;=1.0.1
[INFO][Stream] 17.06.2025 13:28:10 [] (unknown:0) -   Using cached contourpy-1.3.2-cp312-cp312-win_amd64.whl.metadata (5.5 kB)
[INFO][Stream] 17.06.2025 13:28:10 [] (unknown:0) - Using cached contourpy-1.3.2-cp312-cp312-win_amd64.whl (223 kB)
[INFO][Stream] 17.06.2025 13:28:10 [] (unknown:0) - Installing collected packages: contourpy
[INFO][Stream] 17.06.2025 13:28:10 [] (unknown:0) - Successfully installed contourpy-1.3.2
[INFO][Python] 17.06.2025 13:28:10 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing cycler&gt;=0.10 --no-deps...
[INFO][Stream] 17.06.2025 13:28:11 [] (unknown:0) - Collecting cycler&gt;=0.10
[INFO][Stream] 17.06.2025 13:28:11 [] (unknown:0) -   Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
[INFO][Stream] 17.06.2025 13:28:11 [] (unknown:0) - Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
[INFO][Stream] 17.06.2025 13:28:11 [] (unknown:0) - Installing collected packages: cycler
[INFO][Stream] 17.06.2025 13:28:11 [] (unknown:0) - Successfully installed cycler-0.12.1
[INFO][Python] 17.06.2025 13:28:11 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing fonttools&gt;=4.22.0 --no-deps...
[INFO][Stream] 17.06.2025 13:28:12 [] (unknown:0) - Collecting fonttools&gt;=4.22.0
[INFO][Stream] 17.06.2025 13:28:12 [] (unknown:0) -   Using cached fonttools-4.58.4-cp312-cp312-win_amd64.whl.metadata (108 kB)
[INFO][Stream] 17.06.2025 13:28:12 [] (unknown:0) - Using cached fonttools-4.58.4-cp312-cp312-win_amd64.whl (2.2 MB)
[INFO][Stream] 17.06.2025 13:28:12 [] (unknown:0) - Installing collected packages: fonttools
[INFO][Stream] 17.06.2025 13:28:14 [] (unknown:0) - Successfully installed fonttools-4.58.4
[INFO][Python] 17.06.2025 13:28:14 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing kiwisolver&gt;=1.3.1 --no-deps...
[INFO][Stream] 17.06.2025 13:28:15 [] (unknown:0) - Collecting kiwisolver&gt;=1.3.1
[INFO][Stream] 17.06.2025 13:28:15 [] (unknown:0) -   Using cached kiwisolver-1.4.8-cp312-cp312-win_amd64.whl.metadata (6.3 kB)
[INFO][Stream] 17.06.2025 13:28:15 [] (unknown:0) - Using cached kiwisolver-1.4.8-cp312-cp312-win_amd64.whl (71 kB)
[INFO][Stream] 17.06.2025 13:28:15 [] (unknown:0) - Installing collected packages: kiwisolver
[INFO][Stream] 17.06.2025 13:28:15 [] (unknown:0) - Successfully installed kiwisolver-1.4.8
[INFO][Python] 17.06.2025 13:28:15 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing seaborn --no-deps...
[INFO][Stream] 17.06.2025 13:28:16 [] (unknown:0) - Collecting seaborn
[INFO][Stream] 17.06.2025 13:28:16 [] (unknown:0) -   Using cached seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
[INFO][Stream] 17.06.2025 13:28:16 [] (unknown:0) - Using cached seaborn-0.13.2-py3-none-any.whl (294 kB)
[INFO][Stream] 17.06.2025 13:28:16 [] (unknown:0) - Installing collected packages: seaborn
[INFO][Stream] 17.06.2025 13:28:16 [] (unknown:0) - Successfully installed seaborn-0.13.2
[INFO][Python] 17.06.2025 13:28:16 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing imagecodecs --no-deps...
[INFO][Stream] 17.06.2025 13:28:17 [] (unknown:0) - Collecting imagecodecs
[INFO][Stream] 17.06.2025 13:28:17 [] (unknown:0) -   Using cached imagecodecs-2025.3.30-cp312-cp312-win_amd64.whl.metadata (20 kB)
[INFO][Stream] 17.06.2025 13:28:17 [] (unknown:0) - Using cached imagecodecs-2025.3.30-cp312-cp312-win_amd64.whl (28.9 MB)
[INFO][Stream] 17.06.2025 13:28:17 [] (unknown:0) - Installing collected packages: imagecodecs
[INFO][Stream] 17.06.2025 13:28:18 [] (unknown:0) - Successfully installed imagecodecs-2025.3.30
[INFO][Python] 17.06.2025 13:28:18 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing yacs --no-deps...
[INFO][Stream] 17.06.2025 13:28:18 [] (unknown:0) - Collecting yacs
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) -   Using cached yacs-0.1.8-py3-none-any.whl.metadata (639 bytes)
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) - Using cached yacs-0.1.8-py3-none-any.whl (14 kB)
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) - Installing collected packages: yacs
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) - Successfully installed yacs-0.1.8
[INFO][Python] 17.06.2025 13:28:19 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing batchgeneratorsv2&gt;=0.3.0 --no-deps...
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) - Collecting batchgeneratorsv2&gt;=0.3.0
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) -   Using cached batchgeneratorsv2-0.3.0-py3-none-any.whl
[INFO][Stream] 17.06.2025 13:28:19 [] (unknown:0) - Installing collected packages: batchgeneratorsv2
[INFO][Stream] 17.06.2025 13:28:20 [] (unknown:0) - Successfully installed batchgeneratorsv2-0.3.0
[INFO][Python] 17.06.2025 13:28:20 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing fft-conv-pytorch --no-deps...
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) - Collecting fft-conv-pytorch
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) -   Using cached fft_conv_pytorch-1.2.0-py3-none-any.whl.metadata (2.8 kB)
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) - Using cached fft_conv_pytorch-1.2.0-py3-none-any.whl (6.8 kB)
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) - Installing collected packages: fft-conv-pytorch
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) - Successfully installed fft-conv-pytorch-1.2.0
[INFO][Python] 17.06.2025 13:28:21 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing blosc2&gt;=3.0.0b1 --no-deps...
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) - Collecting blosc2&gt;=3.0.0b1
[INFO][Stream] 17.06.2025 13:28:21 [] (unknown:0) -   Using cached blosc2-3.4.0-cp312-cp312-win_amd64.whl.metadata (6.9 kB)
[INFO][Stream] 17.06.2025 13:28:22 [] (unknown:0) - Using cached blosc2-3.4.0-cp312-cp312-win_amd64.whl (2.2 MB)
[INFO][Stream] 17.06.2025 13:28:22 [] (unknown:0) - Installing collected packages: blosc2
[INFO][Stream] 17.06.2025 13:28:22 [] (unknown:0) - Successfully installed blosc2-3.4.0
[INFO][Python] 17.06.2025 13:28:22 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing ndindex --no-deps...
[INFO][Stream] 17.06.2025 13:28:23 [] (unknown:0) - Collecting ndindex
[INFO][Stream] 17.06.2025 13:28:23 [] (unknown:0) -   Using cached ndindex-1.10.0-cp312-cp312-win_amd64.whl.metadata (3.7 kB)
[INFO][Stream] 17.06.2025 13:28:23 [] (unknown:0) - Using cached ndindex-1.10.0-cp312-cp312-win_amd64.whl (157 kB)
[INFO][Stream] 17.06.2025 13:28:23 [] (unknown:0) - Installing collected packages: ndindex
[INFO][Stream] 17.06.2025 13:28:23 [] (unknown:0) - Successfully installed ndindex-1.10.0
[INFO][Python] 17.06.2025 13:28:23 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing msgpack --no-deps...
[INFO][Stream] 17.06.2025 13:28:24 [] (unknown:0) - Collecting msgpack
[INFO][Stream] 17.06.2025 13:28:24 [] (unknown:0) -   Using cached msgpack-1.1.1-cp312-cp312-win_amd64.whl.metadata (8.6 kB)
[INFO][Stream] 17.06.2025 13:28:24 [] (unknown:0) - Using cached msgpack-1.1.1-cp312-cp312-win_amd64.whl (72 kB)
[INFO][Stream] 17.06.2025 13:28:24 [] (unknown:0) - Installing collected packages: msgpack
[INFO][Stream] 17.06.2025 13:28:24 [] (unknown:0) - Successfully installed msgpack-1.1.1
[INFO][Python] 17.06.2025 13:28:24 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing platformdirs --no-deps...
[INFO][Stream] 17.06.2025 13:28:25 [] (unknown:0) - Collecting platformdirs
[INFO][Stream] 17.06.2025 13:28:25 [] (unknown:0) -   Using cached platformdirs-4.3.8-py3-none-any.whl.metadata (12 kB)
[INFO][Stream] 17.06.2025 13:28:25 [] (unknown:0) - Using cached platformdirs-4.3.8-py3-none-any.whl (18 kB)
[INFO][Stream] 17.06.2025 13:28:25 [] (unknown:0) - Installing collected packages: platformdirs
[INFO][Stream] 17.06.2025 13:28:25 [] (unknown:0) - Successfully installed platformdirs-4.3.8
[INFO][Python] 17.06.2025 13:28:25 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing numexpr --no-deps...
[INFO][Stream] 17.06.2025 13:28:26 [] (unknown:0) - Collecting numexpr
[INFO][Stream] 17.06.2025 13:28:26 [] (unknown:0) -   Using cached numexpr-2.11.0-cp312-cp312-win_amd64.whl.metadata (9.2 kB)
[INFO][Stream] 17.06.2025 13:28:26 [] (unknown:0) - Using cached numexpr-2.11.0-cp312-cp312-win_amd64.whl (146 kB)
[INFO][Stream] 17.06.2025 13:28:26 [] (unknown:0) - Installing collected packages: numexpr
[INFO][Stream] 17.06.2025 13:28:26 [] (unknown:0) - Successfully installed numexpr-2.11.0
[INFO][Python] 17.06.2025 13:28:26 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - - Installing py-cpuinfo --no-deps...
[INFO][Stream] 17.06.2025 13:28:27 [] (unknown:0) - Collecting py-cpuinfo
[INFO][Stream] 17.06.2025 13:28:27 [] (unknown:0) -   Using cached py_cpuinfo-9.0.0-py3-none-any.whl.metadata (794 bytes)
[INFO][Stream] 17.06.2025 13:28:27 [] (unknown:0) - Using cached py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
[INFO][Stream] 17.06.2025 13:28:27 [] (unknown:0) - Installing collected packages: py-cpuinfo
[INFO][Stream] 17.06.2025 13:28:27 [] (unknown:0) - Successfully installed py-cpuinfo-9.0.0
[INFO][Python] 17.06.2025 13:28:27 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - PyTorch Python package is required. Installing... (it may take several minutes)
[INFO][Python] 17.06.2025 13:28:27 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/slicer.org/Extensions-33686/PyTorch/lib/Slicer-5.9/qt-scripted-modules/PyTorchUtils.py:216) - Install PyTorch using light-the-torch with arguments: ['install', 'torch&gt;=2.1.2', 'torchvision']
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) - Collecting light-the-torch&gt;=0.5
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) -   Using cached light_the_torch-0.8.0-py3-none-any.whl.metadata (9.3 kB)
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) - Collecting pip&lt;24.4,&gt;=22.3 (from light-the-torch&gt;=0.5)
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) -   Using cached pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) - Using cached light_the_torch-0.8.0-py3-none-any.whl (14 kB)
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) - Using cached pip-24.3.1-py3-none-any.whl (1.8 MB)
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) - Installing collected packages: pip, light-the-torch
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) -   Attempting uninstall: pip
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) -     Found existing installation: pip 25.1.1
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) -     Uninstalling pip-25.1.1:
[INFO][Stream] 17.06.2025 13:28:28 [] (unknown:0) -       Successfully uninstalled pip-25.1.1
[INFO][Stream] 17.06.2025 13:28:30 [] (unknown:0) -
[INFO][Stream] 17.06.2025 13:28:30 [] (unknown:0) - Successfully installed light-the-torch-0.8.0 pip-24.3.1
[DEBUG][Python] 17.06.2025 13:28:30 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:206) - Registered VCS backend: bzr
[DEBUG][Python] 17.06.2025 13:28:30 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:206) - Registered VCS backend: git
[DEBUG][Python] 17.06.2025 13:28:30 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:206) - Registered VCS backend: hg
[DEBUG][Python] 17.06.2025 13:28:30 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\pip\_internal\vcs\versioncontrol.py:206) - Registered VCS backend: svn
[INFO][Stream] 17.06.2025 13:28:35 [] (unknown:0) - Collecting torch&gt;=2.1.2
[INFO][Stream] 17.06.2025 13:28:35 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/cu126/torch-2.7.1%2Bcu126-cp312-cp312-win_amd64.whl.metadata (27 kB)
[INFO][Stream] 17.06.2025 13:28:39 [] (unknown:0) - Collecting torchvision
[INFO][Stream] 17.06.2025 13:28:39 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/cu126/torchvision-0.22.1%2Bcu126-cp312-cp312-win_amd64.whl.metadata (6.3 kB)
[INFO][Stream] 17.06.2025 13:28:39 [] (unknown:0) - Requirement already satisfied: filelock in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch&gt;=2.1.2) (3.18.0)
[INFO][Stream] 17.06.2025 13:28:39 [] (unknown:0) - Requirement already satisfied: typing-extensions&gt;=4.10.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch&gt;=2.1.2) (4.14.0)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Collecting sympy&gt;=1.13.3 (from torch&gt;=2.1.2)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl.metadata (12 kB)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Requirement already satisfied: networkx in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch&gt;=2.1.2) (3.5)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Collecting jinja2 (from torch&gt;=2.1.2)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) -   Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Requirement already satisfied: fsspec in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch&gt;=2.1.2) (2025.5.1)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Requirement already satisfied: setuptools in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch&gt;=2.1.2) (80.9.0)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Requirement already satisfied: numpy in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torchvision) (2.0.2)
[INFO][Stream] 17.06.2025 13:28:42 [] (unknown:0) - Requirement already satisfied: pillow!=8.3.*,&gt;=5.3.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torchvision) (11.2.1)
[INFO][Stream] 17.06.2025 13:28:45 [] (unknown:0) - Collecting mpmath&lt;1.4,&gt;=1.1.0 (from sympy&gt;=1.13.3-&gt;torch&gt;=2.1.2)
[INFO][Stream] 17.06.2025 13:28:45 [] (unknown:0) -   Using cached https://download.pytorch.org/whl/mpmath-1.3.0-py3-none-any.whl (536 kB)
[INFO][Stream] 17.06.2025 13:28:45 [] (unknown:0) - Collecting MarkupSafe&gt;=2.0 (from jinja2-&gt;torch&gt;=2.1.2)
[INFO][Stream] 17.06.2025 13:28:45 [] (unknown:0) -   Using cached MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl.metadata (4.1 kB)
[INFO][Stream] 17.06.2025 13:28:46 [] (unknown:0) - Using cached https://download.pytorch.org/whl/cu126/torch-2.7.1%2Bcu126-cp312-cp312-win_amd64.whl (2716.9 MB)
[INFO][Stream] 17.06.2025 13:28:47 [] (unknown:0) - Using cached https://download.pytorch.org/whl/cu126/torchvision-0.22.1%2Bcu126-cp312-cp312-win_amd64.whl (6.3 MB)
[INFO][Stream] 17.06.2025 13:28:47 [] (unknown:0) - Using cached https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl (6.2 MB)
[INFO][Stream] 17.06.2025 13:28:47 [] (unknown:0) - Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
[INFO][Stream] 17.06.2025 13:28:47 [] (unknown:0) - Using cached MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl (15 kB)
[INFO][Stream] 17.06.2025 13:28:56 [] (unknown:0) - Installing collected packages: mpmath, sympy, MarkupSafe, jinja2, torch, torchvision
[INFO][Stream] 17.06.2025 13:29:45 [] (unknown:0) - Successfully installed MarkupSafe-3.0.2 jinja2-3.1.6 mpmath-1.3.0 sympy-1.13.3 torch-2.7.1+cu126 torchvision-0.22.1+cu126
[INFO][Python] 17.06.2025 13:29:47 [Python] (C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/slicer.org/Extensions-33686/PyTorch/lib/Slicer-5.9/qt-scripted-modules/PyTorchUtils.py:226) - PyTorch 2.7.1+cu126 installed successfully.
[INFO][Python] 17.06.2025 13:29:47 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - Installing a working acvl-utils package version...
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Collecting acvl_utils==0.2
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) -   Using cached acvl_utils-0.2-py3-none-any.whl
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: numpy in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from acvl_utils==0.2) (2.0.2)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: batchgenerators in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from acvl_utils==0.2) (0.25.1)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: torch in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from acvl_utils==0.2) (2.7.1+cu126)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: SimpleITK in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from acvl_utils==0.2) (2.4.0rc2.dev213)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: scikit-image in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from acvl_utils==0.2) (0.25.2)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Collecting connected-components-3d (from acvl_utils==0.2)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) -   Using cached connected_components_3d-3.24.0-cp312-cp312-win_amd64.whl.metadata (33 kB)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: pillow&gt;=7.1.2 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (11.2.1)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: scipy in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.13.1)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: scikit-learn in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.7.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: future in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.0.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: pandas in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (2.3.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: unittest2 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (1.1.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: threadpoolctl in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from batchgenerators-&gt;acvl_utils==0.2) (3.6.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: networkx&gt;=3.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (3.5)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: imageio!=2.35.0,&gt;=2.33 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (2.37.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: tifffile&gt;=2022.8.12 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (2025.6.11)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: packaging&gt;=21 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (25.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: lazy-loader&gt;=0.4 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from scikit-image-&gt;acvl_utils==0.2) (0.4)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: filelock in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (3.18.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: typing-extensions&gt;=4.10.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (4.14.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: sympy&gt;=1.13.3 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (1.13.3)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: jinja2 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (3.1.6)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: fsspec in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (2025.5.1)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: setuptools in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from torch-&gt;acvl_utils==0.2) (80.9.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from sympy&gt;=1.13.3-&gt;torch-&gt;acvl_utils==0.2) (1.3.0)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: MarkupSafe&gt;=2.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from jinja2-&gt;torch-&gt;acvl_utils==0.2) (3.0.2)
[INFO][Stream] 17.06.2025 13:29:48 [] (unknown:0) - Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2.9.0.post0)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Requirement already satisfied: pytz&gt;=2020.1 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2025.2)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Requirement already satisfied: tzdata&gt;=2022.7 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from pandas-&gt;batchgenerators-&gt;acvl_utils==0.2) (2025.2)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Requirement already satisfied: joblib&gt;=1.2.0 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from scikit-learn-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.5.1)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Collecting argparse (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) -   Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Requirement already satisfied: six&gt;=1.4 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.17.0)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Requirement already satisfied: traceback2 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.4.0)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Requirement already satisfied: linecache2 in c:\users\chi.zhang\appdata\local\slicer.org\slicer 5.9.0-2025-06-14\lib\python\lib\site-packages (from traceback2-&gt;unittest2-&gt;batchgenerators-&gt;acvl_utils==0.2) (1.0.0)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Using cached connected_components_3d-3.24.0-cp312-cp312-win_amd64.whl (505 kB)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Installing collected packages: argparse, connected-components-3d, acvl_utils
[INFO][Stream] 17.06.2025 13:29:49 [] (unknown:0) - Successfully installed acvl_utils-0.2 argparse-1.4.0 connected-components-3d-3.24.0
[INFO][Python] 17.06.2025 13:29:49 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\slicer.org\Extensions-33686\NNUNet\lib\Slicer-5.9\qt-scripted-modules\SlicerNNUNetLib\InstallLogic.py:56) - nnUNet installation completed successfully.
[DEBUG][Python] 17.06.2025 13:29:49 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:1049) - Starting new HTTPS connection (1): www.google.com:443
[DEBUG][Python] 17.06.2025 13:29:49 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:544) - https://www.google.com:443 "GET / HTTP/1.1" 200 None
[DEBUG][Python] 17.06.2025 13:29:49 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:1049) - Starting new HTTPS connection (1): api.github.com:443
[DEBUG][Python] 17.06.2025 13:29:49 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:544) - https://api.github.com:443 "GET /repos/gaudot/SlicerDentalSegmentator HTTP/1.1" 200 1477
[DEBUG][Python] 17.06.2025 13:29:49 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:1049) - Starting new HTTPS connection (1): api.github.com:443
[DEBUG][Python] 17.06.2025 13:29:50 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:544) - https://api.github.com:443 "GET /repos/gaudot/SlicerDentalSegmentator/releases HTTP/1.1" 200 817
[DEBUG][Python] 17.06.2025 13:29:50 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:1049) - Starting new HTTPS connection (1): api.github.com:443
[DEBUG][Python] 17.06.2025 13:29:50 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:544) - https://api.github.com:443 "GET /repos/gaudot/SlicerDentalSegmentator/releases/147040025/assets HTTP/1.1" 200 603
[DEBUG][Python] 17.06.2025 13:29:50 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:1049) - Starting new HTTPS connection (1): github.com:443
[DEBUG][Python] 17.06.2025 13:29:50 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:544) - https://github.com:443 "GET /gaudot/SlicerDentalSegmentator/releases/download/v1.0.0-alpha/Dataset111_453CT_v100.zip HTTP/1.1" 302 0
[DEBUG][Python] 17.06.2025 13:29:50 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:1049) - Starting new HTTPS connection (1): objects.githubusercontent.com:443
[DEBUG][Python] 17.06.2025 13:29:51 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\lib\Python\Lib\site-packages\urllib3\connectionpool.py:544) - https://objects.githubusercontent.com:443 "GET /github-production-release-asset-2e65be/770505096/cc62156e-5361-4c66-aebe-57bd05af8d21?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=releaseassetproduction%2F20250617%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20250617T182950Z&amp;X-Amz-Expires=300&amp;X-Amz-Signature=660b1f22a4547fa25103cc647437f370b6230635a551525f9d177ec580bb4b1a&amp;X-Amz-SignedHeaders=host&amp;response-content-disposition=attachment%3B%20filename%3DDataset111_453CT_v100.zip&amp;response-content-type=application%2Foctet-stream HTTP/1.1" 200 229698747
[ERROR][Python] 17.06.2025 13:30:04 [Python] (C:\Users\chi.zhang\AppData\Local\slicer.org\Slicer 5.9.0-2025-06-14\bin\Python\slicer\util.py:3146) - Failed to load the segmentation.
Something went wrong during the nnUNet processing.
Please check the logs for potential errors and contact the library maintainers.
</code></pre>
<p>I then tried TotalSegmentator:</p>
<pre><code class="lang-auto">[Python] Failed to compute results.
[Python] Command '['C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\chi.zhang\\AppData\\Local\\slicer.org\\Slicer 5.9.0-2025-06-14\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/chi.zhang/AppData/Local/Temp/Slicer/__SlicerTemp__2025-06-17_13+35+24.247/total-segmentator-input.nii', '-o', 'C:/Users/chi.zhang/AppData/Local/Temp/Slicer/__SlicerTemp__2025-06-17_13+35+24.247/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 1046, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 1113, in processVolume
    self.logProcessOutput(proc)
  File "C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/slicer.org/Extensions-33686/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules/TotalSegmentator.py", line 892, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/chi.zhang/AppData/Local/slicer.org/Slicer 5.9.0-2025-06-14/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\chi.zhang\\AppData\\Local\\slicer.org\\Slicer 5.9.0-2025-06-14\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/chi.zhang/AppData/Local/Temp/Slicer/__SlicerTemp__2025-06-17_13+35+24.247/total-segmentator-input.nii', '-o', 'C:/Users/chi.zhang/AppData/Local/Temp/Slicer/__SlicerTemp__2025-06-17_13+35+24.247/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>

---
