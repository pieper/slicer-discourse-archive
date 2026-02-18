# Reads DCM volume with grid transform with python

**Topic ID**: 28998
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/reads-dcm-volume-with-grid-transform-with-python/28998

---

## Post #1 by @Thirawat (2023-04-18 23:26 UTC)

<p>Hi all,</p>
<p>I want to read a DCM file and output it with the transform contained in the file.</p>
<p>But now that I’m using SimpleITK, it only outputs untransformed DCM files.</p>
<p>Can you suggest a method?</p>
<p>My code:</p>
<pre><code class="lang-auto">def readDCM(folder_path, win_level=50, win_width=100):
  series_reader = sitk.ImageSeriesReader()
  series_IDs = series_reader.GetGDCMSeriesIDs(folder_path)
  if not series_IDs:
      raise Exception("No DICOMs were found in the directory. Please select a different directory.")
      
  series_file_names = series_reader.GetGDCMSeriesFileNames(folder_path, series_IDs[0])
  series_reader.SetFileNames(series_file_names)
  image = series_reader.Execute()

  image_array = sitk.GetArrayFromImage(image)
  image_array = np.clip(image_array, win_level - 0.5 - (win_width - 1) / 2, win_level - 0.5 + (win_width - 1) / 2)
  image_array = (image_array - (win_level - 0.5)) / (win_width - 1)

  return image_array
</code></pre>
<p>Best,<br>
Thirawat</p>

---

## Post #2 by @lassoan (2023-04-18 23:32 UTC)

<p>SimpleITK’s DICOM reader can only read the most basic images.</p>
<p>dcm2niix tool can deal with a bit more complicated cases. It is a standalone toolfor converting DICOM to NRRD or NIFTI.</p>
<p>For advanced slice grouping, tilted-gantry image rectification, variable slice spacing compensation, etc. you need Slicer’s DICOM reader infrastructure. See examples how to use it <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom">here</a>.</p>

---

## Post #3 by @Thirawat (2023-04-19 08:40 UTC)

<p>I’ve tried to read the docs, but I’m not sure if there is a way to make it possible to use the slicer in colab.</p>

---

## Post #4 by @Thirawat (2023-04-19 09:17 UTC)

<p>I tried to read docs but not sure if it can be used in colab.</p>
<p>Or is there another python library to recommend?</p>
<p>Let me explain more. In my dicom file there is</p>
<ul>
<li>dicom volume</li>
<li>grid transform</li>
</ul>
<p>or I can save transform on dicom volume?</p>

---

## Post #5 by @Thirawat (2023-04-28 04:33 UTC)

<p>I solve my problem in another way <a href="https://discourse.slicer.org/t/transforme-segmentaion/29150/5">[click]</a>.</p>
<p>btw thank you, everyone.</p>

---
