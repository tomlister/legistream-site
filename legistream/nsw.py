from legistream_backend.nsw import Stream as nswStream

nsw_stream = nswStream()

nsw_urls = []

if(nsw_stream.lower_is_live):
    nsw_urls.append({'url': nsw_stream.lower_stream_url, 'title': 'Legislative Assembly', 'safe': 'legislative-assembly-vid'})
if(nsw_stream.upper_is_live):
    nsw_urls.append({'url': nsw_stream.upper_stream_url, 'title': 'Legislative Council', 'safe': 'legislative-council-vid'})
if(nsw_stream.committee_is_live):
    nsw_urls.append({'url': nsw_stream.committe_stream_url, 'title': 'Committee', 'safe': 'com-vid'})
if(nsw_stream.jubilee_is_live):
    nsw_urls.append({'url': nsw_stream.jubilee_stream_url, 'title': 'Jubilee', 'safe': 'jubilee-vid'})

parl_title = 'New South Wales'