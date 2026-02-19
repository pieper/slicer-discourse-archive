---
topic_id: 31227
title: "Scrolling Through Phases In Ct Images"
date: 2023-08-18
url: https://discourse.slicer.org/t/31227
---

# Scrolling through phases in ct images

**Topic ID**: 31227
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/scrolling-through-phases-in-ct-images/31227

---

## Post #1 by @admarques (2023-08-18 17:13 UTC)

<p>Operating system: Ubuntu 22.04.1<br>
Slicer version: 5.2.2 r31382<br>
Expected behavior: Sequence visualization<br>
Actual behavior:  The buttons for running the sequence are not active</p>
<p>Hello,</p>
<p>I’m new to using the 3D Slicer and I’m trying to visualize a dataset with 10 phases of CT images.<br>
I can see different slices for the same phase, but I don’t know how to change phases.<br>
It seems that the 10 phases are being recognized as can be seen in the screenshots</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee321190a49e6c73b6c9ba46a54c09281c91accf.png" data-download-href="/uploads/short-url/xZaUo1DT7mW7KwzZxojzJK4f2sT.png?dl=1" title="Screenshot from 2023-08-18 12-11-44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee321190a49e6c73b6c9ba46a54c09281c91accf_2_690x269.png" alt="Screenshot from 2023-08-18 12-11-44" data-base62-sha1="xZaUo1DT7mW7KwzZxojzJK4f2sT" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee321190a49e6c73b6c9ba46a54c09281c91accf_2_690x269.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee321190a49e6c73b6c9ba46a54c09281c91accf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee321190a49e6c73b6c9ba46a54c09281c91accf.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-08-18 12-11-44</span><span class="informations">731×285 31.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342321034dba3be212c201e3dd48561e04489e88.png" data-download-href="/uploads/short-url/7re5HhKbWY3b8VpCyWDrScsgBxS.png?dl=1" title="Screenshot from 2023-08-18 12-09-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342321034dba3be212c201e3dd48561e04489e88_2_690x168.png" alt="Screenshot from 2023-08-18 12-09-54" data-base62-sha1="7re5HhKbWY3b8VpCyWDrScsgBxS" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342321034dba3be212c201e3dd48561e04489e88_2_690x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342321034dba3be212c201e3dd48561e04489e88_2_1035x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342321034dba3be212c201e3dd48561e04489e88_2_1380x336.png 2x" data-dominant-color="F1F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-08-18 12-09-54</span><span class="informations">1802×440 51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you help me to visualize the other phases?<br>
Thank you</p>

---

## Post #2 by @mikebind (2023-08-18 17:24 UTC)

<p>“MulitVolume” is a deprecated format for sequences of image volumes, try loading as a “VolumeSequence” instead.  In your 2nd screenshot, change the checkbox from the top, multivolume option, to the 4th, volume sequence, option before pressing the “Load” button.  Once you do this, the sequence browser buttons should be enabled and work for looking through the phases. Depending on the version of Slicer you are using, there should be a setting in the preferences which allows you to automatically prefer VolumeSequence to MultiVolume loading (so that the VolumeSequence option will be the default checked box in the future).  It’s a little unfortunate that the “Reader” column still says “MultiVolume” for both MultiVolume loading and VolumeSequence loading; to distinguish between them you are looking for the phrase “as a X frames Volume Sequence” in the left hand column.</p>

---

## Post #3 by @admarques (2023-08-18 17:41 UTC)

<p>Thank you!<br>
It solved my problem!</p>

---

## Post #4 by @lassoan (2023-08-18 20:13 UTC)

<p>Note that in the upcoming Slicer-5.4 version, 4D volumes will be loaded as <em>volume sequence</em> by the default.</p>

---
