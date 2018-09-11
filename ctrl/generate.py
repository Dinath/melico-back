
from subprocess import Popen
import time


"""
    Generates an Android APK, sounds great :)
"""
class Generate:

    # list of users waiting for generation
    queue = []
    # queue = ['alex', 'alexia']

    """
        Start the generate process...abs

        1. lock the list
        2. push the new class
        3. launch npm run
    """
    @staticmethod
    def go(config, json_infos):

        # pushing new item in the queue
        Generate.queue.append(json_infos)

        # waiting for its own glory moment
        while(Generate.queue[0] != json_infos):
            time.sleep(500)

        Generate.make(config, json_infos)

        # quit the queue
        Generate.queue.remove(json_infos)

            
    # make the Android APK...
    @staticmethod
    def make(config, json_infos):
        
        # write config in file
        
        template = """
        export class Authentification {{
            public static WEBSITE_URL: string = '{url}'
            public static WEBSITE_AUTH_USER: string = '{user}'
            public static WEBSITE_AUTH_PASS: string = '{pass}'
        }}
        """
        
        with  open(config.GEN_ANDROID_PATH_CONFIG, 'w') as file:
            file.write(template.format(**json_infos))

        # generate application

        #call('cd ' + config.GEN_ANDROID_PATH + ' && ionic build android --prod --release', shell = True)
        p = subprocess.Popen('/var/www/melico-back/android.sh')
        p.wait()


