# Using VTK filters with the python interactor?

**Topic ID**: 7029
**Date**: 2019-06-04
**URL**: https://discourse.slicer.org/t/using-vtk-filters-with-the-python-interactor/7029

---

## Post #1 by @stevenagl12 (2019-06-04 22:00 UTC)

<p>Are there any instructions for how you can use the python interpreter to apply different vtk filters? For example, the vtkcurvatures filter? Also, does anyone know if there is a VTK filter that works within slicer to differentiate the spread of network like structures (blood vessels for example) to color density patterns? For example, coloring high densities of the vessels one color, and low densities another?</p>

---

## Post #2 by @pieper (2019-06-05 15:26 UTC)

<p>Pretty much anything you can do in VTK is available via the slicer python console.  There are a <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model" rel="nofollow noopener">bunch of examples</a>.  You can look around the [VTK examples](<a href="https://lorensen.github.io/VTKExamples/site/" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/</a>} and if you find a filter that does what you want it should be easy to make use of it in Slicer.</p>

---

## Post #3 by @lassoan (2019-06-05 21:42 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" rel="nofollow noopener">Slicer programming tutorials</a> (such as the PerkLab bootcamp tutorial) show some specifics about how to connect VTK filter inputs and outputs to Slicer.</p>

---
