---
topic_id: 28746
title: "Langchain Query The Complete 3D Slicer Documentation Script"
date: 2023-04-04
url: https://discourse.slicer.org/t/28746
---

# Langchain: Query the complete 3D Slicer documentation, script repository and FAQ (PDF and HTML) with OpenAI LLM

**Topic ID**: 28746
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/langchain-query-the-complete-3d-slicer-documentation-script-repository-and-faq-pdf-and-html-with-openai-llm/28746

---

## Post #1 by @rbumm (2023-04-04 12:55 UTC)

<p>This test implementation enables reading the complete 3D Slicer documentation, including the script repository, from a PDF file, and making it available for queries in an <a href="https://openai.com/">OpenAI</a> LLM using <a href="https://python.langchain.com/en/latest/index.html">Langchain</a>.<br>
The functionality is similar to ChatGPT, but the source is simply this single PDF document.</p>
<p>You’ll need to make a copy of the <a href="https://slicer.readthedocs.io/en/latest/">3D Slicer readthedocs documentation</a> as PDF (or modify the code to scrape it directly) and place it in one of your Google drive folders. In addition, you will need to add your OpenAI secret key to make this functional. It works great.</p>
<p>My highly intelligent prompt engineering <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> includes</p>
<pre><code class="lang-auto">prompts = [
          'What is 3D Slicer?',
          'Is 3D Slicer FDA-approved?',
          'Who is Ron Kirkinis?',
          'Who is Andras Lasso?',
          'Who is Steve Pieper?',
          'Who created 3D Slicer?',
          'What are the main use-cases for 3D Slicer?',
          'Does 3D Slicer support AI?',
          'What is an extension?',
           
          'How can I clone a node? Please provide Python code.',

          'please summarize this document',
          'please summarize chapters 1-12 of this document',
          'please summarize chapter 1 of this document',
          'please summarize chapter 2 of this document',
          'please summarize chapter 3 of this document',
          'please summarize chapter 4 of this document',
          'please summarize chapter 5 of this document',
          'please summarize chapter 6 of this document',
          'please summarize chapter 7 of this document',
          'please summarize chapter 8 of this document',
          'please summarize chapter 9 of this document',
          'please summarize chapter 10 of this document',
          'please summarize chapter 11 of this document',
          'please summarize chapter 12 of this document',
           
           ]

</code></pre>
<p>Here is the Colab notebook, please make your copies for testing.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://colab.research.google.com/drive/1pUicN8MtUEnX5gCJmhdAPEhDxMazuBGp?usp=sharing">
  <header class="source">
      <img src="https://ssl.gstatic.com/colaboratory-static/common/a7dbc30dc1e88b1af99a821b1a669082/img/favicon.ico" class="site-icon" width="" height="">

      <a href="https://colab.research.google.com/drive/1pUicN8MtUEnX5gCJmhdAPEhDxMazuBGp?usp=sharing" target="_blank" rel="noopener">colab.research.google.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://colab.research.google.com/img/colab_favicon_256px.png" class="thumbnail" width="" height="">

<h3><a href="https://colab.research.google.com/drive/1pUicN8MtUEnX5gCJmhdAPEhDxMazuBGp?usp=sharing" target="_blank" rel="noopener">Google Colaboratory</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @rbumm (2023-04-04 13:31 UTC)

