# How to fix the populating font family aliases issue

**Topic ID**: 32739
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/how-to-fix-the-populating-font-family-aliases-issue/32739

---

## Post #1 by @Koko000000000000000 (2023-11-11 13:26 UTC)

<p>I just installed slicer on my MacbookPro that has an M2 chip, but I’m face with this problem   Python 3.9.10 (main, Aug 19 2023, 07:11:06)<br>
[Clang 14.0.6 (<a href="https://github.com/tru/llvm-release-build" rel="noopener nofollow ugc">https://github.com/tru/llvm-release-build</a> 686807a176470032c208f2 on darwin</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt] Populating font family aliases took 147 ms. Replace uses of missing font family “.AppleSystemUIFont” with one that exists to avoid this cost.<br>
and I don’t know how tix it. I did try to specify a font in the slicer script using the python console, but nothing worked. can someone please help me fix this issue ?</p>

---

## Post #2 by @pieper (2023-11-11 14:41 UTC)

<p>It would be great if you could investigate this font issue further.  I get the same message on mac pro (intel).  We tried changing the font in the UI files but couldn’t find anything that made a difference.</p>

---

## Post #3 by @Koko000000000000000 (2023-11-11 17:14 UTC)

<p>I did try changing the font to Arial, and it worked for a while but then it had the same message instead, the missing font was “Menlo” even though it’s available on my device. I keep trying to change the fonts but nothing happens.</p>

---
