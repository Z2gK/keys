#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Mar  3 21:35:50 2019
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sys

inputfilename = ""
outputfilename = ""

class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10000000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
#        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/rubus/workdir/data/train01/iq.raw', False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, inputfilename, False)


        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
#        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/rubus/workdir/data/train01/iq.raw.filtered', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, outputfilename, False)

        self.blocks_file_sink_0.set_unbuffered(True)
        self.band_reject_filter_1 = filter.fir_filter_ccf(1, firdes.band_reject(
        	1, samp_rate*2/5, 1.16e6, 1.2e6, 10e3, firdes.WIN_HAMMING, 6.76))
        self.band_reject_filter_0 = filter.fir_filter_ccf(1, firdes.band_reject(
        	1, samp_rate*2/5, 340e3, 410e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 5e6, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.band_reject_filter_0, 0), (self.band_reject_filter_1, 0))
        self.connect((self.band_reject_filter_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.band_reject_filter_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_reject_filter_1.set_taps(firdes.band_reject(1, self.samp_rate*2/5, 1.16e6, 1.2e6, 10e3, firdes.WIN_HAMMING, 6.76))
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate*2/5, 340e3, 410e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]
    main()
