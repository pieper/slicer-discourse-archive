---
topic_id: 5589
title: "Loadable Module Itk Filters I O"
date: 2019-01-31
url: https://discourse.slicer.org/t/5589
---

# Loadable module ITK filters I/O

**Topic ID**: 5589
**Date**: 2019-01-31
**URL**: https://discourse.slicer.org/t/loadable-module-itk-filters-i-o/5589

---

## Post #1 by @Amn3s14 (2019-01-31 03:22 UTC)

<p>Hello, I am new to Slicer and ITK. I am trying to perform one of the SimpleFilters in my c++ module, but am having trouble getting the right input/output for ITK.</p>
<pre><code>const int dim = 3;

typedef unsigned char PType;
typedef itk::Image&lt; PType, dim &gt; IType;

typedef itk::ImageFileReader&lt; IType &gt; ReaderType;
ReaderType::Pointer reader = ReaderType::New();
reader-&gt;SetFileName(d-&gt;InputVolumeNode-&gt;GetID());

typedef itk::MeanProjectionImageFilter&lt; IType, IType &gt; FilterType;
FilterType::Pointer filter = FilterType::New();
filter-&gt;SetInput(reader-&gt;GetOutput());

itk::SimpleFilterWatcher watcher(filter, "filter");

typedef itk::ImageFileWriter&lt; IType &gt; WriterType;
WriterType::Pointer writer = WriterType::New();
writer-&gt;SetInput(filter-&gt;GetOutput());
writer-&gt;SetFileName(d-&gt;OutputVolumeNode-&gt;GetID());
writer-&gt;Update();
</code></pre>
<p>Both InputVolumeNode and OutputVolumeNode are vtkMRMLScalarVolumeNodes. I am assuming I need to convert to MRMLIDImageIO or similar but am having trouble with the code to do so. Any help would be greatly appreciated.</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.10.0</p>

---

## Post #2 by @lassoan (2019-02-02 02:58 UTC)

<p>You need to add this line to <code>CMakeLists.txt</code> file of your module:</p>
<pre><code>set(ITK_NO_IO_FACTORY_REGISTER_MANAGER 1) # See Libs/ITKFactoryRegistration/CMakeLists.txt 
</code></pre>
<p>See source code of all CLI modules as examples: <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI" rel="nofollow noopener">https://github.com/Slicer/Slicer/tree/master/Modules/CLI</a></p>

---
