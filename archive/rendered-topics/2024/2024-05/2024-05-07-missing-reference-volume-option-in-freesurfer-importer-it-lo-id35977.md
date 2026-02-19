---
topic_id: 35977
title: "Missing Reference Volume Option In Freesurfer Importer It Lo"
date: 2024-05-07
url: https://discourse.slicer.org/t/35977
---

# Missing “Reference Volume” option in FreeSurfer Importer (it looks like version 5.6 onwards)

**Topic ID**: 35977
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/missing-reference-volume-option-in-freesurfer-importer-it-looks-like-version-5-6-onwards/35977

---

## Post #1 by @Nis175 (2024-05-07 22:34 UTC)

<p>Dear 3D Slicer Team,</p>
<p>I have noticed that the “Reference Volume” option available in version 5.4.0 of the FreeSurfer importer has been removed in the latest versions, including 5.6.2.</p>
<p>Please see the attached screenshots.</p>
<p>This option is crucial for me to transform recon-all models to specific MRI. Could you please clarify if this change was intentional, or provide guidance on how to access similar functionality in the newer versions?</p>
<p>Thank you,</p>
<p>Sincerely,</p>
<p>Nis175</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ecf142bb162fa9d65665e783d0bc5df26d78e09.png" data-download-href="/uploads/short-url/4oxZhkhiPUO59qO05uZE9DG8Lvb.png?dl=1" title="Comparison between Slicer 5.4 and Slicer 5.6.2_FreesurferImporter" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ecf142bb162fa9d65665e783d0bc5df26d78e09_2_690x367.png" alt="Comparison between Slicer 5.4 and Slicer 5.6.2_FreesurferImporter" data-base62-sha1="4oxZhkhiPUO59qO05uZE9DG8Lvb" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ecf142bb162fa9d65665e783d0bc5df26d78e09_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ecf142bb162fa9d65665e783d0bc5df26d78e09_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ecf142bb162fa9d65665e783d0bc5df26d78e09.png 2x" data-dominant-color="EDE8DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Comparison between Slicer 5.4 and Slicer 5.6.2_FreesurferImporter</span><span class="informations">1161×618 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2024-05-07 23:47 UTC)

<p>It appears that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> made this change in:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/PerkLab/SlicerFreeSurfer/commit/12c8ffd1014cdf1417d92885ba20bccdb2fc46fd">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerFreeSurfer/commit/12c8ffd1014cdf1417d92885ba20bccdb2fc46fd" target="_blank" rel="noopener nofollow ugc">github.com/PerkLab/SlicerFreeSurfer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PerkLab/SlicerFreeSurfer/commit/12c8ffd1014cdf1417d92885ba20bccdb2fc46fd" target="_blank" rel="noopener nofollow ugc">BUG: Fix FreeSurfer surface loading transformation by switching to NiBabel</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-11-03" data-time="17:13:21" data-timezone="UTC">05:13PM - 03 Nov 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
          <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a>
      </div>

      <div class="lines" title="changed 18 files with 724 additions and 838 deletions">
        <a href="https://github.com/PerkLab/SlicerFreeSurfer/commit/12c8ffd1014cdf1417d92885ba20bccdb2fc46fd" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+724</span>
          <span class="removed">-838</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">NiBabel contains a more complete implementation for loading FreeSurfer models, s<span class="show-more-container"><a href="https://github.com/PerkLab/SlicerFreeSurfer/commit/12c8ffd1014cdf1417d92885ba20bccdb2fc46fd" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">uch as being able to read in the additional information from the surface file footer.
This commit switches from using the vtkFSSurfaceReader implementation to using NiBabel for surface model loading. Other types of FreeSurfer files are currently still loaded using the existing classes.

A benefit of this change is that it is no longer needed to specify a reference volume when loading in a surface, since the information is read from the surface file footer.

Re #17</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>NiBabel contains a more complete implementation for loading FreeSurfer models, such as being able to read in the additional information from the surface file footer.<br>
This commit switches from using the vtkFSSurfaceReader implementation to using NiBabel for surface model loading. Other types of FreeSurfer files are currently still loaded using the existing classes.</p>
<p>A benefit of this change is that it is no longer needed to specify a reference volume when loading in a surface, since the information is read from the surface file footer.</p>
</blockquote>
<p>See the associated conversation at:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/PerkLab/SlicerFreeSurfer/issues/17">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerFreeSurfer/issues/17" target="_blank" rel="noopener nofollow ugc">github.com/PerkLab/SlicerFreeSurfer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PerkLab/SlicerFreeSurfer/issues/17" target="_blank" rel="noopener nofollow ugc">Fail to handle rotated samples?</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-20" data-time="11:26:28" data-timezone="UTC">11:26AM - 20 Oct 23 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2023-12-06" data-time="14:49:18" data-timezone="UTC">02:49PM - 06 Dec 23 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/phcerdan" target="_blank" rel="noopener nofollow ugc">
          <img alt="phcerdan" src="https://avatars.githubusercontent.com/u/3021667?v=4" class="onebox-avatar-inline" width="20" height="20">
          phcerdan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Here is the initial mri from the free dataset: https://openneuro.org/datasets/ds<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">004776/versions/1.0.0

https://s3.amazonaws.com/openneuro.org/ds004776/sub-01/anat/sub-01_T1w.nii.gz?versionId=lob8sYgfY.jRec5aLib_K73v_.NBAeQB

Here is the mrprage.nii.gz file from the pipeline (input grayscale volume):
[mprage.nii.gz.zip](https://github.com/PerkLab/SlicerFreeSurfer/files/13053617/mprage.nii.gz.zip)


Here is the lh.pial (for example) after running infant_recon_all: 
[lh.pial.zip](https://github.com/PerkLab/SlicerFreeSurfer/files/13053527/lh.pial.zip)

Direction Matrix:

![image](https://github.com/PerkLab/SlicerFreeSurfer/assets/3021667/a9581d0c-8866-4e4d-9ade-e299e3a97780)

Opening mprage.nii.gz as a regular volume and opening lh.pial as a Freesurfer model with mprage.nii.gz as reference:

![image](https://github.com/PerkLab/SlicerFreeSurfer/assets/3021667/ce92d564-9b1e-4fd9-b752-55da166fc5fa)


However, freeview reads and align the two files correctly.

![image](https://github.com/PerkLab/SlicerFreeSurfer/assets/3021667/ce24dfd9-38ea-42d7-ad0e-4ab27d73b2c8)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Sunderlandkyl (2024-05-08 13:35 UTC)

<p>We switched to using NiBabel to load FreeSurfer models, which allowed us to read the footer data containing the original reference volume geometry. This means that we should be able to read the models into the correct coordinate system without requiring the reference volume.</p>
<p>Let me know if you encounter any issues or misalignments.</p>

---

## Post #4 by @Nis175 (2024-05-16 21:15 UTC)

<p>Thank you Kyle! I will let you know when I have questions regarding NiBabel.</p>

---

## Post #5 by @Nis175 (2024-05-16 21:17 UTC)

<p>Thank you James for the information!</p>

---
