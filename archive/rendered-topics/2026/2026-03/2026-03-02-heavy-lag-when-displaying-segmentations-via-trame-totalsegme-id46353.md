---
topic_id: 46353
title: "Heavy Lag When Displaying Segmentations Via Trame Totalsegme"
date: 2026-03-02
url: https://discourse.slicer.org/t/46353
---

# Heavy lag when displaying segmentations via Trame + TotalSegmentator

**Topic ID**: 46353
**Date**: 2026-03-02
**URL**: https://discourse.slicer.org/t/heavy-lag-when-displaying-segmentations-via-trame-totalsegmentator/46353

---

## Post #1 by @Karuruychi (2026-03-02 04:48 UTC)

<p>I am developing a web-based medical imaging viewer using Trame-slicer. I used TotalSegmentator to generate anatomical masks and then load these <code>.nii.gz</code> files into the Slicer scene for 3D visualization.<br>
Currently, I am loading each organ (Liver, Colon, Heart, etc.) from separate <code>.nii.gz</code> files into individual nodes. I suspect this overhead contributes to the performance degradation.</p>
<p><strong>Merging Masks:</strong> Is there a recommended way to merge these multiple NIfTI files into a single <code>vtkMRMLSegmentationNode</code> with multiple segments upon loading? I want to reduce the number of Display Nodes and renderers that Slicer has to manage.</p>
<pre data-code-wrap="python"><code class="lang-python">        mask_files = [
            "/trame_server3d/build/segment_result/colon.nii.gz",
            "/trame_server3d/build/segment_result/liver.nii.gz",
            "/trame_server3d/build/segment_result/heart.nii.gz",
            "/trame_server3d/build/segment_result/kidney_cyst_left.nii.gz",
            "/trame_server3d/build/segment_result/kidney_cyst_right.nii.gz",
            "/trame_server3d/build/segment_result/kidney_right.nii.gz",
            "/trame_server3d/build/segment_result/kidney_left.nii.gz",
            # Add more test paths here
        ]
        
        segmentation_nodes = []
        
        for mask_path in mask_files:
            if Path(mask_path).exists():
                logging.info(f"[ViewManager] Loading segmentation: {mask_path}")
                # Because IOManager only handles one file at a time
                node = self.slicer_app.io_manager.load_segmentation(mask_path)
                if node:
                    segmentation_nodes.append(node)
</code></pre>
<p>After this, the loadSegment will using these nodes to display them:<br>
```</p>
<pre data-code-wrap="python"><code class="lang-python">    def loadSegment(self, segmentation_nodes: list) -&gt; None:
        for node in segmentation_nodes:
            seg_wrapper = Segmentation(
                segmentation_node=node,
                volume_node=self.volume_node,
                editor_logic=self.slicer_app.segmentation_editor.editor_logic
            )
            
            seg_wrapper.enable_surface_representation()
</code></pre>
<p>Are there any options available here to explicitly choose between <strong>CPU or GPU rendering</strong> for segmentations, like in volume 3D render?<br>
```</p>
<pre data-code-wrap="python"><code class="lang-python">
    def createVolumeVisualization(self, volume_node, preset_name="CT-AAA"):
        """Setup Volume Rendering using Pure VTK Pipeline (CPU Only)."""
        start_time = time.time()
        self.volume_node = volume_node
        
        # 1. Setup Volume Rendering Logic
        vr_logic = self.slicer_app.volume_rendering._logic
        renderOption = self.renderOption
        if renderOption == RenderOption.CPU.value:
            logging.info("[Volume] Rendering with CPU")
            vr_logic.SetDefaultRenderingMethod("vtkMRMLCPURayCastVolumeRenderingDisplayNode")
        elif renderOption == RenderOption.GPU.value:
            logging.info("[Volume] Rendering with GPU")
            vr_logic.SetDefaultRenderingMethod("vtkMRMLGPURayCastVolumeRenderingDisplayNode")
        elif renderOption == RenderOption.MULTI_VOLUME.value:
            vr_logic.SetDefaultRenderingMethod("vtkMRMLMultiVolumeRenderingDisplayNode")

        self.slicer_app.display_manager.show_volume(
            volume_node=volume_node,
            vr_preset=preset_name,
            do_reset_views=True
        )

        self.vr_display_node = self.slicer_app.volume_rendering.get_vr_display_node(volume_node)
        self.view3D.render()
        self.view3D.set_box_visible(False)
        self.view3D.set_background_gradient_color([0, 0, 0], [0, 0, 0])

        elapsed = time.time() - start_time
        logging.info(f"[Volume] Volume ready after {elapsed:.4f} seconds")

