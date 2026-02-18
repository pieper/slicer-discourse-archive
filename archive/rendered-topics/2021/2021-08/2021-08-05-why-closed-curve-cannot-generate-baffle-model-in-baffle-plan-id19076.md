# Why "closed curve" cannot generate Baffle model in Baffle Planner module?

**Topic ID**: 19076
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/why-closed-curve-cannot-generate-baffle-model-in-baffle-planner-module/19076

---

## Post #1 by @StephenLeePeng (2021-08-05 12:05 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: self-build, Slicer 4.13.0<br>
Expected behavior:<br>
First I load a stl file, then I switch to “Markups” module, and draw a closed curve around the stl model. Then I switch to “Baffle Planner module”, and select the drawed closed curve as Input curve, and select “Create new Model as …”, then a surface will generate automatically.</p>
<p>But, If in Markups module, I select draw a closed curve, by selecting curve type to “Shortest distance on surface” and stl as Model Node. The closed curve drawed will attch on the stl model. Then when I switch to Baffle Planner module, and select the latest curve, and select “Create new Model as …” in Baffle modle, but there is no new Baffle model generated, and there exist no error and warnings in the output.</p>
<p>So, why the new baffle model cannot generate in this condition? How to solve this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7959b08e45118cf6269ceba41bb92330117cc0d9.jpeg" data-download-href="/uploads/short-url/hjvVR3Fbd0mNOn4hGcHljy3ObW1.jpeg?dl=1" title="lALPDiQ3PZO1ZPTNA7jNBPc_1271_952" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7959b08e45118cf6269ceba41bb92330117cc0d9_2_667x500.jpeg" alt="lALPDiQ3PZO1ZPTNA7jNBPc_1271_952" data-base62-sha1="hjvVR3Fbd0mNOn4hGcHljy3ObW1" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7959b08e45118cf6269ceba41bb92330117cc0d9_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7959b08e45118cf6269ceba41bb92330117cc0d9_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7959b08e45118cf6269ceba41bb92330117cc0d9.jpeg 2x" data-dominant-color="9895B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lALPDiQ3PZO1ZPTNA7jNBPc_1271_952</span><span class="informations">1271×952 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Above picture is baffle model generated in the first condition.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dda554d2eb6b838c46afe785e3841507708737e.png" data-download-href="/uploads/short-url/1YxYZX4l0SEgf61LbYX1w16PQPI.png?dl=1" title="lALPDgfLSG2tVdDNAlHNBL4_1214_593" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dda554d2eb6b838c46afe785e3841507708737e_2_690x337.png" alt="lALPDgfLSG2tVdDNAlHNBL4_1214_593" data-base62-sha1="1YxYZX4l0SEgf61LbYX1w16PQPI" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dda554d2eb6b838c46afe785e3841507708737e_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dda554d2eb6b838c46afe785e3841507708737e_2_1035x505.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dda554d2eb6b838c46afe785e3841507708737e.png 2x" data-dominant-color="8F8EB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lALPDgfLSG2tVdDNAlHNBL4_1214_593</span><span class="informations">1214×593 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Above picture is generate failed in the second condition when I draw closed curve attach on the stl model.</p>

---

## Post #2 by @StephenLeePeng (2021-08-06 03:37 UTC)

<p>Hi, <a class="mention" href="/u/lassoan">@lassoan</a> , could you help me explain, why the Baffle Model can’t generate automatically when I draw a closed curve attch on the stl model in the second picture.</p>

---

## Post #3 by @lassoan (2021-08-07 12:09 UTC)

<p>Could you share the scene saved as an .mrb file? (upload somewhere and post the link here)</p>

---

## Post #4 by @StephenLeePeng (2021-08-09 06:11 UTC)

<p>Thank you for reply.<br>
I have uploaded the Slicer mrml file, and related stl, Baffle.vtk and so on, wrapped into a zip file, named: SurfaceCutDemo-0809.zip. Please down the zip file via: <a href="https://drive.google.com/file/d/1EiQwZmUIuOgN6wj4A0iB1-nZVUk96SQi/view" class="inline-onebox" rel="noopener nofollow ugc">SurfaceCutDemo-0809.zip - Google Drive</a><br>
Expect to your reply.</p>

---

## Post #5 by @lassoan (2021-08-09 18:44 UTC)

<p>Thank you, the sample data set helped to understand the problem. The issue is that the “Shortest distance on surface” method connects mesh points and therefore the curve is very jagged and the points are very much out of plane, and so it is very hard to generate a triangulated surface for it (that is required for area measurement).</p>
<p>You can get a better-behaved, smooth curve if you keep curve type = spline, and you resample the control points on the surface using “Resample” section. You just need to make sure that the control points are evenly distributed along the vessel.</p>
<p>SlicerVMTK extension can compute diameter of the airways, it provides minimum inscribed sphere radius for all points of the centerline curve.</p>
<p>Recently <a class="mention" href="/u/chir.set">@chir.set</a> added true (free-form) cross-sectional area computation to “Centerline metrics” module in SlicerVMTK, which will be available from tomorrow for latest Slicer Preview Releases (and maybe latest Slicer Stable Release, too). There are a few things to improve, which may make the cross-section more accurate - you can track the status of these improvements here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/35">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/35" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/35" target="_blank" rel="noopener">Improve Centerline metrics module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="18:35:20" data-timezone="UTC">06:35PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is a follow-up to improve features introduced in https://github.com/vmtk/Sl<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">icerExtension-VMTK/pull/32

