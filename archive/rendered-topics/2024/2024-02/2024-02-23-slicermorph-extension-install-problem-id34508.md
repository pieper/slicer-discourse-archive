# SlicerMorph extension install problem

**Topic ID**: 34508
**Date**: 2024-02-23
**URL**: https://discourse.slicer.org/t/slicermorph-extension-install-problem/34508

---

## Post #1 by @muratmaga (2024-02-23 22:34 UTC)

<p>I am getting this persistent error when I try to install SlicerMorph onto an older computer after the restarting the Slicer.</p>
<p><code>Info: In D:\D\S\S-0\Libs\MRML\Core\vtkArchive.cxx, line 39 vtkArchive Error: Problem with archive_read_open_filename():  Failed to open 'D:/Slicer 5.6.1/slicer.org/Extensions-32438/.updates/32438-win-amd64-SlicerMorph-git06ba525-2023-12-25.zip' Error</code></p>
<p>This computer does not have D:. There is an E:\ drive, which is Slicer 5.6.1 is install.ed But there are no .updates folder underneat.</p>
<p>When I am installing the extension, i can see the SlicerMorph folder is created, and then when I restart Slicer, everythnig inside the folder is removed with this error.  All other extension (MEMOS, ExtraEffects, Markups to  Models, etc) seem to work fine.<br>
Right after installing the extension<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a86044c227d50c69a2fa46936209c783c34f8846.png" data-download-href="/uploads/short-url/o1wt6SSL30TNUgID2l26IrEaKQC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86044c227d50c69a2fa46936209c783c34f8846_2_690x497.png" alt="image" data-base62-sha1="o1wt6SSL30TNUgID2l26IrEaKQC" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86044c227d50c69a2fa46936209c783c34f8846_2_690x497.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86044c227d50c69a2fa46936209c783c34f8846_2_1035x745.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86044c227d50c69a2fa46936209c783c34f8846_2_1380x994.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1566×1129 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After restarting Slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2091b9b14609dd5eb42def5add64375201a71fef.png" data-download-href="/uploads/short-url/4E7uDHUk97JKIS8Bc9zMxUvL80n.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2091b9b14609dd5eb42def5add64375201a71fef_2_690x213.png" alt="image" data-base62-sha1="4E7uDHUk97JKIS8Bc9zMxUvL80n" width="690" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2091b9b14609dd5eb42def5add64375201a71fef_2_690x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2091b9b14609dd5eb42def5add64375201a71fef_2_1035x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2091b9b14609dd5eb42def5add64375201a71fef_2_1380x426.png 2x" data-dominant-color="FEFEFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1481×458 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-02-23 23:16 UTC)

<p>Error disappeared by installing Slicer to another folder from the scratch. I think this is related to bookmarks set to auto install extensions, but I cannot be certain.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #3 by @lassoan (2024-02-24 01:59 UTC)

<p>It seems Slicer was moved to a new location when an extension installation was pending (you have not completed a restart, just quit the application). If this happens to you frequently then submit an issue - we could make this mechanism more robust (e.g., remove the pending extension install entry if the downloaded archive is not found anymore).</p>

---
