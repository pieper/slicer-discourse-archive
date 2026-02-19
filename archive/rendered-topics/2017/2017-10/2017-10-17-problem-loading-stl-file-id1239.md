---
topic_id: 1239
title: "Problem Loading Stl File"
date: 2017-10-17
url: https://discourse.slicer.org/t/1239
---

# Problem loading STL file

**Topic ID**: 1239
**Date**: 2017-10-17
**URL**: https://discourse.slicer.org/t/problem-loading-stl-file/1239

---

## Post #1 by @markz1 (2017-10-17 16:13 UTC)

<p>I’m trying to load an STL file into 3D Slicer, and it doesn’t appear to be loading correctly. It appears like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f45e05322466322997c7b7f168cda8be61955e2a.png" data-download-href="/uploads/short-url/yRLWiGF2bwYl9dcblHMEYExYwmC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f45e05322466322997c7b7f168cda8be61955e2a.png" alt="image" data-base62-sha1="yRLWiGF2bwYl9dcblHMEYExYwmC" width="679" height="500" data-dominant-color="8282B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">685×504 4.94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To get around this, I imported it into other software, saved it as a .ply file, and imported it into 3D Slicer as a .ply, and it looks as it should:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36aadb6a0ad7fe3d0703e441c612d727e8459640.png" data-download-href="/uploads/short-url/7NBQgAlH97aZETywRWxH4IzsBqg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36aadb6a0ad7fe3d0703e441c612d727e8459640.png" alt="image" data-base62-sha1="7NBQgAlH97aZETywRWxH4IzsBqg" width="677" height="500" data-dominant-color="999BCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×504 4.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Further illustrating that there’s an issue, it lists a surface area and volume of a very large number (something like 10^10 mm^2). When I bring in the .ply file, it lists a more reasonable surface area and volume around 1000 mm^2.</p>
<p>I would like to import the STL file directly - does anyone know why I’m getting this import issue?</p>

---

## Post #2 by @lassoan (2017-10-17 16:50 UTC)

<p>Probably some of the triangles in the model are inside out. To see all of them, go to Models module and choose “Visible Sides: All” in 3D Display section (or in older Slicer versions: in Representation section disable “Backface culling”).</p>

---

## Post #3 by @markz1 (2017-10-17 20:49 UTC)

<p>I turned on “Visible Sides: All” and I get the below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38c43bd7888bd09f1de67bdef0b100b6691b6ab7.png" data-download-href="/uploads/short-url/86bamPZ79KI2tsGj1C4OOTlFtvp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38c43bd7888bd09f1de67bdef0b100b6691b6ab7.png" alt="image" data-base62-sha1="86bamPZ79KI2tsGj1C4OOTlFtvp" width="651" height="500" data-dominant-color="9394C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">688×528 5.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This triangular shape is now visible from all angles in the 3D view. If there are “inside out triangles” as you suggested, is there a way to remedy that?</p>
<p>I also attempted to adjust some of the other settings in the “Models” tab. In particular, when checked “Slice Display: Visible” and changed mode to "projection, I saw the following:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/135cb65766239496c5e3b77525210345f602b533.jpeg" data-download-href="/uploads/short-url/2LhHPWYvAyePgTwRmxa4OJvXEaL.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/135cb65766239496c5e3b77525210345f602b533_2_642x500.jpg" alt="image" data-base62-sha1="2LhHPWYvAyePgTwRmxa4OJvXEaL" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/135cb65766239496c5e3b77525210345f602b533_2_642x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/135cb65766239496c5e3b77525210345f602b533_2_963x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/135cb65766239496c5e3b77525210345f602b533_2_1284x1000.jpg 2x" data-dominant-color="464752"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1369×1066 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>That blob in the top left hand corner of the axial and sagittal slices looks like the model I’m looking for, but that large rectangle in each image seems to be some kind of import artifact. Any suggestions?</p>
<p>Just to be clear, the reason why I want to import this STL file directly is because I want it to be in the correct location relative to the DICOM image volume. When I import it via 3rd party software, it appears in the wrong place. If you have suggestions how to preserve relative location of the model from the STL file and the DICOM file, that is the ultimate goal.</p>

---

## Post #4 by @lassoan (2017-10-17 20:52 UTC)

<p>If you see inconsistency between STL files and DICOM files then most probably this post describes the solution:</p><aside class="quote" data-post="2" data-topic="821">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/saved-surface-model-is-not-aligned-with-volume-when-viewed-in-external-software/821/2">Saved surface model is not aligned with volume when viewed in external software</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Most common issue is LPS/RAS coordinate system mismatch. See this post about how this inconsistency can be fixed:
  </blockquote>
</aside>

<p>The STL file that you are trying to import seems to be corrupted. If you upload it somewhere and post the link here then I can have a look.</p>

---

## Post #5 by @markz1 (2017-10-20 18:56 UTC)

