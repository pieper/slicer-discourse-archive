# Volume rendering looks squashed

**Topic ID**: 8541
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/volume-rendering-looks-squashed/8541

---

## Post #1 by @Melodicpinpon (2019-09-24 07:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56951c7a689b65d824d13ff576ca6f5fcfd2a409.jpeg" data-download-href="/uploads/short-url/clWwYkiH7TO5nAXRBQZrsOzReVX.jpeg?dl=1" title="379" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56951c7a689b65d824d13ff576ca6f5fcfd2a409_2_690x302.jpeg" alt="379" data-base62-sha1="clWwYkiH7TO5nAXRBQZrsOzReVX" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56951c7a689b65d824d13ff576ca6f5fcfd2a409_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56951c7a689b65d824d13ff576ca6f5fcfd2a409_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56951c7a689b65d824d13ff576ca6f5fcfd2a409.jpeg 2x" data-dominant-color="8A788A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">379</span><span class="informations">1102×483 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi everyone!</p>
<p>The volume rendering of this dog is outcentered and downsized in depth; I guess it is linked with a wrong image-spacing and origin-coordinates within the volume tab; but I could not achieve any change when I moved the values of the origin coordinates or the image-spacing.</p>
<p>Does this problem sound familiar to anyone?</p>

---

## Post #2 by @Juicy (2019-09-24 07:57 UTC)

<p>I have had problems like this before but it sounds like you have already tried what I would have suggested doing.</p>
<p>Is this from a CT scan? If so I would suggest looking at the DICOM header. In the DICOM module pop up window (where you load the dicom file) click the ‘metadata’ button which is next to the ‘load’ button. In the header info you should be able to find a value for the pixel size or spacing as well as the slice thickness and spacing.</p>
<p>Go to the volumes module (check you have the right volume selected if you have multiple volumes) expand the volume information area. Make sure the image spacing values match what the DICOM header says they should be. For axial images the first two values should be the pixel spacing and the third should be the slice spacing. If they arent the same then change the values and you should see the volume update instantly as long as you are looking at the right volume in the slice views.</p>
<p>Slicer should always read the correct values from the dicom header but very occasionally I have had problems which I solved using the above method. If this fails for some reason then you could correct the shape of the volume with transformations and take measurements to confirm it is accurate. You would need another program which is defiantly showing the images correctly to compare it to.</p>

---

## Post #3 by @Melodicpinpon (2019-09-24 10:00 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="2" data-topic="8541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>the pixel size or spacing</p>
</blockquote>
</aside>
<p>Thank you so much!<br>
I finally understood, -thanks to your explainations- that only the section-views were edited in real time. The 3D rendering do not aknowledge these changes but when I press the button ‘convert’ at the bottom of the ‘volume information’ section of the ‘volumes’ module, it sends the modified version to the folder indicated next to ‘file name’; which can now be opened and show the edited volume rendering.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a34baf8fac5aef9e3d6309fa82bc6bcda635c7b.jpeg" data-download-href="/uploads/short-url/1shKr5G4Kg0alzCPpawf47lDu1d.jpeg?dl=1" title="382" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a34baf8fac5aef9e3d6309fa82bc6bcda635c7b_2_690x293.jpeg" alt="382" data-base62-sha1="1shKr5G4Kg0alzCPpawf47lDu1d" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a34baf8fac5aef9e3d6309fa82bc6bcda635c7b_2_690x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a34baf8fac5aef9e3d6309fa82bc6bcda635c7b_2_1035x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a34baf8fac5aef9e3d6309fa82bc6bcda635c7b_2_1380x586.jpeg 2x" data-dominant-color="9288AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">382</span><span class="informations">1890×805 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-09-24 16:03 UTC)

<p>There seems to be a small volume rendering bug: if you manually change volume spacing, it is not reflected immediately in the volume rendering until you re-render (e.g., you rotate the view or trigger re-render with some other operation). I’ve fixed this now in Slicer Preview release.</p>

---
