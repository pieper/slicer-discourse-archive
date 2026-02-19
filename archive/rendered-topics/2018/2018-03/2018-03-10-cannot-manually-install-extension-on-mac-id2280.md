---
topic_id: 2280
title: "Cannot Manually Install Extension On Mac"
date: 2018-03-10
url: https://discourse.slicer.org/t/2280
---

# cannot manually install extension on mac

**Topic ID**: 2280
**Date**: 2018-03-10
**URL**: https://discourse.slicer.org/t/cannot-manually-install-extension-on-mac/2280

---

## Post #1 by @mgastall (2018-03-10 01:49 UTC)

<p>Trying to manually install radionomics extension.</p>
<p>I followed instructions, and under module settings I added from the extension folder:</p>
<p>/Applications/27030-win-amd64-SlicerRadiomics-git0c693c5-2018-03-07/Lib/Slicer-4.9/qt-scripted-modules</p>
<p>/Applications/27030-win-amd64-SlicerRadiomics-git0c693c5-2018-03-07/Lib/Slicer-4.9/cli-modules</p>
<p>There was no option under the extension folder with:<br>
lib/Slicer-X.Y/qt-loadable-modules</p>
<p>Not sure how to install extension, any help I would appreciated.</p>

---

## Post #2 by @lassoan (2018-03-11 02:47 UTC)

<p>Not all extensions have all module types, if one or two of qt-scripted-modules, cli-modules, or qt-loadable-modules folders are missing you can just ignore that.</p>

---

## Post #3 by @fedorov (2018-03-12 13:56 UTC)

<p><a class="mention" href="/u/mgastall">@mgastall</a> there was a problem with the dashboard, but it was fixed, and Radiomics extension should now be available in the nightly Slicer package. The today’s nightly may still not have it, but I tested with the one from yesterday, and I confirmed Radiomics extension can be installed. Use this link today to access download page with the links for yesterday’s binaries: <a href="http://download.slicer.org/?offset=-1" class="inline-onebox">Download 3D Slicer | 3D Slicer</a>.</p>
<p>If you want to configure it to use your locally built Radiomics extension, you will need to configure more than just module paths, since Radiomics is using several Python packages, and requires you to modify <code>PYTHONPATH</code> variable. It is easiest to do <code>make uploadpackage</code> in the <code>inner-build</code> directory for your local extension build, and then configure the variables in the config file as shown below. But if you just need to use the module, I suggest you just get the nightly build and install from Extension Manager.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3edcfcb193d0666e608491893e6dd4371f16b2.png" data-download-href="/uploads/short-url/qzBuAs9Jnobk1rJvk2Caeempncm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba3edcfcb193d0666e608491893e6dd4371f16b2_2_690x337.png" alt="image" data-base62-sha1="qzBuAs9Jnobk1rJvk2Caeempncm" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba3edcfcb193d0666e608491893e6dd4371f16b2_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3edcfcb193d0666e608491893e6dd4371f16b2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3edcfcb193d0666e608491893e6dd4371f16b2.png 2x" data-dominant-color="111010"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">956×468 61.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
