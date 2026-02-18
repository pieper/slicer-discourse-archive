# Something wrong with the new slicer after installed some modules

**Topic ID**: 30613
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/something-wrong-with-the-new-slicer-after-installed-some-modules/30613

---

## Post #1 by @slicer365 (2023-07-14 23:30 UTC)

<p>What happened?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0bc5b835fc2ce4a0352ce879289de6b8a7960db.png" data-download-href="/uploads/short-url/w46vst4QYEw7ox42FqrMhUWGKU3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0bc5b835fc2ce4a0352ce879289de6b8a7960db.png" alt="image" data-base62-sha1="w46vst4QYEw7ox42FqrMhUWGKU3" width="690" height="286" data-dominant-color="FEEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×796 81.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">
Python 3.9.10 (main, Feb 22 2023, 01:07:37) [MSC v.1930 64 bit (AMD64)] on win32

&gt;&gt;&gt;

[Qt] Error(s):

[Qt] CLI executable: D:/3DSlicer/slicer5.2.2/NA-MIC/Extensions-31382/SlicerVMTK/lib/Slicer-5.2/qt-loadable-modules/vtkvmtk.py

[Qt] The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.

[Qt] Fail to instantiate module "vtkvmtk"

[Qt] The following modules failed to be instantiated:

[Qt] vtkvmtk

Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython

Loading Slicer RC file [D:/3DSlicer/slicer5.2.2/bin/../.slicerrc.py]

[Qt] Installed Qt WebEngine locales directory not found at location D:/3DSlicer/slicer5.2.2/bin/translations\qtwebengine_locales. Trying application directory...

[Qt] Qt WebEngine locales directory not found at location D:/3DSlicer/slicer5.2.2/bin\qtwebengine_locales. Trying fallback directory... Translations MAY NOT not be correct.

[FD] [2656:2524:0715/072641.847:ERROR:tcp_socket_win.cc(352)] bind() returned an error: ä»¥ä¸ç§è®¿é®æéä¸åè®¸çæ¹å¼åäºä¸ä¸ªè®¿é®å¥æ¥å­çå°è¯ã (0x271D)

[FD] [2656:2524:0715/072641.847:ERROR:devtools_http_handler.cc(298)] Cannot start http server for devtools.

[Qt] libpng warning: iCCP: known incorrect sRGB profile

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31382/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31382/win" 0 "A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032."

[Qt] A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.
</code></pre>

---

## Post #2 by @chir.set (2023-07-15 09:24 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="30613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>What happened?</p>
</blockquote>
</aside>
<p>While not answering your question, just 2 notes :</p>
<blockquote>
<p>[Qt] Fail to instantiate module “vtkvmtk”</p>
</blockquote>
<p>This is an old harmless message when SlicerVMTK is installed.</p>
<blockquote>
<p>Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython</p>
</blockquote>
<p>This one is quite recent, indicating than vtkSlicerShapeModuleMRMLPython could not be found while loading vtkSlicerStenosisMeasurement3DModuleLogicPython.<br>
It seems to be harmless too, because in the Python console :</p>
<pre><code class="lang-auto">import vtkSlicerStenosisMeasurement3DModuleLogicPython as vtkSlicerStenosisMeasurement3DModuleLogic
import vtkSlicerShapeModuleMRMLPython as vtkSlicerShapeModuleMRML
</code></pre>
<p>do not produce any errors. Slicer developers may give a real explanation of this output. I suspect that the order in which these python binaries are loaded during startup is important.</p>
<p>In Linux, the other error messages do not appear.</p>

---

## Post #3 by @lassoan (2023-07-15 12:19 UTC)

<p>The other warnings are logged when you open the extensions manager. They are harmless, too, they just indicate that an extension’s icon is downloaded using http protocol instead of encrypted https.</p>

---
