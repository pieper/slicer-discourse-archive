# Issue loading a file from a onedrive backed directory

**Topic ID**: 39494
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/issue-loading-a-file-from-a-onedrive-backed-directory/39494

---

## Post #1 by @Matteboo (2024-10-02 13:43 UTC)

<p>Hello,<br>
I’m setting up a new computer and I’m having issues with oneDrive backed data. I’m using the same code and version of slicer on both computer. On the new computer, I get the following error using slicer.util.loadVolume</p>
<pre><code class="lang-auto">RuntimeError: Failed to load node from file: C:/Users/~/OneDrive - company/volume.nii
Error: Loading C:/Users/~/OneDrive - company/volume.nii -  load failed.
</code></pre>
<p>The exact same code runs without any issue on the old computer. Same Onedrive.</p>
<p>I read this topic but it didn’t bring me any help.</p><aside class="quote quote-modified" data-post="1" data-topic="36153">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/windows-unable-to-import-dicom-files-that-are-in-a-onedrive-backed-up-folder/36153">Windows: Unable to import DICOM files that are in a OneDrive-backed up folder</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    TL;DR: on Windows, do not use folders that are backed up by Microsoft OneDrive for DICOM images that you want to import into Slicer DICOMBrowser! 
<a class="mention" href="/u/vkt1414">@vkt1414</a> and I have been debugging an issue that we thought is a problem with our extension, but upon further investigation it turned out the issue was not in the extension. Logs showed that DCMTK failed to open the DICOM files our extension was downloading. Initially, I thought this is due to the presence of dots in the folder hierarchy, but <a class="mention" href="/u/pieper">@pieper</a> …
  </blockquote>
</aside>

<p>If anybody has a solution or know what possible difference I should check between the computers I’m open to suggestions.<br>
I’m motivated to fix this issue so I don’t have to change several parts of my code so don’t hesitate to ask me to investigate the difference between the computers.</p>

---
