# Segmented NRRD File is 0 Bytes After Editing

**Topic ID**: 36387
**Date**: 2024-05-25
**URL**: https://discourse.slicer.org/t/segmented-nrrd-file-is-0-bytes-after-editing/36387

---

## Post #1 by @DrBorg (2024-05-25 13:46 UTC)

<p>Hello,</p>
<p>I’m working with a segmented NRRD file and I’m trying to remove certain segments.  I wrote the script, shown below, to do this.</p>
<p>It appears to work, however, the output SEG.NRRD outputs the following error when opened:<br>
<strong>This NRRD file contains non-short and non-byte data.  Short or char data formats are required.</strong></p>
<p>Any thoughts?  Thank you!</p>
<pre><code class="lang-auto"># Imports
import slicerio
import nrrd

# Pre-defined Variables
nrrd_file_path = r"\Python Scripts\CTChest segmentation.seg.nrrd"
save_path = r"\Python Scripts\CTChest segmentation EDITED.seg.nrrd"
segment_names_to_labels = [('L3 vertebra', 20), ('L2 vertebra', 21), ('L1 vertebra', 22)]

# Load the existing NRRD file
voxels, header = nrrd.read(nrrd_file_path)

# Obtain NRRD segmentation information
segmentation_info = slicerio.read_segmentation_info(nrrd_file_path)

# Save new file with extracted data
extracted_voxels, extracted_header = slicerio.extract_segments(voxels, header, segmentation_info, segment_names_to_labels)
nrrd.write(save_path, extracted_voxels, extracted_header)
</code></pre>

---
