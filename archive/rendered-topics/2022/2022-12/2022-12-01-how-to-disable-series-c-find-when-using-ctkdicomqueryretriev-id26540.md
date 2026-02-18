# How to disable Series C-FIND when using ctkDICOMQueryRetrieveWidget queries?

**Topic ID**: 26540
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/how-to-disable-series-c-find-when-using-ctkdicomqueryretrievewidget-queries/26540

---

## Post #1 by @Gabriel_WK (2022-12-01 17:10 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.3.0-2022-11-27</p>
<p>I can’t find a way to do “Study level only” queries when using ctkDICOMQueryRetrieveWidget. The behaviour I would like to achieve is one where simple initial queries by date are a single operation that quickly returns a list of studies from a PACS server.</p>
<p>This use case doesn’t include the need to retrieve only some series from a study. It always downloads every series from selected studies. The user may download only one or a few studies so information about every series from every study is unecessary.</p>
<p>The drawback with how ctkDICOMQueryRetrieveWidget queries by default is that it may take several seconds to get a list of studies with anything more than a few dozen studies as it performs a Series C-FIND for every study that’s initially queried.</p>
<p>Is there a way to disable Series C-FIND when querying from the DICOM Query/Retrieve window?</p>

---

## Post #2 by @pieper (2022-12-01 19:40 UTC)

<p>I don’t believe there’s a way to configure that currently, but since you sound knowledgable about the DICOM part side of the problem the I think making the corresponding changes to the ctkDICOM implementation is probably not that difficult.  Maybe you could take a look at <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMQuery.cpp">the c++ code</a> to get an idea what would be involved.</p>

---

## Post #3 by @Gabriel_WK (2022-12-01 20:21 UTC)

<p>That did cross my mind but I’m not sure how I should proceed in this case specifically because CTK is not part of Slicer. That would involve compiling a custom CTK, right? I can compile it but I don’t know how to make my Slicer build point to it. Are there any resources I can take a look at to understand how Slicer bundles CTK and how I could swap it for my custom build? CTK seems to be deeply intertwined with Slicer during build and I’m not yet completely familiar with how exactly the whole cmake process works.</p>

---

## Post #4 by @pieper (2022-12-01 22:24 UTC)

<p>Yes, it’s actually quite easy.  If you do a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">conventional Slicer build</a> on any platform it will checkout and build CTK from source as part of the process.  You can make your own fork of CTK and <a href="https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_CTK.cmake#L68-L78">point Slicer to it during the build</a>.  From there you can edit the code and rebuild to test in Slicer.  Then you can make a pull request to CTK and we can update Slicer to use the new version once it’s integrated (several of us work on both CTK and Slicer).</p>

---
