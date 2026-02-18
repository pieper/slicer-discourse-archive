# Nrrd vs nii regarding affine data and transforms

**Topic ID**: 1896
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/nrrd-vs-nii-regarding-affine-data-and-transforms/1896

---

## Post #1 by @NaglisR (2018-01-22 14:05 UTC)

<p>Hi everyone,</p>
<p>I’ve noticed that after preforming brain registration task, if I save the resulting output file (after transform hardening) as a nrrd file and afterwards load the saved file to slicer, the loaded file is transformed and looks as it did before saving as I would expect. But if I try to save the registered output file as a .nii format, (which I need for further processing) after loading the nii file back to slicer I can see that the affine data doesn’t match with the one that I was saving. Are there any differences with affine data saving for nrrd and nii formats?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2018-01-22 14:41 UTC)

<p>Can you provide a specific example with the steps to reproduce the issue?  As far as Slicer is concerned nrrd and nii should save and reload the same (we prefer nrrd because nii has a history of different software interpreting the standard differently).</p>

---

## Post #3 by @NaglisR (2018-01-22 14:51 UTC)

<p>Sure:<br>
I am performing CT to MRI registration task. I am using BRAINS registration module. I set the MRI volume to be fixed, CT - moving. After registration is done, I check if it looks ok. Then I harden the transforms and save the transformed CT volume. If I save it as nrrd and load it again to the scene with the used MRI volume - everything is fine. If I save it as nii, when I load it to slicer with the used MRI volume, they don’t fit.</p>

---

## Post #4 by @pieper (2018-01-22 16:31 UTC)

