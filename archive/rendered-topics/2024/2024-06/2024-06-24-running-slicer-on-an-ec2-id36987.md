# Running Slicer on an EC2

**Topic ID**: 36987
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/running-slicer-on-an-ec2/36987

---

## Post #1 by @Samuel_Bentley (2024-06-24 18:01 UTC)

<p>Hi,<br>
I’m trying to install Slicer on a Windows EC2. I’ve tried manually installing the NVIDIA drivers on a GPU instance and have also tried using an EC2 AMI with prebuilt NVIDIA drivers, but neither work. I get a message about insufficient graphics availability. The EC2 instance has 1 GPU with 24 GB memory and 4 CPUs. The driver is a Tesla A-Series A10.</p>
<p>I suspect this is because the drivers don’t support OpenGL 3.2 (they support 4.6).</p>
<p>Has anyone any idea how I can fix, or investigate the error further?</p>
<p>I’ve attached a screenshot of the error and a screenshot of the driver (I’ve since disabled the Microsfot Basic Display Adaptor, but this doesn’t fix it)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d17e155539a648717bc3dc9301c69e0ef96765.png" alt="device" data-base62-sha1="g62jmAQrB1EEitoDUozJaLzgoxT" width="528" height="116"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3633a3ceb4a01095414200ade770136b6315d663.png" data-download-href="/uploads/short-url/7Juq7yIoncDgC96PuZxWDxg2gLN.png?dl=1" title="error_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3633a3ceb4a01095414200ade770136b6315d663_2_690x287.png" alt="error_1" data-base62-sha1="7Juq7yIoncDgC96PuZxWDxg2gLN" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3633a3ceb4a01095414200ade770136b6315d663_2_690x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3633a3ceb4a01095414200ade770136b6315d663.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3633a3ceb4a01095414200ade770136b6315d663.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error_1</span><span class="informations">1032×430 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-24 18:03 UTC)

<p>The issue is just Windows Remote Desktop Protocol (RDP) downgrading OpenGL API version. Updating the RDP server and/or client should fix this, but if it is not feasible then you may consider switching to a remote control software (e.g., VNC).</p>

---
