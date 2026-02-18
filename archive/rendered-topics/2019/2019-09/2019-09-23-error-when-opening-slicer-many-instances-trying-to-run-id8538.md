# Error when opening slicer - many instances trying to run

**Topic ID**: 8538
**Date**: 2019-09-23
**URL**: https://discourse.slicer.org/t/error-when-opening-slicer-many-instances-trying-to-run/8538

---

## Post #1 by @Georgian_Ciobotaru (2019-09-23 19:40 UTC)

<p>Hello everyone,</p>
<p>I’m using 4.10.2 version, but in the last 2 days it became unusable: it tries to open, there are many instances appearing to open, but it goes like this for as long as my patience goes. Did you happen to bump into this problem? What else could i do except for installing 4.11?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b68f8f7f37f3ed0c4111f4d580fa01a47fb908b7.png" data-download-href="/uploads/short-url/q30tyeSFaPoQfctyiOnkPW6MGjl.png?dl=1" title="26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68f8f7f37f3ed0c4111f4d580fa01a47fb908b7_2_690x98.png" alt="26" data-base62-sha1="q30tyeSFaPoQfctyiOnkPW6MGjl" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68f8f7f37f3ed0c4111f4d580fa01a47fb908b7_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68f8f7f37f3ed0c4111f4d580fa01a47fb908b7_2_1035x147.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68f8f7f37f3ed0c4111f4d580fa01a47fb908b7_2_1380x196.png 2x" data-dominant-color="677C54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">26</span><span class="informations">1548×220 392 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the error log is here</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1SpCg1N7vWrFFFXt9fj1S47xGkOxdPU5a/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1SpCg1N7vWrFFFXt9fj1S47xGkOxdPU5a/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1SpCg1N7vWrFFFXt9fj1S47xGkOxdPU5a/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1SpCg1N7vWrFFFXt9fj1S47xGkOxdPU5a/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">3dslicer instances error.docx</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Many thanks!</p>

---

## Post #2 by @lassoan (2019-09-23 21:00 UTC)

<p>This usually happens when you have a batch file that starts Slicer in one of the directories specified in “addititional module paths”. The solution is to remove that file.</p>
<p>The reason is that Slicer interprets all executables (exe, py, bat, sh,… files) in module paths as modules. All module files are executed at Slicer startup as part of the module discovery process. If one of these executables starts Slicer then you get an infinite loop.</p>

---

## Post #3 by @aalarcon96 (2019-10-28 20:53 UTC)

<p>If we need to build a new module but this keeps happening, is there a way to fix it without removing that module from the “additional module paths”?</p>

---

## Post #4 by @lassoan (2019-10-28 21:10 UTC)

<p>You can keep the module in the path but move non-module executables to a different folder (e.g., into a subfolder). Or, you can even leave your non-module executables there but make sure that if Slicer launches them (you can determine that from the command-line arguments) then you don’t launch another Slicer instance.</p>

---

## Post #5 by @aalarcon96 (2019-10-29 14:58 UTC)

<p>I tried moving the non-executables in a subfolder but when I try to run slicer it gives me the error that the module has failed to be instantiated. These are the files in my module-build folder (after removing them from the subfolder) :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2304c6aba5b808df59f249387ea9bd4ac7e986fb.png" data-download-href="/uploads/short-url/4ZMWxcccMttZde4kS9BC3qvUYhZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2304c6aba5b808df59f249387ea9bd4ac7e986fb.png" alt="image" data-base62-sha1="4ZMWxcccMttZde4kS9BC3qvUYhZ" width="340" height="500" data-dominant-color="ECE8EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">347×509 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The module only appears when I keep all the files together, but many instances are running. I am not sure what to try next. Any other suggestions?</p>

---

## Post #6 by @aalarcon96 (2019-10-29 15:15 UTC)

<p>All fixed! I had the wrong path to the “additional modules path”… <img src="https://emoji.discourse-cdn.com/twitter/woman_facepalming.png?v=9" title=":woman_facepalming:" class="emoji" alt=":woman_facepalming:"></p>

---

## Post #7 by @nineyoyoyo (2024-08-14 04:21 UTC)

<p>I’ve faced this problem and figured out that because I used subprocess lib to install python package automatically it seems work on mac but not for window then I just knew slicer lib also has easy way to install package by just import slicer and slicer.util.pip_install()</p>

---
