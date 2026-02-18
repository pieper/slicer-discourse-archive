# Transformation field does not match the volume field

**Topic ID**: 3922
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/transformation-field-does-not-match-the-volume-field/3922

---

## Post #1 by @Scorbinwen (2018-08-28 13:39 UTC)

<p>Operating system: window10<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
I’m now ongoing a project of medical image analysis based on deep learning,but the dataset I can obtain is really limited,so I want augment the dataset by applying non-rigid transformation on the dataset I now have to obtain new volumes with different shape.<br>
I use  registration two volumes to get a transformation grid field,but when I apply this transformation to another volumes,I notice that the volume does not match the field of transformation grid field:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a.png" data-download-href="/uploads/short-url/paYf9HZvQtRVug8epKIS9Y8bgTw.png?dl=1" title="field" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a_2_690x491.png" alt="field" data-base62-sha1="paYf9HZvQtRVug8epKIS9Y8bgTw" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a_2_1035x736.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b073d9dc58befce1c36432613d409dae7933029a.png 2x" data-dominant-color="515359"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">field</span><span class="informations">1052×750 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can I move the volume to the field of transformation field?<br>
I’ve tried to translate the volume, but it seem strange that the volume looks not translated after I reload the saved the translated volume.</p>

---
