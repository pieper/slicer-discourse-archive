# Z-axis and intensities change from Slicer to fsleyes

**Topic ID**: 9513
**Date**: 2019-12-16
**URL**: https://discourse.slicer.org/t/z-axis-and-intensities-change-from-slicer-to-fsleyes/9513

---

## Post #1 by @Tommaso_Di_Noto (2019-12-16 10:15 UTC)

<p>Hi everyone!</p>
<p>Small doubt. I have a DICOM series of a T1 scan. I converted this sequence to nifti with “dcm2niix” from command line and now when I overlap both the original T1 dcm and the T1.nii on Slicer I noticed two weird things:</p>
<ol>
<li>
<p>the intensities were rescaled. More specifically, when hovering over the two superimposed volumes with the mouse, the nifti stack has intensities which are from 2-fold up to 10-fold bigger than the original dicom stack.</p>
</li>
<li>
<p>the z-axis is inverted: while the z-axis value increases for the dcm (e.g. from inferior to superior), it decreases for the nifti (and vice-versa).</p>
</li>
</ol>
<p>I though this was somehow related to the dcm2niix conversion, but then I tried opening the two same stacks (dcm and nii) in fsleyes and the two issues don’t happen (i.e. the intensities are the same and the z-axes are non inverted).</p>
<p>Why does this happen? Did I do something wrong?</p>
<p>Thank you very much in advance! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2019-12-16 15:46 UTC)

<p>Which dcm2niix version do you use? Can you share an example data set or at least printout of the header?</p>
<p>Does the image load correctly if you load it with DICOM module? (you can import a DICOM series by drag-and-dropping the file folder to the Slicer application window)</p>
<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Do you have any ideas or suggestions how this issue could be investigated?</p>

---

## Post #3 by @Tommaso_Di_Noto (2019-12-16 17:26 UTC)

<p>Dear Andras,</p>
<p>Thanks for the quick reply. I used dcm2niiX version v1.0.20181125</p>
<p>Here are the dcm and the nifti anonymized.</p>
<p><a href="https://drive.google.com/drive/folders/1iKYJqgEpzJqXr-a9PMJ-I-nCJvTxCafw?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1iKYJqgEpzJqXr-a9PMJ-I-nCJvTxCafw?usp=sharing</a></p>
<p>I think the dicom volume loads correctly because then the two volumes look the same. However, the loading bar only reaches 91% (see image)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcd2a7a73f215dd1bc25fb0ad6e0f979efec065.png" data-download-href="/uploads/short-url/vE95oeplu9BAamGjtBaYcPk1b1z.png?dl=1" title="loading_bar" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddcd2a7a73f215dd1bc25fb0ad6e0f979efec065_2_690x345.png" alt="loading_bar" data-base62-sha1="vE95oeplu9BAamGjtBaYcPk1b1z" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddcd2a7a73f215dd1bc25fb0ad6e0f979efec065_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcd2a7a73f215dd1bc25fb0ad6e0f979efec065.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcd2a7a73f215dd1bc25fb0ad6e0f979efec065.png 2x" data-dominant-color="BEC3C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">loading_bar</span><span class="informations">723×362 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> . I don’t know if this is just a graphical thing. When I click OK, then the loading bar disappears, as expected.</p>

---

## Post #4 by @lassoan (2019-12-16 20:28 UTC)

<p>Thanks, the example data was very useful.<br>
First of all, the DICOM files contained double-precision floating-point voxels. This is highly unusual for MRI volumes. What software generated this DICOM series?</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="3" data-topic="9513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>I used dcm2niiX version v1.0.20181125</p>
</blockquote>
</aside>
<p>This is a rather old version. You may try with latest dcm2niix.</p>
<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Could you check if rescaling of image intensities is correct? Both Slicer and ITK-Snap reports image intensities about 5x lower, so there seems to be an inconsistency between ITK and dcm2niix.</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="3" data-topic="9513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>I think the dicom volume loads correctly because then the two volumes look the same. However, the loading bar only reaches 91% (see image)</p>
</blockquote>
</aside>
<p>Yes, it looks like a GUI glitch. Please try latest Slicer Preview Release.</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="1" data-topic="9513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>z-axis is inverted: while the z-axis value increases for the dcm (e.g. from inferior to superior), it decreases for the nifti (and vice-versa).</p>
</blockquote>
</aside>
<p>I don’t see any issues with image geometry. Images appear the same way. Voxel IJK coordinates are application-specific: it is valid to map a voxel coordinate system axis to any patient coordinate system (LPS, RAS, …) axis and direction.</p>

---

## Post #5 by @pieper (2019-12-16 20:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>First of all, the DICOM files contained double-precision floating-point voxels. This is highly unusual for MRI volumes. What software generated this DICOM series?</p>
</blockquote>
</aside>
<p>Floating point pixel data is not valid for MRI.  As far as I know only the new DICOM Parametric Map type allows that.</p>

---

## Post #6 by @lassoan (2019-12-16 22:08 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="9513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Floating point pixel data is not valid for MRI</p>
</blockquote>
</aside>
<p>The double values might have come from a real-world value mapping lookup table. Do you know if that can be valid?</p>

---

