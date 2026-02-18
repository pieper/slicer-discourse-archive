# Build failed on Window10 when "Performing install step for 'python-scipy'"

**Topic ID**: 25135
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/build-failed-on-window10-when-performing-install-step-for-python-scipy/25135

---

## Post #1 by @Gitty_Wang (2022-09-07 06:27 UTC)

<p>Operating system: Window10<br>
Slicer version: 5.1.0<br>
Expected behavior: build successfully and can run &lt;Slicer_BUILD&gt;/Slicer-build/Slicer.exe<br>
Actual behavior: build failed with some error about python-scipy. And Slicer.exe was not created under Slicer-build folder.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8a3e45a3182f979e27840d5fe546ffd5f635938.jpeg" data-download-href="/uploads/short-url/sCWD7SL7CTexAwPTXIoYBVZpq2I.jpeg?dl=1" title="bdaac5c0ffbb996c9fb137cef7c55cc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8a3e45a3182f979e27840d5fe546ffd5f635938_2_561x500.jpeg" alt="bdaac5c0ffbb996c9fb137cef7c55cc" data-base62-sha1="sCWD7SL7CTexAwPTXIoYBVZpq2I" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8a3e45a3182f979e27840d5fe546ffd5f635938_2_561x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8a3e45a3182f979e27840d5fe546ffd5f635938.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8a3e45a3182f979e27840d5fe546ffd5f635938.jpeg 2x" data-dominant-color="251E1F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bdaac5c0ffbb996c9fb137cef7c55cc</span><span class="informations">830×739 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-09-07 20:40 UTC)

<p>Your build path is too long and that might be the source of this error - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#set-up-source-and-build-folders:~:text=Recommended%20path%3A,total%20path%20length">this info</a>.</p>

---

## Post #3 by @Gitty_Wang (2022-09-08 05:06 UTC)

<p>Thanks for your replying~</p>
<p>I’ve shorten the source path. But the error still occurred~<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daa6cc77ba5af0d00d0ad62eef7288361513105c.jpeg" data-download-href="/uploads/short-url/vchs5Pe3SPWuY31baBLh5etvH3u.jpeg?dl=1" title="slicer_build_error_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa6cc77ba5af0d00d0ad62eef7288361513105c_2_493x500.jpeg" alt="slicer_build_error_1" data-base62-sha1="vchs5Pe3SPWuY31baBLh5etvH3u" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa6cc77ba5af0d00d0ad62eef7288361513105c_2_493x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa6cc77ba5af0d00d0ad62eef7288361513105c_2_739x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa6cc77ba5af0d00d0ad62eef7288361513105c_2_986x1000.jpeg 2x" data-dominant-color="201D1D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_build_error_1</span><span class="informations">1026×1039 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The content of  error log file “python-scipy-install-err.log” is as following,</p>
<pre><code class="lang-auto">WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
ERROR: Could not find a version that satisfies the requirement scipy==1.8.1 (from versions: none)
ERROR: No matching distribution found for scipy==1.8.1
WARNING: There was an error checking the latest version of pip.
</code></pre>
<p>The content of “python-scipy-install-out.log” file is ,</p>
<pre><code class="lang-auto">Could not fetch URL https://pypi.org/simple/scipy/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/scipy/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
</code></pre>

---

## Post #4 by @Gitty_Wang (2022-09-14 01:08 UTC)

