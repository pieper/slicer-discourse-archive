# Table columns customization

**Topic ID**: 436
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/table-columns-customization/436

---

## Post #1 by @lassoan (2017-06-02 20:45 UTC)

<p>Slicer supports loading/saving/editing of spreadsheets (.csv, .txt, .tsv files) for a while now, but there was no standard way of specifying data type, unit (mm, cm3, …), default value, or custom properties for the stored data.</p>
<p>We have recently introduced table column <code>properties</code>, which:</p>
<ul>
<li>can be used for customizing how data is displayed (for example, <code>bit</code> type columns are shown as checkboxes)</li>
<li>what default values should be used for new rows</li>
<li>long description, human-readable name can be specified, which are displayed in the tooltip in table views</li>
<li>any number of custom properties can be defined (useful for developers, maybe will be also exposed for users in some way)</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e50eeebb367d2c1be6ebecb696f4272d9888322d.png" width="335" height="208"></p>
<p>To get started, create a <code>schema</code> file for your table (file that has the same name as your table file, with <code>.schema</code> inserted before the extension) and load your table into Slicer to view it. See more details in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Tables#Table_column_properties">Table node API documentation</a>.</p>
<p>Any questions and suggestions are welcome.</p>

---

## Post #2 by @Ash_Alarfaj (2018-06-21 12:39 UTC)

<p>Hi<br>
I am not a programmer, I am a keen user of 3d slicer, how can I get  the area  measurements(mm2) of MRI  images because I got only volume. and my images are 5 mm thickness so when I compare my result with another software it doesn’t mach?</p>

---

## Post #3 by @lassoan (2018-06-21 15:10 UTC)

<p>If you need area of a single slice then dividing the volume with the slice thickness will give you the correct result. If you can share a data set with segmentation (you can use any of the Slicer sample data sets) and quantification result that you got with other software then we can check what could cause the difference.</p>

---
