# augmented guitar
An Augmented Guitar application that allows us to "see" musical notes and chords being played by an acoustic guitar in real-time.

- Identificação do formato do violão para o desenho das animações das notas musicais
- Biblioteca identificadora de notas musicais

% https://github.com/tensorflow/models/tree/master/research/object_detection/

% https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android

% https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md

% https://patterns.enm.bris.ac.uk/hpa-software-package

Open source chord detection algorithms:

Chordino at http://isophonics.net/nnls-chroma
Chordata at http://clam-project.org/
LabROSA Chord Recognition http://labrosa.ee.columbia.edu/projects/chords/

https://github.com/vadymmarkov/Beethoven

https://musicinformationretrieval.wordpress.com/2017/03/06/state-of-the-art-audio-chord-estimation-algorithms-evaluation/

https://www.codeproject.com/Articles/32172/FFT-Guitar-Tuner

https://stackoverflow.com/questions/1354084/real-time-pitch-detection

https://musicinformationretrieval.wordpress.com/2017/03/05/chosen-audio-chord-estimation-algorithms-explained/

https://musicinformationretrieval.wordpress.com/2017/03/06/state-of-the-art-audio-chord-estimation-algorithms-evaluation/

https://stackoverflow.com/questions/1354084/real-time-pitch-detection?rq=1

Video processing-----\
                      ---------App
Audio processing-----/


			/--tflw_ob_dtc---\
camera image                  ---------\
                                        ----- Visualisation
camera sound                  ---------/
			\--stft----------/


----------------------
I once wrote a utility that does exactly that - it analyses what sounds are being played.

You can look at the code here (or you can download the whole project. its integrated with Frets On Fire, a guitar hero open source clone to create a real guitar hero). It was tested using a guitar, an harmonica and whistles :) The code is ugly, but it works :)

I used pymedia to record, and scipy for the FFT.

Except for the basics that others already noted, I can give you some tips:

If you record from mic, there is a lot of noise. You'll have to use a lot of trial-and-error to set thresholds and sound clean up methods to get it working. One possible solution is to use an electric guitar, and plug its output to the audio-in. This worked best for me.
Specifically, there is a lot of noise around 50Hz. That's not so bad, but its overtones (see below) are at 100 Hz and 150 Hz, and that's close to guitar's G2 and D3.... As I said my solution was to switch to an electric guitar.
There is a tradeoff between speed of detection, and accuracy. The more samples you take, the longer it will take you to detect sounds, but you'll be more accurate detecting the exact pitch. If you really want to make a project out of this, you probably need to use several time scales.
When a tones is played, it has overtones. Sometimes, after a few seconds, the overtones might even be more powerful than the base tone. If you don't deal with this, your program with think it heard E2 for a few seconds, and then E3. To overcome this, I used a list of currently playing sounds, and then as long as this note, or one of its overtones had energy in it, I assumed its the same note being played....
It is specifically hard to detect when someone plays the same note 2 (or more) times in a row, because it's hard to distinguish between that, and random fluctuations of sound level. You'll see in my code that I had to use a constant that had to be configured to match the guitar used (apparently every guitar has its own pattern of power fluctuations).

----------------------------