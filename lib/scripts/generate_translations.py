import argparse
import os
import subprocess
from os.path import abspath, basename, isdir, isfile, join, normpath, splitext
from typing import List

modes = {
    'messages_to_arb': 'm2a',
    'arb_to_messages': 'a2m'
}
parser = argparse.ArgumentParser(description='Script to convert flutter widget localization files to arb format and vice versa')
arg_group = parser.add_mutually_exclusive_group(required=True)
arg_group.add_argument(f"-{modes['messages_to_arb']}", action='store_true', help='Mode in which script converts flutter localization messages to arb files')
arg_group.add_argument(f"-{modes['arb_to_messages']}", action='store_true', help='Mode in which script converts arb files to flutter localization messages')

def get_dir(*args) -> str:
    return join(os.getcwd(), *args)


def execute(package: str,mode: str):
    package_dir = get_dir(package)
    for widget_name in  os.listdir(package_dir):
        if isdir(get_dir(package, widget_name)):
            locales_file = find_locales_file(package, widget_name)
            if locales_file: 
                if mode == modes['messages_to_arb']:
                    generate_message_templates(package, widget_name, locales_file)
                elif mode == modes['arb_to_messages']:
                    generate_messages_from_templates(package, widget_name, locales_file)

def generate_message_templates(package_name: str, widget_name: str, locales_file_name: str):
    generate_translations_proc = subprocess.run(["flutter","pub","run", 
                      "intl_translation:extract_to_arb",
                      "--output-dir", f'lib/{package_name}/{widget_name}/l10n',
                      f"lib/{package_name}/{widget_name}/{locales_file_name}"], shell=True)
    if generate_translations_proc.returncode == 0:
        print('Messages are successfully converted to arb')
    else:
        print(generate_translations_proc.returncode)

def generate_messages_from_templates(package_name: str, widget_name: str, locales_file_name: str):
    translation_files = find_translation_files(package_name, widget_name)
    if len(translation_files) == 0:
        print(f'No translations found for {package_name}/{widget_name}')
        return
    generate_messages_proc = subprocess.run(["flutter", "pub", "run", 
                                            "intl_translation:generate_from_arb",
                                            "--output-dir", f"lib/{package_name}/{widget_name}/l10n",
                                            "--no-use-deferred-loading", 
                                            f"lib/{package_name}/{widget_name}/{locales_file_name}",
                                            *translation_files], shell=True)
    if generate_messages_proc.returncode == 0:
        print('Arb files are successfully converted to Intl messages')
    else:
        print(generate_messages_proc.returncode)

def print_error(return_code):
    print(f'Process unsuccessfully terminated with returncode {return_code}')

def find_translation_files(package: str, widget: str) -> List[str]:
    widgets_l10n_path = get_dir(package, widget, 'l10n')
    if isdir(widgets_l10n_path):
        return [join(widgets_l10n_path, file) for file in os.listdir(widgets_l10n_path) if splitext(file)[-1] == '.arb']

def find_locales_file(package: str, widget_name: str) -> str:
    dirPath = get_dir(package, widget_name)
    for path in os.listdir(dirPath):
        if is_locales_file(path):
            return path

def is_locales_file(path: str) -> bool:
    return  len(path.split('.')) > 2 and path.split('.')[-2] ==  'localizations'

if __name__ == '__main__':
    if basename(normpath(os.getcwd())) != 'lib':
        raise Exception('Script should be executed from the lib folder')
    args = parser.parse_args()
    packages = ['screens', 'shared_widgets']
    for package in packages:
        mode = list(filter(lambda key: vars(args)[key], vars(args).keys()))[0]
        execute(package, 'a2m')
