# Open Nifti in 3D Slicer

**Topic ID**: 24495
**Date**: 2022-07-26
**URL**: https://discourse.slicer.org/t/open-nifti-in-3d-slicer/24495

---

## Post #1 by @GoWi (2022-07-26 08:42 UTC)

<p>I usually converted the image data from our small animal PET scanner into Nifti to be able to open it in slicer. In the newer versions we have problems and get an error message. Neither newly converted data nor Nifti files that were previously already opened in slicer still work.</p>
<p>“Error occured while loading selected files.” Details: “Error: Loading (path+file name) -  load failed.”</p>
<p>In version 4.10.xx it still works, in all versions 5.0x it does not work. I am using the windows-version.<br>
Is there any further information needed to reproduce the problem?</p>
<p>I am grateful for any advice on how I should proceed.</p>
<p>Thank you in advance,<br>
Gordon</p>

---

## Post #2 by @pieper (2022-07-26 13:15 UTC)

<aside class="quote no-group" data-username="GoWi" data-post="1" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b3f665/48.png" class="avatar"> GoWi:</div>
<blockquote>
<p>Is there any further information needed to reproduce the problem?</p>
</blockquote>
</aside>
<p>Yes, please provide a sample file (via dropbox, google drive etc) that demonstrates the issue.</p>
<p>Also note that we routinely tell people to avoid the nifti format if you can since it is very common to get ill-formed files depending on the software that generates them.</p>

---

## Post #3 by @GoWi (2022-07-26 14:11 UTC)

<p>So far, the Nifti format had worked well for us and we had not noticed any problems. We will now also check, if we can convert the image data to some other file format.</p>
<p>For test, please feel free the following data:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/a5ovt46o48e4au4/ChickenEgg-PET-Data.nii?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/a5ovt46o48e4au4/ChickenEgg-PET-Data.nii?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/a5ovt46o48e4au4/ChickenEgg-PET-Data.nii?dl=0" target="_blank" rel="noopener nofollow ugc">ChickenEgg-PET-Data.nii</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I could open this file in 3D Slicer versions 4.10.2 and 4.11.2020930 but not in 5.0.3 or 5.1.0-2022-07-22.</p>

---

## Post #4 by @lassoan (2022-07-26 16:35 UTC)

<aside class="quote no-group" data-username="GoWi" data-post="3" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b3f665/48.png" class="avatar"> GoWi:</div>
<blockquote>
<p>So far, the Nifti format had worked well for us and we had not noticed any problems.</p>
</blockquote>
</aside>
<p>I’ve debugged this issue and the problem according to the NIFTI reader in ITK is that <code>ITK only supports orthonormal direction cosines.  No orthonormal definition found!</code>. I would recommend to report this issue on the <a href="https://discourse.itk.org/">ITK forum</a> and in the meantime switch to NRRD.</p>
<p>You have been really lucky that this is the first time you ran into problem because of NIFTI. NIFTI is really just so unnecessarily complicated and fragile file format that everyone should stay away from it (except neuroimaging researchers, because they have built a lot of tools around it over the years that it would be hard to drop it; and there are also some useful features for brain imaging).</p>

---

## Post #5 by @GoWi (2022-07-28 10:00 UTC)

<p>Just for me to understand again. The Nifti files are opened in Slicer via ITK?<br>
And ITK has changed from Slicer version 4 to version 5?</p>
<p>ITK-SNAP 3.8 can open the file with 16-bit precision, but not the original 32-bit.</p>
<p>Do you have any recommendation for converting image file from preclinical PET to NRRD? I have used Vinci for conversion to Nifti. The software does not convert to NRRD.</p>
<p><a href="https://vinci.sf.mpg.de/" rel="noopener nofollow ugc">VINCI | About (mpg.de)</a></p>
<p>Original PET-Data:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/zwa9neqari3aiv5/ChickenEgg-PET-Data.img.hdr?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/zwa9neqari3aiv5/ChickenEgg-PET-Data.img.hdr?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/zwa9neqari3aiv5/ChickenEgg-PET-Data.img.hdr?dl=0" target="_blank" rel="noopener nofollow ugc">ChickenEgg-PET-Data.img.hdr</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/hdtokjkt8ai8c40/ChickenEgg-PET-Data.img?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/hdtokjkt8ai8c40/ChickenEgg-PET-Data.img?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/hdtokjkt8ai8c40/ChickenEgg-PET-Data.img?dl=0" target="_blank" rel="noopener nofollow ugc">ChickenEgg-PET-Data.img</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would be very grateful for any further advice.</p>

---

## Post #6 by @Chris_Rorden (2022-07-28 13:40 UTC)

