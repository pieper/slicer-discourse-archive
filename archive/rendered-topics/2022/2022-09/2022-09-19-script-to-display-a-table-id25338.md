# Script to display a table

**Topic ID**: 25338
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/script-to-display-a-table/25338

---

## Post #1 by @Jack_Zhang (2022-09-19 14:18 UTC)

<p>Sorry if this is a dumb question, but I’m <strong>very</strong> new to slicer. I’m trying to code a python module that can display coordinates from a csv file. I know that you can do this with properly formatted csv files using the markup module, but I’d like to know how to do this from scratch. The goal is to create a module that allows me to select a csv file I upload to Slicer, append the required header, and then display the points.</p>
<p>Currently, I’m getting stuck on two steps. The first is figuring out how to get script to read whatever file I select with the ctkPathLineEdit widget. The second is figuring out how to display the data points after the csv file has been edited (this is the one I need the most help with). Any tips or hints?</p>

---

## Post #2 by @lassoan (2022-09-20 07:16 UTC)

<h1><a name="p-83604-option-a-1" class="anchor" href="#p-83604-option-a-1" aria-label="Heading link"></a>Option A</h1>
<p>The most flexible and powerful option is to to save the coordinates in a json file:</p>
<pre data-code-wrap="json"><code class="lang-json">{"@schema": "https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json#",
"markups": [{"type": "Fiducial", "coordinateSystem": "LPS", "controlPoints": [
    { "label": "F-1", "position": [-53.388409961685827, -73.33572796934868, 0.0] },
    { "label": "F-2", "position": [49.8682950191571, -88.58955938697324, 0.0] },
    { "label": "F-3", "position": [-25.22749042145594, 59.255268199233729, 0.0] }
]}]}
</code></pre>
<p>You can load using:</p>
<pre><code>markupsNode = slicer.util.loadMarkups("/path/to/MyMarkups.mkp.json")
</code></pre>
<h1><a name="p-83604-option-b-2" class="anchor" href="#p-83604-option-b-2" aria-label="Heading link"></a>Option B</h1>
<p>If you only need to specify coordinates, then you can create a csv file with a few columns:</p>
<pre data-code-wrap="txt"><code class="lang-txt">label,l,p,s,defined,selected,visible,locked,description
F-1,-19.9067,13.9347,29.443,1,1,1,0,
F-2,-7.3939,-76.9499,17.5525,1,1,1,0,
F-3,81.7333,-42.9415,9.62559,1,1,1,0,
</code></pre>
<p>You can load it like this:</p>
<pre data-code-wrap="python"><code class="lang-python">markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
slicer.modules.markups.logic().ImportControlPointsFromCSV(MRMLMarkupsCurveNode")
</code></pre>
<h1><a name="p-83604-more-information-3" class="anchor" href="#p-83604-more-information-3" aria-label="Heading link"></a>More information</h1>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json">Markup file formats</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-markups-from-file">How to load markup files</a></li>
</ul>

---

## Post #3 by @Jack_Zhang (2022-09-20 15:26 UTC)

<p>Thanks this helped a lot!</p>

---

## Post #4 by @Jack_Zhang (2022-09-20 15:30 UTC)

<p>Is there anyway to edit the text for the label displayed in the scene so it doesn’t say “MarkupsCurve”?</p>

---
