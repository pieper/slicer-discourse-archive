# Extension manager in linux empty

**Topic ID**: 22343
**Date**: 2022-03-07
**URL**: https://discourse.slicer.org/t/extension-manager-in-linux-empty/22343

---

## Post #1 by @Alex_Vergara (2022-03-07 11:54 UTC)

<p>I have this problem in my linux machine only, no problem in Windows and MacOS. Extension manager is completely empty. Restore extensions however, works fine. I have tried reinstalling from scratch, so no problem of old configurations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342a53a8d3bdff515bb0f3929bfb38134412cfd0.png" data-download-href="/uploads/short-url/7rtvOKF6ZpX0VR2eMIr6DYKrkWI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342a53a8d3bdff515bb0f3929bfb38134412cfd0_2_690x369.png" alt="image" data-base62-sha1="7rtvOKF6ZpX0VR2eMIr6DYKrkWI" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342a53a8d3bdff515bb0f3929bfb38134412cfd0_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342a53a8d3bdff515bb0f3929bfb38134412cfd0_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342a53a8d3bdff515bb0f3929bfb38134412cfd0.png 2x" data-dominant-color="3D4042"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1282×687 19.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @bpycinski (2022-03-22 08:53 UTC)

<p>Hello, I have the same issue on Manjaro Linux both with the last stable and nightly releases. Have you resolved this?</p>

---

## Post #3 by @chir.set (2022-03-22 10:11 UTC)

<p>Same observation on Arch Linux : extension list is empty, restoring extensions works, with 4.13.0-2022-03-19 r30735 / acc6180.</p>

---

## Post #4 by @Alex_Vergara (2022-03-22 11:14 UTC)

<p>No solution so far, I have to download the extensions manually, or restore them if I have them installed previously</p>

---

## Post #5 by @bpycinski (2022-03-23 13:42 UTC)

<p>Thank for the replies, so the easiest workaround is to download plugins and add them manually. For the reference, the website is e.g. <a href="https://extensions.slicer.org/catalog/All/29738/linux" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/29738/linux</a> , where 29738 is a compilation number of the last stable release (Slicer → Help → About Slicer → 4.11.20210226 r29738 / 7a593c8)</p>

---

## Post #6 by @phcerdan (2022-04-01 17:53 UTC)

<p>The problem is related with the qSlicerWebWidget: <a href="https://github.com/Slicer/Slicer/issues/6293" class="inline-onebox" rel="noopener nofollow ugc">Install extensions is empty · Issue #6293 · Slicer/Slicer · GitHub</a></p>
<p><s>Not sure yet if the error is in the Slicer side or an extra configuration is missing in Archlinux.</s></p>
<p>I can reproduce with pyqt5, no Slicer, so it seems Arch related. I will keep exploring.</p>

---

## Post #7 by @phcerdan (2022-04-01 18:50 UTC)

<p>Bufff, workarounded using:</p>
<pre><code class="lang-auto">QTWEBENGINE_DISABLE_SANDBOX=1 ./Slicer
</code></pre>
<p>I am guessing this is not he  best solution though.</p>
<p>For debugging, using these flags helped:</p>
<pre><code class="lang-auto">QTWEBENGINE_CHROMIUM_FLAGS="--enable-logging --log-level=0 --v=1" ./Slicer 
</code></pre>
<p>By the way, these are the warnings generated during loading:</p>
<pre><code class="lang-auto">Remote debugging server started successfully. Try pointing a Chromium-based browser to http://127.0.0.1:1337
"" 1 "JQuery not loaded - Failed to trigger webkitvisibilitychange"
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/CleverSeg.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/CleverSeg.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e1/CornerAnnotationIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e1/CornerAnnotationIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/index.php/File:ModelClipIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/index.php/File:ModelClipIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2e/OpenCAD.PNG'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2e/OpenCAD.PNG'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Extensions/Testing/SNRMeasurement/SNRMeasurement.png?revision=21745&amp;view=co'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Extensions/Testing/SNRMeasurement/SNRMeasurement.png?revision=21745&amp;view=co'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.na-mic.org/Wiki/images/a/ad/Spharm-pdm-icon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.na-mic.org/Wiki/images/a/ad/Spharm-pdm-icon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/ff/SlicerHeart_Logo_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/ff/SlicerHeart_Logo_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/cd/SwissSkullStripper.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/cd/SwissSkullStripper.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30746/linux' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/30746/linux" 0 "A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032."
A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.

</code></pre>

---

## Post #8 by @lassoan (2022-04-01 19:27 UTC)

<aside class="quote no-group" data-username="phcerdan" data-post="7" data-topic="22343">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/phcerdan/48/1559_2.png" class="avatar"> phcerdan:</div>
<blockquote>
<p><code>QTWEBENGINE_DISABLE_SANDBOX</code></p>
</blockquote>
</aside>
<p>This is does not look like a workaround but a solution if your linux kernel does not fulfill Chromium requirements - see <a href="https://doc.qt.io/Qt-5/qtwebengine-platform-notes.html#sandboxing-support" class="inline-onebox">Qt WebEngine Platform Notes | Qt WebEngine 5.15.16</a></p>
<p>I’ve submitted a pull request that adds this information to the documentation, please check:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6294">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6294" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6294" target="_blank" rel="noopener">DOC: Describe solution for empty blank extensions manager on ArchLinux</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:doc-archlinux-blank-extension-manager</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-04-01" data-time="19:26:26" data-timezone="UTC">07:26PM - 01 Apr 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 6 additions and 3 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6294/files" target="_blank" rel="noopener">
            <span class="added">+6</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See discussion at https://discourse.slicer.org/t/extension-manager-in-linux-empt<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6294" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">y/22343/6 and issue #6293 for more details.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
