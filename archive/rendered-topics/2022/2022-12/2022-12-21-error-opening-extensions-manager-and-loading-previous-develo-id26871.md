# Error opening Extensions Manager and loading previous developed Modules

**Topic ID**: 26871
**Date**: 2022-12-21
**URL**: https://discourse.slicer.org/t/error-opening-extensions-manager-and-loading-previous-developed-modules/26871

---

## Post #1 by @LuisaDantas (2022-12-21 14:22 UTC)

<p>Hey all,</p>
<p>I’ve been using 3D Slicer for a while but I had to install it on a different machine and it’s giving some errors right after the installation.</p>
<p>When I open Extensions Manager this error is printed:</p>
<pre><code class="lang-auto">[Qt] An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.

[FD] DevTools listening on ws://127.0.0.1:1337/devtools/browser/8648ed83-1ee3-4015-8f31-cc414c7a7dff

[Qt] Remote debugging server started successfully. Try pointing a Chromium-based browser to http://127.0.0.1:1337

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS."

[Qt] Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31317/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.

[Qt] "https://extensions.slicer.org/catalog/All/31317/win" 0 "A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032."

[Qt] A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.
</code></pre>
<p>And then I tried loading a Loadable Module I’m developing (through Extension Wizard &gt; Select Extension) and it gave this error:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932b8045c4ca0ffb23b07066902bc83f8ddbf62e.png" alt="image" data-base62-sha1="kZVo6nGMV4BOsDUr3TXRXhFmgc6" width="501" height="97"></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files (x86)\Slicer\Slicer 5.2.1\lib\Python\Lib\imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File ".../SegmentacaoVentricularModule.py", line 3, in &lt;module&gt;
    import cv2
ModuleNotFoundError: No module named 'cv2'
[Qt] loadSourceAsModule - Failed to load file ".../SegmentacaoVentricularModule.py"  as module "SegmentacaoVentricularModule" !
[Qt] Fail to instantiate module  "SegmentacaoVentricularModule"
[Python] The module factory manager reported an error. One or more of the requested module(s) and/or dependencies thereof may not have been loaded.
</code></pre>
<p>I can create a new Extension and Module but it doesn’t load when Slicer is restarted.</p>
<p>Edit: I’m using Slicer 5.2.1 on Windows 10</p>

---

## Post #2 by @pieper (2022-12-21 15:21 UTC)

<p>If the extension manager window comes up normally then the warnings can all be ignored.</p>
<p>The module import issue appears to be due to a missing <a href="https://pypi.org/project/opencv-python/">OpenCV</a> package.  Running <code>pip_install("opencv-python")</code> should fix it.</p>
<p>To avoid this in the future, the module could could be updated with something like this:</p>
<pre><code class="lang-auto">try:
  import cv2
except ModuleNotFoundError:
  pip_install("opencv-python")
  import cv2
</code></pre>

---

## Post #3 by @LuisaDantas (2022-12-21 16:24 UTC)

<p>Thank you for the reply!</p>
<p>It seems to be working fine. Is there some way to supress the warnings?</p>

---

## Post #4 by @pieper (2022-12-21 16:49 UTC)

<p>Most of those warnings are because the extensions list http links to their screenshots but the newer Qt versions require https since the extension page is hosted via https.  Ideally extension providers should sort these out but it may take a while.  For now it’s easier to ignore them.</p>

---
