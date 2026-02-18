# Letters appended to filenames?

**Topic ID**: 40656
**Date**: 2024-12-12
**URL**: https://discourse.slicer.org/t/letters-appended-to-filenames/40656

---

## Post #1 by @hherhold (2024-12-12 17:10 UTC)

<p>Apologies if this topic has been addressed, I searched back several months but didn’t see anything regarding this. This is with Slicer preview 12-06 on Windows.</p>
<p>Filenames of certain files (MRML in particular) are being renamed and appended with 4 random characters - for example, <code>Helogale parvula AMNH 88132.mrml</code> is changed to <code>Helogale parvula AMN_DKFE.mrml</code>. This was not occurring in a preview from a few months back (09-30).</p>
<p>Did something change regarding auto-renaming of filenames or something? Again, apologies if I missed something, but a search of posts going back a bit didn’t reveal anything. I have not gone through a git log since then, so it’s entirely likely I missed this.</p>
<p>Any ideas?  Thanks!!</p>

---

## Post #2 by @hherhold (2024-12-12 18:17 UTC)

<p>Oh, never mind - I just saw this in the commit log.</p>
<pre><code>commit 7438bf24f0cd0b6e220e97c398c4a2da0192357e
Author: Kyle Sunderland &lt;sunderlandkyl@gmail.com&gt; 
Date:   Thu Nov 14 15:42:17 2024 -0500

    BUG: Fix saving with long node names
</code></pre>

---

## Post #3 by @lassoan (2024-12-13 05:23 UTC)

<p>You would not be able to reliably load or save a scene with long filenames on Windows, therefore we consistently limit the filename length that is generated from the node name by default on all platforms. This does not affect the node name, only the default filename that the node is saved to. We can still tweak the logic in case you have any specific suggestion.</p>

---

## Post #4 by @hherhold (2024-12-13 12:17 UTC)

<p>It’s okay, it was just a slight surprise. I’ve not had issues with long filenames on windows; I wonder if it has something to do with filesystem choice? I had a discussion with colleagues recently on NTFS vs exFAT, etc. (I basically only use NTFS, and install a 3rd party NTFS driver on MacOS machines.) But this could have nothing to do with it whatsoever.</p>

---

## Post #5 by @hherhold (2024-12-13 14:08 UTC)

<p>I do find the behavior a little curious, however. For example:</p>
<ol>
<li>Load in an NRRD file with a long filename</li>
<li>Make a change to the node, for example, change the voxel size.</li>
<li>Save the file. In the save dialog, the auto-generated filename with 4 random characters comes up.</li>
<li>Override the filename with the original long filename. Slicer saves it to the long filename.</li>
<li>Do some work, like make a segmentation, etc.</li>
<li>Go to save. The volume node is unmodified, so it is not marked to be saved. However, the filename is <em>not</em> the long filename, it is an auto-generated filename with the 4 random chars. So it’s not saved (which is correct) but the filename does not match the file on disk.</li>
</ol>
<p>I get what’s going on, and it’s okay, but it is a little confusing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5259f44a531bb3fe329a0f6a8c2cb6eadc57b605.png" data-download-href="/uploads/short-url/bKvStFYK8akZlxiLWZnemhLtemh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5259f44a531bb3fe329a0f6a8c2cb6eadc57b605.png" alt="image" data-base62-sha1="bKvStFYK8akZlxiLWZnemhLtemh" width="690" height="338" data-dominant-color="474747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">907×445 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-12-15 05:11 UTC)

<p>If we want to save and load scenes robustly then we need to limit file name length. Even if you happen to be able to save it on your current disk at the current location, you may run into issues when moving to another folder, want to copy it to a USB stick, want to open the files on a Windows computer, or want to cloud sync the folder.</p>
<p>Let us know if you have a better idea how to save nodes with very long names to short filenames (or if you encounter any issue, such as a scene is not saved or loaded correctly).</p>

---

## Post #7 by @hherhold (2024-12-15 16:12 UTC)

<p>Sounds good, I’ll think about it. I do get the issue of portability; as I mentioned before we ran into that recently with a USB stick someone had that was formatted as exFAT or even FAT32.</p>
<p>Maybe an “allow long filenames” checkbox somewhere in preferences? This is probably too much complexity for a fairly innocuous issue, however.</p>

---