<p>I have built successfully now.</p>
<p>The key points which prevent me from compiling successfully are as following,</p>
<ol>
<li>As pieper reminded, my build path is too long,</li>
<li>For the MSB8066 error, it is always caused by network error. Just run the command “cmake --build . --config Release” again and again.</li>
<li>The following error message troubled me 3 days,<br>
<code>C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'D:\S4\Modules\CLI\GradientAnisotropicDiffusion\Data\Baseline\GradientAnisotropicDiffusionTestWithImageSpacingOff.nhdr.md5;D:\S4\Modules\CLI\GradientAnisotropicDiffusion\Data\Baseline\GradientAnisotropicDiffusionTestWithImageSpacingOff.raw.gz.md5;D:\S4\Modules\CLI\GradientAnisotropicDiffusion\Data\Baseline\GradientAnisotropicDiffusionTestWithImageSpacingOn.nhdr.md5;D:\S4\Modules\CLI\GradientAnisotropicDiffusion\Data\Baseline\GradientAnisotropicDiffusionTestWithImageSpacingOn.raw.gz.md5;D:\S4\Modules\CLI\GradientAnisotropicDiffusion\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\GradientAnisotropicDiffusion\Data\Input\MRHeadResampled.raw.gz.md5;D:\S4\Modules\CLI\GrayscaleFillHoleImageFilter\Data\Baseline\GrayscaleFillHoleTest.nhdr.md5;D:\S4\Modules\CLI\GrayscaleFillHoleImageFilter\Data\Baseline\GrayscaleFillHoleTest.raw.gz.md5;D:\S4\Modules\CLI\GrayscaleFillHoleImageFilter\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\GrayscaleFillHoleImageFilter\Data\Input\MRHeadResampled.raw.gz.md5;D:\S4\Modules\CLI\GrayscaleGrindPeakImageFilter\Data\Baseline\GrayscaleGrindPeakTest.nhdr.md5;D:\S4\Modules\CLI\GrayscaleGrindPeakImageFilter\Data\Baseline\GrayscaleGrindPeakTest.raw.gz.md5;D:\S4\Modules\CLI\GrayscaleGrindPeakImageFilter\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\GrayscaleGrindPeakImageFilter\Data\Input\MRHeadResampled.raw.gz.md5;D:\S4\Modules\CLI\HistogramMatching\Data\Baseline\HistogramMatchingTest.nhdr.md5;D:\S4\Modules\CLI\HistogramMatching\Data\Baseline\HistogramMatchingTest.raw.gz.md5;D:\S4\Modules\CLI\HistogramMatching\Data\Input\CTHeadAxial.nhdr.md5;D:\S4\Modules\CLI\HistogramMatching\Data\Input\CTHeadAxial.raw.gz.md5;D:\S4\Modules\CLI\HistogramMatching\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\HistogramMatching\Data\Input\MRHeadResampled.raw.gz.md5;D:\S4\Modules\CLI\LabelMapSmoothing\Data\Baseline\LabelMapSmoothingTest.nhdr.md5;D:\S4\Modules\CLI\LabelMapSmoothing\Data\Baseline\LabelMapSmoothingTest.raw.gz.md5;D:\S4\Modules\CLI\LabelMapSmoothing\Data\Input\CTHeadResampledOtsuSegmented.nhdr.md5;D:\S4\Modules\CLI\LabelMapSmoothing\Data\Input\CTHeadResampledOtsuSegmented.raw.gz.md5;D:\S4\Modules\CLI\MaskScalarVolume\Data\Baseline\MaskedVolume.nrrd.md5;D:\S4\Modules\CLI\MaskScalarVolume\Data\Input\CTHeadAxial.n hdr.md5;D:\S4\Modules\CLI\MaskScalarVolume\Data\Input\CTHeadAxial.raw.gz.md5;D:\S4\Modules\CLI\MaskScalarVolume\Data\Input\CTHeadAxialMask.nrrd.md5;D:\S4\Modules\CLI\MedianImageFilter\Data \Baseline\MedianImageFilterTest.nhdr.md5;D:\S4\Modules\CLI\MedianImageFilter\Data\Baseline\MedianImageFilterTest.raw.md5;D:\S4\Modules\CLI\MedianImageFilter\Data\Input\CTHeadAxial.nhdr.md5 ;D:\S4\Modules\CLI\MedianImageFilter\Data\Input\CTHeadAxial.raw.gz.md5;D:\S4\Modules\CLI\MergeModels\Data\Baseline\sphereCube.vtp.sha256;D:\S4\Modules\CLI\MergeModels\Data\Input\cube.vtk.md5;D:\S4\Modules\CLI\MergeModels\Data\Input\cube.vtp.md5;D:\S4\Modules\CLI\MergeModels\Data\Input\sphere.vtk.md5;D:\S4\Modules\CLI\MergeModels\Data\Input\sphere.vtp.md5;D:\S4\Modules\CLI\ModelMaker\Data\Input\helix-roi-lable2.nrrd.md5;D:\S4\Modules\CLI\ModelMaker\Data\Input\helixMask3Labels.nrrd.md5;D:\S4\Modules\CLI\ModelToLabelMap\Data\Baseline\OAS10001-128.mha.sha256;D:\ S4\Modules\CLI\ModelToLabelMap\Data\Baseline\OAS10001-255.mha.sha256;D:\S4\Modules\CLI\ModelToLabelMap\Data\Input\OAS10001-Transformed.vtp.sha256;D:\S4\Modules\CLI\ModelToLabelMap\Data\Inp ut\OAS10001.nii.gz.sha256;D:\S4\Modules\CLI\MultiplyScalarVolumes\Data\Baseline\MultiplyScalarVolumesTest.1.nrrd.md5;D:\S4\Modules\CLI\MultiplyScalarVolumes\Data\Baseline\MultiplyScalarVol umesTest.nrrd.md5;D:\S4\Modules\CLI\MultiplyScalarVolumes\Data\Input\CTHeadAxial.nhdr.md5;D:\S4\Modules\CLI\MultiplyScalarVolumes\Data\Input\CTHeadAxial.raw.gz.md5;D:\S4\Modules\CLI\N4ITKBiasFieldCorrection\Data\Baseline\he3corrected.nii.gz.md5;D:\S4\Modules\CLI\N4ITKBiasFieldCorrection\Data\Input\he3mask.nii.gz.md5;D:\S4\Modules\CLI\N4ITKBiasFieldCorrection\Data\Input\he3v olume.nii.gz.md5;D:\S4\Modules\CLI\OrientScalarVolume\Data\Baseline\OrientScalarVolumeTestAxial.nrrd.md5;D:\S4\Modules\CLI\OrientScalarVolume\Data\Baseline\OrientScalarVolumeTestCoronal.nr rd.md5;D:\S4\Modules\CLI\OrientScalarVolume\Data\Baseline\OrientScalarVolumeTestSagittal.nrrd.md5;D:\S4\Modules\CLI\OrientScalarVolume\Data\Input\fixed.nrrd.md5;D:\S4\Modules\CLI\ResampleD TIVolume\Data\Baseline\Brain_slice.nrrd.md5;D:\S4\Modules\CLI\ResampleDTIVolume\Data\Baseline\dt-helix-ref-BS.nrrd.md5;D:\S4\Modules\CLI\ResampleDTIVolume\Data\Baseline\dt-helix-ref-BSInte rpolation.nrrd.md5;D:\S4\Modules\CLI\ResampleDTIVolume\Data\Baseline\dt-helix-ref-HField.nrrd.md5;D:\S4\Modules\CLI\ResampleDTIVolume\Data\Baseline\dt-helix-ref-Rotated.nrrd.md5;D:\S4\Modu les\CLI\ResampleDTIVolume\Data\Baseline\dt-helix-ref-RotationAndAffine.nrrd.md5;D:\S4\Modules\CLI\ResampleDTIVolume\Data\Input\deformationField.nrrd.md5;D:\S4\Modules\CLI\ResampleDTIVolume \Data\Input\dt-helix.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadResampled .raw.gz.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadResampledBSplineInterpolationTest.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadRes ampledBSplineWSInterpolationTest.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadResampledHField.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Inp ut\MRHeadResampledHFieldTest.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadResampledRotationAndAffine.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVectorDWIVolume\Data\Input\MRHeadResampledRotationNN.nrrd.md5;D:\S4\Modules\CLI\ResampleScalarVolume\Data\Baseline\ResampleScalarVolumeTest.nhdr.md5;D:\S4\Modules\CLI\ResampleScalarVolume\Data\Baseline\Res ampleScalarVolumeTest.raw.gz.md5;D:\S4\Modules\CLI\ResampleScalarVolume\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\ResampleScalarVolume\Data\Input\MRHeadResampled.raw.gz.md5;D:\ S4\Modules\CLI\RobustStatisticsSegmenter\Data\Input\grayscale-label.nrrd.md5;D:\S4\Modules\CLI\RobustStatisticsSegmenter\Data\Input\grayscale.nrrd.md5;D:\S4\Modules\CLI\SimpleRegionGrowing Segmentation\Data\Baseline\SimpleRegionGrowingSegmentationTest.nhdr.md5;D:\S4\Modules\CLI\SimpleRegionGrowingSegmentation\Data\Baseline\SimpleRegionGrowingSegmentationTest.raw.gz.md5;D:\S4 \Modules\CLI\SimpleRegionGrowingSegmentation\Data\Input\MRHeadResampled.nhdr.md5;D:\S4\Modules\CLI\SimpleRegionGrowingSegmentation\Data\Input\MRHeadResampled.raw.gz.md5;D:\S4\Modules\CLI\S ubtractScalarVolumes\Data\Baseline\SubtractScalarVolumesTest.nhdr.md5;D:\S4\Modules\CLI\SubtractScalarVolumes\Data\Baseline\SubtractScalarVolumesTest.raw.gz.md5;D:\S4\Modules\CLI\SubtractS calarVolumes\Data\Input\CTHeadAxial.nhdr.md5;D:\S4\Modules\CLI\SubtractScalarVolumes\Data\Input\CTHeadAxial.raw.gz.md5;D:\S4\Modules\CLI\SubtractScalarVolumes\Data\Input\CTHeadAxialDoubled .nhdr.md5;D:\S4\Modules\CLI\SubtractScalarVolumes\Data\Input\CTHeadAxialDoubled.raw.gz.md5;D:\S4\Modules\CLI\TestGridTransformRegistration\Data\Input\CTHeadAxial.nhdr.md5;D:\S4\Modules\CLI \TestGridTransformRegistration\Data\Input\CTHeadAxial.raw.gz.md5;D:\S4\Modules\CLI\ThresholdScalarVolume\Data\Baseline\ThresholdScalarVolumeTest.nhdr.md5;D:\S4\Modules\CLI\ThresholdScalarV olume\Data\Baseline\ThresholdScalarVolumeTest.raw.gz.md5;D:\S4\Modules\CLI\ThresholdScalarVolume\Data\Input\CTHeadAxial.nhdr.md5;D:\S4\Modules\CLI\ThresholdScalarVolume\Data\Input\CTHeadAx ial.raw.gz.md5;D:\S4\Modules\CLI\VotingBinaryHoleFillingImageFilter\Data\Baseline\VotingBinaryHoleFillingImageFilterTest.nhdr.md5;D:\S4\Modules\CLI\VotingBinaryHoleFillingImageFilter\Data\ Baseline\VotingBinaryHoleFillingImageFilterTest.raw.gz.md5;D:\S4\Modules\CLI\VotingBinaryHoleFillingImageFilter\Data\Input\CTHeadResampledOtsuSegmented.nhdr.md5;D:\S4\Modules\CLI\VotingBin aryHoleFillingImageFilter\Data\Input\CTHeadResampledOtsuSegmented.raw.gz.md5;D:\S4R\Slicer-build\CMakeFiles\4a390c3a73f82eba1be75b2f4104c2cb\SlicerData.rule' exited with code 1. [D:\S4R\Slicer-build\SlicerData.vcxproj] [D:\S4R\Slicer.vcxproj]</code><br>
 →  it will remind you the download path from which the file was downloaded failed .<br>
At fisrt i tried to<br>
1. copy the download path to chrome, and found that it can downloaded successfully.<br>
2. copy the file to &lt;slice_build&gt;/ExternalData/Objects/MD5 manually.<br>
3.  And re-build again. Then the similar error message appeared again, but with a different download path. then i repeat from 1 to 3.<br>
I found it’s too slow because there are many files listed in this error message . The i try to find the rule. i found out that  this step is trying to download some files to your &lt;slice_build&gt;/ExternalData/Objects/MD5 from “<a href="https://github.com/Slicer/SlicerTestingData/releases/download/" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerTestingData/releases/download/</a>“subfix of the file”/“the content of the file””,  then i wirite a small program to anaysis the error message and do the download automatically.<br>
 → At last , i build succesfully.</li>
</ol>

---

## Post #5 by @pieper (2022-09-14 12:02 UTC)

<p>It’s great that you were able to get the build completed <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>The build should not have required so much manual effort though, and maybe someone can comment.  Perhaps these issues are a consequence of unstable network connections during the build?</p>

---

## Post #6 by @Gitty_Wang (2022-09-23 01:18 UTC)

<p>Yes, i agree, it may caused by the unstable network.</p>

---
