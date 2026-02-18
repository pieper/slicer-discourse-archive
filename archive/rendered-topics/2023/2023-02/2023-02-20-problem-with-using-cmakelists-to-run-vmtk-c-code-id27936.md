# Problem with using 【CMakeLists】 to run 【VMTK c++】 code

**Topic ID**: 27936
**Date**: 2023-02-20
**URL**: https://discourse.slicer.org/t/problem-with-using-cmakelists-to-run-vmtk-c-code/27936

---

## Post #1 by @tigerhu7 (2023-02-20 16:10 UTC)

<p>Dear All,<br>
In my project, I am to run a VMTK c++ code using CMake. My setup are<br>
【linux mint】+ 【gcc】+【visual studio code】+【cmake】, and first serveral lines of code are at the very bottom:<br>
The problem I have is with CMakeLists.txt. To run the code, here are three ways I have tried:<br>
【1】 I download the vmtk source code and build with CMake, and tree structure is as this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32665e11b77c215fa062a94b296e6b9220f531a3.png" alt="Screenshot from 2023-02-20 22-12-04" data-base62-sha1="7bRc4LL8LVWilE2WBpX9BzAdMYz" width="231" height="488"><br>
where include/vmtk and include/vtk-9.1 contain header files, and install/lib contains all the shared libs.</p>
<p>and CMakeLists.txt is as this</p>
<blockquote>
<p>Blockquote<br>
cmake_minimum_required(VERSION 3.0.0)<br>
project(VMTK_TOY VERSION 0.1.0)<br>
include(CTest)<br>
enable_testing()<br>
set(CPACK_PROJECT_NAME ${PROJECT_NAME})<br>
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})<br>
include(CPack)<br>
#<em><strong>/executable</strong></em>/<br>
add_executable(${PROJECT_NAME} main.cpp)<br>
#<em><strong>/headerfiles</strong></em>/<br>
target_include_directories( ${PROJECT_NAME} PRIVATE  XXX/vmtk-build/Install/include/vtk-9.1)<br>
target_include_directories( ${PROJECT_NAME} PRIVATE XXX/vmtk-build/Install/include/vmtk )<br>
#<em><strong>/vmtk shared libs</strong></em>/<br>
set(  VMTK_DIR “XXX/vmtk-build/Install/lib” )<br>
target_link_libraries(${PROJECT_NAME} PRIVATE<br>
${VMTK_DIR}/libvtkvmtkCommon.so<br>
${VMTK_DIR}/libvtkvmtkComputationalGeometry.so<br>
${VMTK_DIR}/libvtkvmtkContrib.so<br>
${VMTK_DIR}/libvtkvmtkDifferentialGeometry.so<br>
${VMTK_DIR}/libvtkvmtkIO.so<br>
${VMTK_DIR}/libvtkvmtkITK.so<br>
${VMTK_DIR}/libvtkvmtkMisc.so<br>
${VMTK_DIR}/libvtkvmtkRendering.so<br>
${VMTK_DIR}/libvtkvmtkSegmentation.so)<br>
#<em><strong>/vtk shared libs</strong></em>/<br>
find_package(VTK<br>
COMPONENTS<br>
CommonCore<br>
CommonDataModel<br>
CommonTransforms<br>
FiltersCore<br>
FiltersGeneral<br>
FiltersGeometry<br>
FiltersModeling<br>
IOImage<br>
IOXML<br>
ImagingCore<br>
ImagingStatistics<br>
InteractionStyle<br>
RenderingCore<br>
RenderingVolume<br>
RenderingOpenGL2<br>
RenderingVolumeOpenGL2<br>
OPTIONAL_COMPONENTS<br>
TestingCore<br>
TestingRendering)<br>
target_link_libraries(${PROJECT_NAME} PRIVATE ${VTK_LIBRARIES})</p>
</blockquote>
<p>then i got error like this.<br>
collect2: error: ld returned 1 exit status</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20bf7dedda2941fb0894f0b9eb5d694cf28d081b.png" data-download-href="/uploads/short-url/4FHy0K887JcRVhaHcGeIAF6UrxN.png?dl=1" title="Screenshot from 2023-02-20 23-35-30-mod" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20bf7dedda2941fb0894f0b9eb5d694cf28d081b_2_690x132.png" alt="Screenshot from 2023-02-20 23-35-30-mod" data-base62-sha1="4FHy0K887JcRVhaHcGeIAF6UrxN" width="690" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20bf7dedda2941fb0894f0b9eb5d694cf28d081b_2_690x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20bf7dedda2941fb0894f0b9eb5d694cf28d081b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20bf7dedda2941fb0894f0b9eb5d694cf28d081b.png 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-02-20 23-35-30-mod</span><span class="informations">961×184 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>vtk shared libs part on this CMakelist.txt are copy and past from cmakelists.txt of a vtk example.<br>
Then I realized that, this way, cmake might have linked to my other vtk-build (Which I have built years earlier, and stored at /usr/local/lib)<br>
So I tried to link every single .so or .so.* files directly<br>
【2】</p>
<blockquote>
<p>Blockquote<br>
cmake_minimum_required(VERSION 3.0.0)<br>
project(VMTK_TOY VERSION 0.1.0)<br>
include(CTest)<br>
enable_testing()<br>
set(CPACK_PROJECT_NAME ${PROJECT_NAME})<br>
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})<br>
include(CPack)<br>
add_executable(${PROJECT_NAME} main.cpp)<br>
target_include_directories( ${PROJECT_NAME} PRIVATE  XXX/vmtk-build/Install/include/vtk-9.1)<br>
target_include_directories( ${PROJECT_NAME} PRIVATE XXX/vmtk-build/Install/include/vmtk )<br>
target_link_directories( ${PROJECT_NAME} PRIVATE<br>
XXX/vmtk-build/Install/lib/libITKBiasCorrection-5.2.so<br>
XXX/vmtk-build/Install/lib/libITKBiasCorrection-5.2.so.1<br>
XXX/vmtk-build/Install/lib/libITKColormap-5.2.so<br>
…<br>
)</p>
</blockquote>
<p>basically, in target_link_directories, I listed every sinlge  .so or .so.* files, in the directory<br>
XXX/vmtk-build/install/lib</p>
<p>still, I got error like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af93c357068cf00c360dc34f1fb5efea8b8166e6.png" data-download-href="/uploads/short-url/p3e8zdYlogN3W7WKqbMxwwz2loy.png?dl=1" title="Screenshot from 2023-02-20 23-48-04-mod" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af93c357068cf00c360dc34f1fb5efea8b8166e6_2_690x180.png" alt="Screenshot from 2023-02-20 23-48-04-mod" data-base62-sha1="p3e8zdYlogN3W7WKqbMxwwz2loy" width="690" height="180" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af93c357068cf00c360dc34f1fb5efea8b8166e6_2_690x180.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af93c357068cf00c360dc34f1fb5efea8b8166e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af93c357068cf00c360dc34f1fb5efea8b8166e6.png 2x" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-02-20 23-48-04-mod</span><span class="informations">969×254 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In fear of vmtk that I built may have flaws,  I tried to install vmtk through anaconda<br>
【3】<br>
under</p>
<blockquote>
<p>Blockquote<br>
XXX/anaconda3/pkg</p>
</blockquote>
<p>there are vmtk-1.4.0-py36**** and vtk-8.10-py36*** folders,  both are like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8ddb0e826c8e3654db3b505d06c86baac5e45e8.png" alt="Screenshot from 2023-02-20 23-54-37" data-base62-sha1="xe1K7YRrQNecAPJQpqlhNvIjU48" width="614" height="110"><br>
so I changed target_link_directories and target_include_directories in method【2】(without the rest changed)<br>
to</p>
<blockquote>
<p>Blockquote<br>
target_include_directories( ${PROJECT_NAME} PRIVATE  XXX/anaconda3/pkg/vtk-8.1.0-py36***/include/vtk-8.1)<br>
target_include_directories( ${PROJECT_NAME} PRIVATE XXX/anaconda3/pkg/vmtk/include/vmtk )<br>
target_link_directories( ${PROJECT_NAME} PRIVATE<br>
XXX/anaconda3/pkg/vtk-8.1.0-py36***/lib/libITKBiasCorrection-5.2.so<br>
XXX/anaconda3/pkg/vtk-8.1.0-py36***/lib/libITKBiasCorrection-5.2.so.1<br>
XXX/anaconda3/pkg/vtk-8.1.0-py36***/lib/libITKColormap-5.2.so<br>
…<br>
)</p>
</blockquote>
<p>and get the same error as 【1】<br>
I have double checked every single path, and there is no typo on the paths.<br>
So I doubt, the shared libs are still not linked in cmakelists.txt</p>
<p>On Windows 10, I tried this code using Visual Studio,  it include headers and link .dll successfully, and the code runs well. Yet, I did not try running this code using CMake on Windows.</p>
<p>I researched on this issue for the whole weekend, but could not get a solution.<br>
Please help me if you have any ideas or suggestions.<br>
Thanks in advance!!!</p>
<p>Here is the c++ code.</p>
<blockquote>
<p>Blockquote<br>
<span class="hashtag-raw">#include</span> &lt;vtkAutoInit.h&gt;<br>
VTK_MODULE_INIT(vtkRenderingOpenGL2);<br>
VTK_MODULE_INIT(vtkInteractionStyle);<br>
<span class="hashtag-raw">#include</span> &lt;vtkSmartPointer.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkRenderWindow.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkRenderer.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkPolyDataMapper.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkActor.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkJPEGReader.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkCamera.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkProperty.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkAxesActor.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkSTLReader.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkDiscreteMarchingCubes.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkWindowedSincPolyDataFilter.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkCleanPolyData.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkTriangleFilter.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkPolyData.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkPointData.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkDataArray.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkIdList.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkDecimatePro.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkDoubleArray.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkParametricSpline.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkParametricFunctionSource.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkLODActor.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkInteractorStyleTrackballCamera.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkRenderWindowInteractor.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkvmtkCapPolyData.h&gt;<br>
<span class="hashtag-raw">#include</span> &lt;vtkvmtkPolyDataCenterlines.h&gt;<br>
#include&lt;vtkSTLWriter.h&gt;<br>
#include&lt;vtkConeSource.h&gt;<br>
<span class="hashtag-raw">#include</span> <br>
<span class="hashtag-raw">#include</span> <br>
using namespace std;<br>
int main()<br>
{<br>
string stl = “rightlumen.stl”;<br>
vtkSmartPointer reader = vtkSmartPointer::New();<br>
reader-&gt;SetFileName(stl.c_str());<br>
reader-&gt;Update();<br>
vtkSmartPointer data = vtkSmartPointer::New();<br>
data-&gt;DeepCopy(reader-&gt;GetOutput());<br>
return 0;<br>
}</p>
</blockquote>

