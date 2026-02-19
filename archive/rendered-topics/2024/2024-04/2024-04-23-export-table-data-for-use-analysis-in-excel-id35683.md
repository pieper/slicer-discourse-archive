---
topic_id: 35683
title: "Export Table Data For Use Analysis In Excel"
date: 2024-04-23
url: https://discourse.slicer.org/t/35683
---

# Export table data for use/analysis in Excel

**Topic ID**: 35683
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/export-table-data-for-use-analysis-in-excel/35683

---

## Post #1 by @Justus_Muller-Goebel (2024-04-23 15:36 UTC)

<p>Hi there,</p>
<p>I am pretty new to 3D-slicer but enjoying the features a lot.<br>
I recently used the function “line profile” to collect data on a CBCT along a straight line. After plotting the curve in 2 dimension the individual values were found in a created table.<br>
Since I wanted to use the values for further calculations (in excel) I was wondering which options of exporting are available.</p>
<p>Specifically asking, due to the conflict with excel by simply “copy and pasting” values. Hereby “,” and “.” are getting confused and values over 1.xx (in the table in 3D-slicer) are imported as higher values of 10000.xx. Values e.g. 0.9xx are saved the same but are not formated as numbers in excel.<br>
Ignoring of predefined “,” and “.” in settings of excel does not solve the wrong importing of values over 1.xx into excel (still importing with 1000.x …).<br>
See example below.</p>
<p>Is there any suggestion solving this issue?<br>
Happy for any input.</p>
<p>Best</p>
<p>Example (distance - Hounfield Units):<br>
a. Values in 3D-slicer:</p>
<p>|0.998547 - 195|<br>
|1.0008 - 194|<br>
|1.00304 - 193|</p>
<p>b. valsues in excel after importing</p>
<p>|0.998547 - 195.00<br>
|10008.000000 - 194.00|<br>
|100304.000000 - 193.00|</p>

---

## Post #2 by @lassoan (2024-04-24 01:36 UTC)

<p>I would recommend to save the table and load the CSV file into Excel.</p>

---

## Post #3 by @Justus_Muller-Goebel (2024-04-25 08:24 UTC)

<p>Hi there,</p>
<p>thanks for uyour input. Unfortunately this still houses the error of wring formating.</p>
<p>best</p>

---

## Post #4 by @lassoan (2024-04-25 12:49 UTC)

<p>When you import the CSV file into Excel then your can choose <code>.</code> as decimal delimiter. This issue impacts all people who use Excel on systems with regional settings set to German (or other region that does not use decimal point). There are many solutions, for example see a handful of them here: <a href="https://stackoverflow.com/questions/11421260/csv-decimal-dot-in-excel" class="inline-onebox">CSV decimal dot in Excel - Stack Overflow</a></p>
<p>Alternatively, you can run this small code snippet in Python (for example, in Slicer’s Python console) to convert the tsv/csv file to xlsx:</p>
<pre data-code-wrap="python"><code class="lang-python">csv_file = r"c:\tmp\Table.tsv"
xls_file = r"c:\tmp\Table.xlsx"

# Install pandas and openpyxl
try:
    import pandas as pd
    import openpyxl
except ImportError:
    pip_install("pandas openpyxl")
    import pandas as pd
    import openpyxl
# Read the TSV/CSV file and write it to an Excel file
df = pd.read_csv(csv_file, sep="\t", decimal=".")
df.to_excel(xls_file, index=False)
</code></pre>

---
