# Segfault when calling destructor on ctkDICOMIndexer and ctkDICOMDatabase

**Topic ID**: 12653
**Date**: 2020-07-21
**URL**: https://discourse.slicer.org/t/segfault-when-calling-destructor-on-ctkdicomindexer-and-ctkdicomdatabase/12653

---

## Post #1 by @Jakew (2020-07-21 00:07 UTC)

<p>I am working on a loadable module extension in which I create a new ctkDICOMIndexer object and a new ctkDICOMDatabase, which I delete in the extension’s destructor. However, when I quit my application, a segfault occurs. I’ve identified that it occurs in the file ctkDICOMIndexer.cpp file in the line “QObject::disconnect(d-&gt;Database, SIGNAL(opened()), this, SLOT(databaseFilenameChanged()));”<br>
Does anyone know what the problem could be?</p>

---

## Post #2 by @lassoan (2020-07-23 02:00 UTC)

<p>Probably when you deleted the database then you forget to set <code>d-&gt;Database</code> to nullptr. Dereferencing a dangling pointer (using then <code>d-&gt;Database</code> after the object is deleted) will cause a segfault. The solution is to set the pointer to nullptr (or use some type of smart pointer) and only disconnect the database if it still exists.</p>

---
