---
topic_id: 26736
title: "Model Point Count Changing After Transformation"
date: 2022-12-14
url: https://discourse.slicer.org/t/26736
---

# Model point count changing after transformation

**Topic ID**: 26736
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/model-point-count-changing-after-transformation/26736

---

## Post #1 by @muratmaga (2022-12-14 20:46 UTC)

<p>We have a visualization tool in SlicerMorph that applies a TPS transformation derived from PCA to a reference model. I have exported transformed models. I am trying to use the model to model distance to visualize a heatmap (using the reference model as the target), specifically with the “corresponding point to point option”.</p>
<p>This generates an error that says:</p>
<pre><code class="lang-auto">Model To Model Distance standard error:

Both input files must have the same number of points to use 'corresponding_point_to_point'
Source model has 172232 points
Target model has 172259 points
</code></pre>
<p>However, if I go to Models menu and check the point counts for these models, they are reported identically and as 173261. Any idea where/why the difference might be coming from?</p>

---

## Post #2 by @lassoan (2022-12-14 21:40 UTC)

<p>Geometric transformation does not change number of points. How did you apply the transform? I suspect that normals were computed for one or both of the surfaces before or after transforming, which can duplicate points (to allow proper rendering of sharp edges).</p>

---

## Post #3 by @muratmaga (2022-12-14 21:52 UTC)

<p>As I export the file, I chose apply transform. But the thing is for the transformed models, Models module report point numbers identical to the original model. That baffles me.</p>

---

## Post #4 by @smrolfe (2022-12-14 22:02 UTC)

<p>It looks like there’s a <a href="https://github.com/NIRALUser/3DMetricTools/blob/4b4e478f9e20ecef0f66a20eb6719bd4a8c4d949/ModelToModelDistance/ModelToModelDistance.cxx#L340" rel="noopener nofollow ugc">step that is cleaning and removing degenerate points</a> from the input and output models, maybe there’s an issue like this with the transformed model?</p>
<p>I tried one example with the GPA module and didn’t see this error.</p>

---

## Post #5 by @muratmaga (2022-12-14 22:04 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="4" data-topic="26736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I tried one example with the GPA module and didn’t see this error.</p>
</blockquote>
</aside>
<p>Can you try with <a href="https://github.com/SlicerMorph/Mouse_Models" class="inline-onebox">GitHub - SlicerMorph/Mouse_Models</a> and skip the scaling at GPA?</p>

---

## Post #6 by @smrolfe (2022-12-14 22:07 UTC)

<p>I’m getting the expected result for this dataset:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4df08d317c36046206dcaf3fefc1f18e14ed11.jpeg" data-download-href="/uploads/short-url/fSDZ16JhSbiQLG7j2qbO8ERwa6B.jpeg?dl=1" title="Screen Shot 2022-12-14 at 2.22.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4df08d317c36046206dcaf3fefc1f18e14ed11_2_690x343.jpeg" alt="Screen Shot 2022-12-14 at 2.22.29 PM" data-base62-sha1="fSDZ16JhSbiQLG7j2qbO8ERwa6B" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4df08d317c36046206dcaf3fefc1f18e14ed11_2_690x343.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4df08d317c36046206dcaf3fefc1f18e14ed11_2_1035x514.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4df08d317c36046206dcaf3fefc1f18e14ed11.jpeg 2x" data-dominant-color="475EBE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-12-14 at 2.22.29 PM</span><span class="informations">1278×636 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @muratmaga (2022-12-14 22:28 UTC)

<p>That can’t be, I think you didn’t skip the scaling step. Make sure you are using the data from the repo linked (not the slicermorph sample data).</p>

---