---

## Post #2 by @RafaelPalomar (2023-02-21 09:36 UTC)

<p>Hello <a class="mention" href="/u/tigerhu7">@tigerhu7</a>. As I see the problem it seems that VMTK configuration files do not account for the ITK and VTK used in the superbuild process. I have opened an issue (<a href="https://github.com/vmtk/vmtk/issues/448" class="inline-onebox" rel="noopener nofollow ugc">Using VMTK build tree for development · Issue #448 · vmtk/vmtk · GitHub</a>) and a PR (<a href="https://github.com/vmtk/vmtk/pull/449" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add ITK and VTK to buildtree VMTKConfig.cmake by RafaelPalomar · Pull Request #449 · vmtk/vmtk · GitHub</a>). It woudl be nice if <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> or <a class="mention" href="/u/jcfr">@jcfr</a> could comment on whether this is an appropriate way to solve the issue.</p>
<p>Using that PR (you can pull it yourself and test it) I was able to build the following project, which was based on your question:</p>
<pre><code class="lang-auto"> # CMake project definition
cmake_minimum_required(VERSION 3.0.0)
project(VMTK_TOY VERSION 0.1.0)

find_package(VMTK REQUIRED)
include(${VMTK_USE_FILE})

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} PRIVATE ${VTK_LIBRARIES})
</code></pre>
<pre data-code-wrap="c++"><code class="lang-plaintext">// main.cpp file
#include &lt;vtkSmartPointer.h&gt;
#include &lt;vtkRenderWindow.h&gt;
#include &lt;vtkRenderer.h&gt;
#include &lt;vtkPolyDataMapper.h&gt;
#include &lt;vtkActor.h&gt;
#include &lt;vtkJPEGReader.h&gt;
#include &lt;vtkCamera.h&gt;
#include &lt;vtkProperty.h&gt;
#include &lt;vtkAxesActor.h&gt;
#include &lt;vtkSTLReader.h&gt;
#include &lt;vtkDiscreteMarchingCubes.h&gt;
#include &lt;vtkWindowedSincPolyDataFilter.h&gt;
#include &lt;vtkCleanPolyData.h&gt;
#include &lt;vtkTriangleFilter.h&gt;
#include &lt;vtkPolyData.h&gt;
#include &lt;vtkPointData.h&gt;
#include &lt;vtkDataArray.h&gt;
#include &lt;vtkIdList.h&gt;
#include &lt;vtkDecimatePro.h&gt;
#include &lt;vtkDoubleArray.h&gt;
#include &lt;vtkParametricSpline.h&gt;
#include &lt;vtkParametricFunctionSource.h&gt;
#include &lt;vtkLODActor.h&gt;
#include &lt;vtkInteractorStyleTrackballCamera.h&gt;
#include &lt;vtkRenderWindowInteractor.h&gt;
#include &lt;vtkvmtkCapPolyData.h&gt;
#include &lt;vtkvmtkPolyDataCenterlines.h&gt;
#include&lt;vtkSTLWriter.h&gt;
#include&lt;vtkConeSource.h&gt;
using namespace std;
int main()
{
  string stl = "rightlumen.stl";
  auto reader = vtkSmartPointer&lt;vtkSTLReader&gt;::New();
  reader-&gt;SetFileName(stl.c_str());
  reader-&gt;Update();
  return 0;
}
</code></pre>
<p>Your sample project did not include any of the VMTK components, though, so you should try with a more complete project.</p>
<p>I hope this helps.</p>

