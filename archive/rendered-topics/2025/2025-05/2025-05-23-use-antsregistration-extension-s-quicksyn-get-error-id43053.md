# Use ANTsRegistration Extension 's QuickSyN get error

**Topic ID**: 43053
**Date**: 2025-05-23
**URL**: https://discourse.slicer.org/t/use-antsregistration-extension-s-quicksyn-get-error/43053

---

## Post #1 by @zhaokaien (2025-05-23 05:21 UTC)

<p>Hello,</p>
<p>I’m trying to register two volumes using the <strong>AntsRegistration</strong> plugin. I’ve had no issues when using the <strong>Rigid</strong> and <strong>Affine+Rigid</strong> modes in ANTs. However, I consistently encounter an error when attempting to use <strong>QuickSyN</strong>. The error message is as follows:<br>
"<br>
WARNING: In C:\D\P\S-0-build\ITK\Modules\Core\Common\include\itkImageBase.hxx, line 87</p>
<p>Image (000001CB03ED4C70): Negative spacing is not supported and may result in undefined behavior.</p>
<p>Proceeding to set spacing to [-inf, 0.0358951]</p>
<p>C:\D\P\S-0-build\ITK\Modules\ThirdParty\VNL\src\vxl\core\vnl/algo/vnl_svd.hxx: suspicious return value (2) from SVDC</p>
<p>C:\D\P\S-0-build\ITK\Modules\ThirdParty\VNL\src\vxl\core\vnl/algo/vnl_svd.hxx: M is 2x2</p>
<p>M = [ …</p>
<p>-inf 0</p>
<p>-nan(ind) 0.0358951193547 ]<br>
"</p>
<p>I’ve spent a considerable amount of time trying to resolve this, including adjusting <strong>convergence parameters</strong> and <strong>shrink factor parameters</strong>, but I haven’t been able to get past it. I suspect I might be doing something incorrectly, but I’m completely stuck.</p>
<p>Could anyone please offer some assistance?</p>

---

## Post #2 by @muratmaga (2025-05-23 05:29 UTC)

<aside class="quote no-group" data-username="zhaokaien" data-post="1" data-topic="43053">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/zhaokaien/48/80265_2.png" class="avatar"> zhaokaien:</div>
<blockquote>
<p>Could anyone please offer some assistance?</p>
</blockquote>
</aside>
<p>What are the spacing of your input images (both reference and moving)? The error is related to a nonsensical spacing. Also I am also seeing two dimensions? Are these 2D images you are trying to register?</p>

---

## Post #3 by @zhaokaien (2025-05-23 06:53 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43053">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>ur input images (both reference and moving)? The error is related to a nonsensical spacing. Also I am also seeing two dimensions? Are these 2D images you are trying to register?</p>
</blockquote>
</aside>
<p>thank you for your replying, the fixed image and the moving image 's spaces are 0.1852mm and 0.1774mm</p>
<p>the full command is<br>
[VTK] E:/D/SR/Slicer-build/slicer.org/Extensions-33563/SlicerANTs/lib/Slicer-5.9/cli-modules/antsRegistrationCLI.exe --antsCommand --dimensionality 3 --use-histogram-matching 0 --winsorize-image-intensities [0.005,0.995] --float $useFloat --verbose 1 --interpolation Linear --output [$outputBase,$outputVolume] --write-composite-transform 1 --collapse-output-transforms 1 --transform Rigid[0.1] --metric MI[$inputVolume01,$inputVolume02,1,32,Regular,0.25] --convergence [1000x500x250x1,1e-6,10] --smoothing-sigmas 4x3x2x1vox --shrink-factors 12x8x4x2 --transform Affine[0.1] --metric MI[$inputVolume01,$inputVolume02,1,32,Regular,0.25] --convergence [1000x500x250x0,1e-6,10] --smoothing-sigmas 4x3x2x1vox --shrink-factors 12x8x4x2 --transform SyN[0.1,3,0] --metric MI[$inputVolume01,$inputVolume02,1,32,Regular,0.25] --convergence [100x100x70x50x0,1e-6,10] --smoothing-sigmas 5x3x2x1x0vox --shrink-factors 10x6x4x2x1 --inputVolume01 C:/Users/Administrator/AppData/Local/Temp/Slicer/BDDHG_vtkMRMLScalarVolumeNodeB.nrrd --inputVolume02 C:/Users/Administrator/AppData/Local/Temp/Slicer/BDDHG_vtkMRMLScalarVolumeNodeC.nrrd --outputVolume C:/Users/Administrator/AppData/Local/Temp/Slicer/BDDHG_vtkMRMLScalarVolumeNodeD.nrrd --outputCompositeTransform C:/Users/Administrator/AppData/Local/Temp/Slicer/BDDHG_vtkMRMLTransformNodeBComposite.h5 --useFloat</p>
<p>[VTK] Zero-valued spacing is not supported and may result in undefined behavior.</p>
<p>[VTK] Refusing to change spacing from [1, 1] to [0.0358338, 0]</p>
<p>[VTK]</p>
<p>[VTK]</p>
<p>[VTK] antsRegistrationCLI completed with errors</p>

---

## Post #4 by @muratmaga (2025-05-23 15:02 UTC)

<p>Given that these looks like 2D images, you will probably better of trying to run the registration directly from ANTs (e.g., ANTsPy), instead of Slicer. I don’t think if anybody tested antsRegistration implementation in Slicer with 2D data (since we all work with 3D).</p>

---

## Post #5 by @zhaokaien (2025-05-30 02:06 UTC)

<p>Hello, I’m not using 2D images. I’m working with 3D data. Specifically, the two volumes I’m using for registration were converted from models into labelmap binary volumes.</p>

---

## Post #6 by @muratmaga (2025-05-30 02:44 UTC)

<p>Your log shows only two dimensions. So I would double check your data. There is something wrong there…</p>
<aside class="quote no-group" data-username="zhaokaien" data-post="3" data-topic="43053">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/zhaokaien/48/80265_2.png" class="avatar"> zhaokaien:</div>
<blockquote>
<p>change spacing from [1, 1] to [0.0358338, 0]</p>
</blockquote>
</aside>

---

## Post #7 by @zhaokaien (2025-06-02 02:53 UTC)

<p>Thank you for your replying！</p>

---
