# How to smooth model boundaries

**Topic ID**: 8893
**Date**: 2019-10-24
**URL**: https://discourse.slicer.org/t/how-to-smooth-model-boundaries/8893

---

## Post #1 by @NClearning (2019-10-24 20:45 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am trying to remove points on the boundary surface in order to create a perfectly flush boundary for a model. How would I go about smoothing this surface and removing points that make the boundary not flush?</p>
<p>I have attached a photo below of the points I am trying to remove.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f2c2c64aaec980e3a3d72532d87f1f6d7ae52ca.png" alt="Boundary" data-base62-sha1="fRtDHnmRAJXUp6l1h4jP8sr4Rmi" width="410" height="283"></p>

---

## Post #2 by @lassoan (2019-10-24 21:41 UTC)

<p>Having points on a planar face is usually not a cause for concern and it is unusual to try to remove them. What would you like to do with the mesh? 3D print, import to CAD software, …? Why do you think these points cause problems?</p>

---

## Post #3 by @NClearning (2019-10-24 21:48 UTC)

<p>I have a collaborator for future CFD studies and they would like the planar face to be smooth. I have attached an image of the original model they created with (what looks to be) a uniform mesh on the planar boundary surfaces.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/097c7107f9576d46403296cff7c4183d7f9057e6.png" data-download-href="/uploads/short-url/1lUUxDTp0rp4BIfTtQMuZ1Ijs0K.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/097c7107f9576d46403296cff7c4183d7f9057e6_2_690x496.png" alt="Capture" data-base62-sha1="1lUUxDTp0rp4BIfTtQMuZ1Ijs0K" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/097c7107f9576d46403296cff7c4183d7f9057e6_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/097c7107f9576d46403296cff7c4183d7f9057e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/097c7107f9576d46403296cff7c4183d7f9057e6.png 2x" data-dominant-color="9091BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1015×731 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
