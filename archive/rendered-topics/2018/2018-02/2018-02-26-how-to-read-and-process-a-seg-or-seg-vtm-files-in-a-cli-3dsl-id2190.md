# How to read and process a '.seg' or '.seg.vtm' files in a CLI 3DSlicer module

**Topic ID**: 2190
**Date**: 2018-02-26
**URL**: https://discourse.slicer.org/t/how-to-read-and-process-a-seg-or-seg-vtm-files-in-a-cli-3dslicer-module/2190

---

## Post #1 by @MachadoL (2018-02-26 21:15 UTC)

<p>Hello Friends!!!</p>
<p>i need to load and process image files generated for a RT planning. Among those files, there is this  ‘.seg’ or ‘.seg.vtm’ files which I would like to read and treat like a label map.</p>
<p>Can anyone here give me a hint on it?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2018-02-26 22:40 UTC)

<p>CLI modules currently only use non-overlapping labelmaps as input/output. If you have time and some C++ programming experience then it would not be too difficult to add it (we can help you to get started). If not, then you can export the segmentation node to a labelmap node using Segmentations module Import/Export section.</p>

---

## Post #3 by @MachadoL (2018-02-27 12:05 UTC)

<p>Hey Dr. Lasso,</p>
<p>I do have some time and a bit of c++ experience. Would like learn how to read and process this… how can I get started?</p>
<p>I’ll also try the segmentation module functions…</p>
<p>Thanks a lot.</p>

---

## Post #4 by @lassoan (2018-02-27 15:16 UTC)

<p>Great! The first step is to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build Slicer</a>. Then, you have to improve <a href="https://github.com/Slicer/Slicer/blob/ac8c769012bf6dc3253ea1ead778cea6bc2c77d8/Base/QTCLI/vtkSlicerCLIModuleLogic.cxx#L822">vtkSlicerCLIModuleLogic::ApplyTask</a> method so that when the input is a vtkMRMLSegmentationNode it can write it to a file.</p>

---

## Post #5 by @MachadoL (2018-02-27 20:49 UTC)

<p>Dr. Lasso,</p>
<p>Is there any loss or limitation in the Export/Import function of the Segmentations module?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2018-02-27 21:15 UTC)

<p>There is no information loss during export. You only lose information if you convert between different representations (closed surface &lt;-&gt; binary labelmap; overlapping segments stored in a 4D volume -&gt; single 3D labelmap containing all segments).</p>
<p>First, I would recommend to make Segmentation nodes show up in <code>image type="label"</code> elements. If user selects a segmentation node then we would export the segmentation to a merged labelmap. Later, we can add support for overlapping labels, by introducing a new <code>type="overlapping-label"</code>, in which case we would write the segmentation to file as a 4D volume.</p>
<p>We could also make Segmentation nodes show up for <code>geometry type="model"</code> elements, as Segmentation nodes can also be saved as surface models.</p>

---

## Post #7 by @brhoom (2018-02-27 22:56 UTC)

<p>I am not a slicer expert but it is just an idea:</p>
<p>if we save more than one color information in the same voxel value, then we can use a 3D volume instead of 4 D e.g. by storing each color value in specific bits, we will have short range of colors but this should be OK as usually we don’t have too many segmentations parts in one image.</p>

---

## Post #8 by @lassoan (2018-02-27 23:01 UTC)

<p>Yes, that’s the first step I’m proposing. You can get a “merged labelmap” from the segmentation, which is a single 3D volume, just like those that are stored in labelmap volume nodes.</p>

---

## Post #9 by @MachadoL (2018-02-28 17:19 UTC)

<p>Thank you, guys. Those information are new to me. I’ll try to read a little and check what is the best way to use it.</p>
<p>Right now, my aim is to use the segmentation areas delimited in an RT planning (.seg file) as a CT image ROI in a numerical analysis.</p>
<p>Thanks again.</p>
<p><strong>Leonardo Machado</strong><br>
Mestre e Doutorando em Física Aplicada a Medicina e Biologia</p>
<p>Laboratório de Computação em Sinais e Imagens Médicas - CSIM</p>
<p>Faculdade de Filosofia, Ciencias e Letras de Ribeirão Preto</p>
<p>Universidade de São Paulo</p>
<p>Cel +55 16 99458 4435</p>
<p>Tel +55 16 3315 0376</p>
<p>leonardomachado@usp.br</p>
<p><a href="mailto:leodemachado@gmail.com">leodemachado@gmail.com</a></p>
<p><em>“Entrega o teu destino a Deus, confia nEle, e com certeza Ele agirá.”</em></p>
<p><strong><em>Sl 36(37), 5.</em></strong></p>

---

## Post #10 by @lassoan (2018-02-28 18:05 UTC)

<p>Note that you can do numerical analysis very efficiently in Python. If you use Python, then you don’t need to implement sending of Segmentation node to CLI modules. You can get a segmentation as numpy array by calling <code>slicer.util.arrayFromSegment(segmentationNode, segmentId)</code>.</p>

---
