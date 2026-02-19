---
topic_id: 2667
title: "Problem With Running Slicer 4 9 0 2018 01 10 Linux Amd64 In"
date: 2018-04-23
url: https://discourse.slicer.org/t/2667
---

# Problem with running Slicer-4.9.0-2018-01-10-linux-amd64 in Fedora core 25

**Topic ID**: 2667
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/problem-with-running-slicer-4-9-0-2018-01-10-linux-amd64-in-fedora-core-25/2667

---

## Post #1 by @shahrokh (2018-04-23 14:38 UTC)

<p>Hello<br>
Dear Slicer Developers</p>
<p>I want to use Slicer-4.9.0-2018-01-10-linux-amd64 in Fedora core 25 with the following specifications:</p>
<pre><code>[sn@localhost ~]$ uname --all
Linux localhost.localdomain 4.8.6-300.fc25.x86_64 #1 SMP Tue Nov 1 12:36:38 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
[sn@localhost ~]$ 
</code></pre>
<p>When I run Slicer, I get the following messages. Anyway, Slicer is run but “Suject Hierarchy” is not seen.</p>
<pre><code class="lang-auto">    [sn@localhost ~]$ Slicer 
    Number of registered modules: 182 
    Enabling C extensions
    ModuleDescriptionParser Error: &lt;index&gt; cannot be specified because a &lt;longflag&gt; and/or &lt;flag&gt; has been specified for this parameter." at line 19 while parsing &lt;?xml version="1.0" encoding="utf-8"?&gt;
    `&lt;executable&gt;`
      &lt;category&gt;Testing&lt;/category&gt;
      &lt;title&gt;Eval Shape&lt;/title&gt;
      &lt;description&gt;&lt;![CDATA[Evaluate shape group index with neural network.]]&gt;&lt;/description&gt;
      &lt;version&gt;1.0.$Revision$&lt;/version&gt;
      &lt;documentation-url&gt;&lt;/documentation-url&gt;
      &lt;license&gt;slicer4&lt;/license&gt;
      &lt;contributor&gt;Priscille de Dumast (University of Michigan)&lt;/contributor&gt;
      &lt;acknowledgements&gt;&lt;![CDATA[This work was supported by the National Institutes of Dental and Craniofacial Research and Biomedical Imaging and Bioengineering of the National Institutes of Health under Award Number R01DE024450.]]&gt;&lt;/acknowledgements&gt;
      &lt;parameters&gt;
        &lt;label&gt;IO&lt;/label&gt;
        &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;inputZip&lt;/name&gt;
          &lt;label&gt;Input Zip&lt;/label&gt;
          &lt;longflag&gt;--inputZip&lt;/longflag&gt;
          &lt;channel&gt;input&lt;/channel&gt;
          &lt;index&gt;0&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Input zip]]&gt;&lt;/description&gt;
        &lt;/file&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;outputZip&lt;/name&gt;
          &lt;label&gt;Output Zip&lt;/label&gt;
          &lt;longflag&gt;--outputZip&lt;/longflag&gt;
          &lt;channel&gt;output&lt;/channel&gt;
          &lt;index&gt;1&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Output zip]]&gt;&lt;/description&gt;
        &lt;/file&gt;
      &lt;/parameters&gt;
    &lt;/executable&gt;
    Failed to parse xml module description:
     "&lt;?xml version="1.0" encoding="utf-8"?&gt;
    &lt;executable&gt;
      &lt;category&gt;Testing&lt;/category&gt;
      &lt;title&gt;Eval Shape&lt;/title&gt;
      &lt;description&gt;&lt;![CDATA[Evaluate shape group index with neural network.]]&gt;&lt;/description&gt;
      &lt;version&gt;1.0.$Revision$&lt;/version&gt;
      &lt;documentation-url&gt;&lt;/documentation-url&gt;
      &lt;license&gt;slicer4&lt;/license&gt;
      &lt;contributor&gt;Priscille de Dumast (University of Michigan)&lt;/contributor&gt;
      &lt;acknowledgements&gt;&lt;![CDATA[This work was supported by the National Institutes of Dental and Craniofacial Research and Biomedical Imaging and Bioengineering of the National Institutes of Health under Award Number R01DE024450.]]&gt;&lt;/acknowledgements&gt;
      &lt;parameters&gt;
        &lt;label&gt;IO&lt;/label&gt;
        &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;inputZip&lt;/name&gt;
          &lt;label&gt;Input Zip&lt;/label&gt;
          &lt;longflag&gt;--inputZip&lt;/longflag&gt;
          &lt;channel&gt;input&lt;/channel&gt;
          &lt;index&gt;0&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Input zip]]&gt;&lt;/description&gt;
        &lt;/file&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;outputZip&lt;/name&gt;
          &lt;label&gt;Output Zip&lt;/label&gt;
          &lt;longflag&gt;--outputZip&lt;/longflag&gt;
          &lt;channel&gt;output&lt;/channel&gt;
          &lt;index&gt;1&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Output zip]]&gt;&lt;/description&gt;
        &lt;/file&gt;
      &lt;/parameters&gt;
    &lt;/executable&gt;" 
    ModuleDescriptionParser Error: &lt;index&gt; cannot be specified because a &lt;longflag&gt; and/or &lt;flag&gt; has been specified for this parameter." at line 19 while parsing &lt;?xml version="1.0" encoding="utf-8"?&gt;
    &lt;executable&gt;
      &lt;category&gt;Testing&lt;/category&gt;
      &lt;title&gt;Train Neural Network&lt;/title&gt;
      &lt;description&gt;&lt;![CDATA[Train a neural network.]]&gt;&lt;/description&gt;
      &lt;version&gt;1.0.$Revision$&lt;/version&gt;
      &lt;documentation-url&gt;&lt;/documentation-url&gt;
      &lt;license&gt;slicer4&lt;/license&gt;
      &lt;contributor&gt;Priscille de Dumast (University of Michigan)&lt;/contributor&gt;
      &lt;acknowledgements&gt;&lt;![CDATA[This work was supported by the National Institutes of Dental and Craniofacial Research and Biomedical Imaging and Bioengineering of the National Institutes of Health under Award Number R01DE024450.]]&gt;&lt;/acknowledgements&gt;
      &lt;parameters&gt;
        &lt;label&gt;IO&lt;/label&gt;
        &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;inputZip&lt;/name&gt;      
          &lt;label&gt;Input Zip&lt;/label&gt;
          &lt;longflag&gt;--inputZip&lt;/longflag&gt;
          &lt;channel&gt;input&lt;/channel&gt;
          &lt;index&gt;0&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Input zip file]]&gt;&lt;/description&gt;
        &lt;/file&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;outputZip&lt;/name&gt;
          &lt;label&gt;Output Zip&lt;/label&gt;
          &lt;longflag&gt;--outputZip&lt;/longflag&gt;
          &lt;channel&gt;output&lt;/channel&gt;
          &lt;index&gt;1&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Output zip]]&gt;&lt;/description&gt;
        &lt;/file&gt;
      &lt;/parameters&gt;
    &lt;/executable&gt;
    Failed to parse xml module description:
     "&lt;?xml version="1.0" encoding="utf-8"?&gt;
    &lt;executable&gt;
      &lt;category&gt;Testing&lt;/category&gt;
      &lt;title&gt;Train Neural Network&lt;/title&gt;
      &lt;description&gt;&lt;![CDATA[Train a neural network.]]&gt;&lt;/description&gt;
      &lt;version&gt;1.0.$Revision$&lt;/version&gt;
      &lt;documentation-url&gt;&lt;/documentation-url&gt;
      &lt;license&gt;slicer4&lt;/license&gt;
      &lt;contributor&gt;Priscille de Dumast (University of Michigan)&lt;/contributor&gt;
      &lt;acknowledgements&gt;&lt;![CDATA[This work was supported by the National Institutes of Dental and Craniofacial Research and Biomedical Imaging and Bioengineering of the National Institutes of Health under Award Number R01DE024450.]]&gt;&lt;/acknowledgements&gt;
      &lt;parameters&gt;
        &lt;label&gt;IO&lt;/label&gt;
        &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;inputZip&lt;/name&gt;      
          &lt;label&gt;Input Zip&lt;/label&gt;
          &lt;longflag&gt;--inputZip&lt;/longflag&gt;
          &lt;channel&gt;input&lt;/channel&gt;
          &lt;index&gt;0&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Input zip file]]&gt;&lt;/description&gt;
        &lt;/file&gt;
        &lt;file fileExtensions=".zip"&gt;
          &lt;name&gt;outputZip&lt;/name&gt;
          &lt;label&gt;Output Zip&lt;/label&gt;
          &lt;longflag&gt;--outputZip&lt;/longflag&gt;
          &lt;channel&gt;output&lt;/channel&gt;
          &lt;index&gt;1&lt;/index&gt;
          &lt;description&gt;&lt;![CDATA[Output zip]]&gt;&lt;/description&gt;
        &lt;/file&gt;
      &lt;/parameters&gt;
    &lt;/executable&gt;" 
    Number of instantiated modules: 182 
    When loading module  "ProstateMRIUSContourPropagation" , the dependency "DicomRtImportExport" failed to be loaded. 
    Number of loaded modules: 181 
    Switch to module:  "Welcome" 
    Loaded volume from file: /home/sn/samanehjan/workspaceSPHARM/input/sample1_C1_group04.nii. Dimensions: 30x13x28. Number of components: 1. Pixel type: unsigned short.


    "Volume" Reader has successfully read the file "/home/sn/samanehjan/workspaceSPHARM/input/sample1_C1_group04.nii" "[0.15s]" 
    Loaded volume from file: /home/sn/samanehjan/workspaceSPHARM/input/sample1_C1_group05.nii. Dimensions: 31x15x17. Number of components: 1. Pixel type: unsigned short.


    "Volume" Reader has successfully read the file "/home/sn/samanehjan/workspaceSPHARM/input/sample1_C1_group05.nii" "[0.03s]" 
    Switch to module:  "Data" 
    Switch to module:  "Segmentations" 
    Switch to module:  "" 
    Switch to module:  "" 
    [sn@localhost ~]$ 
</code></pre>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---
