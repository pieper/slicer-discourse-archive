# Unable to install LesionSpotlight Extension

**Topic ID**: 20018
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/unable-to-install-lesionspotlight-extension/20018

---

## Post #1 by @Johannes (2021-10-05 12:15 UTC)

<p>Hello everyone,</p>
<p>I want to install the LesionSpotlight slicer extension. But I can’t find this by searching in the Extension Manager.<br>
Link to extension: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/LesionSpotlight" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/LesionSpotlight - Slicer Wiki</a></p>
<p>I use MacOS and the slicer version 4.13.0-2021-10-03 r30282 / 04d69cd</p>
<p>I’ve tried other versions of Slicer but can’t find the extension there either.</p>
<p>Is there a way to manually install this through Slicer’s GUI?</p>
<p>Warm greetings</p>

---

## Post #2 by @lassoan (2021-10-05 16:16 UTC)

<p>This extension fails to build on recent Slicer versions due to a <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2425037">small syntax error</a> (probably introduces by Slicer core software build tools or library updates).</p>
<p>The maintainers of the extension should be able to fix the problem easily, so please ask them first by <a href="https://github.com/CSIM-Toolkits/LesionSpotlightExtension/issues">submitting an issue in their tracker</a>.</p>
<p>If they don’t respond within 1-2 weeks then let us know here and we’ll see if Slicer core developers can fix the issue.</p>

---

## Post #3 by @Johannes (2021-10-08 08:26 UTC)

<p>Thank you so much. I reported the error to their tracker … I will inform you, if they remedy/repair the code.</p>

---

## Post #4 by @Johannes (2021-10-25 07:21 UTC)

<p>Unfortunately, none of the LesionSpotlightExtension team responded. You mentioned, that maybe the core development team can fix this issue.</p>

---
