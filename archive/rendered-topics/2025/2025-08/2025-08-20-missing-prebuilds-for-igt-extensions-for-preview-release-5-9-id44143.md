---
topic_id: 44143
title: "Missing Prebuilds For Igt Extensions For Preview Release 5 9"
date: 2025-08-20
url: https://discourse.slicer.org/t/44143
---

# Missing prebuilds for IGT extensions for Preview Release 5.9

**Topic ID**: 44143
**Date**: 2025-08-20
**URL**: https://discourse.slicer.org/t/missing-prebuilds-for-igt-extensions-for-preview-release-5-9/44143

---

## Post #1 by @ruffsl (2025-08-20 07:08 UTC)

<p>Hello, I’m developing slicelet for image guided therapy, particularly a scripted slicelet for simpler R&amp;D. Ideally we’d like to use the Preview Release of Slicer 5.9 that ships with a more recent version of Python 3.12, however, it seems like a number of core IGT extensions are missing as of revision 33856 built 2025-08-19:</p>
<ul>
<li><a href="https://extensions.slicer.org/catalog/IGT/33856/linux" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/IGT/33856/linux</a></li>
</ul>
<p>Inspecting the Extensions-Nightly build status for IGT extensions of interest:</p>
<ul>
<li>SlicerIGSIO
<ul>
<li><a href="https://slicer.cdash.org/builds/3899313" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview - Build Summary</a></li>
<li><a href="https://github.com/IGSIO/SlicerIGSIO/tree/1a89776c9f1c8bbbad62000561aa892afe1e7077" class="inline-onebox" rel="noopener nofollow ugc">GitHub - IGSIO/SlicerIGSIO at 1a89776c9f1c8bbbad62000561aa892afe1e7077</a></li>
</ul>
</li>
<li>SlicerIGT
<ul>
<li><a href="https://slicer.cdash.org/builds/3899419" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview - Build Summary</a></li>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/tree/cc9678a9b6f91aa9ffde3ff0176cad357335616f" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerIGT at cc9678a9b6f91aa9ffde3ff0176cad357335616f</a></li>
</ul>
</li>
<li>SlicerOpenIGTLink
<ul>
<li><a href="https://slicer.cdash.org/builds/3899228" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview - Build Summary</a></li>
<li><a href="https://github.com/openigtlink/SlicerOpenIGTLink/tree/f806007ccc4b5c7cb6ea14979670a468b39c5a45" class="inline-onebox" rel="noopener nofollow ugc">GitHub - openigtlink/SlicerOpenIGTLink at f806007ccc4b5c7cb6ea14979670a468b39c5a45</a></li>
</ul>
</li>
</ul>
<p>The build errors for both SlicerIGSIO and SlicerOpenIGTLink are quite nondescript, while cmake error for SlicerIGT from the missing SlicerIGSIO simple enough.</p>
<pre><code class="lang-auto">[  2%] Creating directories for 'YASM'
[  5%] Performing download step (git clone) for 'YASM'
Cloning into 'YASM'...
Already on 'master'
Your branch is up to date with 'origin/master'.
gmake[5]: *** read jobs pipe: Bad file descriptor.  Stop.
gmake[5]: *** Waiting for unfinished jobs....
[  8%] Generate version-YASM.txt and license-YASM.txt
</code></pre>
<p>Any idea what may be blocking the build server here? Only one test is failing atm:</p>
<details><summary>IGT Extension Test Results:</summary>
<pre data-code-wrap="shell"><code class="lang-shell">ruffsl@box ~/w/s/S/inner-build&gt; make test
Running tests...
Test project /home/ruffsl/ws/slicer/SlicerIGSIO-Release/inner-build
    Start 1: vtkEncodeUncompressedSequenceTest
1/3 Test #1: vtkEncodeUncompressedSequenceTest ................   Passed    0.25 sec
    Start 2: qSlicerMetafileImporterModuleGenericTest
2/3 Test #2: qSlicerMetafileImporterModuleGenericTest .........   Passed    2.08 sec
    Start 3: qSlicerMetafileImporterModuleWidgetGenericTest
3/3 Test #3: qSlicerMetafileImporterModuleWidgetGenericTest ...   Passed    2.33 sec

100% tests passed, 0 tests failed out of 3

Label Time Summary:
qSlicerMetafileImporterModule    =   4.42 sec*proc (2 tests)
qSlicerVideoUtilModule           =   0.25 sec*proc (1 test)

Total Test time (real) =   4.67 sec
</code></pre>
<pre data-code-wrap="shell"><code class="lang-shell">ruffsl@box ~/w/s/SlicerIGT-Release&gt; make test
Running tests...
Test project /home/ruffsl/ws/slicer/SlicerIGT-Release
      Start  1: qSlicerBreachWarningModuleGenericTest
 1/36 Test  #1: qSlicerBreachWarningModuleGenericTest ..................................   Passed    1.67 sec
      Start  2: qSlicerBreachWarningModuleWidgetGenericTest
 2/36 Test  #2: qSlicerBreachWarningModuleWidgetGenericTest ............................   Passed    1.85 sec
      Start  3: py_BreachWarningSelfTest
 3/36 Test  #3: py_BreachWarningSelfTest ...............................................   Passed    9.96 sec
      Start  4: qSlicerCollectPointsModuleGenericTest
 4/36 Test  #4: qSlicerCollectPointsModuleGenericTest ..................................   Passed    1.56 sec
      Start  5: qSlicerCollectPointsModuleWidgetGenericTest
 5/36 Test  #5: qSlicerCollectPointsModuleWidgetGenericTest ............................   Passed    1.74 sec
      Start  6: qSlicerCreateModelsModuleGenericTest
 6/36 Test  #6: qSlicerCreateModelsModuleGenericTest ...................................   Passed    1.56 sec
      Start  7: qSlicerCreateModelsModuleWidgetGenericTest
 7/36 Test  #7: qSlicerCreateModelsModuleWidgetGenericTest .............................   Passed    1.82 sec
      Start  8: qSlicerFiducialRegistrationWizardModuleGenericTest
 8/36 Test  #8: qSlicerFiducialRegistrationWizardModuleGenericTest .....................   Passed    2.35 sec
      Start  9: qSlicerFiducialRegistrationWizardModuleWidgetGenericTest
 9/36 Test  #9: qSlicerFiducialRegistrationWizardModuleWidgetGenericTest ...............   Passed    2.55 sec
      Start 10: py_nomainwindow_qSlicerFiducialsToModelRegistrationModuleGenericTest