<p><strong>Background</strong></p>
<p>I respectfully disagree with <a class="mention" href="/u/lassoan">@lassoan</a>’s comments regarding NIfTI being fragile. From my perspective, the <a href="https://brainder.org/2012/09/23/the-nifti-file-format/" rel="noopener nofollow ugc">NIfTI</a> format is very simple (just 348 bytes) and explicit, but it is tuned to a specific domain. Relative to other formats like DICOM, NRRD and NIfTI are very similar. One main difference between the two is that to support NRRD you need a very good reader to parse the various spatial frames of reference. On the other hand, NIfTI uses only a single <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Spatial_Coordinates" rel="noopener nofollow ugc">spatial coordinate system</a> so reading is simple, but the writing of NIfTI is challenging as you must use the NIfTI frame of reference.</p>
<p>The biggest issue many have with NIfTI is that it can include two different spatial transforms - the QForm and the SForm. The qform_code and sform_code allow you to understand what they refer to. While usage can vary, the original rationale is that the Q-Form code could map the image alignment to the scanner’s acquisition space, while the S-Form can map the image to a standard space where the participants brain is aligned to a typical brain size, rotation and origin (with a full affine 12 degrees of freedom: 3 axes rotation, 3 axes translation, 3 axes zoom and 3 axes shear). It is particularly unfortunate that the NIfTI creation specified that the Q Form uses a quaternion (which only has 9 degrees of freedom) while the S Form uses a matrix (with 12 DoF). This does complicate support for the format. Also, since the SForm supports shears,  where many image viewers require are unable to support rhomboidal images.</p>
<p>The Insight ToolKit (ITK) does not support rhomboidal images. While this may have changed, early versions of ITK always gave precedence to the QForm (presumably because the constrained QForm can not represent rhomboidal images), while most other tools chose between the SForm and QForm by selecting the higher qform_code versus sform_code (and giving precedence to the SForm in the case of ties). This meant that the starting estimates for ITK based tools like ANTS were often very different from other NIfTI tools like SPM and FSL.</p>
<p>For these reasons, most tools today create NIfTI images where the SForm and QForm are identical. Rhomboidal images are virtually never seen in MRI (though they exist with CT scans acquired with gantry tilt), so most tools limit NIfTI images to 9 degrees of freedom.</p>
<p><strong>Problem with your image</strong></p>
<p>Long story short, I think the core issue with your image is that it fails to specify either a sform_code or a qform_code, and the two spatial representations are mutually exclusive:</p>
<pre><code class="lang-auto">fslhd ChickenEgg-PET-Data.nii
...
qform_name	Unknown
qform_code	0
qto_xyz:1	0.865759 0.000000 0.000000 0.000000 
qto_xyz:2	0.000000 0.865759 0.000000 0.000000 
qto_xyz:3	0.000000 0.000000 0.796000 0.000000 
qto_xyz:4	0.000000 0.000000 0.000000 1.000000 
qform_xorient	Left-to-Right
qform_yorient	Posterior-to-Anterior
qform_zorient	Inferior-to-Superior
sform_name	Unknown
sform_code	2
sto_xyz:1	1.000000 0.000000 0.000000 -54.975697 
sto_xyz:2	0.000000 1.000000 0.000000 -54.975697 
sto_xyz:3	0.000000 0.000000 1.000000 -37.411999 
sto_xyz:4	0.000000 0.000000 0.000000 1.000000 
</code></pre>
<p><strong>Solution</strong></p>
<p>The easiest fix is would be to make sure the SForm and QForm store the same representation (e.g. the QForm looks plausible but adding a translation to set the origin is required) and set each to the QForm_code and SForm_code to <code>scanner_anat</code>.</p>
<p>Longer term, it looks like your data was acquired on a CTI Concorde model 2501. I have never seen the text format for the header you provided. I would see if you can either export the data from the scanner as DICOM or ECAT. You can use <a href="https://github.com/rordenlab/dcm2niix" rel="noopener nofollow ugc">dcm2niix</a> to convert those to clean NIfTI or NRRD datasets. dcm2niix can be run from the command line, but it is also available as a slice extension. You might also want to look at <a href="https://github.com/openneuropet/PET2BIDS" rel="noopener nofollow ugc">PET2BIDS</a> which is a wrapper from dcm2niix that helps specify a lot of the PET details that are useful for curated archival datasets.</p>

---

## Post #7 by @issakomi (2022-07-28 14:19 UTC)

<blockquote>
<p>The Nifti files are opened in Slicer via ITK?</p>
</blockquote>
<p>Yes</p>
<blockquote>
<p>And ITK has changed from Slicer version 4 to version 5?</p>
</blockquote>
<p>Yes. BTW, the error message appears in the commit <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/34231b57021418fdb6afd4fcf5082a73b12969ed" rel="noopener nofollow ugc">ENH: Prefer to use sform over qform when both are set</a>.<br>
I have checked, older versions of my app (uses ITK IO for Nifti), like Slicer, can open the nii file:<br>
Spacing: [0.865759, 0.865759, 0.796]<br>
Origin: [54.9757, 54.9757, -37.412]<br>
Direction:<br>
-1 0 0<br>
0 -1 0<br>
0 0 1</p>
<p>(in LPS space)</p>
<p>New version fails, of course.</p>
<p>BTW,</p>
<p><code>$nifti_tool -check_hdr -infiles ChickenEgg-PET-Data.nii</code><br>
said<br>
<code>header IS GOOD for file ChickenEgg-PET-Data.nii</code></p>
<p>The header from nifti_tool:</p>
<p>…<br>
pixdim   76    8   0.0 0.865759 0.865759 0.796 0.0 0.0 0.0 0.0<br>
…<br>
qform_code           344      1    0<br>
sform_code           348      1    2<br>
quatern_b            352      1    0.0<br>
quatern_c            360      1    0.0<br>
quatern_d            368      1    0.0<br>
qoffset_x            376      1    0.0<br>
qoffset_y            384      1    0.0<br>
qoffset_z            392      1    0.0<br>
srow_x               400      4    1.0 0.0 0.0 -54.975697<br>
srow_y               432      4    0.0 1.0 0.0 -54.975697<br>
srow_z               464      4    0.0 0.0 1.0 -37.411999<br>
…</p>
<p>Strange why it fails, specially if sform should be preferred over qform. Probably authors of ITK’s Nifti IO should take a look.</p>
<p>The Analyse7.5(?) img file worked with ITK 4.13 and fails now too.</p>

