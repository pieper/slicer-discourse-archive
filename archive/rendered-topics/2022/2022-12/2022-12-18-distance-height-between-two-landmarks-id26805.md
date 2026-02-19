---
topic_id: 26805
title: "Distance Height Between Two Landmarks"
date: 2022-12-18
url: https://discourse.slicer.org/t/26805
---

# Distance (height) between two landmarks

**Topic ID**: 26805
**Date**: 2022-12-18
**URL**: https://discourse.slicer.org/t/distance-height-between-two-landmarks/26805

---

## Post #1 by @EinatKe (2022-12-18 15:57 UTC)

<p>Hello, I am new to 3D Slicer. sorry if this question was asked before.<br>
I have transform the volume (inside the original ORI)  to align with the Frankfurt plane. I want to calculate distances between landmarks, and I can get he direct distance via 1. right click on two landmarks, 2. export to excel and calculate (in R) with the Euclidean formula.<br>
Now I would like to get the <strong>height</strong> between the points (in the figure here: the distance between the two white dots of the ORI) … how can I get the reference to the axis? is there an easy way to get this value?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc018be3a821a5874683b0c00a909b305baeb8c.jpeg" data-download-href="/uploads/short-url/1ONihjbXrXB9Z5Lfrdjrdoa8K2U.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cc018be3a821a5874683b0c00a909b305baeb8c_2_665x500.jpeg" alt="image" data-base62-sha1="1ONihjbXrXB9Z5Lfrdjrdoa8K2U" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cc018be3a821a5874683b0c00a909b305baeb8c_2_665x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc018be3a821a5874683b0c00a909b305baeb8c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc018be3a821a5874683b0c00a909b305baeb8c.jpeg 2x" data-dominant-color="6E6D77"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×741 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you in advance, Einat</p>

---

## Post #2 by @lassoan (2022-12-18 17:21 UTC)

<p>You can get the size of the ROI by typing this into the Python console:</p>
<pre><code class="lang-python">getNode('Volume rendering ROI').GetSize()
</code></pre>
<p>You can write a few-line Python script that collects all measurements from the scene and writes it into a CSV file that you can load into Excel. I would recommend the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab bootcamp Slicer programming tutorial</a> to get started If you need help then you can always ask us here.</p>

---

## Post #3 by @EinatKe (2022-12-19 06:06 UTC)

<p>Thank you Andras. I typed the python code and received the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f4f431ff026813b248c23892c551cb8a75423a.png" data-download-href="/uploads/short-url/5HtqP2idv9A7yMOR4PaZhiabetQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f4f431ff026813b248c23892c551cb8a75423a_2_690x332.png" alt="image" data-base62-sha1="5HtqP2idv9A7yMOR4PaZhiabetQ" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f4f431ff026813b248c23892c551cb8a75423a_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f4f431ff026813b248c23892c551cb8a75423a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f4f431ff026813b248c23892c551cb8a75423a.png 2x" data-dominant-color="ACABAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">977×471 72.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
what is the difference between these coordinates to those in the Control Point  section?<br>
Einat<br>
** I’ve figure it!<br>
the code gives the actual size in mm of each ROI face and the Control Point  is the location of the ROI middle  point<br>
I’ll go to the tutorial to learn more,<br>
Thank you.</p>

---

## Post #4 by @lassoan (2022-12-19 06:19 UTC)

<p>There is one control point, in the center of the ROI. You can get coordinates of the bounding box corners by adding/subtracting half of the ROI size to the center point coordinates.</p>

---

## Post #5 by @EinatKe (2022-12-19 09:28 UTC)

<p>I was trying to run the code from the python Interactor directly to get the data I need from one of my samples. So instead of coping the <strong>Pre-populate the scene with measurements code</strong> I added a line to define lineNode:</p>
<blockquote>
<blockquote>
<blockquote>
<p>lineNode=[‘Sinuses_LM_template’, ‘Skull_LM_template’, ‘Volume rendering ROI’]<br>
but I got: <strong>Copied 0 length measurements to the clipboard</strong><br>
so I added dummy length measurement ‘L’, cause I thought maybe the code fits only for ‘lengths’, but still I got the same message.<br>
Is there any way I can use this code to retrieve the landmark set ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5916034251ba5ba4a5bf0b19a7d13d780156361d.png" data-download-href="/uploads/short-url/cI5EJekCPHl96RTBLG8C2NbN4PH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5916034251ba5ba4a5bf0b19a7d13d780156361d.png" alt="image" data-base62-sha1="cI5EJekCPHl96RTBLG8C2NbN4PH" width="690" height="436" data-dominant-color="F3F4FE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×562 27.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d19a3ae08166f804c59576918fa7aa0d54e06d83.png" alt="image" data-base62-sha1="tUee6HqZmzi0gIzF7fzlbh9thPt" width="545" height="177"></p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #6 by @lassoan (2022-12-19 14:42 UTC)

