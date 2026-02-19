---
topic_id: 1746
title: "Dwi Loading From Dicom"
date: 2017-12-30
url: https://discourse.slicer.org/t/1746
---

# DWI loading from DICOM

**Topic ID**: 1746
**Date**: 2017-12-30
**URL**: https://discourse.slicer.org/t/dwi-loading-from-dicom/1746

---

## Post #1 by @lassoan (2017-12-30 22:33 UTC)

<p>I’ve tried to load an MRI study from DICOM that contained DWI series (Slicer 4.8.1 on Windows). Although I’ve installed SlierDMRI extension, the series was still loaded using scalar volume importer and appeared garbled.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77dc61475e9028d2910211d4a53affae0a59ef32.png" data-download-href="/uploads/short-url/h6kYOKPbJCKA64BfX68lkYezL6W.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77dc61475e9028d2910211d4a53affae0a59ef32_2_494x500.png" alt="image" data-base62-sha1="h6kYOKPbJCKA64BfX68lkYezL6W" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77dc61475e9028d2910211d4a53affae0a59ef32_2_494x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77dc61475e9028d2910211d4a53affae0a59ef32.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77dc61475e9028d2910211d4a53affae0a59ef32.png 2x" data-dominant-color="666571"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">635×642 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this behavior expected? There used to be a DICOM importer plugin for diffusion data but it seems that it is not available in 4.8.1.</p>

---

## Post #2 by @ihnorton (2017-12-31 01:05 UTC)

<p>Can you please try DWIConvert and let me know if there is a problem loading directly?</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There used to be a DICOM importer plugin for diffusion data but it seems that it is not available in 4.8.1.</p>
</blockquote>
</aside>
<p>I’m not sure where this discussion was (maybe MultiVolumeImporter), but we removed it from Slicer base because there were several complaints about it interfering with other plugins – I think either you or Andrey asked to remove it.</p>
<p>I’ll take another look at putting it into SlicerDMRI. DWIConvert has been refactored quite a bit for library use, so maybe now it is feasible to hook in to the heuristics there to get an accurate response (the existing code did not work very well for Siemens, which requires looking into the private header for a large percent of images).</p>

---

## Post #3 by @lassoan (2017-12-31 01:51 UTC)

<p>I’ve tried DWIConvert. On the DICOM DVD I had my data in 7 subfolders.</p>
<ul>
<li>When I specified the parent folder, the import failed (no files in the parent folder).</li>
<li>Then I copied all files into a single folder and tried to import that. I got <code>LoadFromDisk not relevant</code> error.</li>
<li>After that I tried each of the 7 directories one by one. Import failed with the same message as above (<code>LoadFromDisk not relevant</code>).</li>
</ul>
<pre>Diffusion-weighted DICOM Import (DWIConvert) standard error:

Exception creating converter 
itk::ExceptionObject (00000070D358D430)
Location: "unknown" 
File: D:\D\P\Slicer-481-package\BRAINSTools\DWIConvert\GenericDWIConverter.cxx
Line: 13
Description: itk::ERROR:  LoadFromDisk not relevant
</pre>
<p>These may be all user errors, I just could not figure out how to use this module.</p>
<p>Fortunately, this data set was anonymized and made available publicly, so you can try to import it, too: <a href="https://1drv.ms/f/s!Arm_AFxB9yqHsOArBhZiJ2HPqRA9Cg">https://1drv.ms/f/s!Arm_AFxB9yqHsOArBhZiJ2HPqRA9Cg</a></p>

---

## Post #4 by @lassoan (2017-12-31 01:58 UTC)

<p>The DICOM importer plugin is very useful: we could then avoid painful selection of multiple directories or merging of directories; and would give a single interface for loading all kinds of data from DICOM.</p>
<p>It was a good decision to remove it from the core, but it should be added to SlicerDMRI - the same way as special radiation therapy importers are in SlicerRT extension, and 4D cardiac ultrasound importers are in SlicerHeart. There is very little chance that people who are not interested in diffusion imaging will install SlicerDMRI and then try to load non-diffusion data set that SlicerDMRI will recognize; and if it happens then you can tune the SlicerDMRI importer code any time, without modifying Slicer core. The plugin that worked in Slicer core, should work without any modification in SlicerDMRI extension. You can have a look at SlicerRT or SlicerHeart to see how DICOM plugins are registered.</p>

---

## Post #5 by @ihnorton (2018-01-02 21:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve tried DWIConvert. On the DICOM DVD I had my data in 7 subfolders.</p>
</blockquote>
</aside>
<p>Thanks for sharing the data. The DWI sequence is 1866:</p>
<pre><code class="lang-auto">BWH003265:1861 inorton$ for f in *; do echo $f; dcmdump $f/$(ls $f | head -n 1) | grep Description; done
1863
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [localizer]                              #  10, 1 SeriesDescription
1864
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [SAG TSE T1]                             #  10, 1 SeriesDescription
1865
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [AX TSE T2 H.R.]                         #  14, 1 SeriesDescription
1866
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [AX DWI]                                 #   6, 1 SeriesDescription
1867
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [AX DWI_ADC]                             #  10, 1 SeriesDescription
1868
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [AX SPACE]                               #   8, 1 SeriesDescription
1869
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [COR MPR]                                #   8, 1 SeriesDescription
</code></pre>
<p>But the following basic tags are empty: Manufacturer <code>(0008,0070)</code> and Siemens SoftwareVersion <code>(0018, 1020)</code> so DWIConvert cannot identify the dataset, and falls back to a generic reader implementation, which fails. Certainly the error message could be improved!</p>
<p>However, this data does not have any diffusion-weighting tags, and there are only three volumes total in series 1866 ([1] looks like baseline, [2,3] look like gradient-weighting). So, it could not be used to calculate diffusion tensors or higher-order models.</p>
<p>I tried converting with dcm2nii, which does produce a valid 3-volume NIfTI, but does not extract any diffusion-weighting information (as expected since there are no tags available).</p>
<p>It looks like this data was very aggressively anonymized. If you have more information about the scanner or other details then we could figure out if the raw data would be supported.</p>