## Post #8 by @lassoan (2022-12-14 22:36 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="4" data-topic="26736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>It looks like there’s a <a href="https://github.com/NIRALUser/3DMetricTools/blob/4b4e478f9e20ecef0f66a20eb6719bd4a8c4d949/ModelToModelDistance/ModelToModelDistance.cxx#L340">step that is cleaning and removing degenerate points </a> from the input and output models, maybe there’s an issue like this with the transformed model?</p>
</blockquote>
</aside>
<p>Points may become “degenerate” if their positions are changed, so it is normal that a geometric transform changes the number of points after such cleanup.</p>
<p>If the processing step is unavoidable then you can store <code>PedigreeIds</code> (point ID in the input of the filter) or <code>GlobalIds</code> (some global point ID) in point scalars and make sure that all the used filters preserve point data. ModelToModelDistance module could use these point data to match points between differently processed meshes.</p>

---

## Post #9 by @smrolfe (2022-12-14 22:42 UTC)

<p>Yes, that was the SM sample data. I reran with the data from GitHub and am not seeing an error, but that could be the choice of reference model or transform type.</p>

---

## Post #10 by @muratmaga (2022-12-14 22:43 UTC)

<p>I chose the FVB_NJ, which should be the sample reported as the closest to the mean. You should see a really strong size effect overall.</p>

---

## Post #11 by @smrolfe (2022-12-15 21:14 UTC)

<p>After testing, we found it’s the SlicerMorph extension that breaks the operation of the model to model distance module, but it only happens on Windows. Linux and Mac work as expected with exactly the same Slicer version and settings.</p>
<p>I don’t see any libraries or other dependencies that could result in this kind of OS specific difference. <a class="mention" href="/u/lassoan">@lassoan</a> do you have any ideas? Even importing a single module from the SlicerMorph module causes this difference</p>

---

## Post #12 by @muratmaga (2022-12-15 21:25 UTC)

<p>And removing the SlicerMorph extension fixes the issue. And the only effected functionality is the point-to-point distance calculations, others work fine regardless whether SlicerMorph is installed or not on Windows.</p>
<p>We do not have any idea how to debug this, so your input is most welcomed.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #13 by @pieper (2022-12-15 21:46 UTC)

<p>That’s really strange.  It implies there’s some kind of environment change that causes a side effect, like a library path or variable setting.  From a quick look it seems the ModelToModel distance is a pure C++ CLI so maybe it’s a windows system dll.</p>
<p>One way to debug could be to open the <a href="https://www.dependencywalker.com/">depends</a> from Slicer with and without the SlicerMorph module and compare the trees when examining the CLI executable.  Start it from python with something like <code>os.system(r"C:\Users\piepe\Downloads\depends22_x86\depends.exe")</code> then do File-&gt;Open and browse to the CLI executable.</p>

---

## Post #14 by @lassoan (2022-12-15 21:46 UTC)

<p>What file format do you use for saving meshes? Have you changed any default node settings related to saving meshes?</p>

---

## Post #15 by @pieper (2022-12-15 21:47 UTC)

<p>Interesting point - the MorphPreferences do switch the storage node to ply by default.</p>

---

## Post #16 by @muratmaga (2022-12-15 21:58 UTC)

<p>but it works without slicermorph. All data is already saved as ply.</p>

---

## Post #17 by @lassoan (2022-12-15 22:08 UTC)

<p>Check if you can see any difference when you save to file and load that file. There should be no difference when saving into VTK or VTP format, but there could be subtle differences when exporting/importing non-VTK file formats.</p>

---

## Post #18 by @muratmaga (2022-12-16 04:53 UTC)

<p>I saved the models under the PCA transform as VTK and OBJ and with both formats, and I am still seeing the same error in Model to Model Distance corresponding point to point calculation option if SlicerMorph is installed. Again, only windows build seems to be affected.</p>
<p>If SlicerMorph is uninstalled, calculation with any format (ply, obj, vtk) work fine. I don’t think the issue is coming from the export step.</p>
<p><a href="https://app.box.com/s/plth0mmkovmqrvizoa9j5t3y9dibx0j6">I uploaded all six model here</a> if anyone wants to try to.</p>
<p>I set PC1 as source model, and Mean as target (though order doesn’t seem to matter for error generation).</p>

