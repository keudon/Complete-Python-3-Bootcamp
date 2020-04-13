def cap_text(text):
    '''
    Input : String:
    Output: Capitalized String
    '''
    out_str = text.title()  # replace .capitalize() with .title()
    apos = text.find("'")
    if apos != -1:
        out_str = out_str[:apos+1]+out_str[apos+1].lower()+out_str[apos+2:]
    
    return out_str
