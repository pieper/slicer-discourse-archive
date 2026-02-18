# Is my segmentation not registering to image (source geometry) properly?

**Topic ID**: 42053
**Date**: 2025-03-10
**URL**: https://discourse.slicer.org/t/is-my-segmentation-not-registering-to-image-source-geometry-properly/42053

---

## Post #1 by @brianwskim (2025-03-10 13:06 UTC)

<p><strong>Operating system:</strong> MacOS Sequioa 15.3.1 (24D70)<br>
<strong>Slicer version:</strong> 5.8.0<br>
<strong>Expected behavior:</strong> Image (NIfTI) and segmentation affine matrices to match after exporting segmentation to binary labelmap and saving to file (as NIfTI)<br>
<strong>Actual behavior:</strong> If I use nibabel (nib.load) and check the image and segmentation file data (get_fdata), there is a warning that affines are ill-posed on some but not all segmentation files.</p>
<p>This leads to these particular images’ performance metrics being incorrectly calculated (for example, Dice score become &lt;0.01 but when viewing the the ground truth segmentation and new segementation in Slicer, they overlap near perfectly). Code for Dice is:</p>
<pre><code class="lang-auto">import warnings
import numpy as np
import nibabel as nib
def compute_confusion_matrix(gt_class, seg_class):
    if gt_class.shape != seg_class.shape:
        raise ValueError("Ground truth and segmentation masks must have the same shape.")
    
    # Optimise memory by storing binary label values as integers
    gt_class = gt_class.astype(np.uint8)
    seg_class = seg_class.astype(np.uint8)

    tp = np.sum(gt_class * seg_class, dtype=np.float32)
    fp = np.sum((1 - gt_class) * seg_class, dtype=np.float32)
    tn = np.sum((1 - gt_class) * (1 - seg_class), dtype=np.float32)
    fn = np.sum(gt_class * (1 - seg_class), dtype=np.float32)
    
    # Replace zero values with a tiny number to avoid errors
    tiny_number = 1e-10
    tp = tp if tp != 0 else tiny_number
    fp = fp if fp != 0 else tiny_number
    tn = tn if tn != 0 else tiny_number
    fn = fn if fn != 0 else tiny_number
    
    return {"tp": tp, "fp": fp, "tn": tn, "fn": fn}

def dsc(conf_matrix):
    numerator = 2 * conf_matrix["tp"]
    denominator = 2 * conf_matrix["tp"] + conf_matrix["fp"] + conf_matrix["fn"]
    if denominator == 0:
        warnings.warn("Both gt and s are empty - set to 1 as correct solution even if not defined")
        return 1
    return numerator / denominator```

**Attempted solutions:**
1. Loaded image (as volume) and segmentation (as segmentation) --&gt; Segment Editor --&gt; Chose image as 'Source Volume' --&gt; Click Specify Geometry --&gt; Select image as 'Source Geometry'.
2. Python (3.9), forcing assignment seg.affine = img.affine, set sform code=4, set qform code=4</code></pre>

---

## Post #2 by @pieper (2025-03-10 17:47 UTC)

<p>You’ll find lots of examples where nifii format is ambiguous and hard to use.  If you can switch to nrrd you are likely to have better luck.  If you investigate and find any bugs in the way Slicer handles nifti (and convincing evidence that there is an unambiguous “correct” way to handle do things in nifti) then we’d consider changes.  You can search the forum here or ask a chatbot about why nifti can be problematic.</p>

---

## Post #3 by @brianwskim (2025-03-13 22:17 UTC)

<p>Hi Steve,<br>
I’m consistently amazed at how responsive and supportive the Slicer team is.<br>
I agree. I feel I may just convert all DICOM to NRRD instead and go from there.</p>

---