---

## Post #19 by @muratmaga (2022-12-16 05:12 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
I have uploaded the output from DW with and without SlicerMorph <a href="https://app.box.com/s/plth0mmkovmqrvizoa9j5t3y9dibx0j6">here</a>. I can’t tell much from it.</p>

---

## Post #20 by @lassoan (2022-12-16 06:32 UTC)

<p>ModelToModelDistance module <a href="https://github.com/NIRALUser/3DMetricTools/blob/master/ModelToModelDistance/ModelToModelDistance.cxx#L85">runs the inputs through <code>vtkCleanPolyData</code></a>, which of course changes the number of points (merging of coincident points is one of the most useful cleaning feature). You can see that when you apply Clean step in Surface toolbox module in Slicer then the number of points in the meshes are reduced to exactly 172245 and and 172232 points as expected. Therefore, <strong>Model2ModelDistance extension must be fixed: cleaning must be skipped when <code>corresponding_point_to_point</code> mode is used.</strong></p>
<p>The only somewhat mysterious finding is that why SlicerMorph appear to change the behavior. By the way, I was not able to reproduce the difference between installing SlicerMorph or not on Windows: if I use the .vtk files in the shared folder as inputs then Model to model distance module fails if <code>corresponding_point_to_point</code> option is used because of point count mismatch - even on a computer where SlicerMorph has never been installed. <strong>It may worth checking why on linux and macos model to model distance computation mode succeeds</strong> when corresponding point option is used; because it should fail on all platforms.</p>

---

## Post #21 by @pieper (2022-12-16 16:13 UTC)

<p>It sounds like dependency walker is a red herring.</p>
<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> first step would be to explore fixing the module.</p>
<p>Then we could explore these platform / environment specific issues if they haven’t gone away.</p>

---

## Post #22 by @muratmaga (2022-12-16 18:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="21" data-topic="26736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> first step would be to explore fixing the module.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is any of the extension developers are on this forum?</p>

---

## Post #23 by @lassoan (2022-12-16 20:17 UTC)

<p>It is a trivial change (just skip the <a href="https://github.com/NIRALUser/3DMetricTools/blob/master/ModelToModelDistance/ModelToModelDistance.cxx#L85">cleaning step</a> if corresponding points are used). If you test it locally and send a pull request then we can get it merged quickly. Both <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> seem to have commit rights to the extension.</p>

---

## Post #24 by @smrolfe (2022-12-16 21:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="26736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><strong>It may worth checking why on linux and macos model to model distance computation mode succeeds</strong> when corresponding point option is used; because it should fail on all platforms.</p>
</blockquote>
</aside>
<p>When it does run on Linux and Mac, the output point number is equal to the reduced point number generated by vtkCleanPolyData, not the input mesh, so I suspect it may not actually be generating the point-to-point results.</p>

---

## Post #25 by @jcfr (2022-12-16 22:34 UTC)

<blockquote>
<p>It is a trivial change (just skip the <em>cleaning step</em> if corresponding points are used).</p>
</blockquote>
<p>See <a href="https://github.com/NIRALUser/3DMetricTools/pull/12" class="inline-onebox">ModelToModelDistance: Skip cleaning if corresponding_point_to_point mode is set by jcfr · Pull Request #12 · NIRALUser/3DMetricTools · GitHub</a></p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a>  Let me know if that addresses the issue.</p>

---

## Post #26 by @smrolfe (2022-12-20 06:35 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> it looks like this should fix the issue. I just tried to build the extension to test, but am having a problem with the ITK/VTK builds, which are failing with errors:</p>
<blockquote>
<p>2&gt;Performing download step (git clone) for ‘VTK’<br>
2&gt;Cloning into ‘VTK’…<br>
3&gt;Performing download step (git clone) for ‘ITKv4’<br>
3&gt;Cloning into ‘ITKv4’…<br>
3&gt;fatal: repository ‘<a href="http://itk.org/ITK.git/" rel="noopener nofollow ugc">http://itk.org/ITK.git/</a>’ not found<br>
2&gt;fatal: repository ‘<a href="http://vtk.org/VTK.git/" class="inline-onebox" rel="noopener nofollow ugc">VTK / VTK · GitLab</a>’ not found</p>
</blockquote>
<p>This looks like errors I’ve gotten when building Slicer behind our firewall with USE_GIT_PROTOCOL enabled, but I’ve checked that it’s disabled for this extension build.</p>

