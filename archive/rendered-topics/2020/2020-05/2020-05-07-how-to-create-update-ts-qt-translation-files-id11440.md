# How to create/update ts (qt translation) files?

**Topic ID**: 11440
**Date**: 2020-05-07
**URL**: https://discourse.slicer.org/t/how-to-create-update-ts-qt-translation-files/11440

---

## Post #1 by @quabug (2020-05-07 05:56 UTC)

<p>I am trying to enable i18n support on slicer, and it is generate “fr” translation files by default after enable Slicer_BUILD_I18N_SUPPORT and Slicer_UPDATE_TRANSLATION.<br>
Then I changed “fr” to “zh” in CMakeList.txt and it stop generate new translation files, and even I changed it back to “fr” it is still not working to update or generate new “fr” translation files.</p>
<p>How can I force cmake to generate new or update exist ts files?<br>
Is there any place to cache “ts” files which prevent cmake to generate/update ts files?</p>

---

## Post #2 by @quabug (2020-05-07 08:29 UTC)

<p>Solved by rebuild vs solution.</p>

---
