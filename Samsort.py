import re

def samsort(contents):
    contents = contents
    sdict={}
    time_re = re.search('(((10)|(11)|(12)|[0-9])(:[0-5][0-9]) (AM|PM|am|pm))|(((10)|(11)|(12)|[0-9])(:[0-5][0-9])(AM|PM|am|pm))', contents)
    if time_re:
        sdict['time']=time_re.group(0)

    dates_re = re.search('(\d|\d\d)( st| rd| th|st|rd|th)', contents)
    if dates_re:
        sdict['date'] = dates_re.group(0)

    building_re = re.search('([A-Z][A-Z][A-Z]\d\d\d)|([A-Z][A-Z][A-Z] \d\d\d)', contents)
    if building_re:
        sdict['location'] = building_re.group(0)
    return sdict