---

## Post #3 by @tigerhu7 (2023-02-21 13:12 UTC)

<p>Dear <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> ,<br>
Thank you for your kind reply!!!<br>
I figured it out just a moment ago. Yes, it is the problem with VTK configuration. Here is what I have done:<br>
[1] rebuilt vmtk<br>
[2] rewrite CMakeLists.txt as</p>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 3.0.0)
project(VMTK_TOY VERSION 0.1.0)
include(CTest)
enable_testing()
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
set(VTK_DIR "XXX/vmtk-superbuild/VTK-Build")

# find vtk
find_package(VTK
  COMPONENTS
    CommonCore
    CommonDataModel
    CommonTransforms
    FiltersCore
    FiltersGeneral
    FiltersGeometry
    FiltersModeling
    IOImage
    IOXML
    ImagingCore
    ImagingStatistics
    InteractionStyle
    RenderingCore
    RenderingVolume
    RenderingOpenGL2
    RenderingVolumeOpenGL2
  OPTIONAL_COMPONENTS
    TestingCore
    TestingRendering)

# header files
include_directories(
"XXX/vmtk-superbuild/Install/include/vtk-9.1" 
"XXX/vmtk-superbuild/Install/include/vmtk" 
)

# executable
add_executable(${PROJECT_NAME} main.cpp)