<p>The answers to my intelliprompts, summarizing the PDF and providing details:</p>
<p><strong>The answer to ‘What is 3D Slicer?’ is:</strong><br>
3D Slicer is a software application for visualization and analysis of medical image computing datasets. All commonly used data sets are supported, such as images, segmentations, surfaces, annotations, transformations, etc., in 2D, 3D, and 4D. Visualization is available on desktop and in virtual reality. Analysis includes segmentation, registration, and various quantifications. It is also a research software platform, which allows researchers to quickly develop and evaluate new methods and distribute them to clinical users. 3D Slicer is completely free and there are no restrictions on how it is used, however, it is not approved for clinical use and the distributed application is intended for research use.</p>
<p><strong>The answer to ‘Is 3D Slicer FDA-approved?’ is:</strong><br>
No, 3D Slicer is not FDA-approved. It is not intended for clinical use and is only intended for research use.</p>
<p><strong>The answer to ‘Who is Ron Kirkinis?’ is:</strong><br>
Ron Kirkinis is one of the major contributors to the 3D Slicer core effort. He is listed as the Principal Investigator in the Acknowledgments section of the 3D Slicer Documentation.</p>
<p><strong>The answer to ‘Who is Andras Lasso?’ is:</strong><br>
Andras Lasso is a benevolent dictator for life in the 3D Slicer community. He can integrate changes to keep the platform healthy and help interpret or address conflict related to the contribution guidelines.</p>
<p><strong>The answer to ‘Who is Steve Pieper?’ is:</strong><br>
Steve Pieper is a Chief Architect for 3D Slicer. He is a major contributor to the core engineering of Slicer and is part of the Slicer team at Isomics. He is also an Associate Professor of Radiology at Harvard Medical School.</p>
<p><strong>The answer to ‘Who created 3D Slicer?’ is:</strong><br>
3D Slicer was created by a international community of scientists from multiple fields, including engineering and biomedicine. Major contributors include Ron Kikinis, Steve Pieper, Jean-Christophe Fillion-Robin, Nicole Aucoin, Stephen Aylward, Andrey Fedorov, Noby Hata, Hans Johnson, Tina Kapur, Gabor Fichtinger, Andras Lasso, Csaba Pinter, Jim Miller, Sonia Pujol, Junichi Tokuda, Lauren O’Donnell, Andinet Enquobahrie, and Beatriz Paniagua. Groups contributing to the core engineering of Slicer in a major way include SPL, Isomics, Kitware, the University of Iowa, GE, and the Perk Lab, Queen’s University.</p>
<p><strong>The answer to ‘What are the main use-cases for 3D Slicer?’ is:</strong><br>
3D Slicer is used for visualization and analysis of medical image computing datasets, prototyping and releasing products, and visualization of DICOM datasets and multi-frame datasets. It is also used for exploration of multivolume data, and to display CT or MRI volumes.</p>
<p><strong>The answer to ‘Does 3D Slicer support AI?’ is:</strong><br>
No, 3D Slicer does not have any built-in support for AI.</p>
<p><strong>The answer to ‘What is an extension?’ is:</strong><br>
An extension is a delivery package bundling together one or more 3DSlicer modules that can be added to 3DSlicer by installing the extension.</p>
<p><strong>The answer to ‘How can I clone a node? Please provide Python code.’ is:</strong></p>
<pre><code class="lang-auto"># Get a node from SampleData that we will clone

import SampleData

nodeToClone = SampleData.SampleDataLogic().downloadMRHead()

# Clone the node

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

itemIDToClone = shNode.GetItemByDataNode(nodeToClone)

clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)

