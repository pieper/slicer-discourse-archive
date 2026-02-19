---
topic_id: 23250
title: "Transformation Output Files"
date: 2022-05-03
url: https://discourse.slicer.org/t/23250
---

# Transformation output files

**Topic ID**: 23250
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/transformation-output-files/23250

---

## Post #1 by @Vinny (2022-05-03 01:10 UTC)

<p>Hi,</p>
<p>Slicer-4.13.0-2021-10-10-linux-amd64</p>
<p>I have a question regarding the format and content of the transformation matrix files outputted from the Slicer GUI versus the command-line.  When manually performing a rigid registration within the Slicer GUI, I export the transformation matrix in .txt format and see the following:</p>
<p><span class="hashtag">#Insight</span> Transform File V1.0<br>
<span class="hashtag">#Transform</span> 0<br>
Transform: AffineTransform_double_3_3<br>
Parameters: 0.9960614071380222 0.030830015314365793 -0.08313352732766315 -0.004910023279263162 0.9553428038834216 0.29545899671453507 0.08853002248740502 -0.2938871164646019 0.951731473628198 -4.0468819155405775 -27.4418351879466 -24.1487889338481<br>
FixedParameters: 0 0 0</p>
<p>I also ran the same registration in command-line:</p>
<p>Slicer --launch BRAINSFit --fixedVolume fixed_t1.nii --movingVolume moving_t1.nii --outputVolume moving-to-fixed_Slicer.nii.gz --transformType Rigid --linearTransform moving-to-fixed_Slicer.txt --initializeTransformMode useMomentsAlign</p>
<p>The moving-to-fixed_Slicer.nii.gz volume outputted from the CLI is the same as the one generated from the Slicer GUI, however, the content and format of the transformation matrix file from the CLI is different:</p>
<p><span class="hashtag">#Insight</span> Transform File V1.0<br>
<span class="hashtag">#Transform</span> 0<br>
Transform: VersorRigid3DTransform_double_3_3<br>
Parameters: -0.14915351589150105 -0.04344516579667238 -0.009045329415452575 -3.911482366131585 -27.683694094196184 -25.219819365762543<br>
FixedParameters: 3.4742684230541063 4.699249757355889 -0.05058095645894013</p>
<p>Is there a reason for this difference?  I’ve been able to use the transformation matrix manually outputted from the Slicer GUI for my workflow, and would like to automate the registration through the CLI. But I would like to have the same format as the transformation matrix manually exported from the GUI.  Any help would be greatly appreciated.</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @Vinny (2022-05-03 14:21 UTC)

<p>Hi,</p>
<p>When I run an affine registration between two images in the Slicer GUI vs CLI, the outputted images are again the same between the two, but the transformation matrices, although similar, are different enough to cause deviations when passing points through the transformations.  Is this known behaviour or is there something that is missing from the CLI command.  Here is the CLI command that I ran for the affine registration:</p>
<p>Slicer --launch BRAINSFit --fixedVolume fixed_t1.nii --movingVolume moving_t1.nii --outputVolume moving-to-fixed_SlicerCLI.nii.gz --transformType Affine --linearTransform affine_CLI.txt --initializeTransformMode useMomentsAlign</p>
<p>Here are the affine matrices from the GUI followed by CLI:</p>
<p>GUI:</p>
<p><span class="hashtag">#Insight</span> Transform File V1.0<br>
<span class="hashtag">#Transform</span> 0<br>
Transform: AffineTransform_double_3_3<br>
Parameters: 0.9969910985005138 0.0024328052157900973 0.07747793859880853 -0.02554949429826253 0.9539680535768614 0.2988179648144962 -0.07318451237688048 -0.29989837314256385 0.9511598146129817 0.5957013088022176 -9.779392222671147 11.091346021065451<br>
FixedParameters: 0 0 0</p>
<p>CLI:</p>
<p><span class="hashtag">#Insight</span> Transform File V1.0<br>
<span class="hashtag">#Transform</span> 0<br>
Transform: AffineTransform_double_3_3<br>
Parameters: 0.9970411608367628 0.0022748824367199395 0.07743524660162743 -0.025350088753046847 0.9539358953134315 0.2987708368963429 -0.07316750434063589 -0.2998711858884665 0.950949958153532 0.18483120190382518 -11.850099009857114 8.735680954429876<br>
FixedParameters: 1.7786384902690369 8.312981199696187 -5.499607555825423</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #3 by @mikebind (2022-05-03 15:21 UTC)

