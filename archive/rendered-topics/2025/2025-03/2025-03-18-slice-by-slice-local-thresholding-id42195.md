---
topic_id: 42195
title: "Slice By Slice Local Thresholding"
date: 2025-03-18
url: https://discourse.slicer.org/t/42195
---

# Slice by Slice local Thresholding

**Topic ID**: 42195
**Date**: 2025-03-18
**URL**: https://discourse.slicer.org/t/slice-by-slice-local-thresholding/42195

---

## Post #1 by @tas47 (2025-03-18 06:51 UTC)

<p>Hello everyone,</p>
<p>This is my first post. I’ve been spending a lot of time learning about 3D Slicer, particularly focusing on the docs and segmentation techniques.  I’m currently faced with the challenge of  segmenting tumours that don’t appear in every slice of an MRI  volume.</p>
<p>I’m wondering if there is a method to apply the local thresholding feature in the segmentation editor on a per-slice basis similar to the brush feature. Ideally, the workflow would involve, to :</p>
<ol>
<li>Highlighting masks or regions of interest (ROIs) on individual slices where a tumor is detected.</li>
<li>Applying local thresholding on each of these slices to adjust the threshold by analyzing the local histogram.</li>
<li>Repeating this process for each slice and eventually compiling these into a complete volume segmentation.</li>
</ol>
<p>I found the local threshold useful, but it seems that it highlights all slices when the boundaries are set. Is there any way to achieve this in the segmentation editor directly on a slice by slice basis where it resets the thresholding nodes for each slice?</p>
<p>Alternatively, would creating this workflow as a seperate module be a good work around?</p>
<p>I read a few other post about this:<br>
<a href="https://discourse.slicer.org/t/how-to-threshold-only-one-slice-in-the-dicom-module/10602,but">https://discourse.slicer.org/t/how-to-threshold-only-one-slice-in-the-dicom-module/10602,but</a> they were not too helpful for my use case. Would love some insight in tackling this!</p>
<p>Thank you,<br>
tas</p>

---

## Post #2 by @muratmaga (2025-03-18 14:51 UTC)

<aside class="quote no-group" data-username="tas47" data-post="1" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>I found the local threshold useful, but it seems that it highlights all slices when the boundaries are set. Is there any way to achieve this in the segmentation editor directly on a slice by slice basis where it resets the thresholding nodes for each slice?</p>
</blockquote>
</aside>
<p>I don’t think you can have Slicer apply the threshold only in a single slice, that’s a global (3D) operation. You can do something like this: For your current slice, preview and adjust the threshold range visually but instead of apply, hit use for masking and then switch to the paint/draw tool and select the area you would like to apply that threshold in that slice. Then switch to the next slice and repeat the procedure.</p>
<aside class="quote no-group" data-username="tas47" data-post="1" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>Alternatively, would creating this workflow as a seperate module be a good work around?</p>
</blockquote>
</aside>
<p>With python, it should be possible to extract the intensity values from a single slice, and let you choose the cut off values (or automatically calculate the cut off using one of the automated procedures). Though it is integration with segment editor might be a of work.</p>

---

## Post #3 by @tas47 (2025-03-18 17:29 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I don’t think you can have Slicer apply the threshold only in a single slice, that’s a global (3D) operation. You can do something like this: For your current slice, preview and adjust the threshold range visually but instead of apply, hit use for masking and then switch to the paint/draw tool and select the area you would like to apply that threshold in that slice.</p>
</blockquote>
</aside>
<p>For this portion, it really defeats the purpose. I am looking for something more semi-automatic especially with almost 1000 example of annotations needed. The idea is to really avoid using paintbrush for manual segmentation, but rely on local thresholding from roi masks drawn with the brush.</p>
<p>it would be great practice and experience to automate this workflow using a custom module. If paint/brush is able to segment slice by slice, there has to be a way to code   the local thresholding feature per slice node and reset the state each time we jump to another slice?</p>
<p>Would anybody be able to guide me/help in this process?</p>

---

## Post #4 by @muratmaga (2025-03-18 17:56 UTC)

