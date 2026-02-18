# Can't install Segment Editor Extra Effects (or its update?)

**Topic ID**: 39811
**Date**: 2024-10-23
**URL**: https://discourse.slicer.org/t/cant-install-segment-editor-extra-effects-or-its-update/39811

---

## Post #1 by @pawelk (2024-10-23 05:33 UTC)

<p>Operating system: Win 10<br>
Slicer version: 5.6.2<br>
Expected behavior: extension “Segment Editor Extra Effects” is available and works after installation from zip file<br>
Actual behavior: the additional buttons do not even show up</p>
<p>Important: direct install of extension is blocked on my computer. I have been installing them from zip files. I used Segment Editor Extra Effects before (with 5.6.1)</p>
<p>Now I installed Slicer (current stable, 5.6.2) on a new computer.</p>
<p>I downloaded the zip file from <a href="https://extensions.slicer.org/catalog/All/33069/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a></p>
<p>That page says Last update: Tue Oct 22 2024 (Revision: [7343241]) so I assumed it was current.</p>
<p>Downloaded file name: 33069-win-amd64-SegmentEditorExtraEffects-git7343241-2024-05-03.zip (note the different date)</p>
<p>I installed using Extension manager/Install from file…</p>
<p>Restarted Slicer.</p>
<p>The expected additional buttons in Segment Editor did not appear.</p>
<p>In Extension manager/Manage Extensions I see the extension listed with a comment:<br>
An update is available. Installed NA. Available 73432421 (2024-06-20) which seems to be the same version number (if 73432421 is a version number)  I had installed, but a different date.</p>
<p>Trying to update from within Manage Extensions page gives me an error, I presume because direct extensions are blocked here.</p>
<p>How do I download/install a version of this extension that works with my 5.6.2?</p>

---

## Post #2 by @lassoan (2024-10-23 05:47 UTC)

<p>If you use the generic <a href="https://extensions.slicer.org/">@KitwareMedical/slicer-extensions-webapp</a> link then you see the extensions that are compatible with the latest Slicer Preview Release (currently revision 33069). You need a different URL to see extensions that are compatible with the latest Slicer Stable Release (currently revision 32448).</p>
<p>Please follow the <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#download-extension-packages">instructions given in the documentation</a>. Then the correct extensions catalog page will be opened in your web browser.</p>

---

## Post #3 by @pawelk (2024-10-23 16:02 UTC)

<p>Thank you. This worked.</p>

---