# shared files
target_link_libraries(VMTK_TOY
XXX/vmtk-superbuild/Install/lib/*.so*
(i.e. every *.so* files)
}
</code></pre>
<p>The difference part of my CMakeLists.txt is that I wrote directories explicitly.<br>
I will try your method, too.<br>
Thanks again for your kind help!!</p>

---

## Post #4 by @tigerhu7 (2023-02-22 11:33 UTC)

<p>Dear <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a><br>
I have tested your CMakeLists.txt file, unfortunately it did not work for me.<br>
If I use yours, I got this error</p>
<pre><code class="lang-auto"> fatal error: vtkAutoInit.h: No such file or directory
[build]     3 | #include &lt;vtkAutoInit.h&gt;
[build]       |          ^~~~~~~~~~~~~~~
[build] compilation terminated.

</code></pre>
<p>It seems the header file is not included.<br>
Then I have modified your CMakeLists.txt in several ways, the best I have right now like this</p>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 3.0.0)
project(VMTK_TOY VERSION 0.1.0)
set(VMTK_DIR "XXX/ThirdParties/vmtk-superbuild/VMTK-Build")
set(VTK_DIR "XXX/ThirdParties/vmtk-superbuild/VTK-Build")

find_package(VTK REQUIRED CONFIG PATHS "XXX/ThirdParties/vmtk-superbuild/VTK-Build" NO_DEFAULT_PATH)
find_package(VMTK REQUIRED  PATHS "XXX/ThirdParties/vmtk-superbuild/VMTK-Build" NO_DEFAULT_PATH)

message(STATUS, "VTK DIR = ${VTK_DIR}")
message(STATUS, "VMTK DIR = ${VMTK_DIR}")
include(${VMTK_USE_FILE} ${VTK_USE_FILE})
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE ${VTK_LIBRARIES} )
target_link_libraries(${PROJECT_NAME} PRIVATE ${VMTK_LIBRARIES} )
</code></pre>
<p>Still it says this error.</p>
<pre><code class="lang-auto">[build] Consolidate compiler generated dependencies of target VMTK_TOY
[build] [ 50%] Linking CXX executable VMTK_TOY
[build] /usr/bin/ld: cannot find -litkdouble-conversion
[build] /usr/bin/ld: cannot find -lITKInternalEigen3::Eigen
.....
</code></pre>
<p>I am new to CMake language and did research for only a few days. I might have to learn it more.<br>
Thanks,</p>

---

## Post #5 by @RafaelPalomar (2023-02-22 12:58 UTC)

<aside class="quote no-group" data-username="tigerhu7" data-post="4" data-topic="27936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tigerhu7/48/67201_2.png" class="avatar"> tigerhu7:</div>
<blockquote>
<p>I have tested your CMakeLists.txt file, unfortunately it did not work for me.<br>
If I use yours, I got this error</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/tigerhu7">@tigerhu7</a>, that <code>CMakeLists.txt</code> file is meant to be used with the VMTK changes in <a href="https://github.com/vmtk/vmtk/pull/449" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add ITK and VTK to buildtree VMTKConfig.cmake by RafaelPalomar · Pull Request #449 · vmtk/vmtk · GitHub</a>. In these changes I propose to include the ITK and VTK in the <code>VMTKConfig.cmake</code> file, so when you import VMTK through</p>
<pre><code class="lang-auto">find_package(VMTK REQUIRED)
include(${VMTK_USE_FILE})
</code></pre>
<p>you are also importing ITK and VTK.</p>

---