---

## Post #27 by @muratmaga (2022-12-22 19:38 UTC)

<p>We can build other extensions, but this seems to fail for us. Can anyone else have this issue?<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #28 by @jcfr (2022-12-22 21:11 UTC)

<p>Since we focus our effort on building the extension against Slicer and not into supporting building the project as a standalone project, I suggest you configure the extension directly passing <code>Slicer_DIR</code>.</p>
<p>After removing the content of the build directory, there are two ways:</p>
<ul>
<li>start <code>cmake-gui</code>, add an entry called <code>Slicer_DIR</code> pointing to the <code>C:/path/to/Slicer-Release/Slicer-build</code></li>
<li>directly from the command-line with <code>cmake -DSlicer_DIR:PATH=C:/path/to/Slicer-Release/Slicer-build -S C:/path/to/3DMetricTools -B C:/path/to/3DMetricTools-Release</code></li>
</ul>
<p>If using a single config generator (e.g <code>Unix Makefiles</code>), specify <code>CMAKE_BUILD_TYPE</code> to <code>Release</code>.</p>
<h3><a name="p-88015-background-1" class="anchor" href="#p-88015-background-1" aria-label="Heading link"></a>Background</h3>
<p>Setting reasonable default during the first configuration is the approach we have been using for most extension intended to be build as either a Slicer extension or an independent</p>
<p>This is explained by the following logic:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L4-L17">
  <header class="source">

      <a href="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L4-L17" target="_blank" rel="noopener">github.com/NIRALUser/3DMetricTools</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L4-L17" target="_blank" rel="noopener">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L4-L17" rel="noopener"><code>ff114ebc8</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="4" style="counter-reset: li-counter 3 ;">
          <li>set(_msg "Setting C++ standard")</li>
          <li>message(STATUS "${_msg}")</li>
          <li>if(NOT DEFINED CMAKE_CXX_STANDARD)</li>
          <li>  if(DEFINED Qt5_DIR OR DEFINED Slicer_DIR)</li>
          <li>    set(CMAKE_CXX_STANDARD 17)</li>
          <li>  elseif("${3DMetricTools_VTK_VERSION_MAJOR}" STREQUAL "8")</li>
          <li>    set(CMAKE_CXX_STANDARD 11)</li>
          <li>  else()</li>
          <li>    set(CMAKE_CXX_STANDARD 98)</li>
          <li>  endif()</li>
          <li>endif()</li>
          <li>set(CMAKE_CXX_STANDARD_REQUIRED ON)</li>
          <li>set(CMAKE_CXX_EXTENSIONS OFF)</li>
          <li>message(STATUS "${_msg} - C++${CMAKE_CXX_STANDARD}")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L45-L61">
  <header class="source">

      <a href="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L45-L61" target="_blank" rel="noopener">github.com/NIRALUser/3DMetricTools</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L45-L61" target="_blank" rel="noopener">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/NIRALUser/3DMetricTools/blob/ff114ebc86603773bb32a96b08ccab7713c7e57e/CMakeLists.txt#L45-L61" rel="noopener"><code>ff114ebc8</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
          <li>set(_default OFF)</li>
          <li>set(_reason "${EXTENSION_NAME}_BUILD_SLICER_EXTENSION is ON")</li>
          <li>if(NOT DEFINED ${EXTENSION_NAME}_BUILD_SLICER_EXTENSION AND DEFINED Slicer_DIR)</li>
          <li>  set(_default ON)</li>
          <li>  set(_reason "Slicer_DIR is SET")</li>
          <li>endif()</li>
          <li></li>
          <li>option(${EXTENSION_NAME}_BUILD_SLICER_EXTENSION "Build as a Slicer Extension" ${_default})</li>
          <li></li>
          <li>set(_msg "Checking if building as a Slicer extension")</li>
          <li>message(STATUS ${_msg})</li>
          <li>if(${EXTENSION_NAME}_BUILD_SLICER_EXTENSION)</li>
          <li>  message(STATUS "${_msg} - yes (${_reason})")</li>
          <li>else()</li>
          <li>  message(STATUS "${_msg} - no (${EXTENSION_NAME}_BUILD_SLICER_EXTENSION is OFF)")</li>
          <li>endif()</li>
          <li>mark_as_superbuild(${EXTENSION_NAME}_BUILD_SLICER_EXTENSION:BOOL)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #29 by @smrolfe (2022-12-23 07:28 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> I’m using the instructions in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" rel="noopener nofollow ugc">extensions documentation</a> which includes adding the Slicer_DIR variable, so this has not resolved the git-related error. Is there anything else that might cause this? I did not get this error when I built Slicer.</p>

