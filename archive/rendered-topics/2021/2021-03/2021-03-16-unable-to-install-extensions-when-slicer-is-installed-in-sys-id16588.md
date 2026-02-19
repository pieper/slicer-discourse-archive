---
topic_id: 16588
title: "Unable To Install Extensions When Slicer Is Installed In Sys"
date: 2021-03-16
url: https://discourse.slicer.org/t/16588
---

# Unable to install extensions when Slicer is installed in system location

**Topic ID**: 16588
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/unable-to-install-extensions-when-slicer-is-installed-in-system-location/16588

---

## Post #1 by @jamesobutler (2021-03-16 23:56 UTC)

<p>I have packaged and installed Slicer 4.13.0-2021-03-16 (from a local build) into a system location for all users at “C:/Program Files/Slicer 4.13.0-2021-03-16”, however I’m unable to install extensions.</p>
<p>The following message appears in the console output at startup.</p>
<pre><code class="lang-auto">"Failed to create extensions directory" "C:/Program Files/Slicer 4.13.0-2021-03-16/bin/../NA-MIC/Extensions-29780"
</code></pre>
<p>This message shows when opening the extensions manager.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23f72e42b87596a585151903a1a2bd127c323bc5.png" data-download-href="/uploads/short-url/58aicVmi8L33KrrL1ieLObzaSe9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f72e42b87596a585151903a1a2bd127c323bc5_2_690x376.png" alt="image" data-base62-sha1="58aicVmi8L33KrrL1ieLObzaSe9" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f72e42b87596a585151903a1a2bd127c323bc5_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f72e42b87596a585151903a1a2bd127c323bc5_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f72e42b87596a585151903a1a2bd127c323bc5_2_1380x752.png 2x" data-dominant-color="FCFCFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1049 78.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2021-03-17 04:27 UTC)

<p>The main reason for installing extensions in the application home folder is that Python packages are installed there anyway, so the application home folder has to be writable (or Slicer has to be run as admin when you install extensions). It also allows making Slicer fully portable - see details <a href="https://github.com/Slicer/Slicer/commit/008f8b9571452334e1d7a55cd5a13ec074905963">here</a>.</p>
<p>If you want to allow any user to install extensions without admin rights and you only need to use extensions that don’t install Python packages at runtime then you can specify a custom extension install path folder in Slicer-NNN.ini file or revert to the old behavior of Slicer by specifying<br>
Slicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR:BOOL=OFF when configuring your Slicer build.</p>

---

## Post #3 by @lassoan (2021-07-13 18:16 UTC)

<p>A post was split to a new topic: <a href="/t/deploying-slicer-in-an-immutable-container-singularity/18702">Deploying slicer in an immutable container (Singularity)</a></p>

---
