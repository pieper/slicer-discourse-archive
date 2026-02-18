# Ultrasound image always overexposed

**Topic ID**: 14755
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/ultrasound-image-always-overexposed/14755

---

## Post #1 by @LoganWade (2020-11-24 13:41 UTC)

<p>Operating system: Windows 10<br>
Slicer version:Slicer4.10.2<br>
Ultrasound: Telemed EchoBlaster<br>
Expected behaviour: Ultrasound setting carried over from Echowave<br>
Observed Behaviour: Ultrasound image is over exposed (Gain appears to default to 100)</p>
<p>Hi, I am using slicerIGT link to combine motion capture from OptiTrack and Ultrasound from Telemed. I am using the Telemed 32 bit version of PLUS. I am trying to set up my ultrasound, however the settings that i select in Echowave (Telemed software) do not appear to be carried over. Most of the other settings appear to be carried over fine, however i believe the Gain is not. In Slicer the the image is always over exposed except when i set the image up in echowave to have a gain of 100 and adjust other variables to account for this. This leads me to believe that the gain is always set to 100 instead of copying the gain from Echowave. I have tried to use the default config that sets gain to -1 as well as trying to set the gain to 10. However this does not appear to have any impact on the image. Please let me know if i am doing something wrong, Thanks</p>
<p>Ultrasound image and settings in echowave - you can see the gain is set to 10<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4958e2280e65647fbbb58a8aa01430c2bbdc32d0.jpeg" data-download-href="/uploads/short-url/asRhNZKZc9QcRWhCOuOKaOlW4oM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4958e2280e65647fbbb58a8aa01430c2bbdc32d0_2_690x380.jpeg" alt="image" data-base62-sha1="asRhNZKZc9QcRWhCOuOKaOlW4oM" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4958e2280e65647fbbb58a8aa01430c2bbdc32d0_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4958e2280e65647fbbb58a8aa01430c2bbdc32d0_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4958e2280e65647fbbb58a8aa01430c2bbdc32d0_2_1380x760.jpeg 2x" data-dominant-color="323132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1674×923 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ultrasound image in slicer - you can see that the image is very over exposed<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ac8b00892507ba47b48d006ab3c40cdc9c38a38.png" data-download-href="/uploads/short-url/8o1FcxlMhBuu5T42M384BTPWpS0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ac8b00892507ba47b48d006ab3c40cdc9c38a38_2_690x391.png" alt="image" data-base62-sha1="8o1FcxlMhBuu5T42M384BTPWpS0" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ac8b00892507ba47b48d006ab3c40cdc9c38a38_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ac8b00892507ba47b48d006ab3c40cdc9c38a38_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ac8b00892507ba47b48d006ab3c40cdc9c38a38.png 2x" data-dominant-color="888787"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1286×730 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Telemed exerpt from config file. I have tried with the GainPercent removed from the config, GainPercent set to -1 and GainPercent set to 10. None of these changes have made a difference in Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33e19ca5980df9948565911039f982a3b553f6f.png" data-download-href="/uploads/short-url/yHP4GpuEcCPk1wPDMD5Sfi00bQH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33e19ca5980df9948565911039f982a3b553f6f.png" alt="image" data-base62-sha1="yHP4GpuEcCPk1wPDMD5Sfi00bQH" width="593" height="500" data-dominant-color="F9F5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×746 36.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-11-24 18:50 UTC)

<p>What you see is just the automatic image window/level feature (brightness/contrast) in Slicer, which works well for static volumetric images, but ideal for live 2D ultrasound you probably want to set it manually. You can adjust display window/level in Volumes module or using <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level">window/level mouse mode</a>.</p>

---

## Post #3 by @LoganWade (2020-11-25 14:33 UTC)

<p>Thank you for this advice. This solved my issue. This also solved another issue i had with exposure changing throughout a trial. Manually adjusting this within the Volumes module has fixed both issues</p>

---