<p>The code looks about OK (other than the <code>lineNode</code> list is unnecessary) but I cannot have a closer look because the code is in a screenshot. Could you please copy the code here as text?</p>

---

## Post #7 by @EinatKe (2022-12-21 10:40 UTC)

<p>Hi,<br>
this is the code:</p>
<pre><code class="lang-auto">lineNode=['Sinuses_LM_template', 'Skull_LM_template', 'Volume rendering ROI','L']
def copyLineMeasurementsToClipboard():
  measurements = []
  # Collect all line measurements from the scene
  lineNodes = getNodesByClass('vtkMRMLMarkupsLineNode')
  for lineNode in lineNodes:
    # Get node filename that the length was measured on
    try:
      volumeNode = slicer.mrmlScene.GetNodeByID(lineNode.GetNthControlPointAssociatedNodeID(0))
      imagePath = volumeNode.GetStorageNode().GetFileName()
    except:
      imagePath = ''
    # Get line node n
    measurementName = lineNode.GetName()
    # Get length measurement
    lineNode.GetMeasurement('length').SetEnabled(True)
    length = str(lineNode.GetMeasurement('length').GetValue())
    # Add fields to results
    measurements.append('\t'.join([imagePath, measurementName, length]))
  # Copy all measurements to clipboard (to be pasted into Excel)
  slicer.app.clipboard().setText("\n".join(measurements))
  slicer.util.delayDisplay(f"Copied {len(measurements)} length measurements to the clipboard.")

shortcut2 = qt.QShortcut(slicer.util.mainWindow())
shortcut2.setKey(qt.QKeySequence("Ctrl+Shift+m"))
shortcut2.connect( 'activated()', copyLineMeasurementsToClipboard)

f = open("demofile2.txt", "a")
f.write(lineNode)
f.close()
</code></pre>

---

## Post #8 by @lassoan (2022-12-22 17:39 UTC)

<p>You can create a set of line nodes with predefined names with a keyboard shortcut (Ctrl+Shift+N):</p>
<pre><code class="lang-python">def addLineNodes():
  lineNodeNames = ['Sinuses_LM_template', 'Skull_LM_template', 'Volume rendering ROI', 'L']
  for lineNodeName in lineNodeNames:
    slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", lineNodeName)

shortcut1 = qt.QShortcut(slicer.util.mainWindow())
shortcut1.setKey(qt.QKeySequence("Ctrl+Shift+n"))
shortcut1.connect( 'activated()', addLineNodes)
</code></pre>
<p>Once the line are added, you can go to Markups module, select one, then activate place mode on the toolbar to place the endpoint of that line.</p>
<p>Once your added all the measurements, you can add the results to a file with a keyboard shortcut (Ctrl+Shift+M):</p>
<pre><code class="lang-python">def copyLineMeasurementsToClipboard():
  measurements = []
  # Collect all line measurements from the scene
  lineNodes = getNodesByClass('vtkMRMLMarkupsLineNode')
  for lineNode in lineNodes:
    if lineNode.GetNumberOfDefinedControlPoints() &lt; 2:
      # incomplete line, skip it
      continue
    # Get node filename that the length was measured on
    try:
      volumeNode = slicer.mrmlScene.GetNodeByID(lineNode.GetNthControlPointAssociatedNodeID(0))
      imagePath = volumeNode.GetStorageNode().GetFileName()
    except:
      imagePath = ''
    # Get line node n
    measurementName = lineNode.GetName()
    # Get length measurement
    lineNode.GetMeasurement('length').SetEnabled(True)
    length = str(lineNode.GetMeasurement('length').GetValue())
    # Add fields to results
    measurements.append('\t'.join([imagePath, measurementName, length]))
  # Add all measurements to file
  with open("c:/tmp/demofile2.csv", "a") as f:
    f.write("\n".join(measurements) + "\n")
  slicer.util.delayDisplay(f"Copied {len(measurements)} length measurements to the clipboard.")

shortcut2 = qt.QShortcut(slicer.util.mainWindow())
shortcut2.setKey(qt.QKeySequence("Ctrl+Shift+m"))
shortcut2.connect( 'activated()', copyLineMeasurementsToClipboard)
</code></pre>

---