---

## Post #30 by @smrolfe (2022-12-23 07:32 UTC)

<p>I also got the following error on configuring:</p>
<blockquote>
<p>CMake Error at C:/Program Files/CMake/share/cmake-3.23/Modules/FindQt4.cmake:1314 (message):<br>
Found unsuitable Qt version “5.9.7” from<br>
C:/Users/srolfe/Anaconda3/Library/bin/qmake.exe, this code requires Qt 4.x<br>
Call Stack (most recent call first):<br>
Common.cmake:28 (find_package)<br>
SuperBuild.cmake:12 (include)<br>
CMakeLists.txt:53 (include)</p>
</blockquote>
<p>which I resolved this by getting QT 4.8 and setting the QT_QMAKE_EXECUTABLE. This took care of the error, but I’m wondering if this issue is expected or if using the requested version of Qt might be causing a problem?</p>

---

## Post #31 by @jcfr (2022-12-23 14:08 UTC)

<p>To move forward:</p>
<ul>
<li>Make sure you download the source from <strong><code>NIRALUser/3DMetricTools</code></strong> and not from <code>juliettepera/3DMetricTools</code>. See [1]</li>
<li>Clear build directory</li>
<li>Attempt to configure setting <code>Slicer_DIR</code> first</li>
</ul>
<hr>
<p>[1]: To avoid confusion, we have been trying to reach out to the owner of the “root” fork without success. See <a href="https://github.com/NIRALUser/3DMetricTools/issues/10" class="inline-onebox">Re-fork repositories to avoid confusion · Issue #10 · NIRALUser/3DMetricTools · GitHub</a></p>

---

## Post #32 by @smrolfe (2022-12-23 18:42 UTC)

<p>I rebuilt from <strong><code>NIRALUser/3DMetricTools</code></strong>, set Slicer_DIR and Qt5_DIR before configuring, and its now building correctly.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I tested the fix in <a href="https://github.com/NIRALUser/3DMetricTools/pull/12" class="inline-onebox" rel="noopener nofollow ugc">ModelToModelDistance: Skip cleaning if corresponding_point_to_point mode is set by jcfr · Pull Request #12 · NIRALUser/3DMetricTools · GitHub</a> and it resolves the issue with the point count changing.</p>

---

## Post #33 by @jcfr (2022-12-23 18:55 UTC)

<p>Thanks for testing, changes have been integrated in <code>NIRALUser/3DMetricTools</code> and fixed extension <code>ModelToModelDistance</code> is expected to be published tomorrow for Slicer <code>5.2</code> and <code>Preview</code>.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> If you need the updated extension to be published before that, let me know and I can manually take care of it.</p>

---

## Post #34 by @smrolfe (2022-12-23 19:21 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>! Tomorrow works for me.</p>

---
