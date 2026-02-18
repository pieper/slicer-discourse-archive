# Slicer Build takes too much time to compile using make command

**Topic ID**: 15828
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/slicer-build-takes-too-much-time-to-compile-using-make-command/15828

---

## Post #1 by @Hanumant_Gawali (2021-02-04 07:03 UTC)

<p>Hi there,<br>
I am trying to build slicer from source code on ubuntu 20.04, I have executes command cmake and then make in debuge directory. It is taking too much time to build near about 10 hours. Please help me for understanding exact issue in build</p>

---

## Post #2 by @jcfr (2021-02-04 07:34 UTC)

<p>It should take between 1 and 3 hours.</p>
<p>To help identify the problem, here are few questions:</p>
<ul>
<li>What are the specs of your workstation ? number of cores, type of hard drive</li>
<li>Are you running Ubuntu from within a virtual machine ?</li>
<li>Are you building in parallel by specifying <code>make -jN</code> where <code>N</code> corresponds to the number of cores ?</li>
<li>Do you have an antivirus running ?</li>
<li>Are you building on a mounted network drive ?</li>
</ul>

---

## Post #3 by @lassoan (2021-02-04 14:32 UTC)

<p>On Windows, on a desktop computer a complete build takes 3-4 hours with default settings and 2 hours with parallel build enabled (CMake config:<br>
<code>ADDITIONAL_CXX_FLAGS=/MP</code>, <code>ADDITIONAL_C_FLAGS=/MP</code>; build with <code>cmake.exe --build . -j 8</code>). On an an ultrabook laptop, build typically takes 8-10 hours.</p>
<p>In practice, build time does not make a big difference, because it is too long anyway to wait for it to end while doing nothing else, so we just start it and it runs in the background while we are working on other things. Building after making changes is fast, takes 10-20 seconds if you build the entire inner Slicer-build folder and a few seconds if you build a subproject or on an extension.</p>

---

## Post #4 by @robertsoakes (2021-05-24 15:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Can you provide any detail on how the incremental build system on Windows works? I’m trying to patch an issue preventing us from sending DICOM-SEG files back to our PACS system, and I haven’t been able to launch an incremental build.</p>
<p>If I invoke the build script from from the documentation in the root folder, I get a full end to end build (takes about four hours on my machine). I’ve been doing this by launching a the build command referenced in the documentation from the root of the build folder:</p>
<pre><code class="lang-bash">cmake.exe --build . --config Debug
</code></pre>
<p>Running the same command from the <code>Slicer-build</code> skips compilation of dependencies but still requires a significant amount of time to complete. (I started a compile of the folder, but stopped it after about 20 minutes.)</p>
<p>The last approach I’ve been taking is to compile in Visual Studio, but this also launches a full build rather than an incremental build and seems to require scores of minutes as well. Any suggestions would be appreciated.</p>
<p>PS, I’m pretty new to Slicer. Thank you for creating such a wonderful application. I’m coming from the Mimics world and it’s incredibly inspiring to see such a powerful piece of software available as open source.</p>

---

## Post #5 by @lassoan (2021-05-25 04:09 UTC)

<p>I usually open the <code>c:\D\S4D\Slicer-build\Slicer.sln</code> in Visual Studio (by going to <code>c:\S4D\Slicer-build</code> folder and launching <code>.\Slicer.exe --VisualStudioProject</code>) and run the <code>SlicerApp</code> project. I think some people also load .sln files in subfolders, which might further decrease build time</p>
<p>After a complete, successful build of SlicerApp, repeated build will only rebuild about 70 projects, typically in about a few minutes. About 10 of these are various quick tasks (copying Python files, etc), and the rest are updates of hierarchy files for the Python wrapper.</p>
<p>Based on your problem report, I did some investigation and found that update of hierarchy files is time consuming because vtkWrapHierarchy.exe searches for hundreds of header files in hundreds of include directories. Time to complete these hierarchy files updates depends on how quickly your computer can check for existence of a file. This is a very costly operation and may depend on the file system, antivirus software settings, storage hardware, operating system version, etc. As an experiment, I’ve implemented proof-of-concept pre-fetching and caching of all file paths in include directories in vtkWrapHierarchy, which made update of hierarchy files about 4-5x faster in debug mode. On my computer, a repeated build of SlicerApp project now takes about 50 seconds. I’ll discuss with VTK core developers if this improvement could be integrated into VTK.</p>

---

## Post #6 by @cpinter (2021-05-25 12:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="15828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As an experiment, I’ve implemented proof-of-concept pre-fetching and caching of all file paths in include directories in vtkWrapHierarchy, which made update of hierarchy files about 4-5x faster in debug mode</p>
</blockquote>
</aside>
<p>Wow Andras this would be great if it could be accepted in VTK. Thanks a lot for working on this!</p>

---

## Post #7 by @robertsoakes (2021-05-25 15:17 UTC)

