# Showing totally different content in different views

**Topic ID**: 1342
**Date**: 2017-11-01
**URL**: https://discourse.slicer.org/t/showing-totally-different-content-in-different-views/1342

---

## Post #1 by @jdx-john (2017-11-01 12:07 UTC)

<p>As a newbie to Slicer Dev, I’m interested how view content is managed. We’re interested in having several standard views showing DICOM data but one view showing only some 3D models and other non-DICOM content.<br>
Behind the scenes(!) how are different datasets and objects organised - at a high technical level?</p>
<p>We’re already working with <a class="mention" href="/u/lassoan">@lassoan</a> but it’s nice to have discussions in the public forums I think. Sorry if I’m clearly showing my ignorance here!</p>

---

## Post #2 by @pieper (2017-11-01 13:09 UTC)

<p>Hi John -</p>
<p>Welcome - we hope you find Slicer a good environment for your work - it’s powerful but it can be hard to learn all the features.  Questions here are always welcome.</p>
<p>Regarding how data is organized, let me try a high level view and we can dig in the details as needed.</p>
<p>First, the MRML scene contains all the state that is saved and restored in a scene (e.g. a .mrb file, which under the hood is a .zip of all the serialized content and an xml-formatted .mrml scene file).  The MRML scene consists of nodes, some of which are subclasses of <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html">vtkMRMLDisplayableNode</a>, meaning they are meant to show up in a viewer.  Each viewer has a unique ID (like ‘Red’ for the red slice view).</p>
<p>We have the concept of a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DisplayableManagers">DisplaybleManager</a> which is responsible for mapping the data content of the DisplayableNodes to vtkActors/Mappers in particular Renderers (also mapping back from vtk widgets to changes in the nodes, e.g. for fiducials).</p>
<p>Each DisplayableNode has a list of <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html">DisplayNodes</a> that hold the properties like color, transparency, etc.  Each DisplayNode has a list of <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a447f6ce8ece781ccf15549a6176745db">ViewNodeIDs</a> which can be used to tell the DisplayableManager whether or not to show a particular DisplayableNode with a particuar set of DisplayNode properties.</p>
<p>This allows you to have, for example, one slice view with model outlines and another slice view with fiducial points.  Or you can have a 3D view with volume rendering and another with surface models (or mix and match).</p>
<p>(Note there’s also a slightly different mechanism for handling foreground/background slice compositing in the slice views that relies on similar mechanisms).</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @cpinter (2017-11-01 13:25 UTC)

<p>I’d like to add that the slice views’ content is easiest to manage using the slice composite nodes. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L351-L368">This is an example</a> where all slices are set to show the same thing, but the idea is the same if you want to show different things, except that you need to get the slice composite node for the particular viewer using the slice widgets, <a href="https://github.com/SlicerRt/FilmDosimetryAnalysis/blob/master/FilmDosimetryAnalysis/FilmDosimetryAnalysis.py#L1465-L1473">like this</a>.</p>
<p>3D visibility can be set as Steve described: turning on visibility for the display nodes, with the option to specify the actual view, <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLDisplayNodeViewComboBox.cxx#L175">like this</a>.</p>

---

## Post #4 by @Fokatu (2023-12-16 11:09 UTC)

<p>Are there any examples explaining this?<br>
What should I do if I want to show one 2D data in two views, with different transfer function.</p>

---
