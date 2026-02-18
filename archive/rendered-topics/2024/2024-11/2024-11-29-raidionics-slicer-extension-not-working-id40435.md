# Raidionics-Slicer extension not working

**Topic ID**: 40435
**Date**: 2024-11-29
**URL**: https://discourse.slicer.org/t/raidionics-slicer-extension-not-working/40435

---

## Post #1 by @anuragp2018 (2024-11-29 06:06 UTC)

<p>I tried running the Neuro LGG PreOp segmentation model in Raidionics slicer extension, but when clicking on Run the segmentation, the method never finishes and the following error shows in the python console:</p>
<p>[Python] Traceback (most recent call last):<br>
[Python] File “D:\Raidionics-Slicer-master\Raidionics-Slicer-master\Raidionics\Raidionics\src\gui\Segmentation\ModelsExecutionWidget.py”, line 219, in on_interactive_slider_moved<br>
[Python] if current_class not in list(RaidionicsLogic.getInstance().output_raw_values.keys()):<br>
[Python] AttributeError: ‘RaidionicsLogic’ object has no attribute ‘output_raw_values’</p>

---
