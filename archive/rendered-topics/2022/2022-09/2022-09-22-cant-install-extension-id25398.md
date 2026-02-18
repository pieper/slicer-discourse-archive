# Can't install extension?

**Topic ID**: 25398
**Date**: 2022-09-22
**URL**: https://discourse.slicer.org/t/cant-install-extension/25398

---

## Post #1 by @Moffitt (2022-09-22 13:51 UTC)

<p>New to slicer, tried to install registration but failed</p>

---

## Post #2 by @Moffitt (2022-09-22 14:05 UTC)

<p>For both Slicer versions 5.0.3 and  5.1.0<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dba598d0c5bcbdf297499acd7f4c50a5077f7f9c.jpeg" data-download-href="/uploads/short-url/vl5m3NrJOd5WsoSArDmTYelDu9u.jpeg?dl=1" title="slicer_install_extension_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba598d0c5bcbdf297499acd7f4c50a5077f7f9c_2_634x500.jpeg" alt="slicer_install_extension_error" data-base62-sha1="vl5m3NrJOd5WsoSArDmTYelDu9u" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba598d0c5bcbdf297499acd7f4c50a5077f7f9c_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba598d0c5bcbdf297499acd7f4c50a5077f7f9c_2_951x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba598d0c5bcbdf297499acd7f4c50a5077f7f9c_2_1268x1000.jpeg 2x" data-dominant-color="C7C9C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_install_extension_error</span><span class="informations">1409×1111 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2022-09-22 14:59 UTC)

<p>You may need to click <code>Check for updates</code> button to force downloading latest extension descriptions file from the server and then click <code>Install</code>. (This issue was fixed in the very latest Slicer-5.1 releases)</p>

---

## Post #4 by @Moffitt (2022-09-22 15:07 UTC)

<p>Checked but problem still<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e59df378a9abaf377828c73536500d951ef4040d.jpeg" data-download-href="/uploads/short-url/wLhKsnsieXVDdgSm00zVtSS6sLb.jpeg?dl=1" title="slicer_install_extension_error1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e59df378a9abaf377828c73536500d951ef4040d_2_573x500.jpeg" alt="slicer_install_extension_error1" data-base62-sha1="wLhKsnsieXVDdgSm00zVtSS6sLb" width="573" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e59df378a9abaf377828c73536500d951ef4040d_2_573x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e59df378a9abaf377828c73536500d951ef4040d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e59df378a9abaf377828c73536500d951ef4040d.jpeg 2x" data-dominant-color="F6F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_install_extension_error1</span><span class="informations">679×592 63.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-09-22 15:12 UTC)

<p>Have you clicked <code>Check for updates</code> and then <code>Install</code> for the extension? Can you install some extensions just not Elastix?</p>

---

## Post #6 by @Moffitt (2022-09-22 15:22 UTC)

<p>Yes I clicked <code>Check for updates</code> as shown in the screenshot above, and then <code>Install</code> for the extension.</p>
<p>I tried to install Airway Segmentation and DCMQi but none of them works</p>

---

## Post #7 by @lassoan (2022-09-22 16:03 UTC)

<p>Are you behind some corporate or hospital firewall or proxy server?</p>
<p>If you click the <code>Open extension catalog website</code> button can you download extensions from there?</p>
<p>Can you find any additional information about the failed download in the application log (no write access in temporary folder, out of disk space, etc)?</p>

---

## Post #8 by @Moffitt (2022-09-22 16:11 UTC)

<p>Yes I’m behind my hospital’s firewall and yes when I clicked the <code>Open extension catalog website</code> button I can download extensions from there.</p>
<p>Where to find the application log? Truely thank you!</p>

---

## Post #9 by @lassoan (2022-09-22 17:02 UTC)

