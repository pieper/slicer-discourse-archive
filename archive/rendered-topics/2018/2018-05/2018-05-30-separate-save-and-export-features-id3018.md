# Separate Save and Export features

**Topic ID**: 3018
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/separate-save-and-export-features/3018

---

## Post #1 by @lassoan (2018-05-30 13:48 UTC)

<p>Users are often confused by the complexity of save dialog and that they have to choose file formats and decide what files to overwrite. Saving to MRB simplifies things: everything is saved, and only a single file is used. However, it is not easy to discover this option (people don’t even know that single-file save feature exists).</p>
<p>Should we split the current “Save data” dialog to two independent features (listed separately in the menu)?</p>
<ul>
<li>Save scene: save as MRB, use only a simple file selector</li>
<li>Export data: current save data dialog, maybe with MRB option removed</li>
</ul>

---

## Post #2 by @jcfr (2018-05-30 13:58 UTC)

<blockquote>
<p>Save scene: save as MRB, use only a simple file selector</p>
</blockquote>
<p>The dialog could also indicate that MRB are zip files and that using “Export data” allows more granularity by saving each file independently</p>

---

## Post #3 by @ihnorton (2018-05-30 16:44 UTC)

<p>+1 to clarifying Save vs Export</p>
<p>MRB has double steps of writing to temporary directory and then compression, which can be slow for large scenes. I would suggest to turn off compression, or default to “save to folder” even in this simplified dialog. Perhaps with the folder name corresponding to the MRML filename.</p>

---

## Post #4 by @pieper (2018-05-31 00:10 UTC)

<p>I would vote for using a single dialog but with mrb selected by default, and then with a radio button that allows saving individual items.</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a>’s idea of saving the volumes uncompressed when they are going into an mrb is interesting and should be easy to test.  I also like offering options to easily organize the data even if it’s not being zipped.</p>
<p>(Slightly related note, I also would like to see the mrml scene loader provide a method to specify the path to any data file that isn’t found at the path specified in the mrml file, i.e. because someone moved or renamed it.)</p>

---
