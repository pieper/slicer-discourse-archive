# Convert model to landmarks

**Topic ID**: 4139
**Date**: 2018-09-18
**URL**: https://discourse.slicer.org/t/convert-model-to-landmarks/4139

---

## Post #1 by @shahrokh (2018-09-18 12:32 UTC)

<p>Hi<br>
Dear developers and users.</p>
<p>With Steve’s tips and guidance, at now I can extract intersection points between lines (centerlinesMR and centerlinesCT) and the plane with <strong>model type</strong> separately(with <a href="https://discourse.slicer.org/t/intersection-two-models-plane-and-centerlines-ct-mr/4130/3">python script</a>).<br>
In the figure below, intersection points centerlinesCT and plane are shown green and intersection points centerlinesMR and plane are shown red.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f3880ae22d826445d77d490c8b9020a60b5111e.png" data-download-href="/uploads/short-url/biOM93C0cu3KWhyxxSkdXhX6oSa.png?dl=1" title="Screenshot%20from%202018-09-18%2016-52-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f3880ae22d826445d77d490c8b9020a60b5111e_2_690x431.png" alt="Screenshot%20from%202018-09-18%2016-52-27" data-base62-sha1="biOM93C0cu3KWhyxxSkdXhX6oSa" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f3880ae22d826445d77d490c8b9020a60b5111e_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f3880ae22d826445d77d490c8b9020a60b5111e_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f3880ae22d826445d77d490c8b9020a60b5111e_2_1380x862.png 2x" data-dominant-color="565657"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-09-18%2016-52-27</span><span class="informations">1440×900 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At now, I want get BSpline transform between these group points. For doing it, I think that I must use “<em>Scattered Transform</em>” module. Inputs of this module should be of type landmark.</p>
<p>Now my question is: how can I convert these two <strong>models</strong> to two groups landmarks?</p>
<p>Please guide me.<br>
Thanks a lot,<br>
Shahrokh</p>

---

## Post #2 by @pieper (2018-09-18 12:59 UTC)

<p>Nice progress <a class="mention" href="/u/shahrokh">@shahrokh</a> <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=6" title=":clap:" class="emoji" alt=":clap:"></p>
<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ScatteredTransform">scattered transform</a> looks good, althrough I haven’t used it.  For the next step, you can get a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPoints">numpy array from the model vertices</a> and then use the <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLMarkupsFiducialNode.html#details">markups</a> api to create the fiducials.  I don’t see a simple script for creating fiducials, but <a href="https://github.com/pieper/LandmarkRegistration">this code</a> may give you some ideas.</p>

---
