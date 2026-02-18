# LungCTAnalyzer does not segment tumor/cancer nodule

**Topic ID**: 31125
**Date**: 2023-08-13
**URL**: https://discourse.slicer.org/t/lungctanalyzer-does-not-segment-tumor-cancer-nodule/31125

---

## Post #1 by @A_By (2023-08-13 14:13 UTC)

<p>I could not get LungCTAnalyzer to segmentate tumors.<br>
Is there any solution or other tools I can manage this?<br>
Thank You</p>

---

## Post #2 by @rbumm (2023-08-13 15:02 UTC)

<p>Currently, there isn’t an automated tool specifically for lung tumor segmentation. However, you can utilize the “Local Threshold” effect in the Segment Editor, which employs the Grow Cut algorithm. To do this, select the tumor segment and CTRL-left click within the tumor for manual segmentation. Considering the rapid advancements in the field, it’s anticipated that AI models for lung tumor segmentation will be available in the near future.</p>

---

## Post #3 by @A_By (2023-08-13 15:22 UTC)

<p>Thank you for your answer.<br>
Is there any way to automate/auto segment tumors? Will MONAILabel work for this?</p>

---

## Post #4 by @rbumm (2023-08-13 15:29 UTC)

<p>MonaiLabel is certainly an option to train a U-Net for tumor segmentation.<br>
Apart from that there is a <a href="https://monai.io/model-zoo.html">nodule segmentation tool</a> in the MONAI Model Zoo that I have personally tried. It is working but must probably be trained for better results.</p>

---
