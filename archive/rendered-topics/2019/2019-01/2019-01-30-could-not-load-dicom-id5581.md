---
topic_id: 5581
title: "Could Not Load Dicom"
date: 2019-01-30
url: https://discourse.slicer.org/t/5581
---

# Could not load: DICOM

**Topic ID**: 5581
**Date**: 2019-01-30
**URL**: https://discourse.slicer.org/t/could-not-load-dicom/5581

---

## Post #1 by @alide (2019-01-30 15:55 UTC)

<p>Hi,</p>
<p>I am not able to load DICOM files from SPECT or CT. They seem to be imported fine, but when I try to load them to Slicer I get the follwing error message: “3d slicer could not load as a scalar volume”. I can not see anything missing in the DICOM tag (copied below). Any ideas about what the problem may be?</p>
<p>0002,0002  Media Storage SOP Class UID: 1.2.840.10008.5.1.4.1.1.20<br>
0002,0003  Media Storage SOP Inst UID: 1.2.840.113619.2.281.41170.172195628.1542268821.17567462<br>
0002,0010  Transfer Syntax UID: 1.2.840.10008.1.2.1<br>
0002,0012  Implementation Class UID: 1.2.840.113619.6.281<br>
0002,0013  Implementation Version Name: Xeleris 4.1170<br>
0002,0016  Source Application Entity Title: UNN-TOS-23888<br>
0008,0005  Specific Character Set: ISO_IR 100<br>
0008,0008  Image Type: DERIVED\PRIMARY\RECON TOMO\EMISSION<br>
0008,0012  Instance Creation Date: 20181115<br>
0008,0013  Instance Creation Time: 090351.0000<br>
0008,0014  Instance Creator UID: 1.2.840.113619.6.281<br>
0008,0016  SOP Class UID: 1.2.840.10008.5.1.4.1.1.20<br>
0008,0018  SOP Instance UID: 1.2.840.113619.2.281.41170.172195628.1542268821.17567462<br>
0008,0020  Study Date: 20181101<br>
0008,0021  Series Date: 20181115<br>
0008,0022  Acquisition Date: 20181101<br>
0008,0023  Image Date: 20181115<br>
0008,0030  Study Time: 155643.00<br>
0008,0031  Series Time: 090251.00<br>
0008,0032  Acquisition Time: 161231.00<br>
0008,0033  Image Time: 090251.00<br>
0008,0050  Accession Number:<br>
0008,0060  Modality: OT<br>
0008,0070  Manufacturer: GE MEDICAL SYSTEMS<br>
0008,0080  Institution Name: UNN<br>
0008,0090  Referring Physician’s Name:<br>
0008,1010  Station Name: UNN-TOS-23888<br>
0008,1030  Study Description: I131 Helkropp<br>
0008,103E  Series Description: 011118-QVolMI-TOMO64-OSEM8it6subNonePF-RR-SC-ACM<br>
0008,1060  Name of Physician(s) Reading Study:<br>
0008,1070  Operator’s Name:<br>
0008,1090  Manufacturer’s Model Name: Tandem_Discovery_670<br>
0009,0010  —: GEMS_GENIE_1<br>
0009,1001  —: GEMS_GENIE<br>
0009,1010  —: I131 Helkropp<br>
0009,1020  —: 011118-QVolMI-TOMO64-OSEM8it6subNonePF-RR-SC-ACM<br>
0009,102E  —: 0.0<br>
0009,1033  —: 0.0<br>
0009,1040  —: Fysiker^Tumordosimetri^^^<br>
0009,1045  —: **<br>
0010,0010  Patient’s Name: Fysiker^Tumordosimetri^^^<br>
0010,0020  Patient ID: 111111111<br>
0010,0030  Patient’s Birth Date:<br>
0010,0040  Patient’s Sex: O<br>
0010,1000  Other Patient IDs:<br>
0010,1001  Other Patient Names:<br>
0010,1020  Patient’s Size: 0<br>
0010,1030  Patient’s Weight: 0<br>
0010,2180  Occupation:<br>
0011,0010  —: GEMS_GENIE_1<br>
0011,100D  —: I131 SC[364 and 297]<br>
0011,1012  —: TOMO_EM_IRACSCRR<br>
0011,1019  —: 0.0<br>
0011,102C  —: 0.0<br>
0011,102D  —: 0.0<br>
0011,1030  —: TOMO_EM_IRACSCRR<br>
0011,1031  —: 1.2.840.113619.2.280.2.1.1112018161006936.448906538<br>
0011,1032  —: 1.2.840.113619.2.280.2.1.1112018161007009.1688277019<br>
0011,1033  —: **<br>
0011,1034  —: **<br>
0011,1035  —: **<br>
0011,1036  —: **<br>
0011,1037  —: **<br>
0011,103B  —: 4.179501533508301<br>
0011,103C  —: 0.0<br>
0011,1040  —: current<br>
0011,1042  —: 0.0<br>
0011,1044  —: 2048.0<br>
0011,1045  —: 4096.0<br>
0011,1050  —: TOMO_EM_IRACSCRR<br>
0011,1055  —: 1.0<br>
0011,1056  —: 1.0<br>
0011,1065  —: **<br>
0011,1066  —: **<br>
0011,1073  —: 0.0<br>
0011,1074  —: 0.0<br>
0011,1075  —: 0.0<br>
0011,1079  —: **<br>
0011,107A  —: **<br>
0011,107B  —: **<br>
0011,107C  —: **<br>
0011,107D  —: **<br>
0011,107F  —: 0.0<br>
0011,1081  —: **<br>
0011,1082  —: 0.0<br>
0011,1083  —: 0.0<br>
0011,1084  —: 0.0<br>
0011,1089  —: 0.0<br>
0013,0010  —: GEMS_GENIE_1<br>
0013,1015  —: 0.0<br>
0013,101B  —: 0.0<br>
0013,1023  —: **<br>
0015,0010  —: GEMS_GENIE_1<br>
0018,0015  Body Part Examined: BREAST<br>
0018,0050  Slice Thickness: 8.83612<br>
0018,0070  Counts Accumulated: 30538138<br>
0018,0071  Acquisition Termination Condition: TIME<br>
0018,0088  Spacing Between Slices: -8.83612<br>
0018,1000  Device Serial Number: 21211<br>
0018,1020  Software Versions(s): Xeleris 4.1170<br>
0018,1030  Protocol Name: User&amp;Endocrine&amp;I131 Helkropp<br>
0018,1061  Trigger Source or Type: EKG<br>
0018,1243  Count Rate: 18800<br>
0020,000D  Study Instance UID: 1.2.840.113619.2.280.2.1.1112018153531658.1085622450<br>
0020,000E  Series Instance UID: 1.2.840.113619.2.281.41170.172195628.1542268971.8516410<br>
0020,0010  Study ID: I131 Helkropp<br>
0020,0011  Series Number: 13<br>
0020,0013  Image Number: 4<br>
0020,0052  Frame of Reference UID: 1.2.840.113619.2.280.2.1.1112018161006936.1221307431<br>
0020,1040  Position Reference Indicator:<br>
0020,4000  Image Comments: $ProcessingParentUID1$1.2.840.113619.2.280.2.1.1112018161007009.1688277019.1$ProcessingParentUID2$1.2.840.113619.2.55.3.330057735.135.1541055674.17.1$OrgModality:NM$CrystalThickness$3$MultProj$1$ReconCorr$ACSCRR$ReconFilter$None$ReconMethod$OSEM (8x6)<br>
0028,0002  Samples per Pixel: 1<br>
0028,0004  Photometric Interpretation: MONOCHROME2<br>
0028,0008  Number of Frames: 64<br>
0028,0009  Frame Increment Pointer: T €<br>
0028,0010  Rows: 64<br>
0028,0011  Columns: 64<br>
0028,0030  Pixel Spacing: 8.836120\8.836120<br>
0028,0051  Corrected Image: ATTN<br>
0028,0100  Bits Allocated: 16<br>
0028,0101  Bits Stored: 16<br>
0028,0102  High Bit: 15<br>
0028,0103  Pixel Representation: 1<br>
0028,0106  Smallest Image Pixel Value:<br>
0028,0107  Largest Image Pixel Value:<br>
0028,1050  Window Center: 68460.235119<br>
0028,1051  Window Width: 136920.470238<br>
0033,0010  —: GEMS_GENIE_1<br>
0033,0011  —: GEMS_XELPRV_01<br>
0033,1007  —: 1.2.840.113619.2.281.41170.172195628.1542268821.17567462<br>
0054,0011  Number of Energy Windows: 1<br>
0054,0012  Energy Window Information Sequence:<br>
0054,0013  Energy Window Range Sequence:<br>
0054,0014  Energy Window Lower Limit: 327.6<br>
0054,0015  Energy Window Upper Limit: 400.4<br>
0054,0018  Energy Window Name: I131_EM<br>
0054,0016  Radiopharmaceutical Information Sequence:<br>
0018,0031  Radiopharmaceutical: ATTENUATION MAPS<br>
0018,1071  Radionuclide Volume: 0<br>
0018,1074  Radionuclide Total Dose: 0.000000<br>
0054,0300  Radionuclide Code Sequence:<br>
0054,0021  Number of Detectors: 1<br>
0054,0022  Detector Information Sequence:<br>
0018,1120  Gantry/Detector Tilt: 0<br>
0018,1145  Center of Rotation Offset: 0<br>
0018,1147  Field of View Shape:<br>
0018,1149  Field of View Dimensions(s): 0\0<br>
0018,1180  Collimator/grid Name: HEGP<br>
0018,1181  Collimator Type: PARA<br>
0018,1182  Focal Distance: 0<br>
0018,1183  X Focus Center: 0<br>
0018,1184  Y Focus Center: 0<br>
0020,0032  Image Position (Patient): -272.137780-283.937780\278.337780<br>
0020,0037  Image Orientation (Patient): 1.000000\0.000000\0.000000\0.000000\1.000000\0.000000<br>
0028,0031  Zoom Factor: 1.000000\1.000000<br>
0028,0032  Zoom Center: 0.000000\0.000000<br>
0054,0051  Number of Rotations: 1<br>
0054,0052  Rotation Information Sequence:<br>
0018,1130  Table Height: 0<br>
0018,1131  Table Traverse: 980.1<br>
0018,1140  Rotation Direction: CC<br>
0018,1142  Radial Position: 218.917<br>
0018,1143  Scan Arc: 0<br>
0018,1144  Angular Step: 0<br>
0018,1242  Actual Frame Duration: 30000<br>
0054,0053  Number of Frames in Rotation: 1<br>
0054,0200  Start Angle: 179.99<br>
0054,0080  Slice Vector: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64<br>
0054,0081  Number of Slices: 64<br>
0054,0202  Type of Detector Motion: STEP AND SHOOT<br>
0054,0400  Image ID: TOMO_EM_IRACSCRR<br>
0054,0410  Patient Orientation Code Sequence:<br>
0008,0100  Code Value: F-10450<br>
0008,0102  Coding Scheme Designator: 99SDM<br>
0008,0104  Code Meaning: recumbent<br>
0054,0412  Patient Orientation Modifier Code Sequence:<br>
0008,0100  Code Value: F-10340<br>
0008,0102  Coding Scheme Designator: 99SDM<br>
0008,0104  Code Meaning: supine<br>
0054,0414  Patient Gantry Relationship Code Sequence:<br>
0008,0100  Code Value: F-10470<br>
0008,0102  Coding Scheme Designator: 99SDM<br>
0008,0104  Code Meaning: headfirst<br>
0055,0010  —: GEMS_GENIE_1<br>
7FE0,0010  Pixel Data: 46572</p>
<hr>
<p>Title: TOMO_EM_IRACSCRR001_DS.dcm<br>
Width:  565.51 mm (64)<br>
Height:  565.51 mm (64)<br>
Depth:  -565.51 mm (64)<br>
Resolution:  0.113 pixels per mm<br>
ID: -2<br>
Coordinate origin:  0,0,0<br>
Bits per pixel: 16 (signed)<br>
Display range: 0 - 32767<br>
Image: 1/64<br>
No Threshold</p>
<p>Calibration Function: y = a+bx<br>
a: -32768.000000<br>
b: 1.000000<br>
Unit: “gray value”<br>
Path: P:\Prosjekter\Slicer testing\Fantom\Skann 1t (11nov)\TOMO_EM_IRACSCRR001_DS.dcm</p>
<p>No Selection</p>

---

## Post #2 by @ihnorton (2019-01-30 15:56 UTC)

<p>A post was merged into an existing topic: <a href="/t/could-not-load-dicom/5580">Could not load: DICOM</a></p>

---

## Post #3 by @ihnorton (2019-01-30 15:56 UTC)



---
