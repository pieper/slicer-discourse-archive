---
topic_id: 34991
title: "Custom Color Table At Specified Thresholds"
date: 2024-03-20
url: https://discourse.slicer.org/t/34991
---

# Custom Color Table at Specified Thresholds

**Topic ID**: 34991
**Date**: 2024-03-20
**URL**: https://discourse.slicer.org/t/custom-color-table-at-specified-thresholds/34991

---

## Post #1 by @edwardwang1 (2024-03-20 14:33 UTC)

<p>Hello,</p>
<p>I am trying to create a color table to display isodoses for an RT dose. I want the thresholds to be at percentages of the maximum value in the dose volume (i.e. 10%, 20%, etc). Following an example in the script repository, I have been successful in creating a custom color node:</p>
<pre><code class="lang-auto">   maxDose = 100
   customColorNode = slicer.vtkMRMLColorTableNode()
    #
    # # Define percentage intervals
    thresholds = [0.2, 0.5, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    colorRGB = [(263, 100, 76),
                (0, 237, 255),
                (46, 255, 0),
                (255, 224, 0),
                (255, 109, 0),
                (255, 58, 0),
                (26, 238, 153),
                (91, 255, 73)]

    customColorNode.SetTypeToUser()
    customColorNode.SetNumberOfColors(len(thresholds))
    customColorNode.SetName("CustomGANColorNode")

    for i in range(len(thresholds)):
      customColorNode.SetColor(i, colorRGB[i][0] / 255, colorRGB[i][1] / 255, colorRGB[i][2] / 255)

    slicer.mrmlScene.AddNode(customColorNode)
</code></pre>
<p>However, I am not sure how to specify the thresholds corresponding to each colour. By default, it seems that the colors corresponding to values in increments of 10. I have gone through the ‘classvtkMRMLColorTableNode’ documentation, but haven’t found any methods that would allow me to set thresholds. Any help is appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @edwardwang1 (2024-03-27 16:47 UTC)

<p>I was able to create a custom colour table by cloning “Isodose_Colortable_Relative”, and adding new thresholds. Then, in my script I simply import the table, and apply it to my dose volume.</p>
<pre><code class="lang-auto"># Color table file Isodose_ColorTable_RelativeCustom.ctbl
# 9 values
0 5 74 0 193 0
1 20 0 237 255 51
2 35 46 255 0 51
3 50 255 224 0 51
4 75 255 109 0 51
5 80 255 58 0 51
6 85 26 238 153 51
7 90 91 255 73 51
8 95 255 0 132 255
</code></pre>
<p>There doesn’t seem to be a flag within the colortable file that specifies whether the thresholds should be treated as absolute or relative values, so perhaps that it’s the “Relative” in the title?</p>

---
