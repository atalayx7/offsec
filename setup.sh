#!/bin/sh
set -eu
umask 077

project_dir="$(CDPATH= cd -- "$(/usr/bin/dirname "$0")" && /bin/pwd -P)"
marker="$project_dir/executed.marker"

if [ -e "$marker" ] || [ -L "$marker" ]; then
  printf '%s\n' "MAC-10: İşaret dosyası zaten var. Temiz bir kopya kullan." >&2
  exit 1
fi

/bin/zsh -f -c '
  set -C
  printf "%s\n" "MAC-10: zsh kurulum adımı çalıştı" > "$1"
' mac10-setup "$marker"

printf 'MAC-10: Kurulum tamamlandı. İşaret dosyası: %s\n' "$marker"
