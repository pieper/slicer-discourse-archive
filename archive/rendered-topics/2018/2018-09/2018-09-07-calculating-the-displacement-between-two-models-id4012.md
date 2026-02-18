# Calculating the displacement between two models

**Topic ID**: 4012
**Date**: 2018-09-07
**URL**: https://discourse.slicer.org/t/calculating-the-displacement-between-two-models/4012

---

## Post #1 by @aseman (2018-09-07 04:17 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.8.1<br>
Hi 3D slicer experts<br>
I have CT images in 2 states of normal and free breathing. When the patient breathes deeply , the lung volume increases (like the following figure) . (lung volume in deep breathing: 1805 cm3 and the number of its points:2060 ; and  the lung volume in normal breathing: 997cm3 , and the number of its points: 1698) . I want to calculate the lung displacement in deep breathing , relative to normal breathing. and for this purpose, can I  use the model to model distance module?<br>
thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb3848efe540a9f04198ca0deb26a416b04e4d38.png" data-download-href="/uploads/short-url/sZLw0Uqi4Ydtxu1MY9HedkqKcNW.png?dl=1" title="picture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb3848efe540a9f04198ca0deb26a416b04e4d38.png" alt="picture" data-base62-sha1="sZLw0Uqi4Ydtxu1MY9HedkqKcNW" width="690" height="424" data-dominant-color="84A8BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture</span><span class="informations">799×492 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-09-07 11:40 UTC)

<aside class="quote no-group" data-username="aseman" data-post="1" data-topic="4012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>I want to calculate the lung displacement in deep breathing</p>
</blockquote>
</aside>
<p>Do you know what you would like to compute exactly?</p>
<p>Computing surface-to-surface distance assumes corresponding points in the two models are the ones that are closest to each other. Due to large displacements and shape of lungs, this may not be true everywhere.</p>
<p>If you are interested in the displacement field then performing registration may give more accurate results.</p>
<p>You can use Segment Registration extension to compute displacement field from two segmented models (if you have lungs in model nodes then you need to import model nodes into segmentation node).</p>
<p>You may be able to compute displacement field directly from the original CT volumes, using SlicerElastix extension.</p>
<p>If you have a sequence of several volumes (not just 2) then you can get the displacement field over the whole sequence using SequenceRegistration extension.</p>

---

## Post #3 by @aseman (2018-09-09 17:15 UTC)

<p>Hi<br>
Thanks for your response.I used the Segment Registration extension to compute displacement field from two segmented models (Figure 1 in bottom) ; and I also used separately the SlicerElastix extension to compute the displacement field directly from the original CT volumes(Figure 2 in bottom) . but I want to calculate the amount of this displacement .<br>
1- how I can calculate this amount?<br>
2- What exactly does this displacement represent? and is this displacement the amount of displacement between two lung models?<br>
thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f95d7a005850ffd35157fac76dc86b04028aee.png" alt="Figure%201" data-base62-sha1="8CgguqYar6SUw9GVuO3tCyOUz4" width="399" height="290"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ce0525b6620a34deb0a7fba8c00e2cdba85ca9.png" alt="Figure2" data-base62-sha1="ao3LYVFuH6aYncWczmAF7q7Kc65" width="304" height="289"></p>

---

## Post #4 by @lassoan (2018-09-09 22:46 UTC)

<aside class="quote no-group" data-username="aseman" data-post="3" data-topic="4012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>1- how I can calculate this amount?</p>
</blockquote>
</aside>
<p>Displacement field already contains displacement of corresponding points in the fixed and moving image, so you don’t need to compute anything.</p>
<p>You can see numerical value of displacement at current mouse position in Transforms module / Information section:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8e8a15f6402af7c5ac55ecd9f76df6cd196d32d.png" data-download-href="/uploads/short-url/xepbfhFIXD4AWweSssJzx1av2AB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e8a15f6402af7c5ac55ecd9f76df6cd196d32d_2_690x321.png" alt="image" data-base62-sha1="xepbfhFIXD4AWweSssJzx1av2AB" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e8a15f6402af7c5ac55ecd9f76df6cd196d32d_2_690x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e8a15f6402af7c5ac55ecd9f76df6cd196d32d_2_1035x481.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e8a15f6402af7c5ac55ecd9f76df6cd196d32d_2_1380x642.png 2x" data-dominant-color="C8C4C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1447×674 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can get all the displacement vectors (or their vector magnitudes) using Transforms module / Convert section:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/990698bfe9770b9e247b2cb257b6f13327821d08.png" data-download-href="/uploads/short-url/lPJby7Lefa2jqm7QnqUYKlK7xsQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990698bfe9770b9e247b2cb257b6f13327821d08_2_690x404.png" alt="image" data-base62-sha1="lPJby7Lefa2jqm7QnqUYKlK7xsQ" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990698bfe9770b9e247b2cb257b6f13327821d08_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990698bfe9770b9e247b2cb257b6f13327821d08_2_1035x606.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990698bfe9770b9e247b2cb257b6f13327821d08_2_1380x808.png 2x" data-dominant-color="C4C7BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1514×887 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2018-09-09 23:06 UTC)

