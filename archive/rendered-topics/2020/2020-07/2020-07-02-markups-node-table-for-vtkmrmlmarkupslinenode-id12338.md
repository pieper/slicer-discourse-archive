---
topic_id: 12338
title: "Markups Node Table For Vtkmrmlmarkupslinenode"
date: 2020-07-02
url: https://discourse.slicer.org/t/12338
---

# Markups Node Table for vtkMRMLMarkupsLineNode

**Topic ID**: 12338
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/markups-node-table-for-vtkmrmlmarkupslinenode/12338

---

## Post #1 by @EricM (2020-07-02 15:48 UTC)

<p>Hello Slicer Community,</p>
<p>I’m trying to include a module where annotators can draw major and minor axes on brain images. I found that the <code>vtkMRMLMarkupsLineNode</code> does just the job. In Slicer 4.11 (not sure about previous versions), there is a table widget (perhaps a QTableView ?) that keeps track of all of the <code>vtkMRMLMarkupsLineNode</code>s (see screenshot below). I’d like to take this widget and import it in my module, but I cannot find it in any parent widget or modules accessible through python.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e76f81ec4f31fbe60986051aeead1515df2071.png" data-download-href="/uploads/short-url/5H0t7QnwduhCy80VZyeQRQ9eC41.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e76f81ec4f31fbe60986051aeead1515df2071_2_690x354.png" alt="image" data-base62-sha1="5H0t7QnwduhCy80VZyeQRQ9eC41" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e76f81ec4f31fbe60986051aeead1515df2071_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e76f81ec4f31fbe60986051aeead1515df2071_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e76f81ec4f31fbe60986051aeead1515df2071.png 2x" data-dominant-color="7D8084"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1216×625 97.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ideally, what I would like is to get the different markup buttons (create fiducial, create line, create curve, etc.) as well as the table underneath (with columns Node, Description, Visible, Color). I don’t need to get the collapsable Display or Control Points Widgets.</p>
<p>Thanks for any guidance.<br>
Best,<br>
Eric</p>

---

## Post #2 by @lassoan (2020-07-02 16:11 UTC)

<p>The table widget is a <code>qMRMLSubjectHierarchyTreeView</code>. The buttons above are just simple QPushButtons. You can open Qt Designer and just drag-and-drop these widgets into your module GUI.</p>
<p>For the future, you can find instructions here how to find implementation of a feature that you see on the Slicer GUI <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">here</a>.</p>

---

## Post #3 by @EricM (2020-07-08 13:16 UTC)

<p>Hi Andras,</p>
<p>Thanks for this tip!<br>
While looking around a bit more, I found a way to access the Markups widget and am able to get everything I need</p>
<pre><code class="lang-auto">slicer.modules.markups.widgetRepresentation().children()

(QVBoxLayout (QVBoxLayout at: 0x000001C2B981D5C0), QLabel(0x1c2d23aa960, name="createLabel") , QPushButton(0x1c2d23ab0e0, name="createFiducialPushButton") , QPushButton(0x1c2d23aa2e0, name="createLinePushButton") , QPushButton(0x1c2d23aaca0, name="createAnglePushButton") , QPushButton(0x1c2d23aaa20, name="createOpenCurvePushButton") , QPushButton(0x1c2d23aa5e0, name="createClosedCurvePushButton") , ctkExpandableWidget(0x1c2d23aa620, name="ResizableFrame") , qMRMLCollapsibleButton(0x1c2d23acaa0, name="CollapsibleGroupBox") , ctkCollapsibleButton(0x1c2d2390de0, name="controlPointsCollapsibleButton") , ctkCollapsibleButton(0x1c2d3404090, name="resampleCurveCollapsibleButton") , QAction(0x1c2d391da50 text="Cut" toolTip="Cut" shortcut=QKeySequence("Ctrl+X") menuRole=TextHeuristicRole visible=true) , QAction(0x1c2d391de10 text="Copy" toolTip="Copy" shortcut=QKeySequence("Ctrl+C") menuRole=TextHeuristicRole visible=true) , QAction(0x1c2d391df70 text="Paste" toolTip="Paste" shortcut=QKeySequence("Ctrl+V") menuRole=TextHeuristicRole visible=true) )
</code></pre>
<p>Thanks!</p>

---
