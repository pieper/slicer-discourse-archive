# General questions about Microscopy image processing and & visualization using 3D Slicer

**Topic ID**: 10527
**Date**: 2020-03-03
**URL**: https://discourse.slicer.org/t/general-questions-about-microscopy-image-processing-and-visualization-using-3d-slicer/10527

---

## Post #1 by @zwei2001 (2020-03-03 18:19 UTC)

<p>I’d like to know following if 3D Slcier has following features. Thanks for anyone who helps</p>
<p>GPU for Image Processing?<br>
Multithread?<br>
Well-documented?<br>
Stereo image pairs?<br>
Surface rendering?<br>
Shadowing casting?<br>
VR?<br>
Movie recording<br>
Ortho slices/block face views<br>
Volume xyz/arbitrary cropping<br>
channel specific cropping<br>
Annotation on volume<br>
Mesh display support<br>
Channel specific LUT adjustments<br>
Channel specific opacity<br>
4D Movie Support (xyzt)<br>
3D ROI measurements<br>
Create 3D ROIs based on data<br>
Interactive 3D length, angle measurements<br>
3D particle tracking<br>
Multi-modal/multi-channel 3D co-registration<br>
Can handle datasets larger than RAM capacity?<br>
Can run on a computer cluster?<br>
what Built-in sripting / macro language used?<br>
Size of existing user base?<br>
User forum / online discussion board help<br>
User plugins allowed?<br>
Built-in scripting / macro languages?</p>

---

## Post #2 by @pieper (2020-03-03 18:33 UTC)

<p>Whew, that’s a lot of questions!  Generally Slicer does really well on all those topics.<br>
Maybe you can start by reading some of these references: <a href="https://www.slicer.org/wiki/CitingSlicer">https://www.slicer.org/wiki/CitingSlicer</a></p>

---

## Post #3 by @fedorov (2020-03-03 18:40 UTC)

<p>I agree with <a class="mention" href="/u/pieper">@pieper</a> - some of those questions are trivial (e.g., you should now know the answer to “User forum / online discussion board help” :-D).</p>
<p>Maybe you can start by reviewing the documentation, and summarize your understanding here in this thread, and then have it reviewed by the community, so we can correct as needed?</p>

---

## Post #5 by @lassoan (2020-03-03 19:44 UTC)