---

## Post #8 by @GoWi (2022-07-28 15:23 UTC)

<p>Thank you very much for the detailed answers.</p>
<p>About the data: It is image data from a small animal PET scanner FOCUS 120 from Concorde Microsystem Inc, later Siemens. I have only been able to open the image data with ITK Snap 3.8, Amide and Vinci. ITK Snap 3.8 brings the mentioned error message concerning the 16-bit precision.<br>
For Slicer I had therefore converted the data so far by means of Vinci into Nifti.</p>
<p>At least in Vinci another format is given under “Analysis Image”, I am not sure if Analysis7.5 corresponds to the format of the FOCUS 120.</p>
<p>So as far as I understand the answers correctly, the reason is most likely a changed I/O at the ITK.</p>
<p>Thanks again, then I’ll see if I can realize the other conversions!</p>

---

## Post #9 by @lassoan (2022-07-28 16:13 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> and <a class="mention" href="/u/issakomi">@issakomi</a> Thanks a lot for sharing your valuable insights!</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="6" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>I respectfully disagree with <a class="mention" href="/u/lassoan">@lassoan</a>’s comments regarding NIfTI being fragile.</p>
</blockquote>
</aside>
<p>By “fragile” I meant that if you use NIFTI then it is easy to end up with invalid or ambiguous data because there are so many things that can go wrong.</p>
<p>This seems to be due to inherent flaws of this file format, because the same software developers that struggle to read/write NIFTI correctly have no trouble implementing correct readers and writers for other research file formats with similar capabilities, such as NRRD or MetaIO.</p>

---

## Post #10 by @pieper (2022-07-28 16:19 UTC)

<p>Thanks everyone for the informative discussion.</p>
<p>If this ChickenEgg file is well formed but not readable by the current ITK then for sure the ITK community should be informed and perhaps this can be addressed in a future version (if no one has done it yet, starting a thread at <a href="https://discourse.itk.org/">https://discourse.itk.org/</a> would be a good place to start, as <a class="mention" href="/u/lassoan">@lassoan</a> suggested).</p>
<p>For Slicer, we can often represent images with more generality than ITK, for example by allowing gantry tilt, missing slices, etc.  We typically focus on DICOM for this but if someone wanted to do it it would be possible to introduce options in the nifti reader that would handle these variants.</p>
<p>For example, here’s a <a href="https://github.com/pieper/SlicerDMRI/blob/9565f89d16cd72618cd87f1c9046542450e4937b/Modules/Scripted/NIfTIFile/NIfTIFile.py">work-in-progress module for a custom reader</a> for a common diffusion nifti convention (where there are .bval and .bvec files in the directory with the .nii.gz) that users can optionally select instead of the default ITK-based reader).  Someone could do a similar plugin using something like nibabel in python to read the nifti with options to handle the header variants.</p>

---

## Post #11 by @Chris_Rorden (2022-07-28 19:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> perhaps you can provide examples? From my perspective, NIfTI is extremely explicit and simple. While you can create malformed NIfTIs, the same is true of NRRD. For both, there are obvious correct ways of doing things. It is unfortunate that the NIfTI specification used both quaternions and matrices, which requires a reader to support both types (though a writer can just choose one). For full disclosure, I advocated for not including the QForm when NIfTI was created. I do think the ITK standards implementation of NIfTI was completely different from others. I did ask the ITK team to try to use the same approach as SPM/FSL/etc many, many years ago and was told they would not change things due to fear of unintended consequences. I am glad to know that the latest version of ITK behaves like other tools.</p>
<p>I do think NRRD is nice because you can use a NRRD header to describe an image saved in a different format, adapting to the original formats spatial frame of reference.</p>
<p>I think both NRRD and NIfTI fill a niche, but it seems that NIfTI has gained much broader adoption in the field of brain imaging.</p>

---

