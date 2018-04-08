#alerts and colors

class clr:
    R = "\033[0;31m"
    W = "\033[0m"
    G = "\033[0;32m"
    B = "\033[0;34m"
    Y = "\033[0;93m"


def alrt(msg="accepted", do="pnd"):
    
    switcher = {
            "pnd":clr.Y, #pending
            "fls":clr.R, #false
            "tru":clr.G  #true
            }

    if do not in switcher:
        do = "fls"
        msg = clr.R+"the attribute does not exist"+clr.W
    
    return "["+switcher.get(do)+"!"+clr.W+"]\t"+msg