clonedNode = shNode.GetItemDataNode(clonedItemID)
</code></pre>
<p><strong>The answer to ‘please summarize this document’ is:</strong><br>
This document is 3D Slicer Documentation, which contains two chapters. Chapter 1 is about 3D Slicer, and Chapter 2 covers getting started.</p>
<p><strong>The answer to ‘please summarize chapters 1-12 of this document’ is:</strong><br>
Chapters 1-12 of this document provide information about 3D Slicer, such as how to get started and how to use the indices and tables.</p>
<p><strong>The answer to ‘please summarize chapter 1 of this document’ is:</strong><br>
Chapter 1 of the 3D Slicer Documentation is entitled “About 3D Slicer” and gives an overview of the software and its features.</p>
<p><strong>The answer to ‘please summarize chapter 2 of this document’ is:</strong><br>
Chapter 2 of the 3D Slicer Documentation is titled ‘Getting Started’ and provides an introduction to the 3D Slicer software. It covers topics related to how to install and use the software.</p>
<p><strong>The answer to ‘please summarize chapter 3 of this document’ is:</strong><br>
Chapter 3 of the 3D Slicer Documentation covers how to get help with 3D Slicer.<br>
It outlines different types of help, including online help, tutorials, mailing lists, and user groups.</p>
<p><strong>The answer to ‘please summarize chapter 4 of this document’ is:</strong><br>
Chapter 4 of the 3D Slicer Documentation is about the User Interface.<br>
It explains that data sets are stored in a data repository called the “scene” and each data set is<br>
represented in the scene as a node. It also explains that Slicer contains over 100 built-in modules and<br>
additional modules can be installed by using the Extensions Manager.</p>
<p><strong>The answer to ‘please summarize chapter 5 of this document’ is:</strong><br>
Chapter 5 of the 3D Slicer Documentation covers data loading and saving, giving instructions on how to import, export, and manipulate data in 3D Slicer.</p>
<p><strong>The answer to ‘please summarize chapter 6 of this document’ is:</strong><br>
Chapter 6 of the 3D Slicer Documentation is about Image Segmentation. It covers topics related to the segmentation of images using 3D Slicer.</p>
<p><strong>The answer to ‘please summarize chapter 7 of this document’ is:</strong><br>
Chapter 7 of the 3D Slicer Documentation is titled “Registration” and covers topics related to registering images.</p>
<p><strong>The answer to ‘please summarize chapter 8 of this document’ is:</strong><br>
Chapter 8 of this document covers the DICOM module of 3D Slicer. It provides an overview of the module and its features, which include importing, exporting, and network transferring of DICOM data, as well as querying, retrieving, sending, and receiving data sets. The module also supports DIMSE and DICOMweb networking protocols. It is funded by the National Institutes of Health and a Cancer Care Ontario research unit.</p>
<p><strong>The answer to ‘please summarize chapter 9 of this document’ is:</strong><br>
I don’t know.</p>
<p><strong>The answer to ‘please summarize chapter 10 of this document’ is:</strong><br>
Chapter 10 of the 3D Slicer Documentation outlines the various application settings available to the user.</p>
<p><strong>The answer to ‘please summarize chapter 11 of this document’ is:</strong><br>
Chapter 11 of this document is titled Advanced Topics. It covers topics such as using 3D Slicer in research, developing Slicer modules, and creating Slicer packages.</p>
<p><strong>The answer to ‘please summarize chapter 12 of this document’ is:</strong><br>
Chapter 12 of this document is about Indices and Tables. It includes genindex, modindex, and search as topics. It also has a Python Module Index and an Index.</p>

---

## Post #3 by @lassoan (2023-04-04 13:44 UTC)

<p>Very nice, thanks for digging into this. It has huge potential, especially if the model could also incorporate all the discussions on this forum.</p>
<p>Can it also provide links to the source?</p>
<p>It provided some misleading information with great confidence, which may be misleading or even hurt us:</p>
<blockquote>
<p>The answer to ‘Who is Steve Pieper?’ is: Steve Pieper is a Chief Architect for 3D Slicer. … He is also an Associate Professor of Radiology at Harvard Medical School.</p>
</blockquote>
<blockquote>
<p>The answer to ‘Does 3D Slicer support AI?’ is: No, 3D Slicer does not have any built-in support for AI.</p>
</blockquote>
<p>I expect that soon chat interface will be a standard feature on websites and forums, replacing full-text search (in fact, it has been going on for a while, but the earlier free-text query implementations were so poor that they did not get much attention). Discourse already has some <a href="https://meta.discourse.org/t/discourse-chatbot-supporting-chatgpt/256652">experimental plugin for allowing an AI bot to answer questions</a>. This will of course make more sense when it will use a model that gives more weight to content that it finds on the forum.</p>

---

## Post #4 by @rbumm (2023-04-04 13:49 UTC)

<p>The only source was the PDF document imported, but maybe “enriched” with OpenAI contents, so we’ll need to reconstruct why that happens.</p>

---

## Post #5 by @rbumm (2023-04-04 13:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="28746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>especially if the model could also incorporate all the discussions on this forum.</p>
</blockquote>
</aside>
<p>You could import several different sources. <a href="https://python.langchain.com/en/latest/modules/indexes/document_loaders.html">See here</a>:</p>

---

## Post #6 by @rbumm (2023-06-13 08:40 UTC)

<p>I have updated my langchain-based OPENAI LLM Jupyter notebook to version 2 by integrating an agent which queries:</p>
<ul>
<li>3D Slicer PDF</li>
<li>Script repository (simple Webpage)</li>
<li>FAQ (simple Webpage)</li>
</ul>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1TQhK39EYGFN_9sjHrPvorjuHl3FQfQRj/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1TQhK39EYGFN_9sjHrPvorjuHl3FQfQRj/view?usp=sharing" target="_blank" rel="noopener">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1TQhK39EYGFN_9sjHrPvorjuHl3FQfQRj/view?usp=sharing" target="_blank" rel="noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1TQhK39EYGFN_9sjHrPvorjuHl3FQfQRj/view?usp=sharing" target="_blank" rel="noopener">public-slicer-bot-langchain_V2.ipynb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Select “Open with Colab notebook”<br>
You just need to put in your OpenAI API key.</p>

