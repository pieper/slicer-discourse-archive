# How to use Linux compile the 3DSLicer source code

**Topic ID**: 24028
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/how-to-use-linux-compile-the-3dslicer-source-code/24028

---

## Post #1 by @wangyuyuyujun (2022-06-24 14:08 UTC)

<p>Hello,everyone!I have encountered some installation problems. I hope you can help me.<br>
I want to install 3DSlicer(version:5.0.2).At present, I have successfully installed Qt5 (version:5.12.1or5.13.0) and other dependencies. When I execute cmake/ After slicer-5.0.2/, the system reported the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ea0cd8306bf25669cf16f45bbc6b8d140b33fed.png" data-download-href="/uploads/short-url/4mWQev1IgrjjcrRWPkjPwVAVQlL.png?dl=1" title="YFA6AQ8L8LDN6H6(%1~$P" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ea0cd8306bf25669cf16f45bbc6b8d140b33fed.png" alt="YFA6AQ8L8LDN6H6(%1~$P" data-base62-sha1="4mWQev1IgrjjcrRWPkjPwVAVQlL" width="608" height="500" data-dominant-color="141414"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">YFA6AQ8L8LDN6H6(%1~$P</span><span class="informations">911×749 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I configured the environment variables:<br>
export Qt5_DIR=/usr/local/3Dslicer/qt5<br>
export PATH=/usr/local/3Dslicer/qt5/bin:$PATH<br>
export MANPATH=$Qt5_DIR/man:$MANPATH<br>
export LD_LIBRARY_PATH=$Qt5_DIR/lib:$LD_LIBRARY_PATH</p>
<p>Tried again,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b01f1d21b8b24acf25f0ac5ce4ec52db99a0109.png" data-download-href="/uploads/short-url/3QV3B0vDHQzA65Mx5vJqCmMJUbD.png?dl=1" title="EMZXT3RKMHZX1HPV~BH7_VS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b01f1d21b8b24acf25f0ac5ce4ec52db99a0109.png" alt="EMZXT3RKMHZX1HPV~BH7_VS" data-base62-sha1="3QV3B0vDHQzA65Mx5vJqCmMJUbD" width="690" height="407" data-dominant-color="0F0E0E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">EMZXT3RKMHZX1HPV~BH7_VS</span><span class="informations">1174×693 25.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
There are still two components not found,<br>
I don’t know what’s wrong. I’m looking forward to your reply.</p>

---

## Post #2 by @lassoan (2022-06-24 16:45 UTC)

<p>You need to install (or build) Qt with webengine component enabled.</p>

---

## Post #3 by @wangyuyuyujun (2022-06-26 12:15 UTC)

<p>Thank you for your reply. I installed all modules by default when installing Qt5, but webengine was not compiled, so the installation failed. I don’t know what went wrong</p>

---

## Post #4 by @lassoan (2022-06-26 20:17 UTC)

<p>Webengine component might not be enabled by default. You can run the Qt install tool again and install that component. Also make sure you specify this installed Qt for Slicer (maybe CMake has found some system Qt that did not have Webengine).</p>

---
