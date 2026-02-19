---
topic_id: 41016
title: "Different Slicerrt Behavior When Changing Windows To Linux S"
date: 2025-01-09
url: https://discourse.slicer.org/t/41016
---

# Different SlicerRT behavior when changing Windows to Linux system

**Topic ID**: 41016
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/different-slicerrt-behavior-when-changing-windows-to-linux-system/41016

---

## Post #1 by @Fabio_Lunelli (2025-01-09 16:52 UTC)

<p><strong>Hi there,</strong></p>
<p>I am using 3D Slicer with the SlicerRT extension to simulate radiotherapy (RT) planning. My workflow involves importing two folders into Slicer:</p>
<ol>
<li>One containing the DICOM images.</li>
<li>One containing the contoured structures.</li>
</ol>
<p>When I used a Windows system, importing these two folders displayed both the DICOM images and the contours/structures overlayed correctly.</p>
<p>However, now that I’ve switched to a Linux system, only the DICOM images are visible. Although the structure folder is listed in the series, the contours do not appear on the screen.</p>
<p>Do you have any suggestions for resolving this issue?</p>

---

## Post #2 by @pieper (2025-01-09 17:55 UTC)

<p>That’s odd - they should work the same.  Did you confirm you have the same software versions?  Also check the log files for any messages during import or display.</p>

---

## Post #3 by @Fabio_Lunelli (2025-01-09 23:32 UTC)

<p>I tested the same versions of the software on a Windows system, and it worked successfully. To assist in diagnosing the problem, I am attaching two screenshots of the messages that appear during the display process. These messages do not occur in the Windows version. Could this suggest that the issue is related to the Slicer RT extension on Linux? I attempted to uninstall and reinstall the extension, but the issue persists.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43ef507886d634f65a79f5d49249287496d90b46.png" data-download-href="/uploads/short-url/9GYIAk4ROM7Sopf99bRlDgcswYu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43ef507886d634f65a79f5d49249287496d90b46.png" alt="image" data-base62-sha1="9GYIAk4ROM7Sopf99bRlDgcswYu" width="577" height="237"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×237 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e3e589f462a1d95efb7ce930d329af453c97f3e.png" data-download-href="/uploads/short-url/i0NJInBhGhkLO3LduvmOzy76CZw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e3e589f462a1d95efb7ce930d329af453c97f3e.png" alt="image" data-base62-sha1="i0NJInBhGhkLO3LduvmOzy76CZw" width="325" height="121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">325×121 8.67 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2025-01-09 23:41 UTC)

<p>I’ll let any SlicerRT users or developers comment on if they have any reason to think windows would be different from linux in this regard (seems very unlikely to me).</p>
<p>But based on this message I would guess the data perhaps didn’t copy correctly between your windows and linux machines.  You could check the file sizes and content outside of Slicer to confirm.</p>

---

## Post #5 by @Fabio_Lunelli (2025-01-10 00:16 UTC)

<p>I understand. But thank you for the help. I’ll wait to see if someone has a solution.</p>

---

## Post #6 by @Fabio_Lunelli (2025-01-10 04:15 UTC)

<p>After thoroughly reviewing the data used on both Linux and Windows machines, I found no missing components. To ensure consistency, I copied the exact same data from the Windows machine to the Linux environment. Despite this effort, the warnings persist. Could this potentially be a bug?</p>

---

## Post #7 by @cpinter (2025-01-10 09:30 UTC)

<p>There is a packaging issue on Linux.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/SlicerRT/issues/262">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/issues/262" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/262" target="_blank" rel="noopener">SlicerRT deployment fails on Linux</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-12-16" data-time="15:44:54" data-timezone="UTC">03:44PM - 16 Dec 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          high priority
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See this forum comment: https://discourse.slicer.org/t/segment-statistics-module<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">-on-3d-slicer-5-6-2/40714/8?u=cpinter

Basically the vtkIECTransformLogic binary is deployed to its own directory instead of `Slicer-5.7/qt-loadable-modules`.

@ferdymercury Since you worked on this on Linux, can you please take a look at this problem? Please let me know if you cannot for some reason. Thank you!</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please hang on, or if you have the possibility to try and help we’d appreciate that too.</p>

---

## Post #8 by @Fabio_Lunelli (2025-01-10 23:38 UTC)

<p>Thank you for your efforts in solving this problem. I will continue to monitor the progress closely. As I have a Windows machine with SlicerRT functioning properly, please feel free to reach out if there is any way I can assist. I will do my best to help in any way I can.</p>

---

## Post #9 by @cpinter (2025-01-16 12:29 UTC)

<p>The fix is integrated, but it seems that there are no Windows nor Linux builds of extensions for a few days now. <a class="mention" href="/u/jcfr">@jcfr</a> do you know anything about this? Thanks!</p>

---
