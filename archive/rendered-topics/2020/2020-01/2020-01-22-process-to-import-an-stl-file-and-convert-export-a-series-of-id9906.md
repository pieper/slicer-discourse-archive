---
topic_id: 9906
title: "Process To Import An Stl File And Convert Export A Series Of"
date: 2020-01-22
url: https://discourse.slicer.org/t/9906
---

# Process to Import an STL File and Convert/Export a Series of DICOM Files?

**Topic ID**: 9906
**Date**: 2020-01-22
**URL**: https://discourse.slicer.org/t/process-to-import-an-stl-file-and-convert-export-a-series-of-dicom-files/9906

---

## Post #1 by @aleesdesigner (2020-01-22 16:00 UTC)

<p>Hi,</p>
<p>I’m hoping someone can help with a workflow to import an STL file into Slicer, convert it to a series of DICOM files and export those DICOM files. I’ve checked other forums and can’t find anything that gives a step-by-step of the process. Thank you in advance for the help!</p>
<p>Andrew</p>

---

## Post #2 by @lassoan (2020-01-22 16:01 UTC)

<p>How would you like to export the segmentation: DICOM segmentation object, RT structure set, or fake CT/MRI?</p>

---

## Post #3 by @aleesdesigner (2020-01-22 16:36 UTC)

<p>Hi Andras, I’m interested in exporting a series of DICOM files similar to what is typically imported into Slicer from a CT scan.</p>

---

## Post #4 by @lassoan (2020-01-22 16:41 UTC)

<p>So, would you like to generate a synthetic CT scan from an original CT scan, blanking out regions that are outside a selected segment?</p>

---

## Post #5 by @aleesdesigner (2020-01-22 17:01 UTC)

<p>Not necessarily. I have a 3D model that I’ve saved in STL format that I need to generate DICOM file for. The DICOM files should be the same format as what is generated from a CT or MRI scan.</p>

---

## Post #6 by @lassoan (2020-01-23 00:30 UTC)

<p>STL is a mesh, while CT and MRI are images, so you cannot save in the same format. They are very different kind of data.</p>
<p>You can convert the STL surface mesh to an image for example by blanking out areas inside and/or outside the surface mesh.</p>
<p>Can you tell more about your use case? What software will use the exported STL mesh and how?</p>

---

## Post #7 by @aleesdesigner (2020-01-23 13:18 UTC)

<p>Here’s my process:</p>
<ol>
<li>Import DICOM data from a patient CT scan into Slicer.</li>
<li>Export patient 3D volume to STL file.</li>
<li>Create a 3D component in SolidWorks.</li>
<li>Export 3D component from SolidWorks to STL file.</li>
<li>Combine STL files generated from both Slicer and SolidWorks in Meshmixer and export as a new STL file (3D mesh - not just surface mesh)</li>
<li>Import new STL file into Slicer.</li>
<li>Create 3D segments and export to DICOM files.</li>
<li>Open and review DICOM files in a piece of equipment designed to open and review standard CT/MRI scan DICOM files.</li>
</ol>
<p>I just need help defining the process for steps 6 and 7. Thanks!</p>

---

## Post #8 by @cpinter (2020-01-24 10:03 UTC)

<p>If I understand your needs correctly, given that you will need labelmaps anyway, you can skip the Meshmixer step and do that in Slicer as well. What I can imagine:</p>
<ol start="2">
<li>Do not export it to STL</li>
<li>No change</li>
<li>No change</li>
<li>Import SolidWorks STL into Slicer -&gt; Convert it to segmentation node (if you want to make sure the labelmap geometry matches the CT, you can create empty segmentation in Segmentations module, change master to Closed surface, import STL part, and “advanced create” the labelmap specifying the CT as reference volume) -&gt; Change master to Binary labelmap -&gt; Import “patient 3D volume” that you mention in step 2 (whatever it means…) in this segmentation node -&gt; In Segment Editor, use the Logical operators to unify the part and the “patient volume”</li>
<li>Not needed</li>
<li>In Segmentations module, Export segmentation to labelmap, specifying the CT as reference volume (in Advanced section of Import/Export) -&gt; In Volumes module, change the volume type from labelmap to scalar volume -&gt; In Data module, drag&amp;drop it in the same study as the CT -&gt; Right-click it, Export to DICOM</li>
</ol>

---

