# Proposition: Name volumes imported via Data by Series description

**Topic ID**: 9779
**Date**: 2020-01-11
**URL**: https://discourse.slicer.org/t/proposition-name-volumes-imported-via-data-by-series-description/9779

---

## Post #1 by @Amine (2020-01-11 16:54 UTC)

<p>Currently, volumes added via the Data module will get their name from the first file of the set, while data added via DICOM database will have the series number followed by series description:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62e03bb3bccb369710edad699fa3b24677768857.jpeg" alt="example" data-base62-sha1="e6HcZu6OQB9bt38wvqDcocBNXBJ" width="363" height="194"></p>
<p>My proposition is to extend the volume naming style of DICOM database module to the Data module, as it makes working with temporary data (without adding it to the database) a lot easier,<br>
Maybe it is more practical for some volumes to be imported with their file names (generally single files) so this could only concern multiple-file volumes that have DICOM metadata<br>
thanks for considering this!</p>

---

## Post #2 by @lassoan (2020-01-11 18:13 UTC)

<p>Add data dialog can load many DICOM images but very limited overall (does not work correctly for many object types, does not give access to DICOM fields, ignores cross-references, cannot load data that spans multiple folders, etc). DICOM module should be used for loading all DICOM data. Maybe we should disable DICOM loading by “Add data” to avoid redundancy and confusion.</p>

---

## Post #3 by @Amine (2020-01-11 18:50 UTC)

<p>You mean the data module dicom import is inferior to the dicom browser in other aspects as well, then as an alternative, Add data could use the dicom module to load dicom files (without adding them to the database), so as to keep a unique dicom importing method</p>
<p>The idea being that it’s important to be able to drag and drop data (whole folder) and import the volumes inside it as good as the dicom module would, this is would be an interesting addition since i think some users would prefer adding data “on the go” without having to load in the database first.</p>

---

## Post #4 by @lassoan (2020-01-11 19:26 UTC)

<p>We could add an option to the DICOM browser to use an in-memory database instead of using a file. That way, you would not need to manually clean up after you finished but everything would be automatically deleted when you quit the application.</p>

---

## Post #5 by @Amine (2020-01-11 19:59 UTC)

<p>Yes that’s the concept, when data is drag-dropped on slicer a window asks if it should be added to dicom database or not, what i suggest is simple: if the users choses to not add it (currently corresponds to “Any data”) the volumes should be imported as good as if it was added then opened.</p>

---

## Post #6 by @lassoan (2020-01-11 20:52 UTC)

<p>Unfortunately, a general-purpose DICOM data loader always requires additional information from the user due to ambiguities in the DICOM standard. Also, indexing and allowing access to all DICOM metadata after the data is loaded is necessary because DICOM heavily relies on cross-references between series, so you need to keep around the DICOM database while you are processing the data.</p>
<p>While we cannot offer one-click DICOM import without loss of generality and breaking some features, it is certainly feasible to make assumptions if you work in a specific application domain. You can create a new loading plugin that would take over DICOM loading, and would load the data without asking anything or storing anything persistently.</p>

---

## Post #7 by @Amine (2020-01-11 22:39 UTC)

<p>Thanks for the clarification, in that case the only way to keep doing that kind of import without locally developping a module would be to keep using Add data, wich is limited by the naming method of the volumes.</p>
<p>It would be great if at least the volumes that have metadata get their names changed to their series description (as in my example picture). It will not change the core interactions as it appears.</p>

---

## Post #8 by @lassoan (2020-01-11 23:27 UTC)

<p>Generating name might look like a simple thing, but actually it is a really complex logic, because depending on what kind of data you load, different DICOM fields contain series name and description.</p>
<p>The new DICOM browser in Slicer preview releases is very fast, data is loaded in the background, newly imported data appears at the top, and you can load a complete patient, series, or study by double-clicking on it. Please try it and let us know what aspects do you find still too complex or inconvenient.</p>

---

## Post #9 by @Amine (2020-01-12 16:01 UTC)

