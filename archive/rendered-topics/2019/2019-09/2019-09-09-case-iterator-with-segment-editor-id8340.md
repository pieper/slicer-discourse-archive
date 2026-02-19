---
topic_id: 8340
title: "Case Iterator With Segment Editor"
date: 2019-09-09
url: https://discourse.slicer.org/t/8340
---

# Case Iterator with segment editor

**Topic ID**: 8340
**Date**: 2019-09-09
**URL**: https://discourse.slicer.org/t/case-iterator-with-segment-editor/8340

---

## Post #1 by @muratmaga (2019-09-09 05:05 UTC)

<p>I have a folder full of nifti files that I would like to convert them to 3D models after a threshold effect. I am trying to use Case Iterator to help me with the naming and saving, but so far wasn’t able get very far with it. I can read the input files, go back and forth between cases, but it doesn’t do anything about the saving.</p>
<p>Here is a screenshot of the data module with one of the cases loaded:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e3e89531528ef2ac5f31ab94607d3a6a7dde30.png" alt="image" data-base62-sha1="2YNQ9tyRagXRez4L257U4yJJALm" width="671" height="156"><br>
I would like to have both Segment_1 (the segmentation) and Segment_1 (the model) to be saved with the original nifti file name.</p>
<p>Is there a way to configure Case Iterator to do that?</p>

---

## Post #2 by @JoostJM (2019-09-09 10:01 UTC)

