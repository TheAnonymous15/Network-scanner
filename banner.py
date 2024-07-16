import random

header1 = r"""
 .----------------.  .-----------------. .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. |
| |      __      | || | ____  _____  | || |     ____     | || | ____  _____  | || |  ____  ____  | || | ____    ____ | || |     ____     | || | _____  _____ | || |    _______   | | | |     __       | || |   _    _     | |
| |     /  \     | || ||_   \|_   _| | || |   .'    `.   | || ||_   \|_   _| | || | |_  _||_  _| | || ||_   \  /   _|| || |   .'    `.   | || ||_   _||_   _|| || |   /  ___  |  | | | |    /  |      | || |  | |  | |    | |
| |    / /\ \    | || |     \ | |   | || |  /  .--.  \  | || |  |   \ | |   | || |   \ \  / /   | || |  |   \/   |  | || |  /  .--.  \  | || |  | |    | |  | || |  |  (__ \_|  | | | |    `| |      | || |  | |__| |_   | |
| |   / ____ \   | || |  | |\ \| |   | || |  | |    | |  | || |  | |\ \| |   | || |    \ \/ /    | || |  | |\  /| |  | || |  | |    | |  | || |  | '    ' |  | || |   '.___`-.   | | | |     | |      | || |  |____   _|  | |
| | _/ /    \ \_ | || | _| |_\   |_  | || |  \  `--'  /  | || | _| |_\   |_  | || |    _|  |_    | || | _| |_\/_| |_ | || |  \  `--'  /  | || |   \ `--' /   | || |  |`\____) |  | | | |    _| |_     | || |      _| |_   | |
| ||____|  |____|| || ||_____|\____| | || |   `.____.'   | || ||_____|\____| | || |   |______|   | || ||_____||_____|| || |   `.____.'   | || |    `.__.'    | || |  |_______.'  | | | |   |_____|    | || |     |_____|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | | | |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------' 
"""

header2 = r"""


        __      _____  ___      ______    _____  ___   ___  ___  ___      ___     ______    ____  ____   ________       ____  ___  ___    
        ""\    (\"   \|"  \    /    " \  (\"   \|"  \ |"  \/"  ||"  \    /"  |   /    " \  ("  _||_ " | /"       )     /  " \(: "||_  |   
      /    \   |.\\   \    |  // ____  \ |.\\   \    | \   \  /  \   \  //   |  // ____  \ |   (  ) : |(:   \___/     /__|| ||  (__) :|  
     /' /\  \  |: \.   \\  | /  /    ) :)|: \.   \\  |  \\  \/   /\\  \/.    | /  /    ) :)(:  |  | . ) \___  \          |: | \____  ||   
    //  __'  \ |.  \    \. |(: (____/ // |.  \    \. |  /   /   |: \.        |(: (____/ //  \\ \__/ //   __/  \\        _\  |     _\ '|   
   /   /  \\  \|    \    \ | \        /  |    \    \ | /   /    |.  \    /:  | \        /   /\\ __ //\  /" \   :)      /" \_|\   /" \_|\  
  (___/    \___)\___|\____\)  \"_____/    \___|\____\)|___/     |___|\__/|___|  \\"_____/   (__________)(_______/      (_______) (_______) 
                                                                                                                                          
                                                                                                                                                                       
"""

header3 = r"""


      _   _  _  ___  _  ___   ____  __  ___  _   _ ___   _ _ _  
     /_\ | \| |/ _ \| \| \ \ / /  \/  |/ _ \| | | / __| / | | | 
    / _ \| .` | (_) | .` |\ V /| |\/| | (_) | |_| \__ \ | |_  _|
   /_/ \_\_|\_|\___/|_|\_| |_| |_|  |_|\___/ \___/|___/ |_| |_|       

"""

header4 = r"""

   ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████████████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░         ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
  ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░          ░▒▓█▓▒░▒▓████████▓▒░ 
  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░ 
  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░ 
  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░ 
 
"""
header5 = r"""

                                                                                                         
    ,---.  ,--.  ,--. ,-----. ,--.  ,--.,--.   ,--.,--.   ,--. ,-----. ,--. ,--. ,---.       ,--.  ,---. 
   /  O  \ |  ,'.|  |'  .-.  '|  ,'.|  | \  `.'  / |   `.'   |'  .-.  '|  | |  |'   .-'     /   | /    | 
  |  .-.  ||  |' '  ||  | |  ||  |' '  |  '.    /  |  |'.'|  ||  | |  ||  | |  |`.  `-.     `|  |/  '  | 
  |  | |  ||  | `   |'  '-'  '|  | `   |    |  |   |  |   |  |'  '-'  ''  '-'  '.-'    |     |  |'--|  | 
  `--' `--'`--'  `--' `-----' `--'  `--'    `--'   `--'   `--' `-----'  `-----' `-----'      `--'   `--' 
                                                                                                         
"""
header6 =r"""

                                                                                                                   
    .---.   ___ .-.     .--.    ___ .-.    ___  ___   ___ .-. .-.     .--.    ___  ___      .--.       .--.       ,--.   
   / .-, \ (   )   \   /    \  (   )   \  (   )(   ) (   )   '   \   /    \  (   )(   )   /  _  \     (_  |      /   |   
  (__) ; |  |  .-. .  |  .-. ;  |  .-. .   | |  | |   |  .-.  .-. ; |  .-. ;  | |  | |   . .' `. ;      | |     / .' |   
    .'`  |  | |  | |  | |  | |  | |  | |   | |  | |   | |  | |  | | | |  | |  | |  | |   | '   | |      | |    / / | |   
   / .'| |  | |  | |  | |  | |  | |  | |   | '  | |   | |  | |  | | | |  | |  | |  | |   _\_`.(___)     | |   / /  | |   
  | /  | |  | |  | |  | |  | |  | |  | |   '  `-' |   | |  | |  | | | |  | |  | |  | |  (   ). '.       | |  /  `--' |-. 
  ; |  ; |  | |  | |  | '  | |  | |  | |    `.__. |   | |  | |  | | | '  | |  | |  ; '   | |  `\ |      | |  `-----| |-' 
  ' `-'  |  | |  | |  '  `-' /  | |  | |    ___ | |   | |  | |  | | '  `-' /  ' `-'  /   ; '._,' '      | |        | |   
  `.__.'_. (___)(___)  `.__.'  (___)(___)  (   )' |  (___)(___)(___) `.__.'    '.__.'     '.___.'      (___)      (___)  
                                            ; `-' '                                                                      
                                             .__.'                                                                       


"""

header7 = r"""


   █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗     ██╗██╗  ██╗
  ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔════╝    ███║██║  ██║
  ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║   ██║███████╗    ╚██║███████║
  ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║     ██║╚════██║
  ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║     ██║     ██║
  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝     ╚═╝     ╚═╝
                                                                                                     
"""
header8 = r"""


  ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗     ██████╗ ██╗  ██╗
  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗    ██╔══██╗██║ ██╔╝
  ██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝    ██║  ██║█████╔╝ 
  ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗    ██║  ██║██╔═██╗ 
  ██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║    ██████╔╝██║  ██╗
  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                              
"""
def xe_header():
    headers = [header1, header2, header3, header4, header5, header6, header7, header8]
    return random.choice(headers)


# Example usage:
if __name__ == "__main__":
    print(xe_header())