<p>Thank you for digging into this. Your description of the problem makes a lot of sense and tracks with the (endless) <code>cmake</code> output I was seeing.</p>
<p>For the problem I was trying to fix, I was able to determine that it only affected Python code, so I edited the files in the build folder and then ported the new code to the source folder after I was sure it worked. A little annoying, but good enough that I was able to complete and test my patch.</p>
<p>Slicer is an enormous and complex application, and it’s taken me a couple of days to get familiar enough with everything to where I can make contributions. Finding a workflow for Python files that didn’t incur a 20 or 30 minute build time was the last piece of the puzzle I couldn’t quite figure out. (Your documentation, BTW, is wonderful and has been very helpful.) An efficient cache would be absolutely fantastic and would greatly facilitate a streamlined development process.</p>

---

## Post #8 by @lassoan (2021-05-25 17:56 UTC)

<aside class="quote no-group" data-username="robertsoakes" data-post="7" data-topic="15828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/robertsoakes/48/11042_2.png" class="avatar"> robertsoakes:</div>
<blockquote>
<p>Slicer is an enormous and complex application, and it’s taken me a couple of days to get familiar enough with everything to where I can make contributions</p>
</blockquote>
</aside>
<p>Finding your way around in a way days is outstanding.</p>
<p>It is interesting to note that Slicer is big in the sense that it integrates large libraries and frameworks (Qt, VTK, ITK, Python, …), but compared to these external libraries, Slicer core is relatively small.</p>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="15828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Wow Andras this would be great if it could be accepted in VTK. Thanks a lot for working on this!</p>
</blockquote>
</aside>
<p>I’ve started a discussion about this on the VTK forum:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/python-wrapping-is-slow-on-windows/5862">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/python-wrapping-is-slow-on-windows/5862" target="_blank" rel="noopener" title="05:34PM - 25 May 2021">VTK – 25 May 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/python-wrapping-is-slow-on-windows/5862" target="_blank" rel="noopener">Python wrapping is slow on Windows</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #0088CC;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Development</span>
        </span>
      </span>
  </div>
</div>

  <p>We use VTK’s Python wrapper for VTK classes in 3D Slicer and we find that on Windows it can take several minutes to generate the hierarchy files for each larger library. If we change a header file at lower level, hierarchy generation can add 10...</p>

  <p>
    <span class="label1">Reading time: 3 mins 🕑</span>
      <span class="label2">Likes: 2 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’ve also found a very important other bug in the dependency check mechanism of hierarchy files generation! Hierarchy files are kept regenerated if VTK is updated after the hierarchy files are generated. The workaround is to delete all <code>*Hierarchy.txt</code> files in <code>C:\S4R\Slicer-build</code>. See details here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/vtkAddon/issues/22">
  <header class="source">

      <a href="https://github.com/Slicer/vtkAddon/issues/22" target="_blank" rel="noopener">github.com/Slicer/vtkAddon</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/vtkAddon/issues/22" target="_blank" rel="noopener">vtkWrapHierarchy is kept re-executed</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-25" data-time="17:54:30" data-timezone="UTC">05:54PM - 25 May 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-05-29" data-time="13:03:33" data-timezone="UTC">01:03PM - 29 May 21 UTC</span>
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
    <p class="github-body-container">We experienced huge slowdowns of application builds due to vtkWrapHierarchy kept<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> rebuilding hierarchy files. For example, Slicer build took 10 minutes when nothing changed.

It turned out that this was because VTK was updated after the application was built (which is very common on developer computers). This update updated the vtkWrapHierarchy.exe file's timestamp, which is a [dependency of hierarchy file generation build step](https://github.com/Slicer/vtkAddon/blob/5f040632f8222a71b1eb3564a10ae602bcaf5f94/CMake/vtkWrapHierarchy.cmake#L156-L160). Therefore it triggers rebuilding of hierarchy file. However, the content of the hierarchy file was not changed and therefore its timestamp remained the same (older than timestamp of vtkWrapHierarchy.exe). This means that next time the hierarchy got updated again.

One solution could be vtkWrapHierarchy.cmake should be updated to touch some timestamp file each time vtkWrapHierarchy.exe was executed and use that to determine if the target is up-to-date (rather than use the timestamp of the hierarchy file).

Another solution could be to force writing of hierarchy files (update their timestamp) even if the file has not changed. Currently, [vtkWrapHierarchy only updates the output hierarchy file if its content has changed](https://github.com/Kitware/VTK/blob/37102d559386dcec314775b7dfaa1b317f3b7d7e/Wrapping/Tools/vtkWrapHierarchy.c#L964).

**Workaround to speed up builds after a VTK update**: delete all the `*Hierarchy.txt` files (for example, in c:\D\S4R\Slicer-build).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2021-05-29 13:13 UTC)

<p>The fix to avoid unnecessary *Hierarchy.txt files generation has been <a href="https://github.com/Slicer/vtkAddon/commit/8b5c4b2336a4d2d2aaafe87db3642b5302ddcaa5">integrated in to Slicer</a>.</p>
<p>Following my proof-of-concept prototype, David Gobbi has <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8026">updated the Python wrapper</a> to make *Hierarchy.txt file generation many times faster. It is expected to be integrated into VTK in the coming weeks and we’ll backport that fix into Slicer’s VTK.</p>

