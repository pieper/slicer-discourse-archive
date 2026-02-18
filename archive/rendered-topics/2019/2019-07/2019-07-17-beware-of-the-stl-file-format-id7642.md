# Beware of the STL file format

**Topic ID**: 7642
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/beware-of-the-stl-file-format/7642

---

## Post #1 by @Chris_Rorden (2019-07-17 19:25 UTC)

<p>Many topics on this forum mention the STL format. While it is great that Slicer supports so many formats, I would advocate that Slicer discourage users from exporting to STL (e.g. from the “Save Scene and Unsaved Data” dialog change the file format pull-down to list “STL (.stl) deprecated” versus the current “STL (.stl)”. The only reason to export to STL is if it is the only format supported by the software or 3D printer you are using. Fortunately, modern 3D printing companies like Shapeways now support better formats such as OBJ.</p>
<p>The fundamental issue with STL is that it does not reuse vertices. This means that the resulting meshes will either look faceted (e.g. Slicer) or will be extremely slow to load (if the software attempts to unify vertices, e.g. Surfice). In addition, this feature makes this format exceptionally inefficient yielding large file sizes (about 3 times the file size of a simple uncompressed binary format). Not only are the faceted images ugly, they are slower and more resource intensive to render with <a href="http://hacksoflife.blogspot.com/2010/01/to-strip-or-not-to-strip.html" rel="noopener nofollow ugc">modern methods</a>.</p>
<p>The issue is illustrated in the image below. This is a mesh created with Slicer’s Editor function and then the same mesh is saved as both STL and OBJ format. The two meshes are then reloaded in Slicer. Note that the OBJ file has nice per-pixel shading, while the STL file has jagged per-triangle shading.</p>
<p>Given that the format is so popular with Slicer users, the other option is to support vertex-unification when STL files are loaded. This will make the loaded STL images look nicer (though loading times will increase).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c31b53fccf19e399f051a7b3980c318719f2b7d.jpeg" data-download-href="/uploads/short-url/mhKZ1E2gAs9hcP2Ia14RwzTxTl3.jpeg?dl=1" title="stl_vs_obj" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c31b53fccf19e399f051a7b3980c318719f2b7d_2_690x461.jpeg" alt="stl_vs_obj" data-base62-sha1="mhKZ1E2gAs9hcP2Ia14RwzTxTl3" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c31b53fccf19e399f051a7b3980c318719f2b7d_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c31b53fccf19e399f051a7b3980c318719f2b7d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c31b53fccf19e399f051a7b3980c318719f2b7d.jpeg 2x" data-dominant-color="5A5A69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">stl_vs_obj</span><span class="informations">1030×689 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-07-17 23:11 UTC)

<p>Hi <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> - I totally agree that STL is a <em>terrible</em> format for storing geometry and should be avoided whenever possible.  As you point out, many 3D printer companies don’t seem to realize this and use it for some kind of legacy reasons (even though it must make their lives harder too).  Unfortunately the user community seems to have gotten into the habit of saying STL whenever they mean polygon surface mesh and so the cycle continues.</p>
<p>Regarding your specific proposal, maybe instead of adding the word ‘deprecated’ how about adding ‘discouraged’ or some other term.  I think we should reserve ‘deprecated’ for things we’ll be removing in an upcoming release, but, alas, I don’t think we will ever be able to remove STL.</p>

---

## Post #3 by @lassoan (2019-07-18 00:08 UTC)

<p>Very interesting discussion. I don’t like STL file format either and very surprised that is is still so widely used. However, I find most consumer/gaming mesh formats about equally bad for medical image computing. Yes, STL is the most basic format, and yes, OBJ is better in a couple of things (it supports polygon cells, surface normals, textures), but it has some disadvantages, too, even compared to STL.</p>
<p>Some of the problems with OBJ:</p>
<ul>
<li>it is not possible to specify unit (mm/inches/m) or coordinate system (LPS/RAS/…) in a standard way (same as STL)</li>
<li>no way to store arbitrary metadata (same as STL)</li>
<li>it is ASCII only, so files are larger and/or lose precision and much slower to parse than binary STL (worse than STL)</li>
<li>we cannot claim to be fully compatible with OBJ, as it has some features that would be very difficult to fully support, such as NURBS curves and surfaces, or multi-texture (worse than STL)</li>
</ul>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="1" data-topic="7642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>resulting meshes will either look faceted (e.g. Slicer) or will be extremely slow to load</p>
</blockquote>
</aside>
<p>VTK clean polydata filter can merge coincident points and compute surface normals in negligible time, so computation time should not be an issue.</p>
<p>We’ve been planning to add an optional normal computation step into the model display pipeline. This could be enabled by default for STL files or for any other surface mesh files that did not happen to have the normals available.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="1" data-topic="7642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>In addition, this feature makes this format exceptionally inefficient yielding large file sizes</p>
</blockquote>
</aside>
<p>Standard OBJ format is text only, so file sizes are larger than binary STL.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="1" data-topic="7642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>change the file format pull-down to list “STL (.stl) deprecated”</p>
</blockquote>
</aside>
<p>Adding “deprecated” there sounds too harsh to me (and as <a class="mention" href="/u/pieper">@pieper</a> pointed out not even accurate). But even if we could find a better word: I would not single out STL as the bad guy. Is PLY any better? Would you <em>always</em> recommend OBJ over STL? We should probably just try to educate users on the forum, documentation, etc. where there is a room for explaining our rationale for preferring one file format over another.</p>

---

## Post #4 by @Lorensen (2019-07-18 03:43 UTC)

<p>In the near future, I’ll modify the vtk obj so that there is no loss in precision. I used the class vtkNumberToString in the vtkXMLWriter.</p>

---

## Post #5 by @lassoan (2019-07-18 04:34 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="4" data-topic="7642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I’ll modify the vtk obj so that there is no loss in precision</p>
</blockquote>
</aside>
<p>This will be great, thank you, one issue will be taken care of then!</p>
<p>(Still, writing/reading numbers as text will be much slower and file size will be larger compared to using a binary file format, and other OBJ file issues still remain.)</p>

---

## Post #6 by @Lorensen (2019-07-18 06:05 UTC)

<p>I just submitted an <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests?assignee_id=&amp;author_id=&amp;label_name=&amp;milestone_id=&amp;scope=all&amp;sort=updated_desc&amp;state=opened" rel="nofollow noopener">MR</a> to improve the saved floating point values.</p>

---

## Post #7 by @Chris_Rorden (2019-07-18 17:35 UTC)

<p>PLY format reuses vertices, so it does not suffer the issues of STL. I for one <strong>do</strong> single out STL as the worst popular mesh format as it is the only one that does not reuse vertices.</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> notes, a major disadvantage of OBJ is that it is only ASCII. Both PLY and STL have ASCII and binary variants. With ASCII you need to trade off file size and precision, and file loading is always extremely slow. In my software OBJ (with moderate precision) is about <a href="https://www.nitrc.org/plugins/mwiki/index.php/surfice:MainPage#Supported_Formats" rel="nofollow noopener">13 times slower and 7 times larger</a> than a simple gzipped binary format (MZ3).</p>
<p>The <a href="https://github.com/neurolabusc/surf-ice/tree/master/mz3" rel="nofollow noopener">MZ3</a> format can be extended, is very fast and relatively compact. I might be biased here as I developed it, but I would be happy to extend this. The current version was extended to support features for PALM (Anderson Winkler) and SPM (Guillaume Flandin) and I provide Matlab, <a href="https://neurolabusc.github.io/" rel="nofollow noopener">JavasScript</a> and Python/Blender code. The strength of this format is that is virtually identical to the raw data one sends to the GPU, which makes it fast. However, just like modern GPUs it only represents triangles. The advantage of triangles is that as long as three points are not co-linear they define a single plane, while this is not true of all quads (e.g. all 3-legged stools are stable, but many 4 legged chairs rock between legs). While modern GPUs do not use quads as a base type, quads can be useful for a file format to store if one is interested in subdivision.</p>
<p>The <a href="https://www.nitrc.org/projects/gifti/" rel="nofollow noopener">GIfTI format</a> does allow meta data. It is XML-based and so it is human readable. It uses base-64 storage for binary data which adds a bit of a speed and file size hit, but this is pretty modest. It seems like a reasonable interchange format for brain imaging.</p>
<p>The Draco format is very clever, creating extremely compact files. However, it is very complicated and the fact that it re-indexes vertices would probably be a problem for a lot of brain imaging applications.</p>

---

## Post #8 by @pieper (2019-07-19 00:15 UTC)

<p>And of course let’s not forget <a href="https://www.khronos.org/gltf/" rel="nofollow noopener">glTF</a>, which <a href="https://discourse.slicer.org/t/transferring-models-using-gltf-2-0/7064">is already being integrated with Slicer</a>.  It’s more graphics-oriented than medical, but the features and community support, not to mention compactness and extensibility are impressive.  No reason we couldn’t propose an extension to embed some things like coordinate system reference (probably LPS by default) and other useful things like anatomy codes.</p>

---

## Post #10 by @lassoan (2019-07-19 02:34 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="7" data-topic="7642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>I for one <strong>do</strong> single out STL as the worst popular mesh format as it is the only one that does not reuse vertices.</p>
</blockquote>
</aside>
<p>I’m just curious, why it is a problem that vertices are not reused? I’ve just tried and VTK loads a mesh that contains 1.5 million points in 2 seconds from .vtk file, and in about 3 seconds from .stl file (including coincident point merging). So, performance should not be a huge issue.</p>
<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="7642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>No reason we couldn’t propose an extension to embed some things like coordinate system reference (probably LPS by default) and other useful things like anatomy codes.</p>
</blockquote>
</aside>
<p>I agree, I always feel that there are already too many file formats and we should rather spend our time with improving existing ones.</p>

---

## Post #11 by @Chris_Rorden (2019-07-19 20:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - the 2 second load for a vtk file reflects a poorly optimized VTK loader. Slicer saves <a href="https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf" rel="nofollow noopener">VTK files</a> as triangles in binary VTK format, e.g. the header will report “POLYGONS n sz” where sz = n * 4. This represents a special case: when sz = n * 4 you can read the entire array from disk and ignore the numPointsN as it will always be 3 (if sz &gt; n * 4 you must read the numPointsN for each NGon and reconstruct it).</p>
<pre><code>POLYGONS n size
numPoints0, i0, j0, k0, ...
numPoints1, i1, j1, k1, ...
...
numPointsn-1, in-1, jn-1, kn-1, ...
</code></pre>
<p>Here are times for reading meshes with my software (vtk, obj and stl created with Slicer):<br>
mz3 (raw) 14ms<br>
mz3 (gzip) 134ms<br>
vtk (ignore numPoints) 67ms<br>
obj (ascii) 2710ms<br>
vtk (naive) 2857ms<br>
stl (binary, unify) 4717ms</p>
<p>I think it would be terrific if Slicer would automatically unify STL vertices. However, I would still discourage users from saving in STL unless absolutely required, as many tools do not apply this step and therefore the resulting meshes look poor.</p>

---

## Post #12 by @lassoan (2019-07-19 21:05 UTC)

<p>VTK’s STL reader merges coincident points by default. Slicer uses this default setting.</p>

---

## Post #13 by @Chris_Rorden (2019-07-19 21:26 UTC)

<p>Is this a new feature? The STL and OBJ images from the initial comment were both generated by Slicer and loaded by Slicer (version 4.10.2 on MacOS). The STL and OBJ files look identical to each other when I load them with Surfice (which unifies vertices, e.g. the STL looks faceted in Slicer but not Surfice).</p>

---

## Post #14 by @Chris_Rorden (2019-07-19 22:18 UTC)

<p>One other thought, is it possible that Slicer/VTK estimate the vertex normals before unifying the vertices? This would explain the faceted look. It is important to calculate surface normals after unifying the vertices.</p>

---

## Post #15 by @lassoan (2019-07-19 22:44 UTC)

<p>The faceted look of models loaded from STL files is due to that we do not compute the normals automatically. If normals are not stored in the file then model surface will be displayed with flat shading. I noticed this year’s ago but did not want to simply add a few lines to compute normals with some default settings if they are not available in the input file because of potential rendering artifacts (especially when cells are large and highly angled), the extra computation time, and maybe a module that loads the data may want to compute normals in a specific way (splitting at feature edges, etc). Comouting missing surface normals in the display pipeline would not have any of these limitations, but we have not get around to implement it.</p>
<p>Users can always compute surface normals using Surface toolbox module if they need it.</p>

---

## Post #16 by @Chris_Rorden (2019-07-19 23:17 UTC)

<p>That is understandable. Sounds like a good reason to discourage users from choosing the STL format if they want to render the data in Slicer. As shown above, the per-vertex surface normals of the OBJ files that are created are more accurate than the per-face normals required by the STL format. I appreciate that the vertex unification of slicer will remove my concerns regarding the usage of GPU resources and performance.</p>

---

## Post #17 by @Juicy (2019-07-20 02:05 UTC)

<p>I use the STL file a lot for downstream CAD modelling as well as 3d printing. It is a very well recognised file format across many programs.</p>
<p>I appreciate the education regarding the inefficiencies associated with the format as I was not really aware (I do notice the huge file sizes though)</p>
<p>Although I do think this info would be best shared on forums and documentation as mentioned previously. I think it would look very unprofessional to have little comments next to the file formats in the drop down menu. I have never seen other software with this.</p>
<p>I know when I select STL it is because there is no other option for getting slicer models into other CAD software and 3d printers.</p>

---

## Post #18 by @fangq (2019-09-02 01:56 UTC)

<p>in case someone is still interested in considering a new mesh format, I have been working on (text/binary) JSON based mesh data format - JMesh - as part of the work related to my 3D mesh generator Iso2Mesh (<a href="http://iso2mesh.sf.net" rel="nofollow noopener">http://iso2mesh.sf.net</a>). This summer, I wrote a few JSON/JData based file specifications, including an early draft for JMesh.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/fangq/jmesh" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/226913?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/fangq/jmesh" target="_blank" rel="nofollow noopener">fangq/jmesh</a></h3>

<p>JMesh - A portable and versatile JSON data format for storage of unstructured mesh and shape data - fangq/jmesh</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>More related discussion can be found in my mailing list post in the below link</p>
<p><a href="https://groups.google.com/forum/#!topic/iso2mesh-users/EIG4V7Gzpl0" class="onebox" target="_blank" rel="nofollow noopener">https://groups.google.com/forum/#!topic/iso2mesh-users/EIG4V7Gzpl0</a></p>
<p>Essentially, a text-based JMesh file is basically a plain JSON file that can be parsed by nearly all JSON parsers; to save space, it can be converted to a binary-version (and convert back) using the UBJSON specification (<a href="http://ubjson.org" rel="nofollow noopener">http://ubjson.org</a>). Both formats support strongly-typed data and internal compression.</p>
<p>Currently, working parsers/writers for MATLAB already exist, and the support for other languages (without advanced JData features) can be readily added by linking with any JSON/UBJSON parsers available.</p>
<p>Happy to chat more if anyone is interested in this format. Any suggestion is welcome.</p>

---
