---
topic_id: 33809
title: "Sandbox Module Cannot Be Downloaded Via Extension Manager To"
date: 2024-01-16
url: https://discourse.slicer.org/t/33809
---

# Sandbox module cannot be downloaded via extension manager today?

**Topic ID**: 33809
**Date**: 2024-01-16
**URL**: https://discourse.slicer.org/t/sandbox-module-cannot-be-downloaded-via-extension-manager-today/33809

---

## Post #1 by @mikebind (2024-01-16 22:39 UTC)

<p>I am trying to set up a new computer with Slicer 5.6.1 and the extensions I use.  I am unable to download the Sandbox extension via the extension manager today.  I see it listed in the browser, but when I click to “Install”, I get the following error message:<br>
[Qt] Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/65a664ce2aa6efa9ffee562e/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/65a664ce2aa6efa9ffee562e/download</a></p>
<p>I have trouble understanding the CDash information, but I do see that an error is reported for several modules on the most recent stable build <a href="https://slicer.cdash.org/build/3273316/configure" rel="noopener nofollow ugc">Configure (cdash.org)</a>, but I don’t know if this is related.  I was able to install several extensions a few days ago on the same machine and the same network, so I don’t think the problem is on my end, but could be wrong about that.</p>

---

## Post #2 by @pieper (2024-01-16 22:44 UTC)

