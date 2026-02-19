---
topic_id: 35817
title: "Editing An Existing Nrrd File"
date: 2024-04-29
url: https://discourse.slicer.org/t/35817
---

# Editing an Existing NRRD File

**Topic ID**: 35817
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/editing-an-existing-nrrd-file/35817

---

## Post #1 by @DrBorg (2024-04-29 20:30 UTC)

<p>Hello!  I have a quick question.</p>
<p>I’m using pynrrd to open an existing <strong>segmented NRRD</strong> file.  I’m trying to remove certain segments that are there, then re-save without those removed segments.</p>
<p>I have many Segments, and each apparently is named SegmentX_Property, where “X” is their respective number (e.g., 1, 2, 3…) and “Property” is a property (e.g., Color, Name, etc.).  I have a list of numbers (e.g., [1, 3, 5, 7]), representing segments I wish to keep.</p>
<p>Can someone help me in taking this list and my existing pynrrd file to output a new Segmented NRRD file with only Segments in my list of numbers?</p>
<p>Thank you so much in advanced!</p>
<p>I’ll include my code just for reference, though its scope extends beyond what I’m asking here.</p>
<pre><code class="lang-auto">import SimpleITK as sitk
import numpy as np
import nrrd

def filter_segments_by_name(nrrd_file_path, target_substrings):
    try:
        image = sitk.ReadImage(nrrd_file_path)
        filtered_names = []

        for key in image.GetMetaDataKeys():
            if key.endswith("_Name"):
                segment_name = image.GetMetaData(key)
                if any(substring.lower() in segment_name.lower() for substring in target_substrings):
                    filtered_names.append(segment_name)

        return filtered_names

    except Exception as e:
        print(f"Error reading NRRD file: {e}")
        return []

def filter_segments_properties(image, filtered_names):
    filtered_segments = []

    # Iterate over all metadata keys
    for key in image.GetMetaDataKeys():
        if key.startswith("Segment") and key.endswith("_Name"):
            segment_number = int(key.split("_")[0][len("Segment"):])
            segment_name = image.GetMetaData(key)
            if segment_name in filtered_names:
                filtered_segments.append(segment_number)

    return filtered_segments


def filter_segments(segments_to_keep, filename):
    """
    Filters segments from an NRRD file based on the provided list of segment numbers.

    Args:
        segments_to_keep (list[int]): List of segment numbers to retain.
        filename (str): Path to the input .seg.nrrd file.

    Returns:
        None. Saves the filtered data to a new NRRD file.
    """
    # Load the .seg.nrrd file
    data, header = nrrd.read(filename)

    # Initialize an empty dictionary to store the filtered data
    filtered_data = {}

    # Iterate through each segment
    for segment_number in segments_to_keep:
        segment_key_prefix = f"Segment{segment_number}_"

        # Collect all keys associated with this segment
        segment_keys = [key for key in header.keys() if key.startswith(segment_key_prefix)]

        # Copy the segment data and its properties
        for key in segment_keys:
            filtered_data[key] = data[key]

    # Write the filtered data to a new NRRD file
    output_filename = 'filtered_segments.nrrd'
    nrrd.write(output_filename, filtered_data, header)

    print(f"Filtered data saved to {output_filename}")


# Load the NRRD file
**nrrd_file_path = [insert your .seg.nrrd file here]**
**save_path = [insert your path here for saving]**
data, header = nrrd.read(nrrd_file_path)
image = sitk.ReadImage(nrrd_file_path)

# Define your list of target substrings
target_substrings = ["rib", "vert"]

# Get the filtered segment names
filtered = filter_segments_by_name(nrrd_file_path, target_substrings)

# Filter the segments based on the names
segments_to_keep = filter_segments_properties(image, filtered)


# Create a set for efficient membership checking
segments_to_keep_set = set(segments_to_keep)

# Filter segments
for segment in list(header['labels']):
    if all(item in segments_to_keep_set for item in segment):
        # Segment contains all items from segments_to_keep
        continue
    else:
        # Remove this segment
        del header['labels'][segment]
        del header['sizes'][segment]
        del header['spacings'][segment]
        # Add any other relevant fields to remove


nrrd.write(save_path, data, header)

</code></pre>

---

## Post #2 by @lassoan (2024-04-30 02:37 UTC)

<p>This is inplemented in slicerio Python package: you specify thr list of segment names and label values and you get a new nrrd file that only contains those segments, with the label values that you specified.</p>

---

## Post #3 by @DrBorg (2024-04-30 05:39 UTC)

<p>Hi,</p>
<p>Thank you so much for your prompt reply.  I have been trying to use this library, but cannot get a valid NRRD file to save at the end of the process with extracted features.  See my code below:</p>
<pre><code class="lang-auto">
import slicerio
import numpy as np
import nrrd

nrrd_file_path = [input file path]
save_path = [output file path]

# Load the existing NRRD file
nrrd_data, nrrd_header = nrrd.read(nrrd_file_path)

# Let's say I know I want to keep these three segments with these three corresponding Segment ID numbers (I assume that's what the numbers are for)
filtered_segment_names = ['L3 vertebra', 'L2 vertebra', 'L1 vertebra']  # Segment Names
filtered_numbers = [20, 21, 22]  # Segment IDs

# Construct segments_to_extract from these lists
segments_to_extract = {"Segment" + str(segment): label for segment, label in zip(filtered_segment_names, filtered_numbers)}

# Create a new NRRD data array filled with zeros
new_nrrd_data = np.zeros_like(nrrd_data)

# Loop over the segments and labels
for segment, label in segments_to_extract.items():
    # Find the indices where the segment is located in the original NRRD data
    indices = np.where(nrrd_data == segment)

    # Set these indices to the specified label value in the new NRRD data
    new_nrrd_data[indices] = label

# Write the new NRRD data to a new file using the existing header
nrrd.write(save_path, new_nrrd_data, nrrd_header)

</code></pre>

---

## Post #4 by @lassoan (2024-04-30 11:34 UTC)

<p>See an example of how to do this using slicerio <a href="https://github.com/lassoan/slicerio?tab=readme-ov-file#extract-selected-segments-with-chosen-label-values">here</a>.</p>

---

## Post #5 by @DrBorg (2024-04-30 12:50 UTC)

<p>Hello,</p>
<p>Thank you kindly once again.  I apologize for my rudimentary questions.<br>
I now have a script that outputs a new .seg.nrrd file that has the correct segment names.</p>
<p>However, when I try actually using the file (say, in <a href="https://mi.eng.cam.ac.uk/Main/StradView" rel="noopener nofollow ugc">Stradview</a>), an error occurs (see below).</p>
<p>Is it the <strong>segment_names_to_labels</strong> variable?  For it, I input a paired list of segment names with their corresponding IDs.  See code below error message for context.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b900400d229a3717ff8a1b67190c255f6b3191c.png" data-download-href="/uploads/short-url/6dn5af1S2uHPgvMaCFsO85ao8Ik.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b900400d229a3717ff8a1b67190c255f6b3191c.png" alt="image" data-base62-sha1="6dn5af1S2uHPgvMaCFsO85ao8Ik" width="690" height="272" data-dominant-color="EAE9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×526 34.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
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