10/36 Test #10: py_nomainwindow_qSlicerFiducialsToModelRegistrationModuleGenericTest ...   Passed    2.43 sec
      Start 11: py_FiducialsToModelRegistration
11/36 Test #11: py_FiducialsToModelRegistration ........................................   Passed    4.24 sec
      Start 12: py_Guidelet
12/36 Test #12: py_Guidelet ............................................................   Passed    3.26 sec
      Start 13: qSlicerLandmarkDetectionModuleGenericTest
13/36 Test #13: qSlicerLandmarkDetectionModuleGenericTest ..............................   Passed    1.66 sec
      Start 14: qSlicerLandmarkDetectionModuleWidgetGenericTest
14/36 Test #14: qSlicerLandmarkDetectionModuleWidgetGenericTest ........................   Passed    1.77 sec
      Start 15: vtkLandmarkDetectionTest
15/36 Test #15: vtkLandmarkDetectionTest ...............................................   Passed    0.28 sec
      Start 16: qSlicerLandmarkDetectionModuleGenericTest
16/36 Test #16: qSlicerLandmarkDetectionModuleGenericTest ..............................   Passed    1.56 sec
      Start 17: qSlicerLandmarkDetectionModuleWidgetGenericTest
17/36 Test #17: qSlicerLandmarkDetectionModuleWidgetGenericTest ........................   Passed    1.79 sec
      Start 18: py_nomainwindow_qSlicerModelRegistrationModuleGenericTest
18/36 Test #18: py_nomainwindow_qSlicerModelRegistrationModuleGenericTest ..............   Passed    2.43 sec
      Start 19: py_ModelRegistration
19/36 Test #19: py_ModelRegistration ...................................................   Passed    4.13 sec
      Start 20: qSlicerPathExplorerModuleGenericTest
20/36 Test #20: qSlicerPathExplorerModuleGenericTest ...................................   Passed    2.49 sec
      Start 21: qSlicerPathExplorerModuleWidgetGenericTest
21/36 Test #21: qSlicerPathExplorerModuleWidgetGenericTest .............................   Passed    2.65 sec
      Start 22: vtkPivotCalibrationTest
22/36 Test #22: vtkPivotCalibrationTest ................................................   Passed    0.29 sec
      Start 23: qSlicerPivotCalibrationModuleGenericTest
23/36 Test #23: qSlicerPivotCalibrationModuleGenericTest ...............................   Passed    1.68 sec
      Start 24: qSlicerPivotCalibrationModuleWidgetGenericTest
24/36 Test #24: qSlicerPivotCalibrationModuleWidgetGenericTest .........................   Passed    1.87 sec
      Start 25: py_nomainwindow_qSlicerTextureModelModuleGenericTest
25/36 Test #25: py_nomainwindow_qSlicerTextureModelModuleGenericTest ...................   Passed    2.41 sec
      Start 26: py_TextureModel
26/36 Test #26: py_TextureModel ........................................................   Passed    9.46 sec
      Start 27: qSlicerTransformProcessorModuleGenericTest
27/36 Test #27: qSlicerTransformProcessorModuleGenericTest .............................   Passed    1.50 sec
      Start 28: qSlicerTransformProcessorModuleWidgetGenericTest
28/36 Test #28: qSlicerTransformProcessorModuleWidgetGenericTest .......................   Passed    1.69 sec
      Start 29: qSlicerUltrasoundSnapshotsModuleGenericTest
29/36 Test #29: qSlicerUltrasoundSnapshotsModuleGenericTest ............................   Passed    1.65 sec
      Start 30: qSlicerUltrasoundSnapshotsModuleWidgetGenericTest
30/36 Test #30: qSlicerUltrasoundSnapshotsModuleWidgetGenericTest ......................   Passed    1.84 sec
      Start 31: py_nomainwindow_qSlicerViewpointModuleGenericTest
31/36 Test #31: py_nomainwindow_qSlicerViewpointModuleGenericTest ......................   Passed    2.51 sec
      Start 32: py_Viewpoint
32/36 Test #32: py_Viewpoint ...........................................................   Passed    3.03 sec
      Start 33: qSlicerWatchdogModuleGenericTest
33/36 Test #33: qSlicerWatchdogModuleGenericTest .......................................   Passed    1.70 sec
      Start 34: qSlicerWatchdogModuleWidgetGenericTest
34/36 Test #34: qSlicerWatchdogModuleWidgetGenericTest .................................   Passed    1.78 sec
      Start 35: py_nomainwindow_qSlicerSequenceReplayModuleGenericTest
