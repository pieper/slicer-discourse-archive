# MarkupsPlane Registration

**Topic ID**: 19840
**Date**: 2021-09-24
**URL**: https://discourse.slicer.org/t/markupsplane-registration/19840

---

## Post #1 by @Dhruba (2021-09-24 13:20 UTC)

<p>We have annotated all our CTP data with MarkupsPlane before for LVO detection. Now we have to coregister our CT images to an MNI space. Therefore, we have to change our MarkupsPlane. Is there a way to coregister those MarksupsPlane too? (i.e. use those previous Markups and change their coordinates)<br>
Or do we have to annotate all the images again?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe9e0bbb99834bf7c4d2f3832ea1d8b0bcbc1e08.jpeg" data-download-href="/uploads/short-url/AkrT7NBIRYV1HZIHYxpEsMWFvde.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe9e0bbb99834bf7c4d2f3832ea1d8b0bcbc1e08_2_565x500.jpeg" alt="Capture.PNG" data-base62-sha1="AkrT7NBIRYV1HZIHYxpEsMWFvde" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe9e0bbb99834bf7c4d2f3832ea1d8b0bcbc1e08_2_565x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe9e0bbb99834bf7c4d2f3832ea1d8b0bcbc1e08_2_847x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe9e0bbb99834bf7c4d2f3832ea1d8b0bcbc1e08.jpeg 2x" data-dominant-color="504E4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">1068×944 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mikebind (2021-09-24 16:00 UTC)

<p>I’m not sure I understand your question exactly, but if I have the gist of it, you are registering CT images to an MNI space and want the MarkupsPlane annotations you have created to also move to that MNI space.  If that is correct, you should be able to apply the same Transform to the MarkupsPlane as you do for the CT image, and the MarkupsPlane will then appear in the MNI space along with the transformed CT image. All registration methods in Slicer (I believe) give you the option of obtaining the output transform node in addition to or instead of an output registered volume. In this case, you need that output transform node, and can apply it to the MarkupsPlane using the Transforms module.</p>

---
