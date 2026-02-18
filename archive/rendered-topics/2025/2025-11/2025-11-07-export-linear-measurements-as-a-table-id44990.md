# Export linear measurements as a table

**Topic ID**: 44990
**Date**: 2025-11-07
**URL**: https://discourse.slicer.org/t/export-linear-measurements-as-a-table/44990

---

## Post #1 by @jnations (2025-11-07 16:08 UTC)

<p>I am trying to take multiple linear measurements from a bone using the markups tool, then export the lengths (distances) as a table. This has proven to be incredibly complicated, with posts discussing creating a database in excel from json files, or using python scripts. I can export a single measurement, but I don’t know how to export a table of measurements. I would be content with copy/paste if I could get the lengths in a single table. Again, I don’t need coordinates, points, or anything else, just the measurement name and the length value. Am I missing something really obvious?<br>
Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c831da9e3f249eeb120222f842e454b42551494.jpeg" data-download-href="/uploads/short-url/aURcxk8zhd75uIJRt7hFvDC0TZO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c831da9e3f249eeb120222f842e454b42551494_2_634x500.jpeg" alt="image" data-base62-sha1="aURcxk8zhd75uIJRt7hFvDC0TZO" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c831da9e3f249eeb120222f842e454b42551494_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c831da9e3f249eeb120222f842e454b42551494_2_951x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c831da9e3f249eeb120222f842e454b42551494_2_1268x1000.jpeg 2x" data-dominant-color="606172"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1514 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-11-07 18:22 UTC)

<p>Measurements are saved in the json file. I am not sure if there is a readily available way to export a bunch of measurements from different line Markups. You can use chatGPT or other LLMs to help you create a simple script to do it.</p>

---

## Post #6 by @Andinet_Enquobahrie (2025-11-08 12:33 UTC)

<p>As Murat noted, you can try something along the following line:</p>
<pre data-code-wrap="python"><code class="lang-python"># === Markups → CSV: Node name + numeric value + units ===
# Paste into Slicer's Python console.

import os, csv, datetime
import slicer

# --- Choose output file ---
def pick_save_path(default_name):
    try:
        import qt
        dlg = qt.QFileDialog()
        dlg.setAcceptMode(qt.QFileDialog.AcceptSave)
        dlg.setNameFilter("CSV (*.csv)")
        dlg.selectFile(default_name)
        if dlg.exec():
            return dlg.selectedFiles()[0]
    except:
        pass
    return os.path.join(slicer.app.temporaryPath, default_name)

ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
out_path = pick_save_path(f"markups_values_units_{ts}.csv")

# --- Collect Markups nodes ---
markups_nodes = slicer.util.getNodesByClass("vtkMRMLMarkupsNode")

# --- CSV output ---
header = ["NodeName", "Value", "Units"]
rows = []

for node in markups_nodes:
    name = node.GetName() or ""
    mcount = node.GetNumberOfMeasurements()

    if mcount == 0:
        rows.append([name, "", ""])
        continue

    for i in range(mcount):
        m = node.GetNthMeasurement(i)

        try:
            value = m.GetValue()
        except:
            value = ""

        units = m.GetUnits() or ""

        rows.append([name, value, units])

# --- Write CSV ---
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"[Markups → CSV] {len(rows)} rows written to:\n{out_path}")
slicer.util.delayDisplay(f"Export complete:\n{out_path}", 1500)
</code></pre>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bfaa79bc94e915289d1d2caf037fece475d1529.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f5879a5855d11f8d495491bd3c7b6f80106c00e.jpeg" data-video-base62-sha1="d7GtsbkLxkzHTEYVmZgKTesBjlL.mp4">
  </div><p></p>

---

## Post #7 by @jnations (2025-11-10 18:13 UTC)

<p>This works beautifully, thanks for the help!</p>

---
