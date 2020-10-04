import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/intl.dart';
import 'package:quest_creator/screens/home_screen/home_screen.dart';
import 'package:quest_creator/screens/home_screen/home_screen.localizations.dart';

void main() {
  runApp(QuestCreator());
}

class QuestCreator extends StatelessWidget {
  static const List<Locale> SupportedLocales = [
    const Locale.fromSubtags(languageCode: 'en'),
    const Locale.fromSubtags(languageCode: 'pl')];
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      locale: SupportedLocales.firstWhere((locale) => locale.languageCode == 'pl'),
      localizationsDelegates: [
        const HomeScreenLocalizationsDelegate(SupportedLocales),
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],  
      supportedLocales: SupportedLocales,
      theme: ThemeData(
        primaryColor: Colors.indigo,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HomePage(),
    );
  }
}
