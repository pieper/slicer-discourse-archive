---
topic_id: 18661
title: "Vmtk Not Found After Download"
date: 2021-07-13
url: https://discourse.slicer.org/t/18661
---

# VMTK not found after download

**Topic ID**: 18661
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/vmtk-not-found-after-download/18661

---

## Post #1 by @AshvinGupta (2021-07-13 08:45 UTC)

<p>Hello! After downloading the new preview version of Slicer every time I try to use the VMTK extension I get the same error message: “VMTK library is not found.” This is quite odd as when I go to extensions manager, it says that SlicerVMTK is installed.<br>
Also if I try to access the older version of slicer and download VMTK I get the error seen below or then when I do mange to download it, “VMTK library is not found.” Any help on this would be greatly appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c61dc55dd1a97d92b6bff6f4e21d2156dd23c1b2.png" data-download-href="/uploads/short-url/sgCk29VeOO4rQv7bWLSCxb0XKwO.png?dl=1" title="Screenshot 2021-07-13 at 10.08.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c61dc55dd1a97d92b6bff6f4e21d2156dd23c1b2_2_690x489.png" alt="Screenshot 2021-07-13 at 10.08.20" data-base62-sha1="sgCk29VeOO4rQv7bWLSCxb0XKwO" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c61dc55dd1a97d92b6bff6f4e21d2156dd23c1b2_2_690x489.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c61dc55dd1a97d92b6bff6f4e21d2156dd23c1b2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c61dc55dd1a97d92b6bff6f4e21d2156dd23c1b2.png 2x" data-dominant-color="F4F3E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-07-13 at 10.08.20</span><span class="informations">916×650 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-13 15:14 UTC)

<p>VMTK is available for latest Slicer Stable Release and latest Slicer Preview Release. The errors that you show in the screenshot above are due to instability of the extension server. The server will be replaced later this week, until then a workaround is to retry a few hours later.</p>
<p>If you installed the VMTK extension but modules do not show up or work properly then please upload the application log (menu: Help / Report a bug) somewhere and post the download link here so that we can investigate.</p>

---

## Post #4 by @AshvinGupta (2021-07-14 09:01 UTC)

<p><a href="https://drive.google.com/file/d/1SAK6LiwYOtzvqS6BPxAvlM_grkpJraqo/view?usp=sharing" rel="noopener nofollow ugc">VMTK bug</a></p>

---

## Post #5 by @AshvinGupta (2021-07-23 13:39 UTC)

<p>Has there been any update on this? I tried downloading the latest version and trying again but get the following error messages:<br>
[DEBUG][Qt] 23.07.2021 14:31:18 [] (unknown:0) - Additional module paths …: Extensions-30058/SlicerVMTK/lib/Slicer-4.13/qt-loadable-modules, Extensions-30058/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules<br>
[CRITICAL][Qt] 23.07.2021 14:31:19 [] (unknown:0) -   Error(s):<br>
CLI executable: /Applications/Slicer.app/Contents/Extensions-30058/SlicerVMTK/lib/Slicer-4.13/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 23.07.2021 14:31:19 [] (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 23.07.2021 14:31:19 [] (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 23.07.2021 14:31:19 [] (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 23.07.2021 14:31:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations</p>

---

## Post #6 by @lassoan (2021-08-09 19:15 UTC)

<p>Thank you for your patience. You can use VMTK on other platforms (Windows/Linux) and we’ll fix it in the latest Slicer Stable Release, too - see progress here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/37">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">VMTK gone missing recently in Slicer-4.11.20210226</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="19:08:54" data-timezone="UTC">07:08PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The extension installation package does not contain VMTK binaries, only the Slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er module .py files.

It seems that the recent upgrade to VTK9 broke packaging for VTK-8.2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #7 by @AmandineG (2023-02-20 13:53 UTC)

<p>Hi!</p>
<p>I have this error message today :<br>
[Qt]   Error(s):<br>
[Qt]     CLI executable: /Applications/Slicer.app/Contents/Extensions-31317/SlicerVMTK/lib/Slicer-5.2/qt-loadable-modules/vtkvmtk.py<br>
[Qt]     The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[Qt] Fail to instantiate module  “vtkvmtk”<br>
[Qt] The following modules failed to be instantiated:<br>
[Qt]    vtkvmtk</p>
<p>This extension worked very well until now.<br>
I have the latest Slicer Stable Release.<br>
I have uninstalled and reinstalled the extension with restarts of 3D slicer but the same error message remains.</p>
<p>How can I get it to work again without error?</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2023-03-02 06:28 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="7" data-topic="18661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.</p>
</blockquote>
</aside>
<p>This is a false alarm, you can safely ignore it. See more details <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22">here</a>.</p>
<p>Do you find any issues when you are using VMTK in Slicer?</p>

---
