# Slicer spr export

**Topic ID**: 8627
**Date**: 2019-09-30
**URL**: https://discourse.slicer.org/t/slicer-spr-export/8627

---

## Post #1 by @Chris_Rorden (2019-09-30 16:54 UTC)

<p>I think I found a tiny bug in the Slicer image export.</p>
<p>I am using Slicer 4.10.2 on a MacOS computer. I can open a NRRD volume and choose File/Save to save the file. I want to save as  <a href="https://www.cmrr.umn.edu/stimulate/stimUsersGuide/node57.html" rel="noopener nofollow ugc">Stimulate Sdt</a> so I save <code>Stimulate (.spr)</code> from the pulldown. I accept that I want to save the file as “spr.spr” in the folder <code>/Users/chris/s</code>. It then generates a header (.spr) and image (.sdt) file. If I open the header with a text file I see:</p>
<blockquote>
<p>stimFileName: /Users/chris/s/TempWritenrrd/spr.sdt</p>
</blockquote>
<p>The folder <code>TempWritenrrd</code> does not exist, and both .sdt and .spr files are saved in <code>/Users/chris/s</code>. I think the Slicer writer should only use the file name without path or to include the actual path.</p>

---

## Post #2 by @lassoan (2019-10-02 02:21 UTC)

<p>Yes, this is indeed incorrect behavior. It is a bug in ITK (itkStimulateImageIO.cxx) that file path is not removed. I’ve also noticed that saving and reloading a file results in a 90+90 deg rotation of the volume. Is this file format still used somewhere? (the document that you linked is written in 1996!) If not that much, then maybe it is better to remove it from ITK and Slicer.</p>

---

## Post #3 by @Chris_Rorden (2019-10-02 19:18 UTC)

<p>I only added support to MRIcroGL for Slicer compatibility. Seems safe to retire this format.</p>

---
