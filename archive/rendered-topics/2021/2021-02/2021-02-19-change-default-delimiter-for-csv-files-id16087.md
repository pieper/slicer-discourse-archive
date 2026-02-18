# Change default delimiter for csv files

**Topic ID**: 16087
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/change-default-delimiter-for-csv-files/16087

---

## Post #1 by @elledriver (2021-02-19 14:27 UTC)

<p>Hello there,</p>
<p>I want to use 3DSlicer to plot data from csv files that use semicolons as delimiter. However, it seems that this is not possible. I cannot use a comma as a delimiter for certain reasons.</p>
<p>Is there really no way to use csv files with delimiters other than comma?</p>
<p>Thank you very much in advance!</p>
<p>Elle</p>

---

## Post #2 by @lassoan (2021-02-19 14:34 UTC)

<p>You can rename the file to have .tsv extension (tab-separated-value) and then use tab character as separator. If you can really just use semicolon then you can load it with a 4-5 lines of Python (load the file with pandas into a numpy array and set the array in a table node using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateTableFromArray">slicer.util.updateTableFromArray</a>).</p>

---

## Post #3 by @elledriver (2021-02-19 15:01 UTC)

<p>Hey Andras,<br>
Thank you very much for your quick reply. Indeed, I can only use semicolon as delimiter. Unfortunately, I have almost no experience with coding. Could you please elaborate further?</p>
<p>Thank you very much in advance!</p>

---

## Post #4 by @lassoan (2021-02-19 15:07 UTC)

<p>We could make the delimiter configurable, as long there is a strong use case for it (there is no reasonable alternative and/or many people would find it useful). Can you tell us why you must use semicolon? What generates the file? How are you going to use the table in Slicer?</p>

---

## Post #5 by @elledriver (2021-02-19 15:17 UTC)

<p>I am using 3Dslicer to plot data points (from csv files) in order to inspect whether their positioning is correct. These csv files also contain descriptions (text with quotes etc.), which belong to the data points and are therefore necessary. The plotting in 3D slicer is just a method of inspection, the csv files will be used for further purposes.</p>

---
