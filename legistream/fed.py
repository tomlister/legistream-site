from legistream_backend.federal import Stream as fedStream

fed_stream = fedStream()

fed_urls = []

if(fed_stream.lower_is_live):
    fed_urls.append({'url': fed_stream.lower_stream_url, 'title': 'House of Representatives', 'safe': 'hor-vid', 'thumb': 'legistream/img/thumbs/fed_hor.png'})
if(fed_stream.upper_is_live):
    fed_urls.append({'url': fed_stream.upper_stream_url, 'title': 'Senate', 'safe': 'sen-vid', 'thumb': 'legistream/img/thumbs/fed_sen.png'})
if(fed_stream.committee_is_live):
    fed_urls.append({'url': fed_stream.committee_stream_url, 'title': 'Committee', 'safe': 'com-vid', 'thumb': 'legistream/img/thumbs/fed_com.png'})

parl_title = 'Federal'