#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
#mkdir -p dist/dmg
# Empty the dmg folder.
#rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
#cp -r "dist/KindleVocabMate.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/KindleVocabMate.dmg" && rm "dist/KindleVocabMate.dmg"
create-dmg \
  --volname "Kindle VocabMate" \
  --volicon "kindle_vocab_mate.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "KindleVocabMate.app" 175 120 \
  --hide-extension "KindleVocabMate.app" \
  --app-drop-link 425 120 \
  "dist/KindleVocabMate.dmg" \
  "dist/dmg/"
