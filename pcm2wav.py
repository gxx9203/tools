#!/usr/bin/python3
import wave
import os
import argparse
import sys


def pcm2wav(input_file,output_file,channels,rate,width):
    
    f = open(input_file,'rb')
    str_data  = f.read()
    wave_out=wave.open(output_file,'wb')
    wave_out.setnchannels(channels)
    wave_out.setsampwidth(width)
    wave_out.setframerate(rate)
    wave_out.writeframes(str_data)

def main():
    print(sys.argv)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_file",help="input.pcm file");
    parser.add_argument("-o","--output_file",help="outout.wav",default="pcm2wav.wav")
    parser.add_argument("-c","--channels",help="output_channel",default=8)
    parser.add_argument("-r","--rate",help="samplerate",default=48000)
    parser.add_argument("-w","--width",help="bitwidth",default=2)

    args = parser.parse_args()

    print("input file %s" % args.input_file)
    print("output file %s" % args.output_file)
    print("channels %s" % args.channels)
    print("samplerate %s" % args.rate)
    print("bitwidth %s" % args.width)
    
    if args.input_file is None:
        parser.print_help()
        return 

    pcm2wav(args.input_file,args.output_file,args.channels,args.rate,args.width)

if __name__ == '__main__':
    main()
