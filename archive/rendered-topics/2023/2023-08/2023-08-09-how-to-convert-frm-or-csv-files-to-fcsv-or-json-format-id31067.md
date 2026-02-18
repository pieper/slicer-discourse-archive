# How to convert FRM or CSV files to FCSV or JSON format

**Topic ID**: 31067
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/how-to-convert-frm-or-csv-files-to-fcsv-or-json-format/31067

---

## Post #1 by @AriD (2023-08-09 14:59 UTC)

<p>Hello,<br>
I have a CSV file that includes numerous specimens, each with multiple landmark coordinates. Additionally, there are several FRM files for each specimen, also containing various landmark coordinates.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c75c6e131e3a06700e8ca1b15a875d5c9ab77d93.png" data-download-href="/uploads/short-url/srD2UqhXt8n55E6qQGomV8T6fAv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c75c6e131e3a06700e8ca1b15a875d5c9ab77d93.png" alt="image" data-base62-sha1="srD2UqhXt8n55E6qQGomV8T6fAv" width="690" height="48" data-dominant-color="E4E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1407×99 8.56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a method to upload this CSV file to generate GPA and PCA? Alternatively, is there a way to convert these different files into the FCSV or JSON format for further analysis?</p>
<p>Thank you,<br>
Ariana</p>

---

## Post #2 by @muratmaga (2023-08-09 16:42 UTC)

<p>There is nothing in Slicer that will convert this CSV format in a way that Slicer expects the coordinate data.</p>
<p>With a little scripting you can convert that into FCSV format, which expects each landmarks to be a row of data matrix (see the format here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a>)</p>
<p>If you are comfortable with R, read this csv file into your R session, convert it into the 2D array in which each coordinate is a row, then use the SlicerMorphR extension to write the FCSV file.<br>
you can use devtools to install SlicerMorphR<br>
'devtools::install_github(“SlicerMorph/SlicerMorphR”)</p>
<p>Each of your samples (rows in your original data) should be written as a separate FCSV file. You can then use the GPA module in SlicerMorph to do the GPA alignment and PCA decomposition and visualize the results.</p>

---
