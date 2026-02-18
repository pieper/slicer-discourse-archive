# Model files are now saved in LPS coordinate system

**Topic ID**: 10446
**Date**: 2020-02-26
**URL**: https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446

---

## Post #1 by @lassoan (2020-02-26 17:23 UTC)

<p>While Slicer uses RAS coordinate system internally, images, transforms, and markups files are stored in LPS coordinate system, because DICOM and all medical image computing software (maybe except a few very old ones) uses LPS coordinate system in files.</p>
<p>However, Slicer has been still using its internal RAS coordinate system in mesh files (STL, VTK, VTP, OBJ, PLY), which <a href="https://issues.slicer.org/view.php?id=4445">caused issues when interfacing with third-party software</a>.</p>
<p>Starting from tomorrow (Slicer-4.11.0-2020-02-26, revision 28794), Slicer Preview Release will <strong>save models in LPS coordinate system, and assume mesh files to be in LPS coordinate system by default.</strong></p>
<p>Slicer started embedding coordinate system name in mesh files a few years ago (see <code>SPACE=RAS</code> in the file header), so all the files that Slicer saved in recent years will load correctly and any scene files created with any version of Slicer will also load the models with correct orientation, too.</p>
<p>Manual setting of coordinate system (in Add data dialog / Options column) is only needed when loading a mesh file without a scene that were created by Slicer-4.6 (2017-09-27) and earlier; and obj files created by Slicer-4.6 and Slicer-4.8 (between 2016-10-11 and 2018-03-26), or files are created by third-party software in RAS coordinate system.</p>
<p>See more details and list of modified files in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28794">this commit</a>.</p>
<p>solid 3D Slicer output. SPACE=LPS<br>
facet normal 0.670457 -0.150029 0.726621<br>
outer loop<br>
vertex 86.7619 22.6655 32.2962<br>
vertex 85.9753 22.2651 32.9394</p>
<p>If you encounter orientation issues when loading a model file, you have the following options:</p>
<ul>
<li>Option A: Specify the coordinate system when you open the model file. In “Add data” dialog, click “Show Options” and then choose “RAS” as coordinate system.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c099fed3176b3b3b8f775c657e84587b9694e3cb.png" data-download-href="/uploads/short-url/rtPBH1CZuM81ggyyBvnJnhLwzWz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c099fed3176b3b3b8f775c657e84587b9694e3cb_2_690x285.png" alt="image" data-base62-sha1="rtPBH1CZuM81ggyyBvnJnhLwzWz" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c099fed3176b3b3b8f775c657e84587b9694e3cb_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c099fed3176b3b3b8f775c657e84587b9694e3cb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c099fed3176b3b3b8f775c657e84587b9694e3cb.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">948×392 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>
<p>Option B: Update the third-party software that generate the mesh to save coordinates in LPS coordinate system instead of RAS coordinate system. Conversion is simple inverting the sign of the first two coordinates.</p>
</li>
<li>
<p>Option C: Write “SPACE=RAS” in the comment/description field in the mesh file (for STL, OBJ, PLY, VTK file; for VTP files, add in the first value of a vtkStringArray field array named “SPACE”) to indicate that the values are stored in RAS coordinate system. This option is useful if coordinates have to be stored in RAS coordinate system (for example, for compatibility with other software).</p>
</li>
</ul>
<details>
<summary>
Examples of file headers that specify what coordinate system is used (click on the arrow on the left to expand)</summary>
<p>Example of an STL file header that stores coordinates in RAS coordinate system:</p>
<pre><code class="lang-plaintext">solid 3D Slicer output. SPACE=RAS
 facet normal 0.670457 -0.150029 0.726621
  outer loop
   vertex 86.7619 22.6655 32.2962
   vertex 85.9753 22.2651 32.9394
...
</code></pre>
<p>Example of an OBJ file header that stores coordinates in RAS coordinate system:</p>
<pre><code class="lang-plaintext"># 3D Slicer output. SPACE=RAS

mtllib Segment_1.mtl