<p>You may be seeing this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7531">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7531" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7531" target="_blank" rel="noopener">SlicerDMRI extension is not updating for 5.6.1</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-10" data-time="18:43:14" data-timezone="UTC">06:43PM - 10 Jan 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Even though the repository has been updated [Dec 15, 2023](https:/<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">/github.com/SlicerDMRI/SlicerDMRI/commits/master/), the DMRI extension offered for 5.6.1 is still from Dec 12, 2023.  The s4ext file points to the master branch of SlicerDMRI for both 5.6 and the master branch of the extension index.  The SlicerPreview versions correctly offer a newer build with the most recent SlicerDMRI.

## Steps to reproduce

Try to install dmri in 5.6.1 and you are offered the older version.

5.6.1:

![image](https://github.com/Slicer/Slicer/assets/126077/83f90e48-0d20-46c4-a7ff-a851f0a1aed8)

Nightly:

![image](https://github.com/Slicer/Slicer/assets/126077/a5da4476-0ad6-4c40-9103-adab87a6c13f)


## Environment

For reference: #7530

Possibly related to: https://github.com/AIM-Harvard/SlicerRadiomics/issues/80, but different because there is no superbuild for SlicerDMRI so the same fix does not apply.

@lassoan do you have any suggestions?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a> is looking into whether the extensions are being properly copied to the server for the release branch.</p>
<p>You might try the SlicerPreview version and let us know if that one works.</p>

---

## Post #3 by @mikebind (2024-01-16 23:00 UTC)

<p>No luck, same type of error with a fresh install of today’s preview version.  Here is the error log (with username stripped out as only modification):</p>
<blockquote>
<p>[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20240116_145243<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.7.0-2024-01-15 (revision 32684 / d7080d6) win-amd64 - installed release<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 65220 MB physical, 74948 MB virtual<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 28 cores, 28 logical processors<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users//AppData/Local/slicer.org/Slicer 5.7.0-2024-01-15/bin<br>
[DEBUG][Qt] 16.01.2024 14:52:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 16.01.2024 14:52:46 [Python] (C:\Users&lt;user&gt;\AppData\Local\slicer.org\Slicer 5.7.0-2024-01-15\lib\Slicer-5.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 16.01.2024 14:52:46 [Python] (C:\Users&lt;user&gt;\AppData\Local\slicer.org\Slicer 5.7.0-2024-01-15\lib\Slicer-5.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 16.01.2024 14:52:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png" rel="noopener nofollow ugc">http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png" rel="noopener nofollow ugc">http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png" rel="noopener nofollow ugc">http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269" rel="noopener nofollow ugc">http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32684/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 16.01.2024 14:52:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" rel="noopener nofollow ugc">https://www.chromestatus.com/feature/5088147346030592</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" rel="noopener nofollow ugc">https://www.chromestatus.com/feature/5633521622188032</a>.<br>
[DEBUG][Qt] 16.01.2024 14:53:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Retrieving extension metadata for Sandbox extension<br>
[DEBUG][Qt] 16.01.2024 14:53:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Retrieving Sandbox extension files (extensionId: 65a6429a2aa6efa9ffee3586)<br>
[DEBUG][Qt] 16.01.2024 14:53:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Downloading Sandbox extension (item_id: 65a6429a2aa6efa9ffee3586, file_id: 65a6429a2aa6efa9ffee358d)<br>
[CRITICAL][Qt] 16.01.2024 14:53:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/65a6429a2aa6efa9ffee358d/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/65a6429a2aa6efa9ffee358d/download</a></p>
</blockquote>
<p>I know the https warnings are not important, but the failed download error seems like the problem.</p>

---

## Post #4 by @mikebind (2024-01-16 23:20 UTC)

<p>Hold up, I appear not to be able to install any extensions to the new preview Slicer, even ones where I don’t see any errors on CDash, such as ErodeDilateLabel.  I’m on Windows, FYI.  Also can’t install ErodeDilateLabel  on 5.6.1.</p>
<p><strong>To recap</strong>, on a new Windows laptop, I installed 5.6.1 last week, and successfully installed &gt;20 extensions via the Extension Manager.  Today, I tried to install the Sandbox extension (for the Lights module), and, while it was listed on the Extension Manager, the download failed with the message posted above.  I installed 5.7.0-2024-01-15 just now, and appear to be unable to download/install any extensions via the Extension Manager.  Returning to 5.6.1, I was not able to install a different new extension (ErodeDilateLabel) either, with another “Failed downloading” error.</p>
<p>Since I can’t seem to download any extension, I am less sure that the error isn’t somewhere on my side (though my internet access is fine, and I had no issue downloading and installing the preview Slicer just now).  Any troubleshooting tips?  Anyone else successfully get an extension downloaded and installed via the extension manager on Windows today?</p>
<p>Possibly related to the issue <a class="mention" href="/u/pieper">@pieper</a> linked above, all of the extensions I successfully downloaded last week (&gt;20 of them), show version dates of 2023-12-12 in the “Manage Extensions” tab.</p>

---

## Post #5 by @muratmaga (2024-01-17 00:30 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> you are not behind the SCH firewall/proxy are you? Self-signed certificates can create havoc.</p>
<p>Cdash shows most extensions (including sandbox on windows ) is built.</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/index.php?project=SlicerStable</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #6 by @mikebind (2024-01-17 21:28 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, I am probably inside the SCH firewall (the new laptop is a Seattle Childrens machine), but successfully installed extensions last week, and I’m not sure what would have changed.  How do you manage your Slicer extensions? Do you download them outside the network and then install from file?</p>
<p>I just checked and am able to download extensions for 5.6.0 on a machine outside the firewall without a problem. So, it seems likely that I may be dealing with some sort of firewall issue which is blocking downloads via the extension manager.  Any advice on dealing with this or confirming if it is the case?</p>

---

## Post #7 by @muratmaga (2024-01-17 21:37 UTC)

<p>Firewall issues can be unique to a computer (expired or missing certificates etc) and usually hard to chase. Try pip_install something basic (even numpy probably). If you are getting a SSL (or something along those lines), you are suffering from the certificate/firewall issue.</p>
<p>Separately, If you have Zscaler enabled, i would turn it off and try installing things without it.  It never works with zscaler.</p>
<p>As a backup solution, we usually have zip archives all all three slicer versions with common extensions we use installed somewhere on intranet. unfortunately, I don’t think we did the 5.6.1 yet, so I can’t hep you there. But if you need 5.6.0, I can send you link.</p>

---

## Post #8 by @muratmaga (2024-01-17 21:41 UTC)

<p>This is the error message I get with Zscaler enabled. When disabled, I can install fine.</p>
<blockquote>
<p>" Retrieving extension metadata for Auto3dgm extension</p>
<p>Retrieving Auto3dgm extension files (extensionId: 65782b1f83a3201b44d50df4)</p>
<p>Downloading Auto3dgm extension (item_id: 65782b1f83a3201b44d50df4, file_id: 65782b2083a3201b44d50dfd)</p>
<p>Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/65782b2083a3201b44d50dfd/download">https://slicer-packages.kitware.com/api/v1/file/65782b2083a3201b44d50dfd/download</a>"</p>
</blockquote>

---

## Post #9 by @mikebind (2024-01-17 21:42 UTC)

<p>Thanks, I do have zScaler running, I will try disabling.</p>

---

## Post #10 by @mikebind (2024-01-17 21:52 UTC)

<p>No luck, I still get this error when zScaler is disabled:</p>
<p>[Qt] Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/65a664ce2aa6efa9ffee562e/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/65a664ce2aa6efa9ffee562e/download</a></p>
<p>I was able to pip_install(‘pyvista’) with no problem, though.</p>

---

## Post #11 by @mikebind (2024-01-17 21:59 UTC)

<p>However, if I put that URL into a web browser, it downloads a .zip file which I can use to install the extension from using the Extension Manager’s “Install from file” button. This process seems to work even with zScaler back on, and will be an acceptable workaround procedure for me.  Thanks for the help <a class="mention" href="/u/muratmaga">@muratmaga</a> !</p>

---

## Post #12 by @lassoan (2024-01-17 23:26 UTC)

<p>Heuristics in too agressive firewalls sometimes flag the communication between the extensions server frontend (hosted on netlify) and backend (girder server hosted at Kitware) suspicious and may block access to the backend server. You can avoid the frontend server and download an extension directly from the backend via using bookmarks:</p>
<ul>
<li>Open the Extensions Manager in Slicer</li>
<li>Click on the “wrench” icon in the top-right corner and select <code>Edit Bookmarks...</code></li>
<li>Add the names of the extensions that you want to install to the list (each extension in a new line)</li>
<li>Click <code>Install</code> button next to each extension’s name that you want to install (or click <code>Install bookmarked</code> to install all bookmarked extensions)</li>
</ul>
<p>If <code>Install</code> button is disabled then click <code>Check for updates</code> button to download the latest extension metadata descriptions from the server and then try installing again.</p>
<p>Let us know if this helped and then we add this instruction to the user manual.</p>

---

## Post #13 by @mikebind (2024-01-18 00:18 UTC)

<p>Thanks for the idea, unfortunately it didn’t help:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf531bb9eca917e41c43bff23f3115c8368681f.png" alt="image" data-base62-sha1="xFnwYrM1WJqXi2to2kJW3LoeyvB" width="503" height="230"></p>
<p>Checking for updates identified a newer version of SlicerVMTK, but I was not able to install updated version the normal way (same download error).  Instead I had to uninstall the existing SlicerVMTK and then install from browser-downloaded file.</p>
<p>However, I had not noticed the “Open Extensions Catalog Website” item on the wrench menu before.  That is a better and quicker option for manually downloading several extension zip files than copying URLs from error messages.</p>

---

## Post #14 by @mikebind (2024-01-18 00:31 UTC)

<p>One more thing which I had failed to mention so far but might be relevant for troubleshooting is that some period of time after a failed download (anywhere from 30s to several minutes later) I get another error message which shows up in the python interactor and in the error log:</p>
<p>[FD] [34152:27424:0117/162657.252:ERROR:dns_config_service_win.cc(793)] DNS config watch failed.</p>
<p>By the time I get this, the Extension Manager is closed, and I’m not doing anything related to trying to access the internet; it seems to be related to some monitoring which is happening in the background or some very extended time-out check, or something like that.</p>

---

## Post #15 by @muratmaga (2024-01-18 02:17 UTC)

<p>All I can say, on a properly configured SCH company laptop/desktop everything works fine (both on Mac and Windows) even behind the firewall. you might have to work with the IT to figure out the issue. Or simply do what I used to do, install everything outside of the company network, zip the folder and then copy it over to other computers.</p>

---

## Post #16 by @lassoan (2024-01-18 03:07 UTC)

<p>Thanks for testing. Downloading zip files from the extension manager in the web browser is a good workaround; and when you install from file you can select all the downloaded .zip files at once, so overall it is not too painful. But it would be nice if you could work with your IT team to figure out what caused the problem and share it here so that we can learn from it.</p>

---

## Post #17 by @mikebind (2024-01-18 16:29 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="15" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>All I can say, on a properly configured SCH company laptop/desktop everything works fine (both on Mac and Windows) even behind the firewall.</p>
</blockquote>
</aside>
<p>That’s good to know, thanks.</p>
<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>But it would be nice if you could work with your IT team to figure out what caused the problem and share it here so that we can learn from it.</p>
</blockquote>
</aside>
<p>I will open a ticket on this.  However, since it is a low priority problem with an easy workaround, I’m not sure how likely I am to get our IT people to spend time on it.  If we do figure it out, I will post back here.</p>
<p>Thank you both very much for your help on this, <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>

---

## Post #18 by @mau_igna_06 (2024-01-19 21:27 UTC)

<p>Hi</p>
<p>I do not see the Sandbox extension available <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/65aa4d8a2aa6efa9ffef881d" rel="noopener nofollow ugc">here</a>. Maybe it’s the same issue?</p>
<p>Hope you can help</p>
<p>PS: <a class="mention" href="/u/lassoan">@lassoan</a> could you split this into another topic?</p>

---

## Post #19 by @mikebind (2024-01-19 21:57 UTC)

<p>Thanks for taking a look, but I don’t think that was the issue yesterday.  I could access and download extensions from a laptop outside our corporate network without a problem, and the issue wasn’t limited to just the Sandbox extension for the affected computer. Furthermore, if I copied and pasted the exact same URL into a web browser on the affected computer, I could download the zip file and successfully install the extension from that.  So, I think the most likely explanation is that there is something which is getting blocked by the hospital network in the way the download is being triggered by the extension manager.  I will follow up with our IT department and see if it is possible to diagnose and resolve the issue. If we figure it out, I will post back here.</p>

---

## Post #20 by @lassoan (2024-01-19 22:09 UTC)

<p>The Sandbox extension looks all good, available on the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Sandbox">dashboard</a> and also on the backend server.</p>

---

## Post #21 by @mikebind (2024-01-25 17:40 UTC)

<p>After following up with our hospital IT, the problem was related to certificates.  As a preferably temporary solution, they added an exception to SSL inspection for <a href="http://slicer-packages.kitware.com">slicer-packages.kitware.com</a>.  This resolved the issue and enabled downloading of extensions via the extension manager.</p>
<p>However, they did ask me to investigate adding a certificate to Slicer so that they could remove this exception.  The discussions in this thread seem quite relevant:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19361">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361/1">New extension manager and issues with corporate certificates</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Today I downloaded a new preview version, and tried to install MoniaLabel and SlicerMorph on my work computers, and encountered this error: 

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over H…
  </blockquote>
</aside>

<p>but I have to admit I don’t really follow how this all works.  If I go to <a href="http://slicer.org">slicer.org</a> (as an example domain) in a browser and check the certificate viewer, the “Issued By” section says:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a129599bab1772a11c20b0b7027195b32bae7953.png" alt="image" data-base62-sha1="mZHsOBdggrlvNG2zX25asPNC4jF" width="542" height="121"></p>
<p>This was also the case for <a href="http://slicer-packages.kitware.com">slicer-packages.kitware.com</a> before the exception was added, and, if I am understanding correctly, it was the absence of this Zscaler certificate in the Slicer crt file which led to the failed download.  Zscaler is the software installed on hospital issued laptops for use outside the hospital network so that they can behave as if they are inside the hospital network (I would call this a VPN but since we’re actually talking about details of networking and security I don’t want to accidentally misuse a technical term).</p>
<p>I’d love to find a solution for this which both allowed the hospital to remove the exception for <a href="http://slicer-packages.kitware.com">slicer-packages.kitware.com</a> in their firewall AND allowed Slicer users inside the network to use the extension manager normally. I can try to rebuild Slicer.crt with an additional Zscaler certificate added following the thread linked above, but I don’t yet understand how to do that (and, as <a class="mention" href="/u/muratmaga">@muratmaga</a> pointed out, this isn’t a great general solution for clinical Slicer users who may not be technically savvy).  On the other thread, there is some discussion of “self-signed” certificates, but I am not sure how to tell if this certificate is self-signed or not.  The hospital IT person I worked with was competent and helpful, and I think would be willing to help me troubleshoot further if I knew what questions to be asking or what solutions to be trying.</p>
<p>I find some potentially helpful information on this page: <a href="https://help.zscaler.com/zia/choosing-ca-certificate-ssl-inspection" class="inline-onebox">Choosing the CA Certificate for SSL Inspection | Zscaler</a>.  I am guessing the hospital is using the first option, SSL Inspection Using Zscaler’s default intermediate CA certificate, which looks like it uses a dynamically generated and signed certificate.</p>
<p>Here are some options for moving forward:</p>
<ul>
<li>explore turning off ssl verification from the Slicer side of the connection so that Slicer does not cancel the download because it doesn’t recognize the zscaler certificate</li>
<li>explore adding the zscaler certificate to Slicer’s set of trusted certificates</li>
<li>explore having Slicer get the set of trusted certificates from the OS (or something like that) so that it will trust the zscaler certificate the same way the browser does</li>
<li>explore pushing to have the zscaler certificate added to the outside trusted repository that Slicer builds its list of trusted certificates from (looks like maybe mozilla?).  I think maybe this is essentially what is meant by having it not be self-signed?  However, if the certificate is being dynamically generated and signed and involves intercepting and inspecting traffic (see zscaler link above), this approach probably isn’t possible.</li>
</ul>
<p>Any suggestions about which of these I should pursue?  <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #22 by @lassoan (2024-01-25 19:36 UTC)

<p>Great detective work! I think this explains the all the issues that you have been experiencing.</p>
<p>It seems that ZScaler implements a man-in-the-middle attack on all external network communications. According <a href="https://geekingfrog.com/blog/post/corporate-man-in-the-middle">this blog post</a> ZScaler does not generate generally trustable certificates, just some temporary throwaway ones. The ZScaler agent running on the user’s computer receives these temporary certificates and regularly replaces them on the system.</p>
<p>I’m very surprised that hospitals go this far and doubt that this would be effective (if someone wants to hide something it is always possible to add yet another layer of encryption), while it surely introduces additional complexity and therefore extra cost and more vulnerabilities.</p>
<p>The issue may be due to the Slicer application not trusting the unknown ZScaler certificate but the man-in-the-middle attack might also interfere with the communication between the frontend and backend servers. Adding new certificates in Slicer application should not be hard, so if that is sufficient then we shoul definitely look into it. Adding exceptions or special certificates to the servers is not an option.</p>
<p>Based on these, comments on potential next steps:</p>
<blockquote>
<p>explore turning off ssl verification from the Slicer side of the connection so that Slicer does not cancel the download because it doesn’t recognize the zscaler certificate</p>
</blockquote>
<p>Turning off SSL verification would be quite risky, as man-in-the-middle attacks could allow malicious actors to get manipulated packages installed on user’s computers.</p>
<blockquote>
<p>explore adding the zscaler certificate to Slicer’s set of trusted certificates</p>
</blockquote>
<p>It would be interesting to try and see if adding the current ZScaler certificate to Slicer’s .crt file fixes extension installation using the “Manage” tag using bookmarks (in this case Slicer directly communnicates with the extension server backend) and/or installation by using the “Install” tab (in this case the extensions server frontend is involved as well).</p>
<blockquote>
<p>explore having Slicer get the set of trusted certificates from the OS (or something like that) so that it will trust the zscaler certificate the same way the browser does</p>
</blockquote>
<p>If the previous experiment is successful then we should explore this. Accessing the certificate store is depending on the operating system, but Qt or Python may provide some cross-platform API.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you know why Slicer brings its own .crt file (instead of trying to get the certificates from the operating system)?</p>
<blockquote>
<p>explore pushing to have the zscaler certificate added to the outside trusted repository that Slicer builds its list of trusted certificates from (looks like maybe mozilla?).</p>
</blockquote>
<p>Since these are temporary certificates, these cannot be added to any repository (by the time they were added they could be already replaced).</p>
<hr>
<p>I’ve found many links that complains about ZScaler breaking TLS in various applications and many solutions. A few useful links:</p>
<ul>
<li><a href="https://help.zscaler.com/zia/adding-custom-certificate-application-specific-trust-store" class="inline-onebox">Adding Custom Certificate to an Application Specific Trust Store | Zscaler</a></li>
<li><a href="https://community.zscaler.com/zenith/s/question/0D54u00009jZpG7CAK/installing-tls-ssl-root-certificates-to-nonstandard-environments">https://community.zscaler.com/zenith/s/question/0D54u00009jZpG7CAK/installing-tls-ssl-root-certificates-to-nonstandard-environments</a></li>
<li><a href="https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/non-standard-certs.html" class="inline-onebox">Using non-standard certificates — conda 23.11.1.dev66 documentation</a></li>
<li><a href="https://stackoverflow.com/questions/61635505/installing-zscaler-certificate-to-anaconda3" class="inline-onebox">ssl - Installing Zscaler Certificate to Anaconda3 - Stack Overflow</a></li>
</ul>

---

## Post #23 by @mikebind (2024-01-25 21:09 UTC)

<p>Thanks for the helpful guidance!  It sounds like the first thing for me to try is to add the ZScaler certificate to the Slicer .crt file.  As of right now, I don’t know how to obtain the ZScaler certificate or how to add it to the Slicer .crt file.</p>
<p>I see the readme at <a href="https://github.com/Slicer/Slicer/tree/main/Base/QTCore/Resources/Certs" class="inline-onebox">Slicer/Base/QTCore/Resources/Certs at main · Slicer/Slicer · GitHub</a> and see how the documentation there guides one to building Slicer.crt from data at <a href="https://raw.githubusercontent.com/mozilla/gecko-dev/master/security/nss/lib/ckfw/builtins/certdata.txt">https://raw.githubusercontent.com/mozilla/gecko-dev/master/security/nss/lib/ckfw/builtins/certdata.txt</a>.  Entries in that file look, for example, like this</p>
<pre><code class="lang-auto"># Trust for "Entrust.net Premium 2048 Secure Server CA"
# Issuer: CN=Entrust.net Certification Authority (2048),OU=(c) 1999 Entrust.net Limited,OU=www.entrust.net/CPS_2048 incorp. by ref. (limits liab.),O=Entrust.net
# Serial Number: 946069240 (0x3863def8)
# Subject: CN=Entrust.net Certification Authority (2048),OU=(c) 1999 Entrust.net Limited,OU=www.entrust.net/CPS_2048 incorp. by ref. (limits liab.),O=Entrust.net
# Not Valid Before: Fri Dec 24 17:50:51 1999
# Not Valid After : Tue Jul 24 14:15:12 2029
# Fingerprint (SHA-256): 6D:C4:71:72:E0:1C:BC:B0:BF:62:58:0D:89:5F:E2:B8:AC:9A:D4:F8:73:80:1E:0C:10:B9:C8:37:D2:1E:B1:77
# Fingerprint (SHA1): 50:30:06:09:1D:97:D4:F5:AE:39:F7:CB:E7:92:7D:7D:65:2D:34:31
CKA_CLASS CK_OBJECT_CLASS CKO_NSS_TRUST
CKA_TOKEN CK_BBOOL CK_TRUE
CKA_PRIVATE CK_BBOOL CK_FALSE
CKA_MODIFIABLE CK_BBOOL CK_FALSE
CKA_LABEL UTF8 "Entrust.net Premium 2048 Secure Server CA"
CKA_CERT_SHA1_HASH MULTILINE_OCTAL
\120\060\006\011\035\227\324\365\256\071\367\313\347\222\175\175
\145\055\064\061
END
CKA_CERT_MD5_HASH MULTILINE_OCTAL
\356\051\061\274\062\176\232\346\350\265\367\121\264\064\161\220
END
CKA_ISSUER MULTILINE_OCTAL
\060\201\264\061\024\060\022\006\003\125\004\012\023\013\105\156
\164\162\165\163\164\056\156\145\164\061\100\060\076\006\003\125
\004\013\024\067\167\167\167\056\145\156\164\162\165\163\164\056
\156\145\164\057\103\120\123\137\062\060\064\070\040\151\156\143
\157\162\160\056\040\142\171\040\162\145\146\056\040\050\154\151
\155\151\164\163\040\154\151\141\142\056\051\061\045\060\043\006
\003\125\004\013\023\034\050\143\051\040\061\071\071\071\040\105
\156\164\162\165\163\164\056\156\145\164\040\114\151\155\151\164
\145\144\061\063\060\061\006\003\125\004\003\023\052\105\156\164
\162\165\163\164\056\156\145\164\040\103\145\162\164\151\146\151
\143\141\164\151\157\156\040\101\165\164\150\157\162\151\164\171
\040\050\062\060\064\070\051
END
CKA_SERIAL_NUMBER MULTILINE_OCTAL
\002\004\070\143\336\370
END
CKA_TRUST_SERVER_AUTH CK_TRUST CKT_NSS_TRUSTED_DELEGATOR
CKA_TRUST_EMAIL_PROTECTION CK_TRUST CKT_NSS_TRUSTED_DELEGATOR
CKA_TRUST_CODE_SIGNING CK_TRUST CKT_NSS_MUST_VERIFY_TRUST
CKA_TRUST_STEP_UP_APPROVED CK_BBOOL CK_FALSE
</code></pre>
<p>I assume that what I need is the corresponding entry values for the ZScaler certificate.  Then it looks like I could run <code>make-ca.sh</code> to generate Slicer.crt.  Alternatively, it looks like I could just edit Slicer.crt directly; entries there look like:</p>
<pre><code class="lang-auto">Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 1246989352 (0x4a538c28)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, O = "Entrust, Inc.", OU = See www.entrust.net/legal-terms, OU = "(c) 2009 Entrust, Inc. - for authorized use only", CN = Entrust Root Certification Authority - G2
        Validity
            Not Before: Jul  7 17:25:54 2009 GMT
            Not After : Dec  7 17:55:54 2030 GMT
        Subject: C = US, O = "Entrust, Inc.", OU = See www.entrust.net/legal-terms, OU = "(c) 2009 Entrust, Inc. - for authorized use only", CN = Entrust Root Certification Authority - G2
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:ba:84:b6:72:db:9e:0c:6b:e2:99:e9:30:01:a7:
                    76:ea:32:b8:95:41:1a:c9:da:61:4e:58:72:cf:fe:
                    f6:82:79:bf:73:61:06:0a:a5:27:d8:b3:5f:d3:45:
                    4e:1c:72:d6:4e:32:f2:72:8a:0f:f7:83:19:d0:6a:
                    80:80:00:45:1e:b0:c7:e7:9a:bf:12:57:27:1c:a3:
                    68:2f:0a:87:bd:6a:6b:0e:5e:65:f3:1c:77:d5:d4:
                    85:8d:70:21:b4:b3:32:e7:8b:a2:d5:86:39:02:b1:
                    b8:d2:47:ce:e4:c9:49:c4:3b:a7:de:fb:54:7d:57:
                    be:f0:e8:6e:c2:79:b2:3a:0b:55:e2:50:98:16:32:
                    13:5c:2f:78:56:c1:c2:94:b3:f2:5a:e4:27:9a:9f:
                    24:d7:c6:ec:d0:9b:25:82:e3:cc:c2:c4:45:c5:8c:
                    97:7a:06:6b:2a:11:9f:a9:0a:6e:48:3b:6f:db:d4:
                    11:19:42:f7:8f:07:bf:f5:53:5f:9c:3e:f4:17:2c:
                    e6:69:ac:4e:32:4c:62:77:ea:b7:e8:e5:bb:34:bc:
                    19:8b:ae:9c:51:e7:b7:7e:b5:53:b1:33:22:e5:6d:
                    cf:70:3c:1a:fa:e2:9b:67:b6:83:f4:8d:a5:af:62:
                    4c:4d:e0:58:ac:64:34:12:03:f8:b6:8d:94:63:24:
                    a4:71
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Subject Key Identifier:
                6A:72:26:7A:D0:1E:EF:7D:E7:3B:69:51:D4:6C:8D:9F:90:12:66:AB
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        79:9f:1d:96:c6:b6:79:3f:22:8d:87:d3:87:03:04:60:6a:6b:
        9a:2e:59:89:73:11:ac:43:d1:f5:13:ff:8d:39:2b:c0:f2:bd:
        4f:70:8c:a9:2f:ea:17:c4:0b:54:9e:d4:1b:96:98:33:3c:a8:
        ad:62:a2:00:76:ab:59:69:6e:06:1d:7e:c4:b9:44:8d:98:af:
        12:d4:61:db:0a:19:46:47:f3:eb:f7:63:c1:40:05:40:a5:d2:
        b7:f4:b5:9a:36:bf:a9:88:76:88:04:55:04:2b:9c:87:7f:1a:
        37:3c:7e:2d:a5:1a:d8:d4:89:5e:ca:bd:ac:3d:6c:d8:6d:af:
        d5:f3:76:0f:cd:3b:88:38:22:9d:6c:93:9a:c4:3d:bf:82:1b:
        65:3f:a6:0f:5d:aa:fc:e5:b2:15:ca:b5:ad:c6:bc:3d:d0:84:
        e8:ea:06:72:b0:4d:39:32:78:bf:3e:11:9c:0b:a4:9d:9a:21:
        f3:f0:9b:0b:30:78:db:c1:dc:87:43:fe:bc:63:9a:ca:c5:c2:
        1c:c9:c7:8d:ff:3b:12:58:08:e6:b6:3d:ec:7a:2c:4e:fb:83:
        96:ce:0c:3c:69:87:54:73:a4:73:c2:93:ff:51:10:ac:15:54:
        01:d8:fc:05:b1:89:a1:7f:74:83:9a:49:d7:dc:4e:7b:8a:48:
        6f:8b:45:f6
SHA1 Fingerprint=8C:F4:27:FD:79:0C:3A:D1:66:06:8D:E8:1E:57:EF:BB:93:22:72:D4
-----BEGIN CERTIFICATE-----
MIIEPjCCAyagAwIBAgIESlOMKDANBgkqhkiG9w0BAQsFADCBvjELMAkGA1UEBhMC
VVMxFjAUBgNVBAoTDUVudHJ1c3QsIEluYy4xKDAmBgNVBAsTH1NlZSB3d3cuZW50
cnVzdC5uZXQvbGVnYWwtdGVybXMxOTA3BgNVBAsTMChjKSAyMDA5IEVudHJ1c3Qs
IEluYy4gLSBmb3IgYXV0aG9yaXplZCB1c2Ugb25seTEyMDAGA1UEAxMpRW50cnVz
dCBSb290IENlcnRpZmljYXRpb24gQXV0aG9yaXR5IC0gRzIwHhcNMDkwNzA3MTcy
NTU0WhcNMzAxMjA3MTc1NTU0WjCBvjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUVu
dHJ1c3QsIEluYy4xKDAmBgNVBAsTH1NlZSB3d3cuZW50cnVzdC5uZXQvbGVnYWwt
dGVybXMxOTA3BgNVBAsTMChjKSAyMDA5IEVudHJ1c3QsIEluYy4gLSBmb3IgYXV0
aG9yaXplZCB1c2Ugb25seTEyMDAGA1UEAxMpRW50cnVzdCBSb290IENlcnRpZmlj
YXRpb24gQXV0aG9yaXR5IC0gRzIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQC6hLZy254Ma+KZ6TABp3bqMriVQRrJ2mFOWHLP/vaCeb9zYQYKpSfYs1/T
RU4cctZOMvJyig/3gxnQaoCAAEUesMfnmr8SVycco2gvCoe9amsOXmXzHHfV1IWN
cCG0szLni6LVhjkCsbjSR87kyUnEO6fe+1R9V77w6G7CebI6C1XiUJgWMhNcL3hW
wcKUs/Ja5CeanyTXxuzQmyWC48zCxEXFjJd6BmsqEZ+pCm5IO2/b1BEZQvePB7/1
U1+cPvQXLOZprE4yTGJ36rfo5bs0vBmLrpxR57d+tVOxMyLlbc9wPBr64ptntoP0
jaWvYkxN4FisZDQSA/i2jZRjJKRxAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAP
BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBRqciZ60B7vfec7aVHUbI2fkBJmqzAN
BgkqhkiG9w0BAQsFAAOCAQEAeZ8dlsa2eT8ijYfThwMEYGprmi5ZiXMRrEPR9RP/
jTkrwPK9T3CMqS/qF8QLVJ7UG5aYMzyorWKiAHarWWluBh1+xLlEjZivEtRh2woZ
Rkfz6/djwUAFQKXSt/S1mja/qYh2iARVBCuch38aNzx+LaUa2NSJXsq9rD1s2G2v
1fN2D807iDginWyTmsQ9v4IbZT+mD12q/OWyFcq1rca8PdCE6OoGcrBNOTJ4vz4R
nAuknZoh8/CbCzB428Hch0P+vGOaysXCHMnHjf87ElgI5rY97HosTvuDls4MPGmH
VHOkc8KT/1EQrBVUAdj8BbGJoX90g5pJ19xOe4pIb4tF9g==
-----END CERTIFICATE-----
</code></pre>
<p>Those seem like they have a relatively straightforward structure, so I probably just need to know how to obtain the information for the current ZScaler certificate.  Is there an easy way to do that?</p>

---

## Post #24 by @lassoan (2024-01-25 21:20 UTC)

<p>Since ZScaler hijacks every site, of you open any site on your web browser and click on the site information button in the browser then you will get the ZScaler certificate. You should be able to copy or export the certification from the browser that can be imported into the crt file.</p>
<p>You could also experent if you can use some Qt API (such as <a href="https://doc.qt.io/qt-6/qsslconfiguration.html" class="inline-onebox">QSslConfiguration Class | Qt Network 6.6.1</a>) to retrieve some default system certificates.</p>

---

## Post #25 by @muratmaga (2024-01-25 23:04 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="21" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Any suggestions about which of these I should pursue? <a class="mention" href="/u/lassoan">@lassoan</a></p>
</blockquote>
</aside>
<p>A simple solution that I have been using is to turn off zscaler when I need to run Slicer.</p>

---

## Post #26 by @jamesobutler (2024-01-26 03:16 UTC)

<p>Thanks for the investigation into this. My group has also been struggling with this issue of installing Slicer extensions. We are not part of a hospital network, but we are part of a large enterprise Life Sciences company. Our company-issued laptops have ZScaler on them which is active when we are home and not connected to the corporate network. The issue of installing Slicer extension is not a problem when I’m in the office and ZScaler is not active.</p>
<p>I must say I am a bit confused about what to do next about the ZScaler cert. Navigating all the menus in Chrome is quite a task to figure out. This information should then be added to the file at the “…\Slicer 5.6.1\share\Slicer-5.6\Slicer.crt” location?</p>

---

## Post #27 by @muratmaga (2024-01-26 04:02 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> can’t you disable the Zscaler when you are outside of campus and not actively accessing their intranet? For me that solution works.</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> I think your original issue what the lack of proper certificates on the computer itself. Now that’s taken care of, do try turning off the zscaler (you shouldn’t need zscaler when you are on campus anyways). I have been using that method for 1.5 years successfully.</p>

---

## Post #28 by @mikebind (2024-01-26 20:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="27" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think your original issue what the lack of proper certificates on the computer itself</p>
</blockquote>
</aside>
<p>I don’t think so.  No changes were made on my computer that I am aware of.  Instead, I believe what happened was that <a href="http://slicer-packages.kitware.com">slicer-packages.kitware.com</a> was added to a whitelist of domains which are not run through the Zscaler inspection at the institution level. When Zscaler is on, nearly all network traffic is routed through it, as can be confirmed by checking the certificate hierarchy in a browser visiting a random web page, everything has a Zscaler certificate.  However, after the change, the kitware package site no longer has a Zscaler certificate in the hierarchy. Based on this information, I think you are probably correct that turning Zscaler off may be a viable strategy for installing extensions.  However, when I tried it just now, I get the same type of error in Slicer, and I still see Zscaler certificates in the browser, so I think that there is maybe some lingering of settings (maybe some of this stuff is cached?).  Restarting Slicer didn’t change anything, and I haven’t tried restarting the computer yet.  I work from home nearly all the time, and use the intranet over Zscaler nearly all the time.  It is worth it to me to spend some troubleshooting effort to see if it’s possible to resolve this so that it “just works”.</p>
<aside class="quote no-group" data-username="lassoan" data-post="24" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since ZScaler hijacks every site, of you open any site on your web browser and click on the site information button in the browser then you will get the ZScaler certificate. You should be able to copy or export the certification from the browser that can be imported into the crt file.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> , I am still unclear about how to modify the Slicer.crt.  As you suggest, in Chrome, on a site, I can get to a button to export a certificate, and that generates a .crt file, but the only thing in it is the block of characters between —BEGIN CERTIFICATE— and —END CERTIFICATE— tags.  Is it sufficient to paste that at the bottom of the Slicer.crt file? Or is the metadata section which seems to be present for all other certificates (the version, the serial number, signature algorthim, etc) also required?  Also, there seem to be multiple levels of certificates in a hierarchy, do I need to add all of them?</p>
<p>I can no longer use the extension manager for testing, since the exception is now in place allowing that domain to skip zscaler.  So, I have been using <a href="http://discourse.slicer.org">discourse.slicer.org</a> as the test url instead, which still gives an SSL handshake error.</p>
<pre><code class="lang-auto">def testURL(url):
  request = qt.QNetworkRequest(url)
  manager = qt.QNetworkAccessManager()
  reply = manager.get(request)

  while (not reply.isFinished()):
    slicer.app.processEvents()
	
  print(f"HTTP response code: {reply.attribute(qt.QNetworkRequest.HttpStatusCodeAttribute)}")
  print(f"Error code: {reply.error()}") 
  print(f"ErrorString: {reply.errorString()}")
  #print(reply.readAll())
  return reply


failingURL = qt.QUrl("https://discourse.slicer.org") # no exception for zscaler, ssl handshake fails
passingURL = qt.QUrl("https://slicer-packages.kitware.com") # exception in place for zscaler, data returned
</code></pre>
<p>The passingURL returns response code 200 and the html content of the page.  The failingURL returns</p>
<pre><code class="lang-auto">HTTP response code: None
Error code: 6
ErrorString: SSL handshake failed
</code></pre>
<p>So, I think this method seems like it will work for checking if a sufficient set of certificates has been added to Slicer.crt.  I tried pasting what I got out of Chrome into the bottom of Slicer.crt, restarted Slicer, and ran this test, with no change in result.  However, I don’t know if that is because I grabbed the wrong certificate (maybe I need all the certificates in the hierarchy? or just the top one? or just the bottom one?) or if it is because the certificate I tried to add was ignored because it was missing metadata or otherwise was not the proper format.  For testing, do I need to restart Slicer every time I modify Slicer.crt, or is that dynamically checked each time?  If there is a malformed certificate added, will any errors show up (I don’t see anything obvious in the error log, but I might also have missed something)?</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="26" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Navigating all the menus in Chrome is quite a task to figure out.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>, to get the certificate from Chrome, I click this button next to the url in the browser window <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38ad107ceb0c8eca401b1ade51d059ed04bd9f64.png" alt="image" data-base62-sha1="85nwGgGqma6OW8kuyynxm3trbj6" width="213" height="88">, then click “Connection is secure &gt;”, then “Certificate is valid”, which pops up a window, then click on the “Details” tab, and there, there is an “Export” button in the lower right.   Just discovered as I was writing this out for you that in the “Export” window, it is possible to change the file type from single certificate to certificate chain:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dc78bf502a1a8f40de97ec09ecba980e9b8e38e.png" alt="image" data-base62-sha1="4frn9HwSAOY32qlC9x8DvBpG5j0" width="556" height="181"><br>
If I do this, for the slicer discourse site, I get a chain of four certificates, only the begin/end certificate blocks, no other metadata. I’ll try pasting this at the end of the Slicer.crt file and see if that works.  It did not, same error on the failingURL.</p>

---

## Post #29 by @mikebind (2024-01-26 21:35 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="28" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>and I still see Zscaler certificates in the browser, so I think that there is maybe some lingering of settings (maybe some of this stuff is cached?)</p>
</blockquote>
</aside>
<p>It turns out I wasn’t fully turning Zscaler off, just one component of it.  Once fully turned off, the Zscaler certificates no longer show up in the browser and the failingURL above no longer gives an error in Slicer.</p>
<p>It remains true that adding the 4 certificates (just the begin/end blocks) exported from Chrome to the Slicer.crt file does not allow access from Slicer whenever Zscaler is on.</p>
<p>So, it seems like turning Zscaler off when using the Extension manager is likely a functional workaround in general.  In pursuit of a non-workaround solution, I’m not sure what to try next…</p>

---

## Post #30 by @muratmaga (2024-01-26 22:16 UTC)

<p>Yes, I do not individually turn off Zscaler component, I completely sign off and exit the application.</p>

---

## Post #31 by @jcfr (2024-01-26 22:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="22" data-topic="33809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you know why Slicer brings its own .crt file (instead of trying to get the certificates from the operating system)?</p>
</blockquote>
</aside>
<p>At the time it was implemented, it was the simplest way to have certificates across all platform. The <code>Slicer.crt</code> is generated from the Mozilla certificates similarly to the ones distributed through <a href="https://github.com/certifi/python-certifi">python-certifi</a>. They are also automatically maintained up-to-date using the <a href="https://github.com/Slicer/Slicer/blob/main/.github/workflows/update-slicer-certificate-bundle.yml">update-slicer-certificate-bundle.yml</a> GitHub workflow.</p>
<p>We could revisit this so that Python, CURL and Qt all use certificates when from the system store on platform supporting it.</p>

---
