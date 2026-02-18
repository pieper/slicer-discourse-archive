# NDI Polaris Spectra connection failed

**Topic ID**: 3853
**Date**: 2018-08-20
**URL**: https://discourse.slicer.org/t/ndi-polaris-spectra-connection-failed/3853

---

## Post #1 by @kamrul079 (2018-08-20 20:04 UTC)

<p>I was trying to connect the NDI spectra with slicer 4.8 build version. I had openIGTLinkIF, slicer 4.8 and pre-build Plus. When I connect the NDI device, it can’t connect with slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d7e92ebe24608a1377b885c1884fb995691543f.png" data-download-href="/uploads/short-url/b3xWOl9La2GZ2Lk2PGjwrLUauzZ.png?dl=1" title="polaris" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7e92ebe24608a1377b885c1884fb995691543f_2_690x411.png" alt="polaris" data-base62-sha1="b3xWOl9La2GZ2Lk2PGjwrLUauzZ" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7e92ebe24608a1377b885c1884fb995691543f_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7e92ebe24608a1377b885c1884fb995691543f_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7e92ebe24608a1377b885c1884fb995691543f_2_1380x822.png 2x" data-dominant-color="A8A7A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">polaris</span><span class="informations">1897×1131 603 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2018-08-20 21:44 UTC)

<p>This is a connection error likely due to the Plus configuration file that you are using or some other Plus connection issue. Change the Server Log Level to “Warning” or “Error” and provide the log output in a new git issue over at <a href="https://github.com/PlusToolkit/PlusLib" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib</a> where Plus developers will be able to best help you out. Thanks!</p>

---