<p>Hi Andras,</p>
<p>I tried the transformation you described and it did not solve the issue. The STL volume is still misplaced relative to the image volume.</p>
<p>I sent you the STL file by email.</p>
<p>Thanks,<br>
Mark</p>

---

## Post #6 by @lassoan (2017-10-20 19:20 UTC)

<p>The STL file that you sent contained incorrect coordinate values (in the range of -1e23 to 200). I’ve checked with Paraview as well and it displayed it the same way, as a huge triangle. It seems that there is some problem with your STL writer/converter.</p>

---

## Post #7 by @markz1 (2017-10-20 21:31 UTC)

<p>Hi Andras,</p>
<p>I do believe the coordinate information is there somewhere, because of the following.</p>
<p>I can import the STL files in MeshLab. Along with the tumor model STL file, there is also a “skin” STL file. When I open these two files in MeshLab, they appear in the right location relative to one another. This triangle issue also doesn’t occur in that software.</p>
<p>If I save these STL files as .ply files using MeshLab, I can open them in 3D Slicer, and I see that the relative orientation of these STL meshes (the tumor volume and the skin volume) is preserved. However, when I convert the tumor STL mesh into a segmentation, it appears far from the correct location relative to the DICOM image volume (I cannot convert the skin STL file to a segmentation - the program crashes when I attempt to, I assume because it is a very large file).</p>
<p>The information about where these STL files are in the coordinate space of the DICOM image volume <em>must</em> be somewhere, but I don’t know how to access that information. Do you have any suggestions as to where that information might be? Even if I could find the translation required to align these files somewhere, I could translate the DICOM files manually to the correct location.</p>

---

## Post #8 by @lassoan (2017-10-20 23:13 UTC)

<p>9 out of 11 software fails to to load your STL file:</p>
<ul>
<li>Rejects loading or displays a few huge triangles: Blender, MeshMixer, Slicer, Paraview, 3D Builder, Paint3D, Mixed reality viewer, online viewers (<a href="https://www.viewstl.com/">https://www.viewstl.com/</a>, <a href="http://beta.sharecad.org/viewer">http://beta.sharecad.org/viewer</a>)</li>
<li>Displays some roughly segmented shape: MeshLab, FreeCAD</li>
</ul>
<p>MeshLab (and probably FreeCAD as well) cleans up the model file after it is loaded (removing invalid points, merging concident points), so maybe you just have invalid extra points in your file.</p>
<p>How this STL file was generated? What is your workflow? Can you describe what your project is about, what the end goal is (not just this specific conversion step; which might not be needed at all)?</p>
<p>You can segment DICOM files in Slicer using Segment Editor module.</p>
<p>Importing STL models from external software works well, too. The only problem we encountered in the last couple of years is the LPS/RAS mismatch (it is not an error just a result of different coordinate systems convention) and that can be addressed as described in the linked post above.</p>

---

## Post #9 by @markz1 (2017-10-22 22:30 UTC)

<p>Hi Andras,</p>
<p>These STL files are generated from the Medtronic Stealth neurosurgical planning systems. They are tumor models generated by the neurosurgeon during the surgery. Recreating these tumor models would be a big hassle - it would be much easier to transfer them directly.</p>
<p>My goal is simply to convert this tumor model into DICOM format and transfer it, along with the MR volume, into 3rd party software. Of course it needs to be correctly located relative to the image volume.</p>
<p>Just to be reiterate, I have been able to import the STL file into MeshLab and save it (again as an STL file), and then import it into 3D Slicer, but then the location relative to the MR volume is wrong. I was hoping that if I could import it directly into 3D Slicer, then the location of the STL file would be correct relative to the MR volume. However maybe this isn’t the case (i.e. if it’s imported directly to 3D Slicer it’s still in the wrong place). It’s possible I can just figure out the correct transformation to perform on the image volume or STL file to get them to orient correctly. That would solve my problem as well. I tried the (-1 -1 1 1) transformation you suggested but it didn’t give the desired result.</p>
<p>Thanks for your help.</p>

---

## Post #10 by @lassoan (2017-10-24 01:36 UTC)

<p>There are two probably independent issues:</p>
<ol>
<li>Corrupted STL files</li>
</ol>
<p>If you only use Medtronic software for creating these STL files then probably they are already aware of the issue and may have a solution for you. Which software application and what version did you use on StealthStation to export the models? If you prefer, I can ask our Medtronic contacts, just let us know.</p>
<ol start="2">
<li>Transforming coordinate systems between DICOM and the specific StealthStation application</li>
</ol>
<p>We’ve spent several weeks to figure out the relationship between internal coordinate system of StalthStation SynergyCranial application and the input DICOM files. If you use this specific application then we can help. If you use another then probably you need to ask your Medtronic contact person.</p>

---

## Post #11 by @markz1 (2017-10-24 13:19 UTC)

<p>Hi Andras,</p>
<p>The tech I asked told me the version is “Stealth Cranial 2.2.6”.</p>
<p>-Mark</p>

---
