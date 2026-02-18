# How to update cell data of dicom browser?

**Topic ID**: 19477
**Date**: 2021-09-02
**URL**: https://discourse.slicer.org/t/how-to-update-cell-data-of-dicom-browser/19477

---

## Post #1 by @wycstar (2021-09-02 02:29 UTC)

<p>the cell data of dicom browser, for example, patients table, studies table and series table is from the tags of dicom,or the database, but i want to update it temporarily with python</p>

---

## Post #2 by @lassoan (2021-09-02 04:37 UTC)

<p>We used to display the raw DICOM data directly in the browser, but things are better now. We use the database to cache raw DICOM data and there are rules (see <a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM/Core">ctkDICOM*Rule classes</a>) that compute displayed fields from these raw data, which is displayed in the browser.</p>
<p>Still, changing data in the database is not trivial.</p>
<p>One issue is that the database can be requested to be rebuilt by re-indexing the data sets. This typically happens when the database schema is changed, which can occur when you open the database with a newer or older Slicer version. If you just change the data cached in the database then those changes will be lost when the database is rebuilt.</p>
<p>Another issue is that in DICOM it is prohibited to modify a data set. All you can do is to create a modified clone of a data set with a new UID and request hiding of the old data set. You may need to still keep around the old data set so that you can resolve cross-references between data objects.</p>
<p>So, a clear solution would be to create modified clones of the data set (modify the DICOM files) and remove the old version from the database. A somewhat clean solution could be to add a rule that stores a list of field changes and applies that are used for changing the content of displayed fields.</p>
<p>What exactly would you like to achieve?</p>

---

## Post #3 by @wycstar (2021-09-02 05:15 UTC)

<p>thanks Lassoan <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:">, i want to update the display value not the real value in database or tags, this is my code</p>
<pre><code class="lang-auto">dib = slicer.modules.dicom.widgetRepresentation().self().browserWidget.dicomBrowser
db = dib.database()
pm = dib.dicomTableManager().patientsTable().tableView().model()
pm.setData(pm.index(0,1), "1")
</code></pre>
<p>it returns false when i excute the setData, the patient table is a instance of QTableView, i think there is a general method to update the cell value</p>

---

## Post #4 by @lassoan (2021-09-02 05:27 UTC)

<p>I don’t think you can modify a values in the database by manipulating views. You need to run SQL update statements using Python’s or Qt’s SQLite API. Of course it is just a hack, but if you develop a locked-down custom application then you may be able to ensure that there are no side effects of such low-level manipulations.</p>

---

## Post #5 by @wycstar (2021-09-02 08:29 UTC)

<p>OK i will try it thanks</p>

---
