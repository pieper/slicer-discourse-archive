# Bump VTK minimum OpenGL version to 4.1

**Topic ID**: 35144
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/bump-vtk-minimum-opengl-version-to-4-1/35144

---

## Post #1 by @jspanchu (2024-03-27 22:37 UTC)

<p>Posting this in Slicer3D forum for better visibility. Please feel free to move it to appropriate category where it’s more visible.</p>
<p>We’re looking to update the minimum required OpenGL version in VTK from 3.2 to 4.1 for the desktop platforms. I’m cross posting here to gather feedback because Slicer3D uses VTK and also has a large community.</p>
<p>Since VTK uses a core profile context and asks for the highest available version of OpenGL from the OS, chances are you’re already using 4.6. Please let us know if your team requires VTK to support GPUs with OpenGL 4.0 or lower. We could look into the use case if needed and make necessary updates.</p>
<p>This backward compatibility is starting to hamper the introduction of newer robust rendering capabilities like tessellation shaders, compute shaders, etc. In the future, VTK will move over to WebGPU, however, that is a long term goal, best discussed in another post.</p>
<p>Here are some resources to get the general idea of systems supporting OpenGL 4.1</p>
<ol>
<li><a href="https://developer.apple.com/opengl/OpenGL-Capabilities-Tables.pdf" rel="noopener nofollow ugc">https://developer.apple.com/opengl/OpenGL-Capabilities-Tables.pdf </a> (pg 34 onwards)</li>
<li><a href="https://www.phoronix.com/news/Zink-OpenGL-4.1-Mesa-21.0" rel="noopener nofollow ugc">https://www.phoronix.com/news/Zink-OpenGL-4.1-Mesa-21.0 </a></li>
</ol>
<h2><a name="p-108795-rational-for-choosing-41-instead-of-a-newer-version-1" class="anchor" href="#p-108795-rational-for-choosing-41-instead-of-a-newer-version-1" aria-label="Heading link"></a>Rational for choosing <code>4.1</code> instead of a newer version:</h2>
<ul>
<li>macOS only supports up to 4.1</li>
<li>Mesa 12 onward support OpenGL 4.3 (Ubuntu 20.04 has mesa 21.2.6, Debian 10 has 18.3.6, many distributions considered ‘old’ have a mesa version &gt; 18.)</li>
</ul>
<p>For more details, see <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/19291" rel="noopener nofollow ugc">https://gitlab.kitware.com/vtk/vtk/-/issues/19291 </a></p>
<h2><a name="p-108795-how-you-can-help-us-2" class="anchor" href="#p-108795-how-you-can-help-us-2" aria-label="Heading link"></a>How you can help us?</h2>
<p>Please speak up in this post or over at <a href="https://discourse.vtk.org/t/survey-about-updating-minimum-opengl-version-to-4-1/13631?u=jaswantp" class="inline-onebox" rel="noopener nofollow ugc">Survey about updating minimum OpenGL version to 4.1 - Support - VTK</a> if you really need to support desktop OpenGL &lt; 4.1</p>
<p>In order to know the OpenGL version used by VTK, simply execute <code>vtkProbeOpenGLVersion</code> executable found in the <code>bin</code> folder of your VTK installation.</p>

---

## Post #2 by @lassoan (2024-03-27 22:57 UTC)

<p>Thanks for the heads-up! I don’t expect that this will cause an issue when Slicer is running on physical hardware that is not older than 5 years, but it might cause incompatibility issues in virtualized environments (virtualGL, VirtualBox, Parallels, etc.).</p>
<p>It would be difficult to test all environments where Slicer is used. If you want to ensure a smooth transition for every applications then you could do something like this:</p>
<ul>
<li>change VTK now to require OpenGL 4.1 by default</li>
<li>add a CMake flag that allows using VTK with just OpenGL 3.2 (it is OK to disable any new VTK features in this mode)</li>
<li>remove OpenGL 3.2 support in <strong>2 years</strong></li>
</ul>

---