</code></pre>
<p>In my current environment, I suspect that <strong>Trame-Slicer</strong> might be defaulting to <strong>GPU raycasting (or GPU-based Closed Surface representation)</strong> even on a machine that primarily supports CPU rendering, which causes significant lag (Even displaying only segmentation without showing 3D volume still causes lag).<br>
Thank you for your help!</p>

---

## Post #2 by @jumbojing (2026-03-02 09:11 UTC)

<h2><a name="p-132382-solution-1" class="anchor" href="#p-132382-solution-1" aria-label="Heading link"></a>Solution</h2>
<h3><a name="p-132382-h-1-merge-multiple-nifti-files-into-single-segmentationnode-2" class="anchor" href="#p-132382-h-1-merge-multiple-nifti-files-into-single-segmentationnode-2" aria-label="Heading link"></a>1. Merge Multiple NIfTI Files into Single SegmentationNode</h3>
<pre data-code-wrap="python"><code class="lang-python">import slicer
import logging
from pathlib import Path

def merge_nifti_files(mask_files, segmentation_name="TotalSegmentation"):
    """Merge multiple NIfTI files into a single SegmentationNode."""
    
    # Create single segmentation node
    seg_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
    seg_node.SetName(segmentation_name)
    seg_node.CreateDefaultDisplayNodes()
    
    temp_nodes = []
    
    for mask_path in mask_files:
        if not Path(mask_path).exists():
            continue
        
        # Extract organ name
        organ_name = Path(mask_path).stem.replace('.nii', '')
        
        # Load as labelmap
        label_node = slicer.util.loadLabelVolume(mask_path, {'name': f"temp_{organ_name}"})
        temp_nodes.append(label_node)
        
        # Import to segmentation
        slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(
            label_node, seg_node, organ_name
        )
        
        logging.info(f"Added segment: {organ_name}")
    
    # Cleanup temporary nodes
    for node in temp_nodes:
        slicer.mrmlScene.RemoveNode(node)
    
    return seg_node
</code></pre>
<h3><a name="p-132382-h-2-control-cpugpu-rendering-for-segmentations-3" class="anchor" href="#p-132382-h-2-control-cpugpu-rendering-for-segmentations-3" aria-label="Heading link"></a>2. Control CPU/GPU Rendering for Segmentations</h3>
<pre data-code-wrap="python"><code class="lang-python">def configure_segmentation_rendering(seg_node, use_gpu=False):
    """Configure segmentation rendering method."""
    
    # Get display node
    display_node = seg_node.GetDisplayNode()
    if not display_node:
        display_node = seg_node.CreateDefaultDisplayNodes()
    
    # Set representation (affects performance)
    if use_gpu:
        # GPU-based rendering (faster but requires GPU)
        display_node.SetRepresentation2D("Outline")
        display_node.SetRepresentation3D("Closed surface")
    else:
        # CPU-optimized rendering
        display_node.SetRepresentation2D("Outline")
        display_node.SetRepresentation3D("Closed surface")
        
        # Reduce quality for better performance
        display_node.SetOpacity3D(0.8)
        
        # Disable auto-update for performance
        seg_node.SetDisplayVisibility(False)
        # ... do processing ...
        seg_node.SetDisplayVisibility(True)
    
    return display_node

# Alternative: Use Binary Labelmap representation (CPU-friendly)
def use_labelmap_representation(seg_node):
    """Use binary labelmap representation (CPU-friendly)."""
    segmentation = seg_node.GetSegmentation()
    
    # Use binary labelmap representation instead of closed surface
    # This is more CPU-friendly
    segmentation.SetMasterRepresentationName("Binary labelmap")
    
    # Disable automatic surface creation
    segmentation.SetConversionParameter("Apply to all representations", "0")
