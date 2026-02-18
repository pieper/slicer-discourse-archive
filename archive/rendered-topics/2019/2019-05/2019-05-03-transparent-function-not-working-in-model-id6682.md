# Transparent function not working in model

**Topic ID**: 6682
**Date**: 2019-05-03
**URL**: https://discourse.slicer.org/t/transparent-function-not-working-in-model/6682

---

## Post #1 by @sarvpriya1985 (2019-05-03 05:18 UTC)

<p>Operating system:windows<br>
Slicer version:4.10.1</p>
<p>Hi,</p>
<p>I convered my segmentations into models. However when i tried to make the bones transparent, it does not work (screenshot). I checked that my depth peeling was on. I have installed stable version about few days back. Any fix for this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5590ca310795688b7dac8895b81bf6c54521005f.jpeg" data-download-href="/uploads/short-url/ccWNkLYas9gPJSupF5SvesJ10FF.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5590ca310795688b7dac8895b81bf6c54521005f_2_690x394.jpeg" alt="Capture" data-base62-sha1="ccWNkLYas9gPJSupF5SvesJ10FF" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5590ca310795688b7dac8895b81bf6c54521005f_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5590ca310795688b7dac8895b81bf6c54521005f_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5590ca310795688b7dac8895b81bf6c54521005f_2_1380x788.jpeg 2x" data-dominant-color="696A6C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1902×1088 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks,<br>
Sarv</p>

---

## Post #2 by @JanWitowski (2019-05-03 16:08 UTC)

<p>Hey Sarv, can you please show the 3D view with segmentation layers turned off and just model parts visible?</p>

---

## Post #3 by @sarvpriya1985 (2019-05-03 16:51 UTC)

<p>Hi,<br>
Thanks for getting back. How to turn segmentation layers off. Is it in Data mode.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #4 by @JanWitowski (2019-05-03 17:27 UTC)

<p>You can make segmentation layers non-visible by clicking the <code>eye</code> icon next to layer name in <code>Segment Editor</code> module:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8dee655ac3bced4d0c51f7e84a319af06047b50.png" alt="image" data-base62-sha1="uWwH2bFPWhzHpMkhjrA89mpIuty" width="621" height="157"></p>
<p>Or just turn the 3D view of segmentation completely by clicking “Show 3D”:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83b0d55ed49fc6ba0a98a69e1c3c8445b2b603a1.png" alt="image" data-base62-sha1="iMZpA4coIUny385wCiONFNXV5VT" width="624" height="140"></p>
<p>Make sure the segmentation 3D views are turned off so you’re looking only at models in your 3D view.</p>

---

## Post #5 by @sarvpriya1985 (2019-05-08 04:50 UTC)

<p>Hi,<br>
Thanks a lot!</p>
<p>I did uncheck the segmentations and the models worked just fine with transparency function working as well. Thanks for the tip!!</p>
<p>Sarv</p>

---
