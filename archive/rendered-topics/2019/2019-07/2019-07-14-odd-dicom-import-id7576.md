---
topic_id: 7576
title: "Odd Dicom Import"
date: 2019-07-14
url: https://discourse.slicer.org/t/7576
---

# Odd DICOM import

**Topic ID**: 7576
**Date**: 2019-07-14
**URL**: https://discourse.slicer.org/t/odd-dicom-import/7576

---

## Post #1 by @Amine (2019-07-14 21:18 UTC)

<p>slicer versions: 4.10.1 ; 4.11<br>
windows 10</p>
<p>this particular dicom fails to import and shows up as two copies of the content under the same volume with the original resolution (images are shrunk up to fit in the original resolution)<br>
i used Microdicom program to export the individual slices then reimported them to slicer and manually entered spacing and slice thickness in order to get the correct volume.<br>
Here is the problematic file:</p>
<p><a href="https://drive.google.com/open?id=1RgqhZjg6hXBfXKWZYmBYJOfFyq_XxxiS" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/open?id=1RgqhZjg6hXBfXKWZYmBYJOfFyq_XxxiS</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7da74cd042ea6d83089394324c90bf81156216d.jpeg" data-download-href="/uploads/short-url/x54kPJeaTBXPia15iKCEB7xHgS1.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7da74cd042ea6d83089394324c90bf81156216d_2_687x499.jpeg" alt="PNG" data-base62-sha1="x54kPJeaTBXPia15iKCEB7xHgS1" width="687" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7da74cd042ea6d83089394324c90bf81156216d_2_687x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7da74cd042ea6d83089394324c90bf81156216d_2_1030x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7da74cd042ea6d83089394324c90bf81156216d.jpeg 2x" data-dominant-color="4E4A4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1230×895 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Chris_Rorden (2019-07-14 22:25 UTC)

<p>Different slices in this series report different  X-Ray Exposures. I suspect this will cause most tools to segment these as different images. For example, if you run dcm2niix with default settings:</p>
<blockquote>
<p>$dcm2niix_stable ~/tst/slicer7576/<br>
Chris Rorden’s dcm2niiX version v1.0.20190410  (JP2:OpenJPEG) (JP-LS:CharLS) Clang8.1.0 (64-bit MacOS)<br>
Found 120 DICOM file(s)<br>
…<br>
slices not stacked: X-Ray Exposure varies (exposure 20, 24; number 1, 1). Use ‘merge 2D slices’ option to force stacking</p>
</blockquote>
<p>You can convert this series successfully by using dcm2niix’s “merge” argument (“-m y”). Use this argument with caution - we often want to segment images with different exposures, echo times, etc as these can influence contrast.</p>
<blockquote>
<p>$dcm2niix -m y ~/tst/slicer7576/<br>
Chris Rorden’s dcm2niiX version v1.0.20190410  (JP2:OpenJPEG) (JP-LS:CharLS) Clang8.1.0 (64-bit MacOS)<br>
Found 120 DICOM file(s)<br>
Image Decompression is new: please validate conversions<br>
Convert 120 DICOM as /Users/rorden/tst/slicer7576/2_5.3_THORACO-ABDOMINO-PELVIEN (512x512x120x1)<br>
Conversion required 5.730815 seconds (5.719810 for core code).</p>
</blockquote>

---

## Post #3 by @lassoan (2019-07-14 22:36 UTC)

<p>Slicer uses DICOM reader of ITK library and it seems that this reader cannot cope with the compression method of your image. Please report the problem at <a href="https://discourse.itk.org/" rel="nofollow noopener">https://discourse.itk.org/</a>.</p>
<p>Robustness of dcm2niix is very impressing, so if we keep having problem’s with ITK’s DICOM reader then maybe we’ll add DICOM plugin that allows loading of images using dcm2niix.</p>

---

## Post #4 by @lassoan (2019-07-14 23:09 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Would you be able to add an “examine” option to dcm2niix, which would just quickly return what files dcm2niix would create (without actually creating those files, to save time)?</p>
<p>Slicer performs this “examine” step for each DICOM series with all of its DICOM readers to see which ones can interpret it. The reader that reports the highest confidence will be used by default (in advanced mode, user can freely choose from the list of loadable items).</p>
<p>Ideally, dcm2niix would also provide for each output file a confidence value (between 0.0-1.0 to indicate how probable is that dcm2niix would load the file correctly), a short name (that describes what the file will contain), and “additional comments” (text describing warning messages or any additional information could be relevant for the user).</p>

---

