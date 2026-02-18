# DICOM module not working when used as startup module

**Topic ID**: 20474
**Date**: 2021-11-03
**URL**: https://discourse.slicer.org/t/dicom-module-not-working-when-used-as-startup-module/20474

---

## Post #1 by @jamieawren (2021-11-03 14:37 UTC)

<p>Hi everyone,</p>
<p>Overnight, the DICOM module has stopped working, see attached screenshot. I am seeing this error, too</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py”, line 678, in exit<br>
self.browserWidget.close()<br>
AttributeError: ‘NoneType’ object has no attribute ‘close’</p>
<p>I have updated to the most recent stable build and the behavior is persisting. Interestingly, the behavior is not replicated when Slicer is opened for other users on the same computer.</p>
<p>Any help would be greatly appreciated!</p>
<p>Jamie <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/328ccb3d60178ee6c4d5f86933378365c70526ca.png" data-download-href="/uploads/short-url/7dbwqH0DZakH07orqUPNB0SzJgK.png?dl=1" title="Screen Shot 2021-11-03 at 10.34.12 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328ccb3d60178ee6c4d5f86933378365c70526ca_2_690x443.png" alt="Screen Shot 2021-11-03 at 10.34.12 AM" data-base62-sha1="7dbwqH0DZakH07orqUPNB0SzJgK" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328ccb3d60178ee6c4d5f86933378365c70526ca_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/328ccb3d60178ee6c4d5f86933378365c70526ca_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/328ccb3d60178ee6c4d5f86933378365c70526ca.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-11-03 at 10.34.12 AM</span><span class="informations">1367×879 84.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2021-11-03 14:40 UTC)

<p>İs it possible that you modified your DICOM db location? The location shown in screenshot doesn’t seem right. And i think that setting carries over from versions.</p>

---

## Post #3 by @pieper (2021-11-03 14:41 UTC)

<p>Probably something got broken in the settings.  These documents should help.  If it happens again let us know if you figure out what led to the issue so we can reproduce.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=settings#settings-file-location" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=settings#settings-file-location</a></p>

---

## Post #4 by @jamieawren (2021-11-03 14:44 UTC)

<p>I reset the Application Settings (DICOM module was set as the default module on open) and it works like a charm now! Thank you so much for your speedy solution!</p>
<p>Jamie</p>

---

## Post #5 by @jamieawren (2021-11-03 14:45 UTC)

<p>It’s very possible, I discovered that the behavior resolved when I stopped using DICOM as the default module on open.</p>

---

## Post #6 by @lassoan (2021-11-04 04:55 UTC)

<p>Setting the DICOM module as startup module can be very useful and I see that currently an error is thrown if you do this. I’ll fix this error tomorrow.</p>

---

## Post #7 by @jamieawren (2021-11-04 13:54 UTC)

<p>Great! Thank you very much, it would be very helpful to have the DICOM module as default!</p>

---

## Post #8 by @lassoan (2021-11-04 16:45 UTC)

<p>The <a href="https://github.com/Slicer/Slicer/commit/ceb56b25b6b45ab59917c0195738919486869365">fix</a> will be available in the Slicer Preview Release from tomorrow.</p>

---
