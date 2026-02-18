# MacOS Nightly - extensions manager error

**Topic ID**: 12445
**Date**: 2020-07-08
**URL**: https://discourse.slicer.org/t/macos-nightly-extensions-manager-error/12445

---

## Post #1 by @hherhold (2020-07-08 15:53 UTC)

<p>For the last little while (week or two?) the MacOS nightly version gives me this error when I open the extensions manager. There are also no extensions available. Has anyone else run into this? Does this have to do with the update to the nightly build machine?</p>
<p>Thanks!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7de9403d7e284ce71e90c1a157b440179b8e5e04.png" data-download-href="/uploads/short-url/hXRq8LPkHoNhgnhTEL3IjRPurKk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7de9403d7e284ce71e90c1a157b440179b8e5e04_2_548x500.png" alt="image" data-base62-sha1="hXRq8LPkHoNhgnhTEL3IjRPurKk" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7de9403d7e284ce71e90c1a157b440179b8e5e04_2_548x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7de9403d7e284ce71e90c1a157b440179b8e5e04_2_822x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7de9403d7e284ce71e90c1a157b440179b8e5e04_2_1096x1000.png 2x" data-dominant-color="CACACA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1162×1060 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2020-07-08 16:19 UTC)

<p>Yes it has been reported and something that hasn’t been addressed yet. See <a href="https://discourse.slicer.org/t/problematic-behavior-of-the-extension-manager/10986/11" class="inline-onebox">Problematic behavior of the extension manager</a>.</p>
<p>You can follow its progress at <a href="https://github.com/Slicer/Slicer/issues/5022" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/5022</a></p>

---

## Post #3 by @hherhold (2020-07-08 16:44 UTC)

<p>Oops, sorry - should have checked. Thanks!!</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2020-07-10 12:31 UTC)

<p>In the meantime, is there a way to get updated versions of extensions? There have been changes to extensions that I’d like to use, but I’m forced to just restore extensions from previously installed versions.</p>
<p>I guess I could just grab the git repos and add those in by hand? (Meaning, module paths)</p>
<p>Thanks!</p>

---

## Post #5 by @jamesobutler (2020-07-10 13:26 UTC)

<p>You can download the zip file using your browser and then install manually using install from file option in the extensions manager.</p>
<p><a href="http://slicer.kitware.com/midas3/slicerappstore/?os=macosx&amp;arch=amd64&amp;revision=29212&amp;category=&amp;search=&amp;layout=layout" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore/?os=macosx&amp;arch=amd64&amp;revision=29212&amp;category=&amp;search=&amp;layout=layout</a></p>

---

## Post #6 by @hherhold (2020-07-10 14:52 UTC)

<p>Very cool, thanks!!!</p>

---

## Post #7 by @lassoan (2020-07-10 16:55 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> Do you get that error every time you open the extension manager? What happens if you right-click and choose “Reload”?  Do you get this error only on all the tabs (Manage extensions, Install extensions, Restore extensions) or on just one of them?</p>

---

## Post #8 by @hherhold (2020-07-10 17:09 UTC)

<p>It looks like I get it the first time I open extensions manager, when it goes to the “Install Extensions” tab by default upon opening. I do not get it in the restore extensions or manage extensions tabs. Right-clicking in the “Install Extensions” tab does nothing (no pop-up menu).</p>

---
