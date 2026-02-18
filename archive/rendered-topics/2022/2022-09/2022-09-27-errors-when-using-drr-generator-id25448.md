# Errors when using DRR Generator

**Topic ID**: 25448
**Date**: 2022-09-27
**URL**: https://discourse.slicer.org/t/errors-when-using-drr-generator/25448

---

## Post #1 by @suzume (2022-09-27 14:26 UTC)

<p>Operating system: Mac OS system<br>
Slicer version: Slice 5.0.3<br>
Expected behavior: When I using DRR Generator tool, there is always an error occurred!<br>
The error message is : " The message detail is:</p>
<p>Exception thrown in event: /Volumes/D/S/S-0-build/ITK/Modules/IO/NRRD/src/itkNrrdImageIO.cxx:1118:</p>
<p>ITK ERROR: NrrdImageIO(0x7f96d87621b0): Write: Error writing output_fixed.nrrd:</p>
<p>[nrrd] nrrdSave: couldn’t fopen(“output_fixed.nrrd”,“wb”): Read-only file system"<br>
Is there anyone else met this error before? Could you please tell me how to fix it?</p>

---

## Post #2 by @pieper (2022-09-27 19:32 UTC)

<aside class="quote no-group" data-username="suzume" data-post="1" data-topic="25448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/suzume/48/16794_2.png" class="avatar"> suzume:</div>
<blockquote>
<p>Read-only file system</p>
</blockquote>
</aside>
<p>You don’t have permission to save in the indicated location.</p>
<p>It looks like this name <a href="https://github.com/lancelevine/SlicerDRRGenerator/blob/6ac5f40e0655dfd34437055d8c3bc98b278053a0/DRRGeneratorModule/qSlicerDRRGeneratorModuleModuleWidget.cxx#L527">is hard coded in the DRRGenerator</a>.  If you launch slicer from a terminal in a directory where you have write permission you should be able to make it work.  You could file <a href="https://github.com/lancelevine/SlicerDRRGenerator/issues">an issue</a> to alert the developers of this problem.</p>

---

## Post #4 by @suzume (2022-09-28 03:00 UTC)

<p>Thanks for your reply! I re-installed the 3D slicer and the DRR Generator on Windows system. The error was fixed. It seems that the error occurred because of the Mac OS system.</p>

---
