# Alpaca error in 'Run Subsampling'

**Topic ID**: 22552
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/alpaca-error-in-run-subsampling/22552

---

## Post #1 by @Christianne (2022-03-16 20:53 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 4.13.0-2022-03-10<br>
Expected behavior: Run subsampling<br>
Actual behavior: Error in running subsampling</p>
<p>Hi all,</p>
<p>I’m new to SlicerMorph. I downloaded it a few days ago, but unfortunately the Sandbox extension wasn’t available. SO I ended up downloading the SlicerMorph Nightly version. That worked and I was able to get all the extensions I needed.<br>
Going through the tutorial for running Alpaca (<a href="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA" rel="noopener nofollow ugc">here</a>), I ran into an error when I click ‘Run Subsampling’:</p>
<p>:: Loading point clouds and downsampling<br>
Traceback (most recent call last):<br>
File “C:/ProgramData/NA-MIC/Slicer 4.13.0-2022-03-10/NA-MIC/Extensions-30699/SlicerMorph/lib/Slicer-4.13/qt-scripted-modules/ALPACA.py”, line 352, in onSubsampleButton<br>
self.targetFeatures, self.voxelSize, self.scaling = logic.runSubsample(self.sourceModelSelector.currentPath,<br>
File “C:/ProgramData/NA-MIC/Slicer 4.13.0-2022-03-10/NA-MIC/Extensions-30699/SlicerMorph/lib/Slicer-4.13/qt-scripted-modules/ALPACA.py”, line 903, in runSubsample<br>
source_down, source_fpfh = self.preprocess_point_cloud(source, voxel_size, parameters[“normalSearchRadius”], parameters[“FPFHSearchRadius”])<br>
File “C:/ProgramData/NA-MIC/Slicer 4.13.0-2022-03-10/NA-MIC/Extensions-30699/SlicerMorph/lib/Slicer-4.13/qt-scripted-modules/ALPACA.py”, line 944, in preprocess_point_cloud<br>
from open3d import registration<br>
<strong>ImportError: cannot import name ‘registration’ from ‘open3d’ (C:\ProgramData\NA-MIC\Slicer 4.13.0-2022-03-10\lib\Python\Lib\site-packages\open3d_<em>init</em>_.py)</strong></p>
<p>Open3d didn’t have any issues installing when I had first opened Alpaca. I opened the python interactor window, typed<br>
import open3d<br>
<code>open3d.__version__</code></p>
<p>and the version I have installed is 0.15.1</p>
<p>Alpaca didn’t automatically install pycpd, so I went ahead and installed it : pip_install(“pycpd”)<br>
But I keep getting the ImportError everytime I try and click run subsampling. I’ve tried uninstalling open3d, then reinstalling. I’ve also tried installing open3d versions 1.10 (which doesn’t even want to install) and version 1.14.1, but the error persists.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/288ce008a18313292d33f14803695c6b59c15203.jpeg" data-download-href="/uploads/short-url/5MIVbGHIPnPXMFTBp7YitFdMilR.jpeg?dl=1" title="Landmarks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/288ce008a18313292d33f14803695c6b59c15203_2_690x372.jpeg" alt="Landmarks" data-base62-sha1="5MIVbGHIPnPXMFTBp7YitFdMilR" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/288ce008a18313292d33f14803695c6b59c15203_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/288ce008a18313292d33f14803695c6b59c15203_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/288ce008a18313292d33f14803695c6b59c15203_2_1380x744.jpeg 2x" data-dominant-color="737392"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Landmarks</span><span class="informations">1864×1006 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I also don’t have some features within the Single Alignment tab that the tutorial has, such as the ‘Select subsampling voxel size’. I don’t know if that’s going to harm me down the road.</p>
<p>Any suggestions on how I can get past the ‘Run Subsampling’ without encountering this error?</p>

---

## Post #2 by @smrolfe (2022-03-17 17:33 UTC)

<p><a class="mention" href="/u/christianne">@Christianne</a> thanks for reporting this. The fix for this issue in the Preview version will be available later today on our repository, or in the extension manager tomorrow.</p>

---