---

## Post #6 by @ihnorton (2018-01-02 21:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The DICOM importer plugin is very useful: we could then avoid painful selection of multiple directories or merging of directories; and would give a single interface for loading all kinds of data from DICOM.</p>
</blockquote>
</aside>
<p>Ok, we will put it back in. Hopefully I can pass an error message pointing to DWIConvert through the plugin interface, but I’ll ask questions about that if needed.</p>

---

## Post #7 by @ihnorton (2018-01-02 21:43 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="5" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Certainly the error message could be improved!</p>
</blockquote>
</aside>
<p>I opened the following issue to capture this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/BRAINSia/BRAINSTools/issues/361">
  <header class="source">

      <a href="https://github.com/BRAINSia/BRAINSTools/issues/361" target="_blank" rel="noopener">github.com/BRAINSia/BRAINSTools</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/BRAINSia/BRAINSTools/issues/361" target="_blank" rel="noopener">Improve error message on missing tags-&gt;fallback to generic-&gt;failure</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-01-02" data-time="21:42:51" data-timezone="UTC">09:42PM - 02 Jan 18 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2018-05-09" data-time="13:27:27" data-timezone="UTC">01:27PM - 09 May 18 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/ihnorton" target="_blank" rel="noopener">
          <img alt="ihnorton" src="https://avatars.githubusercontent.com/u/327706?v=4" class="onebox-avatar-inline" width="20" height="20">
          ihnorton
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          U3:Low
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">There is a [discussion and example data](https://discourse.slicer.org/t/dwi-load<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ing-from-dicom/1746) on the Slicer forum where some data (I think Siemens originally) fails to convert due to missing tags from aggressive anonymization. DWIConvert falls back to the generic reader, which also fails. The error shown could be more informative:

```
Diffusion-weighted DICOM Import (DWIConvert) standard error:

Exception creating converter 
itk::ExceptionObject (00000070D358D430)
Location: "unknown" 
File: D:\D\P\Slicer-481-package\BRAINSTools\DWIConvert\GenericDWIConverter.cxx
Line: 13
Description: itk::ERROR:  LoadFromDisk not relevant
```

Ideally DWIConvert could give some descriptive information rather than the exception, and maybe hints/suggestions about common causes of errors (missing tags, anonymization, etc.)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @lassoan (2018-01-03 04:05 UTC)

<p>I’ve anonymized the data set with <a href="http://mircwiki.rsna.org/index.php?title=The_CTP_DICOM_Anonymizer#Accessing_the_CTP_Anonymizer_Configurator">CTP</a>, with default settings. I can access the original data, if needed.</p>
<p>This is a brain CT+MRI data set of the same patient, which has been made available as “CT-MR Brain” data set in sample data module in recent nightly builds. It is also available here: <a href="http://slicer.kitware.com/midas3/folder/4996">http://slicer.kitware.com/midas3/folder/4996</a>. Do you think there can be anything valuable in the diffusion weighted image that would be worth added to the published data set? If yes, then we can continue working on this, re-anonymizing the data set in a way that preserves necessary information.</p>

---

## Post #9 by @ihnorton (2018-01-03 14:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve anonymized the data set with CTP, with default settings. I can access the original data, if needed.</p>
</blockquote>
</aside>
<p><a href="https://gist.github.com/ihnorton/29fd5eec57c317a5796cacb28938e3ad">Here</a> is the CTP script I used recently for Siemens DWI data. After anonymization, there were some warnings from <code>dciodvfy</code>, and one of our vendor collaborators still thought it was too strict – but four independent software were able to read the data as DWI. Note that some of the preserved tag ranges are Siemens private headers. I don’t recall seeing private data in the CSA headers in the past, but I still do a manual audit of all headers before release because I don’t know of any guarantees about whether protected information is stored in the private tags.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you think there can be anything valuable in the diffusion weighted image that would be worth added to the published data set?</p>
</blockquote>
</aside>
<p>If the data is as I described above (1 b0, 2 gradient) then it is probably not worth extra effort (can’t calculate ADC even – and tensors require minimum 6 directions). But if there is a full acquisition then I’m always grateful for more sample data, especially if the anonymized DICOM can be shared too. I don’t think we have any MR + DWI-MR + CT datasets, so that would be nice to have.</p>

---

## Post #10 by @lassoan (2018-01-04 16:44 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="9" data-topic="1746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>If the data is as I described above (1 b0, 2 gradient) then it is probably not worth extra effort</p>
</blockquote>
</aside>
<p>We only have those series that I shared, so I’ll not upload the DWI series to the data store then.</p>

---
