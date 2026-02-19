---
topic_id: 4635
title: "Batch Structure Set Conversion"
date: 2018-11-05
url: https://discourse.slicer.org/t/4635
---

# Batch Structure Set Conversion

**Topic ID**: 4635
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/batch-structure-set-conversion/4635

---

## Post #1 by @stine (2018-11-05 09:53 UTC)

<p>Hi!</p>
<p>Since PyRadiomics does not support DICOM-RTSTRUCT as input mask, I am trying to convert the files to labelmaps (.nrrd files). I have more than 100 files, so I was hoping to do this using a batch processing script. I found the BatchStructureSetConversion.py-file and tried the following:</p>
<p>/Applications/Slicer.app/Contents/MacOS/Slicer --no-main-window --python-script [MyPath/]BatchStructureSetConversion.py --input-folder [MyPath] --output-folder [MyPath]</p>
<p>However, this produces only one .nrrd file (size: 9x10x12), and the size/dimensions does not correspond to that of the PET images…</p>
<p>My input folder contains one subfolder for each patient where the PET DICOM-RT files and the DICOM-RTSTRUCT file are stored together (data from the MICCAI 2018 PET Radiomics Challenge). Could the problem be the folder structure or the file types? I am really stuck on this problem and any help would be much appreciated!</p>
<p>Best regards,<br>
Stine</p>
<p>Slicer version: 4.10.0</p>

---

## Post #2 by @pieper (2018-11-05 13:15 UTC)

<p>Hi -</p>
<p>I assume you are talking about <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py">this script</a>, right?  Since this is public data, it would be great if you can set up a simple test case that’s easy to reproduce and file an issue.</p>
<p>Ideally your test case should automatically download the data files to reproduce the issue, but if that’s not feasible for you at least include links to the data and the specific versions of the code you are using and the exact steps to reproduce.</p>
<p>Thanks!</p>

---

## Post #3 by @stine (2018-11-05 14:08 UTC)

<p>Thank you so much for the quick reply! That’s the script, yes.</p>
<p>I’m sorry but I’m very new to this and I don’t know how to set up that type of test case. I have downloaded a folder (named Training) containing a number of subfolders (one for each patient) where the PET slices and the segmentation contour data (.DCM file) are stored together. I’m trying to obtain a labelmap/binary segmentation mask for each patient.</p>
<p>Here is the link to the data I’m using (the Training.zip-folder): <a href="https://www.kaggle.com/c/pet-radiomics-challenges/data" rel="nofollow noopener">https://www.kaggle.com/c/pet-radiomics-challenges/data</a>.</p>
<p>I have the latest version of the BatchStructureSetConversion.py script and I used the entire Training-folder as input:</p>
<p>/Applications/Slicer.app/Contents/MacOS/Slicer --no-main-window --python-script [path/to/batch-script/]BatchStructureSetConversion.py --input-folder [path/to/Training-folder] --output-folder [path/to/empty/folder]</p>
<p>I hope that this helps explaining my problem.</p>

---

## Post #4 by @cpinter (2018-11-05 14:49 UTC)

<p>Do you see any errors in the output or the log?</p>

---

## Post #5 by @stine (2018-11-05 18:58 UTC)

