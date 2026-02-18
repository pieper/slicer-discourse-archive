# « SegmentEditorExtraEffects »

**Topic ID**: 11488
**Date**: 2020-05-11
**URL**: https://discourse.slicer.org/t/segmenteditorextraeffects/11488

---

## Post #1 by @loubna (2020-05-11 05:13 UTC)

<p>Hi;</p>
<p>How can I integrate « SegmentEditorExtraEffects » extension in the 3d slicer (built version 4.10.2).?</p>
<p>Thank’s in advance</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-05-11 13:06 UTC)

<p>SegmentEditorExtraEffects is an extension module that you can install using the extension manager.</p>

---

## Post #3 by @cpinter (2020-05-11 13:58 UTC)

<p>For built Slicer you cannot use the Extension Manager. In that case you will need to build the extensions you want to use and add the binary paths to the Additional module directories in Application Settings. See more details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#Developer_FAQ:_Extensions">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#Developer_FAQ:_Extensions</a></p>
<p>By the way, I strongly suggest using a recent version, since 4.10.2 is more than one and a half years old, and there has been a huge progress since then.</p>

---
