# Problems with openning TIFF by loading .log document on SkyScanReconImport module

**Topic ID**: 26898
**Date**: 2022-12-23
**URL**: https://discourse.slicer.org/t/problems-with-openning-tiff-by-loading-log-document-on-skyscanreconimport-module/26898

---

## Post #1 by @Nuria_Gallego_Fndz (2022-12-23 13:14 UTC)

<p>Hi everyone! I’m trying to open a .log document on SkyScanReconImport module but when I try it it doesn’t work. On the python console appear some annotations (photo attached) but I don’t understand what does it mean.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00bb285c0885bfb327c3941ecb88206f057ebe61.png" data-download-href="/uploads/short-url/6sYYhJ51LsLXKs8iHSvEp6Cevn.png?dl=1" title="Captura de pantalla 2022-12-23 a las 12.34.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00bb285c0885bfb327c3941ecb88206f057ebe61_2_690x430.png" alt="Captura de pantalla 2022-12-23 a las 12.34.58" data-base62-sha1="6sYYhJ51LsLXKs8iHSvEp6Cevn" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00bb285c0885bfb327c3941ecb88206f057ebe61_2_690x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00bb285c0885bfb327c3941ecb88206f057ebe61_2_1035x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00bb285c0885bfb327c3941ecb88206f057ebe61_2_1380x860.png 2x" data-dominant-color="2D2A2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2022-12-23 a las 12.34.58</span><span class="informations">1440×899 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If anyone knows where is the problem and can help me I will be so grateful!!!</p>

---

## Post #2 by @muratmaga (2022-12-23 18:51 UTC)

<p>It is possible that the log format has changed since we implemented this function. Can you share your *rec.log file and the tiff stack so that we can try to reproduce this error on our end.</p>
<p>Also next time, please tag this question as SlicerMorph as shown below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b82fe95e890749361ef149f1b174ff1abbb3fd3.png" alt="image" data-base62-sha1="fl5K6O0KJo6Ib1rvOnhGcITVx0D" width="293" height="138"></p>

---

## Post #3 by @lassoan (2022-12-24 06:51 UTC)

<p>This is a common error when reading text files with unknown encoding. To fix the error, specify encoding (if you know that the log files contain special characters encoded as utf-8 then use that, otherwise you can use latin1) when you open the file.</p>

---

## Post #4 by @muratmaga (2022-12-24 17:51 UTC)

<p>Is there a way to know this without prior knowledge? Or rather is there an issue trying to read everything with UTF-8 encoding?</p>

---

## Post #5 by @lassoan (2022-12-24 19:02 UTC)

<p>If encoding is not specified by the software developer and not included in the file format then you can only guess.</p>
<p>If you know that the encoding is utf-8 then use that. If you don’t have information then it is safe to use latin1, because not all byte sequences are valid utf-8 but everything is valid latin1. You may also use chardet that tries to guess the most probable encoding.</p>

---

## Post #6 by @muratmaga (2022-12-24 22:53 UTC)

