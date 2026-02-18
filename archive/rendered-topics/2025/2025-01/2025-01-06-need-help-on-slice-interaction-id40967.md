# Need help on Slice Interaction

**Topic ID**: 40967
**Date**: 2025-01-06
**URL**: https://discourse.slicer.org/t/need-help-on-slice-interaction/40967

---

## Post #1 by @alientex (2025-01-06 13:09 UTC)

<p>Hello everyone,</p>
<p>I was experimenting with different parameters in the Slice Display section, as shown below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fb731d1d0664076f73f077c875caf35c5c2eb2a.png" data-download-href="/uploads/short-url/mMUprIXc0wrRAg3At7C05BNvEZc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fb731d1d0664076f73f077c875caf35c5c2eb2a_2_517x251.png" alt="image" data-base62-sha1="mMUprIXc0wrRAg3At7C05BNvEZc" width="517" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fb731d1d0664076f73f077c875caf35c5c2eb2a_2_517x251.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fb731d1d0664076f73f077c875caf35c5c2eb2a_2_775x376.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fb731d1d0664076f73f077c875caf35c5c2eb2a_2_1034x502.png 2x" data-dominant-color="A3ABAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1341×653 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve been trying to locate the code responsible for creating and displaying these lines (or should I say contour-like visuals) in the views. So far, I’ve traced it to the <code>vtkMRMLDisplayableNode</code>, which has the <code>SetDisplay2DVisibility()</code> function. Using this function, I can toggle the visibility of these lines.</p>
<p>Unfortunately, I’m stuck at this point and haven’t been able to figure out the part of the code where these lines are actually created. It feels like I’m going in circles within the codebase.</p>
<p>Could anyone please guide me or point me in the right direction?</p>

---

## Post #2 by @pieper (2025-01-06 14:06 UTC)

<p>The nodes in the scene contain the state, like the visibility on/off.  The actual rendering takes place in the displayable managers, that respond to changes in the state by managing VTK pipelines.  See, for example: Libs/MRML/DisplayableManager/vtkMRMLModelSliceDisplayableManager.cxx</p>

---