<aside class="quote no-group" data-username="tas47" data-post="3" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>it would be great practice and experience to automate this workflow using a custom module. If paint/brush is able to segment slice by slice, there has to be a way to code the local thresholding feature per slice node and reset the state each time we jump to another slice?</p>
</blockquote>
</aside>
<p>I mean there are many ways of doing this. Here is a chatGPT generated script that will extract the intensity values from an arbitrary slice and will put them into a numpy array that you can get min, max, std, mean, and do all sorts of histogram things to calculate a threshold</p>
<pre><code class="lang-auto">import slicer
import numpy as np

# Use "MRHead" as the volume name
volumeNode = slicer.util.getNode("MRHead")

# Get image data and check if it's valid
imageData = volumeNode.GetImageData()
if not imageData:
    raise ValueError("The volume node does not contain image data.")

# Extract the intensity values from slice index 100
sliceIndex = 100
volumeArray = slicer.util.arrayFromVolume(volumeNode)
if sliceIndex &lt; 0 or sliceIndex &gt;= volumeArray.shape[0]:
    raise ValueError("Slice index out of bounds.")

sliceArray = volumeArray[sliceIndex, :, :]

# Print the slice intensity values
print("Intensity values from slice index 100:")
print(sliceArray)

# get values
sliceArray.mean()
sliceArray.max()
sliceArray.std()
</code></pre>
<p>The point though, unless you have a dataset that is very unique and constructed slice by slice (as opposed to a 3D dataset), the intensity distributions from neighboring slices will be very very similar. So you will have a very complicated workflow with marginal gains (or maybe none).</p>
<p>If you describe what you are trying to do, there might be other options. Manual segmentaiton is too tedious.</p>

---

## Post #5 by @tas47 (2025-03-18 19:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<pre><code class="lang-auto">import slicer
import numpy as np

# Use "MRHead" as the volume name
volumeNode = slicer.util.getNode("MRHead")

# Get image data and check if it's valid
imageData = volumeNode.GetImageData()
if not imageData:
    raise ValueError("The volume node does not contain image data.")

# Extract the intensity values from slice index 100
sliceIndex = 100
volumeArray = slicer.util.arrayFromVolume(volumeNode)
if sliceIndex &lt; 0 or sliceIndex &gt;= volumeArray.shape[0]:
    raise ValueError("Slice index out of bounds.")

sliceArray = volumeArray[sliceIndex, :, :]

# Print the slice intensity values
print("Intensity values from slice index 100:")
print(sliceArray)

# get values
sliceArray.mean()
sliceArray.max()
sliceArray.std()
</code></pre>
</blockquote>
</aside>
<p>I tried this workaround initially, but it doesnt scale, and having a gui to set local threshold boundary based on every slice is very helpful, instead of hard coding every slice instance.</p>
<p>Unfortunately, my dataset is composed of gliomas tumours. The intensities distribution dont often contribute to the same intensities on from neighbouring slices because they aren’t found in every slice. That is why i would need a slice by slice case workflow. Certain also have liquid build up creating artifacts thus being very complex for automatic process. The goal is to eventually use the segmentation as a training set for automatic pipelines.</p>

---

## Post #6 by @muratmaga (2025-03-18 19:54 UTC)

