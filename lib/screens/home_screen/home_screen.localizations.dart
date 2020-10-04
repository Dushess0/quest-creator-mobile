
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'l10n/messages_all.dart' as messages;

class HomeScreenLocalizations {
  final String _localeName;

  HomeScreenLocalizations(this._localeName);

  static Future<HomeScreenLocalizations> load(Locale locale) {
    final String localeName = Intl.canonicalizedLocale(locale.languageCode);
    return messages.initializeMessages(localeName).then((_) {
      return HomeScreenLocalizations(localeName);
    });
  }

  static HomeScreenLocalizations of(BuildContext context) {
    return Localizations.of<HomeScreenLocalizations>(
        context, HomeScreenLocalizations);
  }
  String get pythonTest {
    return Intl.message(
        'python test message',
        name: 'pythonTest',
        desc: 'Test message to show how localization works in flutter',
        locale: _localeName
    );
  }
  String get exampleMessage {
    return Intl.message(
        'Example localization message',
      name: 'exampleMessage',
      desc: 'Test message to show how localization works in flutter',
      locale: _localeName
    );
  }
}

class HomeScreenLocalizationsDelegate extends LocalizationsDelegate<HomeScreenLocalizations> {
  // const constructors: https://stackoverflow.com/a/21746692/7516134
  // In some case it is a more advance singleton
  final Iterable<Locale> supportedLocales;
  const HomeScreenLocalizationsDelegate(this.supportedLocales);

  @override
  bool isSupported(Locale locale) => supportedLocales.contains(locale);

  @override
  Future<HomeScreenLocalizations> load(Locale locale) => HomeScreenLocalizations.load(locale);

  // https://api.flutter.dev/flutter/widgets/LocalizationsDelegate/shouldReload.html
  @override
  bool shouldReload(LocalizationsDelegate<HomeScreenLocalizations> old) => false;

}