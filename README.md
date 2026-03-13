# 🚀 AutoApply

**AutoApply** ist eine Django-Webanwendung, die den Bewerbungsprozess teilweise automatisieren soll.  
Das Projekt dient als **Portfolio-Projekt** und konzentriert sich auf eine saubere Architektur, modulare Django-Apps und eine solide Grundlage für zukünftige Automatisierungsfunktionen.

Langfristig soll die Anwendung es ermöglichen, Bewerbungen effizienter zu verwalten, PDFs automatisch zu generieren und E-Mail-Kommunikation zu verfolgen.

---

# 🎯 Projektziel

AutoApply soll den Bewerbungsprozess vereinfachen, indem folgende Funktionen bereitgestellt werden:

- 📄 Generieren von Bewerbungs-PDFs aus Vorlagen
- 🔄 Automatisches Ersetzen von Platzhaltern in Dokumenten
- 📬 Tracking von gesendeten und empfangenen Bewerbungs-Mails
- 📊 Übersicht über Bewerbungsaktivitäten
- 📡 Integration externer Mailkonten über SMTP und IMAP

Die Anwendung wird **kein eigener Mailserver**, sondern nutzt **bestehende Mailanbieter** (z.B. Gmail, Outlook, GMX etc.).

---

# ✅ Aktueller Funktionsstand

Der aktuelle Stand des Projekts bildet die **technische Grundlage der Anwendung**.

## 🔐 Authentifizierungssystem

- Custom Django User Model
- Benutzerregistrierung
- Login / Logout
- Automatisches Einloggen nach Registrierung
- Geschützte Seiten über `login_required`

---

## 🏠 Dashboard

Nach dem Login gelangen Nutzer auf ein persönliches Dashboard.

Das Dashboard enthält aktuell:

- 👤 Begrüßung mit Username
- 📬 Platzhalter für einen zukünftigen **Mail Tracker**
- 📄 Bereich für den **PDF Generator**

---

## 📄 PDF-Bereich (Vorbereitung)

Der PDF-Bereich ist aktuell vorbereitet, die Kernfunktion folgt später.

Geplanter Workflow:

1. Upload einer Bewerbungs-PDF
2. Erkennen von Platzhaltern im Dokument
3. Automatisches Ersetzen der Platzhalter
4. Export der fertigen Bewerbungs-PDF

Beispiel für aktuell definierte Platzhalter:

```
<Date>
<Company>
<Street>
<Postal_Code>
<City>
<Contact_Name>
<Contact_Email>
```

Diese Tokens sollen später automatisch ersetzt werden.

---

# 🔮 Geplante Features

## 📄 PDF-Verarbeitung

- Upload von PDF-Vorlagen
- Analyse von Platzhaltern
- Dynamisches Ersetzen von Daten
- Generierung fertiger Bewerbungsdokumente

---

## 📬 Mail Tracker

- Übersicht gesendeter E-Mails
- Übersicht empfangener Antworten
- Verknüpfung externer Mailkonten
- Historie von Bewerbungs-Kommunikation

---

## 📡 Mail Integration

Das System ist vorbereitet für externe Mailkonten.

Geplante Felder im User-Modell:

- SMTP Host
- SMTP Port
- SMTP Username
- SMTP Passwort
- IMAP Host
- IMAP Port
- IMAP Username
- IMAP Passwort

Damit kann AutoApply später mit echten Maildiensten kommunizieren.

---

# 🏗 Projektstruktur

Das Projekt ist modular aufgebaut.

```
AutoApply/
│
├── accounts/        # Authentifizierung und Custom User Model
├── pdfs/            # PDF-Generierung und Verarbeitung (in Entwicklung)
│
├── templates/       # HTML Templates
├── static/          # CSS und statische Dateien
│
├── AutoApply/       # Django Projektkonfiguration
│
└── manage.py
```

Diese Struktur erlaubt eine saubere Trennung der Features und erleichtert spätere Erweiterungen.

---

# 🧰 Technologie-Stack

- 🐍 Python
- 🌐 Django
- 🎨 HTML / CSS
- 🗄 SQLite (Development)

Mögliche zukünftige Erweiterungen:

- PDF Processing Libraries
- Tracking der Bewerbung (Absage / Zusage / Termine usw.)
- Kalender in Verbindung mit Tracking (Evtl. Synchro mit bekannten wie Google und co.)

---

# 🚧 Projektstatus

Das Projekt befindet sich aktuell in einer **frühen Entwicklungsphase**.

Bereits implementiert:

- Authentifizierungssystem
- Dashboard
- grundlegende Projektstruktur

In Entwicklung:

- PDF-Verarbeitung
- Mail Tracking
- Automatisierung des Bewerbungsprozesses

---

# 🎓 Zweck des Projekts

Dieses Projekt dient als **Portfolio-Projekt**, um folgende Fähigkeiten zu demonstrieren:

- Persönliches Lernprojekt (wenig und somit erste Erfahrung mit den unten genannten)
- Django Backend-Architektur
- modulare Projektstruktur
- Authentifizierungssysteme
- Vorbereitung komplexer Webanwendungen
- Erweiterbare Softwarearchitektur

---

# 👨‍💻 Autor
Mario-Angelo - Entwickelt als persönliches Portfolio-Projekt.