<p>Currently, not without some programming.</p>
<p>If you have checked the “save new masks” and “save loaded masks”, case iterator should at least save your segmentation, though your model will be discarded.</p>
<p>In the github repository, I also have a dev branch, which has multiple additional features, both for the user interface and “under-the-hood” stuff. This includes a more easy way of defining a customized iterator, and auto-updating the layout to accomodate the loaded volumes, aligned on the slices (instead of reformatted volumes to truly transversal/sagittal/coronal).</p>
<p>So if you want to use caseIterator to include saving your models, you’ll have to customize the version you have. You can either update the current master (this would involve adding a function for saving models, and calling that function when the case closes). Alternatively, if you also want to use the newer features, I can help you write a customized iterator which also stores models as part of the workflow.</p>
<p>For updating the current version in the Slicer Extensions index, do the following:</p>
<p>Add this piece of code to <code>CsvTableIterator.py</code>, just after <code>saveMask()</code> function (i.e. make it part of the <code>CaseTableIteratorLogic</code> class:</p>
<pre><code class="lang-auto">  def saveModel(self, node, reader, overwrite_existing=False):
    storage_node = node.GetStorageNode()
    if storage_node is not None and storage_node.GetFileName() is not None:
      # mask was loaded, save the updated mask in the same directory
      target_dir = os.path.dirname(storage_node.GetFileName())
    else:
      target_dir = self.currentCaseFolder

    if not os.path.isdir(target_dir):
      self.logger.debug('Creating output directory at %s', target_dir)
      os.makedirs(target_dir)

    nodename = node.GetName()
    # Add the readername if set
    if reader is not None:
      nodename += '_' + reader
    filename = os.path.join(target_dir, nodename)

    # Prevent overwriting existing files
    if os.path.exists(filename + '.vtk') and not overwrite_existing:
      self.logger.debug('Filename exists! Generating unique name...')
      idx = 1
      filename += '(%d).vtk'
      while os.path.exists(filename % idx):
        idx += 1
      filename = filename % idx
    else:
      filename += '.vtk'

    # Save the node
    slicer.util.saveNode(node, filename)
    self.logger.info('Saved node %s in %s', nodename, filename)

</code></pre>
<p>Add the call to this function in <code>SlicerCaseIterator.py</code>, in function <code>_closeCase()</code> (L423-L446). You can do this by inserting this piece of code in L435 (just after the <code>if self.saveNew:</code> block:</p>
<pre><code class="lang-auto">for n in slicer.util.getNodesByClass('vtkMRMLModelNode'):
  self.iterator.saveModel(n, self.reader)
</code></pre>

---

## Post #3 by @muratmaga (2019-09-11 05:40 UTC)

<p>Thank you it worked to save the segments and models. But it still retains the default naming (segment_1, etc), as oppose to remaining it to the original input volume. I will try to fiddle and see if I can get the original volume name in the input table as the name of files being saved.</p>

---

## Post #4 by @JoostJM (2019-09-11 07:52 UTC)

<p>Ah, I may be able to help with that too. I assume you create new segmenations for each case right?</p>
<p>This is handled in <a href="https://github.com/JoostJM/SlicerCaseIterator/blob/master/SlicerCaseIterator/SlicerCaseIteratorLib/CsvTableIterator.py#L296-L300" rel="nofollow noopener">CsvTableIterator.py:L296-300</a>:</p>
<pre><code class="lang-auto">   ma = self._getColumnValue('mask', case_idx)
   if ma is not None:
     ma_node = self._loadMaskNode(root, ma, im_node)
   else:
     ma_node = None
</code></pre>
<p>Basically, if you don’t specify a mask, none is loaded and when the segment editor module is entered, it creates one for you, with the name ‘Segmentation’.</p>
<p>If you replace update this block to the following:</p>
<pre><code class="lang-auto">    ma = self._getColumnValue('mask', case_idx)
    if ma is not None:
      ma_node = self._loadMaskNode(root, ma, im_node)
    else:
      ma_node = slicer.vtkMRMLSegmentationNode()
      slicer.mrmlScene.AddNode(ma_node)
      ma_node.SetReferenceImageGeometryParameterFromVolumeNode(im_node)
      ma_node.SetName(im_node.GetName() + '_Segmentation')
</code></pre>
<p>This will now add a segmentation node if no mask was specified to load, and set it’s name to match to input volume, with ‘_Segmentation’ appended. It is possible to use exactly the same name as your image volume, but IMHO appending a suffix like ‘segmentation’ keeps it nice and clear that this node represents a segmentation that belongs to your image, and will also be reflected as such in the filesystem upon saving…</p>

---

## Post #5 by @muratmaga (2019-09-11 15:59 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a>. Thank you very much for all your help.</p>
<p>I did the change and restarted the Slicer, but as far as I can tell behavior is still the same. It keeps the default segment names. My initial table did not have field called mask, only the images and path column so I add it an empty column with name mask, but that didn’t make a difference either?</p>

---

## Post #6 by @JoostJM (2019-09-12 11:41 UTC)

<p>Ah I think we were talking about 2 different things here. If I’m correct, it should have added a new segmentation Node, with the name set as described above. However, this still results in the individual segments receiving names like ‘segment_1’, ‘segment_2’, etc.</p>
<p>Can you please clarify why you also want to control the naming of the segments? When stored on the disk, the filename is derived from the node name (i.e. the segmentation node, which contains all your segments). Individual segment names are only visible inside slicer (added in the nrrd header, but as far as I know ignored by most other programs).<br>
I assumed you meant the segmentation node name when you were writing about setting it to the volume name, as the segmentation node is linked to the volume, therefore setting the individual segment’s name to the volume name seemed a bit superfluous to me. When I change the individual segments name, I usually do so to indicate what the ROI designates (like ‘tumour’, ‘lymphnode’, ‘liver’, etc.)</p>

---

## Post #7 by @lassoan (2019-09-12 12:57 UTC)

<p>Typing a segment name each time seems quite error-prone (typos, differences in spelling, etc. can all cause issues). It would be useful to initialize each new segmentation node by copying empty segments with pre-populated names (and terminology) from a “template” segmentation node.</p>
<p>Recent Slicer Preview Releases facilitate this workflow by adding “completion state” (new, being edited, completed, flagged) to each segment - see details here: <a href="https://discourse.slicer.org/t/new-feature-search-and-filter-in-segments-table/7827" class="inline-onebox">New feature: Search and filter in segments table</a>.</p>

---

## Post #8 by @muratmaga (2019-09-12 16:28 UTC)

<p>I want to control the naming, because I ultimately I want to export them as ply volumes. If every  model from a different volume gets the segment_1 name, they will overwrite each other at the time of saving. As Andras mentioned below, manually changing this is tedious (for large number of volumes) and is error prone.</p>
<p>I was looking for a behavior similar to the fiducial list. If I create a fiducial list Murat, then the first point gets the name Murat-1. So along those lines, if my segmentation node is automatically set to the name of the volume, then first segment gets the name volume_Segment_1 (or something along those lines, or the suffices can be managed through a template). Keeping everything in a hierarchy works well when everything is managed within the scene, but when saving/exporting individual elements generic names like Segment_1 causes issues.</p>

---

## Post #9 by @JoostJM (2019-09-13 07:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> very interesting! Great to see how segmentation keeps evolving in Slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
<a class="mention" href="/u/muratmaga">@muratmaga</a>, when something like a template node gets implemented, I’ll probably use that to add prefixes for new segments.</p>
<p>In the meantime, I’ve hacked together a piece of code that does more or less the same. It’ll only work for segmentation nodes that have been added by the case iterator, as it needs to set up observers and keep track of some data to work.</p>
<p>These are the new/adapted functions (all in SlicerCaseIteratorLogic class):</p>
<pre><code class="lang-auto">  import re

  (...)

  def __init__(self, iterator, start, redirect, saveNew=False, saveLoaded=False, multiViewer=False):

    self.logger = logging.getLogger('SlicerCaseIterator.logic')

    self.mask_node_observers = []
    self.prefixes = {}

    (...)  # Rest of the __init__ function

  def __del__(self):
    # Free up the references to the nodes to allow GC and prevent memory leaks
    self.logger.debug('Destroying Case Iterator Logic instance')
    self.currentCase = None
    self.iterator = None

    # New part:
    self.remove_mask_node_observers()

  def observe_mask_node(self, node):
    if node is None:
      self.logger.debug("No node to observe passed. Skipping adding observer")
      return

    # Observe the SegmentAdded event to enable changing the auto-naming behaviour
    segmentation = node.GetSegmentation()
    self.mask_node_observers.append((node, segmentation.AddObserver(segmentation.SegmentAdded, self.onSegmentAdded)))

    # Store the prefix we want to use, as the event only passes the segmentation,
    # not the segmentationNode
    self.prefixes[segmentation.GetAddressAsString(None)] = node.GetName()

  def remove_mask_node_observers(self):
    if len(self.mask_node_observers) == 0:
      self.logger.debug("Not observing any node!")

    for node, obs in self.mask_node_observers:
      segmentation = node.GetSegmentation()
      segmentation.RemoveObserver(obs)
      seg_addr = segmentation.GetAddressAsString(None)
      if seg_addr in self.prefixes:
        del self.prefixes[seg_addr]
    self.mask_node_observers= []

  def onSegmentAdded(self, caller, event):
    # caller is vtkSegment, not vtkMRMLSegmentationNode!
    try:
      # Get the last added segment, and check if it is a new empty segment with standard name
      new_segment = caller.GetNthSegment(caller.GetNumberOfSegments() - 1)
      name_match = re.match(r'Segment_(?P&lt;seg_no&gt;\d+)', new_segment.GetName())
      seg_addr = caller.GetAddressAsString(None)  # Needed to look up prefix

      if seg_addr not in self.prefixes:
        self.logger.debug('Segment added, but segmentation does not have a prefix set. Skipping setting name')
      elif name_match is None:
        self.logger.debug('Segment added, but non-standard name. Possibly imported segment. Skipping setting name')
      else:
        new_name = self.prefixes[seg_addr] + '_%s' % name_match.groupdict()['seg_no']
        self.logger.debug('Segment added, Auto-setting name to %s', new_name)
        new_segment.SetName(new_name)
    except Exception:
      self.logger.warning('Error setting new name for segment!', exc_info=True)

  def _loadCase(self, new_idx):
    
    (...)

      if self.redirect:
        self.iterator.backend.enter_module(im, ma)
        # Observer the master mask to enable auto-renaming new segments
        self.iterator.backend.observe_mask_node(ma)

  def _closeCase(self, new_idx):

    (...)

          if mask is not None:
            self.iterator.saveMask(mask,)
            self.iterator.backend.remove_mask_node_observers()  # clean-up observers
</code></pre>
<p>This will keep track of your master segmentation node, and each time you add a new segment (which will be named <code>Segment_&lt;N&gt;</code>, Case Iterator catches the event, and updates the name to <code>&lt;Prefix&gt;_&lt;N&gt;</code>, where <code>&lt;Prefix&gt;</code> is the segmentation name as it is set during loading.</p>

---