## Post #5 by @Chris_Rorden (2019-07-14 23:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> you may want to look at <a href="https://github.com/rordenlab/dcm2niix/issues/252" rel="noopener nofollow ugc">issue 252</a>.  Both FSLeyes and MRIcroGL use the ‘-n -1’ argument to report how files would be segmented based on all the other arguments. In additon, some vendors have a lot of rounding errors in reporting these values, so the values reported in the DICOM vary even when they are supposed to be the same (hence dcm2niix allows a tolerance for these). If you want to suggest the algorithm used to further estimate outputs, consider posting an issue on the dcm2niix Github page. The merging of echo-times (MRI) and X-ray exposure (CT) is vexing, as some users expect these to be combined while others want them kept separate. A heuristic might be to assume that files should be merged if each slice position is unique, and not to merge if positions repeat across these.</p>
<blockquote>
<p>$ dcm2niix_stable -f %s_%p -n -1 0 -m n ~/dcm_qa_uih</p>
<p>Chris Rorden’s dcm2niiX version v1.0.20190410 (JP2:OpenJPEG) (JP-LS:CharLS) Clang8.1.0 (64-bit MacOS)</p>
<p>Found 388 DICOM file(s)</p>
<p>12 /Users/rorden/dcm_qa_uih/12_dti_tra_dir16_PA_rot</p>
<p>/Users/rorden/dcm_qa_uih/In/DTI_132225/dti_tra_dir16_PA_rot_SaveBySlc__134057/00000001.dcm</p>
<p>2 /Users/rorden/dcm_qa_uih/2_t1_gre_fsp_3d_sag</p>
<p>/Users/rorden/dcm_qa_uih/In/DTI_132225/t1_gre_fsp_3d_sag__132750/00000001.dcm</p>
<p>6 /Users/rorden/dcm_qa_uih/6_dti_tra_dir16_PA</p>
<p>/Users/rorden/dcm_qa_uih/In/DTI_134434/dti_tra_dir16_PA_SaveBySlc__135612/00000001.dcm</p>
<p>12 /Users/rorden/dcm_qa_uih/12_dti_tra_dir16_PA_rot</p>
<p>/Users/rorden/dcm_qa_uih/In/DTI_134434/dti_tra_dir16_PA_rot_SaveBySlc__140451/00000001.dcm</p>
<p>2 /Users/rorden/dcm_qa_uih/2_t1_gre_fsp_3d_sag</p>
<p>/Users/rorden/dcm_qa_uih/In/DTI_134434/t1_gre_fsp_3d_sag__134917/00000001.dcm</p>
<p>9 /Users/rorden/dcm_qa_uih/9_dti_tra_dir16_AP</p>
<p>/Users/rorden/dcm_qa_uih/In/DTI_134434/dti_tra_dir16_AP_SaveBySlc__140028/00000001.dcm</p>
<p>Conversion required 1.252159 seconds (0.661013 for core code).</p>
</blockquote>

---

## Post #6 by @lassoan (2019-07-15 00:09 UTC)

<p>Thanks for the quick response.</p>
<p>I planned to ask for loading from file list later, but did not want to ask for too much at once - it seems <a href="https://github.com/rordenlab/dcm2niix/issues/252" rel="nofollow noopener">#252</a> provides a solution for that.</p>
<p>It is not entirely clear if we would need to re-run dcm2niix several times with all commonly useful loading option combinations to map out what dcm2niix can load, as it may take too long time.</p>
<p>Parsing of dcm2niix output does not seem straightforward either, because warning messages break the structure. Maybe with some heuristics it could work, though: e.g., consider all output lines that do not contain tab characters as warnings. If there are warnings then set confidence to 0.5, if there are no warnings then to 0.9. Warning messages could be used as additional comments.</p>

---

## Post #7 by @Chris_Rorden (2019-07-15 00:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> with regards to ITK support, the Transfer Syntax is 1.2.840.10008.1.2.4.91, which means lossy JPEG-2000 compression. OpenJPEG is the only open source library that can <a href="https://www.mccauslandcenter.sc.edu/crnl/tools/jpeg-formats" rel="nofollow noopener">reliably</a> read these images at high precision. The dcm2niix code shows how to call this library. The Python-based <a href="https://github.com/icometrix/dicom2nifti" rel="nofollow noopener">dicom2nifti</a> shows a different approach - if calls <a href="http://gdcm.sourceforge.net/html/gdcmconv.html" rel="nofollow noopener">gdcmconv</a> to decode compressed DICOMs to raw DICOM (e.g. from the command line ‘gdcmconv -w IM-0001-0001.dcm raw.dcm’).</p>
<p>In these examples, JPEG-2000 achieves an impressive 5:1 compression ratio. However, I would personally suggest users avoid compressed DICOM transfer syntaxes: the DICOM standard only requires DICOM compliant tools to read the uncompressed data, so while one can generate a valid compressed DICOM image, there is no guarantee it will be supported by various DICOM utilities in your tool chain.</p>
<p>As an aside, my own personal opinion is that  lossy JPEG-2000 is particularly ill-suited to medical imaging. The reason is that it is so “good” from the perspective of human observers, avoiding the blocking and other artifacts of classic JPEG. As one increases compression with JPEG-2000 the images exhibit a subtle blurring. Even highly compressed images look great to a human viewer. However, in my experience it is often the high frequency edges that are crucial to diagnoses, e.g. signs of hippocampal sclerosis. One assumes the moderate compression applied in the sample images retains such attributes, but loss in fidelity will be hard to detect.</p>
<p>The <a href="https://github.com/SlicerDMRI/SlicerDcm2nii" rel="nofollow noopener">SlicerDcm2nii</a> extension should help Slicer users in the rare cases where the in-built ITK library fails. The current integration of the ITK libraries in Slicer is so good that I think it would be a major engineering feat to use a different tool. My sense is Slicer users report the rare instances where the ITK library fails, yet the vast number of successful conversions are unreported.</p>
<p>I do not think there is any perfect DICOM converter. This is due to the inherent complexity of DICOM, the fact that different vendors have interpreted it differently, the reality that vendors are evolving their interpretations, and that over the years each vendor has released buggy DICOMs that do not strictly conform to the standard. I suspect that if Slicer relied on dcm2niix rather than ITK, you would be made aware of the instances where dcm2niix fails.</p>

