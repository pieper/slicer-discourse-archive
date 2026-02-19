---
topic_id: 34931
title: "Slicer Crashes While Trying To Load Dicom Files"
date: 2024-03-17
url: https://discourse.slicer.org/t/34931
---

# Slicer crashes while trying to load DICOM files

**Topic ID**: 34931
**Date**: 2024-03-17
**URL**: https://discourse.slicer.org/t/slicer-crashes-while-trying-to-load-dicom-files/34931

---

## Post #1 by @arkinacar (2024-03-17 00:03 UTC)

<p>Hello. I try to load DICOM files in the Slicer, yet it crashes while I’m trying to do so.<br>
I tried both the latest and the stable versions, yet the problem occurred in both.<br>
When I import the folder containing the DICOM files, the series appear on the right side. However, when I try to load them, Slicer crashes.<br>
Can it be problem regarding plugins? I can load jpeg files without any problems.</p>

---

## Post #2 by @lassoan (2024-03-17 00:06 UTC)

<p>Most likely your DICOM files are corrupted (for example, by incorrect anonymization). If the images do not contain patient information then you may share them (upload somewhere and post the link here) and we can have a look and tell what’s wrong with them and how to fix.</p>

---

## Post #3 by @arkinacar (2024-03-17 09:18 UTC)

<p>Ok now. I saw that my DICOM files were not anonymous. So, first, I exported them from my DICOM viewer as anonymous. Yet, I still can’t get them loaded in Slicer.<br>
Here, I share a Google Drive link, including an axial section of chest CT with 362 images.<br>
Thank you so much for your time and thanks in advance.<br>
Please tell me what I do wrong</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1NzTFqbgCKRHL4un8_upbALyUIa5apiI5%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1NzTFqbgCKRHL4un8_upbALyUIa5apiI5%3Fusp%3Ddrive_link&amp;ifkv=ATuJsjwN-hgEMfBiNiD_8plpIS6SI6w_TirobyWVvOm6i37xW_DtV6hbD0KYBh2WTftHAZcg4EHA6g&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1141598184%3A1710667063968212">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1NzTFqbgCKRHL4un8_upbALyUIa5apiI5%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1NzTFqbgCKRHL4un8_upbALyUIa5apiI5%3Fusp%3Ddrive_link&amp;ifkv=ATuJsjwN-hgEMfBiNiD_8plpIS6SI6w_TirobyWVvOm6i37xW_DtV6hbD0KYBh2WTftHAZcg4EHA6g&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1141598184%3A1710667063968212" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1NzTFqbgCKRHL4un8_upbALyUIa5apiI5%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1NzTFqbgCKRHL4un8_upbALyUIa5apiI5%3Fusp%3Ddrive_link&amp;ifkv=ATuJsjwN-hgEMfBiNiD_8plpIS6SI6w_TirobyWVvOm6i37xW_DtV6hbD0KYBh2WTftHAZcg4EHA6g&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1141598184%3A1710667063968212" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2024-03-17 23:24 UTC)

<p>Thank you. I’ve checked the file and it is highly unusual (allocates 32 bits to store a 14-bit image) but probably valid. I’ve submitted a fix to ITK (the library that we use for DICOM loading):</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/pull/4522">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/4522" target="_blank" rel="noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/4522" target="_blank" rel="noopener">Fix 32bits dicom read crash</a>
      </h4>

    <div class="branches">
      <code>InsightSoftwareConsortium:master</code> ← <code>lassoan:fix-32bits-dicom-read-crash</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-03-17" data-time="23:22:29" data-timezone="UTC">11:22PM - 17 Mar 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 2 files with 100 additions and 90 deletions">
          <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/4522/files" target="_blank" rel="noopener">
            <span class="added">+100</span>
            <span class="removed">-90</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fix crash in ITK DICOM reader when attempting to read an unusual but valid DICOM<span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/pull/4522" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> file, which has 32 bits allocated.
Fixes the error reported at https://discourse.slicer.org/t/slicer-crashes-while-trying-to-load-dicom-files/34931/3

## PR Checklist
- [x] No [API changes](https://github.com/InsightSoftwareConsortium/ITK/blob/master/CONTRIBUTING.md#breaking-changes) were made (or the changes have been approved)
- [x] No [major design changes](https://github.com/InsightSoftwareConsortium/ITK/blob/master/CONTRIBUTING.md#design-changes) were made (or the changes have been approved)
- [ ] Added test (or behavior not changed)
- [x] Updated API documentation (or API not changed)
- [x] Added [license](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Utilities/KWStyle/ITKHeader.h) to new files (if any)
- [x] Added Python wrapping to new files (if any) as described in [ITK Software Guide](https://itk.org/ItkSoftwareGuide.pdf) Section 9.5
- [x] Added [ITK examples](https://github.com/InsightSoftwareConsortium/ITKSphinxExamples) for all new major features (if any)

Refer to the [ITK Software Guide](https://itk.org/ItkSoftwareGuide.pdf) for
further development details if necessary.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It’ll probably take a couple of days to get the fix into Slicer.</p>

---

## Post #5 by @lassoan (2024-03-18 15:54 UTC)

<p><a class="mention" href="/u/arkinacar">@arkinacar</a> can I add one of the slices of the image you shared to the test data sets of ITK toolkit? (that would allow all automatic testing to check this unusual but probably valid DICOM file variant)</p>

---

## Post #6 by @arkinacar (2024-03-18 16:03 UTC)

<p>Sure! As long as the problem is solved, it is np really</p>
<p>Android için <a href="https://aka.ms/AAb9ysg" rel="noopener nofollow ugc">Outlook</a> edinin</p>

---

## Post #7 by @arkinacar (2024-03-27 19:55 UTC)

<p>Hello again. Is there any update regarding the issue?</p>

---

## Post #8 by @lassoan (2024-03-27 20:34 UTC)

<p>The problem was in GDCM, used by ITK, used by Slicer. I’ve fixed the issue in GDCM, the fix was merged into ITK, the last step is to merge into Slicer. Since Slicer’s ITK has not been updated for a while, it’ll probably take a couple of more days. So, probably the fix will be available in the Slicer Preview Release late next week.</p>

---
