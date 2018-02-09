from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("english.wav")
mfcc_feat = mfcc(sig,rate)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

print(mfcc_feat.shape)
print(mfcc_feat[1:4,:])
print("\n")

print(d_mfcc_feat.shape)
print(d_mfcc_feat[1:4,:])
print("\n")

print(fbank_feat.shape)
print(fbank_feat[1:4,:])
print("\n")

print(type(fbank_feat))
