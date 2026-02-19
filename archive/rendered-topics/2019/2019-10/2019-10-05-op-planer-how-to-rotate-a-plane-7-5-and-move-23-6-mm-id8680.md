---
topic_id: 8680
title: "Op Planer How To Rotate A Plane 7 5 And Move 23 6 Mm"
date: 2019-10-05
url: https://discourse.slicer.org/t/8680
---

# OP-planer: how to rotate a plane 7,5° and move 23,6 mm

**Topic ID**: 8680
**Date**: 2019-10-05
**URL**: https://discourse.slicer.org/t/op-planer-how-to-rotate-a-plane-7-5-and-move-23-6-mm/8680

---

## Post #1 by @norus (2019-10-05 11:42 UTC)

<p>Hello,<br>
planning an OP at Tibia (vet) we want to cut at fix point with fixed values, but how can I do this. Move and rotate by handles is OK, but if you have a concrete situation?</p>
<p>thank´s to this great team</p>
<p>norus</p>

---

## Post #2 by @Amine (2019-10-06 02:02 UTC)

<p>Hi, did you try transforms module? You can set an exact rotation angle and translation distance (on the main three axis), or use the ruler tool on your model then do the translation for more precision or if you need a custom translation axis you can use reformat module after setting jump slices to centered (in crosshair options) and select your center point using shift, this will provide precise perpendicular slice plane translation (using offset slider) and rotation</p>

---

## Post #3 by @norus (2019-10-06 06:06 UTC)

<p>Hello, thanks for your answer.<br>
transform module I used to move volumes, works fine.<br>
to rotate and translate a new plane I couldn´t use it. We have to position a saw-cut-plane in an exact positon. And in the planner I can rotate and move the plane very well but not with exact parameters.<br>
I will try again with your advice.</p>

---

## Post #4 by @Amine (2019-10-06 07:51 UTC)

<p>What kind of cutting plane are you talking about? Maybe i can give more useful advice if you provide details about your workflow, are you talking about the slice viewer’s plane or a custom 3d model plane you made?</p>
<p>Another interesting approach is to make a polygon (in blender or else) having the height of your translation and the inclination of your rotation to simulate the cutout part frame then use it as a boolean intersection if you are working on models (or in segment editor logical operations)</p>

---

## Post #5 by @norus (2019-10-06 11:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af40436af2a0b653fda1f5a9bc43ce80b267585.png" data-download-href="/uploads/short-url/8pwuL9RxwN9cYvRcjHl0AlVTg4l.png?dl=1" title="OP_Plan_1_0610" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af40436af2a0b653fda1f5a9bc43ce80b267585_2_690x422.png" alt="OP_Plan_1_0610" data-base62-sha1="8pwuL9RxwN9cYvRcjHl0AlVTg4l" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af40436af2a0b653fda1f5a9bc43ce80b267585_2_690x422.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af40436af2a0b653fda1f5a9bc43ce80b267585_2_1035x633.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af40436af2a0b653fda1f5a9bc43ce80b267585_2_1380x844.png 2x" data-dominant-color="B5B9D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OP_Plan_1_0610</span><span class="informations">1628×997 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>this for example is an TTA at a dog. I like the colours for better identifing (mechanical engineer). to cut the Tibia at a given place I tried to use the planner workbench. My problem is to position the cut at this position, there are no fields for translation and rotation parameters. Quantitative its ok, a little bit up and so on…</p>
<p>This is the first problem.</p>
<p>The next is to get a radius plane for TPLO-planning, because the position and the angle are very important. The Tibia head will be cut by a radius saw and rotated some degrees.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db64cdd2fd8beab984139de6508a124c607a3e33.png" data-download-href="/uploads/short-url/viQxky2wLicVyJq3hOqOelEe6FZ.png?dl=1" title="OP_TPLO_radius-plane" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db64cdd2fd8beab984139de6508a124c607a3e33_2_431x499.png" alt="OP_TPLO_radius-plane" data-base62-sha1="viQxky2wLicVyJq3hOqOelEe6FZ" width="431" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db64cdd2fd8beab984139de6508a124c607a3e33_2_431x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db64cdd2fd8beab984139de6508a124c607a3e33.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db64cdd2fd8beab984139de6508a124c607a3e33.png 2x" data-dominant-color="C3CDB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OP_TPLO_radius-plane</span><span class="informations">570×661 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have no idea how to solve this in slicer. I am new, studied all youtube clips I found, but now in the special points its more difficult to find something.<br>
In any case thanks for your advice</p>

---

## Post #6 by @Amine (2019-10-06 20:37 UTC)

