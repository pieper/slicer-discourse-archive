# Convert single files into one .nii

**Topic ID**: 5407
**Date**: 2019-01-17
**URL**: https://discourse.slicer.org/t/convert-single-files-into-one-nii/5407

---

## Post #1 by @siaeleni (2019-01-17 21:55 UTC)

<p>Hi,</p>
<p>I have multiple single .ima files. These contain single slices info.<br>
What I want to achieve is to merge all these into one .nii file.</p>
<p>What is the best way to do that?<br>
Thanks</p>

---

## Post #2 by @Frederic (2019-01-17 22:17 UTC)

<p>Dear Helen,<br>
You could use <a href="http://people.cas.sc.edu/rorden/mricron/dcm2nii.html" rel="nofollow noopener">dcm2nii</a>.<br>
Best.</p>

---

## Post #3 by @siaeleni (2019-01-17 22:25 UTC)

<p>Thanks Frederic,<br>
I want to use python for this task, can I achieve it using dcm2nii?</p>

---

## Post #4 by @Frederic (2019-01-17 22:36 UTC)

<p>Not directly, but yest it’s possible, for example by a thing like that:<br>
After that you load MRIcroGL (dcm2niix)</p>
<blockquote>
<p>import os<br>
command1 = “dcm2nix /YourDirectory/data.IMA”<br>
os.system(command1)</p>
</blockquote>

---

## Post #5 by @Chris_Rorden (2019-01-18 14:15 UTC)

<p>The <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener"><strong>Alternatives</strong> section of the dcm2niix page lists several tools for converting DICOM images to NIfTI</a>. The <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener"><strong>Links</strong> section</a> lists several tools that exploit dcm2niix, many of these are Python-based scripts. I think <a href="https://github.com/icometrix/dicom2nifti" rel="nofollow noopener">dicom2nifti</a> would be my recommendation for  Python-based converter. In my experience, most of the tools listed in the alternatives section do pretty well for most modalities, but you want to carefully validate the converter you have special modalities. In particular, CT scans can have unequal slice spacing and gantry tilt while DWI scans have gradient information. If you are planning to use Slicer in particular, you may want to consider scripting DWIconvert, as is used my most Slicer users and therefore heavily tested. The nice <a href="https://github.com/pieper/nrrdify" rel="nofollow noopener">nrrdify Python script shows how to use DWIconvert to create NRRD images</a> and I think it could be easily adapted if you want NIfTI images.</p>

---

## Post #6 by @lassoan (2019-01-18 14:38 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="5" data-topic="5407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>DWIconvert, as is used my most Slicer users</p>
</blockquote>
</aside>
<p>It is used for DWI import in Slicer, but various DICOM plugins are used for other information objects.</p>
<p>How dcm2niix can handle 4D CTs with unequal spacing, missing and unaligned slices, and gantry tilt? Does dcm2niix support CT reconstruction based on different DICOM tags (frame time, heart cycle phase, various vendor-specific tags)? Can dcm2niix can load multiple series as a 4D volume? If there are many options for interpreting a 4D data set, how dcm2niix tells the user the available options (and probability of which ones are thr most likely correct interpretations) and how the user can choose between those? Slicer has a sophisticated plugin system that can deal with all these, but it would be nice if some of this complex logic could be offloaded to external libraries.</p>

---

## Post #7 by @ihnorton (2019-01-18 14:50 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="3" data-topic="5407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>I want to use python for this task, can I achieve it using dcm2nii?</p>
</blockquote>
</aside>
<p>You can run dcm2niix via <a href="https://github.com/nipy/heudiconv">heudiconv</a> or <a href="https://github.com/nipy/nipype">nipype</a>.</p>

---

## Post #8 by @pieper (2019-01-18 15:09 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> and a group of us researched the various options for dicom conversion a while back and collected our notes <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/" rel="nofollow noopener">on this project page</a> .  There’s also a <a href="https://github.com/QIICR/dcmheat" rel="nofollow noopener">docker based test environment</a> that runs the various tools (slicer, freesurfer, dcm2niix, etc) and compares the results.</p>
<p>As a general rule, it’s best if you don’t need to perform lossy conversions, so keeping the original dicom data is desirable.  Also storing derived data in dicom is the method many of us prefer (or are at least working towards).</p>

---

