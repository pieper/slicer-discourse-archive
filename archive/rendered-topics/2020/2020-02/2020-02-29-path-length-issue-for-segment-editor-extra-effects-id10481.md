# Path length issue for segment editor extra effects

**Topic ID**: 10481
**Date**: 2020-02-29
**URL**: https://discourse.slicer.org/t/path-length-issue-for-segment-editor-extra-effects/10481

---

## Post #1 by @pieper (2020-02-29 19:35 UTC)

<p>I’m passing on an issue that <a class="mention" href="/u/muratmaga">@muratmaga</a> experienced at a recent training event, where one of the users found that SegmentEditorExtraEffects would not load unless moved to a shorter path:</p>
<blockquote>
<p>Path issues are also very big concern. For example I had a person today which followed our instructions to put the SlicerMorph1-3 on their windows desktop. Everything worked pretty much fine, except SegmentEditorExtraEffects refuse to load the effects (gave a path error). There were no special characters or anything I can find. Unzipping everything to c:\ seemed to fix the issue. For example on my SlicerMorph installation at</p>
<p>C:/Users/Murat/Desktop/SlicerMorph1-3</p>
<p>Some paths are already as long as 169 characters.</p>
<p><strong>C:/Users/Murat/Desktop/SlicerMorph1-3//SlicerMorph1-3-Extensions/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThresholdLib/<strong>pycache</strong></strong></p>
<p>Should we be concerned about this?</p>
</blockquote>

---

## Post #2 by @lassoan (2020-02-29 20:01 UTC)

<p>On Windows, paths should work fine up to 260 characters. If we can confirm that this is an issue for reasonably short installation paths, then we can try to switch to UNC paths (prefixing path by <code>\\?\</code>), which can be up to 32000 characters.</p>
<p>The example above is 169 characters, which means that 90 characters of extra space is available, which is a lot. What was the path on that user’s computer?</p>

---

## Post #3 by @muratmaga (2020-03-01 02:20 UTC)

<p>People sometimes have multiple levels of directories, so the remaining 90 character can be exceeded by fairly quickly actually (this person for some reason had three levels). In the end Desktop ended up being a poor choice of placement for slicermorph for other reasons as well.</p>
<p>E.g., In windows 10 Home, onedrive may silently take over the users desktop so <code>c:\Users\Murat\Desktop</code> transparently maps to <code>C:\Users\Murat\Onedrive\Desktop</code> on windows shell and explorer.</p>
<p>But as far as I can tell, that behind the scenes translation doesn’t happen for QT dialog boxes. So a user cannot find a data directory that they copied on the desktop, if they go to Add Data button and navigate to the desktop they end up in real desktop location <code>c:\users\murat\desktop</code>, not where data sits <code>c:\users\murat\Onedrive\Desktop</code>).</p>

---
