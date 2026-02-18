# Create equidistant curves on a given surface

**Topic ID**: 13212
**Date**: 2020-08-28
**URL**: https://discourse.slicer.org/t/create-equidistant-curves-on-a-given-surface/13212

---

## Post #1 by @agv (2020-08-28 10:47 UTC)

<p>Hello Slicer developers,</p>
<p>I am doing research about HDR brachytherapy for skin (plesiotherapy) and intraoperative applications.</p>
<p>For planning purposes, I would like to generate a series of equidistant curves (for example 1 cm away) on a given surface (for example, a model of the patient’s skin or a tumor) that would simulate the trajectories of the catheters to be placed for treatment.</p>
<p>Is there any module or extension that could do this?</p>
<p>What I’ve seen until now is that I could define two points on the mentioned surface and that “Open Curve Markup” from Slicer 4.11 could generate a path connecting them. The problem here is that I do not know if I can constrain the different curves to be separated a certain distance.</p>
<p>Here is an example with two curves:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92fd12a98f1db0d80bfb94753e47a8ac4ebd6102.jpeg" data-download-href="/uploads/short-url/kYjUQsqOsFjFumNADNvJIUGxACC.jpeg?dl=1" title="SkinCurve" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92fd12a98f1db0d80bfb94753e47a8ac4ebd6102_2_385x375.jpeg" alt="SkinCurve" data-base62-sha1="kYjUQsqOsFjFumNADNvJIUGxACC" width="385" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92fd12a98f1db0d80bfb94753e47a8ac4ebd6102_2_385x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92fd12a98f1db0d80bfb94753e47a8ac4ebd6102_2_577x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92fd12a98f1db0d80bfb94753e47a8ac4ebd6102_2_770x750.jpeg 2x" data-dominant-color="737279"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SkinCurve</span><span class="informations">987×959 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Moreover, I would like to obtain a model/segmentation of these curves, so when using “Open Curve Markup” and “Markups to Model” I have the same problem as in this topic: <a href="https://discourse.slicer.org/t/use-open-curve-markup-as-input-node-in-markups-to-model-extension/13118" class="inline-onebox">Use Open Curve Markup as input node in "Markups To Model" extension</a>.</p>
<p>I would like to underline that this should be done preoperatively, so neither “PathReconstruction” nor “SlicerIGT” extensions would help.</p>
<p>Thank you very much in advance,</p>
<p>Alessandro</p>

---

## Post #2 by @muratmaga (2020-08-28 17:21 UTC)

<p>Others may chime in more.</p>
<p>To me, you have two conflicting requirements, you want to curves to be equidistant and yet you want each to follow the surface topography of the model. This may not be always possible, in fact it is probably never possible on something as complex as the region you highlight above.</p>
<p>If 1cm is a soft constraint (e.g., an average), you can draw your 1st curve using a number of tools available (including following the shortest path on the surface) within the Curve Markup annotation (look under the Curve Settings option). Then you can clone this node, and move it away 1 cm in whichever direction you want. It is almost  guaranteed that the control point of this cloned curve will NOT be on the surface (they may be below the surface). You can then use the Resample option with the constrain to the surface option set, which will make the curve follow the surface topography, but then the control points of two curves are not going to be equidistant anymore.</p>

---

## Post #3 by @lassoan (2020-08-29 15:02 UTC)

<p>We have implemented a module for 3D-printed HDR brachytherapy catheter guide for skin cancer treatment a couple of years ago. Is that something similar to what you would like to accomplish?</p>
<p>                    <a href="https://raw.githubusercontent.com/PerkLab/SlicerSkinMouldGenerator/master/Doc/ExampleOutput.png" target="_blank" rel="nofollow ugc noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/PerkLab/SlicerSkinMouldGenerator/master/Doc/ExampleOutput.png" width="400" height="441">
          </a>

</p>
<p>You can find detailed description in <a href="http://perk.cs.queensu.ca/contents/3d-printed-surface-mould-applicator-high-dose-rate-brachytherapy">this paper</a> (full text available at links near the bottom). Full <a href="https://github.com/PerkLab/SlicerSkinMouldGenerator">source code of the module is available here</a>, but since it was written 5 years ago, you probably need to update it a bit to run on current Slicer version (and it could be simplified significantly, because now Slicer supports curves and has many other features that could be utilized). If you have any questions then we are happy to help.</p>

---

## Post #4 by @agv (2020-08-31 09:43 UTC)

<p>Hello Murat Maga,</p>
<p>thank you for the answer and the suggestion, that was more or less what I figured out initially with the Open Curve Markup tool.</p>
<p>However, I think that said curves can meet both requirements. I don’t need them to have same shape/trajectory or be in equidistant planes (as the ones in Andras’s screenshot), I would understand that in such case they could not be equidistant due to the complex surface.</p>
<p>In my problem, I am trying to find the set of points that, laying on same surface and following a certain direction, are 1 cm away for example. I hope I’ve explained myself better now.</p>

---

## Post #5 by @agv (2020-08-31 09:53 UTC)

<p>Hello Andras Lasso,</p>
<p>thank you very much for all the information regarding that module, I did not know it existed. I will read the paper in detail, I think it could help me in the skin brachytherapy part of the problem.</p>
<p>Unfortunately, I do not have experience with Python or testing code within Slicer.</p>
<p>¿Could you please tell me how can I test the module in Slicer? ¿Do I need an older release?</p>
<p>Thank you again in advance for the attention.</p>

---

## Post #6 by @lassoan (2020-08-31 18:24 UTC)

<p>If you use an older Slicer version where this module works (<a href="https://download.slicer.org/?version=4.6">around Slicer-4.6</a>) then you cannot benefit from all those fixes and improvements that we implemented in the past 5 years Slicer. That would be a huge setback for you.</p>
<p>Can you find a computing student or a medical physicist who is interested in Python programming that would be ready to work on this project with you? I could then help you to get started with Python scripting in Slicer so that you can update the module to work with the latest Slicer version and fine-tune it to meet your requirements.</p>

---

## Post #7 by @agv (2020-09-01 09:44 UTC)

<p>Thank you very much Andras, I’ll check how the module works in such older Slicer version and see if my team and I could work in the code updating for latest version.</p>
<p>Could you please give me some references on how to load a module which is not preinstalled in Slicer like that one?</p>

---

## Post #8 by @lassoan (2023-03-21 02:40 UTC)



---
