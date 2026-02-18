# Loading MRB file Leads to Creation of Temporary File that Cannot be Deleted

**Topic ID**: 37363
**Date**: 2024-07-13
**URL**: https://discourse.slicer.org/t/loading-mrb-file-leads-to-creation-of-temporary-file-that-cannot-be-deleted/37363

---

## Post #1 by @edwardwang1 (2024-07-13 21:19 UTC)

<p>Hi all,</p>
<p>I have encountered a bug that I haven’t seen in my many years using Slicer. I was given a .mrb file from a colleague. While Slicer is able to load the MRB correctly, it also reports the error below.</p>
<p><code>Loading C:/Users/Edward/Desktop/UnionML/MRBsOriginal2024/165.mrb - vtkMRMLScene::ReadFromMRB failed: cannot remove directory 'C:/Users/Edward/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleLoadTemp-2024-07-13_165652_79'\n</code></p>
<p>Upon investigation, it appears that Slicer is creating temporary files in <code>\AppData\Local\slicer.org\Slicer\cache\SlicerIO</code> that can not be deleted. I am also unable to delete it manually using either Windows CMD or the GUI. When I attempt this, it says that Windows can no longer find the file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a848884596339f5bf4ccb3eb23fb7b7e3cddabb.png" data-download-href="/uploads/short-url/aDdhBP90Aw21bF95QMiR0XN7caD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a848884596339f5bf4ccb3eb23fb7b7e3cddabb_2_690x74.png" alt="image" data-base62-sha1="aDdhBP90Aw21bF95QMiR0XN7caD" width="690" height="74" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a848884596339f5bf4ccb3eb23fb7b7e3cddabb_2_690x74.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a848884596339f5bf4ccb3eb23fb7b7e3cddabb_2_1035x111.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a848884596339f5bf4ccb3eb23fb7b7e3cddabb_2_1380x148.png 2x" data-dominant-color="1E1E1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1722×187 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Inside the __BundleLoadTempXXX folder there is a subfolder with a patient name. I am unable to open this subfolder (Windows says that the data is unavailable), and it appears to be empty. The subfolder is named XXXXXX Xxxxx. (with a period at the end). My guess is that it’s this period that is causing issues.</p>
<p>Even after a system restart, I was unable to delete the temporary folder. Has anyone ever encountered this before?</p>
<p>Thanks,<br>
Edward</p>
<p>Edit: System Settings:<br>
Windows 11 Pro<br>
Slicer 5.6.2</p>

---

## Post #2 by @lassoan (2024-07-14 14:19 UTC)

<p>Most likely some third-party antivirus or computer monitoring software keeps the folder open while trying to inspect its content and so Slicer cannot delete it. You should be able to delete the empty folders after you restart your computer. You can also just leave the folders there, as their presence does not cause any problem and don’t take up space.</p>
<p>You can install a utility like <a href="https://lockhunter.com/">LockHunter</a> that may be able to tell what application is locking the file and that can help with solving the issue.</p>
<p>You can also choose a different location for cache folder (in menu: Edit / Application settings / Cache / Cache location), which is not monitored or uses a more robust file system.</p>

---

## Post #3 by @edwardwang1 (2024-07-17 18:45 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply. I mentioned this to my colleague and they were able to give me a new .mrb without that issue. Also, after restarting my computer I was able to use CMD to get rid of the folders.</p>

---