<p>Interesting - yes, I can reproduce that, thanks for pointing it out.  Hardening the transform is applying the affine (possibly shear) matrix to the slice directions and it seems that’s preserved in the nrrd header but the directions are orthogonalized in the nii version.</p>
<p>The workaround for this case would be to resample the images before saving (e.g. with BRAINS Resample choosing a reference with orthogonal directions).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> and others: what do you think of enforcing orthogonality of the IJKToRAS directions?</p>
<p>It would mean, for example, resampling when applying a linear transform with shear  E.g. here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4e0a67e33b9334d57f42f65da58a7a40615bcba1/Libs/MRML/Core/vtkMRMLVolumeNode.cxx#L989-L1001" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4e0a67e33b9334d57f42f65da58a7a40615bcba1/Libs/MRML/Core/vtkMRMLVolumeNode.cxx#L989-L1001" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/4e0a67e33b9334d57f42f65da58a7a40615bcba1/Libs/MRML/Core/vtkMRMLVolumeNode.cxx#L989-L1001</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="989" style="counter-reset: li-counter 988 ;">
<li>void vtkMRMLVolumeNode::ApplyTransform(vtkAbstractTransform* transform)</li>
<li>{</li>
<li>vtkHomogeneousTransform* linearTransform = vtkHomogeneousTransform::SafeDownCast(transform);</li>
<li>if (linearTransform)</li>
<li>  {</li>
<li>  this-&gt;ApplyTransformMatrix(linearTransform-&gt;GetMatrix());</li>
<li>  }</li>
<li>else</li>
<li>  {</li>
<li>  this-&gt;ApplyNonLinearTransform(transform);</li>
<li>  }</li>
<li>return;</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2018-01-22 18:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>resampling when applying a linear transform with shear</p>
</blockquote>
</aside>
<p>It’s a good idea, I’ve added a ticket to track this idea: <a href="https://issues.slicer.org/view.php?id=4499" class="inline-onebox">Apply linear transform with shear as non-linear transform · Issue #4499 · Slicer/Slicer · GitHub</a>.</p>
<p>Note that ApplyNonLinearTransform would need some improvements, as currently it resamples the image on the grid of the original volume, so the output may be heavily cropped (<a href="https://issues.slicer.org/view.php?id=4433" class="inline-onebox">Harden non-linear transform may clip volume · Issue #4433 · Slicer/Slicer · GitHub</a>).</p>

---

## Post #6 by @gcsharp (2018-01-22 18:56 UTC)

<p>If I understand the proposal correctly, I vote against.  This is an issue with a specific (and arguably obsolete) file format.  Resampling is a lossy operation.</p>
<p>Both NIFTI-1 and NIFTI-2 support affine transforms.  Would there be a problem if we export using that option?</p>

---

## Post #7 by @lassoan (2018-01-22 19:28 UTC)

<p>It is not just about how to save the file. There are many other places in the Slicer and its dependencies where image axes are assumed to be orthogonal.</p>
<p>For example, image data axes must be orthogonal in VTK and ITK. In VTK, you cannot even store image direction in vtkImageData (just origin and spacing). In ITK, “columns of the Direction matrix are expected to form an orthogonal right handed coordinate system. But this is not checked nor enforced in itk::ImageBase” (<a href="https://itk.org/Doxygen/html/classitk_1_1ImageBase.html#a23ebc76de3b60bb1eeabf66cd4dabc48">source</a>).</p>

---

## Post #8 by @gcsharp (2018-01-22 20:55 UTC)

<p>I guess I’m still not convinced.  Sure, there are some poorly behaved algorithms which would benefit from resampling to orthogonal.  But if I understand correctly, this proposal would exclude the option for lossless computation by well-behaved algorithms.</p>

---

## Post #9 by @pieper (2018-01-22 23:35 UTC)

<p>The slicer volume node design allows non-orthogonal directions but they never really happened much.  Hardening a shear transform is the first user-level case I can think of where this has come up, and difference in output that <a class="mention" href="/u/naglisr">@NaglisR</a> reported is a valid concern.</p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> perhaps well behaved algorithms should accept transforms (linear or nonlinear) instead of expecting it to be in the direction cosines?  The in-between case where algorithms don’t accept nonlinear transforms but do accept non-orthogonal directions is pretty rare (even handling orientation at all is pretty rare).</p>

---

## Post #10 by @lassoan (2018-01-23 01:13 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="8" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>I guess I’m still not convinced.  Sure, there are some poorly behaved algorithms which would benefit from resampling to orthogonal.</p>
</blockquote>
</aside>
<p>It’s more about convincing ITK and VTK algorithm developers. Even just oriented image data is a hard sell sometimes, as it makes many algorithms more complicated and sometimes slightly slower. That’s why VTK still does not support oriented image data - but we’ll try to change this.</p>
<p>However, making algorithm work correctly on images with non-orthogonal axes is a different story. It is often much more difficult (and probably not always feasible) to change algorithms to work directly on images with non-orthogonal axes. As the cost is high and the benefit is relatively low (as we have a quite good workaround of treating shearing transforms as non-linear transforms), direct processing of sheared images will probably not be generally supported in ITK, VTK, or in applications that are built on these toolkits.</p>

---

## Post #11 by @NaglisR (2018-01-23 10:16 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> “This is an issue with a specific (and arguably obsolete) file format.” Which format is obsolete in this case? .nii is used way more widely than nrrd in my opinion. Thanks everyone for your feedback.</p>

---

## Post #12 by @lassoan (2018-01-23 12:43 UTC)

<aside class="quote no-group" data-username="NaglisR" data-post="11" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/naglisr/48/16280_2.png" class="avatar"> NaglisR:</div>
<blockquote>
<p>.nii is used way more widely</p>
</blockquote>
</aside>
<p>I see .nii used extensively in neuroimaging community, but not much elsewhere. Nifti has important neuroimaging-specific features, but suffers from several problems, for example:</p>
<ul>
<li>there seems to be a confusion around axis orientations (different variants may use different conventions)</li>
<li>storage of multidimensional (4D, 5D, …) is limited</li>
<li>header is not user-readable, it is difficult to read/write without a parsing library (non-user-readable binary header has some advantages, too, but most often flexibility and ease of use is more important than storage efficiency or completely lossless encoding of numerical values)</li>
<li>no built-in support for compression (you can only zip the entire file, losing its original file extension, lossy compression cannot be supported this way)</li>
<li>ITK reader ignores patient orientation tag</li>
</ul>
<p>NRRD format has none of these limitations. I don’t use nifty, so maybe not all of these limitations are true anymore or there may be workarounds, but overall nifti is the file format of choice for neuroimaging but does not seem to be an ideal file format for general research use.</p>

---

## Post #13 by @hbraunDSP (2020-02-24 17:42 UTC)

<p>Sorry to resurrect this thread. My lab just ran into this issue, leading to some significant re-work of slightly mis-registered Nifti files.  I would strongly suggest at least warning the user when this occurs. It is completely reasonable for a user to assume that if they harden a transform and then save, the saved file will accurately reflect the whole transform, including any shear.  In fact, this is the case when saving as NRRD.</p>
<p>I believe the NIFTI header is fully capable of storing general affine transforms, including shear.  This is necessary with, for example, CTs acquired with a tilted gantry.  Why does the Nifti writer orthogonalize the transform matrix when saving?</p>

---

## Post #14 by @pieper (2020-02-24 18:06 UTC)

<aside class="quote no-group" data-username="hbraunDSP" data-post="13" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hbraundsp/48/4574_2.png" class="avatar"> hbraunDSP:</div>
<blockquote>
<p>I would strongly suggest at least warning the user when this occurs.</p>
</blockquote>
</aside>
<p>Where would you want the warning - maybe when you select an output format (say nii, but could be others) we should have a pre-save step where it inspects the data and reports if the save operation will be lossy.</p>
<aside class="quote no-group" data-username="hbraunDSP" data-post="13" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hbraundsp/48/4574_2.png" class="avatar"> hbraunDSP:</div>
<blockquote>
<p>Why does the Nifti writer orthogonalize the transform matrix when saving?</p>
</blockquote>
</aside>
<p>I believe this is because ITK images need to have orthogonal direction vectors and we cast the vtkImageData to itk::Image <a href="https://github.com/Slicer/Slicer/blob/c0fd88e77c61b5abeb2b787ded6eede1855990fb/Libs/vtkITK/vtkITKImageWriter.cxx#L304-L519">as part of the save process</a>.</p>

---

## Post #15 by @hbraunDSP (2020-02-24 22:27 UTC)

<p>I think a warning when saving a non-orthogonal volume to Nifti would be appropriate, either when selecting “nii” or “nii.gz” from the list, or when clicking “save”.</p>
<p>Do you know of a way to convert from NRRD (or another format that Slicer handles better than Nifti) to Nifti while preserving the full affine spatial orientation information, including any shear?</p>

---

## Post #16 by @pieper (2020-02-24 23:30 UTC)

<aside class="quote no-group" data-username="hbraunDSP" data-post="15" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hbraundsp/48/4574_2.png" class="avatar"> hbraunDSP:</div>
<blockquote>
<p>I think a warning when saving a non-orthogonal volume to Nifti would be appropriate, either when selecting “nii” or “nii.gz” from the list, or when clicking “save”.</p>
</blockquote>
</aside>
<p>Agreed, a warning would be good.  It would require a bit of effort, so if someone wants to volunteer to work on it and test it out then probably several of us could suggest ways to implement that.  There are lots of other examples of potentially lossy file formats, like saving models to STL.</p>
<aside class="quote no-group" data-username="hbraunDSP" data-post="15" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hbraundsp/48/4574_2.png" class="avatar"> hbraunDSP:</div>
<blockquote>
<p>Do you know of a way to convert from NRRD (or another format that Slicer handles better than Nifti) to Nifti while preserving the full affine spatial orientation information, including any shear?</p>
</blockquote>
</aside>
<p>To answer your specific question, perhaps you could use <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>, which has recently added nrrd conversion options.  <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> may have additional suggestions.</p>
<p>Also, standard warning, nifi format has several ways of encoding orientation (qform and sform modes) and it’s never clear to me which methods any particular tool will or won’t support, so you may run into other software that trips up on shear transforms.  At least for Slicer we defer to ITK’s implementation in the hopes that it will do things right as often as possible, but clearly that approach didn’t work for this particular case.  I’d think other common tools (maybe ITK-snap?) would also have trouble with sheared orientation info.  It would be interesting to hear if people know what the general support is for this feature of nifti.</p>

---

## Post #17 by @lassoan (2020-02-25 04:13 UTC)

<p>This silent orthogonalization of image axes in the image writer should be probably fixed in ITK. I’ve asked about this on the ITK forum: <a href="https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760">https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760</a>.</p>

---

## Post #18 by @Chris_Rorden (2020-02-27 20:26 UTC)

<p><a class="mention" href="/u/hbraundsp">@hbraunDSP</a> the <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h" rel="nofollow noopener">NIfTI header</a> contains two spatial transforms- the quaternion-based QForm and the Matrix-based SForm. It is worth noting that Quaternions can not store shears, so it is worth thinking of them as a 9-degree of freedom transform (translation, rotation, zoom in each of 3 dimensions). On the other hand, the Matrix can store shears and is 12 DoF (translation, rotation, zoom and shear). By design, the QForm was designed for the scanner native space, with the SForm initially identical to the QForm but capable of having a 12-DoF coregistration applied.</p>
<p>This has proved problematic in two ways. First, CT scans are often acquired with shear (gantry tilt). Second, ITK does not allow volumes to have shears, and therefore ITK based tools give precedence to the QForm and if the QForm is not set will orthogonalized the SForm. This is different from other tools, that give precedence to the SForm. Historically, this has caused a lot of issues, e.g. SPM gives precedence to SForm and ANTs gives precedence to QForm, so one tool has vastly different starting estimate to the other.</p>
<p>This explains one bizarre aspect of my dcm2niix tool. In most cases, it goes to great lengths to not interpolate the data, but it will interpolate to <a href="https://github.com/rordenlab/dcm2niix/issues/253" rel="nofollow noopener">remove shear</a>.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> correctly details many of the weaknesses of NIfTI. I have no dog in this fight, but I do think there are tradeoffs, and the popularity of this format reflects Darwinian selection. In defense of NIfTI I would argue:</p>
<ol>
<li>It is very simple and explicit. This makes it very easy for scientists to access the data rapidly and with minimal code.</li>
<li>In general, the spatial transforms are very clear, and it does allow shears. One could argue that ITK simply does not support the NIfTI format as defined. This is a limitation in ITK, not the NIfTI format. NRRD does not resolve this issue either. The core issue is that ITK requires volumes to not have shear.</li>
<li>The while file compression is not an issue, as the header fits in the first 352 bytes. Therefore, you can rapidly extract the first 352 bytes to read the header. From my perspective, this is superior to NRRD compression that uses text at the start that prevents people from using high performance compression and decompression algorithms.</li>
<li>The header is simple and explicit, so there are great tools for reading them (fslhd, 3dinfo, etc), and it is simple to write your own in your favorite language.</li>
<li>Not sure exactly what is meant by ITK ignoring patient orientation, but again this is a weakness of ITK not the format.</li>
<li>I agree that storage of multidimensional data is limited, but this also makes it very easy to make strong assumptions regarding the data across all volumes stored in the 7 dimensions. This makes writing analysis and processing tools much simpler as the input is necessarily constrained, e.g. one knows from the outset that all volumes have consistent resolution.</li>
</ol>
<p>Its nice to have different formats that each fit a niche. While NIfTI is far less flexible than DICOM, it also avoids the <a href="https://github.com/jonclayden/divest" rel="nofollow noopener">complication</a>. Seen from the perspective of DICOM, NRRD and NIfTI are very similar. They have slightly different niches, but are typically used in the same role. So while some advocate medical imaging should rely on a <a href="http://qiicr.org/dicom4miccai/dicom4miccai2017.html" rel="nofollow noopener">single format</a> my sense is one should choose the best tool for the job.</p>
<p>I am not sure whether <a class="mention" href="/u/gcsharp">@gcsharp</a> is referring to NRRD or NIfTI as obsolete. In my field, NIfTI is far more widely used (SPM, FSL, AFNI, BIDS). NRRD is convenient since you can create a header with a text editor, but beyond the basic tags there seems to be no consensus on how to store a lot of meta information. They are far more similar than different.</p>

---

## Post #19 by @lassoan (2020-02-28 02:47 UTC)

<p>There is a large gap between simplest NRRD and hyper-complex DICOM, which domain-specific file formats, such as Nifti can fill. The main problem with Nifti is that it is so poorly specified (or the community misuses/misinterprets so often for some other reasons) that it is really hard to write software that can use it “correctly”.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="18" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>In defense of NIfTI I would argue:</p>
<ol>
<li>It is very simple and explicit</li>
</ol>
</blockquote>
</aside>
<p>Not for everybody. After reading the specification, I was still not sure what the role of qform and sform transforms are. Discussion in the related <a href="https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760/12?u=lassoan">ITK forum topic</a> shows that regular users of Nifti and core ITK developers are uncertain, too.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="18" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>One could argue that ITK simply does not support the NIfTI format as defined</p>
</blockquote>
</aside>
<p>If you know what the correct behavior would be for ITK, it would be great if you could describe it in this <a href="https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760/12?u=lassoan">ITK forum topic</a>.</p>

---

## Post #20 by @Chris_Rorden (2020-02-28 16:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> often the SForm and QForm are the same. A good approach would be to use whichever has the larger <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h" rel="nofollow noopener">NIFTI1_XFORM_CODE</a>, and use the SForm if they are tied. In general, I would only expect these to differ if the acquired data could not reported in the QForm (e.g. CT scan with shear) or if the user coregistered the image so that the raw transform is still in the QForm and the subsequent coregistration uses the SForm. I am pretty sure recent releases of SPM and FSL attempt to set both the QForm and SForm to the same value (to the extent possible) to reduce issues with ITK based tools like ANTs. In this way, modern versions of SPM sacrifice the benefit of two representations (patient space and standard space) in order to ensure ITK compatibility.</p>
<p>In the interest of full disclosure, before the NIfTI format was finalized I explicitly criticized the inclusion of these two spatial mappings. The desire for backward compatibility with the Analyze format made it hard to store two matrices (as they would not fit in the header). The QForm was seen as sufficient for raw MRI and the SForm allowed 12-DoF coregistration without reslicing the data. It does mean that every tool that wants to support this format needs to support these two ways of representing space, e.g. <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1_io.c" rel="nofollow noopener">nifti_quatern_to_mat44 / nifti_mat44_to_quatern</a>. So not only do I feel your pain, but part of me feels that this was an issue that was vocally identified prior to the format being finalized. I feel very similar to the BIDS format, where I also raised concerns. In any democratic discussion of a format one will always feel there was a compromise. However, this niggling issue is small compared to the overall benefits for these unified formats.</p>
<p>I did contact the ITK team about a decade ago about adapting code to behave similar to other tools. I think there was a concern regarding unintended consequences of tools that assumed ITK volumes always have orthogonal dimensions. As I understand it, ITK can not abide by non-rectangular volumes, so while the SForm in NIfTI is particularly clumsy for ITK.</p>
<p>To be clear, this is an limitation with ITK not NIfTI. One could just as easily create a <a href="http://teem.sourceforge.net/nrrd/format.html" rel="nofollow noopener">NRRD</a> header where <code>space directions</code> defines a shear and ITK will treat the volume as rectangular.  Likewise, there are many DICOM CT scans with shear.</p>
<p>Further, while NIfTI is complicated by having both quaternion and matrix representations, the NRRD format is complicated because it allows the user to specify the frame of reference. This makes it really easy to write a NRRD header, as you can use the same frame of reference as the source data (e.g. <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Spatial_Coordinates" rel="nofollow noopener">NIfTI LAS or DICOM RPS</a>). However, a fully compliant NRRD reader must handle all the possible transforms. Form my perspective, NIfTI headers are trickier to write than NRRD, but they are easier to read.</p>
<p>As an aside, matrices tend to be very familiar to developers, as they are useful for so many problems (e.g. GLM statistics). They seem like a natural way to represent space in a manner that is intuitive. Therefore, I think I was not alone when I had an initial distaste for the alien quaternions. However, they do have some remarkable properties. They allow us to interpolate between two orientations gracefully and provide a nice way to avoid gimbal lock. In addition, the inability to store shear can actually be an asset, as it avoids rounding errors from accidentally inducing shears. Therefore, I certainly appreciate quaternions, but I maintain that including both matrices and quaternions into an otherwise simple format has had repercussions.</p>
<p>I do not think NIfTI is poorly specified. I think the ITK developers made an explicit decision to use the representation they could fully encode. This was a different choice than other tools. Nowadays most tools attempt to store the same value in the Q and S Form (to the fullest extent possible). Beyond this one issue, the format is remarkably simple helping developers focus on the unique processing of their tools with simple and efficient I/O routines for interchange.</p>

---

## Post #21 by @lassoan (2020-02-28 17:40 UTC)

<p>Thanks for the detailed response.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="20" data-topic="1896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>To be clear, this is an limitation with ITK not NIfTI. One could just as easily create a <a href="http://teem.sourceforge.net/nrrd/format.html">NRRD</a> header where <code>space directions</code> defines a shear and ITK will treat the volume as rectangular</p>
</blockquote>
</aside>
<p>ITK states that it is allowed to store sheared volumes in itk image data objects (<a href="https://itk.org/Doxygen/html/classitk_1_1ImageBase.html#a23ebc76de3b60bb1eeabf66cd4dabc48">source</a>). I’ve tested current ITK behavior now and found the followings:</p>
<ul>
<li>ITK can <em>read</em> sheared volumes - direction matrix contain shear - from mha and nrrd formats (could not test others, as I could not modify headers to introduce shear)</li>
<li>ITK orthogonalizes direction matrix when writing images in all formats I tested (mha, nrrd, nifti, mgz, mnc)</li>
</ul>
<p>So, there is definitely fundamental inconsistency within ITK between reading and writing files.</p>
<p>A short-term solution could be that we refuse writing volumes with non-orthogonal axes in Slicer. That way we could avoid accidental data corruption. The difficulty is reliable detection of non-orthogonal axes without false alarms.</p>

---

## Post #22 by @gcsharp (2020-03-12 17:19 UTC)

<p>I consider the version of the NIfTI implemented in ITK that does not support affine to be obsolete.  I do not consider NIfTI v1 and NIfTI v2 obsolete!</p>

---

## Post #23 by @Research5 (2021-02-25 05:27 UTC)

<p>My research group encountered the same issue. Was there a resolution to either executing the conversion of Nrrd to Nii while taking into account the orthogonal considerations or completing a step beforehand to account for the differences?</p>

---

## Post #24 by @lassoan (2021-02-25 05:52 UTC)

<p>Until ITK does not support writing of non-orthogonal axes, probably the best is to resample the volume on a rectilinear grid using one of the image resample modules. For example, you can use “Crop volume module”; or use “Resample scalar/vector/dwi volume” module and set “Manual output parameters”.</p>

---
