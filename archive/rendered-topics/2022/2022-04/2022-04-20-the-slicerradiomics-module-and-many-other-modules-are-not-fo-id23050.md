# The slicerRadiomics module and many other modules are not found in the latest version

**Topic ID**: 23050
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/the-slicerradiomics-module-and-many-other-modules-are-not-found-in-the-latest-version/23050

---

## Post #1 by @lrc_09 (2022-04-20 13:59 UTC)

<p>Hi, 3Dslicer give me much more help and I appreciate it. However, The slicerRadiomics module and many other modules are not found in the latest version 4.13.0 revision 30789, are the modules deleted in the new version.</p>

---

## Post #2 by @rbumm (2022-04-20 15:42 UTC)

<aside class="quote no-group" data-username="lrc_09" data-post="1" data-topic="23050">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lrc_09/48/15099_2.png" class="avatar"> lrc_09:</div>
<blockquote>
<p>many other modules</p>
</blockquote>
</aside>
<p>Which modules are you missing?</p>
<p>Concerning Slicerradiomics - the <a href="https://www.radiomics.io/slicerradiomics.html">Slicerradiomics homepage</a> says:<br>
“Pending resolution of packaging issues, SlicerRadiomics is not currently distributed as an extension via the 3D Slicer ExtensionManager. You can however use this extension if you build SlicerRadiomics from source.”<br>
<a href="https://github.com/AIM-Harvard/SlicerRadiomics">Github link</a></p>
<p>All this may be due to Slicer 5 being on the horizon.</p>

---

## Post #3 by @lassoan (2022-04-20 15:59 UTC)

<p>SlicerRadimics is the last major issue preventing releasing Slicer5 (see list of open issues <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Slicer+4.13%22">here</a>). Hopefully <a class="mention" href="/u/jcfr">@jcfr</a> can come up with a solution very soon.</p>

---

## Post #4 by @lrc_09 (2022-04-26 12:19 UTC)

<p>Thank you sir. I’ve found the modules in the latest version.</p>

---

## Post #5 by @lrc_09 (2022-04-26 12:21 UTC)

<p>Thank you sir. I’ve found the modules in the latest version. Very much looking forward to the release of Slicer version 5.</p>

---

## Post #6 by @Ywatana29 (2022-06-13 00:43 UTC)

<p>To Irc_09,<br>
Which version of 3D slicer are you using? I cannot find SlicerRadiomics  in the Extension Manager list. My 3D slicer is 5.1.0 Nightly version.</p>

---

## Post #7 by @lassoan (2022-06-13 12:55 UTC)

<p>Please check if this information helps:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extension-is-not-found-for-current-slicer-version" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extension-is-not-found-for-current-slicer-version</a></p>

---

## Post #8 by @Ywatana29 (2022-06-13 23:24 UTC)

<p>Well. This is not helpful. I saw that SlicerRadiomics is now on the Extension Manager list. But, it is not installable.<br>
I need step-by-step instructions for installing that module.<br>
Thanks.<br>
Yoichi</p>

---

## Post #9 by @pieper (2022-06-13 23:34 UTC)

<p>I just checked and Radiomics is available and installs fine for the 5.0.2 version on linux.</p>

---

## Post #10 by @jcfr (2022-06-14 06:27 UTC)

<aside class="quote no-group" data-username="Ywatana29" data-post="8" data-topic="23050">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ywatana29/48/9178_2.png" class="avatar"> Ywatana29:</div>
<blockquote>
<p>But, it is not installable</p>
</blockquote>
</aside>
<p>Thanks for reaching out and sorry that the troubleshooting information linked by <a class="mention" href="/u/lassoan">@lassoan</a> were not helpful.</p>
<p>To effectively move forward, you would need to provide more details regarding the error (e.g screenshot error messages, …)</p>

---

## Post #11 by @lassoan (2022-06-21 15:26 UTC)

<p>2 posts were split to a new topic: <a href="/t/radiomics-module-panel-is-blank/23989">Radiomics module panel is blank</a></p>

---

## Post #12 by @rbumm (2022-06-21 20:32 UTC)

<p>Radiomics was easy to install and works well in 5.1.0-2022-06-19 r31036 / 5ecfcc3<br>
(Windows 11)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f08668bc336dbc66fecbf8dfc05d55d3df6f57c.png" data-download-href="/uploads/short-url/8ZC4SOHyPAASl65NA9fZZb817ze.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f08668bc336dbc66fecbf8dfc05d55d3df6f57c_2_690x360.png" alt="image" data-base62-sha1="8ZC4SOHyPAASl65NA9fZZb817ze" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f08668bc336dbc66fecbf8dfc05d55d3df6f57c_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f08668bc336dbc66fecbf8dfc05d55d3df6f57c_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f08668bc336dbc66fecbf8dfc05d55d3df6f57c_2_1380x720.png 2x" data-dominant-color="BCBCBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1004 384 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Ywatana29 (2022-12-02 04:14 UTC)

<p>SlicerRadiomics for Windows is now with version 5.3.0-2022.</p>

---
