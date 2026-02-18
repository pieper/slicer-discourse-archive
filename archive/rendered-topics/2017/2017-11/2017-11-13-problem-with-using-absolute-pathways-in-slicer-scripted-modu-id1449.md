# Problem with using absolute pathways in Slicer scripted modules

**Topic ID**: 1449
**Date**: 2017-11-13
**URL**: https://discourse.slicer.org/t/problem-with-using-absolute-pathways-in-slicer-scripted-modules/1449

---

## Post #1 by @purav70 (2017-11-13 17:09 UTC)

<p>Hi there.</p>
<p>While implementing my own scripted module, I was required to add a specific executable to the python resources in its cmake file:</p>
<pre><code class="lang-auto">  set(MODULE_PYTHON_RESOURCES
  ${ALPHA_SHAPES_3_EXECUTABLE}
  Resources/Icons/${MODULE_NAME}.png
  )
</code></pre>
<p>The path of ${ALPHA_SHAPES_3_EXECUTABLE} is absolute, I double checked using the IS_ABSOLUTE function.</p>
<p>However, upon execution, it misreads this absolute path as a relative path, which causes build errors. I’ve narrowed down the problem to ctkMacroCompilePythonScript.cmake.</p>
<pre><code class="lang-auto">  if(DEFINED MY_RESOURCES)
    set(resource_input_files)
    foreach(file ${MY_RESOURCES})
      if(NOT IS_ABSOLUTE ${file})
        set(src "${MY_SOURCE_DIR}/${file}")
      else()
        set(src "${file}")
      endif()
      set_property(GLOBAL APPEND PROPERTY
      _CTK_${target}_PYTHON_RESOURCES "${src}|${file}|${MY_DESTINATION_DIR}")
    endforeach()
  endif()
</code></pre>
<p>The code runs into the problem upon setting the tgt:</p>
<pre><code class="lang-auto">list(GET tuple 0 src)
list(GET tuple 1 tgt_file)
list(GET tuple 2 dest_dir)
set(tgt ${dest_dir}/${tgt_file})
</code></pre>
<p>where tgt_file is taken as the entire filepath, not just the file name - even for absolute paths.</p>
<p>In an attempt to fix the issue, I made the following changes, but it seems to crash CTK:</p>
<pre><code class="lang-auto">if(DEFINED MY_RESOURCES)
    set(resource_input_files)
    foreach(file ${MY_RESOURCES})
      if(NOT IS_ABSOLUTE ${file})
        set(src "${MY_SOURCE_DIR}/${file}")
	set_property(GLOBAL APPEND PROPERTY
        _CTK_${target}_PYTHON_RESOURCES "${src}|${file}|${MY_DESTINATION_DIR}")
      else()
	set(src "${file}")
	get_filename_component(tgt_file_only ${file} NAME)
	set_property(GLOBAL APPEND PROPERTY
        _CTK_${target}_PYTHON_RESOURCES "${src}|${tgt_file_only}|${MY_DESTINATION_DIR}")
      endif()
    endforeach()
  endif()
</code></pre>
<p>Any guidance would me much appreciated.</p>
<p>Thanks,</p>
<p>Purav</p>

---

## Post #2 by @lassoan (2017-11-13 17:19 UTC)

<p>Executable is not really a resource file, as it has to be placed in specific location to allow it to run, maybe fix up rpath (for MacOSX), etc. Do you build the executable? Is that open-source? If yes, then follow the pattern used by <a href="https://github.com/lassoan/SlicerElastix">SlicerElastix</a>.</p>

---

## Post #3 by @purav70 (2017-11-13 17:24 UTC)

<p>Yup, the executable is built from open source code that I modified. I find the .exe using cmake, by having it as one of the flags, and the reason I wish to list it as a resource is to have it copied to the destination directory (where the .py files of the extension are copied to).</p>
<p>The cmake and source code changes I made work locally without having slicer rebuilt, however the code edit seems to break CTK.</p>

---

## Post #4 by @lassoan (2017-11-13 17:30 UTC)

<p>OK, then follow what is done in <a href="https://github.com/lassoan/SlicerElastix">SlicerElastix</a> - it does exactly what you need (downloads &amp; builds the external library, passes targets to the Slicer extension, adds it to the extension package, etc.). Another example is <a href="https://github.com/lassoan/slicersegmentmesher">SegmentMesher</a>.</p>

---

## Post #5 by @purav70 (2017-11-13 17:45 UTC)

<p>I would prefer not to download and build the external library every time, given its size, and given that it has hundreds of executables, only 1 of which I wish to use. If there is a way to tackle this issue using the code I wrote/modified, please let me know. Otherwise I’ll resort to the extensions you mentioned above.</p>

---

## Post #6 by @lassoan (2017-11-13 18:34 UTC)

<p>If you just need alpha shapes algorithm, then you can use <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel">Markups To Model</a> extension. It can create a 3D surface mesh from a sparse set of points. It uses <a href="https://www.vtk.org/doc/nightly/html/classvtkDelaunay3D.html">vtkDelaunay3D filter</a>. To enable alpha shapes, set Convexity (Alpha) parameter to &gt;0.</p>
<p>There may be other relevant modules, so in general, before writing any custom extension it is useful to write to the forum what your goal is and ask if anyone has implemented a similar solution already.</p>
<p>If you need to use a specific alpha shapes implementation and not the one in VTK then there are a couple of options:</p>
<ul>
<li>A. Building it as part of your module. It is the proper way, it ensures that the library is built and packaged properly for any platform that Slicer uses. If the library build system uses CMake and it is modularized then you can configure to build only the components that you need. See SlicerElastix, SegmentMesher extensions as examples.</li>
<li>B. If an algorithm is in a widely used library (such as OpenCV, CGAL, …) then an option is to build that library with all commonly needed features enabled as a Slicer extension. Then, other extensions that need features from this library can depend on this extension. This has already been implemented for OpenCV but it can be done for other libraries, too. See SlicerOpenCV extension as an example.</li>
<li>C. Download binaries. See how <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/ScreenCapture/ScreenCapture.py">ScreenCapture</a> module downloads ffmpeg executable.</li>
<li>D. Add compiled binaries to your extension. Create a target that “builds” the binary by simply copying the file corresponding to the current platform. Add the binary to the extension package by appending installation information to CPACK_INSTALL_CMAKE_PROJECTS variable.</li>
</ul>

---

## Post #7 by @purav70 (2017-11-14 16:34 UTC)

<p>Thanks Andras, I ended up creating a module using the vtkDelaunay3D filter - I didn’t even realize it existed.</p>

---