<aside class="quote no-group" data-username="aseman" data-post="3" data-topic="4012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>What exactly does this displacement represent? and is this displacement the amount of displacement between two lung models?</p>
</blockquote>
</aside>
<p>Yes, it is the 3D displacement (position change) of each corresponding point between fixed and moving image. Note that you can invert the displacement field by a single click in Transforms module.</p>
<p>You can also select specific points (markup fiducials) that you would like to display the displacement of (Transforms mode: Display / Visualization / Advanced / Source points):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40580beb33b2184a94762266822cca123af621ba.png" data-download-href="/uploads/short-url/9bdcddSkljzguzkenssmTeBj1sS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_690x402.png" alt="image" data-base62-sha1="9bdcddSkljzguzkenssmTeBj1sS" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40580beb33b2184a94762266822cca123af621ba_2_1380x804.png 2x" data-dominant-color="C4C3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1455×848 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Finally, you can apply the computed transform to a set of markups fiducial points. You can use this to get original and displaced coordinates for the same anatomical points.</p>

---

## Post #6 by @aseman (2018-09-11 07:06 UTC)

<p>Hi<br>
Thanks for your guidance, Idid the steps mentioned, but I still have a question ! Does the value of this displacement field be achieved for specific area such as lungs?(not the total volume or multiple points?)</p>

---

## Post #7 by @lassoan (2018-09-11 13:24 UTC)

<p>Yes, sure, you can easily compute average displacements in designated areas:</p>
<ul>
<li>export displacement field magnitude to scalar volume using Transforms module</li>
<li>compute average displacement in each segmented region using Segment Statistics module (you need to have the regions defined as segments in a segmentation node)</li>
</ul>

---

## Post #8 by @aseman (2018-09-13 09:35 UTC)

<p>Hi<br>
Thanks for your response. I am sorry !but  How can I export displacement field magnitude to scalar volume using Transforms module?<br>
Thanks a lot</p>

---

## Post #9 by @lassoan (2018-09-13 11:19 UTC)

<p>You can convert any transform to a displacement field image or transform or magnitude image in “Convert” section of Transforms module.</p>

---

## Post #10 by @aseman (2018-09-14 12:51 UTC)

<p>Hi<br>
Thank you very much for your guidance. If I want to show the values between the maximum and minimum values of the obtained displacement field in the  scalar bar , is it possible? and how can I do it?<br>
Thanks a lot</p>

---

## Post #11 by @lassoan (2018-09-14 13:16 UTC)

<p>You can customize scalar bar in Colors module. The controls are not very intuitive, you may need to spend time with tuning the number of colors, labels, range, etc. to get what you need.</p>

---

## Post #12 by @aseman (2018-09-17 05:47 UTC)

<p>Hi<br>
Thank you for your guidance. I was able to calculate the amoun of maximum displacement field for particular segment( left lung) , and I want to find this maximum value is for which displacement  vector?<br>
1- is it possible to get the  displacement field for the maximum displacement field magnitude ?<br>
2- although I was able to achieve the maximum displacement field magnitude for a particular segment (left lung) , but displacement fields still exist in all volume( like  the following figure), and I want to have the displacement vectors only inside the left lung(and  outside the left lung , displacement vectors be zero).how can I do this?<br>
thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c78651315dc1b53a167bc7bd6b22151867b5487.png" data-download-href="/uploads/short-url/aUuepCv5mMv0DkoTbN8wxacRmcL.png?dl=1" title="Pictur%20e" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c78651315dc1b53a167bc7bd6b22151867b5487.png" alt="Pictur%20e" data-base62-sha1="aUuepCv5mMv0DkoTbN8wxacRmcL" width="523" height="500" data-dominant-color="704241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pictur%20e</span><span class="informations">561×536 344 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2018-09-17 18:44 UTC)

