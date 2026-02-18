# Google drive issue

**Topic ID**: 9232
**Date**: 2019-11-20
**URL**: https://discourse.slicer.org/t/google-drive-issue/9232

---

## Post #1 by @BreadBoxGuy (2019-11-20 16:07 UTC)

<p>I use google drive for backing up my data, however it won’t let me save files or export files directly to the google drive folder which is allocated as a standard folder in Microsoft explorer. Any solutions? Or is it a feature that could be added?</p>

---

## Post #2 by @lassoan (2019-11-20 19:09 UTC)

<p>I guess you are trying to use “Drive File Stream”. I haven’t had a chance to try why/how it fails with Slicer, as I don’t have access to a gsuite account, so I can only offer a few workarounds:</p>
<ul>
<li>copy files from the virtual cloud drive to a real local drive</li>
<li>use Google’s “Backup and sync” client instead</li>
<li>use OneDrive, DropBox, or other cloud storage services that make remote files appear as regular local files</li>
</ul>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> Could you please check? Is it common that third-party applications cannot access Google’s “Drive File Stream” drive?</p>

---

## Post #3 by @jcfr (2019-11-20 19:23 UTC)

<p>I do not use the “Drive File Stream” on my workstation and i don’t think it is available on Linux.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> if you are not using it, I could check with our system administrators if that feature is available.</p>

---

## Post #4 by @BreadBoxGuy (2019-11-21 10:43 UTC)

<p>I use Google backup and sync, however whenever I export to it it says it completed the export but the files never appear in the folder. When I export to desktop it works flawlessly.</p>

---

## Post #5 by @jcfr (2022-07-27 20:02 UTC)

<p><a class="mention" href="/u/breadboxguy">@BreadBoxGuy</a>  Is this still an issue using the latest Slicer version ?</p>

---

## Post #6 by @pieper (2022-07-27 20:22 UTC)

<p>I use Google Drive in “Stream files” mode for other files but not for saving from Slicer.  It does not work very well with the mac UI (folders appear empty for several seconds before the contents appear, files are sometimes grayed out until you click on them, and other odd behavior) but generally it’s good enough for what I need.  “Mirror files” mode might work better if you want to back up your Slicer outputs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c567d3195914b8ba7817bb1959912bf9b372ffd.png" data-download-href="/uploads/short-url/8BLWUjZEW02XJpQFRhNn5sfMZul.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c567d3195914b8ba7817bb1959912bf9b372ffd_2_635x500.png" alt="image" data-base62-sha1="8BLWUjZEW02XJpQFRhNn5sfMZul" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c567d3195914b8ba7817bb1959912bf9b372ffd_2_635x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c567d3195914b8ba7817bb1959912bf9b372ffd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c567d3195914b8ba7817bb1959912bf9b372ffd.png 2x" data-dominant-color="F2F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">771×607 59.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