<p>This is the latest version of the log file that I can get my hands onto. There is no format specification I can see of. Application that creates this is windows only. So perhaps UTF-8 will be fine?</p>
<pre><code class="lang-auto">[System]
Scanner=SkyScan1275
Instrument S/N=001
Software Version=1.0.16
Embedded Controller Version=3.5
Home Directory=C:\SkyScan1275
Source Type=Hamamatsu L11871
Camera Type=DEXELA1512
Camera Pixel Size (um)=75.0
Camera X/Y Ratio=1.0000
[User]
User Name=SkyScan
Computer Name=SCAN1275_001
[Acquisition]
Data Directory=D:\Results\kjell\2017-144_embryo Ali\1275_embryo_7um_
Filename Prefix=1275_embryo_7um_~00
Number Of Files=  601
Number Of Rows= 1536
Number Of Columns= 1944
Filename Index Length=8
Partial Width=OFF
Image crop origin X=0
Image crop origin Y=0
Camera binning=1x1
Image Rotation=-0.03800
Optical Axis (line)=  760
Object to Source (mm)=24.755
Camera to Source (mm)=286.0
Source Voltage (kV)=  80
Source Current (uA)= 124
Image Pixel Size (um)=7.000817
Scaled Image Pixel Size (um)=7.000817
Image Format=TIFF
Depth (bits)=16
Reference Intensity=58000
Exposure (ms)=57
Rotation Step (deg)=0.600
Use 360 Rotation=YES
Scanning position=13.965 mm
Frame Averaging=ON (4)
Random Movement=OFF (30)
Flat Field Correction=ON
FF updating interval=120
Filter=Al 1mm
Gantry direction=CC
Rotation Direction=CC
Scanning Start Angle=0.000
Type of Detector Motion=STEP AND SHOOT
Scanning Trajectory=ROUND
Number Of Horizontal Offset Positions=1
Suggested HU - Calibration=180000
Number of connected scans=2
Current scan number=1
Number of lines to be reconstructed=864
Study Date and Time=22 Sep 2017  06h:56m:05s
Scan duration=0h:12m:25s
Maximum vertical TS=5.0
[Reconstruction]
Reconstruction Program=NRecon
Program Version=Version: 1.7.1.2
Program Home Directory=C:\SkyScan1275
Reconstruction engine=GPUReconServer
Engine version=Version: 1.7.1
Reconstruction from batch=No
Postalignment=-1.00
Connected Reconstruction (parts)=2
Sub-scan post alignment [0]=-2.000000
Sub-scan post alignment [1]=-1.000000
Sub-scan scan length [0]=853
Sub-scan scan length [1]=864
Used extra rotation per scan(deg)= 0.000  0.000 
Used extra shift in X per scan(micron)= 0.000  -3.060 
Used extra shift in Y per scan(micron)= 0.000  8.976 
Reconstruction servers= SCAN1275_001 
Dataset Origin=SkyScan1275
Dataset Prefix=1275_embryo_7um_~01
Dataset Directory=D:\Results\kjell\2017-144_embryo Ali\1275_embryo_7um_
Output Directory=D:\Results\kjell\2017-144_embryo Ali\1275_embryo_7um_\1275_embryo_7um_Rec
Time and Date=Sep 22, 2017  07:42:56
First Section=421
Last Section=2050
Reconstruction duration per slice (seconds)=0.381733
Total reconstruction time (854 slices) in seconds=326.000000
Section to Section Step=1
Sections Count=1630
Result File Type=BMP
Result File Header Length (bytes)=1134
Result Image Width (pixels)=1108
Result Image Height (pixels)=876
Pixel Size (um)=7.00082
Reconstruction Angular Range (deg)=360.00
Use 180+=OFF
Angular Step (deg)=0.6000
Smoothing=1
Smoothing kernel=2 (Gaussian)
Ring Artifact Correction=6
Draw Scales=OFF
Object Bigger than FOV=OFF
Reconstruction from ROI=ON
ROI Top (pixels)=1471
ROI Bottom (pixels)=593
ROI Left (pixels)=418
ROI Right (pixels)=1529
ROI reference length=1944
Filter cutoff relative to Nyquist frequency=100
Filter type=0
Filter type description=Hamming (Alpha=0.54)
Undersampling factor=1
Threshold for defect pixel mask (%)=0
Beam Hardening Correction (%)=0
CS Static Rotation (deg)=41.43
Minimum for CS to Image Conversion=0.000000
Maximum for CS to Image Conversion=0.080000
HU Calibration=OFF
BMP LUT=0
Cone-beam Angle Horiz.(deg)=30.740322
Cone-beam Angle Vert.(deg)=24.507914
Automatic matching in Z=50
Automatic matching in X/Y=50
Automatic matching in rotation=5.000000
Automatic fusion=1
[File name convention]
Filename Index Length=8
Filename Prefix=1275_embryo_7um__rec

</code></pre>

---

## Post #7 by @lassoan (2022-12-26 21:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="26898">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>perhaps UTF-8 will be fine?</p>
</blockquote>
</aside>
<p>UTF-8 support in Windows is still fairly new (Windows API support was added a couple of years ago and you still need to specify a manifest to indicate that your application uses UTF-8 and not code pages). So, only use UTF-8 if the manufacturer ID the software explicitly told you that they use UTF-8 or your tests indicate this.</p>
<p>You can test by using non-ASCII characters in the Home directory, Data directory, Output directory, Filename prefix, etc. and see how they get encoded in the log file.</p>
<p>Most likely either the current system code page or some hardcoded code page (e.g. Latin1) is used in the file. I would recommend to assume that the log file uses Latin1 encoding, because the worst that can happen is you get some mojibake in a few lines, which you probably don’t use anyway.</p>

---

## Post #8 by @Nuria_Gallego_Fndz (2023-02-10 08:39 UTC)

<p>How can I make 3Dslicer uses latin1 instead of uft-8 to read the .log file?</p>

---

## Post #9 by @Nuria_Gallego_Fndz (2023-02-10 09:22 UTC)

