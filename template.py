#!/usr/bin/env python3

import os
import re


#
# This file sets a package name for the some android app
#


def apply_replace(src_file, dst_file, template: dict):
    """reads in the src file, applies the replace list and saves the generated file under dst (and creates all dirs)"""
    file = open(src_file, 'r')
    text = file.read()
    file.close()

    for item in template:
        text = re.sub(item, template[item], text)

    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
    file = open(dst_file, 'w')
    file.write(text)
    file.close()


def apply_replace_on_file(file, template: dict):
    apply_replace(file, file, template)


#
# Template
#

# the templates needs a website like structure like de.horsimann.tea for horsimann.de/tea


DOMAIN_NAMESPACE = 'de'
DOMAIN = 'horsimann'
APP = 'Tea'
APP_LOWER = 'tea'

USE_ADMOB = False
USE_BILLING = False


def run_template():
    print('applying template')
    import shutil

    if os.path.exists('out'):
        shutil.rmtree('out')

    print('copying project...')
    shutil.copytree('in', 'out/APP')
    

    print('replacing package names...')
    TEMPLATE = {
        '@@@package_underscored@@@': DOMAIN_NAMESPACE + '_' + DOMAIN + '_' + APP_LOWER,
        '@@@package_dotted@@@': DOMAIN_NAMESPACE + '.' + DOMAIN + '.' + APP_LOWER,
        '@@@package_slashed@@@':  DOMAIN_NAMESPACE + '/' + DOMAIN + '/' + APP_LOWER,
        '@@@app_name@@@': APP
    }
        
    if USE_ADMOB:
        TEMPLATE['//@@@USE_ADMOB@@@'] = ''
        TEMPLATE['#@@@USE_ADMOB@@@'] = ''
        TEMPLATE['<!--@@@USE_ADMOB@@@'] = ''
        TEMPLATE['@@@USE_ADMOB@@@-->'] = ''
        
    if USE_BILLING:
        TEMPLATE['//@@@USE_BILLING@@@'] = ''
        TEMPLATE['#@@@USE_BILLING@@@'] = ''
        TEMPLATE['<!--@@@USE_BILLING@@@'] = ''
        TEMPLATE['@@@USE_BILLING@@@-->'] = ''

    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/mia/Main.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/res/values/strings.xml', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/AndroidManifest.xml', TEMPLATE)
    apply_replace_on_file('out/APP/app/jni/CMakeLists.txt', TEMPLATE)
    apply_replace_on_file('out/APP/app/build.gradle', TEMPLATE)

    print('renaming package dirs...')
    shutil.move('out/APP/app/src/main/java/de/horsimann/mia', 'out/APP/app/src/main/java/de/horsimann/' + APP_LOWER)
    shutil.move('out/APP/app/src/main/java/de/horsimann/', 'out/APP/app/src/main/java/de/' + DOMAIN)
    shutil.move('out/APP/app/src/main/java/de/', 'out/APP/app/src/main/java/' + DOMAIN_NAMESPACE)
    shutil.move('out/APP', 'out/'+APP_LOWER)

    print('finish')

    print('')
    print('~ '*32)
    print('')
    print('Next step is to clone the Mia (+vendor) project into:')
    print('$ cd out/'+APP_LOWER+'/app/jni/ #Mia')
    print('$ git clone --recursive git@github.com:renehorstmann/Mia.git')
    print('And maybe add your apps in there.')
    print('Use the out/'+APP_LOWER+'/app/jni/CMakeLists.txt to setup the C project (cmake config)')
    print('Use the out/'+APP_LOWER+'//app/src/main/AndroidManifest.xml to setup the android project, like enabling mic or webcam')
    print('')
    
    if USE_ADMOB:
        print('AdMob: Replace your ad app id in -> out/'+APP_LOWER+'/app/src/main/AndroidManifest.xml')
        print('AdMob: Replace your ad reward id in -> out/'+APP_LOWER+'/app/src/main/java/'+DOMAIN_NAMESPACE+'/'+DOMAIN+'/'+APP_LOWER+'/SDLActivity.java')
        print('')
    if USE_BILLING:
        print('Billing: Replace your billing product ids in -> out/'+APP_LOWER+'/app/src/main/java/'+DOMAIN_NAMESPACE+'/'+DOMAIN+'/'+APP_LOWER+'/SDLActivity.java')
        print('')
    
    print('You should now be ready to compile your own App in AndroidStudio')

    # checks for anything that's not alphanumeric, underscores, or slashes (file separators)
    if re.search(r'[^\w\-/]', os.getcwd()):
        print('')
        print('WARNING, GENERATED DIRECTORY CONTAINS A SPECIAL CHARACTER OR SPACES!')
        print('  MOVE IT TO ANOTHER LOCATION!')
        print('    pwd is: <' + os.getcwd() + '>')
        print('    windows C:\\android\\\\mia or smth)')

    # wait for user input
    input('')


if __name__ == '__main__':
    import sys
    
    def print_help():
        print('Usage: python3', sys.argv[0], '<DOMAIN_NAMESPACE> <DOMAIN> <APP>'
                                            '[--admob] [--billing]')
        print(' e.g.: python3', sys.argv[0], 'de horsimann Tea')
        exit(1)
    
    args = list(sys.argv[1:])

    if len(args) < 3 or len(args) > 6:
        print_help()

    DOMAIN_NAMESPACE = args[0]
    DOMAIN = args[1]
    APP = args[2]
    APP_LOWER = APP.lower()
    
    if '_' in DOMAIN_NAMESPACE or '_' in DOMAIN or '_' in APP:
        print("package name invalid ( '_' not valid )")
        print_help()
    if ' ' in DOMAIN_NAMESPACE or ' ' in DOMAIN or ' ' in APP:
        print("package name invalid ( ' ' not valid )")
        print_help()
    
    args = args[3:]
    
    if '--admob' in args:
        USE_ADMOB = True
        
    if '--billing' in args:
        USE_BILLING = True

    print('DOMAIN_NAMESPACE =', DOMAIN_NAMESPACE)
    print('DOMAIN =', DOMAIN)
    print('APP =', APP)
    print('APP_LOWER =', APP_LOWER)
    print('--admob =', USE_ADMOB)
    print('--billing =', USE_BILLING)

    run_template()