<p>Slicer uses an RAS coordinate system internally, whereas ITK (and much of the rest of the medical imaging world) has settled on using an LPS coordinate system.  Respecting this, exports from Slicer are automatically converted to use LPS, and imports from LPS are handled correctly.  However, when you compare the internal representation of a transformation in Slicer with the same transformation in some other program they will not match because of the change in coordinate system.</p>
<p>I know I’ve seen this come up many times in the forum, so if you are looking for more information, keep searching here.   Here is one related post I found:</p>
<aside class="quote" data-post="2" data-topic="18152">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/npy-transform-matrix/18152/2">Npy transform matrix</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer uses all data in LPS coordinate system in files (following conventions set by DICOM, ITK, and most other modern medical image computing software), while uses RAS in the scene (for backward compatibility). You need to apply LPS&lt;-&gt;RAS basis transform if you import an LPS transform as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms">here</a>. You also need to be aware of the transform direction (modeling/resampling; from/to parent).
  </blockquote>
</aside>


---

## Post #4 by @Vinny (2022-05-03 16:02 UTC)

<p>Thanks, I am aware of that particular script and have implemented it in my workflow.  I found that I had to change the following line from:</p>
<p>ras2lps = np.diag([-1, -1, 1, 1])</p>
<p>to</p>
<p>ras2lps = np.diag([1, 1, -1, 1])</p>
<p>in order to get the same transformation as in the Slicer GUI.</p>
<p>Here is the transformation in Slicer GUI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad327a792399b4157d007a1b4182c5b409da563b.png" data-download-href="/uploads/short-url/oIaKCf5zjx2zQGnbNpRmBW8jwZd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad327a792399b4157d007a1b4182c5b409da563b_2_569x500.png" alt="image" data-base62-sha1="oIaKCf5zjx2zQGnbNpRmBW8jwZd" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad327a792399b4157d007a1b4182c5b409da563b_2_569x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad327a792399b4157d007a1b4182c5b409da563b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad327a792399b4157d007a1b4182c5b409da563b.png 2x" data-dominant-color="E8E9EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">668×586 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I had employed the above script, I got the following output where the absolute values were similar (not exactly the same) but not the signs (+/-).  See below screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246e58cc65d64bc853967371ee3cbc956c2e8866.png" data-download-href="/uploads/short-url/5chBzvIgoUcaQTXbEjU5qAcn3QW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e58cc65d64bc853967371ee3cbc956c2e8866_2_690x361.png" alt="image" data-base62-sha1="5chBzvIgoUcaQTXbEjU5qAcn3QW" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e58cc65d64bc853967371ee3cbc956c2e8866_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e58cc65d64bc853967371ee3cbc956c2e8866_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246e58cc65d64bc853967371ee3cbc956c2e8866.png 2x" data-dominant-color="222526"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×646 88.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After making the above change in the np.diag, I get the following output, which matches more closely with what’s reported in the Slicer GUI (still slight variation in the values):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82058869b0e8477f9b67ef307f62a4c7023639f3.png" data-download-href="/uploads/short-url/iydVmHRm5TJYVZBUJeEcLLAy2Az.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82058869b0e8477f9b67ef307f62a4c7023639f3_2_690x369.png" alt="image" data-base62-sha1="iydVmHRm5TJYVZBUJeEcLLAy2Az" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82058869b0e8477f9b67ef307f62a4c7023639f3_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82058869b0e8477f9b67ef307f62a4c7023639f3_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82058869b0e8477f9b67ef307f62a4c7023639f3.png 2x" data-dominant-color="222525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1239×664 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the issue is I have ac and pc points given to me in voxel coordinates (from the original T1 image).  I used nibabel to convert to physical coordinates.  I’d like to bring these points into ac-pc space.  I can do this relatively easy using the Slicer GUI.  I’m running into problems when using the Slicer command line.</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #5 by @lassoan (2022-05-03 23:01 UTC)

<p>The example conversion Python script in the script repository was incorrect. I don’t know where it has come from; it did something completely different than the C++ implementation and unsurprisingly, it did not compute correct results. I’ve replaced it now by a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms">correct script</a>.</p>

---

## Post #6 by @Vinny (2022-05-05 13:58 UTC)

<p>Thank you Andras, the revision works great.</p>

---
