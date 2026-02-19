---
topic_id: 10497
title: "Nifti Loading Times"
date: 2020-03-02
url: https://discourse.slicer.org/t/10497
---

# Nifti loading times

**Topic ID**: 10497
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/nifti-loading-times/10497

---

## Post #1 by @rprueckl (2020-03-02 15:59 UTC)

<p>Hi,</p>
<p>I encountered very long loading times for some nifti datasets. I don’t know what it is.</p>
<p><strong>The following dataset takes one minute and 15 seconds to load in slicer 4.10.2 (it has about 60MB):</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cf6bed2d5e947f07072690aaaad535fb0080a0b.png" alt="image" data-base62-sha1="6pLEOtaZhluUfpfSOISGTSwMtp9" width="517" height="254"></p>
<p>Mango file header:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee464d77d808b7ffc407dd4a21d86548ea7192e2.png" alt="image" data-base62-sha1="xZSg9NBzR3bmCZEtopCbB4H18Vc" width="362" height="478"></p>
<p><strong>Another dataset takes less than one second to load (about 80MB):</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bb19c944ebd056108295635f6fefd2508c91c4b.png" alt="image" data-base62-sha1="mdkxqioaFP0WEkin7i30w4do079" width="514" height="258"></p>
<p>Mango file header:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/272efbb117680568b2ebd8f2f2d1033bbc37ab9f.png" alt="image" data-base62-sha1="5ADhvgr54P4lxuxa3iOX9w6iHmf" width="371" height="475"></p>
<p>Any ideas where the long loading times could come from? I could provide a dataset for testing if required.</p>

---

## Post #2 by @pieper (2020-03-02 16:17 UTC)

<p>Thanks for the report.  Yes, it would be good if you could provide a way to replicate this on public data.</p>
<p>Also did you try the latest preview version?</p>

---

## Post #3 by @rprueckl (2020-03-03 11:28 UTC)

<p>In the latest preview version, the problem cannot be reproduced.<br>
As I am working with the sources of 4.10.2 for my project, it would be very interesting what was changed for the problem to be gone as I will have to apply the solution as a patch in my version. I can go through the commits myself, I just would need a hint where to start my search. Thanks</p>

---

## Post #4 by @pieper (2020-03-03 12:43 UTC)

<p>Interesting - thanks for testing and reporting.</p>
<p>4.10.2 uses an <a href="https://github.com/Slicer/Slicer/blob/v4.10.2/SuperBuild/External_ITK.cmake#L56">older version of ITK</a> for file IO, and probably a lot has changed.  You could go back and see if the problem could be reproduced in pure ITK and then perhaps backport whatever changes are needed.  But more sustainable long-term (and maybe easier) would be to port your project to the latest Slicer.</p>

---

## Post #5 by @rprueckl (2020-03-04 12:28 UTC)

<p>Thanks, I found the issue. Here some references:</p>
<aside class="quote" data-post="1" data-topic="5312">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/gipl-files-freezes-slicer/5312">Gipl files freezes slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I was given two volumes in gipl format (image and labelmap), that I can open with ITKsnap without any problem. When I drag and drop them into Slicer, first it suggests to load them as ‘Scalar Overlay’ as oppose to ‘Volume’.  Regardless of what’s chosen, Slicer stalls. This happens with both stable 4.10 and r27623 on windows 10. 
Same volumes exported as NRRD from ITK-Snap loads fine.
  </blockquote>
</aside>
<aside class="onebox githubissue" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/issues/388#issue-397178164">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/388#issue-397178164" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/388#issue-397178164" target="_blank" rel="noopener nofollow ugc">Extermely slow loading of image files due to GDCMImageIO::CanReadFile</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-01-09" data-time="01:56:50" data-timezone="UTC">01:56AM - 09 Jan 19 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2019-01-14" data-time="22:12:00" data-timezone="UTC">10:12PM - 14 Jan 19 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:Performance
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          area:IO
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### Description

Some images take extremely long time to load because GDCMImag<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">eIO::CanReadFile takes several minutes.

### Steps to Reproduce

Download this image:
https://1drv.ms/u/s!Arm_AFxB9yqHtrg3be4uEYghv0JPSw

Using just ITK:
1. Load image file linked above using itk::ImageFileReader

Using 3D Slicer:
1. Drag and drop the image file linked above to the application window
2. Select "Volume" in Description column
3. Click OK

### Expected behavior

The file is loaded within a few seconds.

### Actual behavior

The file is loaded in about 5 minutes.

### Reproducibility

100% with the file linked above.

### Versions

4.13

### Environment

Windows10, VS2015

### Additional Information

Originally reported by a Slicer user here: https://discourse.slicer.org/t/gipl-files-freezes-slicer/5312/3</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/commit/19fa58feb02bfd45154e811d0e13510787e2adfb#diff-824229b4fd5f76e67acd43acc54fdae2">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/19fa58feb02bfd45154e811d0e13510787e2adfb#diff-824229b4fd5f76e67acd43acc54fdae2" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/19fa58feb02bfd45154e811d0e13510787e2adfb" target="_blank" rel="noopener nofollow ugc">PERF: GDCM &amp; DCMTK CanRead fails very slowly for non-DICOM files.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-01-14" data-time="22:11:59" data-timezone="UTC">10:11PM - 14 Jan 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/hjmjohnson" target="_blank" rel="noopener nofollow ugc">
          <img alt="hjmjohnson" src="https://avatars.githubusercontent.com/u/313970?v=4" class="onebox-avatar-inline" width="20" height="20">
          hjmjohnson
        </a>
      </div>

      <div class="lines" title="changed 3 files with 195 additions and 12 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/19fa58feb02bfd45154e811d0e13510787e2adfb" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+195</span>
          <span class="removed">-12</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">NOTE: DCMTK and GDCM demonstrate the same behavior with certain
      non-DICOM <span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/commit/19fa58feb02bfd45154e811d0e13510787e2adfb" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">files that have byte patterns similar to DICOM

Some images take extremely long time to load because
DCMTKImageIO::CanReadFile &amp; GDCMImageIO::CanReadFile takes several
minutes to fail.  This is due to DCMTK's and GDCM's default behavior of
trying to read non-compliant dicom files that do not have the required
DICM header.

Add more extensive testing about the structure of the file to determine
if it looks like a dicom file.  Previous testing only looked to see if the
files without preables had values of 2 or 8 as the first byles of the file,
but that resulted in many false positives.

This implementation looks at all the SOP Instances that start with 2 or 8
to ensure that the proper dicom structure is found.

This resolves #388.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2020-03-04 13:45 UTC)

<p>Note that we will soon (in maybe a couple of weeks) release Slicer-5 and deprecate Slicer-4.10. So, I would not recommend to spend time with backporting any fixes, etc. to Slicer-4.10 but rather spend that time with updating to latest Slicer-4.11 (that will become Slicer-5) and test/fix things.</p>

---

## Post #7 by @rprueckl (2020-03-04 14:02 UTC)

<p>Yes, thanks for the hint.</p>

---
