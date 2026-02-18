# Installing ITK Python package in Slicer 5.1 and above

**Topic ID**: 25636
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/installing-itk-python-package-in-slicer-5-1-and-above/25636

---

## Post #1 by @jcfr (2022-10-11 05:12 UTC)

<p>Following the integration of Slicer pull request <a href="https://github.com/Slicer/Slicer/pull/6564">#6564</a> adding support for ITK custom namespace, it is now possible to install ITK python package from PyPI and use associated filter.</p>
<p>The use of functionalities relying on either ITK C++ (e.g Slicer CLIs, vtkITK library, …) or the SimpleITK python package built within Slicer have been tested and are expected to work on macOS/Linux/Windows.</p>
<h3><a name="p-84384-known-issues-1" class="anchor" href="#p-84384-known-issues-1" aria-label="Heading link"></a>Known Issues</h3>
<ul>
<li>ITK pre-release  ( <code>itk 5.3rc4.post3</code> or newer) should be used</li>
<li>The use of macOS ITK python wheels is broken and issue is been discussed at <a href="https://discourse.itk.org/t/itk-5-3rc4-post3-failure-to-load-libtbb-library-observed-on-macos-10-13/5405" class="inline-onebox">itk 5.3rc4.post3: Failure to load libtbb library (observed on macOS 10.13) - Engineering - ITK</a></li>
</ul>
<h3><a name="p-84384-installing-the-itk-package-2" class="anchor" href="#p-84384-installing-the-itk-package-2" aria-label="Heading link"></a>Installing the ITK Package</h3>
<p>You may install the ITK python wheels using</p>
<pre><code class="lang-auto">slicer.util.pip_install(["--pre", "itk==5.3rc4.post3"])
</code></pre>
<p><em>Alternatively, the instructions posted <a href="https://github.com/Slicer/Slicer/pull/6564#issue-1396422082">here</a> allows to install the wheels in a dedicated directory. This more elaborated approach may be useful to avoid “polluting” the <code>site-packages</code> directory found in your installation of Slicer.</em></p>
<h3><a name="p-84384-example-applying-itk-filter-to-mrml-volume-node-3" class="anchor" href="#p-84384-example-applying-itk-filter-to-mrml-volume-node-3" aria-label="Heading link"></a>Example: Applying ITK filter to MRML Volume node</h3>
<p>The following example demonstrates how to apply an ITK filter to a MRML volume node:</p>
<pre data-code-wrap="python"><code class="lang-python">def updateMatrix3x3From4x4(matrix3x3, matrix4x4):
  for i_idx in range(3):
    for j_idx in range(3):
      matrix3x3.SetElement(i_idx, j_idx, matrix4x4.GetElement(i_idx, j_idx))

# Input node
import SampleData
input_volume_node = SampleData.SampleDataLogic().downloadMRHead()

# (1) Create VTK image data with expected metadata
input_vtk_image = vtk.vtkImageData()
input_vtk_image.ShallowCopy(input_volume_node.GetImageData())
input_vtk_image.SetOrigin(input_volume_node.GetOrigin())
input_vtk_image.SetSpacing(input_volume_node.GetSpacing())

directionMatrix4x4 = vtk.vtkMatrix4x4()
input_volume_node.GetIJKToRASDirectionMatrix(directionMatrix4x4)
directionMatrix3x3 = vtk.vtkMatrix3x3()
updateMatrix3x3From4x4(directionMatrix3x3, directionMatrix4x4)
input_vtk_image.SetDirectionMatrix(directionMatrix3x3)

# (2) Create ITK image data from VTK image data
import itk
input_itk_image = itk.image_from_vtk_image(input_vtk_image)

# (3) Filter ITK image
output_itk_image = itk.discrete_gaussian_image_filter(input_itk_image, variance=5.0)

# (4) Create output node
output_volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "MRHead-Filtered")

# (5) Apply ITK filtering
vtk_output_image = itk.vtk_image_from_image(output_itk_image)

# (6) Update output node using on VTK output image spacing/origin/direction
ijkToRASMatrix = vtk.vtkMatrix4x4()
import vtkAddon
vtkAddon.vtkAddonMathUtilities.SetOrientationMatrix(vtk_output_image.GetDirectionMatrix(), ijkToRASMatrix)
output_volume_node.SetIJKToRASMatrix(ijkToRASMatrix)
output_volume_node.SetOrigin(*vtk_output_image.GetOrigin())
output_volume_node.SetSpacing(*vtk_output_image.GetSpacing())

# (7) Reset spacing/origin/direction from VTK output image
vtk_output_image.SetOrigin((0, 0, 0))
vtk_output_image.SetSpacing((1., 1., 1.))
identidyMatrix = vtk.vtkMatrix3x3()
vtk_output_image.SetDirectionMatrix(identidyMatrix)

# (8) Update output node setting VTK image data
output_volume_node.SetAndObserveImageData(vtk_output_image)
</code></pre>
<h3><a name="p-84384-related-posts-4" class="anchor" href="#p-84384-related-posts-4" aria-label="Heading link"></a>Related posts</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/how-to-install-itk-python-wheels-with-slicer-4-10-and-slicer-4-11/12537" class="inline-onebox">How to install ITK python wheels with Slicer 4.10 and Slicer 4.11?</a></li>
</ul>
<p>cc: <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/pranjal.sahu">@pranjal.sahu</a> <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #2 by @smrolfe (2022-10-11 17:30 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>, this is very exciting news! I think there may be a small typo above, to install I needed to change</p>
<aside class="quote no-group quote-modified" data-username="jcfr" data-post="1" data-topic="25636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><code>slicer.util.pip_install(["--pre", "itk==itk 5.3rc4.post3"])</code></p>
</blockquote>
</aside>
<p>to</p>
<pre><code class="lang-auto">slicer.util.pip_install(["--pre", "itk==5.3rc4.post3"])
</code></pre>

---

## Post #3 by @jcfr (2022-10-11 17:59 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="25636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>there may be a small typo above</p>
</blockquote>
</aside>
<p>Good catch <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> I edited the original post accordingly.</p>

---
