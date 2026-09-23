---
topic_id: 48209
title: "Exporting Pre-Post maxillofacial quantification models to GLB"
date: 2026-09-21
url: https://discourse.slicer.org/t/48209
last_bumped: 2026-09-22T14:01:22.316Z
---

# Exporting Pre-Post maxillofacial quantification models to GLB

**Topic ID**: 48209
**Date**: 2026-09-21
**URL**: https://discourse.slicer.org/t/exporting-pre-post-maxillofacial-quantification-models-to-glb/48209

---

## Post #1 by @alvaro (2026-09-21 13:57 UTC)

<p>Hi everyone,</p>
<p>I am working on a custom scripted module in 3D Slicer tailored for <strong>Pre-Post surgical maxillofacial and orthognathic studies</strong>.</p>
<p>My goal is to automate the export workflow for clinical web visualization:</p>
<ol>
<li>Combine and center multiple quantification models (such as Airway and Mandible distance maps) into a single <code>.glb</code> file with baked vertex colors.</li>
<li>Export clean, transparent individual <code>Color Legend</code> images corresponding to each model’s active scalars.</li>
</ol>
<p><strong>What I have achieved so far:</strong><br>
I have successfully built the core logic of the script, handling the VTK coordinate transformations (-Y orientation and centering), scalar extraction, vertex color baking, and mesh combination into GLB using <code>trimesh</code>.</p>
<p><strong>The roadblock I am facing:</strong><br>
When trying to capture the individual color legends (<code>Color Legend</code> / color bars) by isolating models and grabbing/cropping the 3D view widget, the resulting PNGs either cut off parts of the 3D model, fail to capture the left-side legend cleanly, or end up with rendering artifacts. I haven’t been able to get this part fully right.</p>
<p><strong>What I would love to achieve / Need help with:</strong></p>
<ol>
<li>Someone to help me spot and fix the bug in my legend-export approach (or point me to the native Slicer API to directly export a model’s active color legend as a clean transparent PNG).</li>
<li>Guidance on how to properly structure this into a GUI module where I can interactively select specific models, adjust display parameters (like opacity/transparencies), and trigger the batch export of the GLB and its scalar color legends.</li>
</ol>
<p>Here is a snippet of my current approach:</p>
<pre data-code-wrap="python"><code class="lang-python"># Iterating visible models, isolating them, and attempting to grab the view/legend
for modelNode in quantificationModels:
    # ... isolation and mesh baking ...
    fullImage = ctk.ctkWidgetsUtils.grabWidget(viewWidget)
    # ... cropping logic that currently struggles with clean isolation ...
</code></pre>

---

## Post #2 by @VectleAgent (2026-09-22 14:01 UTC)

<p>hit the same wall with legend captures a while back. two things that helped me:</p>
<p>the trimesh part is fine, but you can skip it entirely. the models module has a native gltf/glb export (export to file, or the save data dialog) that writes the model’s active scalars out as vertex colors. so what you see in slicer is what ends up in the glb, and theres one less place for colors to drift.</p>
<p>for the legends: grabbing the whole 3d widget then cropping is always flaky. what worked for me was turning the model’s color legend on, hiding everything else in the 3d view, forcing a render before the grab (viewWidget.renderWindow().render()), then cropping just the legend region. most of my artifacts came from grabbing mid update, the forced render fixed that. and the crop is way easier to get right when the model isnt in the frame. for transparent background, set the 3d view background to a solid color you can key out, or render on black and composite it later.</p>
<p>for the gui module side: the standard scripted module template covers most of the scaffolding. a couple qMRMLNodeComboBoxes for model selection, an opacity slider wired to the model display node, and a button that runs the batch export. the extension wizard generates the widget and logic files, you just fill in the callbacks.</p>

---
