# How to select a qComboBox programmatically in Simple Filters module

**Topic ID**: 28329
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/how-to-select-a-qcombobox-programmatically-in-simple-filters-module/28329

---

## Post #1 by @WilliamLambert1205 (2023-03-12 15:26 UTC)

<p>Hi,everyone. I’m trying to using code to substitute a series of mouse clicking and I get into trouble, please guide me.<br>
In the first step, I need to select the first item in ‘OutputVolume’.(‘OutputVolume’ is a qComboBox).<br>
In the second step, I need to select another, it means the second item in ‘OutputVolume’.</p>
<p>The apperance of this problem is when I click every qComboBox and select, every thing goes right, however, when I set the qComboBox programmly, it seems like I haven’t changed the ‘OutputVolume’ though the words showed is changed. And the result by program is same as when I only do the first step by clicking, but skip the second step.</p>
<p>I guess the problem is, in the second step, these 2 lines below,</p>
<pre><code class="lang-auto">OutputVolume=SimpleFiltersWidgetWhole[7]
OutputVolume.setCurrentNodeIndex(1)
</code></pre>
<p>which seems to only change what is showed visually in the qComboBox, but don’t truely get the item selected. In other word, it seems I need one more ‘click’ on the item to get it selected.</p>
<p>I loaded 2 .nii as volume.Hi,everyone. I’m trying to using code to substitute a series of mouse clicking and I get into trouble, please guide me.<br>
In the first step, I need to select the first item in ‘OutputVolume’.(‘OutputVolume’ is a qComboBox).<br>
In the second step, I need to select another, it means the second item in ‘OutputVolume’.</p>
<p>The apperance of this problem is when I click every qComboBox and select, every thing goes right, however, when I set the qComboBox programmly, it seems like I haven’t changed the ‘OutputVolume’ though the words showed is changed. And the result by program is same as when I only do the first step by clicking, but skip the second step.</p>
<p>I guess the problem is, in the second step, these 2 lines below,<br>
OutputVolume=SimpleFiltersWidgetWhole[7]<br>
OutputVolume.setCurrentNodeIndex(1)<br>
which seems to only change what is showed visually in the qComboBox, but don’t truely get the item selected. In other word, it seems I need one more ‘click’ on the item to get it selected.</p>
<p>I loaded 2 .nii as volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3186fbcec9c92df20c070013d753e8a61016297.png" data-download-href="/uploads/short-url/u7r6gUE2SNhFqA5AP8pNHXiLZpd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3186fbcec9c92df20c070013d753e8a61016297.png" alt="image" data-base62-sha1="u7r6gUE2SNhFqA5AP8pNHXiLZpd" width="690" height="78" data-dominant-color="323232"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1527×173 9.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
my code below</p>
<pre><code class="lang-auto">#First flip
slicer.modules.simplefilters.widgetRepresentation()
slicer.modules.SimpleFiltersWidget.searchBox.setText(‘FlipImageFilter’)
SimpleFiltersWidgetWhole=slicer.modules.SimpleFiltersWidget.filterParameters.widgets
InputVolume=SimpleFiltersWidgetWhole[0]
InputVolume.setCurrentNodeIndex(0)
FlipAxesSpinbox1=FlipAxesSpinbox[1]#SagittalplaneFlip
FlipAxesSpinbox1.setValue(1)
FlipAxesSpinbox2=FlipAxesSpinbox[2]#CoronalplaneFlip
FlipAxesSpinbox2.setValue(0)
FlipAxesSpinbox3=FlipAxesSpinbox[3]#HorizontalplaneFlip
FlipAxesSpinbox3.setValue(0)
#setFlipAboutOriginchecked
FlipAboutOrigin=SimpleFiltersWidgetWhole[4]
FlipAboutOrigin.setChecked(1)
#setLabelMapchecked

LabelMap=SimpleFiltersWidgetWhole[9]
LabelMap.setChecked(0)
slicer.modules.SimpleFiltersWidget.applyButton.clicked()

#Secondflip
InputVolume=SimpleFiltersWidgetWhole[0]
InputVolume.setCurrentNodeIndex(1)
OutputVolume=SimpleFiltersWidgetWhole[7]
OutputVolume.setCurrentNodeIndex(1)
FlipAxes=SimpleFiltersWidgetWhole[2]#FlipAxes
FlipAxes.coordinates
FlipAxes.children()
FlipAxesSpinbox=FlipAxes.children()

FlipAxesSpinbox1=FlipAxesSpinbox[1]#SagittalplaneFlip
FlipAxesSpinbox1.setValue(1)
FlipAxesSpinbox2=FlipAxesSpinbox[2]#CoronalplaneFlip
FlipAxesSpinbox2.setValue(0)
FlipAxesSpinbox3=FlipAxesSpinbox[3]#HorizontalplaneFlip
FlipAxesSpinbox3.setValue(0)

#setFlipAboutOriginchecked

FlipAboutOrigin=SimpleFiltersWidgetWhole[4]

FlipAboutOrigin.setChecked(1)
#setLabelMapchecked
LabelMap=SimpleFiltersWidgetWhole[9]
LabelMap.setChecked(1)

slicer.modules.SimpleFiltersWidget.applyButton.clicked()
</code></pre>

---

## Post #2 by @pieper (2023-03-12 15:45 UTC)

<p>Rather than trying to script the GUI, you could just use the SimpleITK code directly:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk</a></p>

---
