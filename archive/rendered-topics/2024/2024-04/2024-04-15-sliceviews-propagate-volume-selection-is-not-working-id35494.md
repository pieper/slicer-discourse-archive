---
topic_id: 35494
title: "Sliceviews Propagate Volume Selection Is Not Working"
date: 2024-04-15
url: https://discourse.slicer.org/t/35494
---

# SliceViews - Propagate volume selection is not working?

**Topic ID**: 35494
**Date**: 2024-04-15
**URL**: https://discourse.slicer.org/t/sliceviews-propagate-volume-selection-is-not-working/35494

---

## Post #1 by @Davide_Scorza (2024-04-15 13:37 UTC)

<p>Dear slicer community,</p>
<p>I’ve been used Slicer from quite a while, and I am currently writing a new module which uses some “old” functions I wrote time ago to automate some interaction with 3D Slicer.</p>
<p>In particular, I need to set the sliceViews to a specific volume I just pushed into 3D slicer. To do so, I used the following functions:</p>
<pre><code class="lang-auto">def get_slice_view(color_string):
    lm = slicer.app.layoutManager()
    selected_slice = lm.sliceWidget(color_string)
    return selected_slice
</code></pre>
<p>and</p>
<pre><code class="lang-auto">def set_volume_to_slice_view(
    volume_node, slice_node, layer="background", propagate=False
):
    """
    Assign a volumeNode to a specific view.

    :param volume_node: volume to assign to a specific view
    :param slice_node:  select the slice_node. Could be either the slice_node or the string
                        ['Red', 'Yellow', 'Green']
    :param layer: string specifying the layer where to put the volumeNode
                ['background', 'foreground', 'labelmap']
    :param layer:
    :param propagate:

    :return: True (success) or False (Failure)
    """
    if isinstance(slice_node, str):
        slice_node = get_slice_view(slice_node)

    try:
        logic = slice_node.sliceLogic()
        composite_node = logic.GetSliceCompositeNode()
    except AttributeError:
        slice_node = get_slice_view(slice_node.GetName())
        logic = slice_node.sliceLogic()
        composite_node = logic.GetSliceCompositeNode()

    if layer == "background":
        composite_node.SetBackgroundVolumeID(volume_node.GetID())
        if propagate:
            slicer.app.applicationLogic().PropagateBackgroundVolumeSelection(0)
        return True
    elif layer == "foreground":
        composite_node.SetForegroundVolumeID(volume_node.GetID())
        if propagate:
            slicer.app.applicationLogic().PropagateForegroundVolumeSelection(0)
        return True
    elif layer == "labelmap":
        composite_node.SetLabelVolumeID(volume_node.GetID())
        if propagate:
            slicer.app.applicationLogic().PropagateLabelVolumeSelection(0)
        return True
    else:
        logging.info("*** Error assigning volume to slice View ***")
        return False
</code></pre>
<p>I tested this same code, and it is working without the Propagate*VolumeSelection() (meaning the propagate flag in my function set to True).</p>
<p>I am wondering if I am using it wrong, it is just my problem or it is a function bug.<br>
As I said, with propagate=False the function is working (however, only a single sliceView is changing), and I replicate the failure directly in the 3D Slicer python interactor.</p>
<p>I am using Slicer 5.2.2, on Windows platform.</p>
<p>Thanks in advance for any help you could provide.<br>
Great job with the platform by the way!<br>
Best Regards,<br>
Davide</p>

---

## Post #2 by @pieper (2024-04-15 18:33 UTC)

<p>You might want to try:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L527">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L527" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L527" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L527</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="517" style="counter-reset: li-counter 516 ;">
          <li>        if widgetClassName == "QSpinBox" or widgetClassName == "ctkSliderWidget":</li>
          <li>            parameterNode.SetParameter(parameterName, str(widget.value))</li>
          <li>        elif widgetClassName == "QCheckBox" or widgetClassName == "QPushButton":</li>
          <li>            parameterNode.SetParameter(parameterName, "true" if widget.checked else "false")</li>
          <li>        elif widgetClassName == "QComboBox":</li>
          <li>            parameterNode.SetParameter(parameterName, widget.currentText)</li>
          <li>        elif widgetClassName == "qMRMLNodeComboBox":</li>
          <li>            parameterNode.SetNodeReferenceID(parameterName, widget.currentNodeID)</li>
          <li></li>
          <li></li>
          <li class="selected">def setSliceViewerLayers(background="keep-current", foreground="keep-current", label="keep-current",</li>
          <li>                         foregroundOpacity=None, labelOpacity=None, fit=False, rotateToVolumePlane=False):</li>
          <li>    """Set the slice views with the given nodes.</li>
          <li></li>
          <li>    If node ID is not specified (or value is 'keep-current') then the layer will not be modified.</li>
          <li></li>
          <li>    :param background: node or node ID to be used for the background layer</li>
          <li>    :param foreground: node or node ID to be used for the foreground layer</li>
          <li>    :param label: node or node ID to be used for the label layer</li>
          <li>    :param foregroundOpacity: opacity of the foreground layer</li>
          <li>    :param labelOpacity: opacity of the label layer</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Davide_Scorza (2024-04-16 07:08 UTC)

<p>Thank you very much <a class="mention" href="/u/pieper">@pieper</a>, it did exactly what I needed.<br>
I did look into the utils module from the embedded interpreter, and missed that one.</p>
<p>Thanks again.<br>
Davide</p>

---
