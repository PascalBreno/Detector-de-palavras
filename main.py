import numpy as np 
import matplotlib.pyplot as plt 
import soundfile as sf
from pydub import AudioSegment
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import librosa
import os
import IPython.display as ipd
from pathlib import Path

a = os.listdir('Songs_train')

for train_path in a:
        i =0
        b = os.listdir('Songs_train'+'\\'+train_path)
        for dir_path in b:
                c = os.listdir('Songs_train'+'\\'+train_path+"\\"+dir_path)        
                for file_path in c:
                        i=i+1
                        sound = AudioSegment.from_ogg('Songs_train'+'\\'+train_path+"\\"+dir_path+'\\'+file_path)
                        sound.export("audioconvertido.wav", format="wav")
                        wav, sr = librosa.load("audioconvertido.wav", sr=None)
                        print(wav.shape, wav.max(), wav.min())
                        ipd.Audio(wav, rate=sr)
                        log_spect = np.log(get_spectrogram(wav))
                        plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')
                        plt.imshow(log_spect, aspect='auto', origin='hight')
                        plt.savefig("train\\"+train_path+"\\"+train_path+str(i)+dir_path+".png", dpi=1000, bbox_inches='tight')
          
def get_spectrogram(wav):
    D = librosa.stft(wav, n_fft=1080, hop_length=160,win_length=1080, window='hamming')
    spect, phase = librosa.magphase(D)
    return spect