v 83.3949 8.0714 -7.2143
v 83.3949 9.0714 -7.2143
v 83.3949 10.0714 -7.2143
...
</code></pre>
<p>Example of a VTK file header that stores coordinates in RAS coordinate system:</p>
<pre><code class="lang-plaintext"># vtk DataFile Version 4.2
3D Slicer output. SPACE=RAS
BINARY
DATASET POLYDATA
POINTS 7192 float 
...
</code></pre>
<p>Example of a PLY file header that stores coordinates in RAS coordinate system:</p>
<pre><code class="lang-plaintext">ply
format binary_little_endian 1.0
comment VTK generated PLY File
comment SPACE=RAS
obj_info vtkPolyData points and polygons: vtk4.0
element vertex 13327
property float x
property float y
...
</code></pre>
<p>Example of a VTP file header that stores coordinates in RAS coordinate system:</p>
<pre><code class="lang-plaintext">&lt;?xml version="1.0"?&gt;
&lt;VTKFile type="PolyData" version="0.1" byte_order="LittleEndian" header_type="UInt32"&gt;
  &lt;PolyData&gt;
    &lt;FieldData&gt;
      &lt;Array type="String" Name="SPACE" NumberOfTuples="1" format="ascii"&gt;
        82 65 83 0
      &lt;/Array&gt;
    &lt;/FieldData&gt;
    &lt;Piece NumberOfPoints="13327" NumberOfVerts="0" NumberOfLines="0" NumberOfStrips="0" NumberOfPolys="26650"&gt;
      &lt;PointData&gt;
...
</code></pre>
</details>
<p>See C++ code examples of writing coordinate system information when saving a mesh file <a href="https://github.com/Slicer/SlicerGitSVNArchive/blob/c0829f596f0ea661e0c5484056bd1374a3d22958/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L421-L647">here</a>.</p>

---

## Post #2 by @Juicy (2020-02-26 19:29 UTC)

<p>Will Slicer convert to using LPS internally at some point? It seems as though it would make sense given how many other applications use LPS.</p>

---

## Post #3 by @lassoan (2020-02-26 19:36 UTC)

<p>Compatibility with other applications is taken care of by using LPS in files. It would make things simpler to switch to LPS internally, too. It is just a matter of development priorities. There are other things that would make bigger impact for Slicer developers (such as switching to VTK oriented image data) and users (better widgets, measurements, 4D support, etc.).</p>

---

## Post #4 by @siaeleni (2020-04-10 18:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi Andras, the link at the end seems that it is unavailable. Could you please provide that since I am trying to find a way to read/write files in different spaces using python? Thanks a lot.</p>

---

## Post #5 by @lassoan (2020-04-10 18:34 UTC)

<p>I’ve udpated the link. If you want to load an STL/OBJ/PLY/VTK/VTU file that does not have embedded cordinate system information in it and is stored in RAS coordinate system then you can load it like this:</p>
<pre><code class="lang-python">modelNode = slicer.modules.models.logic().AddModel(
  "something.stl", slicer.vtkMRMLStorageNode.CoordinateSystemRAS)
</code></pre>

---

## Post #6 by @brhoom (2020-10-27 21:06 UTC)

<p>Good to know, I was having some problems recently related to this. It would be nice if this option is also available for markups.</p>

---

## Post #7 by @lassoan (2020-10-27 21:26 UTC)

<p>Yes, the same automatic LPS/RAS coordinate system switch is available for markups, too.</p>

---

## Post #8 by @Saima (2021-04-20 05:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="10446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>slicer.vtkMRMLStorageNode.CoordinateSystemRAS</code></p>
</blockquote>
</aside>
<p>if you add fiducials like<br>
markupsNode3 = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsFiducialNode”)<br>
markupsNode3.CreateDefaultDisplayNodes()</p>
<p>how to get the RAS coordinates for fiducials.</p>
<p>Thanks</p>

---

## Post #9 by @Saima (2021-04-22 04:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="10446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>slicer.vtkMRMLStorageNode.CoordinateSystemRAS</code></p>
</blockquote>
</aside>
<p>how to save node in RAS coordinate system.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #10 by @lassoan (2021-04-22 04:49 UTC)

<p>You can specified the desired coordinate system in <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsStorageNode.html#aaf267d2551286c7b1bb0740bc19aa6a1"><code>SetCoordinateSystem</code> method of the storage node</a>.</p>
<p>I would not recommend saving in RAS though, as in medical image computing, data files generally use LPS.</p>

---

