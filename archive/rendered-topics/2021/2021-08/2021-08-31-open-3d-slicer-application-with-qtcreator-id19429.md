# Open 3d slicer application with qtcreator

**Topic ID**: 19429
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/open-3d-slicer-application-with-qtcreator/19429

---

## Post #1 by @xianger-qi (2021-08-31 09:46 UTC)

<p>There are some problems about opening 3d slicer with qt creator version 4.9.0 in linux.<br>
I preform the instructions following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/qtcreatorcpp.html" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging with Qt Creator — 3D Slicer documentation</a>.</p>
<p>problem 1: when i execute the command " ./Slicer --launch /path/to/qtcreator", and the terminal print the error below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d1dd06a689509cc5e483ac939997eef82a313b.png" data-download-href="/uploads/short-url/zva2ET7JJ3Uhw13wTtjpOdqTwin.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d1dd06a689509cc5e483ac939997eef82a313b_2_690x302.png" alt="image" data-base62-sha1="zva2ET7JJ3Uhw13wTtjpOdqTwin" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d1dd06a689509cc5e483ac939997eef82a313b_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d1dd06a689509cc5e483ac939997eef82a313b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d1dd06a689509cc5e483ac939997eef82a313b.png 2x" data-dominant-color="41273A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">785×344 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>problem2: when i  perform below steps</p>
<p>step1: open qt creator → welcome → open project → select  “/Slicer-Master/CMakeLists.txt”<br>
step2: click tab button “Projects” on the left → select build directory → select “/super-build/Slicer-build/” directory like this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7636f009b93e175186a566a1763dd10dcb98b6d4.png" data-download-href="/uploads/short-url/gRM2MwAfYZJL40toIc30qZdcNQE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7636f009b93e175186a566a1763dd10dcb98b6d4_2_690x443.png" alt="image" data-base62-sha1="gRM2MwAfYZJL40toIc30qZdcNQE" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7636f009b93e175186a566a1763dd10dcb98b6d4_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7636f009b93e175186a566a1763dd10dcb98b6d4_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7636f009b93e175186a566a1763dd10dcb98b6d4_2_1380x886.png 2x" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1444×928 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And the sources files display gray and can’t be edited. picture below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c68ec3e44eae7640ef01d102c4e83653328d2c7.png" data-download-href="/uploads/short-url/43kafmVAf8QIk43VHjEA6SMFAbl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c68ec3e44eae7640ef01d102c4e83653328d2c7_2_689x452.png" alt="image" data-base62-sha1="43kafmVAf8QIk43VHjEA6SMFAbl" width="689" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c68ec3e44eae7640ef01d102c4e83653328d2c7_2_689x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c68ec3e44eae7640ef01d102c4e83653328d2c7_2_1033x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c68ec3e44eae7640ef01d102c4e83653328d2c7.png 2x" data-dominant-color="E2E3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1237×811 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-09-07 19:33 UTC)

<aside class="quote no-group" data-username="xianger-qi" data-post="1" data-topic="19429">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xianger-qi/48/11944_2.png" class="avatar"> xianger-qi:</div>
<blockquote>
<p>problem 1: when i execute the command " ./Slicer --launch /path/to/qtcreator", and the terminal print the error below.</p>
</blockquote>
</aside>
<p>Make sure that you are using the same Qt that you used for building Slicer</p>
<aside class="quote no-group" data-username="xianger-qi" data-post="1" data-topic="19429">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xianger-qi/48/11944_2.png" class="avatar"> xianger-qi:</div>
<blockquote>
<p>And the sources files display gray and can’t be edited.</p>
</blockquote>
</aside>
<p>I guess Qt cannot locate the debug symbol files (e.g., due to Qt version mismatch) or cannot start the debugger. Most likely QtCreator uses gdb for debugging and if so then you may need to apply the workaround described in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/vscodecpp.html#prerequisites">this note</a>.</p>

---
