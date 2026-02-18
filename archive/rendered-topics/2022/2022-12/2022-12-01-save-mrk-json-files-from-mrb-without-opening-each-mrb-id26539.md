# Save .mrk.json files from .mrb without opening each .mrb

**Topic ID**: 26539
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/save-mrk-json-files-from-mrb-without-opening-each-mrb/26539

---

## Post #1 by @Masteling (2022-12-01 15:42 UTC)

<p>Is there a way to save all mrk.json files in a .mrb bundle without opening each .mrb individually and selecting the .mrk.json files individually in the save window?</p>
<p>Context:<br>
For each subject I have a .mrb file that contains the relevant .mrk.json files. I use  Spyder (<a href="https://www.spyder-ide.org/" rel="noopener nofollow ugc">https://www.spyder-ide.org/</a>) for data analysis of the contents of the .mrk.json files.</p>
<p>Currently, I open each .mrb file and select the .mrk.json files manually (about 20 files per subject) in the save window and save them into a folder. Is there a way to do this without needing to open each .mrb file individually? The project is quickly expanding and I would like to automate this step.</p>

---

## Post #2 by @pieper (2022-12-01 16:33 UTC)

<p>The <code>.mrb</code> file is just a <code>.zip</code>, so you can open it and extract the <code>.mrk.json</code> files pretty easily with a python script.</p>

---

## Post #3 by @Masteling (2022-12-01 17:07 UTC)

<p>Thank you for the quick response. I got it working.</p>
<p>Here is my approach in case others have the same question:</p>
<pre><code class="lang-auto">using zipfile
using json

archive = zipfile.ZipFile(directory+mrb_name, 'r')
filenames = [x for x in archive.namelist() if '.mrk.json' in x]
f = archive.open(filenames[i])
data = json.load(f)
</code></pre>

---