<p>I was trying to solve it but I can’t. I send you the .log, maybe this way you can see the problem.<br>
Thank you so much!</p>
<pre><code class="lang-auto">[System]
Scanner=SkyScan1278
Instrument S/N=15B14008
Software Version=1.2
Embedded Controller Version=3.5
Home Directory=C:\SkyScan1278
Source Type=RTW MCBM65B-50
Camera Type=DEXELA1512
Camera Pixel Size (um)=75.0
Camera X/Y Ratio=1.0000
[User]
User Name=u0118485
Computer Name=GBW-D-W2599
[Acquisition]
Data Directory=C:\Users\u0118485\Documents\results\Cage 1\pup16_6mU
Filename Prefix=Pup16_6mT_
Number Of Files=  360
Number Of Rows= 1944
Number Of Columns=  860
Filename Index Length=8
Frame Index Length=8
Partial Width= 56%
Image crop origin X=338
Image crop origin Y=0
Camera binning=1x1
Image Rotation=0.01000
Optical Axis (line)=  964
Object to Source (mm)=200.0
Camera to Source (mm)=286.0
Source Voltage (kV)=  54
Source Current (uA)= 701
Image Pixel Size (um)=51.423000
Scaled Image Pixel Size (um)=51.423000
Image Format=TIFF
Depth (bits)=16
Exposure (ms)=80
Rotation Step (deg)=1.000
Use 360 Rotation=YES
Scanning position=72.675 mm
Frame Averaging=ON (2)
Flat Field Correction=ON
Geometrical Correction=ON
Filter=Al 1mm
Gantry direction=CC
Rotation Direction=CC
List mode=OFF (20)
Scanning Start Angle=0
Number Of Horizontal Offset Positions=1
Type of Detector Motion=STEP AND SHOOT
FF updating interval=   60
Scanning Trajectory=ROUND
Number of connected scans=1
Current scan number=1
Number of lines to be reconstructed=0
Study Date and Time=03 Apr 2020  11h:41m:02s
Scan duration=0h:2m:27s
Suggested HU - Calibration=180000
Maximum vertical TS=5.0
[Reconstruction]
Reconstruction Program=NRecon
Program Version=Version: 1.7.3.1
Program Home Directory=C:\Users\labmo\Desktop\Núria\BMD\NReconServerLocal64 (1)
Reconstruction engine=NReconServer
Engine version=Version: 1.7.3
Reconstruction from batch=No
Postalignment Applied=1
Postalignment=0.50
Reconstruction servers= DESKTOP-NK9CDGM 
Reconstruction mode=Standard
Dataset Origin=SkyScan1278
Dataset Prefix=Pup16_6mT_
Dataset Directory=C:\Users\labmo\Desktop\Núria\TFG\6 months CT\Cage 1\pup16_6mU
Output Directory=C:\Users\labmo\Desktop\Núria\TFG\6 months CT\Cage 1\pup16_6mU\pup16_resprec
Time and Date=Nov 21, 2022  09:54:51
First Section=244
Last Section=1150
Reconstruction duration per slice (seconds)=0.041896
Total reconstruction time (907 slices) in seconds=38.000000
Section to Section Step=1
Sections Count=907
Result File Type=TIF
Result File Header Length (bytes)=12
Result Image Width (pixels)=596
Result Image Height (pixels)=476
Pixel Size (um)=51.42300
Reconstruction Angular Range (deg)=360.00
Use 180+=OFF
Angular Step (deg)=1.0000
Smoothing=1
Smoothing kernel=2 (Gaussian)
Ring Artifact Correction=2
Draw Scales=OFF
Object Bigger than FOV=OFF
Reconstruction from ROI=ON_ROUND
ROI Top (pixels)=738
ROI Bottom (pixels)=259
ROI Left (pixels)=129
ROI Right (pixels)=726
ROI reference length=860
Filter cutoff relative to Nyquist frequency=100
Filter type=0
Filter type description=Hamming (Alpha=0.54)
Undersampling factor=1
Threshold for defect pixel mask (%)=0
Beam Hardening Correction (%)=10
CS Static Rotation (deg)=0.00
CS Static Rotation Total(deg)=0.00
Minimum for CS to Image Conversion=-0.003000
Maximum for CS to Image Conversion=0.050000
HU Calibration=OFF
BMP LUT=0
Cone-beam Angle Horiz.(deg)=12.617935
Cone-beam Angle Vert.(deg)=28.063406
[File name convention]
Filename Index Length=8
Filename Prefix=Pup16_6mT__rec
</code></pre>

---

## Post #10 by @smrolfe (2023-02-10 19:46 UTC)

<p><a class="mention" href="/u/nuria_gallego_fndz">@Nuria_Gallego_Fndz</a> I have updated the SkyScanReconImport module with a field to select the log file encoding type. I’m attaching a screenshot below. The updated module can be downloaded from the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/SkyscanReconImport" rel="noopener nofollow ugc">SlicerMorph Repo</a> or will be available to update from the extension manager tomorrow. It’d be great to know if this solves your issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64b486dba492030f39b26c40342413bb0d317b6e.png" data-download-href="/uploads/short-url/emSwtTAAAoEmnp3QB9JA0THvXQi.png?dl=1" title="CaptureRB" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64b486dba492030f39b26c40342413bb0d317b6e_2_690x411.png" alt="CaptureRB" data-base62-sha1="emSwtTAAAoEmnp3QB9JA0THvXQi" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64b486dba492030f39b26c40342413bb0d317b6e_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64b486dba492030f39b26c40342413bb0d317b6e_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64b486dba492030f39b26c40342413bb0d317b6e_2_1380x822.png 2x" data-dominant-color="D7D8E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CaptureRB</span><span class="informations">1809×1078 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @Nuria_Gallego_Fndz (2023-02-13 08:35 UTC)

<p>Thank you so much! Now I can open de .log file without problem.</p>

---