<p>The answer to most questions is a strong yes. There are a few areas for improvement:</p>
<ul>
<li>multi-channel image display/processing is supported in the internal infrastructure but not much of it is exposed on the GUI</li>
<li>out-of-core/multi-resolution image visualization and processing is not direclty supported (there are many application-specific workarounds)</li>
<li>microscopy file format readers/writers are supported by ITK quite well, but they are not enabled in default builds</li>
<li>custom length unit can be specified (e.g., use nm instead of mm as base unit) but not very well tested, so probably some fixes will be needed if it will be widely used</li>
</ul>
<p>Several of these improvements would be relatively easy to do (even without touching the Slicer core, in custom modules), since Slicer relies on very flexible and powerful libraries, such as VTK and ITK, and you can also import and use <em>any</em> Python packages within Slicer.</p>
<p>Detailed response:</p>
<p>GPU for Image Processing? - We rely on ITK and VTK for most image processing operations and still only a very few processing filters are GPU-accelerated. For performance-critical steps, you can easily install any Python-wrapped GPU-accelerated processing filters from the Python package index and/or add your own (can be implemented in C++ and Python, preferably using GLSL or OpenCL).</p>
<p>Multithread? - Most performance-critical processing filters are multi-threaded.</p>
<p>Well-documented? - Yes. Lots of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training">tutorials</a>, <a href="https://www.slicer.org/wiki/Documentation/Nightly">user guide</a>, <a href="https://apidocs.slicer.org/master/annotated.html">API documentation</a>, training events, very responsive forum.</p>
<p>Stereo image pairs? - Yes. Full <a href="https://github.com/KitwareMedical/SlicerVirtualReality">immersive virtual reality display</a> of anything that is shown in 3D views. Can be activated by a single click. Legacy anaglyph, interlaced, etc. stereo visualization is supported as well, but these have become irrelevant since virtual reality has become widely accessible.</p>
<p>Surface rendering? Yes. With many options.</p>
<p>Shadowing casting? Slicer uses VTK for rendering, which supports it, so probably it could be enabled (maybe by typing a few lines of Python code), but it is not available from the GUI.</p>
<p>VR? - <a href="https://github.com/KitwareMedical/SlicerVirtualReality">Yes</a>.</p>
<p>Movie recording - <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ScreenCapture">Yes</a></p>
<p>Ortho slices/block face views - Yes, with lots of visualization options.</p>
<p>Volume xyz/arbitrary cropping - Yes.</p>
<p>channel specific cropping - I’m not sure what you mean by this, but you can crop, clip, and mask multi-channel images.</p>
<p>Annotation on volume - Yes. You can mark points, lines, curves, etc. on rendered volumes in 2D and 3D.</p>
<p>Mesh display support - Yes. Both surface and volumetric, including coloring by cell and point scalars, slice intersection/projection views, etc.</p>
<p>Channel specific LUT adjustments<br>
Channel specific opacity - Currently, multi-channel image support is quite limited. It would be easy to improve this, as all the underlying infrastructure supports them, but there has not been strong interest in this so far. Adding a module for customizing LUT/opacity for individual channels would be probably take a few days of work.</p>
<p>4D Movie Support (xyzt) - Yes, full support of time sequences of all data types (volumes, meshes, point sets, curves, etc.)</p>
<p>3D ROI measurements - Yes. Lots of metrics.</p>
<p>Create 3D ROIs based on data - Yes. Slicer has the most sophisticated image segmentation tool among all open-source medical image computing software (and it is more powerful than most commercial software, too).</p>
<p>Interactive 3D length, angle measurements - Yes.</p>
<p>3D particle tracking - Yes. <a href="https://github.com/moselhy/SlicerSequenceRegistration">Sequence registration</a> allows tracking of position and deformation of 3D objects in a 3D+t volume sequence.</p>
<p>Multi-modal/multi-channel 3D co-registration - Multi-modal, yes. Multi-channel, I’m not completely sure, but probably yes (via SlicerElastiX).</p>
<p>Can handle datasets larger than RAM capacity? - There is no specific support for out-of-core processing. There are Python-based tools that can be imported and used, and there are many tricks for handling of very large data sets.</p>
<p>Can run on a computer cluster? Yes.</p>
<p>what Built-in sripting / macro language used? Yes, full interactive and batch mode Python scripting. Any python3 packages can be installed directly from the Python package index.</p>
<p>Size of existing user base? About 3000 weekly <a href="https://download.slicer.org/download-stats/">downloads</a> from everywhere around the world (increasing exponentially by about 30% in the last 5 years)</p>
<p>User forum / online discussion board help - Yes. See this forum, with over 3200 members. All questions are answered. Several in-person meetings a year (<a href="https://projectweek.na-mic.org/">Slicer Project Weeks</a>).</p>
<p>User plugins allowed? - Yes. Designed to be customizable and extensible. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">tutorials</a>.</p>
<p>Built-in scripting / macro languages? Yes. See above.</p>

---

## Post #6 by @zwei2001 (2020-03-03 20:21 UTC)

<p>Thank you very much Andras, very instructive and helpful!</p>

---

## Post #7 by @zwei2001 (2020-03-03 21:43 UTC)

<p>Is the source code open to public?</p>

---

## Post #8 by @muratmaga (2020-03-03 21:59 UTC)

<p>You really need to go do <a href="http://www.slicer.org" rel="nofollow noopener">http://www.slicer.org</a> and learn about it yourself.</p>

---
