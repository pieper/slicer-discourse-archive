# How to find the 2 closest concave points of a concave polygon?

**Topic ID**: 25258
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/how-to-find-the-2-closest-concave-points-of-a-concave-polygon/25258

---

## Post #1 by @jumbojing (2022-09-14 12:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999039dbe4a9276d80b7c19e3702bf8d490815ce.png" data-download-href="/uploads/short-url/lUu3sqJA4x72uOCxAjd0HrkcSfk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/999039dbe4a9276d80b7c19e3702bf8d490815ce_2_475x500.png" alt="image" data-base62-sha1="lUu3sqJA4x72uOCxAjd0HrkcSfk" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/999039dbe4a9276d80b7c19e3702bf8d490815ce_2_475x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999039dbe4a9276d80b7c19e3702bf8d490815ce.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999039dbe4a9276d80b7c19e3702bf8d490815ce.png 2x" data-dominant-color="A9ABD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">548×576 56.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How to find the 2 closest concave points of the <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> concave polygon?</p>
<p>pointsArr = np.array([[ 1.9271976e+00,  5.5460022e+01, -1.0658541e+03],<br>
[ 1.7924013e+00,  5.5538818e+01, -1.0669388e+03],<br>
[ 2.1858673e+00,  5.5213562e+01, -1.0623199e+03],<br>
[ 1.4601125e+00,  5.5707939e+01, -1.0692297e+03],<br>
[ 2.0059831e+00,  5.4997200e+01, -1.0588644e+03],<br>
[ 8.9513421e-01,  5.5883709e+01, -1.0714202e+03],<br>
[ 9.8966092e-01,  5.4901222e+01, -1.0565194e+03],<br>
[ 4.8500625e-03,  5.6014091e+01, -1.0726365e+03],<br>
[-3.2594287e-01,  5.4927223e+01, -1.0557750e+03],<br>
[-1.1316023e+00,  5.6141266e+01, -1.0735903e+03],<br>
[-1.6570321e+00,  5.4980713e+01, -1.0554364e+03],<br>
[-2.4740057e+00,  5.6261200e+01, -1.0742552e+03],<br>
[-2.8677700e+00,  5.5085464e+01, -1.0559839e+03],<br>
[-3.6821196e+00,  5.6365063e+01, -1.0747915e+03],<br>
[-3.8956981e+00,  5.5270367e+01, -1.0579122e+03],<br>
[-4.9294081e+00,  5.6470322e+01, -1.0753149e+03],<br>
[-4.7510505e+00,  5.5439716e+01, -1.0597529e+03],<br>
[-6.1751361e+00,  5.6548107e+01, -1.0754209e+03],<br>
[-5.7690206e+00,  5.5625332e+01, -1.0617009e+03],<br>
[-7.4167490e+00,  5.6561523e+01, -1.0745487e+03],<br>
[-6.6816468e+00,  5.5787350e+01, -1.0633801e+03],<br>
[-8.2456007e+00,  5.6491898e+01, -1.0727682e+03],<br>
[-7.4555492e+00,  5.5900158e+01, -1.0644293e+03],<br>
[-9.5117025e+00,  5.6533108e+01, -1.0722987e+03],<br>
[-8.6950483e+00,  5.5933098e+01, -1.0638568e+03],<br>
[-1.0713805e+01,  5.6584663e+01, -1.0720425e+03],<br>
[-9.3179131e+00,  5.5849777e+01, -1.0620460e+03],<br>
[-1.1779905e+01,  5.6563503e+01, -1.0707952e+03],<br>
[-1.0199975e+01,  5.5745140e+01, -1.0596853e+03],<br>
[-1.2771358e+01,  5.6533848e+01, -1.0694832e+03],<br>
[-1.1118530e+01,  5.5704197e+01, -1.0582644e+03],<br>
[-1.3500714e+01,  5.6501316e+01, -1.0683545e+03],<br>
[-1.2302798e+01,  5.5677280e+01, -1.0568269e+03],<br>
[-1.4472707e+01,  5.6398602e+01, -1.0659452e+03],<br>
[-1.3486665e+01,  5.5708134e+01, -1.0562708e+03],<br>
[-1.5076267e+01,  5.6297958e+01, -1.0638871e+03],<br>
[-1.4672162e+01,  5.5814697e+01, -1.0568678e+03],<br>
[-1.5546223e+01,  5.6144699e+01, -1.0611423e+03],<br>
[-1.5542609e+01,  5.6051472e+01, -1.0597238e+03]], )</p>

---

## Post #2 by @jumbojing (2022-09-14 15:23 UTC)

<p>like <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99094e396b2c922e9546c0ea6f0684c2e4405875.png" data-download-href="/uploads/short-url/lPOZnMgIwmF7Xff2NPs6zmYWhhz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99094e396b2c922e9546c0ea6f0684c2e4405875.png" alt="image" data-base62-sha1="lPOZnMgIwmF7Xff2NPs6zmYWhhz" width="600" height="500" data-dominant-color="9597CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">646×538 17.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
