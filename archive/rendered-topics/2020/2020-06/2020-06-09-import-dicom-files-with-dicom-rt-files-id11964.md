# Import Dicom Files with DICOM RT files

**Topic ID**: 11964
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/import-dicom-files-with-dicom-rt-files/11964

---

## Post #1 by @loubna (2020-06-09 17:13 UTC)

<p>Hi;<br>
I am trying to develop a python script in order to import spectroscopy and metabolite data. However when I import the dicom file with SlicerRT structures, I have got an error “DICOM Plugin failed: Dataset does not have attribute ‘ImageType’.”<br>
here is the code :</p>
<p>filePath = file[0]<br>
ds = dicom.read_file(filePath,stop_before_pixels=True)<br>
if ds.ImageType[2] == ‘SPECTROSCOPY’:<br>
<span class="hashtag">#Only</span> a single file when we talk about spectrosopy files<br>
result = []<br>
loadable = DICOMLoadable()<br>
loadable.files = [filePath]<br>
loadable.name = ‘Donnes Spectrophotometriques’<br>
loadable.tooltip = ‘Siemens’<br>
loadable.confidence = 0.95<br>
loadable.selected = True<br>
result.append(loadable)<br>
return result</p>
<p>when I import spectroscopy data in slicer with dicom diles (not DICOM RT), the spectroscopy data displayed without any error.</p>
<p>Can you tell me why the script does not work when import it with DicomRt files</p>
<p>thank’s in advance</p>

---

## Post #2 by @lassoan (2020-06-09 17:33 UTC)

<p><a href="https://dicom.innolitics.com/ciods/cr-image/general-image/00080008">Image type tag</a> is in “General Image” module and so it is probably not permitted in non-image data objects, such as RT structure set. You can put <code>ds.ImageType</code> between try/except or check if the attribute exists before you try to access it.</p>

---