<aside class="quote no-group" data-username="aseman" data-post="12" data-topic="4012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>1- is it possible to get the displacement field for the maximum displacement field magnitude ?</p>
</blockquote>
</aside>
<p>You can highlight maximum displacement regions in 2D and 3D using “Contour” visualization method. You<br>
can clone the transform node (using Data module / Subject hierarchy) and show one as “Glyph” and another as “Contour”.</p>
<aside class="quote no-group" data-username="aseman" data-post="12" data-topic="4012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>outside the left lung , displacement vectors be zero).how can I do this?</p>
</blockquote>
</aside>
<p>You need to mask the displacement field image with segmentation. Steps:</p>
<ul>
<li>Install SegmentEditorExtraEffects extension (it contains Mask volume effect that you’ll need to use) and restart Slicer</li>
<li>Export displacement field into a Volume node (“Displacement field”)</li>
<li>Create/import segment that contain the region where you want to keep the displacement values</li>
<li>Use Mask volume effect in Segment editor module to blank out regions of “Displacement field” volume (output volume: “Displacement Field masked”)</li>
<li>Save “Displacement Field masked” volume to nrrd file (this is needed because there is no graphical user interface available for directly converting a volume node into a grid transform node)</li>
<li>Load the just saved “Displacement Field masked” nrrd file as Transform =&gt; this transform has a displacement field that is set to 0 everywhere outside the masking segment</li>
</ul>
<p>For future reference, if you manage to create visualizations that you needed, please post a few screenshots here.</p>

---

## Post #14 by @aseman (2018-09-18 05:49 UTC)

<p>Hi<br>
Excuse me for my question ! but how can I  Export displacement field into a Volume node (“Displacement field”) ?<br>
thanks a lot</p>

---

## Post #15 by @lassoan (2018-09-18 12:19 UTC)

<p>To export a transform to a displacement field, in Transforms module’s Convert section select a reference volume (e.g., your transformed CT), create a new Volume node for output, and click Create.</p>

---

## Post #16 by @aseman (2018-09-19 05:32 UTC)

<p>Hi<br>
I want to load the displacement field masked in MATLAB  to see the components of all displacement field masked in particular region( which was saved with nrrd format). Which format I can save it?( I could not  save it with mat format!)<br>
Thanks a lot</p>

---

## Post #17 by @lassoan (2018-09-19 20:18 UTC)

<p>You can load displacement field from nrrd file to Matlab using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">nrrdread.m</a>.</p>
<p>I would strongly encourage you to consider learning to do all processing using Python (and its many powerful libraries), instead of relying on proprietary tools such as Matlab. Until you are ready to switch, you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension</a> to run Matlab functions directly from Slicer.</p>

---

## Post #18 by @aseman (2018-10-02 04:17 UTC)

<p>Hi<br>
Thank you very much for your advice. Can you guide me how to learn Python? so  that I can use it in the slicer .<br>
thanks a lot</p>

---

## Post #19 by @lassoan (2018-10-02 18:38 UTC)

<p>There are many Python beginner tutorials out there, just spend a couple of days, randomly picking a few and complete them. This should help you get familiar with the syntax.</p>
<p>After that, you can use these training materials that are more specific to biomedical computing applications: <a href="https://discourse.slicer.org/t/a-free-biomedical-image-analysis-and-visualization-2-day-course/2584/10?u=lassoan">A free biomedical image analysis and visualization 2-day course</a></p>

---

## Post #21 by @labixin (2019-01-21 13:24 UTC)

<p>Hi Andras,</p>
<p>Recently I want to combine image registration with finite element method. I intend to initially register two images (pre- and post-surgical breast mri) using intensity-based registration, and then create a cubic bounding box (an ROI extending 2~3cm on each side of the breast tumor, use segment editor module?) in the moving image.<br>
I would like to export the dvf (generated by the intensity-based registration) of voxels right on the boundary of ROI and define them as boundary displacement constraints of fem.<br>
I wonder how to get the dvf of specific contour (like boundary of the cubic box) of voxels. Could you give me some advice? Thank you very much.</p>
<p>Best regards,<br>
Crayon</p>

---

## Post #22 by @lassoan (2019-01-24 21:32 UTC)

<p>Displacement field is defined for a 3D region of interest, but of course you can just take samples from it anywhere you need it.</p>
<pre><code class="lang-auto">transform = vtk.vtkGeneralTransform()
getNode('MyTransformNodeName').GetTransformToWorld(transform)

originalPoint = [2.4, -1.1, 5.3]
transformedPoint = transform.TransformPoint(originalPoint)
print transformedPoint
</code></pre>

---