<aside class="quote no-group" data-username="tas47" data-post="5" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>I tried this workaround initially, but it doesnt scale, and having a gui to set local threshold boundary based on every slice is very helpful, instead of hard coding every slice instance.</p>
</blockquote>
</aside>
<p>Setting the GUI right is usually the most complex part of the module development. You will have to look into Slicer development (<a href="https://slicer.readthedocs.io" rel="noopener nofollow ugc">https://slicer.readthedocs.io</a>) or hire someone.</p>
<p>Also your glioma tumors have thousands of slices, what kind of modality is that, histology? If you have thousands of slices in total, but only few slices per volume/specimen, you can potentially import every single slice of a specimen as an individual volume, segment them as individual slices (in this case threshold tool will work) and then programmatically stitch them together. This might be less development effort than creating your custom segmentation tool.</p>

---

## Post #7 by @tas47 (2025-03-18 20:08 UTC)

<p>My apologies, i want to just clarify that they are MRI images each composed about about 20-30 slices per volume with  different orientations. I have a couple hundreds of of MRI images requiring segmentation in a  semi-automatic segmentations.   Hope that clarifies.</p>
<p>Thank you for the tips. Will update on  what works best for me.</p>

---

## Post #8 by @muratmaga (2025-03-18 20:21 UTC)

<aside class="quote no-group" data-username="tas47" data-post="7" data-topic="42195">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tas47/48/78529_2.png" class="avatar"> tas47:</div>
<blockquote>
<p>that they are MRI images each composed about about 20-30 slices per volume with different orientations.</p>
</blockquote>
</aside>
<p>If that’s the case, I would at least do couple manually in the way I describe. import each slice as a separate volume, segment the way you are thinking of with local threshold, and save, and then stitch.</p>
<p>If this workflow does indeed show slice-by-slice segmentation gives you better results, then you can consider automating it somehow.</p>

---

## Post #9 by @tas47 (2025-04-10 20:09 UTC)

<p>Hi everyone,</p>
<p>I managed to generate a function for this issue. The script  takes a volume node, a segmentation node, and a segment  which acts as base ROI/mask. It still needs refinement, but is a good starting point.</p>
<ul>
<li>
<p><strong>Step 1: Manual ROI Creation:</strong> First, create a ‘base’ segment in the Segmentation Editor (e.g., named ‘RoughTumorROI’). Roughly paint/outline the general area of interest on the slices where the structure appears.  This first segment is important because it defines the boundary for where the thresholding will happen on each slice</p>
<p><strong>Step 2: Slice-wise Threshold Application:</strong></p>
</li>
<li>
<p>Navigate to the slice you want to refine in the Red (Axial) view.</p>
</li>
<li>
<p>Go to the Segment Editor’s ‘Threshold’ effect.</p>
<ul>
<li>Adjust the threshold with the threshold slider  or the histogram until the threshold visually highlights the target structure <em>on that specific slice</em> optimally <em>within</em> the area defined by by the base ROI segment.</li>
</ul>
</li>
<li>
<p>Then you paste my function into the Slicer Python console, making sure to provide the correct volume name, segmentation node ID, and the target segment name you want.</p>
</li>
</ul>
<p>The script will automatically read the min/max threshold values  set in the UI and will apply that threshold to the current slice  within the boundaries  (the ROI). It will  then save this result into a new  target segment (it creates the target segment if it doesn’t exist yet, using the geometry from the ROI segment). This can be repeated for each slice we need to adjust the threshold for and will be updated into the target segment.</p>
<p>So far the script only works with the axial (‘Red’) slice view with a numpy thresholding logic.</p>
<pre data-code-wrap="python"><code class="lang-python">
def simple_slice_threshold_to_segmentation(
    volume_name="IM-0012-0001.dcm",
    segmentation_node_id="vtkMRMLSegmentationNode2",
    new_segment_name="ThresholdedSlice"
):
    """
    Thresholds current slice in Red view and creates/updates a new segmentation segment.
    (Refactored to remove all error tracking logic).
    """
    try:
        # ========================================
        # 1. Get or create segmentation node
        # ========================================
        print("Setting up segmentation node...")
        seg_node = slicer.util.getNode(segmentation_node_id)
        if seg_node is None:
            seg_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
            seg_node.SetName(segmentation_node_id)
            print(f"Created new segmentation node: {segmentation_node_id}")
        else:
            print(f"Using existing segmentation node: {segmentation_node_id}")

        # ========================================
        # 2. Get current slice index
        # ========================================
        print("Getting slice index...")
        red_widget = slicer.app.layoutManager().sliceWidget("Red")
        if not red_widget:
            raise RuntimeError("Red slice widget not found")
        red_logic = red_widget.sliceLogic()
        slice_index = red_logic.GetSliceIndexFromOffset(red_logic.GetSliceOffset()) - 1
        print(f"Slice index: {slice_index}")

        # ========================================
        # 3. Get input volume and segmentation
        # ========================================
        print("Loading input nodes...")
        volume = slicer.util.getNode(volume_name)
        # Assuming the input segmentation is the same as the output one initially
        input_seg_node = seg_node

        if not volume:
            raise RuntimeError(f"Volume '{volume_name}' not found")
        if not input_seg_node:
            raise RuntimeError(f"Input segmentation node not found or created")
        print("Found both input nodes")

        # ========================================
        # 4. Extract ROI (using first segment of input_seg_node)
        # ========================================
        print("Extracting ROI...")
        segmentation = input_seg_node.GetSegmentation()
        if not segmentation:
             raise RuntimeError("Segmentation data not found in the input node")
        seg_ids = segmentation.GetSegmentIDs()
        if not seg_ids:
            # If the target segmentation node was newly created, it won't have segments.
            # This logic assumes the *intent* is to use an *existing* segmentation
            # (even if it's the same node name as the output) to define the ROI.
            # If the goal is simply to threshold the *entire* volume slice,
            # the ROI extraction part should be skipped or modified.
            # Raising error as per original logic if no segments define the ROI.
            raise RuntimeError("No segments found in input segmentation to define ROI.")

        # Use the first available segment ID from the input_seg_node
        roi = slicer.util.arrayFromSegmentBinaryLabelmap(input_seg_node, seg_ids[0], volume)
        ref_vol = slicer.util.arrayFromVolume(volume)
        extracted = np.where(roi, ref_vol, 0)
        print("ROI extracted")

        # ========================================
        # 5. Threshold current slice
        # ========================================
        print("Thresholding slice...")
        # Get threshold values from Segment Editor
        segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
        threshEffect = segmentEditorWidget.effectByName("Threshold")
        min_threshold=float(threshEffect.parameter("MinimumThreshold"))
        max_threshold=float(threshEffect.parameter("MaximumThreshold"))

        current_slice = extracted[slice_index, :, :]
        mask_slice = ((current_slice &gt;= min_threshold) &amp;
                  (current_slice &lt;= max_threshold)).astype(np.uint8)
        print("Thresholding complete")

        # ========================================
        # 6. Create/update new segment in the output seg_node
        # ========================================
        print("Creating/updating new segment...")
        output_segmentation = seg_node.GetSegmentation() # Use the output node's segmentation
        if not output_segmentation:
             raise RuntimeError("Segmentation data not found in the output node before creating/updating segment")

        new_segment_id = output_segmentation.GetSegmentIdBySegmentName(new_segment_name)
        if new_segment_id == '':
            # Create a new segment if it doesn't exist
            new_segment_id = output_segmentation.AddEmptySegment(new_segment_name)
            print(f"New segment '{new_segment_name}' created with ID: {new_segment_id}")

            # Get labelmap from the *first segment* of the *input* node to copy its structure/mask
            # Ensure seg_ids is not empty (checked in step 4)
            first_segment_labelmap = slicer.util.arrayFromSegmentBinaryLabelmap(input_seg_node, seg_ids[0], volume)
            # Copy the labelmap structure to the new segment in the output node
            slicer.util.updateSegmentBinaryLabelmapFromArray(first_segment_labelmap, seg_node, new_segment_id, volume)
            print("Labelmap structure copied to new segment")
        else:
            print(f"Using existing segment '{new_segment_name}' with ID: {new_segment_id}")

        # Get the labelmap of the new segment (from the output node)
        new_segment_labelmap = slicer.util.arrayFromSegmentBinaryLabelmap(seg_node, new_segment_id, volume)

        # Check if the slice actually needs updating
        if not np.array_equal(new_segment_labelmap[slice_index, :, :], mask_slice):
            new_segment_labelmap[slice_index, :, :] = mask_slice
            # Save the updated labelmap back to the segment
            slicer.util.updateSegmentBinaryLabelmapFromArray(new_segment_labelmap, seg_node, new_segment_id, volume)
            print("New segment labelmap updated with thresholded slice")
        else:
            print("Thresholded slice is identical to the existing slice in the new segment; no update needed.")

        print("\nFunction completed successfully.")

    except Exception as e:
        # Basic error reporting without line tracking
        print(f"\n--- ERROR ---")
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc() # Print full traceback for debugging
        # Optionally re-raise if needed outside this function
        # raise

# Example usage (ensure Slicer environment is running)
# simple_slice_threshold_to_segmentation_no_tracking()

</code></pre>
<ol>
<li>
<p><strong>Current Limitations:</strong></p>
<ul>
<li>Currently, the script only reads the slice index from the ‘Red’ (Axial) view.</li>
<li>Requires pasting into the Python console for each slice.</li>
<li>Relies on having a ‘base ROI’ segment already created."</li>
<li>Requires the Segment Editor module and Threshold effect to be active/available to read parameters."</li>
</ul>
</li>
</ol>

---
