# Load MHA dataset

**Topic ID**: 23690
**Date**: 2022-06-03
**URL**: https://discourse.slicer.org/t/load-mha-dataset/23690

---

## Post #1 by @Jakub_Mitura (2022-06-03 07:19 UTC)

<p>Hello I like the organization that slicer brings to the diceom dataset, and I would like to apply it to my MHA dataset programmatically. So What I would like to achieve (all programmatically - preferably python) :</p>
<ol>
<li>given list of folder names add slicer node for each where each node represent single patient data</li>
<li>load volumes and add them to the nodes</li>
</ol>
<pre><code class="lang-auto">loadedVolumeNode = slicer.util.loadVolume("/home/sliceruser/data/10000/10000_1000000_adc.mha")
</code></pre>
<p>and now somehow add loaded volume to the node - so all volumes of sinlge patient will be associated with this node<br>
3) be able to iterate over all nodes and volumes in python and load chosen into numpy or itk</p>

---