---

## Post #7 by @rbumm (2023-06-13 12:37 UTC)

<p>The latest 3D Slicer documentation in PDF format can be found when you click here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb4155f554f414a5c6a1d578af57eadc354d2c68.png" data-download-href="/uploads/short-url/t04UhoVT1iiz5j0br3yaYCBQm0w.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb4155f554f414a5c6a1d578af57eadc354d2c68_2_163x500.png" alt="image" data-base62-sha1="t04UhoVT1iiz5j0br3yaYCBQm0w" width="163" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb4155f554f414a5c6a1d578af57eadc354d2c68_2_163x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb4155f554f414a5c6a1d578af57eadc354d2c68_2_244x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb4155f554f414a5c6a1d578af57eadc354d2c68.png 2x" data-dominant-color="597EB3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">306×934 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a href="https://slicer.readthedocs.io/en/latest/" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/</a></p>

---

## Post #8 by @rbumm (2023-06-17 13:44 UTC)

<p>There is a new version of the Colab Notebook querying 3D Slicer documentation available.</p>
<p><a href="https://drive.google.com/drive/folders/1doNHe1nCkfIK7zhaIbhcfrIfe6eu4Nbm?usp=sharing" class="onebox" target="_blank" rel="noopener">https://drive.google.com/drive/folders/1doNHe1nCkfIK7zhaIbhcfrIfe6eu4Nbm?usp=sharing</a></p>
<p>There is interaction with:</p>
<p>3D Slicer PDF from readthedocs<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Script Repository</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ">3D Slicer FAQ</a><br>
<a href="https://elib.dlr.de/187800/1/Weber_Jonas_BSc_Thesis.pdf">3D Slicer as a platform for the automatic segmentation of real-time MRI data</a></p>
<p>A simple gradio interface is provided. And we have chat memory (follow up questions) <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98671feacc3a0d0b6efb868abeefae8f227b6a2d.png" data-download-href="/uploads/short-url/lKdwbs7zxjyRKNxdv1Pvv4SByUt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98671feacc3a0d0b6efb868abeefae8f227b6a2d_2_690x306.png" alt="image" data-base62-sha1="lKdwbs7zxjyRKNxdv1Pvv4SByUt" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98671feacc3a0d0b6efb868abeefae8f227b6a2d_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98671feacc3a0d0b6efb868abeefae8f227b6a2d_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98671feacc3a0d0b6efb868abeefae8f227b6a2d_2_1380x612.png 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1639×729 63.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @rbumm (2023-06-18 06:31 UTC)

<p>Also presented are the astounding 3D Slicer citation counts (as of the analysis <a class="mention" href="/u/lassoan">@lassoan</a>).<br>
Could we have an automatic page for this analysis ?</p>
<p>User:<br>
Please comment on the number of citations of 3D Slicer between 2006 and 2022.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/898d3244eafdc948ebc18134872902b62e87de23.png" data-download-href="/uploads/short-url/jCPVmITRJxV62t2rvjFkWYoHU0r.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/898d3244eafdc948ebc18134872902b62e87de23_2_690x389.png" alt="image" data-base62-sha1="jCPVmITRJxV62t2rvjFkWYoHU0r" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/898d3244eafdc948ebc18134872902b62e87de23_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/898d3244eafdc948ebc18134872902b62e87de23_2_1035x583.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/898d3244eafdc948ebc18134872902b62e87de23_2_1380x778.png 2x" data-dominant-color="F8F9FA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1550×874 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could anybody point me to a way to query all 3D Slicer extensions available (short descriptions)?</p>

---

## Post #10 by @lassoan (2023-06-18 12:12 UTC)

<p>You can get information on all extensions for all Slicer versions from the <a href="https://github.com/Slicer/ExtensionsIndex">ExtensionsIndex repository</a>. You can get packages and download counts from the Extensions Catalog (Girder server) - see <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/tree/master/ExtensionStats">ExtensionStats</a>. An easy way to download all extension repositories is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually">build the ExtensionsIndex</a>.</p>

---