## Post #9 by @Juicy (2020-01-24 21:39 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> this is very useful advice.</p>
<p>My only comment would be that <a class="mention" href="/u/aleesdesigner">@aleesdesigner</a> probably needs to design something around the patient’s bone/tissue geometry so would need to export the file at step 2 in order to load it into Solidworks.</p>
<p>If I am interpreting your need correctly, my suggestion would be:</p>
<ol>
<li>Import DICOM data from a patient CT scan into Slicer.</li>
<li>Export patient 3D volume to STL file.</li>
<li>Import patient STL into Solidworks and create a 3D component in SolidWorks WITHOUT moving the location of the patient STL file in 3D space in Solidworks.</li>
<li>Export 3D component from SolidWorks to STL file.</li>
<li>Import the 3D component STL from Solidworks into Slicer. As long as you have not changed the coordinate system in Solidworks then it should appear in exactly the right place on the patient’s bone/tissue in slicer.</li>
<li>Go to Segmentations module (not segment editor). Select the segmentation node which you used to originally segment the patient’s bone/tissue. Go to Import/Export models and labelmaps area and import the model into the segmentation node.</li>
<li>Go to segment editor, click on you original patient bone/tissue segment and then click the logical operators effect. Select Add and add the solidworks model segment to the original segment. (Instead of using meshmixer)</li>
<li>Go back to the segmentations module, click on the newly combined segment and using the same Import/Export area export the segment as a label map.</li>
<li>Go to the volumes module and convert the new label map to a scalar volume.</li>
<li>Go to data module and right click on the new volume and select export to DICOM.</li>
<li>Open and review DICOM files in a piece of equipment designed to open and review standard CT/MRI scan DICOM files.</li>
</ol>
<p>Note that the dicom file is just a completely black and white image. All the bone contrast is lost. You might have to do something a bit more fancy to combine your model volume on top of the original volume if you still want the original bone contrast but I am pretty sure it would be possible.</p>
<p>I tried this out and it worked well for me. Thanks to <a class="mention" href="/u/cpinter">@cpinter</a> for the extra tips about converting back to a scalar volume etc.</p>

---

## Post #10 by @Verena (2025-12-18 21:10 UTC)

<p>Hi there. My use case for Slicer is similar, but with a key difference: I need to import an STL surface mesh of a physical object (either from an optical scanner or a CAD design) and then export it as a stack of DICOM images representing cross-sectional slices of the surface contours.</p>
<p>So far, I have successfully opened my STL file as a “model,” but I am unable to visualize any slice images from it. (Importing the same data as a “segmentation” does not display any object information.) This STL was not generated by SolidWorks.</p>
<p>What specific characteristics does the STL file require for this to work? I am exploring alternative software options, but I would first like to determine if Slicer can accomplish this task—specifically, exporting the 3D object as a stack of 2D DICOM images.</p>

---

## Post #11 by @muratmaga (2025-12-18 22:43 UTC)

<p>After you import model as segmentation, right click on the segmentation and choose export labelmap. Then you can use that labelmap to export to dicom.</p>

---

## Post #12 by @Verena (2025-12-18 23:37 UTC)