35/36 Test #35: py_nomainwindow_qSlicerSequenceReplayModuleGenericTest .................   Passed    2.38 sec
      Start 36: py_SequenceReplay
36/36 Test #36: py_SequenceReplay ......................................................   Passed    3.30 sec

100% tests passed, 0 tests failed out of 36

Label Time Summary:
qSlicerBreachWarningModule                 =   3.53 sec*proc (2 tests)
qSlicerCollectPointsModule                 =   3.31 sec*proc (2 tests)
qSlicerCreateModelsModule                  =   3.38 sec*proc (2 tests)
qSlicerFiducialRegistrationWizardModule    =   4.90 sec*proc (2 tests)
qSlicerLandmarkDetectionModule             =   7.07 sec*proc (5 tests)
qSlicerPathExplorerModule                  =   5.14 sec*proc (2 tests)
qSlicerPivotCalibrationModule              =   3.84 sec*proc (3 tests)
qSlicerTransformProcessorModule            =   3.18 sec*proc (2 tests)
qSlicerUltrasoundSnapshotsModule           =   3.49 sec*proc (2 tests)
qSlicerWatchdogModule                      =   3.48 sec*proc (2 tests)

Total Test time (real) =  90.85 sec
</code></pre>
<pre data-code-wrap="shell"><code class="lang-shell">ruffsl@box ~/w/s/S/inner-build&gt; make test
Running tests...
Test project /home/ruffsl/ws/slicer/SlicerOpenIGTLink-Release/inner-build
    Start 1: vtkMRMLConnectorCommandSendAndReceiveTest
1/8 Test #1: vtkMRMLConnectorCommandSendAndReceiveTest .........***Failed   15.28 sec
    Start 2: vtkMRMLConnectorImageSendAndReceiveTest
2/8 Test #2: vtkMRMLConnectorImageSendAndReceiveTest ...........   Passed   10.36 sec
    Start 3: qSlicerOpenIGTLinkRemoteModuleGenericTest
3/8 Test #3: qSlicerOpenIGTLinkRemoteModuleGenericTest .........   Passed    2.09 sec
    Start 4: qSlicerOpenIGTLinkRemoteModuleWidgetGenericTest
4/8 Test #4: qSlicerOpenIGTLinkRemoteModuleWidgetGenericTest ...   Passed    2.32 sec
    Start 5: qSlicerOpenIGTLinkRemoteModuleGenericTest
5/8 Test #5: qSlicerOpenIGTLinkRemoteModuleGenericTest .........   Passed    2.02 sec
    Start 6: qSlicerOpenIGTLinkRemoteModuleWidgetGenericTest
6/8 Test #6: qSlicerOpenIGTLinkRemoteModuleWidgetGenericTest ...   Passed    2.35 sec
    Start 7: qSlicerPlusRemoteModuleGenericTest
7/8 Test #7: qSlicerPlusRemoteModuleGenericTest ................   Passed    2.12 sec
    Start 8: qSlicerPlusRemoteModuleWidgetGenericTest
8/8 Test #8: qSlicerPlusRemoteModuleWidgetGenericTest ..........   Passed    2.32 sec

88% tests passed, 1 tests failed out of 8

Label Time Summary:
SlicerOpenIGTLink                 =  25.64 sec*proc (2 tests)
qSlicerOpenIGTLinkRemoteModule    =   8.77 sec*proc (4 tests)
qSlicerPlusRemoteModule           =   4.44 sec*proc (2 tests)

Total Test time (real) =  38.86 sec

The following tests FAILED:
          1 - vtkMRMLConnectorCommandSendAndReceiveTest (Failed)
Errors while running CTest
Output from these tests are in: /home/ruffsl/ws/slicer/SlicerOpenIGTLink-Release/inner-build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:91: test] Error 8
ruffsl@box ~/w/s/S/inner-build [2]&gt; make test ARGS="--rerun-failed --output-on-failure"
Running tests...
Test project /home/ruffsl/ws/slicer/SlicerOpenIGTLink-Release/inner-build
    Start 1: vtkMRMLConnectorCommandSendAndReceiveTest
1/1 Test #1: vtkMRMLConnectorCommandSendAndReceiveTest ...***Failed    0.42 sec
SUCCESS: connected to server
error: [/home/ruffsl/ws/slicer/SlicerOpenIGTLink-Release/inner-build/bin/SlicerOpenIGTLinkCxxTests] exit abnormally - Report the problem.


0% tests passed, 1 tests failed out of 1

Label Time Summary:
SlicerOpenIGTLink    =   0.42 sec*proc (1 test)

Total Test time (real) =   0.42 sec

The following tests FAILED:
          1 - vtkMRMLConnectorCommandSendAndReceiveTest (Failed)
