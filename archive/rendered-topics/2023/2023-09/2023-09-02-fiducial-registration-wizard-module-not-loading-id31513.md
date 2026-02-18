# Fiducial Registration Wizard Module not loading

**Topic ID**: 31513
**Date**: 2023-09-02
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-module-not-loading/31513

---

## Post #1 by @Jayme_Goodrum (2023-09-02 01:21 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22981212d54691c8f830a55bdb0221fdc5d24f82.jpeg" data-download-href="/uploads/short-url/4W22Ibx8gbymoLg8lfZAEFsBAD8.jpeg?dl=1" title="Screenshot 2023-09-01 at 7.20.09 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22981212d54691c8f830a55bdb0221fdc5d24f82_2_690x432.jpeg" alt="Screenshot 2023-09-01 at 7.20.09 PM" data-base62-sha1="4W22Ibx8gbymoLg8lfZAEFsBAD8" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22981212d54691c8f830a55bdb0221fdc5d24f82_2_690x432.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22981212d54691c8f830a55bdb0221fdc5d24f82_2_1035x648.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22981212d54691c8f830a55bdb0221fdc5d24f82_2_1380x864.jpeg 2x" data-dominant-color="2B2C2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-01 at 7.20.09 PM</span><span class="informations">1546×968 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Jayme_Goodrum (2023-09-02 01:55 UTC)

<p>this is what comes up in the terminal</p>
<p>Last login: Fri Sep 1 19:51:13 on ttys000</p>
<p>/Applications/Slicer.app/Contents/Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-loadable-modules/libqSlicerFiducialRegistrationWizardModule.dylib ; exit;</p>
<p>(base) jaymegoodrum@Jaymes-MacBook-Air ~ % /Applications/Slicer.app/Contents/Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-loadable-modules/libqSlicerFiducialRegistrationWizardModule.dylib ; exit;</p>
<p>zsh: exec format error: /Applications/Sl<br>
exec format error: /Applications/Slicer.app/Contents/Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-loadable-modules/libqSlicerFiducialRegistrationWizardModule.dylib</p>

---

## Post #4 by @lassoan (2023-09-05 14:11 UTC)

<p>Maybe the extension package was corrupted while it was zipped, downloaded, or unzipped? Could you check if the files that you have on your computer are the same as those that you can download from the <a href="https://extensions.slicer.org/catalog/All/31938/macosx">Extensions Catalog</a>?</p>

---

## Post #5 by @Jayme_Goodrum (2023-09-09 19:45 UTC)

<p>I did try this and still had the same error</p>

---

## Post #6 by @lassoan (2023-09-09 19:55 UTC)

<p>There seems to be something wrong with the extension packages on macOS on Slicer-5.4. While we are working on a fix you can use Slicer-5.2.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Are you aware of this issue? Is this something that you can have a look at or we need to wait for <a class="mention" href="/u/jcfr">@jcfr</a>? Do you know when he is going to be available?</p>

---

## Post #7 by @jcfr (2023-09-12 14:06 UTC)

<p>Thanks for pointing this out, I will be looking into this today and follow up.</p>

---

## Post #8 by @jcfr (2023-09-12 22:11 UTC)

<p>The root cause has been identified and fixed <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>
<p>Valid stable extensions are expected to be uploaded in the next 12 hours <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>For more details, see <a href="https://discourse.slicer.org/t/new-extensions-can-not-work-on-slicer-5-4-0-on-macos/31535/4" class="inline-onebox">New extensions can not work on Slicer 5.4.0 on MacOS - #4 by jcfr</a></p>

---