<p>Great, this works good. Unfortunately on Blender I safe the object file very tiny. Can I ajust the scene in 3D Slicer? The section images on default only alow me three steps: -1, 0, 1 mm. I would love to refine these steps.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43b3a1579f35bf8273663489069a5bd0e8fb202.png" data-download-href="/uploads/short-url/yQzoxwb9zBzZ0oahLh8X91OlUkO.png?dl=1" title="Screen Shot 2025-12-18 at 17.33.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b3a1579f35bf8273663489069a5bd0e8fb202_2_690x401.png" alt="Screen Shot 2025-12-18 at 17.33.13" data-base62-sha1="yQzoxwb9zBzZ0oahLh8X91OlUkO" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b3a1579f35bf8273663489069a5bd0e8fb202_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b3a1579f35bf8273663489069a5bd0e8fb202_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b3a1579f35bf8273663489069a5bd0e8fb202_2_1380x802.png 2x" data-dominant-color="8C8C90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-18 at 17.33.13</span><span class="informations">2052×1194 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79ed3d0f6f2e3e3f23f1fa4c169a7888fc1b9ca1.png" data-download-href="/uploads/short-url/hoC3pOqrvtB7NJsg6dyX5o7LyCJ.png?dl=1" title="Screen Shot 2025-12-18 at 17.31.01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79ed3d0f6f2e3e3f23f1fa4c169a7888fc1b9ca1_2_690x403.png" alt="Screen Shot 2025-12-18 at 17.31.01" data-base62-sha1="hoC3pOqrvtB7NJsg6dyX5o7LyCJ" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79ed3d0f6f2e3e3f23f1fa4c169a7888fc1b9ca1_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79ed3d0f6f2e3e3f23f1fa4c169a7888fc1b9ca1_2_1035x604.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79ed3d0f6f2e3e3f23f1fa4c169a7888fc1b9ca1_2_1380x806.png 2x" data-dominant-color="F7F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-18 at 17.31.01</span><span class="informations">1482×866 44.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Verena (2025-12-18 23:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77fe001b86d3939207e891496cd47672c4c16aa3.png" data-download-href="/uploads/short-url/h7v0LyXEGo21h3wrvJY8hqU3L6b.png?dl=1" title="Screen Shot 2025-12-18 at 17.45.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77fe001b86d3939207e891496cd47672c4c16aa3_2_690x443.png" alt="Screen Shot 2025-12-18 at 17.45.15" data-base62-sha1="h7v0LyXEGo21h3wrvJY8hqU3L6b" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77fe001b86d3939207e891496cd47672c4c16aa3_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77fe001b86d3939207e891496cd47672c4c16aa3_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77fe001b86d3939207e891496cd47672c4c16aa3_2_1380x886.png 2x" data-dominant-color="7A6B6B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-18 at 17.45.15</span><span class="informations">2728×1752 425 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would appreciate, if zooming into the 3D volume would adjust the three predefined section images… This might not be the case, this I only recognize green dots in the center. How can I zoom into the section images?</p>

---

## Post #14 by @muratmaga (2025-12-19 00:03 UTC)

<aside class="quote no-group" data-username="Verena" data-post="12" data-topic="9906">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/9de053/48.png" class="avatar"> Verena:</div>
<blockquote>
<p>I safe the object file very tiny.</p>
</blockquote>
</aside>
<p>Slicer assumes the unit in your STL are millimeters, since mm is its default unit and STL does not have a way to tell Slicer what those units are. You can use the transforms module to scale your model up/down and then you can do the conversions again.</p>

---

## Post #15 by @Verena (2025-12-19 16:54 UTC)

<p>Thank you very much for your attention. I checked the Tranforms Model and attach some outcome. Still, I am on the wrong way. Could you help me out, please? I still believe Slicer is my option on this task. Best regard, Verena</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49e3e6d2506ec67a1b7adbabb53c2ddfed269d2.png" data-download-href="/uploads/short-url/s3mCrF18uJIurM3lGfrZ8BakElY.png?dl=1" title="Screen Shot 2025-12-19 at 10.51.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49e3e6d2506ec67a1b7adbabb53c2ddfed269d2_2_690x360.png" alt="Screen Shot 2025-12-19 at 10.51.08" data-base62-sha1="s3mCrF18uJIurM3lGfrZ8BakElY" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49e3e6d2506ec67a1b7adbabb53c2ddfed269d2_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49e3e6d2506ec67a1b7adbabb53c2ddfed269d2_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49e3e6d2506ec67a1b7adbabb53c2ddfed269d2_2_1380x720.png 2x" data-dominant-color="999092"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-19 at 10.51.08</span><span class="informations">2188×1142 448 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1939a27362570781d903f1b4196cbd3e28e70f9.jpeg" data-download-href="/uploads/short-url/pkUKp0loAp0f53sDHIRxmUTQpjH.jpeg?dl=1" title="Screen Shot 2025-12-19 at 10.37.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1939a27362570781d903f1b4196cbd3e28e70f9_2_690x397.jpeg" alt="Screen Shot 2025-12-19 at 10.37.20" data-base62-sha1="pkUKp0loAp0f53sDHIRxmUTQpjH" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1939a27362570781d903f1b4196cbd3e28e70f9_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1939a27362570781d903f1b4196cbd3e28e70f9_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1939a27362570781d903f1b4196cbd3e28e70f9_2_1380x794.jpeg 2x" data-dominant-color="979698"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-19 at 10.37.20</span><span class="informations">2060×1188 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e671c4aacc31cf2ed7aff6e1f4770abd99f9061f.png" data-download-href="/uploads/short-url/wSBz3PUPodUufo2oCJzJvOYjmLZ.png?dl=1" title="Screen Shot 2025-12-19 at 10.36.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e671c4aacc31cf2ed7aff6e1f4770abd99f9061f_2_690x398.png" alt="Screen Shot 2025-12-19 at 10.36.13" data-base62-sha1="wSBz3PUPodUufo2oCJzJvOYjmLZ" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e671c4aacc31cf2ed7aff6e1f4770abd99f9061f_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e671c4aacc31cf2ed7aff6e1f4770abd99f9061f_2_1035x597.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e671c4aacc31cf2ed7aff6e1f4770abd99f9061f_2_1380x796.png 2x" data-dominant-color="96959A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-19 at 10.36.13</span><span class="informations">2068×1194 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @muratmaga (2025-12-19 17:30 UTC)

<aside class="quote no-group" data-username="Verena" data-post="15" data-topic="9906">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/9de053/48.png" class="avatar"> Verena:</div>
<blockquote>
<p>I checked the Tranforms Model and attach some outcome.</p>
</blockquote>
</aside>
<p>Actually just use the Scale Model option of the Surface Toolbox module and increase the scale on XYZ and up to the maximum. Then check the resultant model, if it is sufficiently large, then proceed with conversion. If not, apply the scaling again.</p>
<p>Note that you are now arbitrarily scaling things, not sure if this is compatible with your end goal.</p>

---

## Post #17 by @Verena (2025-12-19 18:25 UTC)

<p>Hi Murat, thank you for your attention. Scaling sounds great, yet I am not sure how to “apply“ your idea. I found the corresponding toolbox, as atteched in the screenshots. However, I have no clue hoy to perform the scalinging. Can you help me out, please?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dec7496efb7c1426577d987fa6c3a389ba3709f2.jpeg" data-download-href="/uploads/short-url/vMMY35DqXZtT3rjSfGlPM5WjkYO.jpeg?dl=1" title="Screen Shot 2025-12-19 at 12.20.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dec7496efb7c1426577d987fa6c3a389ba3709f2_2_551x499.jpeg" alt="Screen Shot 2025-12-19 at 12.20.15" data-base62-sha1="vMMY35DqXZtT3rjSfGlPM5WjkYO" width="551" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dec7496efb7c1426577d987fa6c3a389ba3709f2_2_551x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dec7496efb7c1426577d987fa6c3a389ba3709f2_2_826x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dec7496efb7c1426577d987fa6c3a389ba3709f2_2_1102x998.jpeg 2x" data-dominant-color="97888B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-19 at 12.20.15</span><span class="informations">1920×1740 1.14 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d091d17188826f6827664148ac3ec677f8b8d1e.jpeg" data-download-href="/uploads/short-url/aZui2Y0mEdM4vzZsOqDh3Zpl5Ho.jpeg?dl=1" title="Screen Shot 2025-12-19 at 12.14.47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d091d17188826f6827664148ac3ec677f8b8d1e_2_690x474.jpeg" alt="Screen Shot 2025-12-19 at 12.14.47" data-base62-sha1="aZui2Y0mEdM4vzZsOqDh3Zpl5Ho" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d091d17188826f6827664148ac3ec677f8b8d1e_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d091d17188826f6827664148ac3ec677f8b8d1e_2_1035x711.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d091d17188826f6827664148ac3ec677f8b8d1e_2_1380x948.jpeg 2x" data-dominant-color="AEA7AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-19 at 12.14.47</span><span class="informations">1920×1320 717 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @Verena (2025-12-19 18:31 UTC)

<p>My end goal is to collect section images of this 3D object  (hollow cylinder), where the surface projects as concentric circles. I am looking forward to compare these image stack with a CT tomography (DICOM image stack) and possibly use some design imformation on the iterative reconstruction task. The real cylinder is a metal one and causes beam hardening.</p>

---

## Post #19 by @muratmaga (2025-12-19 18:53 UTC)

<aside class="quote no-group" data-username="Verena" data-post="17" data-topic="9906">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/9de053/48.png" class="avatar"> Verena:</div>
<blockquote>
<p>. I found the corresponding toolbox, as atteched in the screenshots. However, I have no clue hoy to perform the scalinging. Can you help me out, please?</p>
</blockquote>
</aside>
<p>to accomplish what you need to do, you need to get familiar with Slicer’s UI and how these types of modules are set to work. I think you should begin with Slicer’s official documentation</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/" target="_blank" rel="noopener nofollow ugc">Welcome to 3D Slicer’s documentation! — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and then specifically see the section on Surface Toolbox.</p>

---

## Post #20 by @Verena (2025-12-19 19:38 UTC)

<p>Yes, now I unterstand my operational error of the UI. Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eddc10eb659a89c3a6299ee9f0c7dd73fd6a29c7.png" data-download-href="/uploads/short-url/xWcEij23UepsSEve8QV1xqaJr2D.png?dl=1" title="Screen Shot 2025-12-19 at 13.32.43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eddc10eb659a89c3a6299ee9f0c7dd73fd6a29c7_2_558x500.png" alt="Screen Shot 2025-12-19 at 13.32.43" data-base62-sha1="xWcEij23UepsSEve8QV1xqaJr2D" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eddc10eb659a89c3a6299ee9f0c7dd73fd6a29c7_2_558x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eddc10eb659a89c3a6299ee9f0c7dd73fd6a29c7_2_837x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/eddc10eb659a89c3a6299ee9f0c7dd73fd6a29c7_2_1116x1000.png 2x" data-dominant-color="A1ABA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2025-12-19 at 13.32.43</span><span class="informations">2212×1980 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