## Post #12 by @lassoan (2022-07-28 20:29 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="11" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>perhaps you can provide examples? From my perspective, NIfTI is extremely explicit and simple.</p>
</blockquote>
</aside>
<p>This very topic is an example. But there are many more examples that indicate that for many users and developers NIFTI is too complex and prone to misinterpretation:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/flipped-nifti-image-compared-to-original-nrrd-file/479" class="inline-onebox">Flipped NIFTI image compared to original Nrrd File</a></li>
<li><a href="https://discourse.itk.org/t/nifti-orientation-issues/431" class="inline-onebox">NIFTI Orientation Issues - nifti - ITK</a></li>
<li><a href="https://discourse.itk.org/t/direction-orientation-matrix-dicom-vs-nifti/3289" class="inline-onebox">Direction/Orientation matrix DICOM vs Nifti - Algorithms - ITK</a></li>
<li><a href="https://discourse.itk.org/t/nifti-rpi-orientation-file-exported-to-dicom-wrong-orientation/1612" class="inline-onebox">Nifti (RPI orientation) file exported to DICOM - wrong orientation - ITK</a></li>
<li><a href="https://discourse.slicer.org/t/nifti-file-sform-and-slicer-image-origin-seem-to-disagree/7711" class="inline-onebox">Nifti file sform and Slicer image origin seem to disagree</a></li>
<li><a href="https://discourse.slicer.org/t/misalignment-between-nifti-image-and-mask/11507" class="inline-onebox">Misalignment between Nifti image and mask</a></li>
<li><a href="https://discourse.slicer.org/t/interactive-lung-lobe-segmentation-fails-with-nifti-volume/24052" class="inline-onebox">Interactive lung lobe segmentation fails with NIFTI volume</a></li>
<li><a href="https://github.com/NIFTI-Imaging/nifti_clib/issues/127" class="inline-onebox">Ambiguous interpretation of a NIfTI-1 image · Issue #127 · NIFTI-Imaging/nifti_clib · GitHub</a></li>
<li><a href="https://discourse.itk.org/t/dicom-nrrd-nifti-spacing-origin-mismatch/4311" class="inline-onebox">dicom nrrd nifti spacing, origin mismatch. - ITK</a></li>
<li><a href="https://discourse.itk.org/t/nifti-imagefilereader-imagefilewriter-changes-orientation-matrix/4064" class="inline-onebox">Nifti: ImageFileReader + ImageFileWriter changes orientation matrix - Beginner Questions - ITK</a></li>
<li><a href="https://discourse.itk.org/t/nifti-file-orientation-change-between-2019-08-26-and-itk-v5-1rc01/2594" class="inline-onebox">Nifti file orientation change between 2019-08-26 and ITK v5.1rc01 - Engineering - ITK</a></li>
<li><a href="https://github.com/Project-MONAI/MONAILabel/issues/211" class="inline-onebox">Miscellaneous - Generated mask is shown with different origin from the original image · Issue #211 · Project-MONAI/MONAILabel · GitHub</a></li>
<li><a href="https://github.com/Project-MONAI/MONAILabel/issues/35" class="inline-onebox">[Slicer] ITK reader - orthonormal direction cosines · Issue #35 · Project-MONAI/MONAILabel · GitHub</a></li>
<li><a href="https://discourse.slicer.org/t/nrrd-vs-nii-regarding-affine-data-and-transforms/1896" class="inline-onebox">Nrrd vs nii regarding affine data and transforms</a></li>
<li><a href="https://discourse.slicer.org/t/nifti-problem-with-reformatted-segmentations/16035" class="inline-onebox">NIFTI Problem with Reformatted Segmentations</a></li>
<li><a href="https://discourse.itk.org/t/saving-non-orthogonal-volume-in-nifti-format/2760" class="inline-onebox">Saving non-orthogonal volume in Nifti format - Engineering - ITK</a></li>
<li><a href="https://discourse.slicer.org/t/2d-nifti-sagittal-slice-wont-open-in-3dslicer/24407/8" class="inline-onebox">2D nifti sagittal slice won't open in 3DSlicer - #8 by lassoan</a></li>
<li><a href="https://discourse.slicer.org/t/invalid-nifti-orientation-reported/11358" class="inline-onebox">Invalid NIFTI Orientation Reported</a></li>
<li><a href="https://discourse.itk.org/t/simpleitk-writing-nifti-with-invalid-header/2498" class="inline-onebox">SimpleITK writing NIfTI with invalid header - simpleitk - ITK</a></li>
<li><a href="https://github.com/Project-MONAI/MONAILabel/issues/22" class="inline-onebox">Wrong Orientation/Origin for multichannel volumes (4D) using Slicer - Issue visualizing BRATS images on 3DSlicer · Issue #22 · Project-MONAI/MONAILabel · GitHub</a></li>
<li><a href="https://discourse.itk.org/t/simpleitk-how-to-save-dicom-header-into-nii-gz-file/4278" class="inline-onebox">SimpleITK: how to save dicom header into nii.gz file? - ITK</a></li>
<li><a href="https://discourse.itk.org/t/python-writing-is-not-working-correctly/3864" class="inline-onebox">Python writing is not working correctly - Engineering - ITK</a></li>
</ul>

---

## Post #13 by @issakomi (2022-07-29 15:25 UTC)

<p>I have looked a little closer at the issue with IO, the problem is at this <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/8d3197081233d3a69a44a43dd706dcf7d6661275/Modules/IO/NIFTI/src/itkNiftiImageIO.cxx#L1918" rel="noopener nofollow ugc">line</a></p>
<pre><code class="lang-cpp">if (itk::Math::abs(this-&gt;m_NiftiImage-&gt;dx - scale[0]) &gt; large_value_tolerance)
</code></pre>
<p><em>dx</em> is 0.865759 and <em>scale[0]</em> is 1, the variable <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/8d3197081233d3a69a44a43dd706dcf7d6661275/Modules/IO/NIFTI/src/itkNiftiImageIO.cxx#L1903" rel="noopener nofollow ugc">sform_decomposable_without_skew</a> is set to <em>false</em> here and code runs up to the <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/8d3197081233d3a69a44a43dd706dcf7d6661275/Modules/IO/NIFTI/src/itkNiftiImageIO.cxx#L1994" rel="noopener nofollow ugc">exception</a>.</p>
<p>Looks like ITK IO expects a matrix with respect to spacing here, something like<br>
<em>IndexToPointMatrix</em></p>
<pre><code class="lang-auto">  srow_x   0.865759 0.0      0.0      -54.975697
  srow_y   0.0      0.865759 0.0      -54.975697
  srow_z   0.0      0.0      0.796    -37.411999