<p>When I run the script on a subset of 3 patients (HN-MICCAI2018-0002, HN-MICCAI2018-0004 and HN-MICCAI2018-0005) I get the following output (in addition to one .nrrd file):</p>
<p>Import DICOM data from /Users/stine/PycharmProjects/radiomics/data/PET/TrainingSUB<br>
Switching to temporary DICOM database: /var/folders/1p/dw77r3v93yvbpqkp6vj9wtnm0000gn/T/Slicer-stine/20181105_185446_TempDICOMDatabase<br>
Original DICOM database: /var/folders/1p/dw77r3v93yvbpqkp6vj9wtnm0000gn/T/Slicer-stine/20181105_184533_TempDICOMDatabase<br>
Failed to obtain reference to ‘qSlicerMainWindow’<br>
Failed to obtain reference to ‘qSlicerMainWindow’<br>
QSqlDatabasePrivate::removeDatabase: connection ‘SLICER’ is still in use, all queries will cease to work.<br>
QSqlDatabasePrivate::addDatabase: duplicate connection name ‘SLICER’, old connection removed.<br>
TagCacheDatabase adding table</p>
<p>QSqlDatabasePrivate::removeDatabase: connection ‘SLICER’ is still in use, all queries will cease to work.<br>
QSqlDatabasePrivate::addDatabase: duplicate connection name ‘SLICER’, old connection removed.<br>
QSqlDatabasePrivate::removeDatabase: connection ‘SLICER’ is still in use, all queries will cease to work.<br>
QSqlDatabasePrivate::addDatabase: duplicate connection name ‘SLICER’, old connection removed.<br>
Failed to obtain reference to ‘qSlicerMainWindow’<br>
Could not find main window<br>
Could not find moduleSelector in the main window<br>
E: DcmElement: CommandField (0000,0100) larger (828667202) than remaining bytes in file<br>
Could not load  “/Users/stine/PycharmProjects/radiomics/data/PET/TrainingSUB/.DS_Store”<br>
DCMTK says:  I/O suspension or premature end of stream<br>
Could not read DICOM file:/Users/stine/PycharmProjects/radiomics/data/PET/TrainingSUB/.DS_Store<br>
New patient inserted: 1<br>
New patient inserted as :  1<br>
Need to insert new study:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.916101888211223106723732084398”<br>
Study Added<br>
Need to insert new series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
E: DcmElement: CommandField (0000,0100) larger (828667202) than remaining bytes in file<br>
Could not load  “/Users/stine/PycharmProjects/radiomics/data/PET/TrainingSUB/HN-MICCAI2018-0002/.DS_Store”<br>
DCMTK says:  I/O suspension or premature end of stream<br>
Could not read DICOM file:/Users/stine/PycharmProjects/radiomics/data/PET/TrainingSUB/HN-MICCAI2018-0002/.DS_Store<br>
New patient inserted: 2<br>
New patient inserted as :  2<br>
Need to insert new series:  “1.2.276.0.7230010.3.1.4.4252153939.211348.1528745918.141”<br>
Series Added<br>
Found patient in the database as UId:  1<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.276182720375307817025066820423”<br>
Series Added<br>
New patient inserted: 3<br>
New patient inserted as :  3<br>
Need to insert new study:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338589861935722567365981799683”<br>
Study Added<br>
Need to insert new series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
New patient inserted: 4<br>
New patient inserted as :  4<br>
Need to insert new series:  “1.2.276.0.7230010.3.1.4.4252153939.211348.1528746083.145”<br>
Series Added<br>
Found patient in the database as UId:  3<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.397286022729450579606108175191”<br>
Series Added<br>
New patient inserted: 5<br>
New patient inserted as :  5<br>
Need to insert new study:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.563642908585179401817164347275”<br>
Study Added<br>
Need to insert new series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
New patient inserted: 6<br>
New patient inserted as :  6<br>
Need to insert new series:  “1.2.276.0.7230010.3.1.4.4252153939.211348.1528746059.143”<br>
Series Added<br>
Found patient in the database as UId:  5<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
Used existing series:  “1.3.6.1.4.1.14519.5.2.1.1707.8040.338955629943308958335236734341”<br>
Series Added<br>
“DICOM indexer has successfully processed 298 files [1.90s]”<br>
Load first patient into Slicer<br>
reg inside examine<br>
W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
reg inside examine<br>
W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
Loading series ‘1: RTSTRUCT: MICCAI2018’ from file ‘/Users/stine/PycharmProjects/radiomics/data/PET/TrainingSUB/HN-MICCAI2018-0002/MICCAI2018.DCM’<br>
W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=6857.729132, width=13715.458265) has been applied to volume 65690: LOR-RAMLA<br>
Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 8.00488e-06 mm, tolerance threshold is 0.001 mm).<br>
Convert loaded structure set to labelmap volumes<br>
Converting structure set 1: RTSTRUCT: MICCAI2018<br>
Save labelmaps to directory /Users/stine/PycharmProjects/radiomics/data/PET/TrainingNRRD<br>
Saving structure 1: RTSTRUCT: MICCAI2018_GTVp<br>
to file 1_RTSTRUCT_MICCAI2018_GTVp.nrrd<br>
Generic Warning: In /Volumes/Dashboards/Stable/Slicer-4100/Libs/MRML/Core/vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nrrd</p>
<p>DONE<br>
Segmentation fault: 11</p>

---

## Post #6 by @stine (2018-11-07 15:14 UTC)

<p>I’m thinking that the folder structure and/or the file types might be the problem. What does the script expect? How should the data files be arranged within the input folder, and what format should the PET images have?</p>

---

## Post #7 by @cpinter (2018-11-07 15:53 UTC)

<p>The folder you specify simply needs to contain DICOM data. The script creates a database there, imports all the DICOM in the folder, and processes each patient one by one. In each patient it will iterate through the structure sets, and within those the structures, and saves each as a labelmap with the geometry of the referenced anatomical image.</p>
<p>Unfortunately the log shows nothing interesting.</p>
<p>What happens if you:</p>
<ul>
<li>Open Slicer, open the DICOM browser</li>
<li>Import one of the studies you want to convert</li>
<li>Load the study to Slicer (make sure you have SlicerRT extension installed)</li>
<li>Go to Segmentations module</li>
<li>Open the section called Export/import models and labelmaps</li>
<li>Open Advanced, make sure the reference volume is the anatomical image you want (let us know if it’s not the proper one by default)</li>
<li>Click Export</li>
<li>Show the resulting labelmap in the slice views. If you’re not sure how to do it then go to the Data module and click the show icon in the row of the labelmap ( called [StructureSetName]-label)</li>
</ul>
<p>Does it look OK?</p>

---

## Post #8 by @stine (2018-11-07 19:32 UTC)

<p>Okey, but the input folder can contain subfolders for each patient?</p>
<p>The procedure described above produces a labelmap that looks good and the default reference volume is correct (there is only one option except for the “None”-option).</p>

---

## Post #9 by @cpinter (2018-11-07 21:24 UTC)

<p>I don’t think it matters how the folders are arranged within the input folder. As long as it can be imported into a DICOM database, it’s fine.</p>
<p>Batch Structure Set Conversion works basically the same way the steps above that produced a good labelmap. So not sure what goes wrong with your data without seeing it.</p>

---
