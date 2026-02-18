# In 'Restore Saved Scene', when is 'add & restore' important to do?

**Topic ID**: 1723
**Date**: 2017-12-26
**URL**: https://discourse.slicer.org/t/in-restore-saved-scene-when-is-add-restore-important-to-do/1723

---

## Post #1 by @aNonprofessional (2017-12-26 09:28 UTC)

<p>After loading the SPL Brain Atlas, when I click on ‘Restore or delete saved scene views’, and then click on Restore a named scene, I get an error/warning message about ‘add &amp; restore’, and I wonder:</p>
<ol>
<li>what it means, and</li>
<li>in what circumstances would it be important to pay attention to it?</li>
<li>what exactly will be permanently lost if I don’t select ‘add &amp; restore’?</li>
<li>should I just always ‘add &amp; restore’?</li>
<li>and what would ‘add &amp; restore’ accomplish?</li>
</ol>
<p>The error/warning reads,<br>
“Data missing from Scene View”, and its window contains the messages,</p>
<p>“Add data to scene view “Brainstem” before restoring?<br>
Data is present in the current scene but not in the scene view.<br>
If you don’t add and restore, data not already saved to disk, or saved in another scene view, will be permanently lost!”</p>

---

## Post #2 by @Nicole_Aucoin (2017-12-26 15:00 UTC)

<p>This was a warning we added when we realised that Scene Views were being used in a way not considered in the original design of different visualisations of the loaded data (for example hiding and showing different anatomical models in an atlas).<br>
If new models were created from the loaded volumes after a scene view was already created, and then that scene view is restored, the new model could be lost unless it was already saved to disk from memory.</p>
<p>I would recommend always selecting ‘add &amp; restore’ and then re-saving the atlas.</p>
<p>Nicole</p>

---
