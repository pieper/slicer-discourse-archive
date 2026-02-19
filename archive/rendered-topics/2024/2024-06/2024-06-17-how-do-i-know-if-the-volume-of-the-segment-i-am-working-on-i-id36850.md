---
topic_id: 36850
title: "How Do I Know If The Volume Of The Segment I Am Working On I"
date: 2024-06-17
url: https://discourse.slicer.org/t/36850
---

# How do I know if the volume of the segment I am working on is correct?

**Topic ID**: 36850
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/how-do-i-know-if-the-volume-of-the-segment-i-am-working-on-is-correct/36850

---

## Post #1 by @Sol_Aco (2024-06-17 20:34 UTC)

<p><em>(automatically translated using Google translate)</em></p>
<p>To get the volume of a slice, paint some layers and use the fill between slices effect, set the range to 130. Then I clicked Initialize. Again I set the range to 255.00 and clicked Apply.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb.png" data-download-href="/uploads/short-url/1g8xwimP6HIwZcIkydfexqUIeCL.png?dl=1" title="Captura de pantalla 2024-06-17 142345" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_690x345.png" alt="Captura de pantalla 2024-06-17 142345" data-base62-sha1="1g8xwimP6HIwZcIkydfexqUIeCL" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_1380x690.png 2x" data-dominant-color="5D5D6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-06-17 142345</span><span class="informations">1919×960 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<details>
<summary>
Original in Spanish</summary>
<p>Como saber si el volumen del segmento que estoy trabajando esta correcto?</p>
<p>Para obtener el volumen de un segmento, pinte algunas capas y utilice el efecto fill between slices, ajuste el rango en 130. Posteriormente hice click en Initialize. Nuevamente ajuste el rango a 255.00 y hice click en Apply.</p>
</details>

---

## Post #2 by @LeidyMoraV (2024-06-17 21:26 UTC)

<p><em>(automatically translated using Google translate)</em></p>
<p>I don’t understand your question very well, to know if it is correct you could compare it with some previous segmentation made by an expert.</p>
<details>
<summary>
Original in Spanish</summary>
<p>No entiendo muy bien tu pregunta, para saber si es correcto podrias compararlo con alguna segmentacion previa hecha por algun experto.</p>
</details>

---

## Post #3 by @Sol_Aco (2024-06-17 22:05 UTC)

<p><em>(automatically translated using Google translate)</em></p>
<p>I am using confocal microscope images. I need to segment some parts of an ant’s head. For example, the eyes. First, I painted three layers (one at the beginning, when the eyes started to show, one in the middle, where the eyes look bigger, and one at the end, where they look smaller again.</p>
<p>Second, once I have painted three layers, I used the Fill Between slices effect &gt; set the Editable Intensity range to 130.00 &gt; clicked on Initialize &gt; Show 3D. After this, I again adjust the Editable Intensity range to 255.00 and click Apply.</p>
<p>Use these adjustments on the range and I got a pretty nice segment. However, I’m not sure if adjusting the range twice can affect the volume.</p>
<p>That is why my question is: <strong>Using these steps already mentioned, is the volume you obtain viable? That is, can I trust it?</strong> or can it lead to margins of error in the volume calculation. When I talk about volume, I mean the result when I apply Segment Statitics and it gives me a volume in mm3 and cm3.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb.png" data-download-href="/uploads/short-url/1g8xwimP6HIwZcIkydfexqUIeCL.png?dl=1" title="Captura de pantalla 2024-06-17 142345" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_690x345.png" alt="Captura de pantalla 2024-06-17 142345" data-base62-sha1="1g8xwimP6HIwZcIkydfexqUIeCL" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d52c45246287f4871b421dceabf0fcfcfcb4bb_2_1380x690.png 2x" data-dominant-color="5D5D6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-06-17 142345</span><span class="informations">1919×960 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is how the segment looks for me applying the adjustments that I mention in the second paragraph.</p>
<details>
<summary>
Original in Spanish</summary>
<p>Estoy utlizando imagenes de microscopio confocal. Necesito segmentar algunas partes de la cabeza de una hormiga. Por ejemplo, los ojos. Primero, pinte tres capas (una al inicio, cuando empezaban a verse los ojos, una en el medio, donde los ojos se ven mas grandes y una al final, donde se ven mas pequenos nuevamente.</p>
<p>Segundo, una vez he pintando tres capas, utilice el efecto Fill Between slices &gt; ajuste el rango de Editable Intensity range a 130.00 &gt; hice click en Initialize &gt; Show 3D. Posterior a esto, nuevamente ajusto el rango de Editable Intensity range a 255.00 y hago click en Apply.</p>
<p>Utilice estos ajustes en el rango y obtuve un segmento bastante bonito. Sin embargo, no estoy segura si ajustar el rango dos veces pueda afectar el volumen.</p>
<p>Es por ello que mi pregunta es: <strong>Utilizando estos pasos ya mencionados, el volumen que obtenga es viable? Es decir, puedo confiar en ello?</strong> o puede dar lugar a margenes de error en el calculo de volumen. Cuando hablo de volumen, me refiero al resultado de cuando aplico Segment Statitics y me da un volumen en mm3 y cm3.</p>
<hr>
<p>Asi me queda el segmento aplicando los ajustes que menciono en el segundo parrafo.</p>
</details>

---

## Post #4 by @lassoan (2024-06-18 01:33 UTC)

<aside class="quote no-group" data-username="Sol_Aco" data-post="3" data-topic="36850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sol_aco/48/76962_2.png" class="avatar"> Sol_Aco:</div>
<blockquote>
<p>That is why my question is: <strong>Using these steps already mentioned, is the volume you obtain viable? That is, can I trust it?</strong> or can it lead to margins of error in the volume calculation.</p>
</blockquote>
</aside>
<p>You don’t need to worry about accumulating errors by performing multiple editing operations. If the segmentation matches the underlying image then the segmentation is accurate, regardless of how many steps did it take to achieve it.</p>
<aside class="quote no-group" data-username="Sol_Aco" data-post="3" data-topic="36850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sol_aco/48/76962_2.png" class="avatar"> Sol_Aco:</div>
<blockquote>
<p>When I talk about volume, I mean the result when I apply Segment Statitics and it gives me a volume in mm3 and cm3.</p>
</blockquote>
</aside>
<p>If the image is imported correctly then the volume computed from the segmentation will be accurate.</p>
<p>Unfortunately, it is possible to make mistakes during image import, because micro-CT scanner software is often poorly implemented and/or uses proprietary file formats. So, after importing such images, always make sure that the <code>Spacing</code> values shown in <code>Volumes</code> module’s <code>Volume information</code> section are correct. You can check out <a href="https://github.com/SlicerMorph/Tutorials">SlicerMorph tutorials</a> to learn more about this topic.</p>

---
