---
topic_id: 34341
title: "Show Roi Boxes If Loading From Obj File Then All Boxes Appea"
date: 2024-02-15
url: https://discourse.slicer.org/t/34341
---

# Show ROI boxes - if loading from .obj file then all boxes appear in yellow color

**Topic ID**: 34341
**Date**: 2024-02-15
**URL**: https://discourse.slicer.org/t/show-roi-boxes-if-loading-from-obj-file-then-all-boxes-appear-in-yellow-color/34341

---

## Post #1 by @ayadav01 (2024-02-15 12:24 UTC)

<p>Hi, I have saved bounding box coordinates in an .obj file and i am able to load it in slicer and visualize it correctly. I also have a .mtl file that contains the box color information; however, every time i load up the .obj file, it only shows up in yellow color box. I am not sure if i am specifying the color parameter in the .mtl file correctly. This is what i have in the 6b.nii.obj file:</p>
<pre><code class="lang-auto">mtllib 6b.nii.mtl

v 240.0158052444458 92.24226522445679 -170.0
v 240.0158052444458 78.96100568771362 -170.0
v 226.73454570770264 78.96100568771362 -170.0
v 226.73454570770264 92.24226522445679 -170.0
v 240.0158052444458 92.24226522445679 -190.0
v 240.0158052444458 78.96100568771362 -190.0
v 226.73454570770264 78.96100568771362 -190.0
v 226.73454570770264 92.24226522445679 -190.0

usemtl bbox
f 1 2 3 4
f 5 8 7 6
f 1 5 6 2
f 2 6 7 3
f 3 7 8 4
f 5 1 4 8
</code></pre>
<p>This is what i have in the 6b.nii.mtl file</p>
<pre><code class="lang-auto">newmtl bbox
Ka 0 0 0
Kd 0.0 1.0 0.0
Ks 0 0 0
Ns 3
Tr 1
illum 3
</code></pre>
<p>Any help is greatly appreciated. Also, is there a way to specify line-width in the .mtl file ? Please let me know. Thank you!</p>

---

## Post #2 by @lassoan (2024-02-15 12:29 UTC)

<p>Slicer only loads the geometry from OBJ files. Material files are ignored.</p>
<p>It would not be too hard to implement an importer that creates multiple models (one per material), color and opacity set for each based on the material. Would this be sufficient?</p>
<p>If you just want to load a single colored mesh then your can use ply or vtk file format instead.</p>
<p>What is your overall goal? What would you like to do with the mesh in Slicer?</p>

---

## Post #3 by @muratmaga (2024-02-15 16:48 UTC)

<p>In slicermorph, you can import an OBJ file with materials. We haven’t tested extensively but seem to work for the photogrammetry models we have built for a project.</p>
<p><a class="mention" href="/u/ayadav01">@ayadav01</a><br>
Install slicermorph extension, restart slicer, drag and drop your model, and in the dialog box, choose <strong>OBJ Textured Model</strong> as the Description (as opposed to default Model).</p>
<p>See if that helps…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5057ddc58011a831b6a0958169492db1eab12363.png" data-download-href="/uploads/short-url/bsKrUYa0z2pulkPSw7nfKn5XgmT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5057ddc58011a831b6a0958169492db1eab12363_2_690x222.png" alt="image" data-base62-sha1="bsKrUYa0z2pulkPSw7nfKn5XgmT" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5057ddc58011a831b6a0958169492db1eab12363_2_690x222.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5057ddc58011a831b6a0958169492db1eab12363_2_1035x333.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5057ddc58011a831b6a0958169492db1eab12363_2_1380x444.png 2x" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1468×474 32.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ayadav01 (2024-02-15 20:55 UTC)

<p>Thanks Andras. I have a bunch of .obj files that correspond to different type of detections in a CT scans, and i would like to visualize those detected boxes in different colors (i.e., each .obj should display with a unique color). I am not sure how to convert the coordinates in the .obj to a .vtk file and how to specify the color or line width parameter in that file.</p>

---

## Post #5 by @ayadav01 (2024-02-15 20:58 UTC)

<p>I am working on a plugin that is specific to slicer so ideally i want it to be able to work with slicer.</p>

---

## Post #6 by @lassoan (2024-02-15 22:44 UTC)

<p>I would recommend to use “Markups ROI” nodes for showing ROI boxes in Slicer. You can create a <code>myregions.mrk.json</code> and add any number of ROI boxes to it. For example, file content for two ROI boxes:</p>
<pre data-code-wrap="json"><code class="lang-json">{
    "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json#",
    "markups": [
        {
            "name": "My first region",
            "type": "ROI", "roiType": "Box", "coordinateSystem": "LPS", "coordinateUnits": "mm",
            "controlPoints": [{"position": [5.9, -12.3, -10.2], "locked": true}],
            "orientation": [-1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0],
            "size": [39.3, 32.4, 32.4],
            "display": {"selectedColor": [0.4, 1.0, 1.0], "handlesInteractive": false}
        },
        {
            "name": "My second region",
            "type": "ROI", "roiType": "Box", "coordinateSystem": "LPS", "coordinateUnits": "mm",
            "controlPoints": [{"position": [45.9, -102.3, -10.2], "locked": true}],
            "orientation": [-1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0],
            "size": [20.0, 30.5, 44.4],
            "display": {"selectedColor": [1.0, 0.0, 1.0], "handlesInteractive": false}
        }
     ]
}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15196c8564adc3e5f2f647795d3f9d3e3bc6a2ef.jpeg" data-download-href="/uploads/short-url/30EuPPVE2FDPjEuwtCwcVjQj31t.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15196c8564adc3e5f2f647795d3f9d3e3bc6a2ef_2_690x488.jpeg" alt="image" data-base62-sha1="30EuPPVE2FDPjEuwtCwcVjQj31t" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15196c8564adc3e5f2f647795d3f9d3e3bc6a2ef_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15196c8564adc3e5f2f647795d3f9d3e3bc6a2ef_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15196c8564adc3e5f2f647795d3f9d3e3bc6a2ef.jpeg 2x" data-dominant-color="646368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1271×900 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @ayadav01 (2024-02-16 02:00 UTC)

<p>Thanks Andras. This is exactly what i was looking for. Is there a way to change the opacity of the box in the axial view or line-width of the box by any chance ?</p>

---

## Post #8 by @ayadav01 (2024-02-16 02:02 UTC)

<p>Actually nevermind, i see the opacity key in the template from the github link.</p>

---

## Post #9 by @lassoan (2024-02-16 02:12 UTC)

<p>You can see most options if you save a markup ROI to file and have a look at the file.</p>

---