Errors while running CTest
make: *** [Makefile:91: test] Error 8
</code></pre>
</details>
<hr>
<p>Following the docs, I’ve gone ahead and compiled 3D Slicer from source using Ubuntu 24.04, including the IGT extensions from the HEADs of their respective default branches, as linked above. All seems to build and run fine as show (unsure if SlicerIGSIO is tested here):</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1PGeVYoqFwHGzAL4wC2pgmfMllQj_oYk9/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1PGeVYoqFwHGzAL4wC2pgmfMllQj_oYk9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1PGeVYoqFwHGzAL4wC2pgmfMllQj_oYk9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1PGeVYoqFwHGzAL4wC2pgmfMllQj_oYk9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">simplescreenrecorder-2025-08-19_19.39.42.webm</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Example scene attached, sans the <code>CTChest.nrrd</code> from downloaded sample data:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/18sx1h9j2NFOkWeo37aKfhZh5Q1Wj3Bhd/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/18sx1h9j2NFOkWeo37aKfhZh5Q1Wj3Bhd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/18sx1h9j2NFOkWeo37aKfhZh5Q1Wj3Bhd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/18sx1h9j2NFOkWeo37aKfhZh5Q1Wj3Bhd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">4up_Tracking_RIO.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And synthetic transform publisher for animating the example demo:</p>
<pre data-code-wrap="python"><code class="lang-python">"""
============================
Position sending server
============================

Simple application that starts a server that provides a stream of random positions.

from slicer.util import pip_install
pip_install("pyigtl")

Adapted from:
https://github.com/lassoan/pyigtl/blob/d28132d8e9e1cef4ac531d795f5284c8aa739408/examples/example_position_server.py
https://github.com/lassoan/pyigtl/blob/d28132d8e9e1cef4ac531d795f5284c8aa739408/pyigtl/tests/test_basic_comm.py#L87-L93
"""

import pyigtl  # pylint: disable=import-error

from time import sleep
import numpy as np
from scipy.spatial.transform import Rotation as R

server = pyigtl.OpenIGTLinkServer(port=18944)

transverse180 = np.array([
    [-1.0,  0.0,  0.0,  0.0],
    [ 0.0,  1.0,  0.0,  0.0],
    [ 0.0,  0.0, -1.0,  0.0],
    [ 0.0,  0.0,  0.0,  1.0]
])

timestep = 0
while True:
    if not server.is_connected():
        # Wait for client to connect
        sleep(0.1)
        continue

    # Generate periodic trajectory: Lissajous curve on sphere
    timestep += 1
    radius = 50.0
    center = np.array([0.0, 0.0, -100.0])
    # Use two periodic angles for smooth looping
    phi = (timestep * 0.001) % (2 * np.pi)  # azimuthal
    theta = (timestep * 0.002) % (2 * np.pi) # polar
    x = center[0] + radius * np.sin(theta) * np.cos(phi)
    y = center[1] + radius * np.sin(theta) * np.sin(phi)
    z = center[2] + radius * np.cos(theta)
    position = np.array([x, y, z])

    # Orientation: always point toward center
    forward = center - position
    forward = forward / np.linalg.norm(forward)
    up = np.array([0.0, 1.0, 0.0])
    if np.abs(np.dot(forward, up)) &gt; 0.99:
        up = np.array([1.0, 0.0, 0.0])
    rot_obj, _ = R.align_vectors([forward, up], [[0, 0, 1], [0, 1, 0]])
    rot_matrix = rot_obj.as_matrix()
    # Build 4x4 transform
    transform = np.eye(4)
    transform[:3, :3] = rot_matrix
    transform[:3, 3] = position

    transform_message = pyigtl.TransformMessage(transform, device_name='ToolToRAS')
    server.send_message(transform_message, wait=True)
    transform_message = pyigtl.TransformMessage(transverse180, device_name='TipToTool')
    server.send_message(transform_message, wait=True)
    # Since we wait until the message is actually sent, the message queue will not be flooded
</code></pre>

---

## Post #2 by @RafaelPalomar (2025-08-20 15:48 UTC)

