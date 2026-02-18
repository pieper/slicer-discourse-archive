# Realistic Models, or captures

**Topic ID**: 13955
**Date**: 2020-10-09
**URL**: https://discourse.slicer.org/t/realistic-models-or-captures/13955

---

## Post #1 by @Ugi_Mikla (2020-10-09 13:18 UTC)

<p>Hi! I was wondering if there exists a module or extension where i can work my 3D models, applying textures, shadows, lights, to create a realistic scene or model.<br>
Thank u!</p>
<p>Eugenia</p>

---

## Post #2 by @lassoan (2020-10-09 13:22 UTC)

<p>If you already have your texture baked then you can apply it using Texture Model module (provided by SlicerIGT extension). You can customize lights using Lights module (provided by Sandbox extension).</p>
<p>Latest Slicer Preview Release is updated to use <a href="https://blog.kitware.com/vtk-pbr/">VTK9, which supports physically based rendering</a>. We don’t have any of the PBR features exposed in a module with a convenient GUI yet, but you can set up lights and materials by a few lines of Python script.</p>
<p>If you have working code snippets then you can easily put them into a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">scripted module</a> to have a nice GUI.</p>
<p>Let us know if you run into any trouble or if you could manage to get some nice renderings.</p>

---
