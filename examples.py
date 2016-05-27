#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from nrkdl import NRK


def example_search():
    nrk = NRK()
    search_results = nrk.search('Brannman Sam')
    for search in search_results:
        for season in search.seasons():
            for episode in season.episodes():
                episode.download()
                episode.subtitle()

    print('We found {0!s} episodes to download'.format(len(nrk.downloads())))

# example_search()


def example_site_rip():
    """ Please, dont do this.. """
    nrk = NRK()

    all_programs = nrk.programs()
    print('We found {0!s}'.format(len(all_programs)))

    would_have_downloaded = 0
    for program in all_programs:
        print('So far {0!s}'.format(would_have_downloaded))
        if program.type == 'program':
            would_have_downloaded += 1
            # program.download()
        elif program.type == 'serie':
            would_have_downloaded += len(program.episodes())
            # for e in program.episodes():
            #    e.download() #

    # Start downloading stuff
    nrk.downloads().start()

    print('If we where to download everything we would download {0!s}'.format(would_have_downloaded))
    # 15882.

# example_site_rip()


def example_parse_url():
    # This starts downloading right away
    nrk = NRK()
    nrk.parse_urls('https://tv.nrk.no/serie/skam/MYNT15001016/sesong-2/episode-10 http://tv.nrksuper.no/serie/lili/MSUI28008314/sesong-1/episode-3')

# example_parse_url()