## Post #9 by @Chris_Rorden (2019-01-19 12:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I recognize Slicer has several strategies for handling DICOMs. My response was specific to the original post regarding converting files to a single .nii file.</p>
<p>With regards to special situations encountered with DICOMs, you may want to look at the samples that can be downloaded from the <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage" rel="noopener nofollow ugc">dcm2niix web page</a>. This provides exemplars of archival images, CT scans, DWI scans, and special situations.</p>
<p>The web page also describes how dcm2niix handles various situations, including those described below.</p>
<blockquote>
<p>How dcm2niix can handle 4D CTs with unequal spacing, missing and unaligned slices, and gantry tilt?</p>
</blockquote>
<p>The NIfTI format requires equal slice spacing, while CT scans are sometimes acquired with variable slice spacing (e.g. a lot of slices near the brain stem and wider spacing for more superior locations). In this case dcm2niix generates a warning and creates an interpolated volume with equal slice spacing that has ‘_Eq’ appended to the file name</p>
<p>Unaligned slices are saved as separate volumes.</p>
<p>Gantry tilt is sometimes seen in CT scans. dcm2niix reports this skew in the NIfTI s-form. However, while the NIfTI format supports sheared volumes using the sform, most tools require rectangular volumes (e.g. ITK-based tools like slicer). Therefore, if gantry tilt is detected, dcm2niix also generates an interpolated volume with ‘_Tilt’ appended to the filename.</p>
<blockquote>
<p>Does dcm2niix support CT reconstruction based on different DICOM tags (frame time, heart cycle phase, various vendor-specific tags)?</p>
</blockquote>
<p>Most dcm2niix users work with MRI scans, and so it has been most thoroughly tested in that modality If you have CT examples with these features and dcm2niix does not work as expected, you can generate an issue on the <a href="https://github.com/rordenlab/dcm2niix" rel="noopener nofollow ugc">dcm2niix GitHub page</a>. A command line option allows you to specify if varying X-ray exposures should be stacked in a single volume or saved as separate volumes, as different users prefer different behavior. In general, different properties (for MRI: echo time, image type, trigger time, etc) are saved as separate files as described below.</p>
<blockquote>
<p>Can dcm2niix can load multiple series as a 4D volume?</p>
</blockquote>
<p>In general, separate series are saved as separate files, and this is typically desirable (e.g. for fMRI analyses separate runs are typically saved as separate 4D volumes). An exception is DSC, where Siemens uses separate series for successive volumes. The next release (and current developmental release) of dcm2niix stack these DSC series as a single volume.<br>
Scans of the same series with the same properties are saved as a single 4D volume. Therefore, scans like DSC, fMRI, ASL, DWI, etc are saved as 4D volumes. Separate files are saved for different properties (e.g. type: magnitude, real, imaginary and phase; echo time; trigger delay time, etc.). These situations are described in the<a href="https://github.com/rordenlab/dcm2niix/blob/master/FILENAMING.md" rel="noopener nofollow ugc">dcm2niix file naming</a> page.</p>

---

## Post #10 by @fedorov (2019-01-19 17:12 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="5407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> and a group of us researched the various options for dicom conversion a while back and collected our notes <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/">on this project page </a> . There’s also a <a href="https://github.com/QIICR/dcmheat">docker based test environment </a> that runs the various tools (slicer, freesurfer, dcm2niix, etc) and compares the results.</p>
</blockquote>
</aside>
<p>To be more correct, setting up an environment that packages and tests those tools on a reference sample dataset was the desired goal. Dockers for some of the packages were completed, but the project was never continued after those initial steps.</p>

---

## Post #11 by @lassoan (2019-01-24 21:59 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Thanks a lot for the detailed answer. You’ve done a great job with dcm2niix and nicely implemented all the essential image normalization techniques. We could use your library as a DICOM import plugin in Slicer for some 3D and 4D images, simplifying or replacing current scalar and multivolume plugins. We already have lots of infrastructure developments planned for the near future, but we may get back to this in about a year.</p>

---

## Post #12 by @fedorov (2019-01-24 22:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="5407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We already have lots of infrastructure developments planned for the near future, but we may get back to this in about a year.</p>
</blockquote>
</aside>
<p>A quick but useful initial step could be to provide dcm2niix based DICOM plugin in an extension. I would even avoid superbuilding it, but maybe just pulling a packaged binary from the dcm2niix repo, or letting users install it locally from package, and point to the location of the binary in a setting.</p>

---

## Post #13 by @ihnorton (2019-01-28 22:37 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="5407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>A quick but useful initial step could be to provide dcm2niix based DICOM plugin in an extension.</p>
</blockquote>
</aside>
<p>Please see the following to add an extension (no DICOM browser plugin). We will use this as a dependency for a scripted module within SlicerDMRI, but made the dcm2niix build part a separate extension for reusability.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/pull/1610">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/pull/1610" target="_blank" rel="noopener">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/ExtensionsIndex/pull/1610" target="_blank" rel="noopener">Add SlicerDcm2nii extension</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>ihnorton:slicer_dcm2nii</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2019-01-28" data-time="22:33:38" data-timezone="UTC">10:33PM - 28 Jan 19 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/ihnorton" target="_blank" rel="noopener">
            <img alt="ihnorton" src="https://avatars.githubusercontent.com/u/327706?v=4" class="onebox-avatar-inline" width="20" height="20">
            ihnorton
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 23 additions and 0 deletions">
          <a href="https://github.com/Slicer/ExtensionsIndex/pull/1610/files" target="_blank" rel="noopener">
            <span class="added">+23</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- [x] Extension has a reasonable name (not too general, not too narrow, suggests<span class="show-more-container"><a href="https://github.com/Slicer/ExtensionsIndex/pull/1610" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> what the extension is for)
- [x] Repository name is Slicer+ExtensionName
- [x] Extension description summarizes in 1-2 sentences what the extension is usable (should be understandable for non-experts)
- [x] Extension URL and revision (scmurl, scmrevision) is correct, consider using a branch name (master, release, ...) instead of a specific git has to avoid re-submitting pull request whenever the extension is updated
- [x] Extension icon URL is correct
- [ ] Screenshot URLs (screenshoturls) are correct, contains at least one
- [ ] Homepage URL points to valid webpage containing the following:
  - [ ] Extension name
  - [ ] Short description: 1-2 sentences, which summarizes what the extension is usable for
  - [ ] At least one nice, informative image, that illustrates what the extension can do. It may be a screenshot.
  - [ ] Description of contained modules: at one sentence for each module
  - [ ] Tutorial: step-by-step description of at least the most typical use case, include a few screenshots, provide download links to sample input data set</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="5407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I would even avoid superbuilding it, but maybe just pulling a packaged binary from the dcm2niix repo, or letting users install it locally from package, and point to the location of the binary in a setting.</p>
</blockquote>
</aside>
<p>I set it up to build with superbuild, because (a) it is easy to build, and (b) we want it to have the same host runtime requirements as Slicer – for example, it would be confusing for users if the dcm2niix-provided binaries are built on a newer linux host and don’t run on the same platform as the rest of Slicer.</p>

---