</code></pre>
<p>and not</p>
<pre><code class="lang-auto">  srow_x    1.0   0.0   0.0      -54.975697
  srow_y    0.0   1.0    0.0     -54.975697
  srow_z    0.0   0.0    1.0     -37.411999
</code></pre>
<p>I don’t know is it correct behavior or not, just FYI.</p>
<p><strong>Edit</strong>:<br>
old version worked fine, BTW, spacing and orientation were correct.</p>

---

## Post #14 by @Chris_Rorden (2022-07-29 15:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I think a lot of these simply reflect the popularity of NIfTI versus NRRD. It is certainly possible to save a NRRD with shears using <code>space directions</code>. I think most NRRD creation tools simply enforce orthogonal volumes that match ITKs desires.</p>
<p>The comments about limited hardcoded meta data is a strength from the perspective of simplicity. NRRD is a bit of the Wild West in terms of defining meta data, so when I tried to make dcm2niix NRRD export compatible with Slicer I found that there really is not standard way of preserving much of the meta data even if you can pack it all in a human readable form.  As noted by others in the comments you link, many of these revolve around ITK’s implementation. As I noted earlier, I tried to work with them well over a decade ago to resolve incompatibilities to no avail. As <a class="mention" href="/u/ihnorton">@ihnorton</a> noted in one of those posts, ITK uses LPS, while NIfTI uses RAS. However, I do not know enough about slicer to understand why this is not handle my reorienting each image to the desired orientation and storing the residual rotation matrix. That is the approach <a href="https://github.com/niivue/niivue" rel="noopener nofollow ugc">NiiVue</a> uses - with each volume always approximately RAS and storing a residual as well as an inverse transform.</p>
<p>Again, I do not think NIfTI is perfect. The inclusion of quaternions is very alien to most users, and it does require every tool to handle (typically by converting them to a matrix and  a potentially lossy transform of a matrix). However, if one wants to be the advocate for quaternions you could see their inability to store shears as a strength. It works well with tools like ITK that can not abide by rhomboidal volumes and prevents shears from accumulating doing to rounding errors.</p>

---

## Post #15 by @Chris_Rorden (2022-07-29 16:16 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> it looks like you have done nice detective work. The current ITK code does not seem to have a robust detection of skew, and such a test would fail for both a NRRD and NIfTI that included a sheared matrix. I think the reliable way to detect this would be to leverage the fact that quaternions can not retain shears. So given a matrix that you want to test, convert it to a quaternion and convert that quaternion to a matrix. This will be identical to the input if there is no shear. You can compare the direction of the row, column and slice vectors to provide a human-readable tolerance for shear (e.g. difference in degrees).</p>
<p>ITK already includes these transforms in the NIfTI reading: <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/8d3197081233d3a69a44a43dd706dcf7d6661275/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c#L1547" rel="noopener nofollow ugc">nifti_mat44_to_quatern</a> and  <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/8d3197081233d3a69a44a43dd706dcf7d6661275/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c#L1476" rel="noopener nofollow ugc">nifti_quatern_to_mat44</a> if one wants to do this completely in the NIfTI reader. On the other hand, a more general solution that will work for NRRD files could use the vnl_matrix_fixed and vnl_quaternion functions.</p>

---

## Post #16 by @Chris_Rorden (2022-07-29 18:01 UTC)

<p>A simpler approach is to simply measure the <a href="https://www.omnicalculator.com/math/angle-between-two-vectors" rel="noopener nofollow ugc">angles</a> for the row versus column, row versus slice and column versus slice. These should all be 90 degrees.</p>
<p><a href="https://github.com/niivue/niivue/blob/64386d4cfccde2071e52e93b16cf0ed8095e49c5/src/nvimage.js#L439" rel="noopener nofollow ugc">Here is a JavaScript implementation</a></p>

---

## Post #17 by @lassoan (2022-07-29 18:52 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="14" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>I think a lot of these simply reflect the popularity of NIfTI versus NRRD.</p>
</blockquote>
</aside>
<p>I’ve thought about this, too, but many problems simply cannot occur with other formats, because it is much harder to create ambiguous or invalid files.</p>
<p>For example, other research image file formats use origin, spacing, axis direction vectors (not quaternion) to specify image geometry and explicitly allow non-orthogonal image axes. ITK image class can store images with non-orthogonal axes and ITK readers, writers, and resampling filters support such images. So, there is a simple, unambiguous process to handle sheared images in ITK.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="14" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>many of these revolve around ITK’s implementation</p>
</blockquote>
</aside>
<p>I agree. But ITK developers are smart people with lots of domain knowledge and connections to the neuroimaging community, so if they cannot implement a robust file reader/writer for NIfTI in 10-20 years then there must be something inherently wrong with this format.</p>
<p>The RAS/LPS convention is not an issue. ITK always loads images into LPS coordinate system, performing any necessary conversions. The image orientation problems are usually due to flip around a single axis.</p>
<p>I think the main problems are the usage quaternion, redundancy of sform/qform, and inconsistent behavior of various implementations.</p>

---

## Post #18 by @Chris_Rorden (2022-07-29 19:28 UTC)