## Post #11 by @pya942976269 (2022-05-10 10:13 UTC)

<p>Is there a specific procedure or read/write method to make “SPACE=RAS” in the operation of option C?<br>
Thank you.</p>

---

## Post #12 by @lassoan (2022-05-10 23:23 UTC)

<aside class="quote no-group" data-username="pya942976269" data-post="11" data-topic="10446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pya942976269/48/14267_2.png" class="avatar"> pya942976269:</div>
<blockquote>
<p>Is there a specific procedure or read/write method to make “SPACE=RAS” in the operation of option C?</p>
</blockquote>
</aside>
<p>If you run your Python script in Slicer then you can use the <a href="http://apidocs.slicer.org/master/classvtkMRMLStorageNode.html">vtkMRMLModelStorageNode</a>. It can save models in LPS or RAS and always saves the coordinate system name in the header.</p>
<p>If you run code in a different environment then you can write the coordinate system specification in the file header yourself. If you use VTK then you can copy <a href="https://github.com/Slicer/Slicer/blob/1efef1b35da0f95835c4f56def90629782cd492e/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L479-L732">Slicer’s implementation</a>.</p>

---

## Post #13 by @pya942976269 (2022-05-13 08:24 UTC)

<p>Since I don’t understand this operation well, can you please provide me with a sample program?</p>

---

## Post #14 by @lassoan (2022-05-13 17:04 UTC)

<p>The source code that I linked to shows what Slicer does and you can do exactly the same in your software. If you need more help then you can create a standalone example by copy-pasting the relevant code parts from Slicer’s implementation into a similar VTK example and post the link here so that we can have a look and comment on it.</p>

---

## Post #15 by @joanne40226 (2022-08-20 02:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Hi, i try OptionA with markups however it does not surve the coordinate system choice.<br>
What can i do if i want to read my markups(saved by LPS) into RAS?<br>
Thank you for your time!</p>

---

## Post #16 by @lassoan (2022-08-20 07:27 UTC)

<p>Could you upload your markup file to somewhere (Dropbox, OneDrive, Google drive) and post the link here?</p>

---

## Post #17 by @joanne40226 (2022-08-20 12:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1UHKW3cdwGwKGncme7Dk8VJJQDk1L-3nS/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1UHKW3cdwGwKGncme7Dk8VJJQDk1L-3nS/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1UHKW3cdwGwKGncme7Dk8VJJQDk1L-3nS/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1UHKW3cdwGwKGncme7Dk8VJJQDk1L-3nS/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">000_transed.mrk.json</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
thank you!</p>

---

## Post #18 by @lassoan (2022-08-20 20:51 UTC)

<p>I’ve checked the file and everything looks good. The control point coordinates in the .mrk.json file are defined in LPS coordinate system (first control point: <code>[195.993, 6.125, -90.188]</code>). When Slicer loads the file, it converts the coordinates into RAS coordinate system (first control point: <code>[-195.993, -6.125, -90.188]</code>).</p>
<pre data-code-wrap="json"><code class="lang-json">{
...
    "markups": [ {
            "type": "Fiducial",
            "coordinateSystem": "LPS", ...
            "controlPoints": [
                { ... "position": [195.99323699260385, 6.125348335657372, -90.18842609112076], ... },
                { ... "position": [150.0713619926038, 71.15759015694647, -79.89948566143325], ... }, ...]
...
}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e2a8d188afa51a00bbfd3c98f804159624fd28.png" data-download-href="/uploads/short-url/1prUB27DnhYN4S8DL7qF81XAEQ0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2a8d188afa51a00bbfd3c98f804159624fd28_2_453x500.png" alt="image" data-base62-sha1="1prUB27DnhYN4S8DL7qF81XAEQ0" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2a8d188afa51a00bbfd3c98f804159624fd28_2_453x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2a8d188afa51a00bbfd3c98f804159624fd28_2_679x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2a8d188afa51a00bbfd3c98f804159624fd28_2_906x1000.png 2x" data-dominant-color="3C3F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×1286 86 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you specify the control points in RAS coordinate system then in the file set <code>"coordinateSystem": "RAS"</code>.</p>

---

## Post #19 by @joanne40226 (2022-08-21 02:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I see whats going now! Thank you so much for the information.</p>

---