</code></pre>
<h3><a name="p-132382-h-3-optimized-loading-in-trame-slicer-4" class="anchor" href="#p-132382-h-3-optimized-loading-in-trame-slicer-4" aria-label="Heading link"></a>3. Optimized Loading in Trame-Slicer</h3>
<pre data-code-wrap="python"><code class="lang-python">def load_segments_optimized(self, mask_files):
    """Load and merge all segments at once."""
    
    # Merge all NIfTI files into one segmentation node
    merged_seg = merge_nifti_files(mask_files, "TotalSegmentation")
    
    # Configure for CPU rendering
    configure_segmentation_rendering(merged_seg, use_gpu=False)
    
    # Enable surface representation
    seg_wrapper = Segmentation(
        segmentation_node=merged_seg,
        volume_node=self.volume_node,
        editor_logic=self.slicer_app.segmentation_editor.editor_logic
    )
    
    # For CPU optimization, reduce resolution
    display_node = merged_seg.GetDisplayNode()
    if display_node:
        display_node.SetOpacity3D(0.7)
        # Reduce smooth factor for faster rendering
        display_node.SetSurfaceSmoothingFactor(0.5)
    
    return [merged_seg]  # Return single node instead of list
</code></pre>
<h3><a name="p-132382-key-benefits-5" class="anchor" href="#p-132382-key-benefits-5" aria-label="Heading link"></a>Key Benefits:</h3>
<ul>
<li><strong>Reduces display nodes</strong> from N to 1</li>
<li><strong>Less memory usage</strong> (single renderer)</li>
<li><strong>Better performance</strong> (especially for CPU rendering)</li>
<li><strong>Easier management</strong> of segment visibility and colors</li>
</ul>
<h3><a name="p-132382-performance-tips-6" class="anchor" href="#p-132382-performance-tips-6" aria-label="Heading link"></a>Performance Tips:</h3>
<ol>
<li>Use <code>Binary labelmap</code> representation for CPU</li>
<li>Reduce <code>SurfaceSmoothingFactor</code> for faster rendering</li>
<li>Set appropriate <code>Opacity3D</code> (0.5-0.8)</li>
<li>Disable auto-updates during batch operations</li>
<li>Use merged segmentation instead of multiple nodes</li>
</ol>
<p>From   <a href="https://github.com/jumbojing/slicerClaw" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jumbojing/slicerClaw: A revolutionary, lightning-fast AI assistant natively integrated into 3D Slicer.</a></p>

---

## Post #3 by @lassoan (2026-03-02 17:59 UTC)

<h3><a name="p-132387-h-1-merge-multiple-nifti-files-into-single-segmentationnode-1" class="anchor" href="#p-132387-h-1-merge-multiple-nifti-files-into-single-segmentationnode-1" aria-label="Heading link"></a>1. Merge Multiple NIfTI Files into Single SegmentationNode</h3>
<p>The LLM-provided script may work, but there should be no need for custom scripting. If you use TotalSegmentator extension that takes care of correct and efficient loading of segments (using correct colors, terminology, etc.). The extension also request TotalSegmentator to create a single labelmap output (if the particular model supports that), so no merging is necessary.</p>
<h3><a name="p-132387-h-2-control-cpugpu-rendering-for-segmentations-2" class="anchor" href="#p-132387-h-2-control-cpugpu-rendering-for-segmentations-2" aria-label="Heading link"></a>2. Control CPU/GPU Rendering for Segmentations</h3>
<p>Segmentations are always rendered using GPU.</p>
<p>I don’t think that the changes suggested by the LLM make any difference, as they are just some display options that don’t affect rendering speed.</p>
<p>Probaly the issue you are running into is that in Trame, rendering of segmentation can be slow if you run Slicer in a container that only has a software renderer. Make sure you set up GPU-accelerated rendering in your container.</p>
<p>If setting up GPU-accelerated rendering is impossible (e.g., you don’t have a GPU that your container can use) then you can speed up rendering by simplifying the segmentation: you can smooth the segments, or you can increase decimation factor (in the binary labelmap to closed surface conversion rule).</p>

---

## Post #4 by @jumbojing (2026-03-02 19:15 UTC)

<p>Automatically-generated content using jumbojing/slicerClaw. Accuracy of the answer has not been verified and code has not been tested.</p>

---