<p>Not at all my perspective, NIfTI is simple and supported robustly by a huge number of tools, including major ones like SPM, FSL and AFNI. NIfTI was the lowest common denominator that allowed these tools to work robustly. The ITK implementation is the odd one out. Early ITK implementations gave precedence to the QForm regardless of the Q/SForm codes and were divergent from all other implementations and the NIfTI specification. These choices caused ITK based tools to behave oddly. For many years, the ITK team refused to conform to the standard or other tools, for the sake of backward compatibility. I agree that the ITK team is talented engineers, but they made a willful choice of maintaining the behavior of the software to preserve behavior with previous versions of ITK, regardless of the behavior of all the other tools. The SPM team even changed their NIfTI writer to make the SForm and QForm the same (to the extent possible) to support ITK based tools. I am glad that the ITK team now supports the specification, and I do hope this bug will lead to consistent behavior that is similar to other tools and reduce the number of issues the Slicer developers and users are experiencing.</p>

---

## Post #19 by @lassoan (2022-07-29 20:32 UTC)

<p>ITK should be changed so that it works consistently with the major neuro software packages, which should reduce friction between ITK-based tools and SPM/FSL/AFNI. If there are any remaining issues in the current ITK implementation then please ask on the ITK developers to address it. I and other Slicer community members will support this any way we can. If there is anything to change how ITK NIfTI IO is used in Slicer then let us know.</p>
<p>Still, this does not address the world outside the neuroimaging community. I see many incorrect/ambiguous NIfTI images out there and bad ones are still being created - either because of incorrect writer implementations or misuse by people who just want to save their image and don’t want to learn about sform/qform. One solution would be to simplify NIfTI (e.g., by removing qform), but since the neuroimaging community does not seem to have any problem with it, this will probably not happen. That’s why I keep discouraging use of NIfTI for all users who don’t need it and don’t want to spend time with understanding it (e.g., anyone outside the neuroimaging field) and recommend to use a simpler format instead.</p>

---

## Post #20 by @issakomi (2022-07-30 13:15 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="15" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>code does not seem to have a robust detection of skew, and such a test would fail for both a NRRD and NIfTI that included a sheared matrix</p>
</blockquote>
</aside>
<p>The file could be loaded if the <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/8d3197081233d3a69a44a43dd706dcf7d6661275/Modules/IO/NIFTI/src/itkNiftiImageIO.cxx#L1913-L1932" rel="noopener nofollow ugc">block scope</a> has been removed. From the sform, spacing and orientation are correct.</p>
<p>Spacing: [0.865759, 0.865759, 0.796]<br>
Origin: [54.9757, 54.9757, -37.412]<br>
Direction:<br>
-1 0 0<br>
0 -1 0<br>
0 0 1</p>
<p>We spoke already in the past on ITK forum about sheared matrices / rhomboidal images, i am still a little pessimistic about them.</p>
<p><strong>Edit</strong>:<br>
Does your tool currently write Nrrd files with sheared matrix?</p>

---

## Post #21 by @issakomi (2022-07-30 19:12 UTC)

<aside class="quote no-group" data-username="issakomi" data-post="20" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>Does your tool currently write Nrrd files with sheared matrix?</p>
</blockquote>
</aside>
<p>I can answer it already. I tried dcm2niix with DICOM series (equidistant, parallel, gantry tilt) and “-e y” option, produced 2 files, one has shear matrix and another seems to be orthogonal and corrected.</p>
<p>The shear one looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3bce1b776f92a403c9c65948e1d3a9042dd05c2.jpeg" data-download-href="/uploads/short-url/ud7qfKFKvYZ20YtStJ4qn1Fjrbk.jpeg?dl=1" title="Screenshot at 2022-07-30 20-24-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3bce1b776f92a403c9c65948e1d3a9042dd05c2_2_345x221.jpeg" alt="Screenshot at 2022-07-30 20-24-27" data-base62-sha1="ud7qfKFKvYZ20YtStJ4qn1Fjrbk" width="345" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3bce1b776f92a403c9c65948e1d3a9042dd05c2_2_345x221.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3bce1b776f92a403c9c65948e1d3a9042dd05c2_2_517x331.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3bce1b776f92a403c9c65948e1d3a9042dd05c2_2_690x442.jpeg 2x" data-dominant-color="9E9DA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2022-07-30 20-24-27</span><span class="informations">1211×779 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Neither Nrrd nor Nifti files with shear matrices were recognized by ITK as such. I didn’t look at Nrrd IO, but Nifti IO tried to detect it and failed.</p>
<p>It can be done like this, BTW, very simple (the values are from Nrrd <a href="https://drive.google.com/file/d/1ThD2k6RgcRWAk9j1NzU-tPpNRxpR_C8S/view?usp=sharing" rel="noopener nofollow ugc">files</a> produced by dcm2niix):</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">#include &lt;iostream&gt;
#include &lt;cmath&gt;

typedef struct
{
	double x;
	double y;
	double z;
} V3;

static V3 normalize(V3 v)
{
	const double j = 1.0/(sqrt((v.x*v.x) + (v.y*v.y) + (v.z*v.z)));
	V3 vn;
	vn.x = v.x*j;
	vn.y = v.y*j;
	vn.z = v.z*j;
	return vn;
}

static double dot(V3 a, V3 b)
{
	return ((a.x*b.x) + (a.y*b.y) + (a.z*b.z));
}