---

## Post #8 by @Chris_Rorden (2019-07-15 00:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I think that “-m” is the only dcm2niix argument that influences how DICOM images are combined or segmented. The other arguments influences attributes of the output files (name, format, type of scaling) but do not influence the number of files generated. The only other option that alters the number of files generated is ‘-i’ (ignore) which will skip files that are 2D, derived or localizers.</p>
<p>I agree with your comment that the warnings could be denoted better. This could actually be changed pretty easily, as all text output is one of three types:</p>
<ol>
<li>
<strong>printMessage()</strong>: refers to typical commentary (which one can control with verbosity).</li>
<li>
<strong>printWarning()</strong> refers to an ambiguity that the user should inspect.</li>
<li>
<strong>printError()</strong> is used when their is an exception that terminates conversion.</li>
</ol>
<p>These 3 messages are all piped through the unit print.h, so it would be easy to add different markers to denote each type of error. As you note, perhaps a space could precede every warning, a tab could precede every warning, and an asterisk could mark an error (errors are already easy to detect as they change the return value of the executable).</p>
<p>By the way <a href="https://github.com/jonclayden/divest" rel="nofollow noopener">divest</a> already modifies the print.h file so that messages generated for R are prefixed as  <em>[dcm2niix info]</em>, <em>[dcm2niix WARNING]</em>, and <em>[dcm2niix ERROR]</em>.</p>

---

## Post #9 by @Amine (2019-07-15 00:43 UTC)

<p>Issue reported on ITK forums</p><aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/distorted-dicom-import-on-slicer/2043">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/distorted-dicom-import-on-slicer/2043" target="_blank" rel="noopener nofollow ugc" title="12:39AM - 15 July 2019">ITK – 15 Jul 19</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8496cb21967af99be359755e434d0b0c0c70456d.png" class="thumbnail onebox-avatar" width="32" height="32">

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/distorted-dicom-import-on-slicer/2043" target="_blank" rel="noopener nofollow ugc">Distorted DICOM import on Slicer</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #12A89D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Beginner Questions</span>
        </span>
      </span>
  </div>
</div>

  <p>Hi, coming from 3D Slicer Forum, i was advised to post this issue here  There is a link to the original thread with more info:      DICOM file:  https://drive.google.com/drive/folders/1RgqhZjg6hXBfXKWZYmBYJOfFyq_XxxiS  This file loads up oddly as...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @lassoan (2019-07-15 14:11 UTC)

<p>I’ve implemented a DICOM plugin to allow loading volumes using dcm2niix from the Slicer DICOM browser as usual. After the <a href="https://github.com/SlicerDMRI/SlicerDcm2nii/pull/5">pull request</a> is merged, the dcm2niix plugin will show up in the DICOM browser if users install SlicerDcm2nii extension.</p>
<p>Example of loadables produces for a corrupted series (I’ve removed a few slices from the series):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e24848ff5e1c60dc19dc6379672b195c597c2795.png" data-download-href="/uploads/short-url/whMMgGpn4JkQ6lk9qo8aqgMjK85.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e24848ff5e1c60dc19dc6379672b195c597c2795_2_690x371.png" alt="image" data-base62-sha1="whMMgGpn4JkQ6lk9qo8aqgMjK85" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e24848ff5e1c60dc19dc6379672b195c597c2795_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e24848ff5e1c60dc19dc6379672b195c597c2795_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e24848ff5e1c60dc19dc6379672b195c597c2795_2_1380x742.png 2x" data-dominant-color="C7CFD9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2090×1124 586 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have only tested this with regular scalar volumes, but anything that dcm2niix can convert and <code>slicer.util.loadVolume</code> can load should work.</p>

---
