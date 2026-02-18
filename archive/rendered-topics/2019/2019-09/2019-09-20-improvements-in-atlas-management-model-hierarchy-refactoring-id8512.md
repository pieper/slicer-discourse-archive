# Improvements in atlas management: model hierarchy refactoring

**Topic ID**: 8512
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/improvements-in-atlas-management-model-hierarchy-refactoring/8512

---

## Post #1 by @cpinter (2019-09-20 17:58 UTC)

<p>The preview version of 3D Slicer starting today (Sep 20) includes a major change that affects the management of atlases. The two main goals of the change are:</p>
<ul>
<li>Change the way visibility works in subject hierarchy for folders</li>
<li>Remove the old model hierarchy concept from Slicer</li>
</ul>
<p>Details:</p>
<ol>
<li>
<p>Use only folders in subject hierarchy instead of the former hybrid folder / model hierarchy way. It had some issues, such as erroneous visibility setting, or the inability to create folders that allow overriding display properties (only programmatically or opening a scene). This new mechanism allows</p>
<ul>
<li>Significant speedup when handling larger hierarchies: the NAC brain atlas visibility change takes 1.5s instead of 15s, and works well (instead of ignoring parts of the hierarchy)</li>
<li>Override of display properties for folders (such as color, slice intersection visibility, etc.) for models, segmentations, and markups</li>
<li>Manual creation of hierarchies that can handle display property overrides. This enables converting models in a folder into a single segmentation node.</li>
<li>Correctly import old scenes containing model hierarchies (they are converted to folders)</li>
<li>Subjects and studies to act like the new folders in every way</li>
</ul>
</li>
<li>
<p>Update Models module to use the updated hierarchies</p>
<ul>
<li>If clicked on a folder, the model display properties can be set. Visibility and opacity are always applied on the whole branch, and color, slice intersection visibility etc. are applied if the flag is turned on (right-click menu for the eye, or when explicitly setting the color on a folder)</li>
<li>Setting display properties for multiple selected models at once (such as slice intersection visibility, representation, etc.)</li>
<li>Remove disfunctional fiber related controls (will be added back through SlicerDMRI)</li>
</ul>
</li>
</ol>
<p>Please note that further speedup of show/hide and display property override will hopefully follow soon.</p>
<p>A short video about the feature:</p>
<div class="lazyYT" data-youtube-id="baintMUn98s" data-youtube-title="3D Slicer - Improvements in atlas management" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #2 by @Fernando (2019-09-28 10:30 UTC)

<p>This looks great!</p>
<p>Is there any documentation I can use to go from a bunch of volumes + segments to a nice atlas hierarchy like this?</p>

---
