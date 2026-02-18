# Renamed extension, but now there's a duplicate in the extensions manager

**Topic ID**: 30747
**Date**: 2023-07-23
**URL**: https://discourse.slicer.org/t/renamed-extension-but-now-theres-a-duplicate-in-the-extensions-manager/30747

---

## Post #1 by @jmhuie (2023-07-23 16:40 UTC)

<p>I recently updated my extension formerly called “SegmentGeometry” and renamed it to “SlicerBiomech”. I updated the .s4ext file in the ExtensionsIndex in the main branch and the 5.2 branch. The change was successful for the nightly build extensions catalog, but for the stable release extensions catalog (r31382) I see that both “SegmentGeometry” and “SlicerBiomech” are downloadable extensions.</p>
<p>This is a problem because both extensions are identical (icon, modules, metadata) except for their names. Ideally, I would have liked it to be so that when users go to update “SegmentGeometry” it would get renamed to “SlicerBiomech” and add the new module. Do any Slicer developers have insight on how to fix this problem?</p>
<p>At the very least, I would like to at least remove the “SegmentGeometry” extension from the stable release extension manager so that only “SlicerBiomech” exists.</p>

---

## Post #2 by @lassoan (2023-07-24 03:10 UTC)

<p>Normally we do not remove any existing extension that has been already released for a Slicer version (it could invalidate tutorials, discussions, etc), but instead just not provide the extension for new Slicer Releases. It could make sense to create a new icon for the new extension which has a new name and different/broader scope anyway. If you want to make users aware of the change and motivate them to switch to the new extension then it could help if you added a popup window to the deprecated extension’s modules that would explain that the extension is no longer maintained and they would need to install a new extension.</p>
<p>If you still want to make the existing extension just disappear then you can ask <a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> to delete the package.</p>

---

## Post #3 by @jmhuie (2023-07-24 13:22 UTC)

<p>I understand what you’ve said. I am not so concerned  about loss of functionality because the old extension and the new extension are identical. The only difference is their names in the extension manager. I had updated the github repo link, icon, etc (they share the same repo, which is the same repo I have been using just with an updated name as well). However, by updating the .s4ext it the Extensions Index it made a new extension. I did not intend to make a second one.</p>
<p>What I want is for the old extension to simply be renamed and the new one to be deleted because I don’t want user to have to uninstall the original and have to install the new one. Is that possible? The problem now is that since updating the .s4ext file I no longer have the ability to push changes to the original extension because they all update the new one. That seems to be because I inadvertently created a new package rather than modifying an existing one.</p>
<p>I hope that I am articulating my intentions clearly.</p>

---

## Post #4 by @lassoan (2023-07-24 15:38 UTC)

<p>Generally, released extensions should never disappear, and if you choose to do it anyway then allowing some time for users to switch by having the modules available under both the old and new extension name is useful.</p>
<p>A new Slicer Stable Release (5.4) should be out soon (within a few weeks). In that version the old extension has not been released, so only the new extension will be available. So, I would recommend to not do anything (other than maybe updating the logo, description, etc. of the new extension to reflect its new scope).</p>

---

## Post #5 by @jmhuie (2023-07-24 15:48 UTC)

<p>Makes sense.</p>
<p>If the new stable release will come out soon then that works for me. I will use that and the upcoming weeks to advertise the change. Thanks Andras</p>

---