static bool is_orthogonal(V3 v0, V3 v1, V3 v2)
{
	const double tolerance = 1e-3;
	const V3 n0 = normalize(v0);
	const V3 n1 = normalize(v1);
	const V3 n2 = normalize(v2);
	const double d = dot(n0, n1) + dot(n0, n2) + dot(n1, n2);
	const bool b = fabs(d) &lt;= tolerance;
	return b;
}

int main(int argc, char ** argv)
{
#if 1
	// shear
	V3 v0;
	v0.x = -0.482422;
	v0.y = 0.03;
	v0.z = 0.0;

	V3 v1;
	v1.x = 0.0;
	v1.y = 0.50871;
	v1.z = 0.153075;

	V3 v2;
	v2.x = 0.0;
	v2.y = 2.38419e-07;
	v2.z = 2.24829;
#else
	// orthogonal
	V3 v0;
	v0.x = -0.482422;
	v0.y = -0.0;
	v0.z = 0.0;

	V3 v1;
	v1.x = 0.0;
	v1.y = 0.457492;
	v1.z = 0.153075;

	V3 v2;
	v2.x = -0.0;
	v2.y = -0.752269;
	v2.z = 2.24829;
#endif
	const bool b = is_orthogonal(v0, v1, v2);
	std::cout &lt;&lt; "orthogonal = " &lt;&lt; (b ? "yes" : "no") &lt;&lt; std::endl;
	return 0;
}
</code></pre>

---

## Post #22 by @issakomi (2022-07-31 07:35 UTC)

<aside class="quote no-group" data-username="issakomi" data-post="21" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>Neither Nrrd nor Nifti files with shear matrices were recognized by ITK as such.</p>
</blockquote>
</aside>
<p>Correction for Nifti file: ITK IO preferred qform for the <a href="https://drive.google.com/file/d/1ThD2k6RgcRWAk9j1NzU-tPpNRxpR_C8S/view?usp=sharing" rel="noopener nofollow ugc">file</a> with shear matrix.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30b517230d3ad656f61e136e5d4c37e5283b7166.png" data-download-href="/uploads/short-url/6WSTYR6q6MTp8uWGssqJfx3FBjM.png?dl=1" title="Screenshot at 2022-07-31 09-29-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30b517230d3ad656f61e136e5d4c37e5283b7166_2_345x221.png" alt="Screenshot at 2022-07-31 09-29-53" data-base62-sha1="6WSTYR6q6MTp8uWGssqJfx3FBjM" width="345" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30b517230d3ad656f61e136e5d4c37e5283b7166_2_345x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30b517230d3ad656f61e136e5d4c37e5283b7166_2_517x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30b517230d3ad656f61e136e5d4c37e5283b7166_2_690x442.png 2x" data-dominant-color="A2A1A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2022-07-31 09-29-53</span><span class="informations">1211×779 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @Chris_Rorden (2022-07-31 11:18 UTC)

<p>For reference, the CT with gantry tilt (that results in a sheared matrix) that <a class="mention" href="/u/issakomi">@issakomi</a> refers to is <a href="https://github.com/neurolabusc/dcm_qa_ct" rel="noopener nofollow ugc">available in DICOM and NIfTI format here</a>. You can use dcm2niix to convert it to either NIfTI or NRRD. Since many tools do not handle shear, dcm2niix will also create a copy of the image where the image is interpolated to a orthogonal grid (with the <code>_tilt</code> extension to the file name). This provides an example of what the image should look like.</p>
<p>You can view the image in voxel space (where it appears distorted) or world space (which adjusts for gantry tilt) using the <a href="https://niivue.github.io/niivue/features/worldspace2.html" rel="noopener nofollow ugc">NiiVue live view web page</a> - just drag and drop the NIfTI or NRRD image you wish to inspect. Use the <code>world space</code> button to choose between world (top) and voxel (bottom) space:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/026e13423cd23c0e6b95a5315c1989009d71ce1a.jpeg" data-download-href="/uploads/short-url/luMYSPoOu2URS57aL9mQAbyROa.jpeg?dl=1" title="tilt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026e13423cd23c0e6b95a5315c1989009d71ce1a_2_327x500.jpeg" alt="tilt" data-base62-sha1="luMYSPoOu2URS57aL9mQAbyROa" width="327" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026e13423cd23c0e6b95a5315c1989009d71ce1a_2_327x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026e13423cd23c0e6b95a5315c1989009d71ce1a_2_490x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026e13423cd23c0e6b95a5315c1989009d71ce1a_2_654x1000.jpeg 2x" data-dominant-color="392F3F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tilt</span><span class="informations">785×1198 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> now that ITK supports the same spatial transforms as other tools, I suspect the odd behavior you have been experiencing will diminish dramatically. In cases where the spatial transform was improperly specified, the user will get similar feedback regarding the odd setting regardless of the tool that is used. I also wonder if we could insert a bit of logic into ITK to detect malformed spatial transforms. With NRRD, the spatial transform is optional, but with NIfTI is is required. Therefore, I assume that reading a NRRD without a spatial transform is loaded with an identity matrix, while the explicit usage of a spatial transform in NIfTI requires the user to supply sensible values. Another thing to check with ITK is whether it can discriminate between NIfTI format files and its ancestor the Analyze format which did not include a spatial transform. Analyze files must be treated in the <code>old way</code>, as described in the <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h" rel="noopener nofollow ugc">NIfTI specification</a>.</p>
<p>My tools tend to do a couple checks to detect a bogus spatial transform (regardless of the format). This logic may be useful for detecting files where the spatial transformation matrix should be used. The basic check is:</p>
<ol>
<li>All values of the 4x4 spatial transformation matrix must be finite: NaNs, Infinity, negative Infinity suggest a borked matrix.</li>
<li>Assuming a 3D image (at least 2 voxels in each direction): For the 3x3 rotation matrix (e.g. ignoring translations) each row and each column must have at least one non-zero value and the 9 values of the matrix must have some variability.</li>
</ol>

