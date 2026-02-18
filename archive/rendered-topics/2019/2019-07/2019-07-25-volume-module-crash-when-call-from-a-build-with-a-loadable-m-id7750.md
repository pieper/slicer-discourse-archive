# Volume module crash when call from a build with a loadable module

**Topic ID**: 7750
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/volume-module-crash-when-call-from-a-build-with-a-loadable-module/7750

---

## Post #1 by @rbahegne (2019-07-25 10:47 UTC)

<p>Hello, if I build (debug) a loadable module even empty (freshly created from the extension wizard) and run slicer, when i click on volumes extension i got a crash with this assert :</p>
<blockquote>
<p>Switch to module: “Volumes”</p>
<p>ASSERT: “this-&gt;Table-&gt;columnWidth(j) == newWidth” in file /Slicer/Slicer-SuperBuild-Debug/CTK/Libs/Widgets/ctkMatrixWidget.cpp, line 241</p>
<p>error: [/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
<p>It’s a debug only problem ? Can i safely deactivate this assert or anything ?</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2019-07-25 11:32 UTC)

<p>I run into that assert from time to time too - it crashes debug builds for no good reason as far as I can tell.  It would be great of someone could figure out the logic in the matrix widget but in the short term it’s easiest to comment out the assert and rebuild.</p>

---

## Post #3 by @lassoan (2019-07-25 18:29 UTC)

<p>This assert make the application crash in debug mode if the requested column width of a table cannot be set. There are many reasons why a set size request cannot be fulfilled, so this definitely should not be an assert, but probably not even a warning.</p>
<p>We <a href="https://github.com/commontk/CTK/pull/847" rel="nofollow noopener">already had a fix for this</a> but it has not been committed to CTK. I’ve committed it now. It still logs a warning. If the warning turns out to be annoying then we can remove that, too.</p>

---

## Post #4 by @rbahegne (2019-07-26 13:04 UTC)

<p>OK, it’s fine thank you !</p>

---
