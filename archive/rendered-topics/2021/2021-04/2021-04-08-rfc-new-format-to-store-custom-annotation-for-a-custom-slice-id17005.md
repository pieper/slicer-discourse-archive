---
topic_id: 17005
title: "Rfc New Format To Store Custom Annotation For A Custom Slice"
date: 2021-04-08
url: https://discourse.slicer.org/t/17005
---

# RFC: New "format" to store custom annotation for a custom slicer application

**Topic ID**: 17005
**Date**: 2021-04-08
**URL**: https://discourse.slicer.org/t/rfc-new-format-to-store-custom-annotation-for-a-custom-slicer-application/17005

---

## Post #1 by @jcfr (2021-04-08 17:58 UTC)

<p>In the context of the <a href="https://github.com/BICCN/cell-locator#readme">Cell Locator</a> project, a Slicer-based custom  application to manually aligning specimens to annotated 3D spaces, we developed a json-based format to store annotation.</p>
<h3><a name="p-57669-current-1" class="anchor" href="#p-57669-current-1" aria-label="Heading link"></a>Current</h3>
<p>Until now the format has been used internally to the application</p>
<p>The current cell-locator format is similar to the markup json format expect it removes/includes few additional properties.</p>
<p>See <a href="https://github.com/BICCN/cell-locator/blob/master/Documentation/AnnotationFileFormat.md#2020-09-18">https://github.com/BICCN/cell-locator/blob/master/Documentation/AnnotationFileFormat.md#2020-09-18</a></p>
<h3><a name="p-57669-proposed-plan-2" class="anchor" href="#p-57669-proposed-plan-2" aria-label="Heading link"></a>Proposed plan</h3>
<p>To support the reading/loading of annotation by other application, we are now considering the following:</p>
<ol>
<li>
<p>“standardizing” it by including version information and schema similarly to what we already do for the json file associated with markups (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.1.json">markups-schema-v1.0.1.json</a>)</p>
</li>
<li>
<p>creating standalone python  tool for converting between version and streamline batch migration</p>
</li>
<li>
<p>ensure the application automatically convert older format to newer ones.</p>
</li>
</ol>
<h3><a name="p-57669-questions-3" class="anchor" href="#p-57669-questions-3" aria-label="Heading link"></a>Questions</h3>
<ul>
<li>Should we consider building on existing format or standard ?</li>
</ul>

---

## Post #2 by @pieper (2021-04-08 18:19 UTC)

<p>This is a very timely question.  There are similar efforts around dicom SR encodings of annotations and quantitative results which may share some interests but maybe not others.  Doing something application-specific is easiest to maintain of course, but I would love to see it standardized.</p>

---