---

## Post #10 by @upupming (2021-08-24 09:25 UTC)

<p>I found in each rebuild of Slicer, it will take around 1 hour on VTK building, and the logs looks like the following:</p>
<pre><code class="lang-auto">[build]     Python Wrapping - generating vtkSQLiteQueryPython.cxx
[build]     Python Wrapping - generating vtkSQLiteToTableReaderPython.cxx
[build]     Python Wrapping - generating vtkTableToSQLiteWriterPython.cxx
[build]     Python Wrapping - generating vtkThreadedImageWriterPython.cxx
[build]     Python Wrapping - generating vtkEnSight6BinaryReaderPython.cxx
[build]     Python Wrapping - generating vtkEnSight6ReaderPython.cxx
[build]     Python Wrapping - generating vtkEnSightGoldBinaryReaderPython.cxx
[build]     Python Wrapping - generating vtkEnSightGoldReaderPython.cxx
[build]     Python Wrapping - generating vtkEnSightMasterServerReaderPython.cxx
[build]     Python Wrapping - generating vtkEnSightReaderPython.cxx
[build]     Python Wrapping - generating vtkGenericEnSightReaderPython.cxx
[build]     Python Wrapping - generating vtkCPExodusIIElementBlockPython.cxx
[build]     Python Wrapping - generating vtkCPExodusIIInSituReaderPython.cxx
[build]     Python Wrapping - generating vtkCPExodusIINodalCoordinatesTemplatePython.cxx
[build]     Python Wrapping - generating vtkCPExodusIIResultsArrayTemplatePython.cxx
[build]     Python Wrapping - generating vtkExodusIICachePython.cxx
[build]     Python Wrapping - generating vtkExodusIIReaderPython.cxx
[build]     Python Wrapping - generating vtkExodusIIReaderParserPython.cxx
[build]     Python Wrapping - generating vtkExodusIIWriterPython.cxx
[build]     Python Wrapping - generating vtkModelMetadataPython.cxx
[build]     Python Wrapping - generating vtkAVSucdReaderPython.cxx
[build]     Python Wrapping - generating vtkBYUReaderPython.cxx
[build]     Python Wrapping - generating vtkBYUWriterPython.cxx
[build]     Python Wrapping - generating vtkChacoReaderPython.cxx
[build]     Python Wrapping - generating vtkFacetWriterPython.cxx
[build]     Python Wrapping - generating vtkFLUENTReaderPython.cxx
[build]     Python Wrapping - generating vtkGAMBITReaderPython.cxx
[build]     Python Wrapping - generating vtkGaussianCubeReaderPython.cxx
[build]     Python Wrapping - generating vtkHoudiniPolyDataWriterPython.cxx
[build]     Python Wrapping - generating vtkIVWriterPython.cxx
[build]     Python Wrapping - generating vtkMCubesReaderPython.cxx
[build]     Python Wrapping - generating vtkMCubesWriterPython.cxx
[build]     Python Wrapping - generating vtkMFIXReaderPython.cxx
[build]     Python Wrapping - generating vtkMoleculeReaderBasePython.cxx
[build]     Python Wrapping - generating vtkOBJReaderPython.cxx
[build]     Python Wrapping - generating vtkOBJWriterPython.cxx
[build]     Python Wrapping - generating vtkOpenFOAMReaderPython.cxx
[build]     Python Wrapping - generating vtkParticleReaderPython.cxx
[build]     Python Wrapping - generating vtkPDBReaderPython.cxx
[build]     Python Wrapping - generating vtkProStarReaderPython.cxx
[build]     Python Wrapping - generating vtkPTSReaderPython.cxx
[build]     Python Wrapping - generating vtkSTLReaderPython.cxx
[build]     Python Wrapping - generating vtkSTLWriterPython.cxx
[build]     Python Wrapping - generating vtkTecplotReaderPython.cxx
[build]     Python Wrapping - generating vtkWindBladeReaderPython.cxx
[build]     Python Wrapping - generating vtkXYZMolReaderPython.cxx
[build]     Python Wrapping - generating vtkLSDynaPartPython.cxx
[build]     Python Wrapping - generating vtkLSDynaPartCollectionPython.cxx
[build]     Python Wrapping - generating vtkLSDynaReaderPython.cxx
[build]     Python Wrapping - generating vtkLSDynaSummaryParserPython.cxx
[build]     Python Wrapping - generating LSDynaMetaDataPython.cxx
[build]     Python Wrapping - generating LSDynaFamilyPython.cxx
[build]     Python Wrapping - generating vtkGenericMovieWriterPython.cxx
[build]     Python Wrapping - generating vtkOggTheoraWriterPython.cxx
[build]     Python Wrapping - generating vtkAVIWriterPython.cxx
[build]     Python Wrapping - generating vtkMPASReaderPython.cxx
[build]     Python Wrapping - generating vtkNetCDFCAMReaderPython.cxx
[build]     Python Wrapping - generating vtkNetCDFCFReaderPython.cxx
[build]     Python Wrapping - generating vtkNetCDFPOPReaderPython.cxx
[build]     Python Wrapping - generating vtkNetCDFReaderPython.cxx
[build]     Python Wrapping - generating vtkSLACParticleReaderPython.cxx
[build]     Python Wrapping - generating vtkSLACReaderPython.cxx
[build]     Python Wrapping - generating vtkPLYPython.cxx
[build]     Python Wrapping - generating vtkPLYReaderPython.cxx
[build]     Python Wrapping - generating vtkPLYWriterPython.cxx
[build]     Python Wrapping - generating vtkSegYReaderPython.cxx
[build]     Python Wrapping - generating vtkSegYIOUtilsPython.cxx
[build]     Python Wrapping - generating vtkSegYReaderInternalPython.cxx
[build]     Python Wrapping - generating vtkSegYTraceReaderPython.cxx
[build]     Python Wrapping - generating vtkVeraOutReaderPython.cxx
[build]     Python Wrapping - generating vtkVideoSourcePython.cxx
[build]     Python Wrapping - generating vtkWin32VideoSourcePython.cxx
[build]     Python Wrapping - generating vtkIOKitPythonInit.cxx
[build]     LSDynaFamilyPython.cxx
[build]     LSDynaMetaDataPython.cxx
[build]     vtkASCIITextCodecPython.cxx
[build]     vtkAVIWriterPython.cxx
[build]     vtkAVSucdReaderPython.cxx
[build]     vtkAbstractParticleWriterPython.cxx
[build]     vtkAbstractPolyDataReaderPython.cxx
[build]     vtkArrayDataReaderPython.cxx
[build]     vtkArrayDataWriterPython.cxx
[build]     vtkArrayReaderPython.cxx
[build]     vtkArrayWriterPython.cxx
[build]     vtkBMPReaderPython.cxx
[build]     vtkBMPWriterPython.cxx
[build]     vtkBYUReaderPython.cxx
[build]     vtkBYUWriterPython.cxx
[build]     vtkBase64InputStreamPython.cxx
[build]     vtkBase64OutputStreamPython.cxx
[build]     vtkBase64UtilitiesPython.cxx
[build]     vtkCPExodusIIElementBlockPython.cxx
[build]     vtkCPExodusIIInSituReaderPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkCPExodusIINodalCoordinatesTemplatePython.cxx
[build]     vtkCPExodusIIResultsArrayTemplatePython.cxx
[build]     vtkChacoReaderPython.cxx
[build]     vtkCompositeDataReaderPython.cxx
[build]     vtkCompositeDataWriterPython.cxx
[build]     vtkDEMReaderPython.cxx
[build]     vtkDICOMImageReaderPython.cxx
[build]     vtkDataCompressorPython.cxx
[build]     vtkDataObjectReaderPython.cxx
[build]     vtkDataObjectWriterPython.cxx
[build]     vtkDataReaderPython.cxx
[build]     vtkDataSetReaderPython.cxx
[build]     vtkDataSetWriterPython.cxx
[build]     vtkDataWriterPython.cxx
[build]     vtkDatabaseToTableReaderPython.cxx
[build]     vtkDelimitedTextWriterPython.cxx
[build]     vtkEnSight6BinaryReaderPython.cxx
[build]     vtkEnSight6ReaderPython.cxx
[build]     vtkEnSightGoldBinaryReaderPython.cxx
[build]     vtkEnSightGoldReaderPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkEnSightMasterServerReaderPython.cxx
[build]     vtkEnSightReaderPython.cxx
[build]     vtkExodusIICachePython.cxx
[build]     vtkExodusIIReaderParserPython.cxx
[build]     vtkExodusIIReaderPython.cxx
[build]     vtkExodusIIWriterPython.cxx
[build]     vtkFLUENTReaderPython.cxx
[build]     vtkFacetWriterPython.cxx
[build]     vtkGAMBITReaderPython.cxx
[build]     vtkGESignaReaderPython.cxx
[build]     vtkGaussianCubeReaderPython.cxx
[build]     vtkGenericDataObjectReaderPython.cxx
[build]     vtkGenericDataObjectWriterPython.cxx
[build]     vtkGenericEnSightReaderPython.cxx
[build]     vtkGenericMovieWriterPython.cxx
[build]     vtkGlobFileNamesPython.cxx
[build]     vtkGraphReaderPython.cxx
[build]     vtkGraphWriterPython.cxx
[build]     vtkHoudiniPolyDataWriterPython.cxx
[build]     vtkIOKitPythonInitImpl.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkIVWriterPython.cxx
[build]     vtkImageExportPython.cxx
[build]     vtkImageImportExecutivePython.cxx
[build]     vtkImageImportPython.cxx
[build]     vtkImageReader2CollectionPython.cxx
[build]     vtkImageReader2FactoryPython.cxx
[build]     vtkImageReader2Python.cxx
[build]     vtkImageReaderPython.cxx
[build]     vtkImageWriterPython.cxx
[build]     vtkInputStreamPython.cxx
[build]     vtkJPEGReaderPython.cxx
[build]     vtkJPEGWriterPython.cxx
[build]     vtkJSONImageWriterPython.cxx
[build]     vtkJavaScriptDataWriterPython.cxx
[build]     vtkLSDynaPartCollectionPython.cxx
[build]     vtkLSDynaPartPython.cxx
[build]     vtkLSDynaReaderPython.cxx
[build]     vtkLSDynaSummaryParserPython.cxx
[build]     vtkLZ4DataCompressorPython.cxx
[build]     vtkLZMADataCompressorPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkMCubesReaderPython.cxx
[build]     vtkMCubesWriterPython.cxx
[build]     vtkMFIXReaderPython.cxx
[build]     vtkMPASReaderPython.cxx
[build]     vtkMRCReaderPython.cxx
[build]     vtkMedicalImagePropertiesPython.cxx
[build]     vtkMedicalImageReader2Python.cxx
[build]     vtkMetaImageReaderPython.cxx
[build]     vtkMetaImageWriterPython.cxx
[build]     vtkModelMetadataPython.cxx
[build]     vtkMoleculeReaderBasePython.cxx
[build]     vtkNIFTIImageHeaderPython.cxx
[build]     vtkNIFTIImageReaderPython.cxx
[build]     vtkNIFTIImageWriterPython.cxx
[build]     vtkNetCDFCAMReaderPython.cxx
[build]     vtkNetCDFCFReaderPython.cxx
[build]     vtkNetCDFPOPReaderPython.cxx
[build]     vtkNetCDFReaderPython.cxx
[build]     vtkNrrdReaderPython.cxx
[build]     vtkNumberToStringPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkOBJReaderPython.cxx
[build]     vtkOBJWriterPython.cxx
[build]     vtkOggTheoraWriterPython.cxx
[build]     vtkOpenFOAMReaderPython.cxx
[build]     vtkOutputStreamPython.cxx
[build]     vtkPDBReaderPython.cxx
[build]     vtkPLYPython.cxx
[build]     vtkPLYReaderPython.cxx
[build]     vtkPLYWriterPython.cxx
[build]     vtkPNGReaderPython.cxx
[build]     vtkPNGWriterPython.cxx
[build]     vtkPNMReaderPython.cxx
[build]     vtkPNMWriterPython.cxx
[build]     vtkPTSReaderPython.cxx
[build]     vtkParticleReaderPython.cxx
[build]     vtkPixelExtentIOPython.cxx
[build]     vtkPolyDataReaderPython.cxx
[build]     vtkPolyDataWriterPython.cxx
[build]     vtkPostScriptWriterPython.cxx
[build]     vtkProStarReaderPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkRTXMLPolyDataReaderPython.cxx
[build]     vtkRectilinearGridReaderPython.cxx
[build]     vtkRectilinearGridWriterPython.cxx
[build]     vtkRowQueryPython.cxx
[build]     vtkRowQueryToTablePython.cxx
[build]     vtkSLACParticleReaderPython.cxx
[build]     vtkSLACReaderPython.cxx
[build]     vtkSLCReaderPython.cxx
[build]     vtkSQLDatabasePython.cxx
[build]     vtkSQLDatabaseSchemaPython.cxx
[build]     vtkSQLDatabaseTableSourcePython.cxx
[build]     vtkSQLQueryPython.cxx
[build]     vtkSQLiteDatabasePython.cxx
[build]     vtkSQLiteQueryPython.cxx
[build]     vtkSQLiteToTableReaderPython.cxx
[build]     vtkSTLReaderPython.cxx
[build]     vtkSTLWriterPython.cxx
[build]     vtkSegYIOUtilsPython.cxx
[build]     vtkSegYReaderInternalPython.cxx
[build]     vtkSegYReaderPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkSegYTraceReaderPython.cxx
[build]     vtkSimplePointsReaderPython.cxx
[build]     vtkSimplePointsWriterPython.cxx
[build]     vtkSortFileNamesPython.cxx
[build]     vtkStructuredGridReaderPython.cxx
[build]     vtkStructuredGridWriterPython.cxx
[build]     vtkStructuredPointsReaderPython.cxx
[build]     vtkStructuredPointsWriterPython.cxx
[build]     vtkTIFFReaderPython.cxx
[build]     vtkTIFFWriterPython.cxx
[build]     vtkTableReaderPython.cxx
[build]     vtkTableToDatabaseWriterPython.cxx
[build]     vtkTableToSQLiteWriterPython.cxx
[build]     vtkTableWriterPython.cxx
[build]     vtkTecplotReaderPython.cxx
[build]     vtkTextCodecFactoryPython.cxx
[build]     vtkTextCodecPython.cxx
[build]     vtkThreadedImageWriterPython.cxx
[build]     vtkTreeReaderPython.cxx
[build]     vtkTreeWriterPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkUTF16TextCodecPython.cxx
[build]     vtkUTF8TextCodecPython.cxx
[build]     vtkUnstructuredGridReaderPython.cxx
[build]     vtkUnstructuredGridWriterPython.cxx
[build]     vtkVeraOutReaderPython.cxx
[build]     vtkVideoSourcePython.cxx
[build]     vtkVolume16ReaderPython.cxx
[build]     vtkVolumeReaderPython.cxx
[build]     vtkWin32VideoSourcePython.cxx
[build]     vtkWindBladeReaderPython.cxx
[build]     vtkWriterPython.cxx
[build]     vtkXMLCompositeDataReaderPython.cxx
[build]     vtkXMLCompositeDataWriterPython.cxx
[build]     vtkXMLDataObjectWriterPython.cxx
[build]     vtkXMLDataParserPython.cxx
[build]     vtkXMLDataReaderPython.cxx
[build]     vtkXMLDataSetWriterPython.cxx
[build]     vtkXMLFileReadTesterPython.cxx
[build]     vtkXMLGenericDataObjectReaderPython.cxx
[build]     vtkXMLHierarchicalBoxDataFileConverterPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkXMLHierarchicalBoxDataReaderPython.cxx
[build]     vtkXMLHierarchicalBoxDataWriterPython.cxx
[build]     vtkXMLHierarchicalDataReaderPython.cxx
[build]     vtkXMLHyperTreeGridReaderPython.cxx
[build]     vtkXMLHyperTreeGridWriterPython.cxx
[build]     vtkXMLImageDataReaderPython.cxx
[build]     vtkXMLImageDataWriterPython.cxx
[build]     vtkXMLMultiBlockDataReaderPython.cxx
[build]     vtkXMLMultiBlockDataWriterPython.cxx
[build]     vtkXMLMultiGroupDataReaderPython.cxx
[build]     vtkXMLPDataObjectReaderPython.cxx
[build]     vtkXMLPDataReaderPython.cxx
[build]     vtkXMLPImageDataReaderPython.cxx
[build]     vtkXMLPPolyDataReaderPython.cxx
[build]     vtkXMLPRectilinearGridReaderPython.cxx
[build]     vtkXMLPStructuredDataReaderPython.cxx
[build]     vtkXMLPStructuredGridReaderPython.cxx
[build]     vtkXMLPTableReaderPython.cxx
[build]     vtkXMLPUnstructuredDataReaderPython.cxx
[build]     vtkXMLPUnstructuredGridReaderPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkXMLParserPython.cxx
[build]     vtkXMLPartitionedDataSetCollectionReaderPython.cxx
[build]     vtkXMLPartitionedDataSetCollectionWriterPython.cxx
[build]     vtkXMLPartitionedDataSetReaderPython.cxx
[build]     vtkXMLPartitionedDataSetWriterPython.cxx
[build]     vtkXMLPolyDataReaderPython.cxx
[build]     vtkXMLPolyDataWriterPython.cxx
[build]     vtkXMLReaderPython.cxx
[build]     vtkXMLRectilinearGridReaderPython.cxx
[build]     vtkXMLRectilinearGridWriterPython.cxx
[build]     vtkXMLStructuredDataReaderPython.cxx
[build]     vtkXMLStructuredDataWriterPython.cxx
[build]     vtkXMLStructuredGridReaderPython.cxx
[build]     vtkXMLStructuredGridWriterPython.cxx
[build]     vtkXMLTableReaderPython.cxx
[build]     vtkXMLTableWriterPython.cxx
[build]     vtkXMLUniformGridAMRReaderPython.cxx
[build]     vtkXMLUniformGridAMRWriterPython.cxx
[build]     vtkXMLUnstructuredDataReaderPython.cxx
[build]     vtkXMLUnstructuredDataWriterPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkXMLUnstructuredGridReaderPython.cxx
[build]     vtkXMLUnstructuredGridWriterPython.cxx
[build]     vtkXMLUtilitiesPython.cxx
[build]     vtkXMLWriterCPython.cxx
[build]     vtkXMLWriterPython.cxx
[build]     vtkXYZMolReaderPython.cxx
[build]     vtkZLibDataCompressorPython.cxx
[build]     Generating Code...
[build]        Creating library C:/D/S4/out/build/RelWithDebInfo/VTK-build/lib/Debug/vtkIOKitPython36D-8.2.lib and object C:/D/S4/out/build/RelWithDebInfo/VTK-build/lib/Debug/vtkIOKitPython36D-8.2.exp
[build]     vtkIOKitPythonD.vcxproj -&gt; C:\D\S4\out\build\RelWithDebInfo\VTK-build\bin\Debug\vtkIOKitPython36D-8.2.dll
[build]     Python Wrapping - generating vtkAddMembershipArrayPython.cxx
[build]     Python Wrapping - generating vtkAdjacencyMatrixToEdgeTablePython.cxx
[build]     Python Wrapping - generating vtkArrayNormPython.cxx
[build]     Python Wrapping - generating vtkArrayToTablePython.cxx
[build]     Python Wrapping - generating vtkCollapseGraphPython.cxx
[build]     Python Wrapping - generating vtkCollapseVerticesByArrayPython.cxx
[build]     Python Wrapping - generating vtkContinuousScatterplotPython.cxx
[build]     Python Wrapping - generating vtkDataObjectToTablePython.cxx
[build]     Python Wrapping - generating vtkDotProductSimilarityPython.cxx
[build]     Python Wrapping - generating vtkExtractSelectedTreePython.cxx
[build]     Python Wrapping - generating vtkEdgeCentersPython.cxx
[build]     Python Wrapping - generating vtkExpandSelectedGraphPython.cxx
[build]     Python Wrapping - generating vtkExtractSelectedGraphPython.cxx
[build]     Python Wrapping - generating vtkGenerateIndexArrayPython.cxx
[build]     Python Wrapping - generating vtkGraphHierarchicalBundleEdgesPython.cxx
[build]     Python Wrapping - generating vtkGroupLeafVerticesPython.cxx
[build]     Python Wrapping - generating vtkMergeColumnsPython.cxx
[build]     Python Wrapping - generating vtkMergeGraphsPython.cxx
[build]     Python Wrapping - generating vtkMergeTablesPython.cxx
[build]     Python Wrapping - generating vtkMutableGraphHelperPython.cxx
[build]     Python Wrapping - generating vtkNetworkHierarchyPython.cxx
[build]     Python Wrapping - generating vtkPipelineGraphSourcePython.cxx
[build]     Python Wrapping - generating vtkPruneTreeFilterPython.cxx
[build]     Python Wrapping - generating vtkRandomGraphSourcePython.cxx
[build]     Python Wrapping - generating vtkReduceTablePython.cxx
[build]     Python Wrapping - generating vtkRemoveIsolatedVerticesPython.cxx
[build]     Python Wrapping - generating vtkSparseArrayToTablePython.cxx
[build]     Python Wrapping - generating vtkStreamGraphPython.cxx
[build]     Python Wrapping - generating vtkStringToCategoryPython.cxx
[build]     Python Wrapping - generating vtkStringToNumericPython.cxx
[build]     Python Wrapping - generating vtkTableToArrayPython.cxx
[build]     Python Wrapping - generating vtkTableToGraphPython.cxx
[build]     Python Wrapping - generating vtkTableToSparseArrayPython.cxx
[build]     Python Wrapping - generating vtkTableToTreeFilterPython.cxx
[build]     Python Wrapping - generating vtkThresholdGraphPython.cxx
[build]     Python Wrapping - generating vtkThresholdTablePython.cxx
[build]     Python Wrapping - generating vtkTransferAttributesPython.cxx
[build]     Python Wrapping - generating vtkTransposeMatrixPython.cxx
[build]     Python Wrapping - generating vtkTreeFieldAggregatorPython.cxx
[build]     Python Wrapping - generating vtkTreeDifferenceFilterPython.cxx
[build]     Python Wrapping - generating vtkTreeLevelsFilterPython.cxx
[build]     Python Wrapping - generating vtkVertexDegreePython.cxx
[build]     Python Wrapping - generating vtkRemoveHiddenDataPython.cxx
[build]     Python Wrapping - generating vtkKCoreDecompositionPython.cxx
[build]     Python Wrapping - generating vtkInfovisCorePythonInit.cxx
[build]     vtkAddMembershipArrayPython.cxx
[build]     vtkAdjacencyMatrixToEdgeTablePython.cxx
[build]     vtkArrayNormPython.cxx
[build]     vtkArrayToTablePython.cxx
[build]     vtkCollapseGraphPython.cxx
[build]     vtkCollapseVerticesByArrayPython.cxx
[build]     vtkContinuousScatterplotPython.cxx
[build]     vtkDataObjectToTablePython.cxx
[build]     vtkDotProductSimilarityPython.cxx
[build]     vtkEdgeCentersPython.cxx
[build]     vtkExpandSelectedGraphPython.cxx
[build]     vtkExtractSelectedGraphPython.cxx
[build]     vtkExtractSelectedTreePython.cxx
[build]     vtkGenerateIndexArrayPython.cxx
[build]     vtkGraphHierarchicalBundleEdgesPython.cxx
[build]     vtkGroupLeafVerticesPython.cxx
[build]     vtkInfovisCorePythonInitImpl.cxx
[build]     vtkKCoreDecompositionPython.cxx
[build]     vtkMergeColumnsPython.cxx
[build]     vtkMergeGraphsPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkMergeTablesPython.cxx
[build]     vtkMutableGraphHelperPython.cxx
[build]     vtkNetworkHierarchyPython.cxx
[build]     vtkPipelineGraphSourcePython.cxx
[build]     vtkPruneTreeFilterPython.cxx
[build]     vtkRandomGraphSourcePython.cxx
[build]     vtkReduceTablePython.cxx
[build]     vtkRemoveHiddenDataPython.cxx
[build]     vtkRemoveIsolatedVerticesPython.cxx
[build]     vtkSparseArrayToTablePython.cxx
[build]     vtkStreamGraphPython.cxx
[build]     vtkStringToCategoryPython.cxx
[build]     vtkStringToNumericPython.cxx
[build]     vtkTableToArrayPython.cxx
[build]     vtkTableToGraphPython.cxx
[build]     vtkTableToSparseArrayPython.cxx
[build]     vtkTableToTreeFilterPython.cxx
[build]     vtkThresholdGraphPython.cxx
[build]     vtkThresholdTablePython.cxx
[build]     vtkTransferAttributesPython.cxx
[build]     Generating Code...
[build]     Compiling...
[build]     vtkTransposeMatrixPython.cxx
[build]     vtkTreeDifferenceFilterPython.cxx
[build]     vtkTreeFieldAggregatorPython.cxx
[build]     vtkTreeLevelsFilterPython.cxx
[build]     vtkVertexDegreePython.cxx
[build]     Generating Code...
[build]        Creating library C:/D/S4/out/build/RelWithDebInfo/VTK-build/lib/Debug/vtkInfovisCorePython36D-8.2.lib and object C:/D/S4/out/build/RelWithDebInfo/VTK-build/lib/Debug/vtkInfovisCorePython36D-8.2.exp
[build]     vtkInfovisCorePythonD.vcxproj -&gt; C:\D\S4\out\build\RelWithDebInfo\VTK-build\bin\Debug\vtkInfovisCorePython36D-8.2.dll
[build]     Python Wrapping - generating vtkAbstractMapper3DPython.cxx
[build]     Python Wrapping - generating vtkAbstractMapperPython.cxx
[build]     Python Wrapping - generating vtkAbstractPickerPython.cxx
[build]     Python Wrapping - generating vtkAbstractVolumeMapperPython.cxx
[build]     Python Wrapping - generating vtkActor2DCollectionPython.cxx
[build]     Python Wrapping - generating vtkActor2DPython.cxx
[build]     Python Wrapping - generating vtkActorCollectionPython.cxx
[build]     Python Wrapping - generating vtkActorPython.cxx
[build]     Python Wrapping - generating vtkAssemblyPython.cxx
[build]     Python Wrapping - generating vtkBackgroundColorMonitorPython.cxx
[build]     Python Wrapping - generating vtkBillboardTextActor3DPython.cxx
[build]     Python Wrapping - generating vtkCameraActorPython.cxx
[build]     Python Wrapping - generating vtkCameraPython.cxx
[build]     Python Wrapping - generating vtkCameraInterpolatorPython.cxx
[build]     Python Wrapping - generating vtkCellCenterDepthSortPython.cxx
[build]     Python Wrapping - generating vtkCIEDE2000Python.cxx
[build]     Python Wrapping - generating vtkColorTransferFunctionPython.cxx
[build]     Python Wrapping - generating vtkCompositeDataDisplayAttributesPython.cxx
[build]     Python Wrapping - generating vtkCompositeDataDisplayAttributesLegacyPython.cxx
[build]     Python Wrapping - generating vtkCompositePolyDataMapperPython.cxx
[build]     Python Wrapping - generating vtkCoordinatePython.cxx
</code></pre>
<p>This is the most time-consuming step during rebuild of Slicer, is there anyway can I reduce the rebuild time?</p>
<p>The build command I used is:</p>
<pre><code class="lang-auto">"C:\Program Files\CMake\bin\cmake.EXE" --build c:/D/S4/out/build/RelWithDebInfo --parallel 12
</code></pre>

---

## Post #11 by @lassoan (2021-08-24 12:55 UTC)

<p>This happens because a VTK bug that always rebuilds hierarchy files if the build was not clean and very slow check in the VTK Python wrapper if a file exists. With help from David Gobbi, we fixed both issues in VTK about a month ago, but we have not yet backported these improvements into Slicer.</p>
<p>You can fix the first problem quite easily:</p>
<ol>
<li>Rebuild Slicer (including all dependencies) completely from scratch, from a clean build folder.</li>
<li>If you just change Slicer and its modules, don’t build the top-level folder (c:\D\S4R\Slicer.sln), which builds all the dependencies, only the inner-build (c:\D\S4R\Slicer-build\Slicer.sln)</li>
</ol>
<p>We’ll soon rebase Slicer’s VTK on the latest VTK master, which will speed up hierarchy file generation several times faster.</p>

---

## Post #12 by @upupming (2021-08-24 12:56 UTC)

<p>Thanks for pointing it out. Nice to see you are going to rebase the new VTK version! I will try the two methods to see how they change the build time.</p>

---
