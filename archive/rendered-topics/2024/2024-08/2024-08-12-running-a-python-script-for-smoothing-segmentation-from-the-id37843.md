# Running a Python script for smoothing segmentation from the terminal

**Topic ID**: 37843
**Date**: 2024-08-12
**URL**: https://discourse.slicer.org/t/running-a-python-script-for-smoothing-segmentation-from-the-terminal/37843

---

## Post #1 by @ruili (2024-08-12 13:10 UTC)

<p>Hello,</p>
<p>I have the following script that smooths a binary segmentation using the Joint Taubin method from slicer. Suppose this script is saved at <code>smoothing.py</code>, I am calling it with this command: <code>path/to/slicer --no-splash --python-script smoothing.py -mask path/to/mask -volume path/to/volume -output path/to/output</code>. This will open the slicer software and does the job properly.</p>
<p>However, ideally I want to run it without opening the slicer window. I tried adding the <code>--no-main-window</code> flag, but then it simply does not do the smoothing and no output is generated. I’m wondering if any of the functions I am using in this script requires the slicer main window to be open to work? Help will be very much appreciated!</p>
<pre><code class="lang-auto">import slicer
import argparse

def smooth_mask(mask_path, volume_path, output_path):
    slicer.util.showStatusMessage("Loading files")
    segmentationNode = slicer.util.loadSegmentation(mask_path)
    masterVolumeNode = slicer.util.loadVolume(volume_path)

    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(masterVolumeNode)

    # Smoothing
    slicer.util.showStatusMessage("Smoothing LSA PA mask")
    segmentEditorWidget.setActiveEffectByName("Smoothing")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("SmoothingMethod", "JOINT_TAUBIN")
    effect.setParameter("JointTaubinSmoothingFactor", 0.5)
    effect.self().onApply()

    # Clean up
    segmentEditorWidget = None
    slicer.mrmlScene.RemoveNode(segmentEditorNode)

    # Export segmentation to a labelmap
    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)
    slicer.util.saveNode(labelmapVolumeNode, output_path)
    slicer.util.showStatusMessage("Saved smoothed LSA PA mask")
    return None



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-mask', help='Path to a binary segmentation mask')
    parser.add_argument('-volume', help='Path to the master volume that the segmentation corresponds to')
    parser.add_argument('-output', help='Path to save output mask')

    args = parser.parse_args()
    smooth_mask(args.mask, args.volume, args.output)
</code></pre>

---

## Post #2 by @pieper (2024-08-12 15:06 UTC)

<p>You could make this work by avoiding using the module widget so you don’t need the main window, but a simple workaround could be to add this to your script:</p>
<p><code>slicer.util.mainWindow().showMinimized()</code></p>

---

## Post #3 by @ruili (2024-08-20 12:36 UTC)

<p>Sorry for my late reply. I added the suggested line of code to the beginning of the <code>smooth_mask</code> function, but it did not actually prevent the window of slicer from popping up. Nothing seemed to change. I was running the script on a mac machine. Do you know by any chance how I may fix this?</p>

---

## Post #4 by @pieper (2024-08-20 13:32 UTC)

<p>You may need to call <code>slicer.app.processEvents()</code> if you are running from a script that never uses the GUI.</p>

---

## Post #5 by @ruili (2024-08-20 14:28 UTC)

<p>Yes, I am actually just running the script from terminal. May I ask where in the script should this line of code be called?</p>

---

## Post #6 by @pieper (2024-08-20 15:06 UTC)

<p>Try calling it after calling the <code>showMinimized()</code> method.</p>

---

## Post #7 by @ruili (2024-08-20 20:08 UTC)

<p>That successfully suppressed the main window of slicer. Thank you! The only problem remaining was that it couldn’t stop the pop-up window when loading the files like this one below. Do you know any quick fix for this as well? If not, it is completely fine as well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b0d1309db4a5e097255f20b5c39b34200da0aa.png" data-download-href="/uploads/short-url/xlk4W0DdyOQA2sPcAQ0wwxf6lIe.png?dl=1" title="Screenshot 2024-08-20 at 21.00.40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b0d1309db4a5e097255f20b5c39b34200da0aa_2_690x94.png" alt="Screenshot 2024-08-20 at 21.00.40" data-base62-sha1="xlk4W0DdyOQA2sPcAQ0wwxf6lIe" width="690" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b0d1309db4a5e097255f20b5c39b34200da0aa_2_690x94.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b0d1309db4a5e097255f20b5c39b34200da0aa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b0d1309db4a5e097255f20b5c39b34200da0aa.png 2x" data-dominant-color="B0AFB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-20 at 21.00.40</span><span class="informations">691×95 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @pieper (2024-08-20 20:52 UTC)

<p>No, I think that one is hard coded.</p>

---
