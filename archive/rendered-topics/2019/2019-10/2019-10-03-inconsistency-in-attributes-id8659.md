---
topic_id: 8659
title: "Inconsistency In Attributes"
date: 2019-10-03
url: https://discourse.slicer.org/t/8659
---

# Inconsistency in "Attributes"?

**Topic ID**: 8659
**Date**: 2019-10-03
**URL**: https://discourse.slicer.org/t/inconsistency-in-attributes/8659

---

## Post #1 by @unnmdnwb3 (2019-10-03 13:53 UTC)

<p>Hi everyone,</p>
<p>I had to implement a check, if a file to import has dicom-data associated.<br>
Hence, I took a look at the example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:" rel="nofollow noopener">script repository</a>.</p>
<p>However, I tried different approaches, which resulted in (for me) unexpected results.</p>
<p><strong>Node:</strong></p>
<pre><code class="lang-auto">ID: 2555
DataNode: vtkMRMLScalarVolumeNode
Name (from DataNode): TestName
Parent: 2557
Children: 
OwnerPluginName: Volumes
Expanded: true
UIDs:
  DICOM:2.16.840.1.114033.0.20170412.2476798.0.1
  DICOMInstanceUID:2.16.840.1.114033.0.20170412.2476798.0.1.1
Attributes:
  DICOM.Modality:PT
  DICOM.ReferencedInstanceUIDs:
  DICOM.SeriesNumber:1000
</code></pre>
<p><strong>Function:</strong></p>
<pre><code class="lang-auto">&gt;&gt; shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

&gt;&gt;&gt; attribute = shNode.GetItemAttribute(2555, 'DICOM.instanceUIDs')
&gt;&gt;&gt; attribute
''

&gt;&gt;&gt; attribute = shNode.GetItemDataNode(2555).GetAttribute('DICOM.instanceUIDs')
&gt;&gt;&gt; attribute
'2.16.840.1.114033.0.20170412.2476798.0.1.1'
</code></pre>
<p>The same applies to attribute names:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; names = shNode.GetItemDataNode(2555).GetAttributeNames()
&gt;&gt;&gt; names
('DICOM.instanceUIDs',)

&gt;&gt;&gt; names = shNode.GetItemAttributeNames(2555)
&gt;&gt;&gt; names
('DICOM.Modality', 'DICOM.ReferencedInstanceUIDs', 'DICOM.SeriesNumber')
</code></pre>
<p>Hence, the behaviour is as it follows:</p>
<ul>
<li>
<code>shNode.GetItemAttribute(id, attribute)</code>: <em>returns</em> <strong>Attributes</strong>
</li>
<li>
<code>node.GetAttribute(attribute)</code>: <em>returns</em> <strong>UIDs</strong>
</li>
</ul>
<p>For me as a user, this was kind of surprising. Is this intended behaviour, did I miss something?</p>
<p>Thanks in advance! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @cpinter (2019-10-03 13:58 UTC)

<p>Subject hierarchy is a hierarchy of data nodes containing items pointing to nodes. Data nodes are MRML nodes containing data. The two contain very different information. Some DICOM info is stored in both for convenience and tracking prevalence.</p>
<p>Learn about subject hierarchy<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Labs/SubjectHierarchy" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/SubjectHierarchy</a></p>
<p>Learn about MRML nodes<br>
<a href="http://apidocs.slicer.org/master/classvtkMRMLNode.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classvtkMRMLNode.html</a></p>

---

## Post #3 by @unnmdnwb3 (2019-10-03 15:36 UTC)

<p>hi <a class="mention" href="/u/cpinter">@cpinter</a>,</p>
<p>Thank you for the answer! Okay, I didn’t get the differentiation between <code>item</code> and <code>node</code>… thanks for pointing that out. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Cheers!</p>

---
