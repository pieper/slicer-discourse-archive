# Loaded images are not visible in Slicer running inside Docker container

**Topic ID**: 1408
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/loaded-images-are-not-visible-in-slicer-running-inside-docker-container/1408

---

## Post #1 by @vsivan (2017-11-08 14:22 UTC)

<p>Slicer version: 4.7.0<br>
Expected Behavior: The loaded images are visible on different slices.<br>
Actual Behaviour: The loaded images are not showing on any of the slicer windows. There is no accompanying error message.</p>
<p>The docker container is running Ubuntu 16.04 and the container is vsivan/compiled_slicer and can be found dockerhub.</p>
<p>I have tried loading images through the python interpreter using slicer.util.loadVolume() function as well through the UI. I have verified that these images can be loaded on Slicer running outside the Docker container.</p>
<p>Thanks.</p>
<p>Vignesh</p>

---

## Post #2 by @jcfr (2017-11-08 14:35 UTC)

<p>Out of curiosity, did you also try using the docker images built daily ?</p>
<p>See <a href="https://hub.docker.com/u/slicer/">https://hub.docker.com/u/slicer/</a> and <a href="https://github.com/thewtex/SlicerDocker">https://github.com/thewtex/SlicerDocker</a></p>
<p>I suggest we work and improve these images</p>

---

## Post #3 by @vsivan (2017-11-08 17:24 UTC)

<p>Hi, thanks for the reply. I have not been able to open Slicer from the docker images that you suggested. I get the following error: <code>X Error: BadValue (integer parameter out of range for operation) 2</code>. I can modify the dockerfile I used to build my container to more closely mirror the dockerfiles on Github and I’ll let you know if that works.</p>

---

## Post #4 by @vsivan (2017-11-10 23:50 UTC)

<p>Hi, I am still unable to open Slicer due to the xwindows problem. It would, however, be preferable for me to run Slicer from within my own Docker image. Do you have any ideas as to what could be causing the display issue?</p>
<p>Thanks</p>
<p>EDIT: For more information, the Slicer screen looks like this in the Docker container (RGB windows are all white)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b3d5222487d12c0714c7861c870b93c3163a3b5.png" data-download-href="/uploads/short-url/8s3y6m941Zu7G9WQicQvPFRo18h.png?dl=1" title="Screenshot from 2017-11-13 16-18-04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b3d5222487d12c0714c7861c870b93c3163a3b5_2_690x467.png" alt="Screenshot from 2017-11-13 16-18-04" data-base62-sha1="8s3y6m941Zu7G9WQicQvPFRo18h" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b3d5222487d12c0714c7861c870b93c3163a3b5_2_690x467.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b3d5222487d12c0714c7861c870b93c3163a3b5_2_1035x700.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b3d5222487d12c0714c7861c870b93c3163a3b5.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2017-11-13 16-18-04</span><span class="informations">1098×744 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