<p><a class="mention" href="/u/ruffsl">@ruffsl</a> the infrastructure for building extensions on GNU/Linux has been updated recently. Some extensions seem to have been affected by this update ( <a href="https://discourse.slicer.org/t/slicer-build-environment-upgraded-to-qt5-almalinux8-gcc14/43802/6" class="inline-onebox">Slicer Build Environment Upgraded to `qt5-almalinux8-gcc14` - #6 by fedorov</a> ). Our colleagues from Kitware are aware of this issue and will check on it soon.</p>
<p>While extensions such as SlicerSOFA and DCMQI seem to fail only in the GNU/Linux build system, some other extension may fail legitimately because they need an update to adapt to the new build system. To test in which case the IGT extensions fall into, it is not enough to build them in your own system. A good test to discriminate whether the extension needs an update or the build system needs and adjustment, you would need to build Slicer and the extensions using Slicer building environment. <a class="mention" href="/u/ruffsl">@ruffsl</a>, would you have the availability to give the extensions a try with <a href="https://github.com/Slicer/SlicerBuildEnvironment" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a> using the <code>qt5-almalinux8-gcc14</code> environment? This would help speeding up the diagnostic and eventual resolution of the problem.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #3 by @ruffsl (2025-08-21 02:01 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="2" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>would you have the availability to give the extensions a try with <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a> using the <code>qt5-almalinux8-gcc14</code> environment?</p>
</blockquote>
</aside>
<p>I gave it a go using the reference in the readme, see my exact script included below:</p>
<details><summary>Build Script</summary>
<pre data-code-wrap="bash"><code class="lang-bash">#!/usr/bin/env bash

################################################################################
# MARK: Build Slicer
################################################################################

SLICER_BUILD_ENV_NAME=qt5-almalinux8-gcc14 
SLICER_BUILD_ENV_VERSION=5.9
SLICER_BRANCH=main

ROOT_DIR=/tmp/Slicer-$SLICER_BUILD_ENV_VERSION
mkdir -p $ROOT_DIR

cd ${ROOT_DIR}

slicer_build_env_script=/tmp/bin/slicer-buildenv-$SLICER_BUILD_ENV_NAME-$SLICER_BUILD_ENV_VERSION
mkdir -p $(dirname $slicer_build_env_script)

# Download sources
git clone https://github.com/Slicer/Slicer -b $SLICER_BRANCH

# Download corresponding build environment and generate convenience script
docker run --rm slicer/buildenv-qt5-almalinux8-gcc14 &gt; $slicer_build_env_script
chmod u+x $slicer_build_env_script

# Configure Slicer
$slicer_build_env_script cmake \
  -BSlicer-build \
  -SSlicer \
  -GNinja \
  -DCMAKE_BUILD_TYPE:STRING=Release

# Build Slicer
$slicer_build_env_script cmake --build Slicer-build

# Package Slicer
$slicer_build_env_script cmake --build Slicer-build/Slicer-build --target package

################################################################################
# MARK: Build Extension
################################################################################

EXTENSION_NAME=SlicerOpenIGTLink

# Download extension source
git clone https://github.com/openigtlink/SlicerOpenIGTLink.git ${EXTENSION_NAME}

# Configure the extension
$slicer_build_env_script cmake \
  -B${EXTENSION_NAME}-build \
  -S${EXTENSION_NAME} \
  -GNinja \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DSlicer_DIR:PATH=/work/Slicer-build/Slicer-build

# Build the extension
$slicer_build_env_script cmake --build ${EXTENSION_NAME}-build

# Package the extension
$slicer_build_env_script cmake --build ${EXTENSION_NAME}-build --target package
</code></pre>
</details>
<p>However, the build for the extension failed:</p>
<pre><code class="lang-auto">[24/26] No install step for 'inner'
[26/26] Completed 'inner'
ninja: error: unknown target 'package'
</code></pre>
<aside class="onebox pastebin" data-onebox-src="https://pastebin.com/MYY5NxNs">
  <header class="source">

      <a href="https://pastebin.com/MYY5NxNs" target="_blank" rel="noopener nofollow ugc">pastebin.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://pastebin.com/MYY5NxNs" target="_blank" rel="noopener nofollow ugc">https://pastebin.com/MYY5NxNs</a></h4>

<pre><code class="lang-auto"></code></pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr>
<p>I will note that one thing that tripped my up from the docs while packaging the exetentions from my local source builds on my Ubuntu host was that <code>make package</code> would not work as expected from the toplevel build folder for for either <code>SlicerIGSIO</code> and <code>SlicerOpenIGTLink</code>,</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#create-an-extension-package" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#create-an-extension-package</a></li>
</ul>
<p>Instead I had to <code>cd</code> into <code>SlicerOpenIGTLink-Release/inner-build</code> and <code>SlicerIGSIO-Release/inner-build</code> to find the Makefile with the expected <code>package</code> function call.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO/blob/1a89776c9f1c8bbbad62000561aa892afe1e7077/CMakeLists.txt#L14-L15">
  <header class="source">

      <a href="https://github.com/IGSIO/SlicerIGSIO/blob/1a89776c9f1c8bbbad62000561aa892afe1e7077/CMakeLists.txt#L14-L15" target="_blank" rel="noopener nofollow ugc">github.com/IGSIO/SlicerIGSIO</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/IGSIO/SlicerIGSIO/blob/1a89776c9f1c8bbbad62000561aa892afe1e7077/CMakeLists.txt#L14-L15" target="_blank" rel="noopener nofollow ugc">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/IGSIO/SlicerIGSIO/blob/1a89776c9f1c8bbbad62000561aa892afe1e7077/CMakeLists.txt#L14-L15" rel="noopener nofollow ugc"><code>1a89776c9</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="14" style="counter-reset: li-counter 13 ;">
          <li>set(EXTENSION_BUILD_SUBDIRECTORY inner-build)</li>
          <li>set(SUPERBUILD_TOPLEVEL_PROJECT inner)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/CMakeLists.txt#L14-L15">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/CMakeLists.txt#L14-L15" target="_blank" rel="noopener nofollow ugc">github.com/openigtlink/SlicerOpenIGTLink</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/CMakeLists.txt#L14-L15" target="_blank" rel="noopener nofollow ugc">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/CMakeLists.txt#L14-L15" rel="noopener nofollow ugc"><code>f806007cc</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="14" style="counter-reset: li-counter 13 ;">
          <li>set(EXTENSION_BUILD_SUBDIRECTORY inner-build)</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This isn’t something I encountered when building <code>SlicerIGT</code> from source.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/SuperBuild.cmake#L58-L59">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/SuperBuild.cmake#L58-L59" target="_blank" rel="noopener nofollow ugc">github.com/SlicerIGT/SlicerIGT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/SuperBuild.cmake#L58-L59" target="_blank" rel="noopener nofollow ugc">SuperBuild.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/SuperBuild.cmake#L58-L59" rel="noopener nofollow ugc"><code>cc9678a9b</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="58" style="counter-reset: li-counter 57 ;">
          <li>BINARY_DIR ${EXTENSION_BUILD_SUBDIRECTORY}</li>
          <li>CMAKE_GENERATOR ${gen}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr>
<p>Also, it looks like I can’t run the finished Slicer build from outside the docker image on my host:</p>
<pre data-code-wrap="shell"><code class="lang-shell">ruffsl@box /t/S/S/Slicer-build&gt; ./Slicer --version
/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./SlicerApp-real: error while loading shared libraries: libCTKQtTesting.so.0.1: cannot open shared object file: No such file or directory
</code></pre>
<p>Although I suspect that’s as expected without these new different QT 5 libs installed locally?</p>

---

## Post #4 by @RafaelPalomar (2025-08-23 17:33 UTC)

<p><a class="mention" href="/u/ruffsl">@ruffsl</a>, thanks for having a look at it so quickly. And very good investigation job!</p>
<aside class="quote no-group" data-username="ruffsl" data-post="3" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<p><code>ninja: error: unknown target 'package'</code></p>
</blockquote>
</aside>
<p>This is expected since the SlicerOpenIGTLink is a superbuild extension. Superbuild extensions build first an ecosystem of libraries to support the build of the extension, which as you found out happens in <code>inner-build</code>. The script should probably account for that and issue:</p>
<pre><code class="lang-auto">$slicer_build_env_script cmake --build ${EXTENSION_NAME}-build/inner-build --target package
</code></pre>
<p>–</p>
<aside class="quote no-group" data-username="ruffsl" data-post="3" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<p>Also, it looks like I can’t run the finished Slicer build from outside the docker image on my host:</p>
<pre><code class="lang-auto">ruffsl@box /t/S/S/Slicer-build&gt; ./Slicer --version
/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./SlicerApp-real: error while loading shared libraries: libCTKQtTesting.so.0.1: cannot open shared object file: No such file or directory
</code></pre>
<p>Although I suspect that’s as expected without these new different QT 5 libs installed locally?</p>
</blockquote>
</aside>
<p>Yes, that’s what I think. To fully verify you could try executing 3D Slicer inside the container, but I don’t think it is needed. You have successfully build the SlicerOpenIGTLink, with the Slicer environment, which does not happen in the Slicer infrastructure.</p>
<p>Let’s report all of this as an issue in 3D Slicer (if there’s not one yet) and continue the discussion from there. Send me a private with your github handle, if you want to be notified and participate there. I would be useful if you could give it a try to SlicerIGSIO and SlicerIGT too, as they seem to fail in different ways (in reality, SlicerIGT seems to fail due to SlicerIGSIO not being built).</p>
<p>Thank you for the great insight you have provided on the problem.</p>

---

## Post #5 by @ruffsl (2025-08-25 19:02 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="4" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>The script should probably account for that and issue:</p>
</blockquote>
</aside>
<pre data-code-wrap="diff"><code class="lang-diff">-$slicer_build_env_script cmake --build ${EXTENSION_NAME}-build --target package
+$slicer_build_env_script cmake --build ${EXTENSION_NAME}-build/inner-build --target package
</code></pre>
<p>A case by case change, or something should <code>slicer_build_env_script</code> auto detect?</p>
<p>That worked for packaging <code>SlicerOpenIGTLink</code> via <code>qt5-almalinux8-gcc14</code>:</p>
<pre><code class="lang-auto">[24/26] No install step for 'inner'
[26/26] Completed 'inner'

real    0m36.421s
user    0m0.046s
sys     0m0.053s
[0/1] Run CPack packaging tool...
CPack: Create package using TGZ
CPack: Install projects
CPack: - Install project: SlicerOpenIGTLink []
CPack: - Install project: OpenIGTLink []
CPack: - Install project: OpenIGTLinkIO []
CPack: Create package
CPack: - package: /work/SlicerOpenIGTLink-build/inner-build/33872-linux-amd64-SlicerOpenIGTLink-gitf806007-2025-07-26.tar.gz generated.
</code></pre>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="4" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>would be useful if you could give it a try to SlicerIGSIO and SlicerIGT too</p>
</blockquote>
</aside>
<p>Looks like they both build packages, but as before, can’t run this Slicer on host to test:</p>
<pre><code class="lang-auto">[31/34] No install step for 'inner'
[34/34] Completed 'inner'

real    1m11.141s
user    0m0.031s
sys     0m0.056s
[0/1] Run CPack packaging tool...
CPack: Create package using TGZ
CPack: Install projects
CPack: - Install project: SlicerIGSIO []
CPack: - Install project: IGSIO []
CPack: Create package
CPack: - package: /work/SlicerIGSIO-build/inner-build/33872-linux-amd64-SlicerIGSIO-git1a89776-2023-10-03.tar.gz generated.
</code></pre>
<pre data-code-wrap="diff"><code class="lang-diff">EXTENSION_NAME=SlicerIGT

# Download extension source
git clone https://github.com/SlicerIGT/SlicerIGT.git ${EXTENSION_NAME}

# Configure the extension
$slicer_build_env_script cmake \
  -B${EXTENSION_NAME}-build \
  -S${EXTENSION_NAME} \
  -GNinja \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DSlicer_DIR:PATH=/work/Slicer-build/Slicer-build \
+  -DSlicerIGSIO_DIR:PATH=/work/SlicerIGSIO-build/inner-build

# Build the extension
time $slicer_build_env_script cmake --build ${EXTENSION_NAME}-build | tee extension_build.log

# Package the extension
$slicer_build_env_script cmake --build ${EXTENSION_NAME}-build --target package
</code></pre>
<pre><code class="lang-auto">real    0m30.716s
user    0m0.045s
sys     0m0.062s
[0/1] Run CPack packaging tool...
CPack: Create package using TGZ
CPack: Install projects
CPack: - Install project: SlicerIGT []
CPack: Create package
CPack: - package: /work/SlicerIGT-build/33872-linux-amd64-SlicerIGT-gitcc9678a-2025-08-19.tar.gz generated.
</code></pre>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="4" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Let’s report all of this as an issue in 3D Slicer (if there’s not one yet) and continue the discussion from there.</p>
</blockquote>
</aside>
<p>On which repo issue tracker in particular? Of these?</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a></li>
<li><a href="https://github.com/Slicer/DashboardScripts" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/DashboardScripts: Collection of scripts used to configure/build/test/package 3D Slicer and associated extensions</a></li>
<li><a href="https://github.com/Slicer/SlicerBuildEnvironment" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a></li>
</ul>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="4" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>your github handle, if you want to be notified and participate there.</p>
</blockquote>
</aside>
<p>My user handle on GitHub is the same as here:</p>
<ul>
<li><a href="https://github.com/ruffsl" class="inline-onebox" rel="noopener nofollow ugc">ruffsl (Ruffin) · GitHub</a></li>
</ul>

---

## Post #6 by @lassoan (2025-08-25 19:40 UTC)

<p>If you used the official Slicer build environment to build the package then you can install that package in the matching official Slicer Preview Release.</p>

---

## Post #7 by @ruffsl (2025-08-25 22:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can install that package in the matching official Slicer Preview Release.</p>
</blockquote>
</aside>
<p>The source checkout of Slicer I used with the build environment was the current <code>HEAD</code> of the <code>main</code> branch (<code>b5a65a49a08171276f6a9624999450c0e8ec0116</code>). How can discover what commit was used in the compilation for a given build jobs. E.g:</p>
<ul>
<li><a href="https://slicer.cdash.org/builds/3905813" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview - Build Summary</a></li>
<li><a href="https://slicer.cdash.org/build/3905813/files" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview - Uploads</a></li>
</ul>
<p>It looks like the <code>Help -&gt; About 3D Slicer</code> menu does display a valid commit sha in the version string (but not in <code>Slicer --launcher-version</code> oddly enough):</p>
<pre><code class="lang-auto">5.9.0-2025-08-22 r33871 / c7e7ed1
</code></pre>
<ul>
<li><a href="https://github.com/Slicer/Slicer/commit/c7e7ed13f809b6af859af7aae3e7736d72057a5f" class="inline-onebox" rel="noopener nofollow ugc">ENH: Match color label title font size to legend font size · Slicer/Slicer@c7e7ed1 · GitHub</a></li>
</ul>
<p>But I can’t find the corresponding job for commit <code>c7e7ed1</code>, nor what commit a given job corresponds without downloading and inspecting each separate binary archive.</p>
<p>I’d just like to be sure I’m using the exact matching source trees for apples to apples.</p>
<p>That said, it looks to be installing &amp; working, so I suppose the extensions built on top of <code>b5a65a4</code> are close enough to <code>c7e7ed1</code> in terms of API/ABI at the moment.</p>
<hr>
<p>This all aside, it is concerning that the official Slicer build environment when used locally is not outputting an equivalent running binary as the remote buildfarm does.</p>

---

## Post #8 by @jamesobutler (2025-08-26 00:29 UTC)

<p>The Slicer Preview across all platforms is built daily starting at 11pm ET, so the latest commit on <code>main</code> is what is used for the build. You can see at <a href="https://slicer.cdash.org/index.php?project=SlicerPreview" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview</a> the commit hash that was checked out for each platform. As of writing this <code>c7e7ed1</code>was the latest commit when it was triggered last night. The <code>b5a65a4</code> was the next commit which came several hours later in the morning ET. Slicer Previews are built once daily by the factory machines and are not built and packaged for each commit to <code>main</code>.</p>

---

## Post #9 by @ruffsl (2025-08-26 15:26 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Slicer Previews are built once daily by the factory machines and are not built and packaged for each commit to <code>main</code>.</p>
</blockquote>
</aside>
<p>Now understood; not every commit may be scheduled for daily build.</p>
<p>Thanks for pointing out the <code>Revision</code> column in the <code>Nightly-Packages</code> table includes the Git commit sha. I was fruitlessly looking for the sha under the job’s own page. From the dashboard URLs, I see the build stores this revision info under the slug <code>/update</code>.</p>
<pre data-code-wrap="diff"><code class="lang-diff">-https://slicer.cdash.org/builds/3906947
+https://slicer.cdash.org/builds/3906947/update
</code></pre>
<p>However, where is this revision info for extensions jobs under <code>Extensions-Nightly</code>?</p>
<ul>
<li><a href="https://slicer.cdash.org/builds/3907251/update" rel="noopener nofollow ugc">https://slicer.cdash.org/builds/3907251/update</a></li>
</ul>

---

## Post #10 by @ruffsl (2025-08-26 16:48 UTC)

<aside class="quote no-group" data-username="ruffsl" data-post="7" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<p>This all aside, it is concerning that the official Slicer build environment when used locally is not outputting an equivalent running binary as the remote buildfarm does.</p>
</blockquote>
</aside>
<p>In searching for resources on the missing <code>libCTKQtTesting.so</code> library, in found:</p>
<aside class="quote quote-modified" data-post="4" data-topic="31318">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-5-2-2-linux-amd64-slicer-does-not-launch/31318/4">Slicer-5.2.2-linux-amd64/Slicer does not launch</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hi <a class="mention" href="/u/tbillah">@tbillah</a> - it looks like you didn’t run the ldd inside the shell launched by the Slicer launcher. 
Try this: 
ubuntu@sdp-console:/home/pieper$ cd ~/Downloads/Slicer-5.4.0-linux-amd64
ubuntu@sdp-console:~/Downloads/Slicer-5.4.0-linux-amd64$ ./Slicer --launch ldd bin/SlicerApp-real 
        linux-vdso.so.1 (0x00007ffc31a93000)
        libqSlicerApp.so =&gt; /home/ubuntu/Downloads/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/libqSlicerApp.so (0x00007fc7d156e000)
        libqSlicerBaseQTApp.so =&gt; …
  </blockquote>
</aside>

<p>An sure enough, <code>libCTKQtTesting.so</code> was merely just the first shared lib not found:</p>
<pre data-code-wrap="shell"><code class="lang-shell">~/t/S/S/Slicer-build&gt; ./Slicer --launch ldd ./bin/SlicerApp-real | head
        linux-vdso.so.1 (0x0000773d3e11d000)
        libqSlicerApp.so =&gt; /home/ruffsl/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./libqSlicerApp.so (0x0000773d3e073000)
        libqSlicerBaseQTApp.so =&gt; /home/ruffsl/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./libqSlicerBaseQTApp.so (0x0000773d3e01f000)
        libqSlicerModulesCore.so =&gt; /home/ruffsl/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./libqSlicerModulesCore.so (0x0000773d3dfff000)
        libqSlicerBaseQTCLI.so =&gt; /home/ruffsl/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./libqSlicerBaseQTCLI.so (0x0000773d3df9d000)
        libqSlicerBaseQTGUI.so =&gt; /home/ruffsl/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./libqSlicerBaseQTGUI.so (0x0000773d3dc00000)
        libqMRMLWidgets.so =&gt; /home/ruffsl/tmp/Slicer-5.9/Slicer-build/Slicer-build/bin/./libqMRMLWidgets.so (0x0000773d3d800000)
        libCTKQtTesting.so.0.1 =&gt; not found
        libCTKVisualizationVTKWidgets.so.0.1 =&gt; not found
        libCTKScriptingPythonWidgets.so.0.1 =&gt; not found
</code></pre>
<p>After downloading and inspecting the buildfarm artifacts for the same commit, noticed the file tree was different compared to my local cmake build folder, and that I was attempting to run the <code>Slicer</code> binary directly, rather than from the extracted launcher binary from the generated <code>.tar.gz</code> archive nested inside the very same local build.</p>
<p>Sure enough, the packaged version is working as expected without any missing libs:</p>
<pre><code class="lang-auto">~/t/S/S/Slicer-build/Slicer-5.9.0-2025-08-25-linux-amd64$ ./Slicer \
    --launch ldd ./bin/SlicerApp-real | grep "not found"
~/t/S/S/Slicer-build/Slicer-5.9.0-2025-08-25-linux-amd64$
</code></pre>
<p>Is this the Cmake macro triggered by this corresponding command? Cpack is new to me.</p>
<pre><code class="lang-auto">$slicer_build_env_script cmake --build Slicer-build/Slicer-build --target package
</code></pre>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/CMake/SlicerPackageAndUploadTarget.cmake#L142-L146">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/CMake/SlicerPackageAndUploadTarget.cmake#L142-L146" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/CMake/SlicerPackageAndUploadTarget.cmake#L142-L146" target="_blank" rel="noopener nofollow ugc">CMake/SlicerPackageAndUploadTarget.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/CMake/SlicerPackageAndUploadTarget.cmake#L142-L146" rel="noopener nofollow ugc"><code>284df9431</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="142" style="counter-reset: li-counter 141 ;">
          <li>#-----------------------------------------------------------------------------</li>
          <li># Package and upload</li>
          <li>#-----------------------------------------------------------------------------</li>
          <li></li>
          <li># Build package target and extract list of generated packages</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @jamesobutler (2025-08-26 16:49 UTC)

<h4><a name="p-127879-h-33881-slicerigt-gitcc9678a-g-64bits-qt515-release-1" class="anchor" href="#p-127879-h-33881-slicerigt-gitcc9678a-g-64bits-qt515-release-1" aria-label="Heading link"></a><strong>33881-SlicerIGT-gitcc9678a-g+±64bits-Qt5.15-Release</strong></h4>
<p>^This was building commit <a href="https://github.com/SlicerIGT/SlicerIGT/commit/cc9678a9b6f91aa9ffde3ff0176cad357335616f" rel="noopener nofollow ugc">cc9678a</a> of SlicerIGT repo using the SlicerPreview build of Slicer core that was built.</p>

---

## Post #12 by @ruffsl (2025-08-26 16:55 UTC)

<p>How is that association traced? Or just fuzzy search via timestamps? Git only timestamps commits creation, not when the commit was push to a remote branch.</p>

---

## Post #13 by @jamesobutler (2025-08-26 17:01 UTC)

<p>SlicerIGT’s extension index entry specifies to use the latest of the <code>master</code> branch as stated <a href="https://github.com/Slicer/ExtensionsIndex/blob/3d062ee7cd56253dc70305d20b8fee1031ba865f/SlicerIGT.json#L8" rel="noopener nofollow ugc">here</a>. So at build time it will pull the latest which in that specific case was <a href="https://github.com/SlicerIGT/SlicerIGT/commit/cc9678a9b6f91aa9ffde3ff0176cad357335616f" rel="noopener nofollow ugc">cc9678a</a>. Git has both authored date and commit date, and in this situation was pulling the latest of the <code>master</code> branch at build time.</p>

---

## Post #14 by @ruffsl (2025-08-28 14:42 UTC)

<aside class="quote no-group quote-modified" data-username="ruffsl" data-post="5" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="4" data-topic="44143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Let’s report all of this as an issue in 3D Slicer (if there’s not one yet) and continue the discussion from there.</p>
</blockquote>
</aside>
<p>On which repo issue tracker in particular? Of these?</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a></li>
<li><a href="https://github.com/Slicer/DashboardScripts" rel="noopener nofollow ugc">GitHub - Slicer/DashboardScripts: Collection of scripts used to configure/build/test/package 3D Slicer and associated extensions</a></li>
<li><a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a></li>
</ul>
</blockquote>
</aside>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> , was a ticket created, our should I add it?</p>

---