<p>You can find the application log in menu: Help / Report a bug. Please check if you find any additional information.</p>
<p>Hospital firewalls might interfere communication between the extension frontend and backend. Could you try installing the extension via bookmarks:</p>
<ul>
<li>click on the wrench icon (in the Extensions Manager in the top-right corner)</li>
<li>select <code>Edit bookmarks</code>
</li>
<li>type <code>SlicerElastix</code> to the textbox, click OK</li>
<li>click <code>Install bookmarked</code> button (near the top)</li>
</ul>

---

## Post #10 by @Moffitt (2022-09-22 17:20 UTC)

<p>Information from the log file:</p>
<pre><code class="lang-auto">====================================================================
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Session start time .......: 2022-09-22 12:07:53
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Slicer version ...........: 5.1.0-2022-09-19 (revision 31142 / cc3ca58) win-amd64 - installed release
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Memory ...................: 130805 MB physical, 150261 MB virtual
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - CPU ......................: GenuineIntel , 16 cores, 16 logical processors
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Application path .........: C:/Users/4472950/AppData/Local/NA-MIC/Slicer 5.1.0-2022-09-19/bin
[DEBUG][Qt] 22.09.2022 12:07:53 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 22.09.2022 12:08:04 [Python] (C:\Users\4472950\AppData\Local\NA-MIC\Slicer 5.1.0-2022-09-19\lib\Slicer-5.1\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 22.09.2022 12:08:05 [Python] (C:\Users\4472950\AppData\Local\NA-MIC\Slicer 5.1.0-2022-09-19\lib\Slicer-5.1\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 22.09.2022 12:08:05 [Python] (C:\Users\4472950\AppData\Local\NA-MIC\Slicer 5.1.0-2022-09-19\lib\Slicer-5.1\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 22.09.2022 12:08:05 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.na-mic.org/Wiki/images/a/ad/Spharm-pdm-icon.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/ff/SlicerLiver.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:58 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 12:13:59 [] (unknown:0) - A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.
[DEBUG][Qt] 22.09.2022 12:14:08 [] (unknown:0) - Retrieving extension metadata for AirwaySegmentation extension
[DEBUG][Qt] 22.09.2022 12:14:08 [] (unknown:0) - Retrieving AirwaySegmentation extension files (extensionId: 632969c4e911182f1dfca50c)
[DEBUG][Qt] 22.09.2022 12:14:08 [] (unknown:0) - Downloading AirwaySegmentation extension (item_id: 632969c4e911182f1dfca50c, file_id: 632969c5e911182f1dfca514)
[CRITICAL][Qt] 22.09.2022 12:14:08 [] (unknown:0) - Failed downloading: https://slicer-packages.kitware.com/api/v1/file/632969c5e911182f1dfca514/download
[WARNING][Qt] 22.09.2022 13:15:24 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win?q=log' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.
[WARNING][Qt] 22.09.2022 13:15:24 [] (unknown:0) - Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/31142/win?q=log' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.
[DEBUG][Qt] 22.09.2022 13:15:37 [] (unknown:0) - Retrieving extension metadata for VASSTAlgorithms extension
[DEBUG][Qt] 22.09.2022 13:15:37 [] (unknown:0) - Retrieving VASSTAlgorithms extension files (extensionId: 632988dae911182f1dfcc9d4)
[DEBUG][Qt] 22.09.2022 13:15:37 [] (unknown:0) - Downloading VASSTAlgorithms extension (item_id: 632988dae911182f1dfcc9d4, file_id: 632988dbe911182f1dfcc9db)
[CRITICAL][Qt] 22.09.2022 13:15:37 [] (unknown:0) - Failed downloading: https://slicer-packages.kitware.com/api/v1/file/632988dbe911182f1dfcc9db/download
</code></pre>

---

## Post #11 by @lassoan (2022-09-22 17:49 UTC)

<p>Thank you, the messages indicates that Slicer downloads from the correct location but the download server returns an error, which is most likely due to a too strict proxy server.</p>
<p>If downloading via bookmarking does not work then you can download the extension packages using the Extensions Catalog website and then install the packages using <code>Install from file</code>.</p>

---
