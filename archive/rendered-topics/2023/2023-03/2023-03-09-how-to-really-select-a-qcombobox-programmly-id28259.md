---
topic_id: 28259
title: "How To Really Select A Qcombobox Programmly"
date: 2023-03-09
url: https://discourse.slicer.org/t/28259
---

# How to really select a qComboBox programmly

**Topic ID**: 28259
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/how-to-really-select-a-qcombobox-programmly/28259

---

## Post #1 by @WilliamLambert1205 (2023-03-09 14:23 UTC)

<p>Hi,everyone. I’m trying to using code to substitute a series of mouse clicking and I get into trouble, please guide me.<br>
In the first step, I need to select the first item in ‘OutputVolume’.(‘OutputVolume’ is a qComboBox).<br>
In the second step, I need to select another, it means the second  item in ‘OutputVolume’.</p>
<p>The apperance of this problem is when I click every qComboBox and select, every thing goes right, however, when I set the qComboBox programmly, it seems like I haven’t changed the ‘OutputVolume’ though the words showed is changed. And the result by program is same as when I only do the first step by clicking, but skip the second step.</p>
<p>I guess the problem is, in the second step, these 2 lines below,<br>
OutputVolume=SimpleFiltersWidgetWhole[7]<br>
OutputVolume.setCurrentNodeIndex(1)<br>
which seems to only change what is showed visually in the qComboBox, but don’t truely get the item selected. In other word, it seems I need one more ‘click’ on the item to get it selected.</p>
<p>I loaded 2 .nii as volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3186fbcec9c92df20c070013d753e8a61016297.png" data-download-href="/uploads/short-url/u7r6gUE2SNhFqA5AP8pNHXiLZpd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3186fbcec9c92df20c070013d753e8a61016297.png" alt="image" data-base62-sha1="u7r6gUE2SNhFqA5AP8pNHXiLZpd" width="690" height="78" data-dominant-color="323232"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1527×173 9.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>my code below</p>
<p><span class="hashtag">#First</span> flip<br>
slicer.modules.simplefilters.widgetRepresentation()<br>
slicer.modules.SimpleFiltersWidget.searchBox.setText(‘FlipImageFilter’)<br>
SimpleFiltersWidgetWhole=slicer.modules.SimpleFiltersWidget.filterParameters.widgets<br>
InputVolume=SimpleFiltersWidgetWhole[0]<br>
InputVolume.setCurrentNodeIndex(0)<br>
FlipAxesSpinbox1=FlipAxesSpinbox[1]<span class="hashtag">#SagittalplaneFlip</span><br>
FlipAxesSpinbox1.setValue(1)<br>
FlipAxesSpinbox2=FlipAxesSpinbox[2]<span class="hashtag">#CoronalplaneFlip</span><br>
FlipAxesSpinbox2.setValue(0)<br>
FlipAxesSpinbox3=FlipAxesSpinbox[3]<span class="hashtag">#HorizontalplaneFlip</span><br>
FlipAxesSpinbox3.setValue(0)<br>
<span class="hashtag">#setFlipAboutOriginchecked</span><br>
FlipAboutOrigin=SimpleFiltersWidgetWhole[4]<br>
FlipAboutOrigin.setChecked(1)<br>
<span class="hashtag">#setLabelMapchecked</span></p>
<p>LabelMap=SimpleFiltersWidgetWhole[9]<br>
LabelMap.setChecked(0)<br>
slicer.modules.SimpleFiltersWidget.applyButton.clicked()</p>
<p><span class="hashtag">#Secondflip</span><br>
InputVolume=SimpleFiltersWidgetWhole[0]<br>
InputVolume.setCurrentNodeIndex(1)<br>
OutputVolume=SimpleFiltersWidgetWhole[7]<br>
OutputVolume.setCurrentNodeIndex(1)<br>
FlipAxes=SimpleFiltersWidgetWhole[2]<span class="hashtag">#FlipAxes</span><br>
FlipAxes.coordinates<br>
FlipAxes.children()<br>
FlipAxesSpinbox=FlipAxes.children()</p>
<p>FlipAxesSpinbox1=FlipAxesSpinbox[1]<span class="hashtag">#SagittalplaneFlip</span><br>
FlipAxesSpinbox1.setValue(1)<br>
FlipAxesSpinbox2=FlipAxesSpinbox[2]<span class="hashtag">#CoronalplaneFlip</span><br>
FlipAxesSpinbox2.setValue(0)<br>
FlipAxesSpinbox3=FlipAxesSpinbox[3]<span class="hashtag">#HorizontalplaneFlip</span><br>
FlipAxesSpinbox3.setValue(0)</p>
<p><span class="hashtag">#setFlipAboutOriginchecked</span></p>
<p>FlipAboutOrigin=SimpleFiltersWidgetWhole[4]</p>
<p>FlipAboutOrigin.setChecked(1)<br>
<span class="hashtag">#setLabelMapchecked</span><br>
LabelMap=SimpleFiltersWidgetWhole[9]<br>
LabelMap.setChecked(1)</p>
<p>slicer.modules.SimpleFiltersWidget.applyButton.clicked()</p>

---
