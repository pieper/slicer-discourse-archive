# Extensions updates are not dispayed in the Stable

**Topic ID**: 23648
**Date**: 2022-05-30
**URL**: https://discourse.slicer.org/t/extensions-updates-are-not-dispayed-in-the-stable/23648

---

## Post #1 by @muratmaga (2022-05-30 23:31 UTC)

<p>At this point,“check for updates” functionality of the extension manager in 5.0.2 stable is problematic. It doesn’t find the updates…  There are a lot of warnings about https, but I don’t see an actual error:</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<pre><code class="lang-auto">"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/CleverSeg.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/CleverSeg.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/index.php/File:ModelClipIcon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/index.php/File:ModelClipIcon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Extensions/Testing/SNRMeasurement/SNRMeasurement.png?revision=21745&amp;view=co'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Extensions/Testing/SNRMeasurement/SNRMeasurement.png?revision=21745&amp;view=co'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.na-mic.org/Wiki/images/a/ad/Spharm-pdm-icon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.na-mic.org/Wiki/images/a/ad/Spharm-pdm-icon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/ff/SlicerHeart_Logo_128x128.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/ff/SlicerHeart_Logo_128x128.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/w/images/6/6b/RadiomicsExtension.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/w/images/6/6b/RadiomicsExtension.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.

"https://extensions.slicer.org/catalog/All/30822/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS."

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30822/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.
</code></pre>

---

## Post #2 by @jamesobutler (2022-05-31 01:21 UTC)

<p>You have a certain version of an extension installed and you know from <a href="https://slicer.cdash.org/index.php?project=SlicerStable" class="inline-onebox" rel="noopener nofollow ugc">CDash</a> that there is a new version of it available and the “Check for updates” option doesn’t indicate a new version available?</p>

---

## Post #3 by @muratmaga (2022-05-31 01:26 UTC)

<p>Yes, exactly. There is this commit from 2 days ago, which my version SlicerMorph doesn’t have. <a href="https://github.com/SlicerMorph/SlicerMorph/commits/master" class="inline-onebox" rel="noopener nofollow ugc">Commits · SlicerMorph/SlicerMorph · GitHub</a><br>
CDash shows the current version is built from that commit. So if you install the stable you will get the latest version, but won’t update an existing one.</p>

---

## Post #4 by @jamesobutler (2022-05-31 01:30 UTC)

<p>Are you able to install new extensions from this same build? The install extensions tab is working appropriately?</p>

---

## Post #5 by @muratmaga (2022-05-31 01:38 UTC)

<p>Yes, extension manager is fully functional. I will try uninstall and reinstalling it (to see if it is going to bring the latest package).</p>

---

## Post #6 by @muratmaga (2022-05-31 01:42 UTC)

<p>Uninstalling and reinstalling does bring the latest package. But we do need the update functionality function properly…</p>

---

## Post #7 by @lassoan (2022-05-31 14:49 UTC)

<p>I’ve noticed this, too. I’ll push a fix today.</p>

---

## Post #8 by @Aki (2022-06-09 08:48 UTC)

<p>Hello, everyone</p>
<p>I also have a problem of the extension maneger on Ubuntu 22.04.<br>
I downloaded 3DSlicer 5.0.2 (r30822) &amp; installed it, then I tried to install an extension.<br>
the extension maneger can show the extensions, but when I install an extension the extension maneger shows the below error and interupts the installation.</p>
<p>Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/62871f5ee8408647b39fe7a5/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/62871f5ee8408647b39fe7a5/download</a></p>
<p>I could download a extension from the kitware site <a href="https://extensions.slicer.org/catalog/All/30822/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a></p>
<p>Is this something related to this thread issue?<br>
I hope this is a temprally issue.<br>
Thanks.</p>
<p>AKi</p>

---
