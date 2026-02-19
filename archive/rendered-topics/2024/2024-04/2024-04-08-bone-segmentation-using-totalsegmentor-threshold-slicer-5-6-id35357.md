---
topic_id: 35357
title: "Bone Segmentation Using Totalsegmentor Threshold Slicer 5 6"
date: 2024-04-08
url: https://discourse.slicer.org/t/35357
---

# Bone Segmentation using TotalSegmentor Threshold Slicer 5.6.2

**Topic ID**: 35357
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/bone-segmentation-using-totalsegmentor-threshold-slicer-5-6-2/35357

---

## Post #1 by @hmaguile (2024-04-08 16:10 UTC)

<p>Hi,</p>
<p>I’ve been on the hunt for the best method to extract ribs from CT scans. It’s not a big deal if other internal parts get included in the process since my goal is to create 3D models of the bones, and study the rib curvatures. In fact, if the heart is also segmented, that is just a bonus. I’ve experimented with TotalSegmentor, but I have not been able to segment just the bones here, only the Vertebrae. I have also been guided by some tutorials on YouTube where they use tools like PaintBrush and WaterShed. All of these methods works, but I TotalSegmentor takes a lot of time (noGPU), and I would be very happy I could do as little manual annotation as possible.</p>
<p>I’ve seen discussions on this forum recommending the Threshold method. Yet, it seems I’m hitting a snag with my version of Slicer, as I can’t seem to apply this threshold (see attached image). It would be ideal if I could segment directly based on what the threshold outlines.</p>
<p>Any advice or workaround suggestions would be greatly appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/646a4d79703051bee705e2871d20bc170a3ade91.jpeg" data-download-href="/uploads/short-url/ekjuXEeR81OdIKqPwUWE7AP9TeF.jpeg?dl=1" title="Screenshot 2024-04-08 at 15.56.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646a4d79703051bee705e2871d20bc170a3ade91_2_690x365.jpeg" alt="Screenshot 2024-04-08 at 15.56.36" data-base62-sha1="ekjuXEeR81OdIKqPwUWE7AP9TeF" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646a4d79703051bee705e2871d20bc170a3ade91_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646a4d79703051bee705e2871d20bc170a3ade91_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646a4d79703051bee705e2871d20bc170a3ade91_2_1380x730.jpeg 2x" data-dominant-color="5F5F74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-08 at 15.56.36</span><span class="informations">1920×1018 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Hans Martin</p>

---

## Post #2 by @hmaguile (2024-04-15 07:53 UTC)

<p>Hi,</p>
<p>I solved this by writing a script that takes all the STLs from the folder with the search word rib, sternum and costal cartilage, and combines it into one. If any one is interested in such scripts see below.</p>
<p>import os<br>
import numpy as np<br>
from stl import mesh</p>
<p>def merge_stl_files(folder_path):<br>
# Initialize an empty list to store mesh data<br>
mesh_data = <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
<pre><code># Iterate through files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.stl') and ('rib' in file_name.lower() or 'sternum' in file_name.lower() or 'costal cartilage' in file_name.lower()):
        file_path = os.path.join(folder_path, file_name)
        print(f'Processing file: {file_name}')

        # Load the STL file
        part_mesh = mesh.Mesh.from_file(file_path)

        # Add mesh data to the list
        mesh_data.append(part_mesh.data.copy())

# Concatenate mesh data to create merged mesh
merged_mesh_data = np.concatenate(mesh_data)

# Create a mesh object from the merged mesh data
merged_mesh = mesh.Mesh(merged_mesh_data)

# Output file path for the merged STL file
output_file = os.path.join(folder_path, 'Merged_Thoracic.stl')

# Write the merged mesh to the output STL file
merged_mesh.save(output_file)
print(f'Merged STL file saved as: {output_file}')
</code></pre>
<h1><a name="p-109582-folder-path-containing-the-stl-files-to-merge-1" class="anchor" href="#p-109582-folder-path-containing-the-stl-files-to-merge-1" aria-label="Heading link"></a>Folder path containing the STL files to merge</h1>
<p>folder_path = ‘folderpath’</p>
<h1><a name="p-109582-call-the-function-to-merge-stl-files-2" class="anchor" href="#p-109582-call-the-function-to-merge-stl-files-2" aria-label="Heading link"></a>Call the function to merge STL files</h1>
<p>merge_stl_files(folder_path)</p>

---
