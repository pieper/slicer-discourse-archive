# Segments disappeared!

**Topic ID**: 12698
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/segments-disappeared/12698

---

## Post #1 by @skentis (2020-07-22 22:32 UTC)

<p>Problem report for Slicer 4.10.2 macosx-amd64: [please describe expected and actual behavior] Hi I was using segment editor to annotate MRI images and saving regularly onto a server (but never actually closing slicer). When I finally closed and reopened slicer today all of my segments were gone and when I tried to add new segments all came up in the same shade of gray (instead of a color palette as usual). Any idea what the issue is? Thanks!</p>

---

## Post #2 by @lassoan (2020-07-23 01:23 UTC)

<p>Saving to a server is always inherently risky. Network problems may corrupt files of prevent full saving or restoring of a scene. It is always safer to save locally and copy manually (or synchronize folders).</p>
<p>I would recommend to use a recent Slicer-4.11 release, as it contains many improvements and fixes.</p>
<p>How did you save the scene? Into a single mrb file or into many separate files? Is any error logged when you load the scene (menu: Help / Report a bug)?</p>

---

## Post #3 by @skentis (2020-08-10 15:13 UTC)

<p>Hi! I restarted the work and downloaded Slicer-4.11 but now am having some new issues:</p>
<p>First a large amount of the time I use segment editor the paint brush/eraser disappear within the first few edits and I can only get them back by reloading in my data. Is there any way to avoid this?</p>
<p>Second, some of the time I open my annotations the segments are opaque and uneditable- any idea why this is?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2020-08-10 16:02 UTC)

<p>Since the issues you are experiencing seem to be unrelated, please report them in a separate topic. Also include a few screenshots or screen capture that demonstrate the problem.</p>

---