- [ ] "Segmentation" section should be renamed to Cross-section area measurement
- [ ] "Surface area" should be renamed to "Cross-sectional area"
- [ ] "Derived diameter" should be renamed to "Circular equivalent diameter"
- [ ] "VMTK" diameter should be renamed to "Minimum inscribed sphere diameter" (or MIS diameter for short, and put the full word in tooltip). Difference and ratio compared to circular equivalent diameter should be made more clear. For example, a complete line could look like this: `MIS diameter: 16.80mm (CE diameter +2.4mm, +18%)`
- [ ] Allow using centerline curve as centerline input (as opposed to just model nodes). In Slicer Preview Releases, the MIS radius values are saved in the curve node (can be used for coloring, saved in the markups json file, etc.) and can be accessed as a numpy like this: `a=slicer.util.arrayFromMarkupsControlPointData(curveNode, 'Radius')`
- [ ] Allow using model node as input for cross-section area measurement instead of just segmentation node, if it can be easily made work with surface models (e.g., we don't rely on labelmap representations).
- [ ] Computation of cross-sections does not seem to be very robust: spacing between planes is quite large, non-uniform, and their orientation is changing quite randomly. The degree of these problems may depend on the resolution of the input mesh. For example for the mesh in this scene, things are quite bad: https://1drv.ms/u/s!Arm_AFxB9yqHxfZSIMXrFc2FDfTe8Q?e=XYC420 (see image below)

![image](https://user-images.githubusercontent.com/307929/128756086-7922a866-4cc1-4121-9cee-c2631b05b8c4.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @StephenLeePeng (2021-08-10 11:54 UTC)

<p>Thank you for your reply.<br>
But when I change the curve type as ‘spline’, and use Resample section, and select<br>
“Output node” as ‘Overwrite current node’,<br>
“Constrain points to surface” to the loaded stl model.<br>
And then I switch to Baffle Planner module, and select closed curve as Input curve, but when I select “Create new model” in the Baffle model. But no Baffle surface generate automaticlly.<br>
So I think “the curve is too jagged to cause no Baffle surface generate” is not the main reason, maybe because the curve controlPoint or the connect line is inside the stl model.</p>
<p>attched zip file is mrml file stored. <a href="https://drive.google.com/file/d/1HJMqXp7izbRHkW8U9UnwaDiY5igq2o6w/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">SurfaceCutDemo-0810.zip - Google Drive</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782a382017f3e9874f31da4be8a2198ac2b01fd3.png" data-download-href="/uploads/short-url/h91KxUBo7xiS4VQ2lFbKNcPMWXN.png?dl=1" title="0810-001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782a382017f3e9874f31da4be8a2198ac2b01fd3_2_690x376.png" alt="0810-001" data-base62-sha1="h91KxUBo7xiS4VQ2lFbKNcPMWXN" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782a382017f3e9874f31da4be8a2198ac2b01fd3_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782a382017f3e9874f31da4be8a2198ac2b01fd3_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782a382017f3e9874f31da4be8a2198ac2b01fd3_2_1380x752.png 2x" data-dominant-color="BAB7BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0810-001</span><span class="informations">1760×960 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f96f5b6680db253b26c26abe1d6f66a3ac38b96.png" data-download-href="/uploads/short-url/icI4fV8Cz2AgKRMXUrwbmv2dbn0.png?dl=1" title="0810-002" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f96f5b6680db253b26c26abe1d6f66a3ac38b96_2_690x256.png" alt="0810-002" data-base62-sha1="icI4fV8Cz2AgKRMXUrwbmv2dbn0" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f96f5b6680db253b26c26abe1d6f66a3ac38b96_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f96f5b6680db253b26c26abe1d6f66a3ac38b96_2_1035x384.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f96f5b6680db253b26c26abe1d6f66a3ac38b96_2_1380x512.png 2x" data-dominant-color="B4B2BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0810-002</span><span class="informations">1911×711 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-08-10 16:39 UTC)

<p>We use two different approaches in Slicer for fitting closed surface on an arbitrary closed curve: “ProjectWarp” and “DiskWarp”. They are described <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.h#L218-L250">here</a>. Baffle planner uses DiskWarp, which is more tolerant to out-of-plane points, but only works for quasi-circular contours. Markups closed curves use “ProjectWarp”, which works for arbitrarily concave shapes, but more sensitive to contour points being out of plane.</p>
<p>If you find the surface computed by baffle planner appropriate then you can go to Models module and get the surface are in the Information section:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b3b9c1f8d5593bd7d8a7ad9636a9ecf55f72540.png" data-download-href="/uploads/short-url/jRI54U1XnGaA4X1hchvJuIgHCDe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b3b9c1f8d5593bd7d8a7ad9636a9ecf55f72540_2_650x499.png" alt="image" data-base62-sha1="jRI54U1XnGaA4X1hchvJuIgHCDe" width="650" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b3b9c1f8d5593bd7d8a7ad9636a9ecf55f72540_2_650x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b3b9c1f8d5593bd7d8a7ad9636a9ecf55f72540_2_975x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b3b9c1f8d5593bd7d8a7ad9636a9ecf55f72540_2_1300x998.png 2x" data-dominant-color="C5C3BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1468×1128 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
