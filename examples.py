#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from nrkdl import NRK


def example_search():
    nrk = NRK
    search_results = nrk.search('Brannman Sam')
    for search in search_results:
        for season in search.seasons():
            for episode in season.episodes():
                episode.download()
                episode.subtitle()

    print('We found %s episodes to download' % len(nrk.downloads()))

# example_search()


def example_site_rip():
    """ Please, dont do this.. """
    nrk = NRK

    all_programs = nrk.site_rip()

    for media in all_programs:
        if media.type == 'serie':
            for serie in media.episodes():
                #serie.download()
                pass
        else:
            #media.download()
            pass

    #nrk.downloads().start()

example_site_rip()


def example_parse_url():
    # This starts downloading right away

    NRK.parse_urls('https://tv.nrk.no/serie/skam/MYNT15001016/sesong-2/episode-10 http://tv.nrksuper.no/serie/lili/MSUI28008314/sesong-1/episode-3')

# example_parse_url()