<p>Hi, I would do that in blender after exporting the models, you can make any precisely crafted shape to cut your models using booleans, in your case a polygon and a cylinder; you could also make the models in blender then import them back to calibrate and position them in slicer if you’re feeling more comfortable with that, this <a href="https://projectweek.na-mic.org/PW32_2019_London_Canada/Projects/BronchoscopeLocalizationFromDepthMaps/#installing-and-importing-blender-within-slicer" rel="noopener nofollow ugc">link</a> provides a way to import blender in slicer and perform boolean operations with a script. (you could also do that from segment editor if you wish to convert your models to segments)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be04e5720dc20ae5487e6d5d29321309a106725c.png" data-download-href="/uploads/short-url/r6ZcZHg2n2fferSQjNLn097oWL2.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be04e5720dc20ae5487e6d5d29321309a106725c_2_345x228.png" alt="Capture" data-base62-sha1="r6ZcZHg2n2fferSQjNLn097oWL2" width="345" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be04e5720dc20ae5487e6d5d29321309a106725c_2_345x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be04e5720dc20ae5487e6d5d29321309a106725c_2_517x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be04e5720dc20ae5487e6d5d29321309a106725c_2_690x456.png 2x" data-dominant-color="555555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1159×769 573 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In blender you can even go as far as to set the pivot axis for the cut part to be the same as of the cutting cylinder so it allows you to rotate it by your desired angle on the cutting axis.</p>
<p>I have no idea as how to to it natively in slicer (unless developping a module that will generate curved cutting planes, do boolean operations then transform the resulting models in reference to the cutting plane axis)</p>

---

## Post #7 by @norus (2019-10-06 21:34 UTC)

<p>Yes, blender, or maybe in FreeCAD. The solution is outside slicer.<br>
Thank you a lot for your advice</p>

---

## Post #8 by @Amine (2019-10-06 21:59 UTC)

<p>It would be relatively easy to implement as a slicer module, it’s just difficult to cover all specific planning procedures, there might be a more appropriate existent module that i’m not aware of though</p>

---

## Post #9 by @norus (2019-10-07 15:12 UTC)

<p>In FreeCAD it´s easy to cut and rotate the Tibia-head for this purpose. Only  transfer the stl files to CAD is sometimes a littlebit tricky, even to reduce to 10.000 faces max. With meshmixer and/or meshlab no problem but the CAD has sometimes difficulties to create a shell and a body. But we never give up</p>

---

## Post #10 by @lassoan (2019-10-07 16:58 UTC)

<p>Most CAD software (FreeCAD, SolidWorks, AutoCAD Fusion 360, etc.) struggles with surface meshes. In some cases, if you have simple enough geometry, limit the maximum number of cells, etc. then you might be able to import them and there is a chance that you can even apply Boolean operators, but it is a hit and miss.</p>
<p>Slicer uses a different approach, it does all editing in labelmap representation. The advantage is that all operations are always guaranteed to work correctly. The disadvantage is that the higher resolution you need, the more memory and computation power is required (for 2x higher resolution along each axis, you need 8x more memory). If you can afford to buy a computer that is strong enough for your requirements, or you are not time constrained then this is not a huge issue.</p>
<p>You can position clipping planes in Slicer, many ways, both visually and quantitatively.</p>
<p>If you want to clip segmentation then I would recommend to use the slice view plane as clipping plane, because then you can use Scissors effect / Slice cut option to cut only on one side of a slice plane.</p>
<p>You can use Volume Reslice Driver module in SlicerIGT extension to position a slice plane quantitatively, using a transform. So, you can set a transformation by typing translation, rotation angle values in Transforms module and use that transform in Volume Reslice Driver to position the slice plane.</p>

---

## Post #11 by @norus (2019-10-07 19:00 UTC)

<p>Many thanks for this advice, it seems SlicerIGT will manage what we have to do.</p>

---

## Post #12 by @norus (2019-10-07 20:56 UTC)

<p>sorry, sorry, SlicerIGT is installed but I cannot find anything regarding IGT or volume-reslice Driver.  What I am doing wrong. If we get it running I will write a small manual, for sure.</p>

---

## Post #13 by @lassoan (2019-10-07 21:13 UTC)

<p>Which Slicer version do you use? Are there any error messages logged?</p>
<p>You can try to uninstall and reinstall the extension. Wait until “Restart” button becomes enabled in the extension manager and click it to restart.</p>

---

## Post #14 by @Sam_Horvath (2019-10-07 21:45 UTC)

<p>So, the Osteotomy Planner currently does not support manual transformations on the cutting plane.  This is mainly due to the cutting plane node not being a fully implemented fiducial node that responds to transformation other than those made on the interactive 3D widget.  We are intending to implement the plane fiducial in the new markups format and update this module before the next Slicer release.</p>

---

## Post #15 by @norus (2019-10-08 08:05 UTC)

<p>Volume reslice driver arrived, I think it was my fault, because I didn´t see the restart button at the end of the screne, it was hidden.<br>
many thank´s for the information regarding Osteotomy Planner.</p>
<p>The best wishes to you and the developers</p>

---
