# Ctrl+Z crashes Slicer sometimes

**Topic ID**: 35935
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/ctrl-z-crashes-slicer-sometimes/35935

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-05-06 07:49 UTC)

<p>Hi to everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Today I’m having some bad responses when I try to use Ctrl+Z shortcut in segmentEditor. The shortcut is not modified (his function is Undo).</p>
<p>In my complete routine program, Ctrl+Z works well some of the times, but after a few steps ( One of them is reduce the number of Undo using <code>slicer.modules.SegmentEditorWidget.editor.setMaximumNumberOfUndoStates(1)</code>), then, when I try to use again the shortcut, it blocks the Slicer UI and finally closes the app.</p>
<p>It is a very disappointing issue, so if anyone could give me any advices I would be grateful.</p>
<p>Thanks.</p>
<p>Pd: I mentioned a similar behaviour  in Slicer UI a few weeks ago (<a href="https://discourse.slicer.org/t/segment-editor-shortcurts-does-not-work/35303" class="inline-onebox">Segment Editor shortcurts does not work</a>)</p>

---

## Post #2 by @pieper (2024-05-06 11:19 UTC)

<p>It would help a lot if you can find a way to reproduce this behavior using sample data and a set sequence of steps so the underlying issue can be isolated.</p>
<p>In the meantime, you should save frequently.</p>

---

## Post #3 by @THartman (2024-05-09 22:33 UTC)

<p>My (admittedly rather naive) thought would be to check your computer’s Memory usage in Task Manager if you’re on Windows, and if it seems to spike when this action is attempted, I would hazard a guess that the behavior you’re attempting to undo might be prompting a big change to the files and this might be causing the crash.  I had an issue where slicer was crashing due to drive code I was passing into it for a bit, and it turned out that I was using way too much memory, which caused the crash.</p>

---