## Post #3 by @jspanchu (2024-03-27 23:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but it might cause incompatibility issues in virtualized environments (virtualGL, VirtualBox, Parallels, etc.).</p>
</blockquote>
</aside>
<p>These can use mesa3d (on windows too <sup class="footnote-ref"><a href="#footnote-108802-1" id="footnote-ref-108802-1">[1]</a></sup>). It provides software implementation for OpenGL 4.1+</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>add a CMake flag that allows using VTK with just OpenGL 3.2 (it is OK to disable any new VTK features in this mode)</p>
</blockquote>
</aside>
<p>Yes, this  is possible. VTK can force the OpenGL context to 3.2 and it can be controlled with a compile-time setting. (also possible at runtime, just need a new Set/Get macro)</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-108802-1" class="footnote-item"><p><a href="https://discourse.paraview.org/t/how-to-run-paraview-including-the-binary-release-using-mesa-on-windows/4321" class="inline-onebox" rel="noopener nofollow ugc">How to run ParaView (including the binary release) using Mesa on Windows - Tips and Tricks - ParaView</a> <a href="#footnote-ref-108802-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #4 by @pieper (2024-03-27 23:28 UTC)

<p><a class="mention" href="/u/jspanchu">@jspanchu</a> thanks for posting this <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Can you suggest a test program (e.g. glxgears, blender, maybe a game or something) that people could run to see if this change will break something for them?  If there isn’t something already could we make one?  I don’t think most people know or care what OpenGL version they use unless it breaks.</p>

---

## Post #5 by @jspanchu (2024-03-27 23:49 UTC)

<p>There is one already. <code>vtkProbeOpenGLVersion</code> can be found inside <code>bin/</code> directory of a VTK installation. When you run it, it will print lots of information or show a dialog on windows. So look for this line:</p>
<pre><code class="lang-auto">OpenGL version string:  4.5 (Core Profile) Mesa 24.0.1-arch1.1
</code></pre>
<p>This works too:</p>
<pre data-code-wrap="python"><code class="lang-python">import vtk

renderer = vtk.vtkRenderer()
renderWindow  = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.Render()
print(renderWindow.ReportCapabilities())
</code></pre>
<p>In C++, you can also use</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">vtkNew&lt;vtkRenderer&gt; renderer;
vtkNew&lt;vtkRenderWindow&gt; renderWindow;
renderWindow-&gt;AddRenderer(renderer);
renderWindow-&gt;Render()
int major, minor;
renderWindow-&gt;GetOpenGLVersion(major, minor);
std::cout &lt;&lt; "OpenGL version" &lt;&lt; major &lt;&lt; '.' &lt;&lt; minor &lt;&lt; '\n'
</code></pre>

---

## Post #6 by @pieper (2024-03-28 12:36 UTC)

<p>Thanks <a class="mention" href="/u/jspanchu">@jspanchu</a> - just trying to make sure this is clear for people who aren’t in the weeds of OpenGL.</p>
<p>So if I run the python script you provided in Slicer 5.6.1 my mac pro, I get the following, which is consistent with the expectation that 4.1 should be supported.</p>
<pre><code class="lang-auto">...
OpenGL version string:  4.1 ATI-4.12.7
... 
</code></pre>
<p>So what we need is for people to check this out and report back if they see a version string less than 4.1.  It’s possible this might happen with older machines, virtualized environments, or specific remote desktop systems.</p>
<p>it will be helpful to know if those systems exist, but it may also be the case that we move ahead anyway and just let people know that they may need to use older Slicer/VTK versions with those systems.</p>

---

## Post #7 by @lassoan (2024-03-28 12:57 UTC)

<aside class="quote no-group" data-username="jspanchu" data-post="3" data-topic="35144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jspanchu/48/69787_2.png" class="avatar"> jspanchu:</div>
<blockquote>
<p>Yes, this is possible. VTK can force the OpenGL context to 3.2 and it can be controlled with a compile-time setting. (also possible at runtime, just need a new Set/Get macro)</p>
</blockquote>
</aside>
<p>Could you set up a build with this 3.2 option enabled so that you know what is broken - and if it is not too much trouble then keep most things working with OpenGL 3.2 for a transition period of 2 years? I would expect that most incompatibilities will be introduced accidentally and should be easy to avoid (maybe by adding a few <span class="hashtag-raw">#ifdefs</span>, which can be all wiped out once the transition period is over).</p>

---
