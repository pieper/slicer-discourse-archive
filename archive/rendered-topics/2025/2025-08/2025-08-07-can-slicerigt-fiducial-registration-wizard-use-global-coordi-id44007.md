# Can SlicerIGT Fiducial Registration Wizard use global coordinates instead of RAS?

**Topic ID**: 44007
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/can-slicerigt-fiducial-registration-wizard-use-global-coordinates-instead-of-ras/44007

---

## Post #1 by @Noam_Borenstein (2025-08-07 18:38 UTC)

<p>Hi everyone!</p>
<p>I am working with a tracked knee model using an NDI camera. I am trying to find the transform between two sets of moving point lists using the fiducial registration wizard. If I move a point in the local/RAS system, the auto-update function works, however, my points move because they are nested under transforms streamed by the NDI camera. I’d like to use the point list’s global coordinate system so that I can auto-update the transform.</p>
<p>Is this possible? Any help is appreciated!</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2025-08-07 18:53 UTC)

<p>The coordinates are actually always recorded relative to the world coordinate system. You can freely choose what coordinate system you use as “World”, but most often it is the Reference or Tracker. After you compute the transform you can change this.</p>
<p>You can configure Plus Server to send transforms between any two coordinate systems and you can compute derived transforms using Combine transforms module, but often you still have to reorganize the transform tree as you switch between workflow steps. In early phases of a project, when you are still figuring out your workflow, you can do this using the GUI of existing modules. Once you know exactly what you want to do, it makes sense to fully automate your workflow in a custom Python scripted module.</p>

---

## Post #3 by @Noam_Borenstein (2025-08-07 19:11 UTC)

<p>So I have the point lists HexPoints and PortalPoints nested under HexToRef and TibiaToRef transforms which are streamed by the NDI camera. Then I set up the fiducial registration wizard to be the transformation between those point lists.  When the HexToRef and TibiaToRef transforms change, it does not trigger the auto-update in the fiducial registration wizard. Any ideas of how to fix this? Here of some pictures of my set up in case that helps.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac600af7899210686097ff745de48c0d8d2c22c2.png" data-download-href="/uploads/short-url/oATTxgOi7IVRN6AFDWbezkCK46e.png?dl=1" title="Screenshot 2025-08-07 150431" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac600af7899210686097ff745de48c0d8d2c22c2_2_648x500.png" alt="Screenshot 2025-08-07 150431" data-base62-sha1="oATTxgOi7IVRN6AFDWbezkCK46e" width="648" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac600af7899210686097ff745de48c0d8d2c22c2_2_648x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac600af7899210686097ff745de48c0d8d2c22c2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac600af7899210686097ff745de48c0d8d2c22c2.png 2x" data-dominant-color="9A98C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-07 150431</span><span class="informations">838×646 65.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11fc8dc6165efe710273d8295bf8d89f8229ab8a.png" data-download-href="/uploads/short-url/2z7d5bBiPgTBpTkr2MXlGGa2gsO.png?dl=1" title="Screenshot 2025-08-07 150547" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11fc8dc6165efe710273d8295bf8d89f8229ab8a.png" alt="Screenshot 2025-08-07 150547" data-base62-sha1="2z7d5bBiPgTBpTkr2MXlGGa2gsO" width="474" height="500" data-dominant-color="E5EBEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-07 150547</span><span class="informations">942×992 34.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ungi (2025-08-08 20:49 UTC)

<p>If you don’t mind writing a few lines of python code, you could add an observer function to any of the transform nodes that you need to trigger the registration update. That function could update the fiducial registration either by calling this module or even using vtkLandmarkTransform directly. This module was not really planned for the use case you are describing. It only updates automatically if the points change.</p>

---
