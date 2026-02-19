---
topic_id: 33061
title: "Clarius Live Via Plus Imu Data"
date: 2023-11-27
url: https://discourse.slicer.org/t/33061
---

# Clarius Live via Plus IMU Data

**Topic ID**: 33061
**Date**: 2023-11-27
**URL**: https://discourse.slicer.org/t/clarius-live-via-plus-imu-data/33061

---

## Post #1 by @kst (2023-11-27 15:06 UTC)

<p>Hello, is it possible to transfer the IMU position data of the Clarius C3HD3 to Slicer? The connection via Plus works and live images can also be displayed. How can the position data be used to display the ultrasound image live in the 3D view?<br>
Thank you!</p>

---

## Post #2 by @Sunderlandkyl (2023-11-28 19:23 UTC)

<p>You can see a config file with IMU transforms on this page at " Example configuration file for Clarius B-mode image acquisition with IMU data":<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceClarius.html" class="onebox" target="_blank" rel="noopener nofollow ugc">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceClarius.html</a></p>

---

## Post #3 by @kst (2023-11-30 12:19 UTC)

<p>Thank you! How can I create a transform node that transforms the live image depending on the orientation of the probe (including the information from each sensor)?</p>

---

## Post #4 by @kst (2023-12-01 14:28 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54efbc5a835715505e64d863aad2e717ab265eec.png" data-download-href="/uploads/short-url/c7nJOJUkCRYQ6lIdkGlN0ePGGDO.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54efbc5a835715505e64d863aad2e717ab265eec_2_684x499.png" alt="Screenshot" data-base62-sha1="c7nJOJUkCRYQ6lIdkGlN0ePGGDO" width="684" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54efbc5a835715505e64d863aad2e717ab265eec_2_684x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54efbc5a835715505e64d863aad2e717ab265eec_2_1026x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54efbc5a835715505e64d863aad2e717ab265eec.png 2x" data-dominant-color="6D6D84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1334×975 72.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
