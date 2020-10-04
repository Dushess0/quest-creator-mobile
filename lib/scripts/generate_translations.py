import os
import subprocess
from os.path import abspath, basename, isdir, isfile, join, normpath, splitext

modes = {
    'messages_to_arb': '-m2a',
    'arb_to_messages': '-a2m'
}

widget_localizations_file_prefix = 'localizations'

def gen_locales(package: str, mode: str):
    path = join(os.getcwd(), package)
    for widget_name in  os.listdir(path):
        widget_folder_path = join(path, widget_name)
        if isdir(widget_folder_path):
            locales_file = find_locales_file(widget_folder_path)
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
        print('Intl messages are successfully generated')
    else:
        print(generate_translations_proc.returncode)


def generate_messages_from_templates(package_name: str, widget_name: str, locales_file_name: str):
    translation_files = find_translation_files(package_name, widget_name)
    generate_messages_proc = subprocess.run(["flutter", "pub", "run", 
                                            "intl_translation:generate_from_arb",
                                            "--output-dir", f"lib/{package_name}/{widget_name}/l10n",
                                            "--no-use-deferred-loading", 
                                            f"lib/{package_name}/{widget_name}/{locales_file_name}",
                                            *translation_files ])
    if generate_messages_proc.returncode == 0:
        print('Translations for locales are generate successfuly')
    else:
        print(generate_messages_proc.returncode)

def print_error(return_code):
    print(f'Process unsuccessfully terminated with returncode {return_code}')

def find_translation_files(package_name, widget_name):
    widgets_l10n_path = join(os.getcwd(), package_name, widget_name, 'l10n')
    if isdir(widgets_l10n_path):
        return [file for file in os.listdir(widgets_l10n_path) if splitext(file)[1] == 'arb']


def find_locales_file(dirPath: str) -> str:
    for path in os.listdir(dirPath):
        if is_locales_file(path):
            return path

def is_locales_file(path: str) -> bool:
    return  len(path.split('.')) > 2 and path.split('.')[-2] == widget_localizations_file_prefix


if __name__ == '__main__':
    if basename(normpath(os.getcwd())) != 'lib':
        raise Exception('Script should be executed from the lib folder')
    packages = ['screens', 'shared_widgets']
    for package in packages:
        gen_locales(package, '-m2a')
    