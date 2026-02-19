---
topic_id: 28101
title: "Extension Manager Icons Not Shown On Mac"
date: 2023-02-28
url: https://discourse.slicer.org/t/28101
---

# Extension manager icons not shown on Mac

**Topic ID**: 28101
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/extension-manager-icons-not-shown-on-mac/28101

---

## Post #1 by @muratmaga (2023-02-28 17:58 UTC)

<p>For some extensions on Mac, the icons are not found and instead of the extension specific icon, the generic plug-in one is shown. This doesn’t seem to happen in Windows or Linux. Screenshot below is from v5.2.2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf2dda5f8b62f79ed27eb425fb97402e9e21e160.png" data-download-href="/uploads/short-url/rhfr3TUbwDfSTkzRvPkSIrvJr7q.png?dl=1" title="Screen Shot 2023-02-28 at 9.56.19 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf2dda5f8b62f79ed27eb425fb97402e9e21e160_2_317x500.png" alt="Screen Shot 2023-02-28 at 9.56.19 AM" data-base62-sha1="rhfr3TUbwDfSTkzRvPkSIrvJr7q" width="317" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf2dda5f8b62f79ed27eb425fb97402e9e21e160_2_317x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf2dda5f8b62f79ed27eb425fb97402e9e21e160_2_475x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf2dda5f8b62f79ed27eb425fb97402e9e21e160_2_634x1000.png 2x" data-dominant-color="E2E4E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 9.56.19 AM</span><span class="informations">874×1378 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @smrolfe (2023-03-01 15:05 UTC)

<p>After some more testing, the issue appears to be specific to our network, not an OS. When I install SurfaceWrapSolidify (or one of the others that is failing) on Windows I get a series Qt errors and the following HTTPS related warnings:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dba2b7482a6f04ac590f9c1750edd5ca092e9b3c.jpeg" data-download-href="/uploads/short-url/vkZbmJgMpyYSaa3AMzPJker2gDG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2b7482a6f04ac590f9c1750edd5ca092e9b3c_2_690x346.jpeg" alt="image" data-base62-sha1="vkZbmJgMpyYSaa3AMzPJker2gDG" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2b7482a6f04ac590f9c1750edd5ca092e9b3c_2_690x346.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2b7482a6f04ac590f9c1750edd5ca092e9b3c_2_1035x519.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2b7482a6f04ac590f9c1750edd5ca092e9b3c_2_1380x692.jpeg 2x" data-dominant-color="374449"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×963 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.
"https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS."
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.```</code></pre>

---

## Post #3 by @muratmaga (2023-03-01 16:02 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="28101">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>the issue appears to be specific to our networ</p>
</blockquote>
</aside>
<p>Weird. So why are the other icons not affected?</p>

---

## Post #4 by @lassoan (2023-03-06 13:56 UTC)

<p>Extension icons that do not appear use some kind of redirect.</p>
<p>For example:</p>
<p>Current URL: <a href="https://github.com/SlicerMorph/SlicerMEMOS/raw/main/MEMOS/Resources/Icons/MEMOS.png">https://github.com/SlicerMorph/SlicerMEMOS/raw/main/MEMOS/Resources/Icons/MEMOS.png</a></p>
<p>Direct URL: <a href="https://raw.githubusercontent.com/SlicerMorph/SlicerMEMOS/main/MEMOS/Resources/Icons/MEMOS.png">https://raw.githubusercontent.com/SlicerMorph/SlicerMEMOS/main/MEMOS/Resources/Icons/MEMOS.png</a></p>

---
