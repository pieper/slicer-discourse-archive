# Dashes silently removed from filename in "export to file" operation

**Topic ID**: 43923
**Date**: 2025-08-01
**URL**: https://discourse.slicer.org/t/dashes-silently-removed-from-filename-in-export-to-file-operation/43923

---

## Post #1 by @flomei (2025-08-01 06:59 UTC)

<p>Hi,<br>
I’m using Slicer (v5.8.1) for manual annotation of structural MRI nifti data (T1 + parcellations).<br>
I’m loading T1 volume and freesurfer parcellations (both .nii.gz) via a selfmade startup script, but use the GUI for saving modified parcellations. Here, I use the “Segmentations” toolkit (selected in dropdown on  top right), and there the “Export to files“ submenu on the left.<br>
I select a new destination folder, and when I export my parcellation there, any dashes are removed from the filename.<br>
This does not happen when saving e.g. a .nrrd file using the file → save dialog. What gives, and can I change this behavior somehow?</p>

---

## Post #2 by @pieper (2025-08-01 10:57 UTC)

<p>Please try to reproduce this with something that narrows down what’s different in your workflow from things anyone can reproduce with the standard Slicer.  For example, if I save a SampleData volume that has dashes in the name to a nii.gz file the dashes are preserved.  So there seems to be something unique in your data or workflow.</p>

---

## Post #3 by @flomei (2025-08-01 11:24 UTC)

<p>minimal reproduction example:</p>
<p>open slicer, use file → Download sample data → MRHead</p>
<p>switch to “Segment Editor” in top dropdown, create a segmentation with dashes in the name. select that segmentation, and MRHead as Source volume.</p>
<p>add a few segments and annotate something in them, eg with the 3d paintbrush.</p>
<p>switch to “Segmentations” in top dropdown, also set “Segmentation” to your newly made one, then go to “Export to files” in left toolbar, set file format to nifti, hit the export button.</p>
<p>For me, this produces a .nii file in my output folder that is named like my segmentation except dashes are removed, eg if my segmentation is called “foo-bar”, the file is then called “foobar.nii”</p>
<p>i hope this is clear to follow and reproduce.</p>

---

## Post #4 by @pieper (2025-08-01 14:32 UTC)

<p>Okay, yes, that is more clear, and I do see this issue.  <a class="mention" href="/u/lassoan">@lassoan</a> may know why it works like this.</p>
<p>What you can do instead is export the Segmentation to a Labelmap and then you can export that to an nii.gz file with the dashes retained (you may still need to rename the exported labelmap).</p>

---

## Post #5 by @flomei (2025-08-01 15:11 UTC)

<p>I was able to resolve my particular issue by simply adapting a naming scheme with only underscores, which are not affected by this. Luckily the names were not set in stone.</p>
<p>I still wanted to bring up this behavior since I could not find documentation of it. Thank you for verifying/replicating the behavior for now.</p>

---

## Post #6 by @pieper (2025-08-01 15:36 UTC)

<p>Thanks for brining it up.  If you want this issue to remain on the radar you can file an issue on github since those get reviewed.  You can include a link back to this chat thread as part of the issue description.</p>

---

## Post #7 by @lassoan (2025-08-01 21:09 UTC)

<p>It is a good catch, the regular expression that created a safe filename from a node name was incorrectly filtered out the dash character (due to a subtle inconsistency between the regular expression engine in Qt and kwsys). I’ve submitted a fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8617">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8617" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8617" target="_blank" rel="noopener">BUG: Fix removal of dash characters from exported segmentation filename</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:fix-dash-removal-from-segmentation-filename</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-01" data-time="21:29:18" data-timezone="UTC">09:29PM - 01 Aug 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 4 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8617/files" target="_blank" rel="noopener">
            <span class="added">+4</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes the issue reported at https://discourse.slicer.org/t/dashes-silently-remov<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8617" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ed-from-filename-in-export-to-file-operation/43923</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>That said, I would recommend to save segmentations in Slicer (not export) and use terminologies to specify what each segment contains (instead of relying on some arbitraily chosen names). This representation is archival quality, can be used forever, for any projects, without ambiguity, and supports overlapping labels (and can be losslessly saved into standard DICOM segmentation objects). Then, when you want to use this data to train an AI model, you can specify a mapping from terminology code to label value. I recently gave mini-presentation on this topic, <a href="https://1drv.ms/b/c/872af7415c00bfb9/EYVxmPHVis1GvQWRvGXh4IcBPndpw_w3YgUXBiK4dabSTg?e=CCxUtj">see the slides here</a> - it explains some of the motivation includes links where you can learn more.</p>

---