## Post #7 by @pieper (2019-12-16 22:28 UTC)

<p>I see - it’s because of this:</p>
<p><code>RescaleSlope : "4.65714285714285"</code></p>
<p>So the pixel data itself in the dicom file is unsigned short, but the result of reading it should be float.  That’s fine, but yes, unusual for MRI.</p>

---

## Post #8 by @Chris_Rorden (2019-12-17 01:35 UTC)

<p>DICOM images tend like this one store each voxel as a 16-bit integer. This is usually converted into a floating point value using the public tags rescale intercept (0028,1052) and rescale slope (0028,1053). However, this scan comes from a Philips scanner, and Philips introduces several alternative scaling factors. Therefore, most Philips scans can be converted as “Display” value (D) or precise floating point  (I refer to these as P, but PAR files refer to these as FP):</p>
<p>The relevant DICOM tags are RS = rescale slope (<a href="http://dicomlookup.com/lookup.asp?sw=Tnumber&amp;q=(0028,1053)" rel="nofollow noopener">0028,1053</a>) RI = rescale intercept (<a href="http://dicomlookup.com/lookup.asp?sw=Tnumber&amp;q=(0028,1052)" rel="nofollow noopener">0028,1052</a>) SS = scale slope (2005,100E) RealWorldIntercept = (0040,9224) Real World Slope = (0040,9225) The transformation formulas are: R = raw value, P = precise value, D = displayed value D = R * RS + RI P = D/(RS * SS),</p>
<p>For more details read <a href="https://github.com/rordenlab/dcm2niix/tree/master/Philips" rel="nofollow noopener">this</a>. Since this is a T1, intensities are relative, so it does not matter which method you use. However, these multiple scaling factors have caused a lot of confusion, in particular with ASL, where different tools expect different values. This explains why dcm2niix reports</p>
<p><code>Philips Scaling Values RS:RI:SS = 4.65714:0:0.044161 (see PMC3998685)</code></p>
<p>You can change dcm2niix’s conversion behaviour using the ‘-p’ argument<br>
-p : Philips precise float (not display) scaling (y/n, default y)</p>
<p>I want to emphasise this is not a limitation in dcm2niix. Rather, Philips has invented their own parameters that do not conform to the DICOM standard.</p>

---

## Post #9 by @lassoan (2019-12-17 04:21 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Thanks a lot for the detailed and very informative explanation. To avoid all kinds of issues, it would be nice if we could harmonize <em>default</em> rescaling behavior among commonly used DICOM image readers (dcm2niix, ITK, vtkDICOM). Do you think current rescaling behavior in ITK’s DICOM reader is good as a default or it should use some of the alternatives instead?</p>
<p>FYI <a class="mention" href="/u/dzenanz">@dzenanz</a> <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #10 by @Tommaso_Di_Noto (2019-12-17 08:23 UTC)

<p>Thank you all very much! <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a></p>

---

## Post #11 by @Chris_Rorden (2019-12-17 11:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> at the moment there is no consensus among the groups who generate ASL tools. Therefore, hard to give guidance regarding what the solution would be. Mathematically, there could in theory be situations where you can not generate store the precise value in a NIfTI or NRRD style pair of intercepts and slopes, so you would have to convert the raw data to float to preserve these values. Adding to this, it is possible that Philips could store different coefficients for the “RealWorld” values than the precise values, so one need to consider what to do if you have a different NIfTI/NRRD scl_slope/scl_inter for the Precise versus RealWorld values. For GitHub, I have usually trusted  @<strong><a href="https://github.com/drmclem" rel="nofollow noopener">drmclem</a></strong>’s guidance (as he works at Philips and has encyclopaedic knowledge). My current solution is to use Precise values by default, provide the option to use the Display values, report original coefficients in the BIDS sidecar, and report discrepancies between solutions in the command line during conversion. <a class="mention" href="/u/fedorov">@fedorov</a> may also have thoughts on this.</p>
<p>I also note the development branch of dcm2niix provides <a href="https://github.com/rordenlab/dcm2niix/tree/development/Philips" rel="nofollow noopener">clearer notes</a> on these matters than the current stable release.</p>

---

## Post #12 by @Chris_Rorden (2019-12-17 15:48 UTC)

<p>As an aside:</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="1" data-topic="9513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>but then I tried opening the two same stacks (dcm and nii) in fsleyes and the two issues don’t happen (i.e. the intensities are the same and the z-axes are non inverted).</p>
</blockquote>
</aside>
<p>You should be aware that FSLeyes includes dcm2niix and uses it for DICOM file imports. Therefore, the fact that FSLeyes agrees with command line usage of dcm2niix should not be used as evidence that this is the right way to do things: these are not independent tests.</p>
<p>One looming concern for Philips compatibility is not only can the image specify three different scaling factors (display, precise, real world), but also that a <a href="https://github.com/rordenlab/dcm2niix/issues/363" rel="noopener nofollow ugc">separate intensity scaling factor can be applied to each and every slice</a> of a volume. While this is legal DICOM,  neither NIfTI nor NRRD can support this, so I assume converters will need to store voxels as 32-bit floats instead of 16-bit integers to represent these datasets.</p>

---