<p>The new DICOM browser is excellent, the only thing i pointed out is about the lack of possibility to load data without having to manually open it from the DICOM browser and clean up afterwards.<br>
Here is are steps i took that did exactly the same result as what i suggested, these could handle the majority of common cases with no user input:</p>
<ol>
<li>Drag and drop data, and select “load directory into DICOM database”</li>
<li>Go into DICOM browser, select the newly loaded patient/series and import it</li>
<li>Delete the patient/series from DICOM browser</li>
</ol>
<p>As you can see there was no additional input from me versus if 3D Slicer performed the above steps automatically, it would make the process more flexible if the user wishes to skip these steps (also more beginner friendly)<br>
Practically, along with “load directory into DICOM database” in the popup list (first step) there simply needs to be an option to perform these steps automatically, something like “Load volumes without adding to Database” (separate option, or handles the volume loading of the current “Any data” option)</p>

---

## Post #10 by @lassoan (2020-01-12 17:51 UTC)

<p>I think patient/study/series selection is useful and as far as I remember, DICOM import includes this step in all applications that I have seen. Maybe applying a filter that would only show the newly imported data sets by default would help? (unfortunately, it would not be easy to implement)</p>
<p>I agree that persistence is not always desired and manual deletion is an extra step that we could eliminate. Maybe by default the DICOM database could be in-memory. That way users would not need to worry about deleting the data after importing. Would this help?</p>

---

## Post #11 by @Amine (2020-01-12 19:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="9779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think patient/study/series selection is useful</p>
</blockquote>
</aside>
<p>It is indeed, my suggestion is to keep it and give more freedom in the case users occasionally prefer to manage their data differently. An example of an application that has this functionality is “MicroDicom viewer”, (PS: they load the data directly without asking if it should be added to the database or not, which would not a good thing in slicer as you said)</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="9779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe by default the DICOM database could be in-memory</p>
</blockquote>
</aside>
<p>The current way of handling the DICOM database is great, if such a function was added, it would be better to only place the dicom database in-memory if the users choses it upon import.</p>
<p>Alternatively, here is a way i think would be based on the existing DICOM database logic with minor additions:</p>
<ol start="0">
<li>Once the “Load volumes without adding to Database” or such option is chosen upon import:</li>
<li>add the entries to the database as usual, and keep two lists: one containing all the entries that the user tried to import, and a second list only containing the new entries (that were not part of the database, only those will be removed afterwards)<br>
(the purpose of having two lists is to not cause a conflict in case some of the the imported files were already present in the database)</li>
<li>import the entries in the first list (Pre-existent + new) from the dicom database</li>
<li>delete the entries  in the second list (new only) from the dicom database</li>
</ol>

---

## Post #12 by @pieper (2020-01-12 22:55 UTC)

<p><a class="mention" href="/u/amine">@Amine</a> have you tried dropping a folder on Slicer?  In that case the default is to load it to DICOM (but you also have the option of going the add data path).  It sounds like what you’d like is a third option that would load to a temp database that would go away when you close the app (or maybe close the scene).  It would also be nice to have an easy option to move the database to a permanent directory if the user wants to keep it.  I agree that could save some steps, I currently tend to create a new database manually when importing a new data collection (e.g. a bunch of stuff downloaded from TCIA or a PACS).</p>
<p>Currently we have this menu:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a9b65531984dd122dd66204f8def1c99abb5b3.png" alt="image" data-base62-sha1="uCZMHkZFuY1RsN4UTm5okRvLmHp" width="292" height="120"></p>
<p>Maybe it could be:</p>
<ul>
<li>Load directory into existing DICOM database</li>
<li>Load directory into a temporary DICOM database</li>
<li>Select new DICOM database location and load directory…</li>
<li>Load directory with Add Data dialog</li>
</ul>

---

## Post #13 by @Amine (2020-01-13 16:47 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Indeed drag and drop is what i’m trying to improve, the “any data” option uses the Data module which does not import DICOMs as good as  the DICOM browser as <a class="mention" href="/u/lassoan">@lassoan</a> pointed out. The “Load directory into dicom database” option is fine but requires extra steps (go in DICOM browser, import, then delete)</p>
<p>As of your proposition, these would be the ideal options when dropping a folder on slicer:</p>
<ul>
<li>Load directory into DICOM database.</li>
<li><em>Load directory into temporary DICOM database.</em></li>
<li>
<em>Select new DICOM database location and load directory</em> <strong>(PS: for this option and the ones above, a pop up asking if the newly added entries should be imported in the scene would be great.)</strong>
</li>
<li>Any data: since its DICOM importing functions are not as good as DICOM browser, maybe these functions could be replaced by loading into temporary database and importing directly afterwards.</li>
</ul>

---