---

## Post #24 by @issakomi (2022-07-31 12:23 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="23" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>where the image is interpolated to a orthogonal grid (with the <code>_tilt</code> extension to the file name)</p>
</blockquote>
</aside>
<p>They (blue) are really nice and match perfectly with the original DICOM slices (red), BTW.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb38b6377a0e55a6fbbc77b28b133be63922841b.png" data-download-href="/uploads/short-url/qIeN4bmsTcBQZSfNrijdmmT5pKb.png?dl=1" title="20220731-141731" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb38b6377a0e55a6fbbc77b28b133be63922841b_2_238x250.png" alt="20220731-141731" data-base62-sha1="qIeN4bmsTcBQZSfNrijdmmT5pKb" width="238" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb38b6377a0e55a6fbbc77b28b133be63922841b_2_238x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb38b6377a0e55a6fbbc77b28b133be63922841b_2_357x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb38b6377a0e55a6fbbc77b28b133be63922841b_2_476x500.png 2x" data-dominant-color="735E66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20220731-141731</span><span class="informations">606×635 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @Chris_Rorden (2022-07-31 16:26 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> thanks for noticing. dcm2niix does attempt to preserve spatial information. The method is <a href="https://github.com/rordenlab/dcm2niix/issues/253" rel="noopener nofollow ugc">discussed here</a>. It uses in-plane linear interpolation which might not be ideal for all applications. This can mean some loss of high frequencies, but for most uses is less jagged than nearest-neighbor and avoids the ringing artifacts of higher-order interpolation.</p>

---

## Post #26 by @pieper (2022-07-31 16:39 UTC)

<p>A note to Slicer users, if you have DICOM images with gantry tilt or variable spacing you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html?highlight=geometry">Acquisition geometry regularization</a> option is enabled as <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">described here</a>.  This creates a nonlinear transform that can later be hardened with whatever options are needed in terms of filters and target sample grid.</p>

---

## Post #27 by @issakomi (2022-08-02 00:03 UTC)

<p>S. issue: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/3514" class="inline-onebox" rel="noopener nofollow ugc">Nifti file can not be opened after Jul 2020 commit · Issue #3514 · InsightSoftwareConsortium/ITK · GitHub</a></p>

---

## Post #28 by @issakomi (2022-08-08 20:42 UTC)

<p>Update. ITK rejected to fix the issue, the Nifti file is incorrectly written. S. <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/3514#issuecomment-1208523126" rel="noopener nofollow ugc">post</a></p>
<p>P.S. I tried to download that VINCI, filled a form several days ago with address, phone, etc. and there is still no reply. The only thing i shall do with VINCI is to file a request to delete my personal data and confirm it.</p>

---

## Post #29 by @pieper (2022-08-08 22:14 UTC)

<p>Thanks for following up on that <a class="mention" href="/u/issakomi">@issakomi</a>.  I see Hans’s point and I don’t like supporting ill-formed nifti files but in this case it’s an unfortunate backwards compatibility issue with no clear path for users.   On the plus side it’s probably not a common issue.  If a lot of people end up having this trouble perhaps a nifti patcher like the dicom patcher would be the easiest solution.</p>

---

## Post #30 by @lassoan (2022-08-09 07:26 UTC)

<p>Nifti file ambiguities and non-conformances such as this one could be caught early or automatically fixed up by Nifti IO implementations. Therefore it seems that a major contributor to Nifti headaches is that commonly used Nifti implementations behave inconsistently.</p>
<p>Is there a forum where handling of Nifti inconsistencies could be discussed and binding decisions could be made for all implementations that want to claim they comply to the standard?</p>

---

## Post #31 by @pieper (2022-08-09 12:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="24495">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there a forum where handling of Nifti inconsistencies</p>
</blockquote>
</aside>
<p>The NIH encouraged working groups to standardize and expand nifti in the early 2000s but it’s always been pretty ad hoc.  The closest now would be <a href="https://bids.neuroimaging.io/">the BIDS group</a>.  But I don’t think it’ll ever by <a href="https://www.iso.org/standard/72941.html">an ISO standard like DICOM</a> with a formal process.</p>

---

## Post #32 by @lassoan (2022-08-09 22:36 UTC)

<p>I see. This is quite discouraging. I added a comment to <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/3514#issuecomment-1209957193">ITK#3514</a> to see if <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> sees any chance that inconsistency of Nifti readers could be reduced.</p>

---

## Post #33 by @lassoan (2022-08-15 22:28 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> <a class="mention" href="/u/issakomi">@issakomi</a> could you help with answering <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> at <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/3514" class="inline-onebox">Nifti file can not be opened after Jul 2020 commit · Issue #3514 · InsightSoftwareConsortium/ITK · GitHub</a>?</p>

---

## Post #34 by @dzenanz (2022-09-19 16:01 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6454" rel="noopener nofollow ugc">PR 6454</a> should fix many NIFTI-related issues. The latest preview release should have it now.</p>

---
