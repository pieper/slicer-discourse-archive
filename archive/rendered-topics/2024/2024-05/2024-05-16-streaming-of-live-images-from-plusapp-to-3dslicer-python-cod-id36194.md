# Streaming of live images from PlusApp to 3DSlicer/Python code (TELEMED Probe)

**Topic ID**: 36194
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/streaming-of-live-images-from-plusapp-to-3dslicer-python-code-telemed-probe/36194

---

## Post #1 by @Viktor_Sokolov (2024-05-16 05:27 UTC)

<p>I am trying to stream messages from PlusApllication to 3D Slicer. I use TELEMED probe and follow this <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ProcedureStreamingToSlicer.html" rel="noopener nofollow ugc">tutorial</a>.<br>
I use default config file in Plus from <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceTelemed.html" rel="noopener nofollow ugc">here</a>.</p>
<p>Everything seems to work, but VolumeResliceDriver for some reason doesn’t show anything on the red channel screen, what can cause this problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/552ea1784cbad736bd4ea3cb9eb6ace59d104847.jpeg" data-download-href="/uploads/short-url/c9yuqZhomF1GiIete3CEQju0OkD.jpeg?dl=1" title="3d_slicer_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/552ea1784cbad736bd4ea3cb9eb6ace59d104847_2_690x332.jpeg" alt="3d_slicer_1" data-base62-sha1="c9yuqZhomF1GiIete3CEQju0OkD" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/552ea1784cbad736bd4ea3cb9eb6ace59d104847_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/552ea1784cbad736bd4ea3cb9eb6ace59d104847_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/552ea1784cbad736bd4ea3cb9eb6ace59d104847.jpeg 2x" data-dominant-color="847F75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_slicer_1</span><span class="informations">1229×592 78.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>PS: I know that PlusApp streams data via OpenIGTLink. Is it possible to recieve those images in python code without using 3D Slicer at all?</p>

---

## Post #2 by @Sunderlandkyl (2024-05-16 13:50 UTC)

<p>This is using the 64-bit Telemed? You may need to run Plus in either Administrator mode or in Windows 8 compatibility mode to get the images to show up.</p>
<p>It is a known issue with the 64-bit Telemed SDK.</p>

---

## Post #3 by @Viktor_Sokolov (2024-05-17 08:54 UTC)

<p><strong>Kyle Sunderland</strong>, thank you very much, running in Administrator mode helped! Do you know, by any chance, is it possibloe to recieve a stream of live images from Plus in Python code? Preferably, I want to be able to  take snapshots at specific times from the Python code instead of just continuous stream.</p>

---

## Post #4 by @Sunderlandkyl (2024-05-17 15:51 UTC)

<p>Do you mean accessing the images in pure Python, without Slicer, or accessing the images in Slicer using Python?</p>
<p>For pure Python, you can use the pyIGTL package (<a href="https://pypi.org/project/pyigtl/" class="inline-onebox" rel="noopener nofollow ugc">pyigtl · PyPI</a>).</p>

---
